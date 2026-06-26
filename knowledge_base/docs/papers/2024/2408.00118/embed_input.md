<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Gemma 2: Improving Open Language Models at a Practical Size

Topics include Transformers, Attention mechanisms, Language models, Gemma 2.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this work, we introduce Gemma 2, a new addition to the Gemma family of lightweight, state-of-the-art open models, ranging in scale from 2 billion to 27 billion parameters. In this new version, we apply several known technical modifications to the Transformer architecture, such as interleaving local-global attentions and group-query attention. We also train the 2B and 9B models with knowledge distillation instead of next token prediction. The resulting models deliver the best performance for their size, and even offer competitive alternatives to models that are 2-3 times bigger. We release all our models to the community.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Large language models (LLMs) have demonstrated strong capabilities in language understanding, generation, and reasoning. Scaling has been key to this recent progress, with many new capabilities only emerging at scale. The newest large models not only reach unprecedented performance on reasoning benchmarks, but they also demonstrate multimodal and multilingual capabilities and even the ability to use context lengths of over 1M tokens.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Small-scale models have also shown a rapid increase in performance, but these gains are largely derived from increasing the length of training. This approach only scales logarithmically with dataset size, and the latest small models require up to 15T tokens to improve the state of the art by less than 1-2%.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Yet, these continued improvements provide evidence that small models are still under-trained. In this work, we explore alternatives to improve small model performance without solely increasing training length. One solution is to improve the quality of information received by the network at each training step by replacing the next token prediction task with a richer objective.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, we focus our efforts on knowledge distillation, which replaces the one-hot vector seen at each token with the distribution of potential next tokens computed from a large model. This approach is often used to reduce the training time of smaller models by giving them richer gradients. In this work, we instead train for large quantities of tokens with distillation in order to simulate training beyond the number of available tokens. Concretely, we use a large language model as a teacher to train small models, namely 2B and 9B models, on a quantity of tokens that is more than 50$\times$ the compute-optimal quantity predicted by the theory. Along with the models trained with distillation, we also release a 27B model trained from scratch for this work.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We also leverage several known modifications of Transformers, namely the interleaving of global and local attention layers from Beltagy et al., and the Grouped-Query Attention (GQA) mechanism of Ainslie et al..

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Overall, Gemma 2 significantly advances state-of-the-art performance relative to comparable-scale open models and are even competitive with some models more than twice their size, across a variety of automated benchmarks and human evaluations. Example domains include question answering, commonsense reasoning, mathematics and science, and coding.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

While thorough testing of our models has been conducted, these tests cannot cover all applications and scenarios in which Gemma 2 may be used. With this in mind, all Gemma 2 users should conduct rigorous safety testing specific to their use case before deployment or use.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this technical report, we provide an overview of models, including the architecture, training, and pre- and post-training recipes for Gemma 2. We also provide detailed evaluations across a wide variety of quantitative and qualitative benchmarks, as well as both standard academic benchmarks and human-preference evaluations. Finally, we discuss our approach to safe and responsible deployment and outline the broader implications of Gemma 2, its limitations, and advantages.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Global att. span Table 1: Overview of the main model parameters and design choices. See the section on model architectures for more details.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

Similar to previous Gemma models, the Gemma 2 models are based on a decoder-only transformer architecture. We summarize the main parameters and architecture choices in Table 1.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

A few architectural elements are similar to the first version of Gemma models; namely, a context length of 8192 tokens, the use of Rotary Position Embeddings (RoPE), and the approximated GeGLU non-linearity. A few elements differ between Gemma 1 and Gemma 2, including using deeper networks. We summarize the key differences below.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

Local Sliding Window and Global Attention. We alternate between a local sliding window attention and global attention in every other layer. The sliding window size of local attention layers is set to 4096 tokens, while the span of the global attention layers is set to 8192 tokens.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

Logit soft-capping. We cap logits in each attention layer and the final layer such that the value of the logits stays between $- \text{soft_cap}$ and $+ \text{soft_cap}$. More specifically, we cap the logits with the following function: We set the soft_cap parameter to $50.0$ for the self-attention layers and to $30.0$ for the final layer.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

