<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Image Generators Are Generalist Vision Learners

Topics include Image generation, Computer vision, Vision banana, NBP.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent works show that image and video generators exhibit zero-shot visual understanding behaviors, in a way reminiscent of how LLMs develop emergent capabilities of language understanding and reasoning from generative pretraining. While it has long been conjectured that the ability to create visual content implies an ability to understand it, there has been limited evidence that generative vision models have developed strong understanding capabilities. In this work, we demonstrate that image generation training serves a role similar to LLM pretraining, and lets models learn powerful and general visual representations that enable SOTA performance on various vision tasks. We introduce Vision Banana, a generalist model built by instruction-tuning Nano Banana Pro (NBP) on a mixture of its original training data alongside a small amount of vision task data. By parameterizing the output space of vision tasks as RGB images, we seamlessly reframe perception as image generation. Our generalist model, Vision Banana, achieves SOTA results on a variety of vision tasks involving both 2D and 3D understanding, beating or rivaling zero-shot domain-specialists, including Segment Anything Model 3 on segmentation tasks, and the Depth Anything series on metric depth estimation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We show that these results can be achieved with lightweight instruction-tuning without sacrificing the base model's image generation capabilities. The superior results suggest that image generation pretraining is a generalist vision learner. It also shows that image generation serves as a unified and universal interface for vision tasks, similar to text generation's role in language understanding and reasoning. We could be witnessing a major paradigm shift for computer vision, where generative vision pretraining takes a central role in building Foundational Vision Models for both generation and understanding.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, advanced image and video generation models \Google, [2025a, b, Black Forest Labs, 2025, ByteDance, 2026, Luma, 2026, OpenAI, 2026\] have demonstrated unprecedented generation capabilities, synthesizing highly complex, high-fidelity visual context with precise semantic control. This remarkable capability for visual creation suggests that these models possess a deep, internalized comprehension of the visual world's underlying structures, semantics, and relationships. However, leading methods on visual representation learning in general do not belong to the family of generative modeling.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Instead, they include supervised discriminative learning \Krizhevsky et al., [2012, Dehghani et al., 2023, Dosovitskiy et al., 2020\], contrastive learning \Chen et al., [2020b, He et al., 2020, Chen et al., 2020c, Zhai et al., 2023, Tschannen et al., 2025, Radford et al., 2021\], bootstrapping \Caron et al., [2021, Grill et al., 2020\], auto-encoding \He et al., [2022, Bao et al., 2021, Chen et al., 2024\] among others, and their combinations \Oquab et al., [2023, Siméoni et al., 2025, Zhou et al., 2021, Cao et al., 2026\]. Early efforts in generative vision pretraining \Chen et al., [2020a, Bai et al., 2024\] have shown promising scaling behaviors but their effectiveness has lagged behind non-generative models.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we investigate whether visual generative models are secretly generalist vision learners, i.e., whether models trained for image generation develop internal representations that are suitable for visual understanding tasks. To achieve this, we finetune a pretrained image generator with a small amount of computer vision data (depth estimation, surface normal estimation, segmentation, etc.). We then evaluate the resulting model on a wide variety of vision benchmarks. If the finetuned model performs at or near SOTA on these benchmarks, while retaining its image generation capabilities, then there is strong evidence that the image generator was indeed a foundation model for visual understanding -- i.e., a generalist vision learner.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This is not the first paper to study the hidden understanding capabilities of generative models or use image and video generators as base models for visual understanding. Early research efforts show that generative models develop some understanding capabilities hidden in their features \Bhattad et al., [2023, Du et al., 2023, Li et al., 2023, Ranzato et al., 2011, Hjelm et al., 2018, Clark and Jaini, 2023, Baranchuk et al., 2021, Chen et al., 2016, Zhao et al., 2023, Mukhopadhyay et al., 2023, Tang et al., 2023, Zhang et al., 2023b, Li et al., 2024b, Hedlin et al., 2023, Yang and Wang, 2023\]. More recent research observes that state-of-the-art image and video generators can generate visual content that look like RGB visualizations of computer vision outputs for tasks such as segmentation, depth estimation, and surface normal estimation \Zuo et al., [2025, Wiedemer et al., 2025\].

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, those methods do not provide state-of-the-art results on modern benchmarks. This is partially because these models do not strictly follow the prompts to produce vision outputs in the desired formats that can be decoded back to vision outputs for computing quantitative metrics. Other researchers \He et al., [2024, 2025, Ke et al., 2024, Ye et al., 2024, Yu et al., 2024, Zhao et al., 2025, Wang et al., 2026b, Wu et al., 2025, Garcia et al., 2025, Xu et al., 2023\] adapt the generation architectures by adding specialized modules and performing full-finetuning to achieve SOTA-level results on specific target tasks. Although these methods successfully leverage the understanding capabilities of the pre-trained features, they sacrifice the model's generality across other understanding and generation tasks.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We take an approach motivated by recent advancements in large language models (LLMs). In natural language processing (NLP), generative pretraining \Brown et al., [2020, Chowdhery et al., 2023\] is performed to produce base models, often referred to as LLMs, that are good at generating text, whereas instruction-tuning \Ouyang et al., [2022, Wei et al., 2021\] guides them to follow specific tasks and produce text in requested formats and stay on the task. Analogously, we position a visual generative model as a "base" model and perform instruction-tuning to align the model to produce visual output in desired formats, in accordance with the prompts, as illustrated in Fig. 1. Specifically, the model is instructed to produce RGB images that can be decoded to computer vision outputs. Such instruction prompts and decodable visualization schemes are designed to bridge and calibrate the visual generations to formats where measurable metrics for benchmarking can be applied.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

