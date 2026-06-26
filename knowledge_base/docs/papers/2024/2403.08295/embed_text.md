## Introduction

We present Gemma, a family of open models based on Google's Gemini models.

We trained Gemma models on up to 6T tokens of text, using architectures, data, and training recipes inspired by the Gemini model family. Like Gemini, these models achieve strong generalist capabilities in text domains, alongside state-of-the-art understanding and reasoning skills at scale. With this work, we release both pre-trained and fine-tuned checkpoints, as well as an open-source codebase for inference and serving.

Gemma comes in two sizes: a 7 billion parameter model for efficient deployment and development on GPU and TPU, and a 2 billion parameter model for CPU and on-device applications. Each size is designed to address different computational constraints, applications, and developer requirements. At each scale, we release raw, pretrained checkpoints, as well as checkpoints fine-tuned for dialogue, instruction-following, helpfulness, and safety. We thoroughly evaluate the shortcomings of our models on a suite of quantitative and qualitative benchmarks. We believe the release of both pretrained and fine-tuned checkpoints will enable thorough research and investigation into the impact of current instruction-tuning regimes, as well as the development of increasingly safe and responsible model development methodologies.

Gemma advances state-of-the-art performance relative to comparable-scale (and some larger), open models across a wide range of domains including both automated benchmarks and human evaluation. Example domains include question answering, commonsense reasoning, mathematics and science, and coding. See complete details in the Evaluation section.

Figure 1: Language understanding and generation performance of Gemma 7B across different capabilities compared to similarly sized open models. We group together standard academic benchmark evaluations by capability and average the respective scores; see Table 6 for a detailed breakdown of performance.

Like Gemini, Gemma builds on recent work on sequence models and transformers, deep learning methods based on neural networks, and techniques for large-scale training on distributed systems. Gemma also builds on Google's long history of open models and ecosystems, including Word2Vec, the Transformer, BERT, and T5 and T5X.

We believe the responsible release of LLMs is critical for improving the safety of frontier models, for ensuring equitable access to this breakthrough technology, for enabling rigorous evaluation and analysis of current techniques, and for enabling the development of the next wave of innovations. While thorough testing of all Gemma models has been conducted, testing cannot cover all applications and scenarios in which Gemma may be used. With this in mind, all Gemma users should conduct rigorous safety testing specific to their use case before deployment or use. More details on our approach to safety can be found in section Responsible Deployment.

In this technical report, we provide a detailed overview of the model architecture, training infrastructure, and pretraining and fine-tuning recipes for Gemma, followed by thorough evaluations of all checkpoints across a wide-variety of quantitative and qualitative benchmarks, as well as both standard academic benchmarks and human-preference evaluations. We then discuss in detail our approach to safe and responsible deployment. Finally, we outline the broader implications of Gemma, its limitations and advantages.

## Model Architecture

The Gemma model architecture is based on the transformer decoder. The core parameters of the architecture are summarized in Table 1. Models are trained on a context length of 8192 tokens. We also utilize several improvements proposed after the original transformer paper, and list them below: Feedforward hidden dims Table 1: Key model parameters.

Multi-Query Attention. Notably, the 7B model uses multi-head attention while the 2B checkpoints use multi-query attention (with ${num_ kv_ heads} = 1$), based on ablations that showed that multi-query attention works well at small scales.

RoPE Embeddings. Rather than using absolute positional embeddings, we use rotary positional embeddings in each layer; we also share embeddings across our inputs and outputs to reduce model size.

GeGLU Activations. The standard ReLU non-linearity is replaced by the approximated version of the GeGLU activation function.

RMSNorm. We normalize the input of each transformer sub-layer, the attention layer and the feedforward layer, with RMSNorm to stabilize the training.

## Training Infrastructure

