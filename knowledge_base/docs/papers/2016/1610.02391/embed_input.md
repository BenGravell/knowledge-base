<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization

Topics include Reinforcement learning, Robustness, Convolutional networks, Attention mechanisms, Classification, Datasets, Generalization, Learning, Grad-CAM, Visual question answering, Question answering.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a technique for producing "visual explanations" for decisions from a large class of CNN-based models, making them more transparent. Our approach - Gradient-weighted Class Activation Mapping (Grad-CAM), uses the gradients of any target concept, flowing into the final convolutional layer to produce a coarse localization map highlighting important regions in the image for predicting the concept. Grad-CAM is applicable to a wide variety of CNN model-families: CNNs with fully-connected layers, CNNs used for structured outputs, CNNs used in tasks with multimodal inputs or reinforcement learning, without any architectural changes or re-training. We combine Grad-CAM with fine-grained visualizations to create a high-resolution class-discriminative visualization and apply it to off-the-shelf image classification, captioning, and visual question answering (VQA) models, including ResNet-based architectures.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In the context of image classification models, our visualizations (a) lend insights into their failure modes, (b) are robust to adversarial images, (c) outperform previous methods on localization, (d) are more faithful to the underlying model and (e) help achieve generalization by identifying dataset bias. For captioning and VQA, we show that even non-attention based models can localize inputs. We devise a way to identify important neurons through Grad-CAM and combine it with neuron names to provide textual explanations for model decisions. Finally, we design and conduct human studies to measure if Grad-CAM helps users establish appropriate trust in predictions from models and show that Grad-CAM helps untrained users successfully discern a 'stronger' nodel from a 'weaker' one even when both make identical predictions. Our code is available at along with a demo at and a video at youtu.be/COjUB9Izk6E.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep neural models based on Convolutional Neural Networks (CNNs) have enabled unprecedented breakthroughs in a variety of computer vision tasks, from image classification krizhevsky_nips12; he_cvpr15, object detection girshick2014rcnn, semantic segmentation long2015fcn to image captioning vinyals_cvpr15; chen2015microsoft; fang2015captions; johnson_cvpr16, visual question answering antol2015vqa; gao2015you; malinowski_iccv15; ren_nips15 and more recently, visual dialog visdial; guesswhat; visdial_rl and embodied question answering embodiedqa; gordon2017iqa. While these models enable superior performance, their lack of decomposability into *individually intuitive* components makes them hard to interpret lipton_arxiv16. Consequently, when today's intelligent systems fail, they often fail spectacularly disgracefully without warning or explanation, leaving a user staring at an incoherent output, wondering why the system did what it did.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Interpretability matters.* In order to build trust in intelligent systems and move towards their meaningful integration into our everyday lives, it is clear that we must build 'transparent' models that have the ability to explain *why they predict what they predict*. Broadly speaking, this transparency and ability to explain is useful at three different stages of Artificial Intelligence (AI) evolution. First, when AI is significantly weaker than humans and not yet reliably deployable (*e.g*. visual question answering antol2015vqa ), the goal of transparency and explanations is to identify the failure modes agrawal2016analyzing; hoiem2012diagnosing, thereby helping researchers focus their efforts on the most fruitful research directions. Second, when AI is on par with humans and reliably deployable (*e.g*., image classification karpathy_imagenet trained on sufficient data), the goal is to establish appropriate trust and confidence in users. Third, when AI is significantly stronger than humans (*e.g*.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

chess or Go silver2016mastering ), the goal of explanations is in machine teaching JohnsCVPR2015 -- *i.e*., a machine teaching a human about how to make better decisions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

(b) Guided Backprop ‘Cat’ (d) Guided Grad-CAM ‘Cat’ (e) Occlusion map ‘Cat’ (f) ResNet Grad-CAM ‘Cat’ (h) Guided Backprop ‘Dog’ (j) Guided Grad-CAM ‘Dog’ (k) Occlusion map ‘Dog’ (l) ResNet Grad-CAM ‘Dog’ Figure 1: (a) Original image with a cat and a dog. (b-f) Support for the cat category according to various visualizations for VGG-16 and ResNet. (b) Guided Backpropagation springenberg_arxiv14: highlights all contributing features. (c, f) Grad-CAM (Ours): localizes class-discriminative regions, (d) Combining (b) and (c) gives Guided Grad-CAM, which gives high-resolution class-discriminative visualizations. Interestingly, the localizations achieved by our Grad-CAM technique, (c) are very similar to results from occlusion sensitivity (e), while being orders of magnitude cheaper to compute.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

(f, l) are Grad-CAM visualizations for ResNet-18 layer. Note that in (c, f, i, l), red regions corresponds to high score for class, while in (e, k), blue corresponds to evidence for the class. Figure best viewed in color.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

There typically exists a trade-off between accuracy and simplicity or interpretability. Classical rule-based or expert systems jackson_expertsys are highly interpretable but not very accurate (or robust). Decomposable pipelines where each stage is hand-designed are thought to be more interpretable as each individual component assumes a natural intuitive explanation. By using deep models, we sacrifice interpretable modules for uninterpretable ones that achieve greater performance through greater abstraction (more layers) and tighter integration (end-to-end training). Recently introduced deep residual networks (ResNets) he_cvpr15 are over 200-layers deep and have shown state-of-the-art performance in several challenging tasks. Such complexity makes these models hard to interpret. As such, deep models are beginning to explore the spectrum between interpretability and accuracy.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Zhou *et al*. zhou_cvpr16 recently proposed a technique called Class Activation Mapping (CAM) for identifying discriminative regions used by a restricted class of image classification CNNs which do not contain any fully-connected layers. In essence, this work trades off model complexity and performance for more transparency into the working of the model. In contrast, we make existing state-of-the-art deep models interpretable without altering their architecture, thus avoiding the interpretability *vs*. accuracy trade-off. Our approach is a generalization of CAM zhou_cvpr16 and is applicable to a significantly broader range of CNN model families: CNNs with fully-connected layers (*e.g*. VGG), CNNs used for structured outputs (*e.g*. captioning), CNNs used in tasks with multi-modal inputs (*e.g*. VQA) or reinforcement learning, without requiring architectural changes or re-training.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