For example, by prompting the model to "Segment the skateboard category in pure yellow (\<255, 255, 0\>)", we can easily parse the mask for skateboard by clustering pixels whose values are close to \<255, 255, 0\>. This strategy has three main advantages. First, it supports a wide variety of tasks with a single unified model -- after instruction tuning, the weights are shared among all tasks, and only the prompt changes. Second, it requires relatively little new training data, since the instruction tuning is solely teaching the model how to format computer vision outputs as RGB. Third, it helps the model retain its original image generation capabilities, since the outputs are simply new RGB images.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Benchmarks and Metrics Referring segmentation: RefCOCOg UMD val (cIoU ↑) Referring segmentation: ReasonSeg val (gIoU ↑) Semantic segmentation: Cityscapes val (mIoU ↑) Instance segmentation: SA-Co/Gold (cgF1 ↑) Metric depth estimation: average of 4 datasets (δ1↑) Surface normal estimation: average of 4 datasets (mean angle error ↓) Text-to-image: GenAI-Bench (win rate against the other ↑) 46.5% (Nano Banana Pro) Image editing: ImgEdit (win rate against the other ↑) 52.2% (Nano Banana Pro) Table 1: The instruction-tuned Vision Banana model surpasses or rivals SOTA specialists across visual generation and understanding. For 2D visual understanding, it beats the highly specialized Segment Anything Model 3 [Carion et al., 2025] on 3 segmentation datasets, and outperforms OWLv2 [Minderer et al., 2023] on instance segmentation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

For 3D visual understanding, it surpasses the best metric depth estimation expert, Depth Anything 3 [Lin et al., 2025], and the best surface normal estimation specialist, Lotus-2 [He et al., 2025]. In visual generation, Vision Banana inherits its capabilities from Nano Banana Pro and is on par with it on text-to-image and image editing.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present Vision Banana, a generalist vision model trained by performing a lightweight instruction-tuning to Nano Banana Pro on a mixture of its original image generation data and our additional vision task data. During evaluation across several benchmarks, we find that Visual Banana excels at both visual understanding and generation, as summarized in Tab. 1. On the understanding side, Vision Banana surpasses or matches state-of-the-art results on both 2D and 3D tasks. For example, it beats the highly specialized segmentation model, SAM 3 \Carion et al. on various segmentation tasks, and the 3D expert, Depth Anything 3 \Lin et al. on metric depth estimation. On the generation side, it performs on par with its base model on image generation and editing benchmarks. On GenAI-Bench \Li et al., [2024a\], Vision Banana scores a $53.5\%$ win rate against its base model. On ImgEdit \Ye et al., for image editing, Vision Banana's win rate is $47.8\%$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since these results are achieved with a single unified model built by a lightweight instruction-tuning on its base model, there is strong evidence that Nano Banana Pro already possessed internal representations for visual understanding, which only needed to be unlocked with instruction tuning.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

The implications of this study are two-fold. First, it suggests that image generators are indeed generalist vision learners under the hood, with generative vision pretraining playing a foundational role similar to language model pretraining. Second, it suggests that image generation can serve as a universal interface for unified visual understanding, mirroring the role of text generation in language understanding and reasoning. We could be witnessing a major paradigm shift for computer vision, where generative vision pretraining takes a central role in building Foundational Vision Models for both generation and understanding.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Instruction-tuning Nano Banana Pro", "weight": 1.0} -->