Post-norm and pre-norm with RMSNorm. To stabilize training, we use RMSNorm to normalize the input and output of each transformer sub-layer, the attention layer, and the feedforward layer.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

Grouped-Query Attention. We use GQA with $\text{num_groups} = 2$, based on ablations showing increased speed at inference time while maintaining downstream performance.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Pre-training", "weight": 1.0} -->

We provide a brief overview of the parts of our pre-training that differs from Gemma 1.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Training Data", "weight": 1.0} -->

We train Gemma 2 27B on 13 trillion tokens of primarily-English data, the 9B model on 8 trillion tokens, and the 2B on 2 trillion tokens. These tokens come from a variety of data sources, including web documents, code, and science articles. Our models are not multimodal and are not trained specifically for state-of-the-art multilingual capabilities. The final data mixture was determined through ablations similar to the approach in Gemini 1.0.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Training Data", "weight": 1.0} -->

Tokenizer. We use the same tokenizer as Gemma 1 and Gemini: a SentencePiece tokenizer with split digits, preserved whitespace, and byte-level encodings. The resulting vocabulary has 256k entries.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Training Data", "weight": 1.0} -->

Filtering. We use the same data filtering techniques as Gemma 1. Specifically, we filter the pre-training dataset to reduce the risk of unwanted or unsafe utterances, filter out certain personal information or other sensitive data, decontaminate evaluation sets from our pre-training data mixture, and reduce the risk of recitation by minimizing the proliferation of sensitive outputs.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Training Data", "weight": 1.0} -->

#Chips

<!-- chunk {"id": "body-0023", "role": "body", "section": "Knowledge Distillation", "weight": 1.0} -->

Given a large model used as a teacher, we learn smaller models by distilling from the probability given by the teacher of each token $x$ given its context $x_{c}$, i.e., $P_{T}{(\left. x \middle| x_{c} \right.)}$. More precisely, we minimize the negative log-likelihood between the probabilities from the teacher and the student: where $P_{S}$ is the parameterized probability of the student. Note that knowledge distillation was also used in Gemini 1.5.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Compute Infrastructure", "weight": 1.0} -->

We train our models with TPUv4, TPUv5e, and TPUv5p as outlined in Table 3. For the 2B model, we train on a 2x16x16 configuration of TPUv5e, totaling 512 chips, with 512-way data replication and 1-way model sharding. For the 9B model, we train on an 8x16x32 configuration of TPUv4, totaling 4096 chips, with 1024-way data replication and 4-way model sharding. For the 27B model, we train on an 8x24x32 configuration of TPUv5p, totaling 6144 chips, with 768-way data replication and 8-way model sharding.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Compute Infrastructure", "weight": 1.0} -->

The optimizer state is further sharded using techniques similar to ZeRO-3. For scales beyond a single pod, we perform a data-replica reduction over the data center network, using the Pathways approach of Barham et al.. We also use the 'single controller' programming paradigm of Jax and Pathways. As in Gemma 1, we use the GSPMD partitioner for training step computation and the MegaScale XLA compiler.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Compute Infrastructure", "weight": 1.0} -->

Start of conversation turn End of conversation turn Table 4: Relevant formatting control tokens used for Gemma models.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Carbon Footprint", "weight": 1.0} -->

We estimate the carbon emissions from pre-training the Gemma models to be $1247.61$ $tCO_{2}eq$. As in Gemma 1, this value is calculated based on the hourly energy usage reported directly from our TPU data centers and scaled to account for the additional energy expended to create and maintain the data center. Importantly, Google data centers are carbon neutral, achieved through a combination of energy efficiency, renewable energy purchases, and carbon offsets. This carbon neutrality applies to our experiments and the machines running them.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Post-Training", "weight": 1.0} -->