We train the Gemma models using TPUv5e; TPUv5e are deployed in pods of 256 chips, configured into a 2D torus of 16 x 16 chips. For the 7B model, we train our model across 16 pods, totaling to 4096 TPUv5e. We pretrain the 2B model across 2 pods, totaling 512 TPUv5e. Within a pod, we use 16-way model sharding and 16-way data replication for the 7B model. For the 2B, we simply use 256-way data replication. The optimizer state is further sharded using techniques similar to ZeRO-3. Beyond a pod, we perform data-replica reduce over the data-center network, using Pathways approach of.

Table 2: Parameter counts for the Gemma models. We inherit from the large Gemini vocabulary (256k entries), that is designed to work on large quantities of languages, hence, the larger embedding parameter counts compared to models that are limited to one or a few languages.

We follow Gemini and we leverage the 'single controller' programming paradigm of Jax and Pathways. This simplifies the development process by enabling a single Python process to orchestrate the entire training run; we also leverage the GSPMD partitioner for the training step computation and the MegaScale XLA compiler.

### Carbon Footprint

We estimate the carbon emissions from pretraining the Gemma models to be $\sim 131$ $tCO_{2}eq$. This value is calculated based on the hourly energy usage reported directly from our TPU datacenters; we also scale this value to account for the additional energy expended to create and maintain the data center, giving us the total energy usage for our training experiments. We convert total energy usage to carbon emissions by joining our hourly energy usage against hourly per-cell carbon emission data reported by our data centers.

In addition, Google data centers are carbon neutral, achieved through a combination of energy efficiency, renewable energy purchases, and carbon offsets. This carbon neutrality applies to our experiments and the machines running them.

## Pretraining

### Training Data

Gemma 2B and 7B are trained on 3T and 6T tokens respectively of primarily-English data from web documents, mathematics, and code. Unlike Gemini, these models are not multimodal, nor are they trained for state-of-the-art performance on multilingual tasks.

We use a subset of the SentencePiece tokenizer of Gemini for compatibility. It splits digits, does not remove extra whitespace, and relies on byte-level encodings for unknown tokens, following the techniques used for both and. The vocabulary size is 256k tokens.

### Filtering

We filter the pre-training dataset to reduce the risk of unwanted or unsafe utterances, and filter out certain personal information or other sensitive data. This includes both heuristics and model-based classifiers to remove harmful or low-quality content. Further, we filter all evaluation sets from our pre-training data mixture, run targeted contamination analyses to check against evaluation set leakage, and reduce the risk of recitation by minimizing proliferation of sensitive outputs.

The final data mixture was determined through a series of ablations on both the 2B and 7B models. Similar to the approach advocated , we stage training to alter the corpus mixture throughout training to increase the weight of relevant, high-quality data towards the end of training.

## Instruction Tuning

We finetune Gemma 2B and 7B with supervised fine-tuning (SFT) on a mix of text-only, English-only synthetic and human-generated prompt-response pairs and reinforcement learning from human feedback (RLHF) with the reward model trained on labelled English-only preference data and the policy based on a set of high-quality prompts. We find that both stages are important for improved performance on downstream automatic evaluations and human preference evaluations of model outputs.

### Supervised Fine-Tuning

We selected our data mixtures for supervised fine-tuning based on LM-based side-by-side evaluations. Given a set of held-out prompts, we generate responses from a test model, generate responses on the same prompts from a baseline model, shuffle these randomly, and ask a larger, high capability model to express a preference between two responses. Different prompt sets are constructed to highlight specific capabilities, such as instruction following, factuality, creativity, and safety. Our LM-based judges employ a number of known strategies, such as chain-of-thought prompting, rubrics and constitutions, to be aligned with human preferences.

### Filtering

When using synthetic data, we run several stages of filtering over it, removing examples that show certain personal information, unsafe or toxic model outputs, mistaken self-identification data, or duplicated examples. Following Gemini, we find that including subsets of data that encourage better in-context attribution, hedging, and refusals to minimize hallucinations improves performance on factuality metrics, without degrading model performance on other metrics.