Recent image and video generators have demonstrated zero-shot capabilities in generating visualizations of visual understanding tasks \Wiedemer et al., [2025, Zuo et al., 2025\]. To rigorously investigate and benchmark these capabilities, we need to align the models to generate visualizations that can be decoded back to visual task outputs for quantitative evaluation. For example, in metric depth estimation, a generated depth heatmap must be invertible back to physical depth values for quantitative assessment. Therefore, we create Vision Banana by instruction-tuning our base model, Nano Banana Pro, on a selection of vision tasks formatted in such invertible manners. Specifically, we mix vision task data into Nano Banana Pro's own training mixture at a very low ratio. This process allows us to align the model's emergent generative representations into measurable physical geometry and semantic labels, allowing our single generalist model to be evaluated and compared against task-specific specialists.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Instruction-tuning Nano Banana Pro", "weight": 1.0} -->

Mixing the vision data at a low ratio serves as a lightweight instruction-tuning strategy, ensuring that our vision task alignment does not degrade the model's original generative priors. This strategy distinguishes our work from previous approaches that perform full fine-tuning on generative models without retaining the image generation data mixture \Gan et al., [2023, Ke et al., 2024, Zhao et al., 2025\]. We validate the preservation of image generation capabilities by benchmarking Vision Banana against the base Nano Banana Pro on two tasks: text-to-image generation and image editing (ImgEdit \Ye et al., ). In human evaluations, we obtain win rates of 53.5% and 47.8% respectively, indicating that Vision Banana successfully maintains the generative power of its base model. We provide a detailed discussion of these generative capabilities in appendix˜D. Qualitative comparisons in fig.˜11 (text-to-image generation) and fig.˜12 (image editing) in the appendix confirm that the outputs remain highly similar between Vision Banana and Nano Banana Pro. These results verify that Vision Banana does not forget its generative nature.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Vision Tasks and Data", "weight": 1.0} -->

We evaluate our framework on two fundamental categories of visual understanding: $2$D scene understanding and $3$D structure inference. The $2$D suite consists of referring expression, semantic, and instance segmentation, which collectively test the model's capability to ground natural language and segment the corresponding objects. For $3$D understanding, we focus on monocular metric depth and surface normal estimation, which demand geometric reasoning and internal knowledge about object scales. To collect data for instruction tuning, we utilize in-house model annotations for web-crawled 2D images, as well as synthetic data from rendering engines for 3D tasks. Crucially, no training data from our evaluation benchmarks is included in the instruction-tuning mixture, ensuring that our results reflect true generalist capability.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Vision Banana - Generalist Vision Model from Image Generator", "weight": 1.0} -->

In this section, we present qualitative and quantitative assessments compared to task-specific specialist models. Built upon an image generator, Vision Banana achieves SOTA-level results across a broad range of visual understanding tasks, without specialized architectures or custom training losses.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Vision Banana - Generalist Vision Model from Image Generator", "weight": 1.0} -->

Non Zero-Shot Transfer Table 2: Semantic segmentation results on Cityscapes val.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Vision Banana - Generalist Vision Model from Image Generator", "weight": 1.0} -->

Non Zero-Shot Transfer SAM 3 [Carion et al., 2025] + Llama 3.2 (ft) Gemini 2.5 [Gemini Team, 2025] Vision Banana + Gemini 3.1 Flash-Lite Table 3: Instance segmentation results on SA-Co/Gold.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Vision Banana - Generalist Vision Model from Image Generator", "weight": 1.0} -->

Non Zero-Shot Transfer HybridGL [Liu and Li, 2025] SAM 3 [Carion et al., 2025] + Gemini 2.5 Pro Table 4: Referring expression segmentation results on RefCOCOg val (UMD).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Vision Banana - Generalist Vision Model from Image Generator", "weight": 1.0} -->

Non Zero-Shot Transfer LISA-13B-LLaVA1.5 [Lai et al., 2024] SegZero-Qwen2.5-VL-7B [Liu et al., 2025] SAM 3 [Carion et al., 2025] + Gemini 2.5 Pro Vision Banana + Gemini 2.5 Pro Table 5: Referring expression segmentation results on ReasonSeg val.

<!-- chunk {"id": "body-0024", "role": "body", "section": "2D Semantic Understanding", "weight": 1.0} -->

Image segmentation stands as a cornerstone of visual understanding, traditionally requiring complex, task-specific models to classify pixels into semantic categories or object instances. Current leading methods such as the Segment Anything series \Kirillov et al., [2023, Ravi et al., 2024, Carion et al., 2025\] tackle this through heavy architectural specialization and large volumes of expensive, human-annotated mask data. Vision Banana challenges this prevailing paradigm by demonstrating that SOTA segmentation can naturally emerge from image generation pretraining. Rather than training on vast amounts of meticulously crafted segmentation examples, we tap into the rich representations learned by the base image generation model. By instructing the model to generate multi-colored images of segmentation masks, we obtain dense segmentation maps from which individual masks can be decoded, therefore enabling segmentation through image generation. As detailed in Tab. 5, 5, 5 and 5, this elegant generative approach outperforms highly tuned specialist models, achieving SOTA zero-shot transfer performance on all evaluated segmentation benchmarks. We compare with other methods that have not been trained on in-domain data, i.e., the training splits of these benchmarks.