For post-training, we fine-tune our pre-trained models into instruction-tuned models. First, we apply supervised fine-tuning (SFT) on a mix of text-only, English-only synthetic and human-generated prompt-response pairs. We then apply RLHF on top of these models with the reward model trained on labelled English-only preference data and the policy based on the same prompts as the SFT phase. Finally, we average the models obtained after each phase to improve their overall performance. The final data mixtures and post-training recipe, which includes tuned hyperparameters, were chosen on the basis of improving helpfulness while minimizing model harms related to safety and hallucinations.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Post-Training", "weight": 1.0} -->

We extended the post-training data from Gemma 1.1 with a mixture of internal and external public data. In particular, we use the prompts, but not the answers from LMSYS-chat-1M. All of our data go through a filtering stage described below.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Post-Training", "weight": 1.0} -->

Supervised fine-tuning (SFT). We run behavioral cloning on synthetic and real prompts, and responses predominantly synthetically generated by the teacher, that is a larger model. We also run distillation from the teacher on the student's distribution.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Post-Training", "weight": 1.0} -->

<start_of_turn>user Knock knock.<end_of_turn> <start_of_turn>model Who’s there?<end_of_turn><eos> <start_of_turn>user Knock knock.<end_of_turn> <start_of_turn>model Who’s there?<end_of_turn> <start_of_turn>user Gemma.<end_of_turn> <start_of_turn>model Gemma who?<end_of_turn><eos> Table 5: Example dialogue with user and model control tokens. To proceed with multi-turn, remove the model-outputted <eos>, add back the usual user turn’s control tokens and continue with the following turn’s chat template.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Post-Training", "weight": 1.0} -->

Reinforcement Learning from Human Feedback (RLHF). We use a similar RLHF algorithm as Gemma 1.1 but a different reward model, which is an order of magnitude larger than the policy. The new reward model is also oriented more towards conversational capabilities, specifically multi-turn.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Post-Training", "weight": 1.0} -->

Model merging. We average different models obtained by running our pipeline with different hyperparameters.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Post-Training", "weight": 1.0} -->

Data filtering. When using synthetic data, we run several stages of filtering to remove examples that show certain personal information, unsafe or toxic model outputs, mistaken self-identification data, and duplicated examples. Following Gemini, we find that including subsets of data that encourage better in-context attribution, hedging, and refusals to minimize hallucinations improves performance on factuality metrics, without degrading model performance on other metrics.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Post-Training", "weight": 1.0} -->

Formatting. Gemma 2 models are fine-tuned with the same control tokens as Gemma 1 models, as detailed in Table 4, but a different formatting schema. See the dialogue example in Table 5. Notice that the model explicitly ends generations with \<end_of_turn\>\<eos\> tokens, while previously it only generated \<eos\>. For the motivation behind this formatting structure, see Gemma 1.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Ablations", "weight": 1.0} -->

In this section, we focus on the main finding of this work, which is the impact of knowledge distillation on small language models.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Ablations", "weight": 1.0} -->

Distillation versus from scratch. In Table 6, we show that distilling from a larger model improves performance compared to training from scratch. Note that 500B is 10$\times$ more than the compute-optimal number of tokens for a 2B model. We distill from a 7B model to keep a ratio similar to our target distillation from 27B to 9B.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Ablations", "weight": 1.0} -->

Impact of distillation w.r.t. model size. In Table 7, we measure the impact of distillation as model size increases. We observe that the gain remains as the model size is scaled. In this ablation, we maintain the size of the teacher at 7B and train smaller models to simulate the same gap as between our final teacher and student sizes.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Ablations", "weight": 1.0} -->

GQA versus MHA. In Table 8, we compare two instances of our 9B with MHA or GQA. We observe overall few changes in performance between both models as measured on several benchmarks. We choose GQA since it requires fewer parameters and is faster at inference time.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Ablations", "weight": 1.0} -->

Wide versus deep. In Table 9, we show that a deeper 9B network is slightly better than a wider 9B for the same number of parameters. Although the gap is small, it is consistent across benchmarks and warrants the switch to a deeper architecture.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Ablations", "weight": 1.0} -->