The final data mixtures and supervised fine-tuning recipe, which includes tuned hyperparameters, were chosen on the basis of improving helpfulness while minimizing model harms related to safety and hallucinations.

### Formatting

Instruction tuned models are trained with a specific formatter that annotates all instruction tuning examples with extra information, both at training and inference time. It has two purposes: 1) indicating roles in a conversation, such as the User role, and 2) delineating turns in a conversation, especially in a multi-turn conversation. Special control tokens are reserved in the tokenizer for this purpose. While it is possible to get coherent generations without the formatter, it will be out-of-distribution for the model, and will very likely produce worse generations.

The relevant formatting control tokens are presented in Table 3, with a dialogue example presented in Table 4.

Start of conversation turn End of conversation turn Table 3: Relevant formatting control tokens used for both SFT and RLHF of Gemma models.

<start_of_turn>user Knock knock.<end_of_turn> <start_of_turn>model Who’s there?<end_of_turn> <start_of_turn>user Gemma.<end_of_turn> <start_of_turn>model Gemma who?<end_of_turn> Table 4: Example dialogue with user and model control tokens.

### Reinforcement Learning from Human Feedback

We further finetuned the supervised fine-tuned model using RLHF. We collected pairs of preferences from human raters and trained a reward function under the Bradley-Terry model, similarly to Gemini. The policy was trained to optimize this reward function using a novel reinforcement learning algorithm. Similar to the SFT phase, and in order to tune hyperparameters and additionally mitigate reward hacking we relied on a high capacity model as an automatic rater and computed side-by-side comparisons against baseline models.

## Evaluation

We evaluate Gemma across a broad range of domains, using both automated benchmarks and human evaluation.

### Human Preference Evaluations

In addition to running standard academic benchmarks on the finetuned models, we sent final release candidates to human evaluation studies to be compared against the Mistral v0.2 7B Instruct model.

On a held-out collection of around 1000 prompts oriented toward asking models to follow instructions across creative writing tasks, coding, and following instructions, Gemma 7B IT has a 61.2% positive win rate and Gemma 2B IT has a 45% win rate over Mistral v0.2 7B Instruct. On a held-out collection of around 400 prompts oriented towards testing basic safety protocols, Gemma 7B IT has a 63.5% win rate, while Gemma 2B IT has a 60.1% win rate. We report the corresponding numbers in Table 5.

Win / Tie / Loss Win / Tie / Loss Table 5: Win rate of Gemma 1.1 IT models versus Mistral 7B v0.2 Instruct with 95% confidence intervals. We report breakdowns of wins, ties, and losses, and we break ties evenly when reporting the final win rate. Gemma 1.0 results can be found in the appendix.

### Automated Benchmarks

Table 6: Academic benchmark results, compared to similarly sized, openly-available models trained on general English text data. † Mistral reports 50.2 on a different split for MBPP and on their split our 7B model achieves 54.5. ∗ evaluations run by us. Note that due to restrictive licensing, we were unable to run evals on LLaMA-2; all values above were previously reported in Touvron et al..

We measure Gemma models' performance on domains including physical reasoning, social reasoning, question answering, coding, mathematics, commonsense reasoning, language modeling, reading comprehension, and more.

Table 7: HuggingFace H6 benchmark. The performance of small models are sensitive to small modifications in prompts and we further validate the quality of our models on an independent implementation of multiple known benchmarks. All evaluations were run by HuggingFace.

For most automated benchmarks we use the same evaluation methodology as in Gemini. Specifically for those where we report performance compared with Mistral, we replicated methodology from the Mistral technical report as closely as possible. These specific benchmarks are: ARC, CommonsenseQA, Big Bench Hard, and AGI Eval (English-only). Due to restrictive licensing, we were unable to run any evaluations on LLaMA-2 and cite only those metrics previously reported.

We compare Gemma 2B and 7B models to several external open-source (OSS) LLMs across a series of academic benchmarks, reported in Table 6 and Table 7.