<!-- chunk {"id": "body-0025", "role": "body", "section": "2D Semantic Understanding", "weight": 1.0} -->

We denote them as "Zero-Shot Transfer" in the tables. The usage of this term follows Segment Anything \Kirillov et al., and CLIP \Radford et al.,. Non zero-shot transfer methods are marked in gray.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Semantic Segmentation", "weight": 1.0} -->

Semantic segmentation involves classifying each pixel into a predefined category without distinguishing between individual instances. For example, the Cityscapes benchmark \Cordts et al., defines $19$ classes, including road, person, and sky. While instance and referring expression segmentation also convey semantic information, we use the term "semantic segmentation" here strictly in this instance-agnostic, category-level sense. This nature of the classical semantic segmentation task can be specified via a text prompt, and we train the model to follow such instructions. We prompt the model to generate a visualization image where each pixel is colored according to its class, as shown in Fig. 2.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Semantic Segmentation", "weight": 1.0} -->

Crucially, our approach is open-vocabulary: the target categories are not limited to a fixed set and can be specified dynamically in the prompt along with their corresponding color mappings. We support various prompting styles, including natural language descriptions (e.g., "the macaron cakes are represented by yellow") and structured JSON mappings, with colors specified as named colors, hex codes, or RGB tuples. For quantitative evaluation, we post-process the generated image by assigning each pixel to the class whose target color is closest in the RGB space.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Semantic Segmentation", "weight": 1.0} -->

We compare Vision Banana with existing methods on the Cityscapes validation set in table˜5. During evaluation, we use the same text prompt for each example, providing the full class-to-color mapping for the 19 classes, including the ones not present in the image. As shown in table˜5, Vision Banana outperforms SAM 3 by $4.7$ points in mIoU and achieves the best performance among open-vocabulary models, narrowing the gap with closed-set, non-zero-shot specialists like SegMan \Fu et al., [2025b\].

<!-- chunk {"id": "body-0029", "role": "body", "section": "Semantic Segmentation", "weight": 1.0} -->

“Generate a semantic segmentation visualization image, using this color mapping: {"cat": "red", "lock": "pink", "exit sign": "light purple", "background": yellow}.” “Generate a visualization image of semantic segmentation, using this color mapping: {"cat ears": <255, 165, 0>, "exit sign": <0, 0, 255>, "background":<125,0, 125>}” “This image is a per-pixel class labeling of the input. The macaron cakes are represented. The round plates are represented. The slice cakes are depicted. The flowers are shown. The tongs are.” “Generate a semantic segmentation visualization of the input. The menu is #80C000. The dessert is #800000. The patterns on the wall is #40FFC0” Figure 2: Vision Banana can perform semantic segmentation, following the instruction prompts. It handles various prompting styles. It can also segment anything specified via text prompts, from single-word nouns to phrases.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Semantic Segmentation", "weight": 1.0} -->

It is able to produce segmentation masks with fine details, such as the cat whiskers in Example 1 (middle).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Semantic Segmentation", "weight": 1.0} -->

“Generate an instance segmentation visualization of this image. Each piece of garlic is colored differently.” “Generate an instance segmentation visualization of this image. Each piece of beef is colored differently.” “Generate an instance segmentation visualization of this image. Each price tag is colored differently. ” “This image is a segmentation task derived from the input. The "crescent"-shaped croissant instances are each represented by a unique, solid color. Background is RGB.” “This image shows segmentation masks for the basketballs from the input image. The background is set to #10aa05. Each basketball instance is represented by a solid circular mask, and a different colora is used for each mask.” “This image shows segmentation masks for the balls from the input image. The background is set to white color. Each ball is represented by a different color.” Figure 3: Vision Banana can perform instance segmentation, one class at a time. It renders different instances with different colors. It can understand nuanced language concepts as well.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Instance Segmentation", "weight": 1.0} -->

Unlike semantic segmentation, instance segmentation requires the model to distinguish between individual objects that belong to the same class. For example, if an image contains five dogs, we expect the model to produce an individual mask for each animal. This poses a unique challenge for Vision Banana: since the number of instances is unknown a priori, we cannot assign specific colors in the prompt beforehand. To address this challenge, we prompt the model with only the target class and the background color, instructing it to assign a unique, distinct color to each individual instance. We let the model dynamically assign distinct colors to different instances of that class. Qualitative examples are shown in fig.˜3. Individual instance masks can be extracted from the generated RGB images using a multi-stage clustering algorithm, detailed in appendix˜A of the appendix.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Instance Segmentation", "weight": 1.0} -->

