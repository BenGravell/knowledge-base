<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Kimi-VL Technical Report

Topics include Reinforcement learning, Robustness, Language models, Learning, Kimi-VL, Vision-language models, Supervised fine-tuning, SFT.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present Kimi-VL, an efficient open-source Mixture-of-Experts (MoE) vision-language model (VLM) that offers advanced multimodal reasoning, long-context understanding, and strong agent capabilities - all while activating only 2.8B parameters in its language decoder (Kimi-VL-A3B). Kimi-VL demonstrates strong performance across challenging domains: as a general-purpose VLM, Kimi-VL excels in multi-turn agent tasks (e.g., OSWorld), matching flagship models. Furthermore, it exhibits remarkable capabilities across diverse challenging vision language tasks, including college-level image and video comprehension, OCR, mathematical reasoning, and multi-image understanding. In comparative evaluations, it effectively competes with cutting-edge efficient VLMs such as GPT-4o-mini, Qwen2.5-VL-7B, and Gemma-3-12B-IT, while surpassing GPT-4o in several key domains. Kimi-VL also advances in processing long contexts and perceiving clearly.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

With a 128K extended context window, Kimi-VL can process diverse long inputs, achieving impressive scores of 64.5 on LongVideoBench and 35.1 on MMLongBench-Doc. Its native-resolution vision encoder, MoonViT, further allows it to see and understand ultra-high-resolution visual inputs, achieving 83.2 on InfoVQA and 34.5 on ScreenSpot-Pro, while maintaining lower computational cost for common tasks. Building upon Kimi-VL, we introduce an advanced long-thinking variant: Kimi-VL-Thinking-2506. Developed through long chain-of-thought (CoT) supervised fine-tuning (SFT) and reinforcement learning (RL), the latest model exhibits strong long-horizon reasoning capabilities (64.0 on MMMU, 46.3 on MMMU-Pro, 56.9 on MathVision, 80.1 on MathVista, 65.2 on VideoMMMU) while obtaining robust general abilities. Code and models are publicly accessible at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

With the rapid advancement of artificial intelligence, human expectations for AI assistants have transcended traditional language-only interactions, increasingly aligning with the inherently multimodal nature of our world. To better understand and interact with these expectations, new generations of natively multimodal models, such as GPT-4o \\parenciteopenai2024gpt4ocard and Google Gemini \\parencitegeminiteam2024gemini15unlockingmultimodal, have emerged with the capability to seamlessly perceive and interpret visual inputs alongside language processing. Most recently, advanced multimodal models, pioneered by OpenAI o1 series \\parenciteo12024 and Kimi k1.5 \\parenciteteam2025kimi, have further pushed these boundaries by incorporating deeper and longer reasoning on multimodal inputs, thereby tackling more complex problems in the multimodal domain.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nevertheless, development in large VLMs in the open-source community has significantly lagged behind their language-only counterparts, particularly in aspects of scalability, computational efficiency, and advanced reasoning capabilities. While language-only model DeepSeek R1 \\parencitedeepseekai2025deepseekr1incentivizingreasoningcapability has already leveraged the efficient and more scalable mixture-of-experts (MoE) architecture and facilitated sophisticated long chain-of-thought (CoT) reasoning, most recent open-source VLMs, e.g. Qwen2.5-VL \\parencitebai2025qwen25vltechnicalreport and Gemma-3 \\parencitegemmateam2025gemma3technicalreport, continue to rely on dense architectures and do not support long-CoT reasoning.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Early explorations into MoE-based vision-language models, such as DeepSeek-VL2 \\parencitewu2024deepseekvl2mixtureofexpertsvisionlanguagemodels and Aria \\parenciteli2024ariaopenmultimodalnative, exhibit limitations in other crucial dimensions. Architecturally, both models still adopt relatively traditional fixed-size vision encoders, hindering their adaptability to diverse visual inputs. From a capability perspective, DeepSeek-VL2 supports only a limited context length (4K), while Aria falls short in fine-grained visual tasks. Additionally, neither of them supports long-thinking abilities. Consequently, there remains a pressing need for an open-source VLM that effectively integrates structural innovation, stable capabilities, and enhanced reasoning through long-thinking.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In light of this, we present Kimi-VL, a vision-language model for the open-source community. Structurally, Kimi-VL consists of our Moonlight \\parenciteliu2025muonscalablellmtraining MoE language model with only 2.8B activated (16B total) parameters, paired with a 400M native-resolution MoonViT vision encoder. In terms of capability, as illustrated in Figure, Kimi-VL can robustly handle diverse tasks (fine-grained perception, math, college-level problems, OCR, agent, etc.) across a broad spectrum of input forms (single-image, multi-image, video, long-document, etc.).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

1\) Kimi-VL is smart: it has comparable text ability against efficient pure-text LLMs; without long thinking, Kimi-VL is already competitive in multimodal reasoning and multi-turn agent benchmarks, e.g., MMMU, MathVista, OSWorld.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

2\) Kimi-VL processes long: it effectively tackles long-context understanding on various multimodal inputs within its 128K context window, far ahead of similar-scale competitors on long video benchmarks and MMLongBench-Doc.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

3\) Kimi-VL perceives clear: it shows all-round competitive ability over existing efficient dense and MoE VLMs in various vision-language scenarios: visual perception, visual world knowledge, OCR, high-resolution OS screenshot, etc.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, with long-CoT activation and reinforcement learning (RL), we introduce the long-thinking version of Kimi-VL, Kimi-VL-Thinking, which further substantially improves performance on more complex multimodal reasoning scenarios. Despite its small scale, Kimi-VL-Thinking offers compelling performance on hard reasoning benchmarks (e.g., MMMU, MathVision, MathVista), outperforming many state-of-the-art VLMs with even larger sizes. We further release and improved version of the thinking model, Kimi-VL-Thinking-2506. The improved version has even better performance on these reasoning benchmarks while retaining or improving on common visual perception and understanding scenarios, e.g. high-resolution perception (V\*), OS grounding, video and long document understanding.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

The architecture of Kimi-VL consists of three parts: a native-resolution vision encoder (MoonViT), an MLP projector, and an MoE language model, as depicted in Figure. We introduce each part in this section.