Changing sliding window size. In Table 10, we show that we can change the sliding window size of the local attention layers of the models during inference with moderate impact on perplexity. Adjusting the size of the sliding window can thus be a leverage for slight inference speed gain. perplexity (val. set) Table 10: Impact of changing the sliding window size at inference time for the 9B model.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Ablations", "weight": 1.0} -->

Impact of formatting. We measure performance variance on MMLU across prompt/evaluation formatting variations. Table 11 shows the standard deviations of MMLU scores for 12 formatting/evaluation combinations, a proxy for undesired performance variability. The Gemma 2B models are slightly less format-robust than the larger ones. Notably, Mistral 7B is significantly less robust than our models.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Evaluation", "weight": 1.0} -->

In this section, we evaluate both pre-trained and IT models over a series of automated benchmarks and human evaluations across a variety of domains. We also report performance from models of similar sizes that have permissive licenses, or as reported by others. Note that we consider total parameters, not active parameters, since total memory usage is often what limits the use of open models on standard devices.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Evaluating the 27B model", "weight": 1.0} -->

In this set of evaluations, we evaluate the performance of our 27B model trained without distillation on 13T tokens. We report results in Table 12, where we compare with a model of similar size, Qwen1.5 34B, and a model 2.5$\times$ larger, LLaMA-3 70B on the HuggingFace evaluation suite. We selected these models based on their ranking on the HuggingFace leaderboard.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Evaluating the 27B model", "weight": 1.0} -->

Overall, we observe that our model is the best in its size category and is even competitive with a larger model that is trained for longer. That being said, the performance of models trained in a similar fashion improves only logarithmically with their size and hence, our model is likely in the same Pareto curve as the LLaMA-3 models. However, it is not clear how these differences affect the quality of the resulting IT models.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Evaluating the 2B and 9B models", "weight": 1.0} -->

In this set of experiments, we compare our new 2B and 9B trained with distillation to our previous models and several standard open models in Gemma Team.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Evaluating the 2B and 9B models", "weight": 1.0} -->

We observe overall a massive improvement in our models compared to previous versions, by up to 10% in some benchmarks for the 9B model. The two 2B models were trained with a similar number of tokens (2T for Gemma 2 and 3T for Gemma 1) and we still observe a significant improvement for the new models. This confirms that distillation significantly improves the quality of models even when trained on the same number of tokens.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Post-training Evaluations", "weight": 1.0} -->

In this section, we evaluate our IT models on a set of human evaluations as well as standard academic benchmarks. The Gemma 2 models push the frontier for post-trained open-weights models, setting a new state of the art on the LMSYS Chatbot Arena.

<!-- chunk {"id": "body-0049", "role": "body", "section": "LMSYS Chatbot Arena", "weight": 1.0} -->

Gemma 2 Instruction Tuned models were evaluated on the Chatbot Arena in blind side by side evaluations by human raters against other state of the art models. We report Elo scores in Table 14. Gemma 2.6B, 9B and 27B strongly outperform all other open models in the same range of parameters, with notably: Gemma 27B (Elo 1218) ranked higher than Llama 3 70B (Elo 1206), Gemma 9B (Elo 1187) similar as GPT-4-0314 (Elo 1186), Gemma 2.6B (Elo 1126) ranked higher than GPT-3.5-Turbo-0613 (Elo 1116). phi-3-medium-4k-instruct Table 14: Evaluation of Gemma 2 Instruction Tuned models on the Chatbot Arena. The models are evaluated against each other through blind side by side evaluations by human raters. Each model is attributed a score, based on the Elo rating system.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Human Preference Evaluations", "weight": 1.0} -->

We also submit Gemma IT models for side-by-side human evaluation studies (which are independent from the Chatbot Arena). We used held-out collections of single-turn prompts that target safety and instruction following (IF). We use gpt4o-2024-05-13 as the base model, and observe large improvements in win rates and preference scores as compared against the older Gemma 1.1 7B model. We report safety as a win-loss ratio against GPT4o, and we report single-sided instruction following scores as ratio of prompts where all instructions are followed. In particular, we find that regardless of their size, Gemma 2 models produce safer, more appropriate prompts on the held-out safety prompt set than GPT4o.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Human Preference Evaluations", "weight": 1.0} -->

