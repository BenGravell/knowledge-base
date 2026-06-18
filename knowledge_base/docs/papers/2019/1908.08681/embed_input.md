Mish: A Self Regularized Non-Monotonic Activation Function

Topics include Activation functions, Mish, Non-monotonic activations, Self-regularization, Computer vision, Object detection, ImageNet, COCO, ReLU alternatives.

Mish proposes a smooth non-monotonic activation, x tanh(softplus(x)), and argues that its derivative shape gives useful self-regularizing behavior. The paper is best read as part of the post-Swish family of smooth ReLU alternatives, with evidence across classification and detection benchmarks rather than a narrow architectural change.

We propose Mish, a novel self-regularized non-monotonic activation function which can be mathematically defined as: f(x) = xtanh(softplus(x)). As activation functions play a crucial role in the performance and training dynamics in neural networks, we validated experimentally on several well-known benchmarks against the best combinations of architectures and activation functions. We also observe that data augmentation techniques have a favorable effect on benchmarks like ImageNet-1k and MS-COCO across multiple architectures. For example, Mish outperformed Leaky ReLU on YOLOv4 with a CSP-DarkNet-53 backbone on average precision (AP_50^(val)) by 2.1% in MS-COCO object detection and ReLU on ResNet-50 on ImageNet-1k in Top-1 accuracy by approx1% while keeping all other network parameters and hyperparameters constant. Furthermore, we explore the mathematical formulation of Mish in relation with the Swish family of functions and propose an intuitive understanding on how the first derivative behavior may be acting as a regularizer helping the optimization of deep neural networks. Code is publicly available at

### blog link

### DBLP - CS Bibliography

## BibTeX formatted citation

### Bookmark

## Bibliographic and Citation Tools

Bibliographic Explorer *(What is the Explorer?)*

Connected Papers *(What is Connected Papers?{target="_blank"})*

Litmaps *(What is Litmaps?{target="_blank"})*

scite Smart Citations *(What are Smart Citations?{target="_blank"})*

## Code, Data and Media Associated with this Article

alphaXiv *(What is alphaXiv?{target="_blank"})*

CatalyzeX Code Finder for Papers *(What is CatalyzeX?{target="_blank"})*

DagsHub *(What is DagsHub?{target="_blank"})*

Gotit.pub *(What is GotitPub?{target="_blank"})*

Hugging Face *(What is Huggingface?{target="_blank"})*

ScienceCast *(What is ScienceCast?{target="_blank"})*

## Demos

Replicate *(What is Replicate?{target="_blank"})*

Hugging Face Spaces *(What is Spaces?{target="_blank"})*

TXYZ.AI *(What is TXYZ.AI?{target="_blank"})*

## Recommenders and Search Tools

Influence Flower *(What are Influence Flowers?{target="_blank"})*

## arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv\'s community? **Learn more about arXivLabs**.

Which authors of this paper are endorsers? \| [Disable MathJax](javascript:setMathjaxCookie) (What is MathJax?)