What makes a good visual explanation? Consider image classification imagenet_cvpr09 -- a 'good' visual explanation from the model for justifying any target category should be (a) class-discriminative (*i.e*. localize the category in the image) and (b) high-resolution (*i.e*. capture fine-grained detail).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fig. 1 shows outputs from a number of visualizations for the 'tiger cat' class (top) and 'boxer' (dog) class (bottom). Pixel-space gradient visualizations such as Guided Backpropagation springenberg_arxiv14 and Deconvolution zeiler_eccv14 are high-resolution and highlight fine-grained details in the image, but are not class-discriminative (Fig. 1(b) and Fig. 1(h) are very similar).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, localization approaches like CAM or our proposed method Gradient-weighted Class Activation Mapping (Grad-CAM), are highly class-discriminative (the 'cat' explanation exclusively highlights the 'cat' regions but not 'dog' regions in Fig. 1(c), and vice versa in Fig. 1(i)).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to combine the best of both worlds, we show that it is possible to fuse existing pixel-space gradient visualizations with Grad-CAM to create Guided Grad-CAM visualizations that are both high-resolution and class-discriminative. As a result, important regions of the image which correspond to any decision of interest are visualized in high-resolution detail even if the image contains evidence for multiple possible concepts, as shown in Figures 1d and 1j. When visualized for 'tiger cat', Guided Grad-CAM not only highlights the cat regions, but also highlights the stripes on the cat, which is important for predicting that particular variety of cat.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

To summarize, our contributions are as follows: \(1\) We introduce Grad-CAM, a class-discriminative localization technique that generates visual explanations for *any* CNN-based network without requiring architectural changes or re-training. We evaluate Grad-CAM for localization (Sec. 4.1), and faithfulness to model (Sec. 5.3), where it outperforms baselines.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

\(2\) We apply Grad-CAM to existing top-performing classification, captioning (Sec. 8.1), and VQA (Sec. 8.2) models. For image classification, our visualizations lend insight into failures of current CNNs (Sec. 6.1), showing that seemingly unreasonable predictions have reasonable explanations. For captioning and VQA, our visualizations expose that common CNN + LSTM models are often surprisingly good at localizing discriminative image regions despite not being trained on grounded image-text pairs.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

\(3\) We show a proof-of-concept of how interpretable Grad-CAM visualizations help in diagnosing failure modes by uncovering biases in datasets. This is important not just for generalization, but also for fair and bias-free outcomes as more and more decisions are made by algorithms in society.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

\(4\) We present Grad-CAM visualizations for ResNets he_cvpr15 applied to image classification and VQA (Sec. 8.2).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

\(5\) We use neuron importance from Grad-CAM and neuron names from netdissect and obtain textual explanations for model decisions (Sec. 7).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

\(6\) We conduct human studies (Sec. 5) that show Guided Grad-CAM explanations are class-discriminative and not only help humans establish trust, but also help untrained users successfully discern a 'stronger' network from a 'weaker' one, *even when both make identical predictions.* Paper Organization: The rest of the paper is organized as follows. In section 3 we propose our approach Grad-CAM and Guided Grad-CAM. In sections 4 and 5 we evaluate the localization ability, class-discriminativeness, trustworthyness and faithfulness of Grad-CAM. In section 6 we show certain use cases of Grad-CAM such as diagnosing image classification CNNs and identifying biases in datasets. In section 7 we provide a way to obtain textual explanations with Grad-CAM. In section 8 we show how Grad-CAM can be applied to vision and language models -- image captioning and Visual Question Answering (VQA).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Grad-CAM", "weight": 1.0} -->

A number of previous works have asserted that deeper representations in a CNN capture higher-level visual constructs bengio2013representation; mahendran2016visualizing. Furthermore, convolutional layers naturally retain spatial information which is lost in fully-connected layers, so we can expect the last convolutional layers to have the best compromise between high-level semantics and detailed spatial information. The neurons in these layers look for semantic class-specific information in the image (say object parts). Grad-CAM uses the gradient information flowing into the last convolutional layer of the CNN to assign importance values to each neuron for a particular decision of interest. Although our technique is fairly general in that it can be used to explain activations in any layer of a deep network, in this work, we focus on explaining output layer decisions only.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Grad-CAM", "weight": 1.0} -->

As shown in Fig. 2, in order to obtain the class-discriminative localization map Grad-CAM $L_{\text{Grad-CAM}}^{c}$ $\in {\mathbb{R}}^{u \times v}$ of width $u$ and height $v$ for any class $c$, we first compute the gradient of the score for class $c$, $y^{c}$ (before the softmax), with respect to feature map activations $A^{k}$ of a convolutional layer, *i.e*. $\frac{\partial y^{c}}{\partial A^{k}}$. These gradients flowing back are global-average-pooled ^22^2Empirically we found global-average-pooling to work better than global-max-pooling as can be found in the Appendix.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Grad-CAM", "weight": 1.0} -->

