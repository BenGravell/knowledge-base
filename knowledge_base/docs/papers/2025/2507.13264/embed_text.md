<!-- arxiv-full-text:v1 {"arxiv_id": "2507.13264", "source": "arxiv-html"} -->

## Introduction

This paper describes Voxtral Mini and Voxtral Small, a pair of multimodal language models trained to understand both speech and text, released with open-weights under an Apache 2.0 license. Voxtral is pretrained on a large-scale corpus of audio and text documents, and subsequently instruction tuned on real and synthetic data. It is capable of responding directly to audio (or text) and answering questions about audio files. With a 32K token context window, Voxtral is capable of processing audio files up to 40 minutes long.

Compared with similarly sized models in the same evaluation setting, we find that Voxtral delivers strong audio reasoning capabilities without sacrificing text-only performance. Its performance is state-of-the-art for speech transcription and translation, outperforming other open-weights and closed models. In speech question-answering (QA) and summarization, it performs comparably with closed models of a similar price class, such as GPT-4o mini \[Hurst et al., 2024\] and Gemini 2.5 Flash \[Comanici et al., 2025\].

During evaluation of Voxtral and other models, we found that the existing ecosystem of speech evaluations lacked breadth and standardization; the majority of previous work focused on evaluation of transcription and translation quality, and less on other understanding tasks. In Section 3.4, we present evaluations that measure a wider range of speech comprehension and reasoning tasks.

Our primary contributions are: Two open-weights audio models with state-of-the-art transcription and multilingual speech understanding for audio durations up to their 32K context window Native function calling support with audio Evaluation benchmarks that measure speech understanding and reasoning The report is structured as follows: First, we outline our modeling choices. Next, we describe methods for pretraining, post-training, and response quality enhancement. Finally, we present benchmark results along with architectural and data ablations.

## Modeling

Voxtral is based on the Transformer architecture \[Vaswani et al., 2017\], consisting of three components: an audio encoder to process speech inputs, an adapter layer to downsample audio embeddings, and a language decoder to reason and generate text outputs. The overall architecture is depicted in Figure 1.

Figure 1: Voxtral Architecture. The audio encoder processes the speech input, attending to 30-second chunks of audio independently. The audio embeddings are concatenated at the output, and downsampled by a factor of 4x in the audio-language adapter. The multimodal LLM decoder auto-regressively predicts text tokens, conditional on the audio and text inputs.

### Audio Encoder

The audio encoder is based on Whisper large-v3 \[Radford et al., 2023\]. A raw audio waveform is first mapped to a log-Mel spectrogram \[Davis and Mermelstein, 1980\] with 128 Mel-bins and 160 hop-length. Within the Whisper encoder, the spectrogram passes through a convolutional stem that downsamples its temporal resolution by a factor of two, after which it is fed into a stack of bidirectional self-attention layers. The resulting audio embeddings have a frame rate of 50 Hz.

Whisper has a fixed receptive field of 30 seconds. To accommodate audio sequences exceeding this duration, we compute the log-Mel spectrogram for the entire audio, but restrict the encoder to independently process each 30 second chunk. The absolute positional encodings are reset for each chunk, and chunks from the same audio are partitioned into a batch axis. Within the encoder's attention layers, this approach is functionally equivalent to chunk-wise attention \[Zhang et al., 2023\], which mitigates the computational overhead for longer audio inputs and enhances length generalization. The embeddings computed from each chunk are concatenated at the output stage, forming a unified representation of the complete audio sequence.

Due to its fixed receptive field, Whisper also pads short audios to 30 seconds. In Section 5.1, we investigate removing this padding requirement to allow continuous audio lengths. However, empirical results demonstrated a decline in performance, even when tuning the encoder to adapt. Consequently, we maintain the practice of padding all audio inputs to the next multiple of 30 seconds.

### Adapter Layer

The high frame-rate of the audio encoder would result in long sequence-lengths through the language decoder. For example, a 30 minute audio at 50Hz has a sequence length of 90k tokens, leading to high memory and slow inference. To circumvent this, we append an additional MLP layer at the audio encoder outputs that is responsible for downsampling the audio embeddings. In Section 5.2, we show a downsampling factor of 4x yields the best trade-off between sequence-length and performance. This results in an effective frame-rate of 12.5Hz, enabling Voxtral to gracefully handle audios up to 40 minutes with a context-length of 32k tokens.