<!-- chunk {"id": "body-0013", "role": "body", "section": "MoonViT: A Native-resolution Vision Encoder", "weight": 1.0} -->

We design MoonViT, the vision encoder of Kimi-VL, to natively process images at their varying resolutions, eliminating the need for complex sub-image splitting and splicing operations, as employed in LLaVA-OneVision \\parenciteli2024llavaonevisioneasyvisualtask. We incorporate the packing method from NaViT \\parencitedehghani2023patchnpacknavit, where images are divided into patches, flattened, and sequentially concatenated into 1D sequences. These preprocessing operations enable MoonViT to share the same core computation operators and optimization as a language model, such as the variable-length sequence attention mechanism supported by FlashAttention \\parencitedao2022flashattentionfastmemoryefficientexact, ensuring non-compromised training throughput for images of varying resolutions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "MoonViT: A Native-resolution Vision Encoder", "weight": 1.0} -->

MoonViT is initialized from and continually pre-trained on SigLIP-SO-400M \\parencitezhai2023sigmoidlosslanguageimage, which originally employs learnable fixed-size absolute positional embeddings to encode spatial information. While we interpolate these original position embeddings to better preserve SigLIP's capabilities, these interpolated embeddings become increasingly inadequate as image resolution increases. To address this limitation, we incorporate 2D rotary positional embedding (RoPE) \\parencitesu2023roformerenhancedtransformerrotary across the height and width dimensions, which improves the representation of fine-grained positional information, especially in high-resolution images. These two positional embedding approaches work together to encode spatial information for our model and seamlessly integrate with the flattening and packing procedures. This integration enables MoonViT to efficiently process images of varying resolutions within the same batch. The resulting continuous image features are then forwarded to the MLP projector and, ultimately, to the MoE language model for subsequent training stages.

<!-- chunk {"id": "body-0015", "role": "body", "section": "MoonViT: A Native-resolution Vision Encoder", "weight": 1.0} -->

In Kimi-VL-A3B-Thinking-2506, we further continually train this MoonViT to authentically encode up to 3.2 million pixels from a single image, 4 times compared to the original limit.

<!-- chunk {"id": "body-0016", "role": "body", "section": "MLP Projector", "weight": 1.0} -->

We employ a two-layer MLP to bridge the vision encoder (MoonViT) and the LLM. Specifically, we first use a pixel shuffle operation to compress the spatial dimension of the image features extracted by MoonViT, performing 2×2 downsampling in the spatial domain and correspondingly expanding the channel dimension. We then feed the pixel-shuffled features into a two-layer MLP to project them into the dimension of LLM embeddings.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Mixture-of-Experts (MoE) Language Model", "weight": 1.0} -->

The language model of Kimi-VL utilizes our Moonlight model \\parenciteliu2025muonscalablellmtraining, an MoE language model with 2.8B activated parameters, 16B total parameters, and an architecture similar to DeepSeek-V3 \\parencitedeepseekai2025deepseekv3technicalreport. For our implementation, we initialize from an intermediate checkpoint in Moonlight's pre-training stage---one that has processed 5.2T tokens of pure text data and activated an 8192-token (8K) context length. We then continue pre-training it using a joint recipe of multimodal and text-only data totaling 2.3T tokens, as detailed in Sec. 2.3.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Muon Optimizer", "weight": 1.0} -->

We use an enhanced Muon optimizer \\parenciteliu2025muon for model optimization. Compared to the original Muon optimizer \\parencitejordan2024muon, we add weight decay and carefully adjust the per-parameter update scale. Additionally, we develop a distributed implementation of Muon following the ZeRO-1 \\parenciterajbhandari2020zero optimization strategy, which achieves optimal memory efficiency and reduced communication overhead while preserving the algorithm's mathematical properties. This enhanced Muon optimizer is used throughout the entire training process to optimize all model parameters, including the vision encoder, the projector, and the language model.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Pre-Training Stages", "weight": 1.0} -->

As illustrated in Figure and Table, after loading the intermediate language model discussed above, Kimi-VL's pre-training comprises a total of 4 stages consuming 4.4T tokens overall: first, standalone ViT training to establish a robust native-resolution visual encoder, followed by three joint training stages (pre-training, cooldown, and long-context activation) that simultaneously enhance the model's language and multimodal capabilities. The details are as follows.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Pre-Training Stages", "weight": 1.0} -->

ViT &amp; LLM
ViT &amp; LLM
ViT &amp; LLM

<!-- chunk {"id": "body-0021", "role": "body", "section": "ViT Training Stages", "weight": 1.0} -->

The MoonViT is trained on image-text pairs, where the text components consist of a variety of targets: image alt texts, synthetic captions, grounding bboxes, and OCR texts. The training incorporates two objectives: a SigLIP \\parencitezhai2023sigmoidlosslanguageimage loss $\mathcal{L}_{siglip}$ (a variant of contrastive loss) and a cross-entropy loss $\mathcal{L}_{caption}$ for caption generation conditioned on input images. Following CoCa's approach \\parenciteyu2022cocacontrastivecaptionersimagetext, the final loss function is formulated as $\mathcal{L} = {\mathcal{L}_{siglip} + {\lambda\mathcal{L}_{caption}}}$, where $\lambda = 2$. Specifically, the image and text encoders compute the contrastive loss, while the text decoder performs next-token prediction (NTP) conditioned on features from the image encoder.

<!-- chunk {"id": "body-0022", "role": "body", "section": "ViT Training Stages", "weight": 1.0} -->

To accelerate training, we initialized both encoders with SigLIP SO-400M \\parencitezhai2023sigmoidlosslanguageimage weights and implemented a progressive resolution sampling strategy to gradually allow larger size; the text decoder is initialized from a tiny decoder-only language model. During training, we observed an emergence in the caption loss while scaling up OCR data, indicating that the text decoder had developed some OCR capabilities. After training the ViT in the CoCa-alike stage with 2T tokens, we align the MoonViT to the MoE language model using another 0.1T tokens, where only MoonViT and MLP projector are updated. This alignment stage significantly reduces the initial perplexity of MoonViT embeddings in the language model, allowing a smoother joint pre-training stage as follows.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Joint Pre-training Stage", "weight": 1.0} -->