over the width and height dimensions (indexed by $i$ and $j$ respectively) to obtain the neuron importance weights $\alpha_{k}^{c}$: {ceqn} During computation of $\alpha_{k}^{c}$ while backpropagating gradients with respect to activations, the exact computation amounts to successive matrix products of the weight matrices and the gradient with respect to activation functions till the final convolution layer that the gradients are being propagated to. Hence, this weight $\alpha_{k}^{c}$ represents a *partial linearization* of the deep network downstream from A, and captures the 'importance' of feature map $k$ for a target class $c$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Grad-CAM", "weight": 1.0} -->

We perform a weighted combination of forward activation maps, and follow it by a ReLU to obtain, {ceqn} Notice that this results in a coarse heatmap of the same size as the convolutional feature maps ($14 \times 14$ in the case of last convolutional layers of VGG simonyan_arxiv14 and AlexNet krizhevsky_nips12 networks) ^33^3We find that Grad-CAM maps become progressively worse as we move to earlier convolutional layers as they have smaller receptive fields and only focus on less semantic local features.. We apply a ReLU to the linear combination of maps because we are only interested in the features that have a *positive* influence on the class of interest, *i.e*. pixels whose intensity should be *increased* in order to increase $y^{c}$. Negative pixels are likely to belong to other categories in the image. As expected, without this ReLU, localization maps sometimes highlight more than just the desired class and perform worse at localization.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Grad-CAM", "weight": 1.0} -->

Figures 1c, 1f and 1i, 1l show Grad-CAM visualizations for 'tiger cat' and 'boxer (dog)' respectively. Ablation studies are available in Sec. B.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Grad-CAM", "weight": 1.0} -->

In general, $y^{c}$ need not be the class score produced by an image classification CNN. It could be any differentiable activation including words from a caption or answer to a question.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Grad-CAM generalizes CAM", "weight": 1.0} -->

In this section, we discuss the connections between Grad-CAM and Class Activation Mapping (CAM) zhou_cvpr16, and formally prove that Grad-CAM generalizes CAM for a wide variety of CNN-based architectures. Recall that CAM produces a localization map for an image classification CNN with a specific kind of architecture where global average pooled convolutional feature maps are fed directly into softmax. Specifically, let the penultimate layer produce $K$ feature maps, $A^{k} \in {\mathbb{R}}^{u \times v}$, with each element indexed by $i,j$. So $A_{ij}^{k}$ refers to the activation at location $(i,j)$ of the feature map $A^{k}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Grad-CAM generalizes CAM", "weight": 1.0} -->

These feature maps are then spatially pooled using Global Average Pooling (GAP) and linearly transformed to produce a score $Y^{c}$ for each class $c$, {ceqn} Let us define $F^{k}$ to be the global average pooled output, {ceqn} CAM computes the final scores, {ceqn} where $w_{k}^{c}$ is the weight connecting the $k^{th}$ feature map with the $c^{th}$ class. Taking the gradient of the score for class c ($Y^{c}$) with respect to the feature map $F^{k}$ we get, {ceqn} Taking partial derivative of w.r.t. $A_{ij}^{k}$, we can see that $\frac{\partial F^{k}}{\partial A_{ij}^{k}} = \frac{1}{Z}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Grad-CAM generalizes CAM", "weight": 1.0} -->

Substituting this, we get, {ceqn} From we get that, $\frac{\partial Y^{c}}{\partial F^{k}} = w_{k}^{c}$. Hence, Summing both sides of over all pixels $(i,j)$, Since $Z$ and $w_{k}^{c}$ do not depend on $(i,j)$, rewriting this as Note that $Z$ is the number of pixels in the feature map (or $Z = {\sum_{i}{\sum_{j}\mathbf{1}}}$). Thus, we can re-order terms and see that Up to a proportionality constant ($1/Z$) that gets normalized-out during visualization, the expression for $w_{k}^{c}$ is identical to $\alpha_{k}^{c}$ used by Grad-CAM. Thus, Grad-CAM is a strict generalization of CAM.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Grad-CAM generalizes CAM", "weight": 1.0} -->

This generalization allows us to generate visual explanations from CNN-based models that cascade convolutional layers with much more complex interactions, such as those for image captioning and VQA (Sec. 8.2).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Guided Grad-CAM", "weight": 1.0} -->

While Grad-CAM is class-discriminative and localizes relevant image regions, it lacks the ability to highlight fine-grained details like pixel-space gradient visualization methods (Guided Backpropagation springenberg_arxiv14, Deconvolution zeiler_eccv14 ). Guided Backpropagation visualizes gradients with respect to the image where negative gradients are suppressed when backpropagating through ReLU layers. Intuitively, this aims to capture pixels detected by neurons, not the ones that suppress neurons. See Figure 1c, where Grad-CAM can easily localize the cat; however, it is unclear from the coarse heatmap why the network predicts this particular instance as 'tiger cat'. In order to combine the best aspects of both, we fuse Guided Backpropagation and Grad-CAM visualizations via element-wise multiplication ($L_{\text{Grad-CAM}}^{c}$ is first upsampled to the input image resolution using bilinear interpolation). Fig. 2 bottom-left illustrates this fusion.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Guided Grad-CAM", "weight": 1.0} -->