### Language Decoder

We release two variants of Voxtral: Mini and Small. Voxtral Mini is built on top of Ministral 3B \[Mistral AI Team, 2024\], an edge-focused model that delivers competitive performance with a small memory footprint. Voxtral Small leverages the Mistral Small 3.1 24B backbone \[Mistral AI Team, 2025\], giving strong performance across a range of knowledge and reasoning tasks. Table 1 decomposes the number of parameters in each checkpoint based on the sub-components.

Table 1: Parameter Counts. Number of parameters for Voxtral Mini and Small.

## Methodology

We train the model in three phases: pretraining, supervised finetuning, and preference alignment. Each phase is described separately below. Finally, we describe our evaluation protocol for speech understanding tasks.

### Pretraining

The pretraining stage of Voxtral is designed to introduce speech to the language decoder, complementary to the existing modality of text. Given an audio dataset with text transcriptions, we first chunk the audio into short segments together with their corresponding transcription, forming parallel audio-text pairs: $(A_{1},T_{1}),(A_{2},T_{2}),\dots,(A_{N},T_{N})$. The segmentation boundaries are defined by upstream voice activity detection and diarization models. If transcripts are unavailable, we pseudo-label the audio with an ASR model.

Similar to prior works \[Nguyen et al., 2025, Zeng et al., 2024\], we define two patterns that combine audio and text into training samples for the model: audio-to-text repetition and cross-modal continuation.

The audio-to-text repetition pattern is defined as an audio segment $A_{n}$ followed by the corresponding transcription $T_{n}$. A training sample consists of a single audio-text pair $(A_{n},T_{n})$. This formulation mimics speech recognition and is used to explicitly teach the model speech-to-text alignment.

On the other hand, the cross-modal continuation pattern is designed to implicitly align the speech and text modalities through modality-invariant context modeling. Specifically, for each audio segment $A_{n}$, the corresponding text is the proceeding text segment in the sequence $T_{n+1}$. In addition, a training sample is composed by interleaving audio and text for multiple consecutive segments: $(A_{1},T_{2},A_{3},T_{4},\dots,A_{N-1},T_{N})$. This structure resembles tasks like QA or conversation, where the model must maintain discourse continuity across modalities.

Since we use two different data patterns, the proceeding text segment for a given audio segment is ambiguous; both repeat and continuation are valid. To eliminate ambiguity, we introduce two special tokens to specify the expected output: \<repeat\> for repetition and \<next\> for continuation. These tokens are used for pattern indication during training and as part of the prompt during inference to control model behavior.

The two pretraining patterns are shown with their special tokens in Figure 2. Note that we treat each audio-transcription pair as a standalone sequence wrapped with \<bos\>/\<eos\> without previous context.

Figure 2: Pretraining patterns. A single audio-text example (A, T) is first segmented into a set of audio-text pairs {(An, Tn)}n = 1N, based on the timestamps and transcriptions returned by segmentation stage. For the audio-to-text repetition pattern, a given audio An is repeated in the text space Tn. For the cross-modal continuation pattern, each audio An is followed by its subsequent text Tn + 1. The task is signaled to the model by the <repeat> and <next> special tokens respectively.

During pretraining, we balance the two patterns evenly. We demonstrate in Section 5.3 that this balanced approach is essential; the audio-to-text repetition pattern drives transcription performance, while the cross-modal continuation pattern prepares the model for speech understanding tasks that require deeper reasoning and context integration, such as audio-based QA or dialogue. To preserve text capabilities, we also include text pretraining data in the data mixture.

For the first pass over the data mixture, we freeze the audio encoder and language decoder, training only the adapter. We found this warm-up stage beneficial for speech understanding evaluations, whereas speech recognition results are similar with and without warm-up. We also perform one pretraining run on the Mini scale with just the audio-to-text repetition pattern. We call this model Voxtral Mini Transcribe, and compare it to other ASR-only models in Section 4.1.

### Supervised Finetuning