On MMLU, Gemma 7B outperforms all OSS alternatives at the same or smaller scale; it also outperforms several larger models, including LLaMA2 13B. However, human expert performance is gauged at 89.8% by the benchmark authors; as Gemini Ultra is the first model to exceed this threshold, there is significant room for continued improvements to achieve Gemini and human-level performance.

Gemma models demonstrate particularly strong performance on mathematics and coding benchmarks. On mathematics tasks, which are often used to benchmark the general analytical capabilities of models, Gemma models outperform other models by at least 10 points on GSM8K and the more difficult MATH benchmark. Similarly, they outperform alternate open models by at least 6 points on HumanEval. They even surpass the performance of the code-fine-tuned CodeLLaMA-7B models on MBPP (CodeLLaMA achieves a score of 41.4% where Gemma 7B achieves 44.4%).

Table 8: Safety academic benchmark results of Gemma 1.1 IT models, compared to similarly sized, openly-available models. Evaluations run by us. Note that due to restrictive licensing, we were unable to run evals on LLaMA-2; we do not report previously-published numbers for LLaMA-2 on TruthfulQA, as we use different, non-comparable evaluation set-ups: we use MC2, where LLaMA-2 uses GPT-Judge. Results for Gemma 1.0 IT models can be found in appendix.

### Memorization Evaluations

Recent work has shown that aligned models may be vulnerable to new adversarial attacks that can bypass alignment. These attacks can cause models to diverge, and sometimes regurgitate memorized training data in the process. We focus on discoverable memorization, which serves as a reasonable upper-bound on the memorization of a model and has been the common definition used in several studies.

Figure 2: Comparing average memorization rates across model families. We compare the Gemma pretrained models to PaLM and PaLM 2 models of comparable size and find similarly low rates of memorization.

We test for memorization^11^1Our use of "memorization" relies on the definition of that term found at www.genlaw.org/glossary.html. of the Gemma pretrained models with the same methodology performed in Anil et al.. We sample 10,000 documents from each corpus and use the first 50 tokens as a prompt for the model. We focus mainly on exact memorization, where we classify texts as memorized if the subsequent 50 tokens generated by the model exactly match the ground truth continuation in the text. However, to better capture potential paraphrased memorizations, we include approximate memorization using an 10% edit distance threshold. In Figure 2, we compare the results of our evaluation with the closest sized PaLM and PaLM 2 models.

### Verbatim Memorization

PaLM 2 compared with PaLM by evaluating on a shared subset of their training corpora. However, there is even less overlap between the Gemma pretraining data with the PaLM models, and so using this same methodology, we observe much lower memorization rates (Figure 2 left). Instead, we find that estimating the "total memorization" across the entire pretraining dataset gives a more reliable estimate (Figure 2 right) where we now find the Gemma memorizes training data at a comparable rate to PaLM.

Figure 3: Measuring personal and sensitive data memorization rates. No sensitive data was memorized, hence it is omitted from the figure.

### Personal Data

Perhaps of higher importance is the possibility that personal data might be memorized. As part of making Gemma pre-trained models safe and reliable, we used automated techniques to filter out certain personal information and other sensitive data from training sets.

To identify possible occurrences of personal data, we use Google Cloud Sensitive Data Protection^22^2Available : This tool outputs three severity levels based on many categories of personal data (e.g., names, emails, etc.). We classify the highest severity as "sensitive" and the remaining two as simply "personal". Then, we measure how many memorized outputs contain any sensitive or personal data. As shown in Figure 3, *we observe no cases of memorized sensitive data.* We do find that the model memorizes some data we have classified as potentially "personal" according to the above, though often at a much lower rate. Further, it is important to note that these tools are known to have many false positives (because they only match patterns and do not consider the context), meaning that our results are likely overestimates of the amount of personal data identified.

Figure 4: Comparing exact and approximate memorization.

### Approximate Memorization