This visualization is both high-resolution (when the class of interest is 'tiger cat', it identifies important 'tiger cat' features like stripes, pointy ears and eyes) and class-discriminative (it highlights the 'tiger cat' but not the 'boxer (dog)'). Replacing Guided Backpropagation with Deconvolution gives similar results, but we found Deconvolution visualizations to have artifacts and Guided Backpropagation to be generally less noisy.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Counterfactual Explanations", "weight": 1.0} -->

Using a slight modification to Grad-CAM, we can obtain explanations that highlight support for regions that would make the network change its prediction. As a consequence, removing concepts occurring in those regions would make the model more confident about its prediction. We refer to this explanation modality as counterfactual explanations.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Counterfactual Explanations", "weight": 1.0} -->

Specifically, we negate the gradient of $y^{c}$ (score for class $c$) with respect to feature maps $A$ of a convolutional layer. Thus the importance weights $\alpha_{k}^{c}$ now become {ceqn} As, we take a weighted sum of the forward activation maps, $A$, with weights $\alpha_{k}^{c}$, and follow it by a ReLU to obtain counterfactual explanations as shown in Fig. 3.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Counterfactual Explanations", "weight": 1.0} -->

(b) Cat Counterfactual exp (c) Dog Counterfactual exp Figure 3: Counterfactual Explanations with Grad-CAM

<!-- chunk {"id": "body-0036", "role": "body", "section": "Weakly-supervised Localization", "weight": 1.0} -->

In this section, we evaluate the localization capability of Grad-CAM in the context of image classification. The ImageNet localization challenge imagenet_cvpr09 requires approaches to provide bounding boxes in addition to classification labels. Similar to classification, evaluation is performed for both the top-1 and top-5 predicted categories.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Weakly-supervised Localization", "weight": 1.0} -->

Given an image, we first obtain class predictions from our network and then generate Grad-CAM maps for each of the predicted classes and binarize them with a threshold of 15% of the max intensity. This results in connected segments of pixels and we draw a bounding box around the single largest segment. Note that this is weakly-supervised localization -- the models were never exposed to bounding box annotations during training.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Weakly-supervised Localization", "weight": 1.0} -->

We evaluate Grad-CAM localization with off-the-shelf pretrained VGG-16 simonyan_arxiv14, AlexNet krizhevsky_nips12 and GoogleNet szegedy2016rethinking (obtained from the Caffe jia2014caffe Zoo). Following ILSVRC-15 evaluation, we report both top-1 and top-5 localization errors on the val set in Table. 1. Grad-CAM localization errors are significantly better than those achieved by c-MWP zhang2016top and Simonyan *et al*. simonyan_arxiv13, which use grab-cut to post-process image space gradients into heat maps. Grad-CAM for VGG-16 also achieves better top-1 localization error than CAM zhou_cvpr16, which requires a change in the model architecture, necessitates re-training and thereby achieves worse classification errors (2.98% worse top-1), while Grad-CAM does not compromise on classification performance.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Weakly-supervised Localization", "weight": 1.0} -->

Backprop simonyan_arxiv13 c-MWP zhang2016top CAM zhou_cvpr16 c-MWP zhang2016top CAM zhou_cvpr16 Table 1: Classification and localization error % on ILSVRC-15 val (lower is better) for VGG-16, AlexNet and GoogleNet. We see that Grad-CAM achieves superior localization errors without compromising on classification performance.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Weakly-supervised Segmentation", "weight": 1.0} -->

Semantic segmentation involves the task of assigning each pixel in the image an object class (or background class). Being a challenging task, this requires expensive pixel-level annotation. The task of weakly-supervised segmentation involves segmenting objects with just image-level annotation, which can be obtained relatively cheaply from image classification datasets. In recent work, Kolesnikov *et al*. seed_eccv16 introduced a new loss function for training weakly-supervised image segmentation models. Their loss function is based on three principles -- 1) to seed with weak localization cues, encouraging segmentation network to match these cues, 2) to expand object seeds to regions of reasonable size based on information about which classes can occur in an image, 3) to constrain segmentations to object boundaries that alleviates the problem of imprecise boundaries already at training time. They showed that their proposed loss function, consisting of the above three losses leads to better segmentation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Weakly-supervised Segmentation", "weight": 1.0} -->

However, their algorithm is sensitive to the choice of weak localization seed, without which the network fails to localize objects correctly. In their work, they used CAM maps from a VGG-16 based network which are used as object seeds for weakly localizing foreground classes. We replaced the CAM maps with Grad-CAM obtained from a standard VGG-16 network and obtain a Intersection over Union (IoU) score of 49.6 (compared to 44.6 obtained with CAM) on the PASCAL VOC 2012 segmentation task. Fig. 4 shows some qualitative results.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Weakly-supervised Segmentation", "weight": 1.0} -->

(b) AMT interface for evaluating the class-discriminative property (c) AMT interface for evaluating if our visualizations instill trust in an end user (a) Raw input image. Note that this is not a part of the tasks (b) and (c) Figure 5: AMT interfaces for evaluating different visualizations for class discrimination (b) and trustworthiness (c). Guided Grad-CAM outperforms baseline approaches (Guided-backprop and Deconvolution) showing that our visualizations are more class-discriminative and help humans place trust in a more accurate classifier.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Pointing Game", "weight": 1.0} -->

Zhang *et al*. zhang2016top introduced the Pointing Game experiment to evaluate the discriminativeness of different visualization methods for localizing target objects in scenes. Their evaluation protocol first cues each visualization technique with the ground-truth object label and extracts the maximally activated point on the generated heatmap. It then evaluates if the point lies within one of the annotated instances of the target object category, thereby counting it as a hit or a miss.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Pointing Game", "weight": 1.0} -->