In the joint pre-training stage, we train the model with a combination of pure text data (sampled from the same distribution as the initial language model) and a variety of multimodal data (as discussed in Sec. 3.1). We continue training from the loaded LLM checkpoint using the same learning rate scheduler, consuming an additional 1.4T tokens. The initial steps utilize solely language data, after which the proportion of multimodal data gradually increases. Through this progressive approach and the previous alignment stage, we observe that joint pre-training preserves the model's language capabilities while successfully integrating visual comprehension abilities.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Joint Cooldown Stage", "weight": 1.0} -->

The stage following the pre-training stage is a multimodal cooldown phase, where the model is continue trained with high-quality language and multimodal datasets to ensure superior performance. For the language part, through empirical investigation, we observe that the incorporation of synthetic data during the cooling phase yields significant performance improvements, particularly in mathematical reasoning, knowledge-based tasks, and code generation. The general text components of the cooldown dataset are curated from high-fidelity subsets of the pre-training corpus. For math, knowledge, and code domains, we employ a hybrid approach: utilizing selected pre-training subsets while augmenting them with synthetically generated content. Specifically, we leverage existing mathematical knowledge and code corpora as source material to generate question-answer (QA) pairs through a proprietary language model, implementing rejection sampling techniques to maintain quality standards \\parenciteyue2023mammoth,su2024nemotron. These synthesized QA pairs undergo comprehensive validation before being integrated into the cooldown dataset.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Joint Cooldown Stage", "weight": 1.0} -->

For the multimodal part, in addition to the two strategies as employed in text cooldown data preparation, i.e. question-answer synthesis and high-quality subset replay, to allow more comprehensive visual-centric perception and understanding \\parenciteli2024llavaonevisioneasyvisualtask,tong2024cambrian1fullyopenvisioncentric,guo2024mammothvlelicitingmultimodalreasoning, we filter and rewrite a variety of academic visual or vision-language data sources to QA pairs. Unlike post-training stages, these language and multimodal QA pairs in the cooldown stage are only included for activating specific abilities and henceforth facilitating learning high-quality data, thus, we keep their ratio at a low portion to avoid overfitting these QA patterns. The joint cooldown stage significantly improves both language and multimodal abilities of the model.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Joint Long-context Activation Stage", "weight": 1.0} -->

In the final pre-training stage, we extend the context length of the model from 8192 (8K) to 131072 (128K), with the inverse frequency of its RoPE \\parencitesu2023roformerenhancedtransformerrotary embeddings reset from 50,000 to 800,000. The joint long-context stage is conducted in two sub-stages, where each one extends the model's context length by four times. For data composition, we filter and upsample the ratio of long data to 25% in each sub-stage, while using the remaining 75% tokens to replay shorter data in its previous stage; our exploration confirms that this composition allows the model to effectively learn long-context understanding while maintaining short-context ability.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Joint Long-context Activation Stage", "weight": 1.0} -->

To allow the model to activate long-context abilities on both pure-text and multimodal inputs, the long data used in Kimi-VL's long-context activation consists of not only long text, but also long multimodal data, including long interleaved data, long videos, and long documents. Similar as cooldown data, we also synthesize a small portion of QA pairs to augment the learning efficiency of long-context activation. After the long-context activations, the model can pass needle-in-a-haystack (NIAH) evaluations with either long pure-text or long video haystack, proving its versatile long-context ability. We provide the NIAH recall accuracy on various range of context length up to 128K in Table.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Joint Supervised Fine-tuning (SFT)", "weight": 1.0} -->

In this phase, we fine-tune the base model of Kimi-VL with instruction-based fine-tuning to enhance its ability to follow instructions and engage in dialogue, culminating in the creation of the interactive Kimi-VL model. This is achieved by employing the ChatML format, which allows for a targeted instruction optimization while maintaining architectural consistency with Kimi-VL. We optimize the language model, MLP projector, and vision encoder using a mixture of pure-text and vision-language SFT data, which will be described in Sec 3.2. Supervision is applied only to answers and special tokens, with system and user prompts being masked. The model is exposed to a curated set of multimodal instruction-response pairs, where explicit dialogue role tagging, structured injection of visual embeddings, and preservation of cross-modal positional relationships are ensured through the format-aware packing. Additionally, to guarantee the model's comprehensive proficiency in dialogue, we incorporate a mix of multimodal data and pure text dialogue data used in Moonlight, ensuring its versatility across various dialogue scenarios.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Joint Supervised Fine-tuning (SFT)", "weight": 1.0} -->

We first train the model at the sequence length of 32k tokens for 1 epoch, followed by another epoch at the sequence length of 128k tokens. In the first stage (32K), the learning rate decays from $2 \times 10^{- 5}$ to $2 \times 10^{- 6}$, before it re-warmups to $1 \times 10^{- 5}$ in the second stage (128K) and finally decays to $1 \times 10^{- 6}$. To improve training efficiency, we pack multiple training examples into each single training sequence.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Long-CoT Supervised Fine-Tuning", "weight": 1.0} -->

With the refined RL prompt set, we employ prompt engineering to construct a small yet high-quality long-CoT warmup dataset, containing accurately verified reasoning paths for both text and image inputs. This approach resembles rejection sampling (RS) but focuses on generating long-CoT reasoning paths through prompt engineering. The resulting warmup dataset is designed to encapsulate key cognitive processes that are fundamental to human-like reasoning, such as planning, where the model systematically outlines steps before execution; evaluation, involving critical assessment of intermediate steps; reflection, enabling the model to reconsider and refine its approach; and exploration, encouraging consideration of alternative solutions. By performing a lightweight SFT on this warm-up dataset, we effectively prime the model to internalize these multimodal reasoning strategies. As a result, the fine-tuned long-CoT model demonstrates improved capability in generating more detailed and logically coherent responses, which enhances its performance across diverse reasoning tasks.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

To further advance the model's reasoning abilities, we then train the model with reinforcement learning (RL), enabling the model to autonomously generate structured CoT rationales. Specifically, similar as Kimi k1.5 \\parenciteteam2025kimi, we adopt a variant of online policy mirror descent as our RL algorithm, which iteratively refines the policy model $\pi_{\theta}$ to improve its problem-solving accuracy.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