In Figure 4, we observe that roughly 50% more data is approximately memorized (note the log scale) and that this is nearly consistent across each of the different subcategories over the dataset.

## Responsible Deployment

In line with previous releases of Google's AI technologies, we follow a structured approach to responsible development and deployment of our models, in order to identify, measure, and manage foreseeable downstream societal impacts. As with our recent Gemini release, these are informed by prior academic literature on language model risks, findings from similar prior exercises conducted across the industry, ongoing engagement with experts internally and externally, and unstructured attempts to discover new model vulnerabilities.

### Benefits

We believe that openness in AI science and technology can bring significant benefits. Open-sourcing is a significant driver of science and innovation, and a responsible practice in most circumstances. But this needs to be balanced against the risk of providing actors with the tools to cause harm now or in the future.

Google has long committed to providing broader access to successful research innovations (GraphCast, Transformer, BERT, T5, Word2Vec), and we believe that releasing Gemma into the AI development ecosystem will enable downstream developers to create a host of beneficial applications, in areas such as science, education and the arts. Our instruction-tuned offerings should encourage a range of developers to leverage Gemma's chat and code capabilities to support their own beneficial applications, while allowing for custom fine-tuning to specialize the model's capabilities for specific use cases. To ensure Gemma supports a wide range of developer needs, we are also releasing two model sizes to optimally support different environments, and have made these models available across a number of platforms (see Kaggle for details). Providing broad access to Gemma in this way should reduce the economic and technical barriers that newer ventures or independent developers face when incorporating these technologies into their workstreams.

As well as serving developers with our instruction-tuned models, we have also provided access to corresponding base pretrained models. By doing so, it is our intention to encourage further AI safety research and community innovation, providing a wider pool of models available to developers to build on various methods of transparency and interpretability research that the community has already benefited .

### Risks

In addition to bringing benefits to the AI development ecosystem, we are aware that malicious uses of LLMs, such as the creation of deepfake imagery, AI-generated disinformation, and illegal and disturbing material can cause harm on both an individual and institutional levels. Providing access to model weights, rather than releasing models behind an API, also raises new challenges for responsible deployment.

First, we cannot prevent bad actors from fine tuning Gemma for malicious intent, despite their use being subject to Terms of Use that prohibit the use of Gemma models in ways that contravene our Gemma Prohibited Use Policy. However, we are cognizant that further work is required to build more robust mitigation strategies against intentional misuse of open models, which Google DeepMind will continue to explore both internally and in collaboration with the AI community.

The second challenge we face is protecting developers and downstream users against the unintended behaviours of open models, including generation of toxic language or perpetuation of discriminatory social harms, model hallucinations and leakage of personally identifiable information. When deploying models behind an API, these risks can be reduced via various filtering methods.

### Mitigations

Without this layer of defense for the Gemma family of models, we have endeavoured to safeguard against these risks by filtering and measuring biases in pre-training data in line with the Gemini approach, assessing safety through standardized AI safety benchmarks, internal red teaming to better understand the risks associated with external use of Gemma, and subjecting the models to rigorous ethics and safety evaluations, the results of which can be seen in 8.

While we've invested significantly in improving the model, we recognize its limitations. To ensure transparency for downstream users, we've published a detailed model card to provide researchers with a more comprehensive understanding of Gemma.

We have also released a Generative AI Responsible Toolkit to support developers to build AI responsibly. This encompasses a series of assets to help developers design and implement responsible AI best practices and keep their users safe.

The relative novelty of releasing open weights models means new uses, and misuses, of these models are still being discovered, which is why Google DeepMind is committed to the continuous research and development of robust mitigation strategies alongside future model development.

### Assessment

Ultimately, given the capabilities of larger systems accessible within the existing ecosystem, we believe the release of Gemma will have a negligible effect on the overall AI risk portfolio. In light of this, and given the utility of these models for research, auditing and downstream product development, we are confident that the benefit of Gemma to the AI community outweighs the risks described.