In post-training, our primary objective is to preserve or slightly enhance the transcription capabilities established during pretraining, while simultaneously extending the model's proficiency over a range of speech understanding tasks. We also develop robust instruction-following behavior, irrespective of whether user inputs are in audio or text form.

Our speech understanding data falls into two categories: tasks where audio is provided as context and the assistant responds to text queries, and tasks where the assistant responds directly to audio inputs. Both categories rely significantly on synthetic data.

### Audio Context, Text Query

To create synthetic data for tasks involving audio context paired with text queries, we utilize long-form audio data (segments up to approximately 40 minutes) with corresponding transcripts and language identification metadata. Transcripts are paired with tailored prompts and fed into an LLM (Mistral Large), which then generates question-answer pairs related to the audio content. The prompts explicitly instruct the LLM to frame both questions and answers as though they arise from auditory comprehension rather than text analysis, thereby encouraging natural responses from the downstream audio model. To achieve data diversity and richness, we vary question types, including straightforward factual inquiries, \"needle-in-haystack\" retrieval tasks, and reasoning-intensive problems. Moreover, to minimize repetitive question styles, the LLM generates multiple candidate question-answer pairs per audio segment, from which we sample a single pair for inclusion in the post-training dataset. While we typically ensure that the question-answer pairs match the language of the original audio and transcript, we occasionally instruct Mistral Large to produce pairs in different languages to enable QA for audios in languages the user does not speak.

Additionally, we allocate another portion of the long-form audio data for synthetic summarization and translation data. For translation tasks, we leverage language identification metadata to select a target language different from the original audio language. To mitigate overfitting to a narrow range of user message patterns, we sampled from a large, manually curated set of plausible user requests.

### Audio-Only Input

For scenarios in which the user provides only audio input, we adapt existing text supervised finetuning data, including function calling datasets, by converting text user messages into synthetic audio using a text-to-speech (TTS) model. However, reliance solely on TTS-generated audio leads to poor generalization to genuine human speech, particularly accented voices, manifesting most commonly in erroneous transcription of conversational prompts rather than appropriate continuation. To address this limitation, we extract questions from long-form ASR data that can be adequately answered through general world knowledge, thus requiring no additional audio context. We then isolate audio excerpts containing these questions and generate corresponding text answers using Mistral Large. This process yields datasets consisting of genuine human speech questions paired with text answers.

Speech recognition is a distinctive use case characterized by an unambiguous task, rendering the text prompt redundant. To address this, we introduce a dedicated \"transcribe mode,\" signaled via a new special token. This mode explicitly instructs the model to perform transcription tasks, thereby eliminating the need for a text prompt.

### Preference Alignment

Direct Preference Optimization (DPO) \[Rafailov et al., 2024\] offers a lightweight alternative to full RLHF by learning directly from pairwise preferences. We also adopt its online variant \[Guo et al., 2024\], where for each example, we sample two candidate responses from the current policy with temperature $T{=}0.5$. To rank responses, we take the entire conversation, replace the audio with its transcription, and leverage a text-based reward model. Although the reward model only has access to the audio transcription - rather than the raw audio itself - it is able to capture semantics, style, and factual coherence from this information, attributes that transfer to the generated text response. Our Online DPO implementation utilizes the sampling and reward infrastructure that powered the Magistral \[Mistral-AI et al., 2025\] series.

We apply DPO and Online DPO to both Voxtral Mini and Small, for which we present results in Section 5.4. While both DPO and Online DPO helped improve the response quality, the online variant was more effective.

### Evaluation

In addition to standard benchmarks for speech transcription, translation, and understanding - detailed in Sections A.1 and A.2 - we create our own test sets. These sets build upon existing research and evaluate model attributes that are typically underrepresented, particularly long-context QA.

### Speech-Synthesized Benchmarks

To evaluate spoken-language understanding, prior works take existing text benchmarks and synthesize the text prompt into speech \[Nachmani et al., 2024, Chen et al., 2024\]. We extend these test suites by creating speech-synthesized versions of three established text benchmarks: GSM8K \[Cobbe et al., 2021\], TriviaQA \[Joshi et al., 2017\], and MMLU \[Hendrycks et al., 2020\].