where $r$ is a reward model that justifies the correctness of the proposed answer $y$ for the given problem $x$, by assigning a value ${r{(x,y,y^{\ast})}} \in {\{ 0,1\}}$ based on the ground truth $y^{\ast}$, and $\tau > 0$ is a parameter controlling the degree of regularization.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

Each training iteration begins by sampling a problem batch from the dataset $\mathcal{D}$, and the model parameters are updated to $\theta_{i + 1}$ using the policy gradient derived, with the optimized policy model subsequently assuming the role of reference policy for the subsequent iteration. To enhance RL training efficiency, we implement a length-based reward to penalize excessively long responses, mitigating the overthinking problem where the model generates redundant reasoning chains. Besides, we employ two sampling strategies including curriculum sampling and prioritized sampling, which leverage difficulty labels and per-instance success rates to focus training effort on the most pedagogically valuable examples, thereby optimizing the learning trajectory and improving training efficiency.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

Through large-scale reinforcement learning training, we can derive a model that harnesses the strengths of both basic prompt-based CoT reasoning and sophisticated planning-enhanced CoT approaches. During inference, the model maintains standard autoregressive sequence generation, eliminating the deployment complexities associated with specialized planning algorithms that require parallel computation. Simultaneously, the model develops essential meta-reasoning abilities including error detection, backtracking, and iterative solution refinement by effectively utilizing the complete history of explored reasoning paths as contextual information. With endogenous learning from its complete reasoning trace history, the model can effectively encode planned search procedures into its parametric knowledge.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Infrastructure", "weight": 1.0} -->

Storage We utilize S3 \\parenciteamazon_s3 compatible object storage from cloud service vendors to store our visual-text data. To minimize the time between data preparation and model training, we store visual data in its original format and have developed an efficient and flexible data loading system.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Infrastructure", "weight": 1.0} -->

Supports on-the-fly data shuffling, mixing, tokenization, loss masking and packing during training, allowing us to adjust data proportions as needed;

<!-- chunk {"id": "body-0037", "role": "body", "section": "Infrastructure", "weight": 1.0} -->

Enables random augmentation of both visual and text data, while preserving the correctness of 2D coordinate and orientation information during transformations;

<!-- chunk {"id": "body-0038", "role": "body", "section": "Infrastructure", "weight": 1.0} -->

Ensures reproducibility by strictly controlling random states and other states across different data loader workers, guaranteeing that any interrupted training can be resumed seamlessly---the data sequence after resumption remains identical to an uninterrupted run;

<!-- chunk {"id": "body-0039", "role": "body", "section": "Infrastructure", "weight": 1.0} -->

Delivers high-performance data loading: through multiple caching strategies, our system reliably supports training on large scale clusters while maintaining controlled request rates and throughput to the object storage.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Infrastructure", "weight": 1.0} -->

Additionally, to ensure consistent dataset quality control, we developed a centralized platform for data registration, visualization, compiling statistics, synchronizing data across cloud storage systems, and managing dataset lifecycles.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Infrastructure", "weight": 1.0} -->

Parallelism We adopt a 4D parallelism strategy---Data Parallelism \\parenciteli2020pytorchdistributedexperiencesaccelerating, Expert Parallelism \\parencitefedus2022switchtransformersscalingtrillion, Pipeline Parallelism \\parencitehuang2019gpipeefficienttraininggiant,narayanan2021efficientlargescalelanguagemodel, and Context Parallelism \\parencitejacobs2023deepspeedulyssesoptimizationsenabling,liu2023ringattentionblockwisetransformers---to accelerate the speed of Kimi-VL. After optimizing parallel strategies, the resulting training throughput of our model is around 60% higher than a 7B dense VLM (e.g. VLMs based on Qwen2.5-7B).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Infrastructure", "weight": 1.0} -->

Data Parallelism (DP). DP replicates the model across multiple devices, each processing different micro-batches. This setup allows larger effective batch sizes by simply increasing the number of devices.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Infrastructure", "weight": 1.0} -->

Expert Parallelism (EP). EP distributes expert modules in the MoE layer across multiple devices. When combined with DP, experts on a given device can handle tokens from different DP groups, enhancing computational efficiency.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Infrastructure", "weight": 1.0} -->

Pipeline Parallelism (PP). PP splits the model into multiple layer-based stages. To minimize pipeline bubbles, we allocate the Vision Tower (VT) and several decoder layers to the first stage, place the output layer and additional decoder layers in the last stage, and distribute the remaining decoder layers evenly across intermediate stages based on their time overhead.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Infrastructure", "weight": 1.0} -->

Context Parallelism (CP). CP addresses long-sequence training by splitting sequences across different CP ranks in conjunction with flash attention \\parencitedao2022flashattentionfastmemoryefficientexact. This substantially reduces peak memory usage and relieves the memory pressure from attention computations.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Infrastructure", "weight": 1.0} -->

Beyond these four parallel strategies, we incorporate ZeRO1 \\parenciterajbhandari2020zero and Selective Checkpointing Activation \\parencitechen2016trainingdeepnetssublinear, korthikanti2022reducingactivationrecomputationlarge to further optimize memory usage. ZeRO1 reduces optimizer state overhead by using a distributed optimizer while avoiding extra communication costs. Selective Checkpointing Activation trades time for space by recomputing only those layers that have low time overhead but high memory consumption, striking a balance between computation efficiency and memory demands. For extremely long sequences, we expand recomputation to a broader set of layers to prevent out-of-memory errors.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Pre-Training Data", "weight": 1.0} -->

Our multimodal pre-training corpus is designed to provide high-quality data that enables models to process and understand information from multiple modalities, including text, images, and videos. To this end, we have also curated high-quality data from six categories -- caption, interleaving, OCR, knowledge, video, and agent -- to form the corpus.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Pre-Training Data", "weight": 1.0} -->

When constructing our training corpus, we developed several multimodal data processing pipelines to ensure data quality, encompassing filtering, synthesis, and deduplication. Establishing an effective multimodal data strategy is crucial during the joint training of vision and language, as it both preserves the capabilities of the language model and facilitates alignment of knowledge across diverse modalities.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Caption Data", "weight": 1.0} -->