### Going Forward

As a guiding principle, Google DeepMind strives to adopt assessments and safety mitigations proportionate to the potential risks from our models. Although we are confident that Gemma models will provide a net benefit to the community, our emphasis on safety stems from the irreversible nature of this release. As the harms resulting from open models are not yet well defined, nor does an established evaluation framework for such models exist, we will continue to follow this precedent and take a measured and cautionary approach to open model development. As capabilities advance, we may explore extended testing, staggered releases or alternative access mechanisms to ensure responsible AI development.

As the ecosystem evolves, we urge the wider AI community to move beyond simplistic 'open vs. closed' debates, and avoid either exaggerating or minimising potential harms, as we believe a nuanced, collaborative approach to risks and benefits is essential. At Google DeepMind we're committed to developing high-quality evaluations and invite the community to join us in this effort for a deeper understanding of AI systems.

## Discussion and Conclusion

We present Gemma, an openly available family of generative language models for text and code. Gemma advances the state of the art of openly available language model performance, safety, and responsible development.

In particular, we are confident that Gemma models will provide a net benefit to the community given our extensive safety evaluations and mitigations; however, we acknowledge that this release is irreversible and the harms resulting from open models are not yet well defined, so we continue to adopt assessments and safety mitigations proportionate to the potential risks of these models. In addition, our models outperform competitors on 6 standard safety benchmarks, and in human side-by-side evaluations.

Gemma models improve performance on a broad range of domains including dialogue, reasoning, mathematics, and code generation. Results on MMLU (64.3%) and MBPP (44.4%) demonstrate both the high performance of Gemma, as well as the continued headroom in openly available LLM performance.

Beyond state-of-the-art performance measures on benchmark tasks, we are excited to see what new use-cases arise from the community, and what new capabilities emerge as we advance the field together. We hope that researchers use Gemma to accelerate a broad array of research, and that developers create beneficial new applications, user experiences, and other functionality.

Gemma benefits from many learnings of the Gemini model program including code, data, architecture, instruction tuning, reinforcement learning from human feedback, and evaluations. As discussed in the Gemini technical report, we reiterate a non-exhaustive set of limitations to the use of LLMs. Even with great performance on benchmark tasks, further research is needed to create robust, safe models that reliably perform as intended. Example further research areas include factuality, alignment, complex reasoning, and robustness to adversarial input. As discussed by Gemini, we note the need for more challenging and robust benchmarks.

## Contributions and Acknowledgments

Mihir Sanjay Kale\Pier Giuseppe Sessa Lars Lowe Sjoesund\Alek Andreev$\dagger$\Kathleen Kenealy$\dagger$ ^††^$\dagger$ equal contribution.

Our work is made possible by the dedication and efforts of numerous teams at Google. We would like to acknowledge the support from the following teams: Gemini, Gemini Safety, Gemini Infrastructure, Gemini Evaluation, Google Cloud, Google Research Responsible AI, Kaggle, and Keras.

Special thanks and acknowledgment to Adrian Hutter, Andreas Terzis, Andrei Kulik, Angelos Filos, Anushan Fernando, Aurelien Boffy, Danila Sinopalnikov, Edouard Leurent, Gabriela Surita, Geoffrey Cideron, Jilin Chen, Karthik Raveendran, Kathy Meier-Hellstern, Kehang Han, Kevin Robinson, Kritika Muralidharan, Le Hou, Leonard Berrada, Lev Proleev, Luheng He, Marie Pellat, Mark Sherwood, Matt Hoffman, Matthias Grundmann, Nicola De Cao, Nikola Momchev, Nino Vieillard, Noah Constant, Peter Liu, Piotr Stanczyk, Qiao Zhang, Ruba Haroun, Seliem El-Sayed, Siddhartha Brahma, Tianhe (Kevin) Yu, Tom Le Paine, Yingjie Miao, Yuanzhong Xu, and Yuting Sun.