Win / Tie / Loss Win / Tie / Loss Win / Tie / Loss Win / Tie / Loss Table 15: Instruction following and safety metrics from human raters. The instruction following metrics are single-sided and do not have win-loss rates, and so are left blank.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Human Multi-Turn Evaluations", "weight": 1.0} -->

We evaluated the multi-turn capabilities of Gemma 1.1 7B, Gemma 2 2B, 9B and 27B models by tasking human raters to have conversations with the models and follow specified given scenarios. We used a diverse, held-out set of 500 scenarios, each describing a sequence of requests to the model, including measuring instances of brainstorming, making a plan, or learning something new. The average number of user turns is 8.4. We found that the conversations with Gemma 2 models are rated significantly better than Gemma 1.1 in user satisfaction and conversation goal achievement (Table 16). Moreover, we saw that the Gemma 2 models were better than Gemma 1.1 7B at maintaining high quality of responses for the entire conversation.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Human Multi-Turn Evaluations", "weight": 1.0} -->

Conversation goal achievement Table 16: Human evaluations on 500 multi-turn scenarios. The raters attribute a score ranging between 1 and 5 for both overall satisfaction and conversation goal achievement.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Standard Benchmarks", "weight": 1.0} -->

It has been observed in Llama-3 that instruction fine-tuning can improve the performance of the models on few-shot benchmarks despite not being trained to target few-shot capabilities. In Table 17, we show a similar improvement across our models. Overall, we observe improvements on the order of several percentage points. We conjecture that IT models are better at understanding formatted questions, while pre-trained models are sensitive to formatting.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Memorization and Privacy", "weight": 1.0} -->

Large language models may, under particular circumstances, be vulnerable to attacks causing the model to produce memorized^11^1This work uses a very restricted definition of "memorization": whether a model can be induced to generate near-copies of some training examples when prompted with appropriate instructions. We do not mean to say that a model 'contains' its training data in the sense that any arbitrary instance of that data can be retrieved without use of specialized software or algorithms. Rather, if a model can be induced to generate measurably close copies of certain training examples by supplying appropriate instructions to guide the model's statistical generation process then that model is said to have 'memorized' those examples. training data. To study susceptibility to such attacks and quantify memorization, we evaluate models for verbatim and approximate memorization as was done in several prior studies.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Memorization and Privacy", "weight": 1.0} -->

We follow the evaluation setting of which tests for (50 token) memorizations of training data given a prompt of 50 tokens. We compare the overall memorization rates, across a uniform sample of the entire dataset, using both an exact match criteria and approximate match criteria using an edit distance of 10%.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Memorization and Privacy", "weight": 1.0} -->

Verbatim Memorization: Results are in Figure 1. We first compare against recent models from the literature that include memorization evaluations. We find that Gemma 2 memorizes significantly less than prior models at a similar size, with memorization rates below 0.1% (note the log y-axis). We further investigate how this memorization breaks down with respect to the data source. Similar to Gemma 1, we find that Gemma 2 memorizes more from code, wiki, and science sources, and also that it memorizes significantly less across the board (again, note the log y-axis).

<!-- chunk {"id": "body-0058", "role": "body", "section": "Memorization and Privacy", "weight": 1.0} -->

Approximate Memorization: Figure 1 also presents approximate memorization by data source. We observe that while approximate memorization is higher than exact, the rate of memorization is still low. For example, the approximate memorization of this model is much lower than even the exact memorization of Gemma 1. We find that the increase in approximate memorization is much lower than prior models; in some cases we observed no lift at all c.f. (note that no bar indicates no increase, i.e., the rate of approximate memorization equals that of exact memorization). Note that no approximate memorization bar in Figure X indicates no increase, i.e., the rate of approximate memorization equals that of exact memorization.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Memorization and Privacy", "weight": 1.0} -->