Our caption data provides the model with fundamental modality alignment and a broad range of world knowledge. By incorporating caption data, the multimodal LLM gains wider world knowledge with high learning efficiency. We have integrated various open-source Chinese and English caption datasets like \\parenciteschuhmann2022laion, gadre2024datacomp and also collected substantial in-house caption data from multiple sources. However, throughout the training process, we strictly limit the proportion of synthetic caption data to mitigate the risk of hallucination stemming from insufficient real-world knowledge.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Caption Data", "weight": 1.0} -->

For general caption data, we follow a rigorous quality control pipeline that avoids duplication and maintain high image-text correlation. We also vary image resolution during pre-training to ensure that the vision tower remains effective when processing images of both high- and low-resolution.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Caption Data", "weight": 1.0} -->

Image-text Interleaving Data During the pre-training phase, the model benefits from interleaving data for many aspects. For example, multi-image comprehension ability can be boosted by interleaving data; interleaving data always provides detailed knowledge for the given image; a longer multimodal context learning ability can also be gained by interleaving data. What's more, we also find that interleaving data can contribute positively to maintaining the model's language abilities. Thus, image-text interleaving data is an important part in our training corpus. Our multimodal corpus considered open-sourced interleave datasets like \\parencitezhu2024multimodal,laurenccon2024obelics and also constructed large-scale in-house data using resources like textbooks, webpages, and tutorials. Further, we also find that synthesizing the interleaving data benefits the performance of multimodal LLM for keeping the text knowledge.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Caption Data", "weight": 1.0} -->

To ensure each image's knowledge is sufficiently studied, for all the interleaving data, despite standard filtering, deduping, and other quality control pipeline, we also integrate a data reordering procedure to keep all the image and text in the correct order.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Caption Data", "weight": 1.0} -->

OCR Data Optical Character Recognition (OCR) is a widely adopted technique that converts text from images into an editable format. In our model, a robust OCR capability is deemed essential for better aligning the model with human values. Accordingly, our OCR data sources are diverse, ranging from open-source to in-house datasets, encompassing both clean and augmented images, and spanning over single-page and multi-page inputs.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Caption Data", "weight": 1.0} -->

In addition to the publicly available data, we have developed a substantial volume of in-house OCR datasets, covering multilingual text, dense text layouts, web-based content, and handwritten samples. Furthermore, following the principles outlined in OCR 2.0 \\parencitewei2024general, our model is also equipped to handle a variety of optical image types, including figures, tables, geometry diagrams, mermaid plots, and natural scene text. We apply extensive data augmentation techniques---such as rotation, distortion, color adjustments, and noise addition---to enhance the model's robustness. As a result, our model achieves a high level of proficiency in OCR tasks.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Caption Data", "weight": 1.0} -->

In addition to single-page OCR data, we collect and convert a large volume of in-house multi-page OCR data to activate the model's understanding of long documents in the real world. With the help of these data, our model is capable of performing accurate OCR on a single image but can also comprehend an entire academic paper or a scanned book.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Caption Data", "weight": 1.0} -->

Knowledge Data The concept of multimodal knowledge data is analogous to the previously mentioned text pre-training data, except here we focus on assembling a comprehensive repository of human knowledge from diverse sources to further enhance the model's capabilities. For example, carefully curated geometry data in our dataset is vital for developing visual reasoning skills, ensuring the model can interpret the abstract diagrams created by humans.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Caption Data", "weight": 1.0} -->

Our knowledge corpus adheres to a standardized taxonomy to balance content across various categories, ensuring diversity in data sources. Similar to text-only corpora, which gather knowledge from textbooks, research papers, and other academic materials, multimodal knowledge data employs both a layout parser and an OCR model to process content from these sources. While we also include filtered data from internet-based and other external resources.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Caption Data", "weight": 1.0} -->

Because a significant portion of our knowledge corpus is sourced from internet-based materials, infographics can cause the model to focus solely on OCR-based information. In such cases, relying exclusively on a basic OCR pipeline may limit training effectiveness. To address this, we have developed an additional pipeline that better captures the purely textual information embedded within images.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Caption Data", "weight": 1.0} -->

Agent Data For agent tasks, the model's grounding and planning capabilities have been significantly enhanced. In addition to utilizing publicly available data, a platform has been established to efficiently manage and execute virtual machine environments in bulk. Within these virtual environments, heuristic methods were employed to collect screenshots and corresponding action data. This data was then processed into dense grounding formats and continuous trajectory formats. The design of the Action Space was categorized according to Desktop, Mobile, and Web environments. Furthermore, icon data was collected to strengthen the model's understanding of the meanings of icons within software graphical user interfaces (GUIs). To enhance the model's planning ability for solving multi-step desktop tasks, a set of computer-use trajectories was collected from human annotators, each accompanied by synthesized Chain-of-Thought (Aguvis \\parencitexu2024aguvis). These multi-step agent demonstrations equip Kimi-VL with the capability to complete real-world desktop tasks (on both Ubuntu and Windows).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Caption Data", "weight": 1.0} -->

Video Data In addition to image-only and image-text interleaved data, we also incorporate large-scale video data during pre-training, cooldown, and long-context activation stages to enable two directions of essential abilities of our model: first, to understand a long-context sequence dominated by images (e.g. hour-long videos) in addition to long text; second, to perceive fine-grained spatio-temporal correspondence in short video clips.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Caption Data", "weight": 1.0} -->

Our video data are sourced from diverse resources, including open-source datasets as well as in-house web-scale video data, and span videos of varying durations. Similarly, to ensure sufficient generalization ability, our video data cover a wide range of scenes and diverse tasks. We cover tasks such as video description and video grounding, among others. For long videos, we carefully design a pipeline to produce dense captions. Similar to processing the caption data, we strictly limit the proportion of the synthetic dense video description data to reduce the risk of hallucinations.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Caption Data", "weight": 1.0} -->