The localization accuracy is then calculated as\${Acc} = \frac{\#Hits}{{\#Hits} + {\#Misses}}$. However, this evaluation only measures precision of the visualization technique. We modify the protocol to also measure recall -- we compute localization maps for top-5 class predictions from the CNN classifiers^44^4We use GoogLeNet finetuned on COCO, as provided by zhang2016top. and evaluate them using the pointing game setup with an additional option to reject any of the top-5 predictions from the model if the maximally activated point in the map is below a threshold, *i.e*. if the visualization correctly rejects the predictions which are absent from the ground-truth categories, it gets that as a hit. We find that Grad-CAM outperforms c-MWP zhang2016top by a significant margin (70.58% *vs*. 60.30%).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Pointing Game", "weight": 1.0} -->

Qualitative examples comparing c-MWP zhang2016top and Grad-CAM on can be found in Sec. D^55^5 c-MWP zhang2016top highlights arbitrary regions for predicted but non-existent categories, unlike Grad-CAM maps which typically do not..

<!-- chunk {"id": "body-0046", "role": "body", "section": "Evaluating Visualizations", "weight": 1.0} -->

In this section, we describe the human studies and experiments we conducted to understand the interpretability *vs*. faithfulness tradeoff of our approach to model predictions. Our first human study evaluates the main premise of our approach -- are Grad-CAM visualizations more class discriminative than previous techniques? Having established that, we turn to understanding whether it can lead an end user to trust the visualized models appropriately. For these experiments, we compare VGG-16 and AlexNet finetuned on PASCAL VOC 2007 train and visualizations evaluated on val.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Evaluating Class Discrimination", "weight": 1.0} -->

In order to measure whether Grad-CAM helps distinguish between classes, we select images from the PASCAL VOC 2007 val set, which contain exactly $2$ annotated categories and create visualizations for each one of them. For both VGG-16 and AlexNet CNNs, we obtain category-specific visualizations using four techniques: Deconvolution, Guided Backpropagation, and Grad-CAM versions of each of these methods (Deconvolution Grad-CAM and Guided Grad-CAM). We show these visualizations to 43 workers on Amazon Mechanical Turk (AMT) and ask them "Which of the two object categories is depicted in the image?" (shown in Fig. 5(a)).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Evaluating Class Discrimination", "weight": 1.0} -->

Intuitively, a good prediction explanation is one that produces discriminative visualizations for the class of interest. The experiment was conducted using all 4 visualizations for 90 image-category pairs (*i.e*. 360 visualizations); 9 ratings were collected for each image, evaluated against the ground truth and averaged to obtain the accuracy in Table. 2. When viewing Guided Grad-CAM, human subjects can correctly identify the category being visualized in $61.23$% of cases (compared to $44.44$% for Guided Backpropagation; thus, Grad-CAM improves human performance by $16.79$%). Similarly, we also find that Grad-CAM helps make Deconvolution more class-discriminative (from $53.33$% $\rightarrow$ $60.37$%). Guided Grad-CAM performs the best among all methods. Interestingly, our results indicate that Deconvolution is more class-discriminative than Guided Backpropagation ($53.33$% *vs*. $44.44$%), although Guided Backpropagation is more aesthetically pleasing.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Evaluating Class Discrimination", "weight": 1.0} -->

To the best of our knowledge, our evaluations are the first to quantify this subtle difference.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Evaluating Class Discrimination", "weight": 1.0} -->

Human Classification Accuracy Rank Correlation w/ Occlusion Table 2: Quantitative Visualization Evaluation. Guided Grad-CAM enables humans to differentiate between visualizations of different classes (Human Classification Accuracy) and pick more reliable models (Relative Reliability). It also accurately reflects the behavior of the model (Rank Correlation w/ Occlusion).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Evaluating Trust", "weight": 1.0} -->

Given two prediction explanations, we evaluate which seems more trustworthy. We use AlexNet and VGG-16 to compare Guided Backpropagation and Guided Grad-CAM visualizations, noting that VGG-16 is known to be more reliable than AlexNet with an accuracy of $79.09$ mAP (*vs*. $69.20$ mAP) on PASCAL classification. In order to tease apart the efficacy of the visualization from the accuracy of the model being visualized, we consider only those instances where *both* models made the same prediction as ground truth. Given a visualization from AlexNet and one from VGG-16, and the predicted object category, 54 AMT workers were instructed to rate the reliability of the models relative to each other on a scale of clearly more/less reliable (+/-$2$), slightly more/less reliable (+/-$1$), and equally reliable ($0$). This interface is shown in Fig. 5(a). To eliminate any biases, VGG-16 and AlexNet were assigned to be 'model-1' with approximately equal probability. Remarkably, as can be seen in Table.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Evaluating Trust", "weight": 1.0} -->

2, we find that human subjects are able to identify the more accurate classifier (VGG-16 over AlexNet) *simply from the prediction explanations, despite both models making identical predictions.* With Guided Backpropagation, humans assign VGG-16 an average score of $1.00$ which means that it is slightly more reliable than AlexNet, while Guided Grad-CAM achieves a higher score of $1.27$ which is closer to saying that VGG-16 is clearly more reliable. Thus, our visualizations can help users place trust in a model that generalizes better, just based on individual prediction explanations.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Faithfulness *vs*. Interpretability", "weight": 1.0} -->

Faithfulness of a visualization to a model is its ability to accurately explain the function learned by the model. Naturally, there exists a trade-off between the interpretability and faithfulness of a visualization -- a more faithful visualization is typically less interpretable and vice versa. In fact, one could argue that a fully faithful explanation is the entire description of the model, which in the case of deep models is not interpretable/easy to visualize. We have verified in previous sections that our visualizations are reasonably interpretable. We now evaluate how faithful they are to the underlying model. One expectation is that our explanations should be locally accurate, *i.e*. in the vicinity of the input data point, our explanation should be faithful to the model lime_sigkdd16.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Faithfulness *vs*. Interpretability", "weight": 1.0} -->

For comparison, we need a reference explanation with high local-faithfulness. One obvious choice for such a visualization is image occlusion zeiler_eccv14, where we measure the difference in CNN scores when patches of the input image are masked. Interestingly, patches which change the CNN score are also patches to which Grad-CAM and Guided Grad-CAM assign high intensity, achieving rank correlation $0.254$ and $0.261$ (*vs*. $0.168$, $0.220$ and $0.208$ achieved by Guided Backpropagation, c-MWP and CAM respectively) averaged over 2510 images in the PASCAL 2007 val set. This shows that Grad-CAM is more faithful to the original model compared to prior methods. Through localization experiments and human studies, we see that Grad-CAM visualizations are *more interpretable*, and through correlation with occlusion maps, we see that Grad-CAM is *more faithful* to the model.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Diagnosing image classification CNNs with Grad-CAM", "weight": 1.0} -->

In this section we further demonstrate the use of Grad-CAM in analyzing failure modes of image classification CNNs, understanding the effect of adversarial noise, and identifying and removing biases in datasets, in the context of VGG-16 pretrained on imagenet.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Analyzing failure modes for VGG-16", "weight": 1.0} -->

In order to see what mistakes a network is making, we first get a list of examples that the network (VGG-16) fails to classify correctly. For these misclassified examples, we use Guided Grad-CAM to visualize both the correct and the predicted class. As seen in Fig. 6, some failures are due to ambiguities inherent in ImageNet classification. We can also see that *seemingly unreasonable predictions have reasonable explanations*, an observation also made in HOGgles vondrick_iccv13. A major advantage of Guided Grad-CAM visualizations over other methods is that due to its high-resolution and ability to be class-discriminative, it readily enables these analyses.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Effect of adversarial noise on VGG-16", "weight": 1.0} -->

Goodfellow *et al*. goodfellow2015explaining demonstrated the vulnerability of current deep networks to adversarial examples, which are slight imperceptible perturbations of input images that fool the network into misclassifying them with high confidence. We generate adversarial images for an ImageNet-pretrained VGG-16 model such that it assigns high probability ($> 0.9999$) to a category that is not present in the image and low probabilities to categories that are present. We then compute Grad-CAM visualizations for the categories that are present. As shown in Fig. 7, despite the network being certain about the absence of these categories ('tiger cat' and 'boxer'), Grad-CAM visualizations can correctly localize them. This shows that Grad-CAM is fairly robust to adversarial noise.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Effect of adversarial noise on VGG-16", "weight": 1.0} -->

(f) Grad-CAM “Space Shuttle” Figure 7: (a-b) Original image and the generated adversarial image for category “airliner”. (c-d) Grad-CAM visualizations for the original categories “tiger cat” and “boxer (dog)” along with their confidence. Despite the network being completely fooled into predicting the dominant category label of “airliner” with high confidence (>0.9999), Grad-CAM can localize the original categories accurately. (e-f) Grad-CAM for the top-2 predicted classes “airliner” and “space shuttle” seems to highlight the background.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Identifying bias in dataset", "weight": 1.0} -->

In this section, we demonstrate another use of Grad-CAM: identifying and reducing bias in training datasets. Models trained on biased datasets may not generalize to real-world scenarios, or worse, may perpetuate biases and stereotypes (w.r.t. gender, race, age, *etc*.). We finetune an ImageNet-pretrained VGG-16 model for a "doctor" *vs*. "nurse" binary classification task. We built our training and validation splits using the top $250$ relevant images (for each class) from a popular image search engine. And the test set was controlled to be balanced in its distribution of genders across the two classes. Although the trained model achieves good validation accuracy, it does not generalize well ($82$% test accuracy).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Identifying bias in dataset", "weight": 1.0} -->

Grad-CAM visualizations of the model predictions (see the red box^66^6The green and red boxes are drawn manually to highlight correct and incorrect focus of the model. regions in the middle column of Fig. 8) revealed that the model had learned to look at the person's face / hairstyle to distinguish nurses from doctors, thus learning a gender stereotype. Indeed, the model was misclassifying several female doctors to be a nurse and male nurses to be a doctor. Clearly, this is problematic. Turns out the image search results were gender-biased (78% of images for doctors were men, and 93% images for nurses were women).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Identifying bias in dataset", "weight": 1.0} -->

Through these intuitions gained from Grad-CAM visualizations, we reduced bias in the training set by adding in images of male nurses and female doctors, while maintaining the same number of images per class as before. The re-trained model not only generalizes better ($90$% test accuracy), but also looks at the right regions (last column of Fig. 8). This experiment demonstrates a proof-of-concept that Grad-CAM can help detect and remove biases in datasets, which is important not just for better generalization, but also for fair and ethical outcomes as more algorithmic decisions are made in society.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Textual Explanations with Grad-CAM", "weight": 1.0} -->

Equation. gives a way to obtain neuron-importance, $\alpha$, for each neuron in a convolutional layer for a particular class. There have been hypotheses presented in the literature Zhou2014ObjectDE; zeiler_eccv14 that neurons act as concept 'detectors'. Higher positive values of the neuron importance indicate that the presence of that concept leads to an increase in the class score, whereas higher negative values indicate that its absence leads to an increase in the score for the class.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Textual Explanations with Grad-CAM", "weight": 1.0} -->

Given this intuition, let's examine a way to generate textual explanations. In recent work, Bau *et al*. netdissect proposed an approach to automatically name neurons in any convolutional layer of a trained network. These names indicate concepts that the neuron looks for in an image. Using their approach. we first obtain neuron names for the last convolutional layer. Next, we sort and obtain the top-5 and bottom-5 neurons based on their class-specific importance scores, $\alpha_{k}$. The names for these neurons can be used as text explanations.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Textual Explanations with Grad-CAM", "weight": 1.0} -->

Fig. 9 shows some examples of visual and textual explanations for the image classification model (VGG-16) trained on the Places365 dataset zhou2017places. In (a), the positively important neurons computed by look for intuitive concepts such as book and shelf that are indicative of the class 'Book-store'. Also note that the negatively important neurons look for concepts such as sky, road, water and car which don't occur in 'Book-store' images. In (b), for predicting 'waterfall', both visual and textual explanations highlight 'water' and 'stratified' which are descriptive of 'waterfall' images. (e) is a failure case due to misclassification as the network predicted 'rope-bridge' when there is no rope, but still the important concepts (water and bridge) are indicative of the predicted class. In (f), while Grad-CAM correctly looks at the door and the staircase on the paper to predict 'Elevator door', the neurons detecting doors did not pass the IoU threshold^77^7Area of overlap between ground truth concept annotation and neuron activation over area of their union.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Textual Explanations with Grad-CAM", "weight": 1.0} -->

More details of this metric can be found in netdissect of 0.05 (chosen in order to suppress the noise in the neuron names), and hence are not part of the textual explanations. More qualitative examples can be found in the Sec. F.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Textual Explanations with Grad-CAM", "weight": 1.0} -->

(a) Image captioning explanations Figure 10: Interpreting image captioning models: We use our class-discriminative localization technique, Grad-CAM to find spatial support regions for captions in images. Fig. 10(a) Visual explanations from image captioning model karpathy2015deep highlighting image regions considered to be important for producing the captions. Fig. 10(b) Grad-CAM localizations of a global or holistic captioning model for captions generated by a dense captioning model johnson_cvpr16 for the three bounding box proposals marked on the left. We can see that we get back Grad-CAM localizations (right) that agree with those bounding boxes – even though the captioning model and Grad-CAM techniques do not use any bounding box annotations.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Grad-CAM for Image Captioning and VQA", "weight": 1.0} -->

Finally, we apply Grad-CAM to vision & language tasks such as image captioning chen2015microsoft; johnson_cvpr16; vinyals_cvpr15 and Visual Question Answering (VQA) antol2015vqa; gao2015you; malinowski_iccv15; ren_nips15. We find that Grad-CAM leads to interpretable visual explanations for these tasks as compared to baseline visualizations which do not change noticeably across changing predictions. Note that existing visualization techniques either are not class-discriminative (Guided Backpropagation, Deconvolution), or simply cannot be used for these tasks/architectures, or both (CAM, c-MWP).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Image Captioning", "weight": 1.0} -->

In this section, we visualize spatial support for an image captioning model using Grad-CAM. We build Grad-CAM on top of the publicly available neuraltalk2^88^8 implementation karpathy2015deep that uses a finetuned VGG-16 CNN for images and an LSTM-based language model. Note that this model does not have an explicit attention mechanism. Given a caption, we compute the gradient of its log probability w.r.t. units in the last convolutional layer of the CNN ($conv5_3$ for VGG-16) and generate Grad-CAM visualizations as described in Sec. 3. See Fig. 10(a). In the first example, Grad-CAM maps for the generated caption localize every occurrence of both the kites and people despite their relatively small size. In the next example, Grad-CAM correctly highlights the pizza and the man, but ignores the woman nearby, since 'woman' is not mentioned in the caption. More examples are in Sec. C.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Image Captioning", "weight": 1.0} -->

Comparison to dense captioning. Johnson *et al*. johnson_cvpr16 recently introduced the Dense Captioning (DenseCap) task that requires a system to jointly localize and caption salient regions in a given image. Their model consists of a Fully Convolutional Localization Network (FCLN) that produces bounding boxes for regions of interest and an LSTM-based language model that generates associated captions, all in a single forward pass. Using DenseCap, we generate 5 region-specific captions per image with associated ground truth bounding boxes. Grad-CAM for a whole-image captioning model (neuraltalk2) should localize the bounding box the region-caption was generated, which is shown in Fig. 10(b). We quantify this by computing the ratio of mean activation inside *vs*. outside the box. Higher ratios are better because they indicate stronger attention to the region the caption was generated. Uniformly highlighting the whole image results in a baseline ratio of $1.0$ whereas Grad-CAM achieves $3.27$ $\pm$ $0.18$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Image Captioning", "weight": 1.0} -->

Adding high-resolution detail gives an improved baseline of $2.32$ $\pm$ 0.08 (Guided Backpropagation) and the best localization at $6.38$ $\pm$ 0.99 (Guided Grad-CAM). Thus, Grad-CAM is able to localize regions in the image that the DenseCap model describes, even though the holistic captioning model was never trained with bounding-box annotations.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Grad-CAM for individual words of caption", "weight": 1.0} -->

In our experiment we use the Show and Tell model vinyals_cvpr15 pre-trained on MSCOCO without fine-tuning through the visual representation obtained from Inception szegedy2016rethinking architecture. In order to obtain Grad-CAM map for individual words in the ground-truth caption we one-hot encode each of the visual words at the corresponding time-steps and compute the neuron importance score using Eq. and combine with the convolution feature maps using Eq..

<!-- chunk {"id": "body-0072", "role": "body", "section": "Grad-CAM for individual words of caption", "weight": 1.0} -->

Comparison to Human Attention We manually created an object category to word mapping that maps object categories like $<$person$>$ to a list of potential fine-grained labels like \["child", "man", \"woman\",...\]. We map a total of 830 visual words existing in COCO captions to 80 COCO categories. We then use the segmentation annotations for the 80 categories as human attention for this subset of matching words.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Grad-CAM for individual words of caption", "weight": 1.0} -->

We then use the pointing evaluation from zhang2016top. For each visual word from the caption, we generate the Grad-CAM map and then extract the maximally activated point. We then evaluate if the point lies within the human attention mapsegmentation for the corresponding COCO category, thereby counting it as a hit or a miss. The pointing accuracy is then calculated as\${Acc} = \frac{\#Hits}{{\#Hits} + {\#Misses}}$. We perform this experiment on 1000 randomly sampled images from COCO dataset and obtain an accuracy of 30.0%. Some qualitative examples can be found in Fig. 11.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Visual Question Answering", "weight": 1.0} -->

Typical VQA pipelines antol2015vqa; gao2015you; malinowski_iccv15; ren_nips15 consist of a CNN to process images and an RNN language model for questions. The image and the question representations are fused to predict the answer, typically with a $1000$-way classification ($1000$ being the size of the answer space). Since this is a classification problem, we pick an answer (the score $y^{c}$ in ) and use its score to compute Grad-CAM visualizations over the image to explain the answer. Despite the complexity of the task, involving both visual and textual components, the explanations (of the VQA model from Lu *et al*. Lu2015 ) described in Fig. 12 are surprisingly intuitive and informative.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Visual Question Answering", "weight": 1.0} -->

We quantify the performance of Grad-CAM via correlation with occlusion maps, as in Sec. 5.3. Grad-CAM achieves a rank correlation (with occlusion maps) of 0.60 $\pm$ 0.038 whereas Guided Backpropagation achieves 0.42 $\pm$ 0.038, indicating higher faithfulness of our Grad-CAM visualization.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Visual Question Answering", "weight": 1.0} -->

(a) Visualizing VQA model from Lu2015 (b) Visualizing ResNet based Hierarchical co-attention VQA model from Lu2016 Figure 12: Qualitative Results for our VQA experiments: (a) Given the image on the left and the question “What color is the firehydrant?”, we visualize Grad-CAMs and Guided Grad-CAMs for the answers “red", “yellow" and “yellow and red". Grad-CAM visualizations are highly interpretable and help explain any target prediction – for “red”, the model focuses on the bottom red part of the firehydrant; when forced to answer “yellow”, the model concentrates on it‘s top yellow cap, and when forced to answer “yellow and red", it looks at the whole firehydrant! (b) Our approach is capable of providing interpretable explanations even for complex models.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Visual Question Answering", "weight": 1.0} -->

Comparison to Human Attention. Das *et al*. vqahat collected human attention maps for a subset of the VQA dataset antol2015vqa. These maps have high intensity where humans looked in the image in order to answer a visual question. Human attention maps are compared to Grad-CAM visualizations for the VQA model from Lu2015 on 1374 val question-image (QI) pairs from antol2015vqa using the rank correlation evaluation protocol as in vqahat. Grad-CAM and human attention maps have a correlation of 0.136, which is higher than chance or random attention maps (zero correlation). This shows that despite not being trained on grounded image-text pairs, even non-attention based CNN + LSTM based VQA models are surprisingly good at localizing regions for predicting a particular answer.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Visual Question Answering", "weight": 1.0} -->

Visualizing ResNet-based VQA model with co-attention. Lu *et al*. Lu2016 use a 200 layer ResNet he_cvpr15 to encode the image, and jointly learn a hierarchical attention mechanism on the question and image. Fig. 12(b) shows Grad-CAM visualizations for this network. As we visualize deeper layers of the ResNet, we see small changes in Grad-CAM for most adjacent layers and larger changes between layers that involve dimensionality reduction. More visualizations for ResNets can be found in Sec. G. To the best of our knowledge, we are the first to visualize decisions from ResNet-based models.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we proposed a novel class-discriminative localization technique -- Gradient-weighted Class Activation Mapping (Grad-CAM) -- for making *any* CNN-based model more transparent by producing visual explanations. Further, we combined Grad-CAM localizations with existing high-resolution visualization techniques to obtain the best of both worlds -- high-resolution and class-discriminative Guided Grad-CAM visualizations. Our visualizations outperform existing approaches on both axes -- interpretability and faithfulness to original model. Extensive human studies reveal that our visualizations can discriminate between classes more accurately, better expose the trustworthiness of a classifier, and help identify biases in datasets. Further, we devise a way to identify important neurons through Grad-CAM and provide a way to obtain textual explanations for model decisions. Finally, we show the broad applicability of Grad-CAM to various off-the-shelf architectures for tasks such as image classification, image captioning and visual question answering. We believe that a true AI system should not only be intelligent, but also be able to reason about its beliefs and actions for humans to trust and use it.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Future work includes explaining decisions made by deep networks in domains such as reinforcement learning, natural language processing and video applications.