The first step in creating these benchmarks involves filtering to only include prompts that are viable as speech-synthesized inputs, similar to [Fang et al.](#bib.bib10). For every example, we classify it into one of three categories with Mistral Large: Verbalizable: plain wording or simple numerals. No re-write necessary.

Verbalizable with Rewrite: math, code, or symbols, that can be deterministically rewritten into speech-friendly text. For example, digits are converted to spelled-out form, acronyms expanded, markdown removed. The specific prompt used to achieve this is outlined in Appendix A.3.

Non-Verbalizable: text that cannot be naturally spoken, such as tables, figures or lengthy math and code, is discarded.

Once the valid set of examples is established, we synthesize each one individually using a TTS engine. To ensure diversity in speakers, we randomly sample speaker embeddings from a diverse set, trimmed to six-second clips and filtered to only include single-speaker utterances. For each prompt, we sample a speaker embedding from this pool and generate the corresponding audio input using the TTS engine. Since the model output is in the text-space, scoring the generations requires no additional modifications.

We are releasing the synthesized evaluations under a permissive license and encourage their adoption as standard benchmarks for speech understanding.

### Speech Understanding (SU) Benchmark

We develop an internal benchmark that measures the ability of models to answer questions about audios in a helpful manner. The audio files range up to 19 minutes in duration, assessing understanding on moderately long audio contexts. We use an LLM as a judge, which has access to a transcription of the audio, the question, a reference answer, and the proposed answer. The LLM judge returns two complementary metrics: llm_judge_score: a *binary helpfulness indicator*. The score is 1 if the answer is deemed correct and helpful to the user's question, 0 otherwise. grade_llm_judge_score: a *0--5 quality grade*. A score of 0 means the answer is completely wrong, unhelpful, and poorly written; 5 denotes that it is factually correct, well-reasoned, and clearly presented. Intermediate values reflect partial correctness, clarity, and overall usefulness, as instructed in the grading prompt.

During evaluation, we independently judge each answer multiple times to capture sampling variability. The judge prompts are provided in A.4.

## Results

We evaluate Voxtral on a range of speech recognition, translation, speech understanding, speech function calling and text benchmarks. We compare the model to GPT-4o mini Audio (/Transcribe) and Gemini 2.5 Flash, as well as Scribe and Whisper large-v3 on speech recognition tasks.

### Speech Recognition

Figure 3 plots the macro-averaged word error rates (WER) on four benchmarks: English Short-Form, English Long-Form, Mozilla Common Voice 15.1 (MCV) \[Ardila et al., 2020\] and FLEURS \[Conneau et al., 2022\]. We compute the macro-average across tasks for English Short and Long-Form, and languages for MCV and FLEURS.

Voxtral Small achieves state-of-the-art transcription results on English Short-Form and MCV, beating all open and closed-source models. Voxtral Mini Transcribe performs competitively with much larger closed-source models, surpassing GPT-4o mini Transcribe and Gemini 2.5 Flash across all tasks. A full breakdown of English and multilingual word error rates are provided in A.1.

Figure 3: Speech Recognition Benchmarks. Macro-average WER results across tasks. Voxtral Small outperforms all open and closed-source models on English Short-Form and MCV. Voxtral Mini Transcribe beats GPT-4o mini Transcribe and Gemini 2.5 Flash in every task.

### Speech Translation

We evaluate Voxtral on the FLEURS Speech Translation benchmark. We show BLEU scores for a subset of source/target pairs in Figure 4. Voxtral Small achieves state-of-the-art translation scores in every source/target combination.

Figure 4: FLEURS Translation. BLEU scores for source/target language pairs on the FLEURS Translation benchmark. Voxtral Small achieves state-of-the-art for every combination of languages.

### Speech Understanding

We evaluate Voxtral on a range of public Speech QA benchmarks, such as Llama QA \[Nachmani et al., 2024\] and Openbook QA \[Chen et al., 2024\], as well as the speech-synthesized subsets of standard Text Understanding benchmarks. We also evaluate on our in-house speech understanding (SU) benchmark, consisting of in-the-wild audio examples with challenging QA-style prompts. Figure 5 highlights that Voxtral Small performs competitively with closed-source models, beating GPT-4o mini Audio on three of the seven tasks.

Figure 5: Speech Understanding Benchmarks. We report the accuracy across three speech understanding benchmarks and three synthesized speech subsets of text benchmarks. Voxtral Small is competitive with closed-source models, surpassing GPT-4o mini Audio on three of the seven benchmarks.

### Text Benchmarks

Figure 6 compares the performance of Voxtral Mini and Small to the text-only Mistral Small 3.1 model. Voxtral Small maintains performance across text-benchmarks, making it a suitable drop-in replacement for both text and audio tasks.

Figure 6: Text-Only Benchmarks. We report the accuracy across five standard text understanding benchmarks. Voxtral Small performs comparably to Mistral Small 3.1, highlighting its strong text capabilities.

## Analysis

In this Section, we share results and analyses for two architectural ablations, the pretrain pattern format, and improvements from Online DPO.

### To Pad or Not To Pad

Whisper pads short audios to 30-seconds. We investigate whether this padding constraint is necessary during pre-training, under the setting that the encoder weights are trained in order to adapt to the new configuration.

Figure 8 plots a subset of ASR and speech understanding results for models trained with and without padding. Disabling padding incurs almost no penalty on FLEURS English, however there is a 0.5% WER degradation on French. The 3-Shot Accuracy on Llama QA is comparable over the course of training for the two runs. To achieve the best possible speech recognition scores without compromise to speech understanding, we opt to maintain padding in the audio encoder.

Figure 7: Effect of Padding. Word error rate results on FLEURS English (left) and FLEURS French (middle), alongside 3-shot Accuracy on Llama QA (right) for models trained with and without 30-second padding.

### Adapter Downsampling

The baseline audio encoder operates at a frame-rate of 50 Hz. To reduce decoder computation and memory, we insert an MLP adapter layer that downsamples the audio embeddings along the temporal axis. We experiment with target frame-rates of 50, 25, 12.5 and 6.25 Hz, corresponding to downsampling factors of 1x, 2x, 4x and 8x.

Figure 8 plots the WER on FLEURS English and French, as well as 3-Shot Accuracy on Llama QA. For 25 and 12.5 Hz, there is little degradation on ASR benchmarks. However, for 6.25 Hz, there is a penalty of over 1% on FLUERS French. On Llama QA, 12.5 Hz surpasses the 50 Hz baseline, achieving a score 1.5% higher. We hypothesize that at 12.5 Hz, each audio-embedding encodes a similar amount of information as a text-embedding in the language decoder backbone, leading to superior understanding performance. Based on the trade-off between sequence-length, ASR and speech-understanding performance, we select 12.5 Hz as the optimal frame-rate for Voxtral.

Figure 8: Effect of Downsampling. Word error rate results on FLEURS English (left) and FLEURS French (middle), alongside 3-shot Accuracy on Llama QA (right) for various frame-rates, achieved by increasing the downsampling factor by powers of 2.

### Pre-Training Patterns

Recall that we leverage two data patterns during pretraining: audio-to-text repetition and cross-modal continuation. Figure 9 demonstrates how changing the ratio of these two patterns affects ASR and speech understanding. To better understand the underlying capabilities of the cross-modal continuation pattern for ASR, we evaluate it on the 3-Shot version of the FLEURS ASR task, which is more aligned with the multi-turn pattern presented during training.

Including just the audio-to-text repetition pattern results in strong ASR performance, at the expense of nearly zero-performance on Llama QA. Conversely, training on just the cross-modal continuation pattern yields strong Llama QA performance, but a WER of nearly 60% on ASR. Balancing the two tasks with equal ratios achieves ASR and Llama QA performance comparable to the runs with a single pattern. Thus, we sample each pattern with equal probability during pretraining.

Figure 9: Pattern Proportions. Word error rate results on FLEURS English (left) and FLEURS French (middle), alongside 3-shot Accuracy on Llama QA (right) for varying proportions of pretrain patterns.

### DPO and Online DPO

Table 2 shows the LLM Judge and Grade scores on the SU Benchmark for the Voxtral SFT, DPO and Online DPO checkpoints. Each answer is independently judged ten times and we report the mean ± standard deviation.

For both Mini and Small, DPO and Online DPO improve response quality metrics relative to the SFT baselines. Qualitative inspection---including informal "vibe checks"---shows that the Voxtral Mini Online DPO variant delivers crisper grounding, fewer hallucinations, and generally more helpful responses, so we are releasing it as the public Voxtral Mini checkpoint.

For Voxtral Small, we saw substantial gains in response quality score as measured by the Speech Understanding Benchmark, but they are accompanied by a slight regression on the English short-form benchmarks. Hence, the default checkpoint remains the SFT model. We aim to release an Online DPO Voxtral Small model which does not regress on those ASR metrics in the near future.

Voxtral Mini SFT Voxtral Mini Offline DPO Voxtral Mini Online DPO Voxtral Small SFT Voxtral Small Offline DPO Voxtral Small Online DPO GPT-4o mini Audio Table 2: Response Improvements with Online DPO. Response quality on the internal SU benchmark (mean ± SD over ten trials), as well as the macro-average WER on the English short-form test sets. The differences in scores for other tasks were not significant. Hence, we omit them from this table. Note that GPT-4o mini Audio does not support transcription.

## Conclusion

This paper presented Voxtral Mini and Voxtral Small, a pair of open-weights audio chat models. It demonstrated their capabilities in understanding spoken audio and text, both on existing and new benchmarks. Their strengths across a wide array of speech tasks, strong instruction following, and multilingual prowess make them highly versatile for complex multimodal tasks. Both models are released under the Apache 2.0 license.

### Core contributors

Alexander H. Liu, Andy Ehrenberg, Andy Lo, Clément Denoix, Corentin Barreau, Guillaume Lample, Jean-Malo Delignon, Khyathi Raghavi Chandu, Patrick von Platen, Pavankumar Reddy Muddireddy, Sanchit Gandhi, Soham Ghosh, Srijan Mishra, Thomas Foubert

### Contributors

Abhinav Rastogi, Adam Yang, Albert Q. Jiang, Alexandre Sablayrolles, Amélie Héliou, Amélie Martin, Anmol Agarwal, Antoine Roux, Arthur Darcet, Arthur Mensch, Baptiste Bout, Baptiste Rozière, Baudouin De Monicault, Chris Bamford, Christian Wallenwein, Christophe Renaudin, Clémence Lanfranchi, Darius Dabert, Devendra Singh Chaplot, Devon Mizelle, Diego de las Casas, Elliot Chane-Sane, Emilien Fugier, Emma Bou Hanna, Gabrielle Berrada, Gauthier Delerce, Gauthier Guinet, Georgii Novikov, Guillaume Martin, Himanshu Jaju, Jan Ludziejewski, Jason Rute, Jean-Hadrien Chabran, Jessica Chudnovsky, Joachim Studnia, Joep Barmentlo, Jonas Amar, Josselin Somerville Roberts, Julien Denize, Karan Saxena, Karmesh Yadav, Kartik Khandelwal, Kush Jain, Lélio Renard Lavaud, Léonard Blier, Lingxiao Zhao, Louis Martin, Lucile Saulnier, Luyu Gao, Marie Pellat, Mathilde Guillaumin, Mathis Felardos, Matthieu Dinot, Maxime Darrin, Maximilian Augustin, Mickaël Seznec, Neha Gupta, Nikhil Raghuraman, Olivier Duchenne, Patricia Wang, Patryk Saffer, Paul Jacob, Paul Wambergue, Paula Kurylowicz, Philomène Chagniot, Pierre Stock, Pravesh Agrawal, Rémi Delacourt, Romain Sauvestre, Roman Soletskyi, Sagar Vaze, Sandeep Subramanian, Saurabh Garg, Shashwat Dalal, Siddharth Gandhi, Sumukh Aithal, Szymon Antoniak, Teven Le Scao, Thibault Schueller, Thibaut Lavril, Thomas Robert, Thomas Wang, Timothée Lacroix, Tom Bewley, Valeriia Nemychnikova, Victor Paltz, Virgile Richard, Wen-Ding Li, William Marshall, Xuanyu Zhang, Yihan Wan, Yunhao Tang