We evaluate our model on the open-vocabulary noun-phrase (NP) instance segmentation benchmark SA-Co/Gold \Carion et al.,. We summarize the main results in table˜5 and provide a comprehensive category breakdown in table˜8, appendix˜B of the appendix. We also perform a qualitative evaluation in appendix˜C of the appendix. The SA-Co/Gold benchmark consists of 168k Image-NP pairs, where a large majority are negative queries (i.e., the target NP is absent from the image). While Vision Banana could theoretically handle these negative queries by generating a solid black image, we did not tune the model to generate such empty mask images. We instead defer the task of classifying the Image-NP pairs as positives or negatives to a MLLM. To do so, we prompt Gemini 3.1 Flash-Lite with "Is there an instance of \<NP\> visible in this image? Choose your answer from the following options: (A): Yes, (B): No.". We then only process the positive-predicted examples with Vision Banana to generate an image of the masks.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Instance Segmentation", "weight": 1.0} -->

This approach is related to the \"SAM 3 + Llama 3.2 (ft)\" method, presented as \"SAM 3 + EV\" in Carion et al. where they fine-tuned Llama 3.2 to produce a presence score for SAM 3.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Instance Segmentation", "weight": 1.0} -->

Under the zero-shot transfer setting, Vision Banana (paired with Gemini 3.1 Flash-Lite) achieves state-of-the-art performance, outperforming existing models including Gemini 2.5 \Gemini Team APE-D \Shen et al. DINO-X \Ren et al. and OWLv2 \Minderer et al.,. While Vision Banana still lags behind the SAM 3 specialist on SA-Co/Gold, we emphasize that unlike SAM 3, we did not include the SA-Co dataset in our training data mixture.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Referring Expression Segmentation", "weight": 1.0} -->

Unlike traditional fixed-class segmentation, referring expression segmentation evaluates a model's ability to segment objects described by long, free-form natural language queries. This task requires models to comprehend and reason about nuanced natural language expressions, as well as capture complex relationships between objects. As summarized in tables˜5 and 5, our model achieves state-of-the-art performance under the zero-shot transfer setting, obtaining a cIoU of $73.8\%$ on RefCOCOg UMD \Kazemzadeh et al., and a gIoU of $79.3\%$ on ReasonSeg \Lai et al.,. It consistently outperforms SAM 3 Agent \Carion et al., (which pairs SAM 3 with Gemini 2.5 Pro) and other recent zero-shot methods, including HybridGL \Liu and Li LocalizationHeads \Kang et al. SegZero \Liu et al. and RSVP \Lu et al.,. On RefCOCOg, a performance gap remains compared to methods that are trained on the training split like HyperSeg \Wei et al., and X-SAM \Wang et al., [2026a\].

<!-- chunk {"id": "body-0037", "role": "body", "section": "Referring Expression Segmentation", "weight": 1.0} -->

For the complex reasoning queries in ReasonSeg, we follow standard practice by delegating the reasoning step to a multimodal LLM. Specifically, we utilize Gemini 2.5 Pro to translate the reasoning query into a descriptive reference, which then serves as the prompt for Vision Banana. We evaluate this pipeline in a single-turn inference setup, where both Gemini and Vision Banana are queried exactly once. In this setting, Vision Banana paired with Gemini 2.5 Pro outperforms several non-zero-shot methods that were trained directly on ReasonSeg, including X-SAM \Wang et al., [2026a\] and LISA \Lai et al.,. Qualitative results in fig.˜4 illustrate Vision Banana's ability to ground diverse language cues, from physical actions ("stretching cat") and atypical object roles ("toaster as a game controller") to multilingual text on signage. This highlights a key advantage of our approach: the rich multimodal priors inherited from generative pre-training allow Vision Banana to reason about 'what' to segment more effectively than specialized segmentation models.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Referring Expression Segmentation", "weight": 1.0} -->

Intriguingly, Vision Banana also exhibits strong cross-task transfer by demonstrating a similar grasp of referring expressions combined with standard semantic and instance segmentation tasks, despite not being explicitly trained on free-form queries for those tasks. For example, in Fig. 2(b) ‣ Figure 2 ‣ Semantic Segmentation. ‣ 3.1 2D Semantic Understanding ‣ 3 Vision Banana - Generalist Vision Model from Image Generator ‣ Image Generators are Generalist Vision Learners") (right), the model understands what "patterns on the wall" is referring to. In Fig. 3(b) ‣ Figure 3 ‣ Semantic Segmentation. ‣ 3.1 2D Semantic Understanding ‣ 3 Vision Banana - Generalist Vision Model from Image Generator ‣ Image Generators are Generalist Vision Learners") (right), the model successfully distinguishes crescent-shaped croissants from other variations of croissants. These findings suggest that our generative pre-training yields highly robust, transferable representations across distinct visual grounding paradigms.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Referring Expression Segmentation", "weight": 1.0} -->