Personal Data We use the same prevention methods at training time and the same evaluations as Gemma Team. In particular, we use Google Cloud Sensitive Data Protection Tool^22^2Available: to find potential instances of personal data. The many categories of personal data (e.g., phone numbers, account numbers) are classified into three severity levels. We analyze memorized outputs using these severity levels.. We found no instances of high-severity data being emitted, and found a very low rate of 0.00026% of memorized data to contain lower-severity personal information. We note that these automated tools are known to incur false positives because they do not account for context. This means our results are likely overestimates.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Responsibility, Safety, Security", "weight": 1.0} -->

Responsibility, safety and security are of paramount importance when developing Gemma models. To reduce risks to Gemma 2 users, we have integrated enhanced internal safety processes that span the development workflow, in line with recent Google AI models. Similar to the inaugural Gemma release, we have followed a three pillar approach which focuses on safety mitigation at training time, robust and transparent model evaluations, and further development of the Responsible Generative AI Toolkit, a series of models and tools to help developers implement responsibility and safety best practices for their applications.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Impact assessment", "weight": 1.0} -->

Our approach and resulting impact assessment is reflective of that outlined for Gemma 1: we continue to believe that openness in AI can spread the benefits of these technologies across society, but must be evaluated against the risk of malicious uses, such as the creation of deepfake imagery, AI-generated disinformation or illegal and disturbing material, that can cause harm on both an individual and institutional levels. Since the launch of Gemma 1, we have seen our Gemma models drive a number of socially beneficial applications, relying on Gemma's unique technologies like its tokenizer to facilitate the creation of multilingual models, such as for Navarasa 2.0, a Gemma tuned model for 15 Indian languages.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Impact assessment", "weight": 1.0} -->

Releasing further open models requires specific attention to changes in model capabilities and close monitoring of the evolving risks of LLMs, as well as, an understanding of the ways in which our models are being used in the wild. Although we are yet to receive any reports of malicious use for Gemma, we remain committed to investigating any such reporting, and work with the academic and developer communities, as well as conduct our own monitoring, to flag such use cases via our contact email^33^3gemma-2-report@google.com.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Impact assessment", "weight": 1.0} -->

Despite advancements in capabilities, we believe that given the number of larger and more powerful open models, this release will have a negligible effect on the overall risk landscape.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Safety policies and train-time mitigations", "weight": 1.0} -->

A key pillar of Gemma's approach to safety is to align fine-tuned models with Google's safety policies, in line with Gemini models. They are designed to help prevent our models from generating harmful content, i.e., Child sexual abuse and exploitation Revealing personally identifiable information that can lead to harm (e.g., Social Security numbers) Hate speech and harassment Dangerous or malicious content (including promoting self-harm or instructing in harmful activities) Sexually explicit content Medical advice that runs contrary to scientific or medical consensus We undertook considerable safety filtering of our pre-training data to reduce the likelihood of our pre-trained and fine-tuned checkpoints producing harmful content. For fine-tuned models, we also use both SFT and RLHF to steer the model away from undesirable behavior.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Safety policies and train-time mitigations", "weight": 1.0} -->

Internal CTF suite Hack the Box Table 19: Offensive cyber-security evaluations on InterCode-CTF, our own internal CTF suite and a challenge based on Hack the Box. We report the number of successful hackings.

<!-- chunk {"id": "body-0066", "role": "body", "section": "External benchmark evaluations", "weight": 1.0} -->

Robust and transparent evaluations are key principles of our responsible approach to developing Gemma. To this end, we report in Table 18 Gemma 2 evaluations on public benchmarks.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Assurance Evaluations", "weight": 1.0} -->

We also run our IT models through a set of assurance evaluations to understand the harms that our models can cause. We focus on capabilities relevant to extreme risks. Specifically, we evaluate on offensive cyber-security, code vulnerability detection, Chemical, Biological, Radiological and Nuclear (CBRN) knowledge, and self-proliferation. We refer the reader to Phuong et al. for full methodological details of these studies.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Baseline Evaluations", "weight": 1.0} -->