Text Data Our text pretrain corpus directly utilizes the data in Moonlight \[liu2025muonscalablellmtraining\], which is designed to provide comprehensive and high-quality data for training large language models (LLMs). It encompasses five domains: English, Chinese, Code, Mathematics & Reasoning, and Knowledge. We employ sophisticated filtering and quality control mechanisms for each domain to ensure the highest quality training data. For all pretrain data, we conducted rigorous individual validation for each data source to assess its specific contribution to the overall training recipe. This systematic evaluation ensures the quality and effectiveness of our diverse data composition. To optimize the overall composition of our training corpus, the sampling strategy for different document types is empirically determined through extensive experimentation. We conduct isolated evaluations to identify document subsets that contribute most significantly to the model's knowledge acquisition capabilities. These high-value subsets are upsampled in the final training corpus. However, to maintain data diversity and ensure model generalization, we carefully preserve a balanced representation of other document types at appropriate ratios. This data-driven approach helps us optimize the trade-off between focused knowledge acquisition and broad generalization capabilities.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Caption Data", "weight": 1.0} -->

^11^footnotetext: GPT-4o and GPT-4o-mini results use Omniparser without UIA, according to \[bonatti2024windowsagentarenaevaluating\].

<!-- chunk {"id": "body-0064", "role": "body", "section": "Instruction Data", "weight": 1.0} -->

At this stage, the data is primarily aimed at enhancing the model's conversational abilities and instruction-following capabilities. To cover as many scenarios as possible, we enrich the data across different domains. For non-reasoning tasks, including chart interpretation, agent grounding, OCR, image-grounded conversations, question-answering, writing, and text processing, we initially construct a seed dataset through human annotation. This seed dataset is used to train a seed model. Subsequently, we collect a diverse set of prompts and employ the seed model to generate multiple responses to each prompt. Annotators then rank these responses and refine the top-ranked response to produce the final version. For reasoning tasks like visual coding, visual reasoning, and math/science problems, where rule-based and model-based verifications are more accurate and efficient than human judgment, we utilize rejection sampling to expand the SFT dataset. The complete vanilla SFT dataset comprises approximately a 1:1 ratio of text tokens to image tokens.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Reasoning Data", "weight": 1.0} -->

Our reasoning data is meticulously constructed for activation and enhancement of the model's multimodal reasoning capabilities during both the long-CoT supervised fine-tuning and reinforcement learning stages. Through developing a generation pipeline that resembles rejection sampling (RS) and prompt engineering, we collect and synthesize an amount of high-quality long-CoT data. Specifically, we first assemble a collection of QA data with ground truth annotations that require multi-step reasoning, such as mathematical problem-solving and domain-specific VQA. Subsequently, we sample multiple detailed reasoning trajectories for each question by leveraging a powerful long-CoT model - Kimi k1.5 \\parenciteteam2025kimi with curated reasoning prompts. In rejection sampling, we feed the true labels and model predictions into an off-the-shelf reward model for judgment. Wrong chain-of-thought responses are filtered out according to the model evaluation as well as some rule-based rewards, thus improving the reasoning data quality.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We begin by presenting our comprehensive model and conducting a comparative analysis with leading state-of-the-art (SoTA) solutions. Following this introduction, we proceed to assess various sub-capabilities of the model through detailed performance evaluations. This part examines how effectively the model handles different tasks and scenarios, providing insights into its strengths and limitations across diverse functional domains.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Comparison to the State-of-the-Art Models", "weight": 1.0} -->

Table presents a comprehensive evaluation of Kimi-VL against state-of-the-art vision-language models across multiple benchmarks. Although having a more parameter-efficient architecture (2.8B+0.4B activated parameters) compared to larger models such as GPT-4o, Llama-3.2-11B-Inst. and Gemma3-12B-IT, Kimi-VL demonstrates competitive or superior performance in several key areas. Our model employs a Mixture-of-Experts (MoE) architecture similar to DeepSeek-VL2, but outperforms it on most benchmarks with significantly fewer parameters (activated: 2.8B vs 4.5B; total: 16B vs 28B); it also outperforms Qwen2.5-VL-7B (actually 8.3B) on 19 out of 24 benchmarks, though the latter has 2.59$\times$ more activated parameters. The following sections analyze performance across specific domains, which reveals Kimi-VL 's strengths in OCR, math, agent, long-form content understanding, multi-image and video perception.

<!-- chunk {"id": "body-0068", "role": "body", "section": "College-level Academic Problems", "weight": 1.0} -->

Our Kimi-VL model demonstrates competitive performance on college-level academic benchmarks. On MMMU validation set, it achieves a score of 57.0%, which outperforms DeepSeek-VL2 (51.1%) and is comparable to Qwen2.5-VL-7B (58.6%) and even Gemma-3-12B-IT (59.6%), despite having significantly fewer activated parameters. On video college-level problems, it significantly outperforms Qwen2.5-VL-7B and DeepSeek-VL2, only behind \>10B Gemma-3-12B-IT, demonstrating reasonable university-level understanding capabilities compared to larger models. These results indicate that Kimi-VL effectively balances parameter efficiency with academic reasoning abilities.

<!-- chunk {"id": "body-0069", "role": "body", "section": "General Visual Ability", "weight": 1.0} -->

Kimi-VL exhibits strong general visual understanding capabilities across multiple benchmarks. On MMBench-EN-v1.1, it achieves 83.1% accuracy, outperforming all efficient VLMs in comparison, and performing on par with GPT-4o. For AI2D, our model achieves 84.9% and surpasses all compared models including GPT-4o (84.6%). On MMVet, Kimi-VL scores 66.7% and ties closely with Qwen2.5-VL-7B (67.1%) and GPT-4o-mini (66.9%). For RealWorldQA, it achieves 68.1%, outperforming Gemma3-12B (59.1%) and approaching Qwen2.5-VL-7B (68.5%). These results demonstrate that our model maintains robust general visual understanding despite its compact architecture.

<!-- chunk {"id": "body-0070", "role": "body", "section": "General Visual Ability", "weight": 1.0} -->

In multi-image reasoning tasks, Kimi-VL shows promising capabilities with a score of 57.3% on the BLINK benchmark. This performance surpasses Qwen2.5-VL-7B (56.4%), GPT-4o-mini (53.6%), Gemma3-12B-IT (50.3%), and Llama3.2-11B-Inst. (39.8%). The ability to reason across multiple images requires understanding spatial and temporal relationships between visual elements, which our model handles effectively with fewer parameters than most competitors.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Mathematical Reasoning", "weight": 1.0} -->

