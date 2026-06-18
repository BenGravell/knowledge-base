<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Mish: A Self Regularized Non-Monotonic Activation Function

Topics include Activation functions, Mish, Non-monotonic activations, Self-regularization, Computer vision, Object detection, ImageNet, COCO, ReLU alternatives.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Mish proposes a smooth non-monotonic activation, x tanh(softplus(x)), and argues that its derivative shape gives useful self-regularizing behavior. The paper is best read as part of the post-Swish family of smooth ReLU alternatives, with evidence across classification and detection benchmarks rather than a narrow architectural change.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose Mish, a novel self-regularized non-monotonic activation function which can be mathematically defined as: f(x) = xtanh(softplus(x)). As activation functions play a crucial role in the performance and training dynamics in neural networks, we validated experimentally on several well-known benchmarks against the best combinations of architectures and activation functions. We also observe that data augmentation techniques have a favorable effect on benchmarks like ImageNet-1k and MS-COCO across multiple architectures. For example, Mish outperformed Leaky ReLU on YOLOv4 with a CSP-DarkNet-53 backbone on average precision (AP_50^(val)) by 2.1% in MS-COCO object detection and ReLU on ResNet-50 on ImageNet-1k in Top-1 accuracy by approx1% while keeping all other network parameters and hyperparameters constant. Furthermore, we explore the mathematical formulation of Mish in relation with the Swish family of functions and propose an intuitive understanding on how the first derivative behavior may be acting as a regularizer helping the optimization of deep neural networks. Code is publicly available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Bibliographic and Citation Tools", "weight": 1.0} -->

Bibliographic Explorer *(What is the Explorer?)*

<!-- chunk {"id": "body-0005", "role": "body", "section": "Bibliographic and Citation Tools", "weight": 1.0} -->

Connected Papers *(What is Connected Papers?{target="_blank"})*

<!-- chunk {"id": "body-0006", "role": "body", "section": "Bibliographic and Citation Tools", "weight": 1.0} -->

Litmaps *(What is Litmaps?{target="_blank"})*

<!-- chunk {"id": "body-0007", "role": "body", "section": "Bibliographic and Citation Tools", "weight": 1.0} -->

scite Smart Citations *(What are Smart Citations?{target="_blank"})*

<!-- chunk {"id": "body-0008", "role": "body", "section": "Code, Data and Media Associated with this Article", "weight": 1.0} -->

alphaXiv *(What is alphaXiv?{target="_blank"})*

<!-- chunk {"id": "body-0009", "role": "body", "section": "Code, Data and Media Associated with this Article", "weight": 1.0} -->

CatalyzeX Code Finder for Papers *(What is CatalyzeX?{target="_blank"})*

<!-- chunk {"id": "body-0010", "role": "body", "section": "Code, Data and Media Associated with this Article", "weight": 1.0} -->

DagsHub *(What is DagsHub?{target="_blank"})*

<!-- chunk {"id": "body-0011", "role": "body", "section": "Code, Data and Media Associated with this Article", "weight": 1.0} -->

Gotit.pub *(What is GotitPub?{target="_blank"})*

<!-- chunk {"id": "body-0012", "role": "body", "section": "Code, Data and Media Associated with this Article", "weight": 1.0} -->

Hugging Face *(What is Huggingface?{target="_blank"})*

<!-- chunk {"id": "body-0013", "role": "body", "section": "Code, Data and Media Associated with this Article", "weight": 1.0} -->

ScienceCast *(What is ScienceCast?{target="_blank"})*

<!-- chunk {"id": "body-0014", "role": "body", "section": "Demos", "weight": 1.0} -->

Replicate *(What is Replicate?{target="_blank"})*

<!-- chunk {"id": "body-0015", "role": "body", "section": "Demos", "weight": 1.0} -->

Hugging Face Spaces *(What is Spaces?{target="_blank"})*

<!-- chunk {"id": "body-0016", "role": "body", "section": "Demos", "weight": 1.0} -->

TXYZ.AI *(What is TXYZ.AI?{target="_blank"})*

<!-- chunk {"id": "body-0017", "role": "body", "section": "Recommenders and Search Tools", "weight": 1.0} -->

Influence Flower *(What are Influence Flowers?{target="_blank"})*

<!-- chunk {"id": "body-0018", "role": "body", "section": "arXivLabs: experimental projects with community collaborators", "weight": 1.0} -->

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

<!-- chunk {"id": "body-0019", "role": "body", "section": "arXivLabs: experimental projects with community collaborators", "weight": 1.0} -->

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

<!-- chunk {"id": "body-0020", "role": "body", "section": "arXivLabs: experimental projects with community collaborators", "weight": 1.0} -->

Have an idea for a project that will add value for arXiv\'s community? **Learn more about arXivLabs**.

<!-- chunk {"id": "body-0021", "role": "body", "section": "arXivLabs: experimental projects with community collaborators", "weight": 1.0} -->

Which authors of this paper are endorsers? \| [Disable MathJax](javascript:setMathjaxCookie) (What is MathJax?)