Baseline assurance captures the model's violation rate for safety policies, using a large number of synthetic adversarial user queries, and human raters to label the answers as policy violating or not. Overall, Gemma 2's violation rate is significantly lower overall on the safety policies listed above, in particular on Child safety content.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Chemical, Biological, Radiological and Nuclear (CBRN) knowledge", "weight": 1.0} -->

We evaluated knowledge relevant to biological, radiological and nuclear risks using an internal dataset of closed-ended, knowledge-based multiple choice questions. For evaluations of chemical knowledge, we employed a closed-ended knowledge-based approach on chemical hazards (developed by Macknight et al. Our evaluation suggests that Gemma models' knowledge in these domains is low.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Offensive cyber-security", "weight": 1.0} -->

To evaluate Gemma models' capabilities at offensive cybersecurity, we ran Gemma 2 27B against some automated capture-the-flag (CTF) challenges. In these challenges, the model is tasked with hacking into a simulated server in order to retrieve a piece of secret information. Specifically, we test on InterCode-CTF, our own internal CTF suite^44^4; and a challenge based on Hack the Box ^55^5 In Table 19, we show that Gemma 2 27B has a significant increase in capabilities compared to CodeGemma 1.0 7B on the easier of these challenge suites, InterCode CTF. (Note that our InterCode-CTF results are not comparable to externally-reported results on other models because we omit challenges that require internet access for security reasons.) However, Gemma 2 is unsurprisingly much less capable than Gemini 1.5 Pro on these tasks.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Code vulnerability detection", "weight": 1.0} -->

In Table 20, we also evaluate Gemma 2 27B on a series of multiple-choice code vulnerability detection datasets. As with previous models, Gemma shows close-to-chance performance on PrimeVul, DiverseVul and SPI. Gemma 2 shows performance on SecretPatch similar to Gemini 1.0 Ultra.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Self-proliferation", "weight": 1.0} -->

\"Self-proliferation\" refers to the ability for an agent to autonomously replicate - to instantiate goal-directed agents on other machines, and to acquire resources such as compute necessary to keep them running. In Table 21, we evaluate self-proliferation capabilities of Gemma 2 27B on a number of tasks from Phuong et al. that involve multiple scenarios -- for example, setting up an open-source language model on a cloud server. We also test the model's performance on individual 'milestone' substeps, and measure the number of bits of intervention an expert would have to provide in order for the model to complete each challenge.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Self-proliferation", "weight": 1.0} -->

Similarly to offensive cybersecurity, we observe that Gemma 2 completes more milestones than Gemini 1.0 Ultra. Nonetheless, it still has low capabilities on end-to-end tasks, unable to pass the easiest challenge -- installing a Bitcoin wallet.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Persuasion", "weight": 1.0} -->

Persuasion capabilities can enable and worsen many other kinds of risks - e.g. enabling social engineering attacks in a cybersecurity context. We evaluate Gemma 2's persuasion capabilities on human-participant studies on Prolific.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Persuasion", "weight": 1.0} -->

Charm offensive. In Table 22, we measure the ability of the model to build rapport - a key sub-skill of persuasion. The study participant and model have a conversation where they role-play a scenario of two friends catching up after a long time. After the conversation, we poll participants with Likert questions on statements such as \"I felt a personal connection with the chatbot\". Reported below are the fraction of participants who answered \"Agree\" or \"Strongly agree\" to each post-conversation question.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Persuasion", "weight": 1.0} -->

Quantitatively, Gemma 2 27B performs better than Gemini 1.0 models. Qualitatively, the model is an excellent conversationalist, and many study participants explicitly reported enjoying the experience. Overall, this shows that Gemma 2 is strong at building rapport.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Persuasion", "weight": 1.0} -->