With its relatively small scale, Kimi-VL also demonstrates strong mathematical reasoning capabilities, particularly on the MathVista benchmark where it achieves 68.7%, outperforming all compared models including GPT-4o (63.8%) and Qwen2.5-VL-7B (68.2%). It indicates our model's exceptional ability to understand and solve mathematical problems presented in visual contexts. On the more challenging MathVision benchmark, due to limited activated parameters, Kimi-VL outperforms DeepSeek-VL2 and Llama-3.2-11B-Inst., but lags behind Qwen2.5-VL-7B and Gemma-12B-IT. Nevertheless, through RL and test-time scaling, Kimi-VL-Thinking has significantly improved and already on par with 30B-level VLMs. These results highlight our model's effectiveness in combining visual perception with mathematical problem-solving, an essential capability for real-world applications.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Document Understanding and OCR", "weight": 1.0} -->

Kimi-VL excels in document understanding and OCR tasks across all benchmarks in this category. On InfoVQA, it achieves 83.2% accuracy, outperforming GPT-4o (80.7%) and DeepSeek-VL2 (78.1%). For OCRBench, our model scores 86.7%, surpassing all other models including GPT-4o-mini (78.5%) and DeepSeek-VL2 (81.1%). These results demonstrate that our model has exceptional text recognition and document understanding capabilities, making it especially suitable for applications involving document processing and information extraction.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Agent Grounding and Multi-turn Agent Interaction", "weight": 1.0} -->

In agent-based tasks, Kimi-VL demonstrates remarkable performance. On single-step grounding, our model shows strong accuracy, with 92.0% on ScreenSpot-V2 and 34.5% on extremely difficult ScreenSpot-Pro (on 4K screens), proving its strong agent grounding abilities. More importantly, it also shows strong multi-step turn agent interaction abilities: For OSWorld, Kimi-VL reaches 8.22%, outperforming GPT-4o (5.03%) and other capable open-source models; On WindowsAgentArena, our model achieves 10.4%, also surpassing GPT-4o (9.4%) and others. These results highlight Kimi-VL's exceptional ability to understand and interact with operating system interfaces, suggesting strong potential for applications in automated UI navigation and task execution.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Long Document and Long Video Understanding", "weight": 1.0} -->

Kimi-VL demonstrates competitive performance in long-form content understanding. On MMLongBench-Doc, a challenging benchmark with question-answering on up to 100+ pages, it achieves 35.1%, outperforming GPT-4o-mini (29.0%) and Qwen2.5-VL-7B (29.6%), only behind GPT-4o (42.8%). For long video understanding, on Video-MME, our model outperforms all efficient VLMs and especially leads on the fairer w/o subtitle setting, where models have to find answers from video frames instead of hacking from input subtitles; on w/ subtitlesetting, it also reaches extraordinary 72.6% accuracy. On the MCQ subset of MLVU, Kimi-VL achieves an impressive 74.2% score, achieving state-of-the-art and surpassing both GPT-4o (64.6%) and Qwen2.5-VL-7B (70.2%).

<!-- chunk {"id": "body-0075", "role": "body", "section": "Long Document and Long Video Understanding", "weight": 1.0} -->

For LongVideoBench, it scores 64.5%, outperforming all compared models except GPT-4o (66.7%). These results demonstrate Kimi-VL 's strong capability to understand long-form PDFs and videos.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Egocentric and Fine-grained Video Perception", "weight": 1.0} -->

Kimi-VL also shows strong performance in more nuanced video perception tasks. On EgoSchema full set (hidden test set), it achieves 78.5%, significantly outperforming GPT-4o (72.2%), Qwen2.5-VL-7B (65.0%). For VSI-Bench, a very challenging benchmark that requires to understand spatial relationships and correspondences of multiple objects in a video, our model scores 37.4%, surpassing GPT-4o (34.0%) and Qwen2.5-VL-7B (34.2%). In TOMATO that examines fine-grained temporal perception of VLMs, Kimi-VL reaches 31.7%, outperforming Qwen2.5-VL-7B (27.6%) and GPT-4o-Mini (28.8%). These results demonstrate our model's strong capability to understand dynamic visual content, track objects over time, and interpret complex actions in video sequences, making it well-suited for applications requiring temporal visual understanding.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Kimi-VL-A3B-Thinking: A Reasoning Extension of Kimi-VL", "weight": 1.0} -->

Furthermore, we conduct a reasoning extension to empower Kimi-VL to reason with CoT and present a long-thinking version of the model, Kimi-VL-Thinking, through long-CoT activation and reinforcement learning. We validate its superior performance on several image benchmarks, as shown in Table.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Kimi-VL-A3B-Thinking: A Reasoning Extension of Kimi-VL", "weight": 1.0} -->

Kimi-VL-Thinking significantly improves over the base Kimi-VL model, with gains of 2.6% on MathVista, 4.7% on MMMU, and 15.4% on MathVision, demonstrating its capability to leverage test-time computation for deeper reasoning and better handling of complex multimodal queries. In Table, Kimi-VL-Thinking further outperforms or rivals state-of-the-art thinking and non-thinking models: achieving 71.3% on MathVista, outperforming GPT-4o (63.8%) and GPT-4o-mini (56.7%); scoring 61.7% on MMMU, surpassing GPT-4o-mini (60.0%) and Qwen2.5-VL-7B (58.6%); and reaching 36.8% on MathVision, exceeding GPT-4o (30.4%) and Gemma-3-27B-IT (35.5%), even QVQ-72B (35.9%).

<!-- chunk {"id": "body-0079", "role": "body", "section": "Kimi-VL-A3B-Thinking: A Reasoning Extension of Kimi-VL", "weight": 1.0} -->

While marginally behind some larger-scale models on select benchmarks, Kimi-VL-Thinking accomplishes these results with only 3B activated parameters---orders of magnitude fewer than its counterparts---underscoring its strong efficiency and effectiveness in multimodal reasoning.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Kimi-VL-A3B-Thinking: A Reasoning Extension of Kimi-VL", "weight": 1.0} -->