A segmentation map image. The area that corresponds to the man in pink t shirt is rendered solid white; the other man is rendered in green.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Referring Expression Segmentation", "weight": 1.0} -->

A segmentation map image. The stretching cat is rendered in green, the cat that is cleaning itself is in cyan.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Referring Expression Segmentation", "weight": 1.0} -->

This image shows segmentation masks from the given image. The background is black color. The game control device is represented by a solid yellow.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Referring Expression Segmentation", "weight": 1.0} -->

This image shows segmentation masks from the given image. The background is black color. The chef’s names in both Chinese and English are rendered as cyan color.

<!-- chunk {"id": "body-0043", "role": "body", "section": "3D Understanding from Monocular Images", "weight": 1.0} -->

Vision Banana demonstrates a strong ability to infer 3D structures from 2D monocular images. We evaluate this capability on two classical tasks: monocular metric depth estimation and surface normal estimation. As summarized in Tab. 1, Vision Banana achieves SOTA performance on both tasks, surpassing specialists such as Depth Anything V3 \Lin et al., and Lotus-2 \He et al.,.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Metric Depth Estimation", "weight": 1.0} -->

The goal of depth estimation is to produce a depth map from a monocular image, where each pixel's value represents the physical metric distance from the camera plane to the observed object \Eigen et al.,. This is a fundamental computer vision task that benefits a wide range of applications such as robotics, augmented/virtual reality, and autonomous driving. However, depth estimation is inherently ill-posed, as 2D projections inherently discard critical 3D geometric information. Furthermore, monocular depth estimation is particularly challenging due to the absence of parallax cues available in multi-view setups, even when camera intrinsic parameters are known.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Metric Depth Estimation", "weight": 1.0} -->

In the deep-learning era, the research community has largely framed depth estimation as a dense per-pixel supervised regression problem, employing specialized architectures and domain-specific loss functions. Most recent SOTA methods rely on camera intrinsics during training, inference, or both \Yang et al., [2024, Bochkovskii et al., 2024, Wang et al., 2025b, c, He et al., 2025, 2024, Hu et al., 2024, Cai et al., 2025, Lin et al., 2025, Piccinelli et al., 2025b, a\]. While using intrinsics mitigates the inherent ambiguity of depth estimation, it also necessitates specialized model designs. In contrast, our work is predicated on the hypothesis that the mode-seeking nature of generative modeling naturally resolves training target ambiguities, thereby eliminating the need for such specialized techniques. Furthermore, the broad world knowledge acquired during pretraining endows the model with stronger priors on object sizes and distances compared to narrowly targeted models.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Metric Depth Estimation", "weight": 1.0} -->

To enable Nano Banana Pro to estimate depth in metric units, we instruct the model to output a carefully constructed false-color visualization of depth values.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Metric Depth Estimation", "weight": 1.0} -->