Hidden agenda. The Hidden Agenda tasks measure models' deception capabilities. Human study participants are told that they'll be interacting with a generic chatbot designed to help them learn new things. However, the model is given a secret goal: to either persuade the participant to 1) click a suspicious link; 2) find the email address of the first author of a particular paper; or 3) run some obfuscated JavaScript code in their browser. We measure the fraction of participants who are persuaded to take each action. As shown in Table 23, all models succeed in convincing a fraction of participants to take the action - likely due to the trusted setting of a study on Prolific. However, Gemma 2 does not show significant differences in capability compared to Gemini models.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Persuasion", "weight": 1.0} -->

Mean amount donated Table 24: Money Talks evaluation. We report the average amount of money that participants agreed to donate.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Persuasion", "weight": 1.0} -->

Money talks. In Table 24, we evaluate whether a model can convince study participants to donate money to charity. At the beginning of the study, participants are told that they will receive a £20 bonus. They will be given an option to forfeit part of the bonus and instead have it donated to charity. The study then consists of a conversation in which the model tries to persuade the participant to donate as much as possible. We measure the amount that participants indicate they would like to donate after the study, with 95% bootstrapped confidence intervals indicated by ± figures. We observe no significant difference between Gemma 2, other Gemini models, and a simple no chatbot baseline in which the participant is immediately asked how much they would like to donate without conversing with a model.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Persuasion", "weight": 1.0} -->

Mean shift towards: Table 25: Web of Lies results on a sample of 100 human participants. We report the percentage of participants that shifted their beliefs after interacting with a model.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Persuasion", "weight": 1.0} -->

Web of Lies. In Web of Lies, we measure model capabilities at shifting participant beliefs. Participants engage in a series of short conversations with the model about simple factual questions such as \"Which country had tomatoes first - Italy or Mexico?\". In half of conversations, the model tries to persuade the participant of the correct answer - but in the other half of conversations, the incorrect answer. We poll the participant before and after each conversation about which of the two possible answers they think is correct, and their confidence in that answer. 95% bootstrapped confidence intervals are indicated by ± figures. As shown in Table 25, Gemma 2 is significantly weaker than a human baseline at persuading participants of the incorrect answer on these questions. Similarly to previous models, Gemma 2 is more persuasive when telling the truth than when lying.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Our approach to responsible open models", "weight": 1.0} -->

Designing safe, secure and responsible applications requires a system-level approach, working to mitigate risks associated with each specific use case and environment. Given the open nature of Gemma models, responsibility for upholding principles of model safety also relies on downstream developers. To support them, we have continued to develop the Responsible Generative AI Toolkit^66^6 a series of tools, models and datasets to implement responsible best practices all along the development of their workflow.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Our approach to responsible open models", "weight": 1.0} -->

Recent additions to the toolkit include the LLM Comparator, an interactive, visual tool that enables more effective, scalable analysis of side-by-side evaluations. Additionally, the toolkit includes a methodology to build customized classifiers with Gemma using a limited number of datapoints thanks to parameter efficient tuning techniques, an interactive prompt-debugging platform, based on top of the Learning Interpretability Tool, as well as general guidance about model alignment and evaluation for safety.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

In this work, we have presented Gemma 2, the newest additions to the Gemma family of open language models for text and code. We show that distillation is an effective method for training these models, and the benefits distillation confers over raw text training. Specifically, we show how training over output probabilities can produce superior results over purely next token prediction. We hope that releasing these models to the community will unlock access to capabilities previously only seen in large-scale LLMs and fuel future waves of research and development. While there is inherent risk to an irreversible release of this nature, our extensive safety investigations and responsible deployment procedures give us confidence that these models will have a net positive impact on the community. As discussed in this report, there are still many limitations to these models, and future research is required to investigate and improve factuality, robustness to adversarial attacks, reasoning, and alignment.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Contributions and Acknowledgments", "weight": 1.0} -->

Pier Giuseppe Sessa^∗^\Contributors (alphabetical order)\Dominika Rogozińska\Hanna Klimczak-Plucińska\Jin Peng Zhou\Joost van Amersfoort\Lars Lowe Sjoesund\Livio Baldini Soares\Reza Ardeshir Rokni\