Our Kimi-VL-Thinking model also exhibits strong test-time scaling properties, as shown in Figure. Specifically, increasing the max thinking token length at inference time consistently improves test-time accuracy across all three benchmarks. For example, on MathVision, the accuracy rises steadily from 18.7% at 1k tokens to 36.8% at 16k tokens, and similar upward trend is also observed on MMMU, indicating that the model is able to utilize longer reasoning chains for better performance. However, not all benchmarks benefit equally from longer thinking lengths. On MathVista, performance saturates early, with accuracy reaching 70.9% at 4k tokens and no further significant gains observed as the token length increases to 16k. It suggests that for this task, the necessary reasoning depth is already captured within a relatively short context, and additional computation does not yield further improvements.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Kimi-VL-A3B-Thinking-2506: From Reasoning Extension to Integrated Thinking Model", "weight": 1.0} -->

While Kimi-VL-A3B-Thinking shows excellent thinking abilities on hard reasoning tasks, we further provide the updated Kimi-VL-A3B-Thinking-2506^∥∥^∥Tech Blog: a new reasoning variant that is not only smarter, but integrates key abilities of Kimi-VL-A3B-Instruct (perception, video, long-document, and OS-agent abilities) into this thinking model.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Kimi-VL-A3B-Thinking-2506: From Reasoning Extension to Integrated Thinking Model", "weight": 1.0} -->

Kimi-VL-Thinking-2506 significantly improves reasoning efficiency while reducing token consumption. As shown in Table, Kimi-VL-Thinking-2506 achieves 56.9% on MathVision (+20.1% improvement on original Kimi-VL-Thinking), 80.1% on MathVista (+8.4%), 46.3% on MMMU-Pro (+3.2%), and 64.0% on MMMU (+2.1%), demonstrating non-trivial gains across multiple reasoning benchmarks. Meanwhile, while solving these hard reasoning problems, the 2506 version reduces the average output token length by around 20% (e.g., 2.9K $\rightarrow$ 2.4K on MMMU-val and 5.8K $\rightarrow$ 4.4K on MathVision), facilitating it to be more efficient and user-friendly for practical deployments.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Kimi-VL-A3B-Thinking-2506: From Reasoning Extension to Integrated Thinking Model", "weight": 1.0} -->

Beyond extensive reasoning tasks, Kimi-VL-Thinking demonstrates stronger visual perception capabilities. Compared to the previous non-thinking variant (Kimi-VL-A3B-Instruct), Kimi-VL-A3B-Thinking-2506 achieves competitive or superior results on general multimodal understanding benchmarks: 84.4% on MMBench-EN-v1.1, 70.4% on MMStar, 70.0% on RealWorldQA, and 78.4% on MMVet, underscoring its broader competence in vision-language tasks. In terms of token efficiency, the 2506 version only requires in average 180 tokens per answer when solving MMBench, 1/3 compared to the previous thinking model while improving 8.4% accuracy.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Kimi-VL-A3B-Thinking-2506: From Reasoning Extension to Integrated Thinking Model", "weight": 1.0} -->

Kimi-VL-A3B-Thinking-2506 also extends its reasoning ability to video and long-context domains. It establishes new state-of-the-art results among open-source models on VideoMMMU (65.2%, 4% better than GPT-4o), a challenging video reasoning benchmark; it also maintains robust general video understanding performance with 71.9% on Video-MME, matching the long video understanding ability of Kimi-VL-A3B-Instruct. It also scores 42.1% (first open-source model matching GPT-4o) on MMLongBench-Doc, a 10% improvement over the previous thinking model and 7% over the previous instruct model, demonstrating its robust ability on broader long-form visual inputs.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Kimi-VL-A3B-Thinking-2506: From Reasoning Extension to Integrated Thinking Model", "weight": 1.0} -->

As mentioned in the method part, the continual training on MoonViT (3.2 million max input pixels) of Kimi-VL-A3B-Thinking-2506 leads to substantial improvements on high-resolution perception and OS grounding benchmarks, achieving 83.2% on V\* Benchmark (without external tools), 52.8% on ScreenSpot-Pro, and 52.5% on OSWorld-G (full set with refusal samples), showing huge improvements over both previous variants. We hope that this high-resolution multimodal reasoning model brings about interesting new capabilities in the real world.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Conclusion, Limitation, and Future Work", "weight": 1.5} -->

We introduce Kimi-VL, a VLM designed with a balanced approach to cover both multimodal and text-only pre-training/post-training, underpinned by an MoE-based architecture for scalable efficiency. Its 128K extended context window enables precise retrieval in lengthy texts and videos, while the native-resolution encoder MoonViT helps maintain high accuracy with low computational overhead in ultra-high-resolution visual tasks. Additionally, Kimi-VL-Thinking facilitates effective long-chain reasoning in complex image and video inference. Overall, Kimi-VL demonstrates robust adaptability and efficiency across multimodal, long-context, and high-resolution tasks, indicating substantial potential for future research and industrial applications.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Conclusion, Limitation, and Future Work", "weight": 1.5} -->

Although the current model size performs effectively for many standard tasks, it remains too limited to address highly specialized or domain-specific problems, or problems that are strongly dependent on language abilities, restricting Kimi-VL's ability to handle extremely complex scenarios.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Conclusion, Limitation, and Future Work", "weight": 1.5} -->

While the reasoning capability is already strong for typical use cases, it has yet to reach its theoretical upper bound, particularly for intricate tasks requiring multi-step inference or deeper contextual understanding.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Conclusion, Limitation, and Future Work", "weight": 1.5} -->

Despite providing a 128K extended context window, due to limited parameters in its attention layers (which is only comparable to a 3B model), its long-context abilities is still insufficient for certain advanced applications that involve extremely long sequences or high-volume contextual information.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Conclusion, Limitation, and Future Work", "weight": 1.5} -->

In the future, we will tackle these challenges by scaling up the model size, expanding pre-training data, and enhancing post-training algorithms. Our next steps include optimizing Kimi-VL and releasing larger versions, as well as refining post-training and test-time scaling mechanisms for a better thinking model. These efforts will pave the way for more advanced applications in both research and industry.