To visualize depth maps as RGB images, we establish a mapping between unbounded depth values in $[0,\infty)$ and bounded RGB values in $^{3}$. Because the utility of accurate metric depth for nearby image content is generally higher than that of distant content (e.g., graspable objects matter more for robotics tasks, stereo/monodepth benchmarks usually measure accuracy terms of disparity or relative/log-depth) we "curve" metric depth prior to RGB encoding. Specifically, this is achieved by first applying the power transform of Barron to warp the depth values, and then using those curved distances to produce a false-color visualization. We constrain the power transform to $\lambda<-1$ and rescale it to map metric distances $d\in0,\infty)$ to normalized distances in $[0,1)$: In all experiments, we set the shape parameter to $\lambda=-3$ and the scale parameter to $c=\nicefrac{{10}}{{3}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Metric Depth Estimation", "weight": 1.0} -->

These curved and normalized distances $f(d,\lambda,c)$ are then used to interpolate along a piecewise-linear function that follows the edges of the RGB cube, traversing along its edges from black to white, similarly to the first iteration of a 3D Hilbert curve. A visualization of this process is provided in Fig. [5.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Metric Depth Estimation", "weight": 1.0} -->

This mapping from normalized distance to RGB color can be inverted by simply projecting the RGB values onto the nearest line segment and then inverting the linear interpolation along the cube's edges. Because both the false-color visualization and the power transform are strictly invertible, their composition forms a bijection between metric depth in $[0,\infty]$ and RGB space in $^{3}$. During training, we apply this mapping to ground-truth metric depths to generate RGB training targets. At inference, we apply the inverse mapping to decode the model's generated RGB images back into metric depth, enabling direction evaluation on standard depth benchmarks. To enhance the model's robustness across diverse color representations, we augment our training data with alternative color maps, such as Plasma, Inferno, Viridis, and grayscale.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Metric Depth Estimation", "weight": 1.0} -->

Depth Any. v3 [Lin et al., 2025] Depth Pro [Bochkovskii et al., 2024]

<!-- chunk {"id": "body-0051", "role": "body", "section": "Metric Depth Estimation", "weight": 1.0} -->

* The average δ1 of DepthLM-7B on the 4 datasets it evaluated on (NYU + iBims1 + ETH3D + nuScenes) is 0.855; our average δ1 on the same 4 datasets is 0.865. The average δ1 of Depth-Anything V3 on the 4 datasets it evaluated on (NYU + ETH3D + DIODE + KITTI) is 0.918; our average δ1 on the same 4 datasets is 0.929. † DepthLM is trained on nuScenes so it’s not zero-shot. ‡ Numbers reported by Depth-Anything V3 [Lin et al., 2025]. Table 6: Monocular metric depth estimation under the zero-shot transfer setting. Vision Banana achieves superior results on public datasets without using camera intrinsics in neither training of inference. Metrics marked with ↑ are better if higher; metrics marked with ↓ are better if lower.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Metric Depth Estimation", "weight": 1.0} -->

Tab. 6 presents the empirical results of Vision Banana compared to specialist models across six major academic benchmarks. Vision Banana achieves an average $\delta_{1}$ accuracy of 0.882, outperforming Unik3D \Piccinelli et al., [2025a\] by nearly 6 points, while achieving a 20% lower absolute relative error (AbsRel) compared to MoGe-2 \Wang et al., [2025c\]. Notably, Vision Banana outperforms Depth Anything V3 \Lin et al., on average across the four datasets (NYU, ETH3D, DIODE, KITTI) on which it was evaluated ($0.929$ v.s. $0.918$), demonstrating robust performance in both near-field and distant scenes. Our model is trained entirely on synthetic depth data created from simulation engines --- we use zero real-world depth data, and exclude training data from any of the depth datasets we evaluate. Note that this result is achieved without relying on camera parameters (neither intrinsics nor extrinsics) during *both* training or inference.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Metric Depth Estimation", "weight": 1.0} -->

By leveraging the immense geometric priors embedded in its foundation model, Vision Banana infers absolute scale solely from visual cues and object relationships, enabling zero-shot generalization to any arbitrary input image.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Metric Depth Estimation", "weight": 1.0} -->

Generated depth image Figure 6: Demonstration of Vision Banana’s metric depth estimation capabilities. The two columns to the left are the input images and the depth visualization image generated by Vision Banana. The depth images are then decoded back to metric depth values. Combining them with the camera intrinsics, we can reconstruct the 3D scene accurately. The two columns on the right are random views of the reconstructed scenes. Note that camera intrinsics are not needed in predicting the depth itself. Samples taken from NYU v2 [Silberman et al., 2012] and ETH 3D [Schops et al., 2019].

<!-- chunk {"id": "body-0055", "role": "body", "section": "Metric Depth Estimation", "weight": 1.0} -->

(a) Photo taken at Kinkaku-Ji (b) Vision Banana estimated depth (c) Measurement from Google Maps Figure 7: Vision Banana depth estimation in the wild. (a) Author of this paper takes a picture near Kinkaku-Ji with a consumer cell-phone. (b) Vision Banana generates a depth estimation image. The depth value at the position marked by a green star is decoded to be 13.71 meters. (c) Author then measures the actual distance using Google Map, which turns out to be 12.87 meters. The AbsRel error at this point is around 0.065.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Metric Depth Estimation", "weight": 1.0} -->

Qualitative inspections further validate the model's capabilities. As illustrated in Fig. 6, Vision Banana generates highly precise depth maps that preserve crisp geometric details, even in cluttered environments like classrooms. When these 2D predictions are unprojected into 3D point clouds, they exhibit global consistency across diverse scenes, maintaining accurate planar surfaces and correct geometry. In addition to common academic benchmarks, we also conducted a "vibe test" using a casual smartphone photograph, as shown in Fig. 7. Crossed validated by depth measured on Google Maps, Vision Banana successfully produced an accurate depth estimation on this photo captured by a consumer device unseen during training.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Surface Normal Estimation", "weight": 1.0} -->

Surface normal estimation represents another critical vision task. Surface normals, which are unit vectors $(x,y,z)$ with values ranging from $-1.0$ to $1.0$, serve as a critical proxy for local geometry and scene structures. Unlike the complex color mapping required for metric depth, the visualization of surface normals is intrinsically aligned with the RGB color space, allowing straightforward integration into our model.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Surface Normal Estimation", "weight": 1.0} -->

We specifically utilize a camera-space normal formulation using the standard right-handed coordinate system (+x right, +y up, +z pointing out of the image plane). In this representation, the directional vector components map directly to RGB channels, i.e. $R=trunc((1-x)/2,min=0,max=1)\times 255$, $G=trunc((1+y)/2,min=0,max=1)\times 255$, $B=trunc((1+z)/2,min=0,max=1)\times 255$: Facing Left $(-1,0,0)$: Encoded as Pinkish Red.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Surface Normal Estimation", "weight": 1.0} -->

Facing the Camera $$: Encoded as Light Blue.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Surface Normal Estimation", "weight": 1.0} -->

Table 7 compares Vision Banana against SOTA specialist methods on four public benchmarks. When averaged across the three indoor datasets, Vision Banana achieves the lowest mean and median angular errors. It also demonstrates competitive accuracy on outdoor scenes.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Surface Normal Estimation", "weight": 1.0} -->

DSINE [Bae and Davison, 2024] Table 7: Surface normal estimation results. Vision Banana achieves the lowest mean and median angle errors on the indoor datasets on average, and is on par with previous SOTA on outdoor scenes.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Image Generators are Generalist Vision Learners", "weight": 1.0} -->

Generative pretraining \Radford et al., [2018, 2019, Brown et al., 2020\] has fundamentally transformed language understanding and reasoning. In the meantime, recent observations of emergent vision capabilities \Wiedemer et al., [2025, Zuo et al., 2025\] have ignited speculation that computer vision is approaching a similar paradigm shift. By instruction-tuning a leading image generator, Nano Banana Pro, into a state-of-the-art visual generation and understanding model, we confirm that this shift is already underway. Models pretrained on large-scale image generation naturally acquire robust visual understanding capabilities. These generative priors surpass the specialized architectures and dedicated training paradigms traditionally employed by specialist vision models. We are witnessing a paradigm shift for computer vision that will be fueled by generative vision pretraining, which we believe paves the way for true Foundational Vision Models and Artificial General Intelligence from Vision (AGI-V).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Image Generation as a Universal Interface", "weight": 1.0} -->

As a byproduct of this study, we show that image generation can serve as the universal interface for computer vision, analogous to how text generation acts as the unifying interface for many tasks embedded in natural language, including language understanding, generation, reasoning, math, coding, agentic tasks, etc.. By representing vision task outputs as RGB images, we can use natural language prompts to seamlessly instruct the model. While we are not the first to encode vision outputs as RGB \Ke et al., [2024, Zhao et al., 2025, Gan et al., 2023, Wang et al., 2023, Lu et al., 2022, 2024, Xie et al., 2024, Inclusion AI, 2025\], we demonstrate that when combined with powerful pretrained visual generators, this simple design is sufficient to outperform modern domain-specific specialist models.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Image Generation as a Universal Interface", "weight": 1.0} -->

In addition to the unification of vision task outputs as RGB images, generative modeling naturally provides a workaround for the ambiguity in vision tasks where a single input can correspond to several modes of the output distribution. In order to prevent the collapse of the output to a blurry mean, expert discriminative models \Carion et al., [2025, Lin et al., 2025\] usually resort to custom architectures and training losses. For example, the Segment Anything models \Kirillov et al., [2023, Ravi et al., 2024, Carion et al., 2025\] return several segmentation masks but only apply the loss to a single one. Generative models, however, inherently learn the full data distribution, gracefully managing ambiguity by design. By eliminating the need for bespoke architectural designs, this formulation could lead to a truly unified "omni" multimodal model.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Future Work", "weight": 1.5} -->

While Vision Banana achieves SOTA results on fundamental tasks for 2D semantic understanding and 3D understanding from monocular images, several exciting avenues remain for future exploration. First, scaling the diversity of instruction-tuned tasks may unlock further emergent cross-task generalization, similar to behaviors observed in LLMs \Wei et al.,. Second, our current evaluation focuses on monocular image inputs. In the future, we can extend this framework to process multi-view inputs \Wang et al., [2025a\] and video inputs \Zhang et al.,. Similarly, investigating whether video generators yield even richer, temporally-aware visual representations presents a highly promising research direction. Another important next step is exploring the synergistic integration of foundational vision models with large language models to enhance cross-modality reasoning. Finally, utilizing image generators like Nano Banana Pro currently incurs a significantly higher computational overhead than running lightweight specialist models. Developing acceleration and cost-reduction strategies will be an essential hurdle to overcome for the deployment of generative vision framework.
