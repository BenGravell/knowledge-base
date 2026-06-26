<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Three Decades of Activations: A Comprehensive Survey of 400 Activation Functions for Neural Networks

Topics include Activation functions, Neural networks, Deep learning, Survey, Function taxonomy, Transfer functions.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

This survey builds a large catalog of activation functions and organizes the historical design space so that new proposals can be compared against existing functions. Its main value is as a reference map for avoiding duplicate activation-function rediscoveries and for seeing how modern deep-learning nonlinearities fit into older neural-network transfer-function work.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Neural networks have proven to be a highly effective tool for solving complex problems in many areas of life. Recently, their importance and practical usability have further been reinforced with the advent of deep learning. One of the important conditions for the success of neural networks is the choice of an appropriate activation function introducing non-linearity into the model. Many types of these functions have been proposed in the literature in the past, but there is no single comprehensive source containing their exhaustive overview. The absence of this overview, even in our experience, leads to redundancy and the unintentional rediscovery of already existing activation functions. To bridge this gap, our paper presents an extensive survey involving 400 activation functions, which is several times larger in scale than previous surveys. Our comprehensive compilation also references these surveys; however, its main goal is to provide the most comprehensive overview and systematization of previously published activation functions with links to their original sources. The secondary aim is to update the current understanding of this family of functions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Neural networks - and deep learning in particular - have exhibited remarkable success in addressing diverse challenges across various fields. They stand as state-of-the-art approaches, showcasing their prowess in solving complex and intricate problems. At the heart of these networks, activation functions (AFs) play an important role by introducing nonlinearity to neural network layers. In the absence of nonlinear AFs, typical neural networks would only model a weighted sum of inputs, limiting their capacity to capture intricate relationships within the data.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The choice of activation functions profoundly influences a network's ability to learn and generalize, directly impacting its performance across a spectrum of tasks. Effective activation functions possess several key properties, as outlined by Dubey, Singh, and Chaudhuri: a) introducing non-linear curvature to enhance training convergence within the optimization landscape; b) maintaining an unobstructed gradient flow during training; c) ensuring a minimal increase in the computational complexity of the model; and d) preserving the distribution of data to optimize the network's training.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are many activation functions proposed in the literature in the last three decades - some more computationally complex or with higher performance than others. However, further research of the activation functions is hampered by the absence of a consolidated list. This gap leads to the inadvertent reinvention of existing activation functions and the independent proposal of identical or very similar ones, resulting in a wasteful consumption of research resources. Even comprehensive surveys and reviews, such as those by Dubey, Singh, and Chaudhuri and Apicella et al., often omit numerous activation functions present in the literature; furthermore, these reviews are also a bit older and many new activation functions emerged since then. This oversight can lead to instances where an AF is redundantly proposed as novel, despite its prior introduction in the literature - e.g., rectified power unit (RePU) (section 3.6.39), dual parametric ReLU (DPReLU) (section 4.2.20), truncated rectified (TRec) (section 3.6.21), ReLU-Swish (section 3.6.46), and bounded ReLU (BReLU) (section 3.6.16).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

By providing a more extensive list of available activation functions, we aim to avoid such redundancy and promote faster advances in the research of activation functions in neural networks.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this issue, we strive to provide an extensive and consolidated list of available AFs. This survey aims to prevent redundancy, eliminate the reinvention of established AFs to promote innovation, and accelerate the advancement of research in the field of neural networks. By offering a comprehensive resource, we aim to promote efficiency and innovation in the exploration of AFs within the field.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is important to note that our contribution primarily focuses on providing a comprehensive list of AFs rather than conducting extensive benchmarks or in-depth analyses. The breadth of the compilation encompasses a wide array of AFs, making a detailed benchmark or a deeper analysis beyond the scope of this work. Our aim is to provide researchers with a foundational resource that facilitates informed decision-making in selecting AFs for neural networks, recognizing that a more exhaustive exploration or detailed analysis would necessitate a dedicated and focused effort beyond the scope of this comprehensive listing. The presented overview is limited to real-valued activation functions; complex-valued neural networks (e.g. brief overview available in), bicomplex-valued neural networks (e.g.,), quaternion-valued neural networks (e.g.,), photonic neural networks (e.g.,), fuzzy neural networks (e.g.,), AFs for probabilistic boolean logic (e.g.,), quantum AFs (e.g.,) and others are out of the scope of this work.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

1 We have chosen to categorize AFs into two main classes: fixed AFs (section 3) and adaptive activation functions (AAFs) (section 4), the latter having a parameter that is trained alongside the other weights in a network. Although instances exist where AFs are virtually identical, differing only in the presence of a particular adaptive parameter (e.g., swish (see section 4.4.1) and SiLU (see section 3.3)), this classification proves valuable. AAFs, by virtue of their parameterization, offer an added layer of flexibility in capturing complex relationships within the data during the training process.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Literature review", "weight": 1.0} -->

There are several reviews of AFs available in the literature; however, most of them encompass only the most commonly known AFs. While this is sufficient for an overview for newcomers to the field, it does not allow for efficient research of AFs themselves. Probably the most extensive review is the from 2022, which lists over 70 AFs and provides a benchmark for 18 of them. Other reviews works containing list of AFs include.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Literature review", "weight": 1.0} -->

While there are several existing works that offer benchmarks and empirical comparisons of various AFs, it is unfortunate that these studies are often constrained by a limited selection of AFs. Typically, the focus is centered on the most well-known and widely used functions, neglecting the broader spectrum of AFs available in the literature.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Literature review", "weight": 1.0} -->

To avoid the manual selection of AFs, many researchers resort to various optimization approaches to find the optimal AF for their problems. e.g. an evolutionary approach was used to evolve the optimal activation function in and grid search using artificial data was used. Another search for the optimal activation functions was presented in where several simple activation functions were found to perform remarkably well. These automatic approaches might be used for evolving the activation functions (e.g., ) or for selecting the optimal activation function for a given neuron (e.g., ). While evolved activation function may perform well for a given problem, they also might be very complex - e.g., evolved activation functions. The complexity of an activation function is also important characteristic as it significantly influences the computational efficiency of a neural network; however, this might be mitigated by efficient implementations (including hardware implementations) of such activation functions (e.g., ). An empirical analysis of computational efficiency and power consumption of various AFs is available.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Classical activation functions", "weight": 1.0} -->

First, our discussion delves into fixed activation functions, devoid of adaptive parameters. This category of activation functions represents the basic type that was predominantly employed in the initial neural network architectures and continues to be prevalent today. Fixed activation functions, such as the logistic sigmoid and hyperbolic tangent, are characterized by their predetermined mathematical formulations, where the activation output solely depends on the input without the introduction of any trainable parameters.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Classical activation functions", "weight": 1.0} -->

1 While these kinds of neural networks (NNs) are not discussed throughout this work, some of these approaches will use AFs presented in this work.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Binary activation function", "weight": 1.0} -->

The binary activation function (binary AF) - also called a step function - is a simple yet important activation function used in neural networks. It assigns an output value of 1 if the input is positive or zero and an output value of 0 if the input is negative. Mathematically, it can be defined as follows: Similar to binary activation function is the sign function, which produces an output value of -1 if the input is negative and 1 if it is positive (and 0 for outputs that are exactly zero). Since the sign and the binary activation functions have nearly exact properties from the point of view of neural networks, only the binary activation function is mentioned, but the points hold similarly for the sign activation function.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Binary activation function", "weight": 1.0} -->

The main advantage of the binary activation function is that it is straightforward and computationally efficient to implement. It does not involve complex mathematical operations, making it suitable for networks with low computational resources or for hardware implementations. However, the binary activation function has one glaring disadvantage - the lack of differentiability. The binary activation function is not differentiable at the point of discontinuity (x = 0) and is zero elsewhere. This poses challenges for optimization algorithms that rely on gradients, such as backpropagation (BP), since the gradient is noninformative. Since the gradient-based methods are used predominantly, the binary activation function is used very rarely and is important mainly for historical reasons as it was used in the original perceptron.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Sigmoid family of activation functions", "weight": 1.0} -->

Various smoothed variants of the binary activation functions (sigmoids) are commonly used; the most common is the logistic function - the standard logistic sigmoid function was dominant in the field prior the introduction of rectified linear unit (ReLU) (see section 3.6), the logistic function is often called just sigmoid in the literature which is also used throughout this work for brevity (unless specified otherwise, sigmoid is equivalent to standard logistic function in the text). Standard logistic function is defined as The logistic sigmoid was a popular choice since its output values can interpreted as the probability that a binary variable is 1 since it squashes the input to the interval. The problem of sigmoid activation functions is that they saturate - they saturate when their input z is either a large positive number or a large negative number, which makes gradient-based learning difficult; therefore their use in feedforward networks is usually discouraged. Another option, albeit significantly less popular in artificial neural networks (ANNs), is the probit AF, which is just the cumulative standard normal distribution function used as an AF.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Sigmoid family of activation functions", "weight": 1.0} -->

Another popular sigmod function is the hyperbolic tangent (tanh) activation function which is just scaled and shifted logistic sigmoid Similarly as the logistic sigmoid, the tanh also squashes the inputs; however, it squashes them to the interval (-1, 1). The tanh function is often advantageous over the logistic sigmoid function because it is centered around zero and it is similar to the identity function near zero, which makes training of a network easier if the activations are kept small. Nevertheless, the tanh function saturates similarly as does the logistic sigmoid and therefore similarly suffers from the vanishing gradients. Computationally efficient approximation of the tanh activation functions based on splines were proposed in tanh36 based on approximation relying on 36 equidistant points and tanh3 using only 3 points. Scaled variant tanh (z 2) was used. The linearized unit (LRTanh) is a tanh variant used together with modified BP that substitutes a different activation function derivative proposed.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Sigmoid family of activation functions", "weight": 1.0} -->

There are also approximations of the logistic sigmoid and tanh that are meant to speed up the computations; e.g., pRPPSG and other similar piecewise approximations.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Sigmoid family of activation functions", "weight": 1.0} -->

A scaled version of the logistic sigmoid function was proposed in with the motivation to have the same linear regimes as the tanh and relu activation functions when initialized with the popular normalized initialized method proposed. The scaled version used fixed parameters A more complicated variant named n-sigmoid was proposed; however, it seems that the formula presented in the paper is not as the authors intended and, therefore, we omit this AF from the list.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Shifted and scaled sigmoid (SSS)", "weight": 1.0} -->

The shifted and scaled sigmoid (SSS) was used; it is the logistic sigmoid with horizontal scaling and translation defined as where a and b are predetermined parameters; Arai and Imamura used a = 0. 02 and b = 600.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Variant sigmoid function (VSF)", "weight": 1.0} -->

The variant sigmoid function (VSF) is an older parametric variant of the logistic sigmoid proposed. It is defined as where a, b, and c are predetermined parameters.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Scaled hyperbolic tangent", "weight": 1.0} -->

A parametric version called scaled hyperbolic tangent (stanh) was used: where a and b are fixed hyperparameters that control the scaling of the function. Lecun et al. proposed using a = 1. 7159 and b = 2 3 A similar concept was analyzed in where sigmoids with bi-modal derivatives were used as activation functions. An example of such a function is where b is a hyperparameter; similarly, additional three activation functions with bi-modal derivates were proposed.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Arctan", "weight": 1.0} -->

The arctangent (arctan) function and its variation were used as activation functions: The arctan resembles a logistic sigmoid activation, however, it covers wider range (-π 2, π 2). The arctan and several its variation were compared with the tanh, ReLU, leaky ReLU (LReLU), logistic sigmoid activation, and swish; the best-performing functions in the presented experiments were the arctan and its variation arctanGR. Interestingly, the arctan was used as an AF twenty years earlier. The arctanGR is a scaled version of the arctan and is defined as Other scaling variants such as division by the π, 1+ √ 5 2, or the Euler number are presented.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Sigmoid-Algebraic activation function", "weight": 1.0} -->

The Sigmoid-Algebraic is a sigmoid variant defined. It is defined as

<!-- chunk {"id": "body-0027", "role": "body", "section": "Triple-state sigmoid", "weight": 1.0} -->

The triple-state sigmoid unit (TS-sigmoid) is a cascaded AF similar to TS-swish (see section 3.3.6); it is defined as where a and b are fixed parameters.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Improved logistic sigmoid", "weight": 1.0} -->

The improved logistic sigmoid is yet another sigmoid based activation function designed to deal with the vanishing gradient problem where a and b are fixed parameters; a controls the slope and b is a thresholding parameter. The authors recommend a bound on the slope parameter a: Even though the parameters are fixed during the training of a network, a procedure for preseting them based on the network and data was proposed. The output range of the sigmoid-weighted linear unit (SiLU) is (-∞, ∞). The authors Qin, Wang, and Zou also showed that the improved logistic sigmoid AF has a higher convergence speed than the logistic sigmoid AF.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Combination of the sigmoid and linear activation (SigLin)", "weight": 1.0} -->

A SigLin 2 was used as an AF. The SigLin is defined as where σ (z) is the logistic sigmoid AF and a is a fixed parameter; however, this AF was used only in a modified optimization procedure. Roodschild, Gotay Sardiñas, and Will experimented with a ∈ { 0, 0. 05, 0. 1, 0. 15 }.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Penalized hyperbolic tangent", "weight": 1.0} -->

A penalized hyperbolic tangent (ptanh) the LReLU (see section 3.6) but uses the tanh function instead of the linear function: where a ∈ (1, ∞). This function has similar values near 0 as the LReLU with identical parameter a as they both share the same Taylor expansion up to the first order; however this function saturates to -1 a for z →-∞ and to 1 for z →∞. The ptanh AF was found to perform consistently well for various natural language processing (NLP) tasks compared to ReLU, LReLU and several other activation functions.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Soft-root-sign (SRS)", "weight": 1.0} -->

A soft-root-sign (SRS) activation function is a parametric, smooth, non-monotonic, and bounded activation function. It is defined as where a and b are predetermined parameters; the authors Li and Zhou propose using a = 2 and b = 3 whereas the parameters are said to be learnable. The output range of SRS is [ab b -a e, a]. The performance of the SRS was demonstrated using hte CIFAR-10 and CIFAR-100 task in comparison with the ReLU (see section 3.6 for the description of the ReLU family of AFs), LReLU, parametric rectified linear unit (PReLU), softplus, exponential linear unit (ELU), scaled ELU (SELU), and swish.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Soft-root-sign (SRS)", "weight": 1.0} -->

2 This abbreviation is used only in this work; Roodschild, Gotay Sardiñas, and Will did not name the function.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Soft clipping (SC)", "weight": 1.0} -->

The soft clipping (SC) AF is another bounded AF; it is approximatelly piecewise linear in the range z ∈ and it is defined as where a is a fixed parameter.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Hexpo", "weight": 1.0} -->

The Hexpo activation function was proposed in order to minimize the problem of vanishing gradient; it resembles a tanh activation function with scaled gradients: where a, b, c, and d are fixed parameters. While the parameters could be trainable in theory, it is not recommended as it would lead to the vanishing gradient problem. The Hexpo functions allow for control over the gradient by tunning the parameters a, b, c, and d and the ratios a b and c d -with increasing the ratios a b or c d, the rate of gradient decay to zero decreases; increasing only a and c scales the gradient around the origin up.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Softsign", "weight": 1.0} -->

A softsign activation function is a smooth activation function similar to the tanh activation; however, it is less prone to vanishing gradients. It is defined as where | z | denotes the absolute value of z.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Smooth step", "weight": 1.0} -->

The smooth step is a sigmoid AF; it is defined as where a is a fixed hyperparameter.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Elliott activation function", "weight": 1.0} -->

Elliott activation function is one of the earliest proposed activation functions to replace to replace the logistic sigmoid or tanh activation functions; the Elliott AF is a scaled and translated softsign AF. It is defined as The output of the Elliott activation functions is in range. The main advantage of the Elliott AF is that it can be calculated much faster than the logistic sigmoid.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Sinc-Sigmoid", "weight": 1.0} -->

The Sinc-Sigmoid is a sigmoid-based AF proposed. It is defined as where sinc (x) is the unnormalized 3 sinc function.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Sinc-Sigmoid", "weight": 1.0} -->

3 Koçak and Üstünda˘ g ¸ Siray did not specify whether it is the normalized or unnormalized variant. Still, they provided the derivative of the Sinc-Sigmoid, which suggests that the unnormalized variant was used.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Sigmoid-Gumbel activation function", "weight": 1.0} -->

The Sigmoid-Gumbel (SG) is a non-adaptive AF proposed recently; it is defined as

<!-- chunk {"id": "body-0041", "role": "body", "section": "NewSigmoid", "weight": 1.0} -->

The NewSigmoid is a sigmoid variant proposed. It is defined as

<!-- chunk {"id": "body-0042", "role": "body", "section": "Root2sigmoid", "weight": 1.0} -->

The root2sigmoid is another sigmoid variant proposed. It is defined 4 as

<!-- chunk {"id": "body-0043", "role": "body", "section": "LogLog", "weight": 1.0} -->

The LogLog is a simple AF proposed; it is defined as The LogLog, cLogLog (see section 3.2.21) were used in NNs for forecasting financial time-series.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Complementary Log-Log (cLogLog)", "weight": 1.0} -->

The complementary LogLog (cLogLog) is another simple AF proposed in complementing the LogLog (see section 3.2.20);

<!-- chunk {"id": "body-0045", "role": "body", "section": "SechSig", "weight": 1.0} -->

The SechSig is another AF utilizing the logistic sigmoid in its definition; it is defined as Közkurt et al. also proposed a parametric version which we will call parametric SechSig (pSechSig): where a is a fixed parameter.

<!-- chunk {"id": "body-0046", "role": "body", "section": "TanhSig", "weight": 1.0} -->

The TanhSig is an AF similar to SechSig; it is defined as Közkurt et al. also proposed a parametric version which we will call parametric TanhSig (pTanhSig): where a is a fixed parameter.

<!-- chunk {"id": "body-0047", "role": "body", "section": "TanhSig", "weight": 1.0} -->

4 The author had probably a typo in the definition in the original paper; we present the formula we think Kumar and Sodhi intended to write - it resembles the NewSigmoid and fits the numerical values given in the paper.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Multistate activation function (MSAF)", "weight": 1.0} -->

The multistate activation function (MSAF) is a logistic sigmoid based AF proposed. The general MSAF is defined as where a and b k, k = 1,..., N are fixed parameters; a ∈ R, N ∈ N +, b k ∈ R +, and b 1 < b 2 <... < b N. If a = 0, it is named as N -order 5 MSAF.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Multistate activation function (MSAF)", "weight": 1.0} -->

There is also a special case called symmetrical MSAF (SymMSAF) defined as where a is required to be significantly smaller than 0

<!-- chunk {"id": "body-0050", "role": "body", "section": "Rootsig and others", "weight": 1.0} -->

The rootsig is one of the activations listed. It is defined as where a is a parameter. This function is called rootsig in where the authors list a variant with a = 1.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Sigmoid and tanh combinations", "weight": 1.0} -->

Guevraa et al. proposed several activations mostly combining the logistic sigmoid, tanh, and linear function. The general approach is where g (z) and h (z) are two different AFs. The authors used the following pairs { g (z), h (z) }: { σ 2 (z), tanh(z) }, { σ 2 (z), tanh(z) }, { σ 2 (z), 0 }, { tanh(z), 0 }, { σ 2 (z), az }, and { tanh(z), az }, where a > 0 is a fixed parameter and Guevraa et al. also proposed an AF we termed SigLU (see section 3.6.52) and nonadaptive variant of PTELU.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Class of sigmoid-weighted linear units", "weight": 1.0} -->

The SiLU is the most common example of a larger class of sigmoidal units defined as where s (z) is any sigmoidal function; it becomes the SiLU if the logistic sigmoid function is used. The SiLU is thus defined as 5 This does not exactly fit into the exemplar MSAF of order two presented; it is possible that authors intended another constraint b 1 = 0 for such case. where σ (z) is the logistic sigmoid. The SiLU has the output range of (-0. 5, ∞) and was first used for reinforcement learning tasks such as SZ-Tetris and Tetris. The SiLU was also found to work well for the CIFAR-10/100 and ImageNet tasks. The adaptive variant of the SiLU is called swish (see section 4.4.1).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Class of sigmoid-weighted linear units", "weight": 1.0} -->

For the purposes of this work, we also consider any squashing functions s ( z ) and not necessarily only sigmoids - for example, we classify rectified hyperbolic secant (see section 3.3.27) as a member of this class. We also list functions that are closely based on the SiLU and its variants.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Class of sigmoid-weighted linear units", "weight": 1.0} -->

A similar approach named weighted sigmoid gate unit (WiG) was proposed, where the AF was used only for gating each of the raw inputs: where x denotes the vector of raw inputs, w i the weights of neuron i and b i its bias

<!-- chunk {"id": "body-0055", "role": "body", "section": "Gaussian error linear unit (GELU)", "weight": 1.0} -->

Gaussian error linear unit (GELU) is an activation function based on the standard Gaussian cumulative distribution function, and it weights inputs by their value rather than gating them as ReLUs do. It is defined as where Φ(z) is the standard Gaussian cumulative distribution function (CDF) and erf (x) is the Gauss error function. It is similar to the SiLU but it uses Φ(z) instead of the σ (z). However, due to the complicated formula, the GELU can be approximated as if the performance gains are worth the loss of exactness. The function is similar to SiLU (see section 3.3), it only uses Gaussian CDF Φ(z) instead of the logistic distribution CDF σ (z). GELU was found to outperform many competitors (e.g., ReLU, ELU, SELU, continuously differentiable exponential linear unit (CELU), sigmoid, tanh).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Gaussian error linear unit (GELU)", "weight": 1.0} -->

Hendrycks and Gimpel also proposed to parameterize the GELU by µ and σ 2 -the parameters defining mean and variance of the Gaussian distribution whose CDF is used in the GELU, however, only the standard Gaussian distribution was used in experiments. Replacing ReLUs with GELUs led to better performance. More details about GELU are available.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Symmetrical Gaussian error linear unit (SGELU)", "weight": 1.0} -->

A symmetric variant of GELU called symmetrical Gaussian error linear unit (SGELU) was proposed. It is defined as where a is a fixed hyperparameter. The symmetrical nature of the SGELU also leads to more symmetrically distributed weights of the neural network compared to SGELU; it is believed that normal distribution of the weights can make the network more rational, accurate, and robust.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Cauchy linear unit (CaLU)", "weight": 1.0} -->

Another function related to the GELU and SiLU is the Cauchy linear unit (CaLU) which uses the CDF of the standard Cauchy distribution instead of the Gaussian CDF in GELU and logistic sigmoid in SiLU. It is defined as where Φ Cauchy (z) is the CDF of the standard Cauchy distribution.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Laplace linear unit (LaLU)", "weight": 1.0} -->

Another function related to the GELU and SiLU is the Laplace linear unit (LaLU) which uses the CDF of the Laplace distribution; it is defined as where Φ Laplace (z) is the CDF of the Laplace distribution.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Collapsing linear unit (LaLU)", "weight": 1.0} -->

The Collapsing linear unit (CoLU) is an AF similar to the SiLU proposed. It is defined as

<!-- chunk {"id": "body-0061", "role": "body", "section": "Triple-state swish", "weight": 1.0} -->

The triple-state swish unit (TS-swish) 6 is a cascaded AF similar to TS-sigmoid (see section 3.2.6); it is defined as where a and b are fixed parameters.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Generalized swish", "weight": 1.0} -->

A SiLU variant called generalized swish 7 was proposed. It is defined as

<!-- chunk {"id": "body-0063", "role": "body", "section": "Exponential swish", "weight": 1.0} -->

Another SiLU variant called exponential swish 8 was proposed. It is defined as

<!-- chunk {"id": "body-0064", "role": "body", "section": "Derivative of sigmoid function", "weight": 1.0} -->

The derivative of logistic sigmoid was used as an AF. Koçak and Üstünda˘ g ¸ Siray formulate the AF using the following form

<!-- chunk {"id": "body-0065", "role": "body", "section": "Gish", "weight": 1.0} -->

Gish is another SiLU variant; the gish is defined as Kaytan, Aydilek, and Yero˘ glu found that gish outperformed logistic sigmoid, softplus, ReLU, LReLU, ELU, swish, mish, logish, and smish on the MNIST and CIFAR-10 datasets.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Logish", "weight": 1.0} -->

Logish is yet another SiLU variant; it is defined as 6 Koçak and Üstünda˘ g ¸ Siray called the function swish but it is actually based on the SiLU.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Logish", "weight": 1.0} -->

7 Also based on the SiLU instead of its adaptive variant swish.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Logish", "weight": 1.0} -->

8 Again, based on the SiLU instead of its adaptive variant swish.

<!-- chunk {"id": "body-0069", "role": "body", "section": "LogLogish", "weight": 1.0} -->

LogLogish is a SiLU variant based on the LogLog (see section 3.2.20); it is defined as

<!-- chunk {"id": "body-0070", "role": "body", "section": "Self arctan", "weight": 1.0} -->

The self arctan is an AF proposed in whose formula resembles the SiLU. The self arctan is defined as where tan -1 (z) is the arctangent function.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Parametric logish", "weight": 1.0} -->

Zhu et al. also proposed a parametric variant of logish - we will call it parametric logish (pLogish) in this work. It is defined as where a and b are fixed parameters; Zhu et al. used a = 1 and b = 10.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Phish", "weight": 1.0} -->

Phish is a SiLU variant combining GELU and tanh; it is defined as The phish was found to outperform GELU, tanh, logistic sigmoid, and ReLU; it performed similarly as the mish and swish in the experiments.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Suish", "weight": 1.0} -->

The suish was proposed as an alternative to the swish AF. It is defined as

<!-- chunk {"id": "body-0074", "role": "body", "section": "Tangent-sigmoid ReLU (TSReLU)", "weight": 1.0} -->

The tangent-sigmoid ReLU (TSReLU) is an AF very similar to phish, mish, and TanhExp - it just uses the logistic sigmoid instead of the GELU in phish, softplus in mish, and the exponential in TanhExp. It is defined as

<!-- chunk {"id": "body-0075", "role": "body", "section": "Tangent-bipolar-sigmoid ReLU (TBSReLU)", "weight": 1.0} -->

The tangent-bipolar-sigmoid ReLU (TBSReLU) is a variant of TSReLU proposed. It is defined as

<!-- chunk {"id": "body-0076", "role": "body", "section": "Log-sigmoid", "weight": 1.0} -->

A logarithm of the logistic sigmoid is sometimes used as an activation function. It is defined as

<!-- chunk {"id": "body-0077", "role": "body", "section": "Derivative of sigmoid-weighted linear unit (dSiLU)", "weight": 1.0} -->

The derivative of sigmoid-weighted linear unit (dSiLU) can also be used as an activation function resembling a sigmoid. It is defined as where σ (z) is the logistic sigmoid. The dSiLU has a maximum value of around 1.1, and the minimum is approximately -0.1.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Double sigmoid-weighted linear unit (DoubleSiLU)", "weight": 1.0} -->

The double sigmoid-weighted linear unit (DoubleSiLU) 9 is an AF proposed. It is defined as where σ (z) is the logistic sigmoid.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Modified sigmoid-weighted linear unit (MSiLU)", "weight": 1.0} -->

A modified sigmoid-weighted linear unit (MSiLU) is a variant of the SiLU that has faster convergence than the SiLU. It is defined as where σ (z) is the logistic sigmoid.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Hyperbolic tangent sigmoid-weighted linear unit (TSiLU)", "weight": 1.0} -->

Another SiLU variant is the hyperbolic tangent sigmoid-weighted linear unit (TSiLU), which combines the tanh and SiLU. It is defined 10 as

<!-- chunk {"id": "body-0081", "role": "body", "section": "Arctan sigmoid-weighted linear unit (ASiLU)", "weight": 1.0} -->

Arctan sigmoid-weighted linear unit (ATSiLU) is yet another SiLU variant proposed; it is defined as

<!-- chunk {"id": "body-0082", "role": "body", "section": "SwAT", "weight": 1.0} -->

Verma, Chug, and Singh proposed an AF named SwAT combining the SiLU and arctan. This function is defined as

<!-- chunk {"id": "body-0083", "role": "body", "section": "Rectified hyperbolic secant", "weight": 1.0} -->

Arectified hyperbolic secant activation function was proposed. This function is totally differentiable, symmetric about the origin, and is approaching zero for inputs going to positive or negative infinity: where sech(z) is the hyperbolic secant function.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Rectified hyperbolic secant", "weight": 1.0} -->

9 Verma, Chug, and Singh termed the unit as DSiLU but that would collide with the dSiLU (see section 3.3.21) proposed earlier by Elfwing, Uchibe, and Doya.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Rectified hyperbolic secant", "weight": 1.0} -->

10 The formula in was wrong as it evaluated to 2 x 0, we present the formula we think authors intented.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Linearly scaled hyperbolic tangent (LiSHT)", "weight": 1.0} -->

A linearly scaled hyperbolic tangent (LiSHT) activation function was proposed in to address the problem of vanishing gradients and the non-utilization of large negative input values. The LiSHT function is defined as The output range of LiSHT function is [0, ∞].The output of LiSHT is close to the ReLU (see section 3.6) and swish for large positive values; however, unlike the aforementioned AFs, the output is symmetric, and, therefore, it behaves identically for large negative values. While the LiSHT is symmetric, the fact that its output is unbounded and non-negative could be considered a disadvantage. The effectiveness of the LiSHT activation function was tested on several different architectures ranging from multilayer perceptron (MLP) and residual neural networks to LSTM-based networks and on various tasks - the Iris dataset, the MNIST, CIFAR-10 and CIFAR-100 and the sentiment140 dataset from Twitter for sentiment analysis.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Linearly scaled hyperbolic tangent (LiSHT)", "weight": 1.0} -->

A parametric version of LiSHT named SoftModulusT (see section 3.6.31) was proposed.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Mish", "weight": 1.0} -->

A popular activation function mish is a combination of the tanh and softplus activation function; the function resembles swish activation (see section 4.4.1). It is defined as Mish was found to outperform swish; it performed similarly to f (z) = z · ln (1 + tanh (exp (z))) but this activation function was found to often lead to unstable training. The mish was found to outperform swish and ReLU for many architectures such as various ResNet architectures, Inception v3, DenseNet-121, and others. Detailed comparison with other activation functions was run using the Squeeze Net where it outperformed swish, GELU, ReLU, ELU, LReLU, SELU, softplus, S-shaped ReLU (SReLU), inverse square root unit (ISRU), tanh, and randomized leaky ReLU (RReLU). The mish activation function was, for example, used in the YOLOv4 and its variant Scaled-YOLOv4.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Smish", "weight": 1.0} -->

The smish is a variant of the mish where the exponential function is replaced by the logistic sigmoid. It is, therefore, defined as where a and b are parameters; however, Wang, Ren, and Wang recommend a = 1 and b = 1 based on a small parameter search.

<!-- chunk {"id": "body-0090", "role": "body", "section": "TanhExp", "weight": 1.0} -->

Similarly as the mish is the combination of tanh and softplus, the TanhExp is a combination of tanh and the exponential function. It is defined as

<!-- chunk {"id": "body-0091", "role": "body", "section": "Serf", "weight": 1.0} -->

The serf is an AF similar to the mish; however, it uses the error function instead of the tanh. It is defined as where erf is the Gauss error function. It was found to outperform mish, GELU, and ReLU for various architectures on Multi30K, ImageNet, the CIFAR-10, and CIFAR-100 datasets; see for details.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Efficient asymmetric nonlinear activation function (EANAF)", "weight": 1.0} -->

An activation function combining tanh and softplus called efficient asymmetric nonlinear activation function (EANAF) was proposed. The function is defined as where h(z) is the softplus function and g(z) = tanh (z 2), which can be simplified to The EANAF is continuously differentiable. The EANAF is very similar to swish with similar amount of computation but Chai et al. found that it performs better than swish and several other activation functions in RetinaNet and YOLOv4 architectures on object detection tasks.

<!-- chunk {"id": "body-0093", "role": "body", "section": "SinSig", "weight": 1.0} -->

SinSig is a self-gated non-monotonic activation function defined as where σ (z) is the logistic sigmoid function. While SinSig is similar to swish and mish, it outperformed them in experiments in as the number of layers in a neural network increased. It was also shown that the SinSig converges faster. The SinSig outperformed ReLU and mish on several deep architectures including ResNet 20 v2, ResNet 110 v2, SqueezeNet, and ShuffleNet among others on the CIFAR-100 task in experiments.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Gaussian error linear unit with sigmoid activation function (SiELU)", "weight": 1.0} -->

The with sigmoid activation function (SiELU) was proposed; it is defined as

<!-- chunk {"id": "body-0095", "role": "body", "section": "Gated linear unit (GLU)", "weight": 1.0} -->

A gated activation called gated linear unit (GLU) similar to SiLU (see section 3.3) for use in recurrent neural networks (RNNs) was proposed. The GLU is defined as where ⊗ is the element-wise product and z and z ′ are two learned linear transformations of input vector x.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Gated tanh unit (GTU)", "weight": 1.0} -->

A gated activation called gated tanh unit (GTU) similar to GLU (see section 3.4) for use in RNNs was proposed. The GTU is defined as where ⊗ is the element-wise product and z and z ′ are two learned linear transformations of input vector x.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Gated ReLU (ReGLU)", "weight": 1.0} -->

Another GLU extension is the gated (ReGLU). The ReGLU is defined as where ⊗ is the element-wise product and z and z ′ are two learned linear transformations of input vector x.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Gated GELU (GEGLU)", "weight": 1.0} -->

A GELU-based GLU extension is the gated (GEGLU); it is defined as where ⊗ is the element-wise product and z and z ′ are two learned linear transformations of input vector x.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Swish GELU (SwiGLU)", "weight": 1.0} -->

A swish-based GLU extension is the gated swish (SwiGLU); it is defined as where ⊗ is the element-wise product, z and z ′ are two learned linear transformations of input vector x, and swish is the swish with its own trainable parameter.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Softmax", "weight": 1.0} -->

The softmax is not a usual type of AF taking in a single value, but it takes all the output value of the unit i and, also, the output values of other units in order to compute a soft argmax of the values. It is defined as where f (z j) is the output of a neuron j in a softmax layer consisting of N neurons.

<!-- chunk {"id": "body-0101", "role": "body", "section": "β -softmax", "weight": 1.0} -->

The β -softmax is a softmax extension proposed; it is defined as where f (z j) is the output of a neuron j in a softmax layer consisting of N neurons and b takes random value from N + 11.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Rectified linear function (ReLU)", "weight": 1.0} -->

The rectified linear unit (ReLU) is widely regarded as the most popular activation function in modern feedforward networks due to its simplicity and improved performance. It has been observed that ReLUs can significantly expedite the convergence of stochastic gradient descent. Additionally, traditional ReLUs are computationally less expensive compared to activation functions like the logistic or tanh functions. ReLUs often outperform sigmoidal activation functions. However, a drawback of ReLUs is the potential for neurons to become "dead" or "disabled" during training. This means that they may never activate again for any input, resulting in a permanently zero output gradient. This issue can occur after a weight update when a large gradient flows through the unit. This might happen after a weight update after a large gradient flows through the unit. However, ReLUs often lead to faster convergence than for sigmoid activation, as shown. It can also be shown that ReLUs and rational function efficiently approximate each other. The ReLU was used as an example of the more general class of piecewise affine AFs for neural network verification 12 using theorem provers.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Rectified linear function (ReLU)", "weight": 1.0} -->

A ReLU is mathematically defined as the maximum of zero and the input value: ReLU is commonly recommended as the default choice for feedforward networks due to its usually superior performance compared to sigmoidal functions and its computational efficiency; furthermore, it works comparably to its modifications. Many popular NN models utilize ReLU as the activation function of choice, e.g.,.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Rectified linear function (ReLU)", "weight": 1.0} -->

Many ReLU modification and derivations were proposed - e.g. leaky ReLU (LReLU), very leaky ReLU (VLReLU), parametric ReLU, randomized leaky ReLU (RReLU) or S-shaped ReLU. Smoothed modifications are, for example, exponential linear unit and softplus. Most of the modifications solve the problem of dying out neurons as they allow for gradient flows for any input.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Shifted ReLU", "weight": 1.0} -->

A Shifted ReLU is a simple translation of a ReLU and is defined as 11 No further specification was provided.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Shifted ReLU", "weight": 1.0} -->

12 More details are out of the scope of this work, see for more details.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Leaky ReLU (LReLU)", "weight": 1.0} -->

Leaky ReLU (LReLU) is defined as where a ∈ (1, ∞) is set to large number; 13 the recommended setting from is a = 100.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Leaky ReLU (LReLU)", "weight": 1.0} -->

LReLU solves the problem of dying neurons when neurons have permanently zero output gradient in classical ReLU by "leaking" the information for z < 0 instead of outputting exact zero. Both ReLU and LReLU can be considered to be a special case of the maxout unit (see section 4.47). A theoretical analysis of the ReLU and LReLU is available.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Leaky ReLU (LReLU)", "weight": 1.0} -->

Very leaky ReLU (VLReLU) is almost identical to the LReLU but has much higher slope when the z is negative for faster training by setting a i = 3. While it can be considered as a special case of LReLU, some researchers consider it as a separate case, e.g.,.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Leaky ReLU (LReLU)", "weight": 1.0} -->

The so-called optimized leaky ReLU (OLReLU) propose another reformulation of LReLU and calculation of the slope parameter a that is inspired by the RReLU (see section 3.6.3): where u and l are hyperparameters of the bounds of the RReLU.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Randomized leaky ReLU (RReLU)", "weight": 1.0} -->

RReLU is a leaky ReLU where the leakiness is stochastic during the training, i.e.: where a i is a sampled for each epoch and neuron i from the uniform distribution: a i ∼ U (l, u) where l < u and l, u ∈ (0, ∞). Similarly as in the dropout approach, an average over all a i over is taken during inference phase - the a i is set to l + u 2: Recommended distribution is U for sampling the a i.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Softsign randomized leaky ReLU (S-RReLU)", "weight": 1.0} -->

The softsign randomized leaky ReLU (S-RReLU) 14 is a RReLU combined with the softsign proposed. It is defined as where a i is a sampled for each epoch and neuron i from the uniform distribution: a i ∼ U (l, u) where l < u and l, u ∈ (0, ∞). Elakkiya and Dejey used l = 1 8 and u = 1 3.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Softsign randomized leaky ReLU (S-RReLU)", "weight": 1.0} -->

13 Depending on the source, researchers use either this form z a or the inverted form az for the negative inputs.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Softsign randomized leaky ReLU (S-RReLU)", "weight": 1.0} -->

14 Elakkiya and Dejey used S-RReLU as a name and not an abbreviation; however, since S-RReLU is a combination of the softsign and RReLU, we feel that using it as an abbreviation is appropriate.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Sloped ReLU (SlReLU)", "weight": 1.0} -->

A Sloped ReLU (SlReLU) is similar to the LReLU - whereas the LReLU parameterizes the slope for negative inputs, the SlReLU parameterizes the slope of ReLU for positive inputs. It is, therefore, defined as where a is a fixed, predetermined parameter. Seo, Lee, and Kim recommended a ∈ based on their experiments.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Noisy ReLU (NReLU)", "weight": 1.0} -->

A stochastic variant of the ReLU called noisy ReLU (NReLU) was proposed: where a is a stochastic parameter a ∼ N(0, σ (z)), N (0, σ 2) is the Gaussian distribution with zero mean and variance σ 2 and σ (z) is the standard deviation of the inputs z. The NReLU was designed for use with Restricted Boltzmann machines. More details about the NReLU is available.

<!-- chunk {"id": "body-0117", "role": "body", "section": "SineReLU", "weight": 1.0} -->

The SineReLU is a ReLU based activation that uses trigonometric functions for negative inputs. It is defined as where a is a fixed parameter.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Minsin", "weight": 1.0} -->

The minsin is a ReLU-based AF used. It is defined as

<!-- chunk {"id": "body-0119", "role": "body", "section": "Variational linear unit (VLU)", "weight": 1.0} -->

The variational linear unit (VLU) is an AF combining the ReLU and sine functions proposed. It is defined as where a and b are fixed parameters.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Spatial context-aware activation (SCAA)", "weight": 1.0} -->

The spatial context-aware activation (SCAA) is a ReLU extension proposed. The ReLU performs an elementwise max operation on the feature map X: where ReLU(X) is the ReLU in the matrix notation and 0 is a matrix of zeroes with the same shape as X. The SCAA first applies a depth-wise convolution on X to produce spatial context aggregated feature map denoted f DW (X) and then proceeds with the elementwise max operation; the SCAA is, therefore, defined as

<!-- chunk {"id": "body-0121", "role": "body", "section": "Randomly translational ReLU (RT-ReLU)", "weight": 1.0} -->

A randomly translational ReLU (RT-ReLU) is a ReLU with a randomly added jitter during each iteration of the training process. It is defined as where a i is stochastic parameter for each neuron i randomly sampled from the Gaussian distribution at each iteration, a i ∼ N (0, σ 2), where σ 2 is the variance of the Gaussian distribution. The authors Cao et al. set the σ 2 = 0. 75 2 for their experiments. The a i is set to 0 during the test phase.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Natural-Logarithm-ReLU (NLReLU)", "weight": 1.0} -->

The natural-logarithm-ReLU (NLReLU) introduces non-linearity to ReLU similarly as rectified linear tanh (ReLTanh) (see section 4.2.36) but only for positive part of the activation function: where a is a predefined constant.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Softplus linear unit (SLU)", "weight": 1.0} -->

An activation function softplus linear unit (SLU) combining the ReLU with the softplus activation function was proposed; the function is based around the assumption that zero mean activations improve learning performance. The SLU is defined as where a i, b i, and c i are predefined parameters; however, to ensure that the function is continuous, differentiable at zero and to avoid vanishing or exploding gradients, its parameters are set to a = 1, b = 2, and c = 2ln. The SLU is therefore equal to

<!-- chunk {"id": "body-0124", "role": "body", "section": "Rectified softplus (ReSP)", "weight": 1.0} -->

Another activation function combining ReLU and softplus called rectified softplus (ReSP) was proposed. The function is defined as where a is a fixed hyperparameter controlling the slope. Larger values of a between 1.4 and 2.0 were found to work well.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Parametric rectified non-linear unit (PReNU)", "weight": 1.0} -->

A ReLU variant called parametric rectified non-linear unit (PReNU) replaces the linear part of the ReLU for positive inputs by a non-linear function similarly to RePU (see section 3.6.39). It is defined as where a is a fixed hyperparameter - however, this parameter could be adaptive similarly as in PReLU (see section 4.2.1) that PReNU extends since Jaafari, Ellahyani, and Charfi thought of the PReLU as non-adaptive function for some reason.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Bounded ReLU (BReLU)", "weight": 1.0} -->

A BReLU is a variant of ReLU that limits the output as the unlimited output of the original ReLU might lead to an instability. It is defined as where a is a predefined parameter. The BReLU appeared later in the literature under the name ReLUN, where it seems that it was independently proposed.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Hard sigmoid", "weight": 1.0} -->

A Hard sigmoid is very similar to BReLU; it is a very crude approximation of the logistic sigmoid and is commonly defined as Other definitions are sometimes used; e.g. variant from is defined as While the Hard sigmoid is not as commonly used as the logistic sigmoid, it can be used, for example, in binarized neural network with stochastic activation functions - the binaryized neural networks can lead to much faster inference than regular neural networks, e.g., Courbariaux et al. reached up to 7 × speed up without any loss in classification accuracy (however, even better speed-ups can be obtained using, for example, field-programmable gate array (FPGA) implementations as in).

<!-- chunk {"id": "body-0128", "role": "body", "section": "HardTanh", "weight": 1.0} -->

The HardTanh is another piecewise linear function; it is very similar to Hard sigmoid, but it approximates the tanh instead of the logistic sigmoid. It is defined as where a and b are fixed parameters; Liu et al. used a = -1 and b = 11. NNs with HardTanhs are more suitable for linear predictive control than NNs with ReLUs as they usually require less hidden layers and neurons for representing identical min-max maps.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Shifted HardTanh", "weight": 1.0} -->

Kim et al. proposed HardTanh variants with vertical and horizontal shifts. The SvHardTanh 15 is defined as where a is a fixed parameter. Kim et al. used HardTanh variant with thresholds -1 and 1; a more general variant with parametric thresholds from eq. could be defined similarly.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Shifted HardTanh", "weight": 1.0} -->

The SvHardTanh is defined as where a is a fixed parameter.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Shifted HardTanh", "weight": 1.0} -->

The ShHardTanh is defined as where a is a fixed parameter.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Shifted HardTanh", "weight": 1.0} -->

Kim et al. used HardTanh variant with thresholds -1 and 1; more general variants of SvHardTanh and ShHardTanh with parametric thresholds from eq. could be defined similarly.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Hard swish", "weight": 1.0} -->

A linearized variant of the swish AF (see section 4.4.1) was proposed. It is defined as The linearization allows for more efficient computation.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Hard swish", "weight": 1.0} -->

15 Both SvHardTanh and ShHardTanh are named using the same convention as shifted ELUs (see section 4.2.56) for the purposes of this work.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Truncated rectified (TRec) activation function", "weight": 1.0} -->

The truncated rectified (TRec) AF is a truncated variant of the ReLU. It resembles onesided variant of the Hardshrink (see section 3.6.22) - it is defined as where a is a fixed parameter. Konda, Memisevic, and Krueger used a = 1 for most of their experiments.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Hardshrink", "weight": 1.0} -->

The Hardshrink (named thresholded linear AF in 16) is very similar to Hard sigmoid, TRec, and other piecewise linear functions; it is defined as where a > 0 is a fixed parameter.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Softshrink", "weight": 1.0} -->

The Softshrink is an AF similar to the Hardshrink used. It is defined as where a > 0 is a fixed thresholding parameter.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Bounded leaky ReLU (BLReLU)", "weight": 1.0} -->

Similarly as the BReLU is a bounded variant of the ReLU, the bounded leaky ReLU (BLReLU) is a bounded variant of LReLU (see section 3.6.2). It is defined as where a and b are predefined parameters and c is computed such that b = ab + c, i.e. c = (1 -a) b. The parameter a controls the leakiness, the parameter b is the threshold of saturation, and c is computed such that the function is continuous.

<!-- chunk {"id": "body-0139", "role": "body", "section": "V-shaped ReLU (vReLU)", "weight": 1.0} -->

A V-shaped variant of ReLU called V-shaped ReLU (vReLU) is proposed in and tackles the problem of dying neurons that is present with ReLUs. The vReLU is identical to the absolute value function and is defined as The output range of vReLU is [0, ∞). The modulus activation function later proposed in the literature by Vallés-Pérez et al. in is identical to the vReLU. The absolute value function was used as an AF also.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Pan function", "weight": 1.0} -->

The pan function is an AF similar to the vReLU and Softshrink. It is defined as where a is a fixed boundary parameter.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Pan function", "weight": 1.0} -->

16 Konda, Memisevic, and Krueger proposed it as a novel AF but it was already proposed.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Absolute linear unit (AbsLU)", "weight": 1.0} -->

The absolute linear unit (AbsLU) is a ReLU-based AF similar to the vReLU. It is defined as where a ∈ is a fixed hyperparameter.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Mirrorer rectified linear unit (mReLU)", "weight": 1.0} -->

The mirrored rectified linear unit (mReLU) is a bounded AF that suppresses the output for unusual inputs. It is defined as

<!-- chunk {"id": "body-0144", "role": "body", "section": "Leaky single-peaked triangle linear unit (LSPTLU)", "weight": 1.0} -->

An AF similar to vReLU, AbsLU, and tent activation named leaky single-peaked triangle linear unit (LSPTLU) was proposed. It is defined as where a is a fixed parameter. An identical AF was proposed under the name leaky rectified triangle linear unit (LRTLU).

<!-- chunk {"id": "body-0145", "role": "body", "section": "SoftModulusQ", "weight": 1.0} -->

The SoftModulusQ is a quadratic approximation of the vReLU proposed. The SoftModulusQ is defined as

<!-- chunk {"id": "body-0146", "role": "body", "section": "SoftModulusT", "weight": 1.0} -->

While the SoftModulusQ (see section 3.6.30) is a quadratic approximation of the vReLU (see section 3.6.25), the SoftModulusT is a tanh based approximation of the vReLU. It is basically a parametric version of the LiSHT activation function (see section 3.3.28): where a is a predetermined parameter; the authors Vallés-Pérez et al. used a = 0. 01 in their experiments. When a = 1, the SoftModulusT becames the LiSHT activation function.

<!-- chunk {"id": "body-0147", "role": "body", "section": "SignReLU", "weight": 1.0} -->

The combination of ReLU and softsign resulted in SignReLU that improves the convergence rate and alleviates the vanishing gradient problem. The SignReLU is defined as where a is a fixed parameter; the SignReLU becomes ReLU for a = 0. The SignReLU was independently proposed under the name DLU; 17 this name is sometimes used in the literature - e.g.,.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Li-ReLU", "weight": 1.0} -->

Elakkiya and Dejey proposed a combination of a linear function and the ReLU; they named the function Li-ReLU 18 and it is defined as where a i is a fixed parameter.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Concatenated ReLU (CReLU)", "weight": 1.0} -->

A concatenated ReLU (CReLU) is an adaptation of the ReLU function proposed based on the observation that filters in convolutional neural networks (CNNs) in the lower layers form pairs consisting of filters with opposite phase. The CReLU conserves both negative and positive linear responses after convolution by concatenating the output of two ReLUs (hence the name). The CReLU is a function R → R 2 and is defined as with the output range of [0, ∞) for both output elements.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Negative CReLU (NCReLU)", "weight": 1.0} -->

A CReLU extension named negative CReLU (NCReLU) was proposed; while it is very similar to CReLU, it multiplies the second element by -1: Very similar AF was proposed concurrently in under the name bipolar activation function (BAF). Unlike the NCReLU, it does not produce a vector output but is applied in an alternating manner similar to All-ReLU (see section 4.34) but for neurons instead of layers. It is defined for the i -th neuron as where g (z i) is any ReLU family AF and % is the modulo operation.

<!-- chunk {"id": "body-0151", "role": "body", "section": "DualReLU", "weight": 1.0} -->

Where CReLU activation functions takes a single value and outputs a vector of two values, the DualReLU takes two values as an input and outputs a single value. The DualReLU is a two-dimensional activation function meant as a replacement of the tanh activation function for Quasi-Recurrent neural networks. It is defined as

<!-- chunk {"id": "body-0152", "role": "body", "section": "Orthogonal permutation liner unit", "weight": 1.0} -->

The orthogonal permutation liner unit (OPLU) is not applied to a single neuron but always to a pair of neurons. First, the neurons are grouped into pairs of neurons { i, j } and the OPLU takes two inputs z i and z j of neurons i and j and produces the output for neuron i and

<!-- chunk {"id": "body-0153", "role": "body", "section": "Elastic ReLU (EReLU)", "weight": 1.0} -->

Another extension is the elastic ReLU (EReLU), which slightly randomly changes the slope of the positive part of the ReLU during the training. The EReLU is defined as where k i is a sampled for each epoch and neuron i from the uniform distribution: a i ∼ U (1 -α, 1+ α) where α ∈ is a parameter controlling the degree of response fluctuations. The EReLU thus complements the principle of RReLU, which randomly changes the leakiness during the training while keeping the positive part fixed, while the EReLU changes the positive part and keeps the output constantly zero for negative inputs. The EReLU sets the k i its expected value E(k i) which is equal to one - the EReLU becomes the ReLU during the test phase.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Power activation functions & rectified power units (RePU)", "weight": 1.0} -->

A power activation function extending ReLU together with a training scheme for better generalization was proposed. This activation function was later independently proposed under the name RePU. The RePU is defined as where a is a fixed parameter. The RePU is a generalization of several activation functions - it becomes the Heaviside step function for a = 0 and ReLU for a = 1; the case a = 2 is called rectified quadratic unit (ReQU) in and squared ReLU; finally, the case a = 3 is called rectified cubic unit (ReCU). The disadvantage of RePU is its unbounded and asymmetric nature and that it is prone to vanishing gradient. Theoretical analysis of the RePU is available.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Power activation functions & rectified power units (RePU)", "weight": 1.0} -->

However, Berradi recommends alternating using a = b and a = 1 b each epoch; i.e.: Then the activation function f 1 (z) is used during odd epochs and f 2 (z) during even epochs; their mean is used during the test phase. The value b > 1 was used in the experiments in b ∈ { 1. 05, 1. 1, 1. 15, 1. 20, 1. 25 }.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Approximate ReLU (AppReLU)", "weight": 1.0} -->

The approximate ReLU (AppReLU) 19 is the RePU with aditional scaling parameter; it is defined as

<!-- chunk {"id": "body-0157", "role": "body", "section": "Power linear activation function (PLAF)", "weight": 1.0} -->

The power linear activation function (PLAF) 20 is a class of two similar AFs proposed. The first, even power linear activation function (EPLAF), is defined as 19 Saha et al. used the abbreviation AReLU but this is already used for the Attention-based ReLU in this work.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Power linear activation function (PLAF)", "weight": 1.0} -->

20 Originally, Nasiri and Ghiasi-Shirazi named PLAF as PowerLinear AF. Also, its variants EPLAF and OPLAF were named as EvenPowLin and OddPowLin. and where d is a fixed parameter. Similarly, the second AF - odd power linear activation function (OPLAF) - is defined as where d is a fixed parameter. Nasiri and Ghiasi-Shirazi focused on the EPLAF in their work and showed that EPLAF with d = 2 performed similarly as the ReLU for some of the tasks but it performed significantly better for other tasks; the OPLAF was not experimentally validated.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Average biased ReLU (ABReLU)", "weight": 1.0} -->

Similarly as the RT-ReLU (see section 3.6.11), the average biased ReLU (ABReLU) uses horizontal shifting in order to handle negative values. It is defined as where a i is the average of input activation map to the neuron/filter i, which makes the function data dependent and adjusts the threshold based on the positive and negative data dominance. The output range is [0, ∞).

<!-- chunk {"id": "body-0160", "role": "body", "section": "Delay ReLU (DRLU)", "weight": 1.0} -->

The delay ReLU (DRLU) 21 is a function that also adds a horizontal shift to the ReLU; however, the DRLU uses a fixed, predetermined shift whereas RT-ReLU uses stochastic shifts (see section 3.6.11) and ABReLU computes the shift as the average of input activation map (see section 3.6.42). The DRLU is defined as where a is a fixed, predetermined parameter. Shan, Li, and Chen also add a constraint a > 0 and they used a ∈ { 0. 06, 0. 08, 0. 10 } in their experiments.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Displaced ReLU (DisReLU)", "weight": 1.0} -->

Very similar to the flexible ReLU (FReLU) (see section 4.2.15) and dynamic ReLU (DReLU) (see section 4.2.14) is the displaced ReLU (DisReLU) 22 as it also shifts the ReLU: where a is a predefined hyperparameter. A Shifted ReLU (see section 3.6.1) is a special case of DisReLU with a = 1. The VGG-19 with DisReLUs outperform the ReLU, LReLU, PReLU, and ELU activation functions with a statistically significant difference in performance on the CIFAR-10 and CIFAR-100 datasets as shown.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Modified LReLU", "weight": 1.0} -->

Inspired by the DisReLU, Yang et al. proposed the modified LReLU (MLReLU). The MLReLU is a translated LReLU and is defined as where a is a fixed parameter controlling both the slope and the threshold.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Modified LReLU", "weight": 1.0} -->

21 Authors termed the function DRLU; however, the usual notation in this work would be DReLU. Since such notation would collide with the dynamic ReLU, we will use the original notation from despite the inconsistency.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Modified LReLU", "weight": 1.0} -->

22 Macêdo et al. originally abbreviated the displaced ReLU as DReLU but that is already taken by dynamic ReLU from section 4.2.14.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Flatted-T swish", "weight": 1.0} -->

An activation function flatted-T swish (FTS) combines ReLU and the logistic sigmoid activation function; it is defined as where T is a predefined hyperparameter, the recommended value is T = -0. 20. The FTS is identical to a shifted swish for the positive z. The FTS was shown to outperform ReLU, LReLU, swish, ELU, and FReLU activation functions. The special case with T = 0 was proposed independently under the name of ReLU-Swish.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Optimal activation function (OAF)", "weight": 1.0} -->

The so-called Optimal Activation Functio (OAF) is a combination of ReLU and swish activations proposed. It is defined as

<!-- chunk {"id": "body-0167", "role": "body", "section": "Exponential linear unit (ELU)", "weight": 1.0} -->

An ELU is an extension of LReLU where the function employs an exponential function for the negative inputs, which speeds up the learning process: where a is a hyperparameter; the authors Clevert, Unterthiner, and Hochreiter used a = 1 in their work. The a determines the value to which an ELU saturates for inputs going to negative infinity.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Rectified exponential unit (REU)", "weight": 1.0} -->

A rectified exponential unit (REU) is an activation function inspired by the ELU and swish (see sections 3.6.48 and 4.4.1) and is based on the assumption that the success of the swish activation functions is due to the non-monotonic property in the negative quadrant. The REU is defined as A parametric version called parametric rectified exponential unit (PREU) was also proposed; see section 4.2.9 for details.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Apical dendrite activation (ADA)", "weight": 1.0} -->

A biologically inspired AF named apical dendrite activation (ADA) was proposed. It is similar to the ELU, but it applies an exponential function for positive inputs. It is defined as where a and b are fixed parameters.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Leaky apical dendrite activation (LADA)", "weight": 1.0} -->

As LReLU extends the ReLU, the leaky apical dendrite activation (LADA) extends the ADA. where a, b, and c ∈ are fixed parameters. Georgescu et al. used c = 0. 01 in their experiments.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Sigmoid linear unit (SigLU)", "weight": 1.0} -->

The sigmoid linear unit (SigLU) 23 is an ELU alternative that uses a modified logistic sigmoid instead of the exponential. It is defined as

<!-- chunk {"id": "body-0172", "role": "body", "section": "Swish and ReLU activation (SaRa)", "weight": 1.0} -->

The swish and ReLU activation (SaRa) is an AF combining the swish and ReLU AFs proposed. It is defined 24 as where a and b are fixed parameters; Qureshi and Sarosh Umar recommend a = 0. 5 and b = 0. 7.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Maxsig", "weight": 1.0} -->

The maxsig is one of the AFs listed. The maxsig is similar to the SigLU (see section 3.6.52) and is defined as where σ (z) is the logistic sigmoid.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Tanh linear unit (ThLU)", "weight": 1.0} -->

The tanh linear unit (ThLU) 25 is an AF combining tanh and ReLU. It is defined as The ThLU is a special case of the tanh based ReLU (TReLU) with b i = 1 2. Similar AF was used under the name maxtanh in - it just omitted the scaling factor. The maxtanh can also be written as f (z) = max(z, tanh (z)).

<!-- chunk {"id": "body-0175", "role": "body", "section": "DualELU", "weight": 1.0} -->

The DualELU is equivalent of DualReLU (see section 3.6.36) for ELUs and are defined as where f EL (z) is the ELU activation function applied to an input z.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Difference ELU (DiffELU)", "weight": 1.0} -->

An ELU variant named difference exponential linear unit (DiffELU) 26 was proposed. It is defined as where a and b ∈ are fixed parameters. Hu et al. also tested setting the parameters to be trainable but that led to worse performance. The recommended setting is a = 0. 3 and b = 0. 1.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Difference ELU (DiffELU)", "weight": 1.0} -->

23 The AF is unnamed in the original work.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Difference ELU (DiffELU)", "weight": 1.0} -->

24 The formula in is malformed; we believe that this is the intended case. It is possible that authors intended that the SaRa is actually only the part that is defined for the negative inputs in eq. - however, we think that it is less likely as that would be only a swish (see section 4.4.1) AF with some fixed scaling of the output or the AHAF (see section 4.4.2) with fixed parameters.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Difference ELU (DiffELU)", "weight": 1.0} -->

25 The ref is not the original work with ThLUs; it references another work but that uses pure tanh as the AFs.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Difference ELU (DiffELU)", "weight": 1.0} -->

26 Hu et al. used the abbreviation DELU but this name is used for the AF proposed by Pishchik in throughout this work.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Polynomial linear unit (PolyLU)", "weight": 1.0} -->

The polynomial linear unit (PolyLU) is an AF similar to the ELU proposed. It is defined as Despite the similarity with the ELU, Feng and Yang have shown that the PolyLU outperformed the ELU on the CIFAR-10/100 and Dogs vs. Cats datasets. The PolyLU was also proposed under the name first power linear unit with sign (FPLUS) 27.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Inverse polynomial linear unit (IpLU)", "weight": 1.0} -->

The polynomial linear unit (IpLU) was proposed; it is defined as where a > 0 is a fixed hyperparameter guaranteeing a small slope for negative inputs.

<!-- chunk {"id": "body-0183", "role": "body", "section": "Power linear unit (PoLU)", "weight": 1.0} -->

The power linear unit (PoLU) is an AF similar to the ELU. It is defined as where a is a fixed parameter. Li, Ding, and Li used a ∈ { 1, 1. 5, 2 } in their experiments.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Power function linear unit (PFLU)", "weight": 1.0} -->

The power function linear unit (PFLU) is an AF proposed; it is defined as

<!-- chunk {"id": "body-0185", "role": "body", "section": "Faster power function linear unit (FPFLU)", "weight": 1.0} -->

The faster power function linear unit (FPFLU) is an AF proposed in that resembles the IpLU (see section 3.7.5) It is defined as

<!-- chunk {"id": "body-0186", "role": "body", "section": "Elastic adaptively parametric compounded unit (EACU)", "weight": 1.0} -->

The elastic adaptively parametric compounded unit (EACU) is a stochastic AF. It is defined as where b i is stochastically sampled during training as and a i is an adaptive parameter for each neuron or channel i.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Elastic adaptively parametric compounded unit (EACU)", "weight": 1.0} -->

27 Duan, Yang, and Dai used the equivalent definition f ( z ) = (sgn ( z ) · z +1) sgn( z ) -1, hence the name.

<!-- chunk {"id": "body-0188", "role": "body", "section": "Lipschitz ReLU (L-ReLU)", "weight": 1.0} -->

A L-ReLU is a piecewise linear activation function. The slope of the negative part is selected with respect to a data-dependent Lipschitz constant. It builds on a proposed piecewise function that treats the positive z > 0 and negative values (z ≤ 0) separately: where ϕ (z) and µ (z) can be any function f: R → R. This makes the positive part of the piecewise lay in the first quadrant of the Cartesian coordinate system and the negative part in the third quadrant.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Scaled exponential linear unit (SELU)", "weight": 1.0} -->

A SELU was proposed in order to make the network self-normalize by automatically converging towards zero mean and unit variance. The ELU was chosen as the basis for self-normalizing neural networks (SNNs) because these cannot be derived with ReLUs, sigmoid, and tanh units or even LReLUs - the activation function has to have negative and positive values for controlling the mean, saturation region where derivatives approach zero in order to dampen the variance if it is too large, a slope larger than one in order to increase the variance if it is too small, and a continuous curve to ensure a fixed point where the variance dampening is balanced out by the variance increasing. The SELU is defined as where a > 1 and b are predefined parameters; the recommended values are a ≈ 1. 05078 and b ≈ 1. 6733.

<!-- chunk {"id": "body-0190", "role": "body", "section": "Leaky scaled exponential linear unit (LSELU)", "weight": 1.0} -->

A leaky variant of SELU called leaky scaled exponential linear unit (LSELU) was proposed in and is defined as where a > 1 and b are predefined parameters of the original SELU (see section 3.7.11), and c is a new, predefined parameter controlling the leakiness of the unit.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Scaled exponentially-regularized linear unit (SERLU)", "weight": 1.0} -->

The scaled exponentially-regularized linear unit (SERLU) is a modification of the SELU proposed; it is defined as where a > 0 and b > 0 are predefined parameters. An extension of this approach named ASERLU for bidirectional long short-term memory (BiLSTM) architectures was proposed.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Scaled scaled exponential linear unit (sSELU)", "weight": 1.0} -->

Additional scaling of the negative pre-activations was introduced in the scaled scaled exponential linear unit (sSELU): where a > 1 and b are predefined parameters of the original SELU (see section 3.7.11), and c is a new, predefined parameter controlling the scaling of the negative inputs to the unit.

<!-- chunk {"id": "body-0193", "role": "body", "section": "RSigELU", "weight": 1.0} -->

A parametric ELU variant called RSigELU is defined as where a is a predefined parameter, Kiliçarslan and Celik used 0 < a < 1 in their work. For a = 0, the RSigELU becomes ReLU. The RSigELU was shown to outperform ReLU, LReLU, softsign, swish, ELU, SEU, GELU, LISA, Hexpo and softplus on the MNIST dataset, Fashion MNIST and the IMDB Movie dataset; it still outperformed these activation functions on the CIFAR-10 dataset but it was outperformed by its variant RSigELUD.

<!-- chunk {"id": "body-0194", "role": "body", "section": "HardSReLUE", "weight": 1.0} -->

Another AF proposed by Kiliçarslan is the HardSReLUE. Kiliçarslan defined the AF as where a is a fixed slope parameter.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Exponential linear sigmoid squashing (ELiSH)", "weight": 1.0} -->

An activation function exponential linear sigmoid squashing (ELiSH) combines the swish (see section 4.4.1) and the ELU function. It is defined as

<!-- chunk {"id": "body-0196", "role": "body", "section": "Hard exponential linear sigmoid squashing (HardELiSH)", "weight": 1.0} -->

As ELiSH (see section 3.7.17) combines swish with ELU and linear function, the hard exponential linear sigmoid squashing (HardELiSH) combines the Hard sigmoid with ELU and linear function. It is defined as

<!-- chunk {"id": "body-0197", "role": "body", "section": "RSigELUD", "weight": 1.0} -->

The RSigELUD is a double parameter variant of the RSigELU (see section 3.7.15) that is defined as where a and b are predefined parameters, Kiliçarslan and Celik used 0 < a < 1 and 0 < b < 1 in their work. For a = b = 0, the RSigELUD becomes the ReLU the same as the RSigELU; however, for a = 0 and positive b, the function resembles the vanilla ELU.

<!-- chunk {"id": "body-0198", "role": "body", "section": "LS-ReLU", "weight": 1.0} -->

The LS-ReLU 28 is a ReLU-inspired AF proposed. It is defined as where a and b are fixed 29 parameters.

<!-- chunk {"id": "body-0199", "role": "body", "section": "LS-ReLU", "weight": 1.0} -->

29 Wang et al. do not specify whether the parameters are trainable or fixed.

<!-- chunk {"id": "body-0200", "role": "body", "section": "Square-based activation functions", "weight": 1.0} -->

Several square-based activation functions were proposed in for better computational efficiency, especially on low-power devices. The approach uses the square function to replace the potentially costly exponential function. These function leads to significantly more efficient computation when there is no hardware implementation of the exponential function. The efficiency gains can be further improved with a custom hardware operator which can be used for efficient hardware implementation of all of the activation functions of the square-based family. The usage of the AFs from the family can lead to performance gains of one order of magnitude compared to traditional AFs for both forward and backward passes (depends on the particular activation function and the usage of fixed or floating point representations).

<!-- chunk {"id": "body-0201", "role": "body", "section": "SQNL", "weight": 1.0} -->

Acomputationally efficient activation function was proposed; unlike many other sigmoidal functions, it uses the square operator instead of the exponential function in order to achieve better computational efficiency. The derivative of the function is linear, which leads to a less computationally costly computation of the gradient. The function is defined in (the original paper had several mistakes in the definition) as The SQNL 30 has bounded range. The performance of the SQNL was verified on several datasets from the UCI Machine Learning Repository and on the MNIST dataset; more details available.

<!-- chunk {"id": "body-0202", "role": "body", "section": "Square linear unit (SQLU)", "weight": 1.0} -->

Similarly as the SQNL (see section 3.8.1) uses square function to form a sigmoidal function to approximate tanh, the square linear unit (SQLU) uses square function to form a ELU-like activation function that is computationally efficient: The SQLU basically uses the negative part of the SQNL and replaces the positive part with a linear function.

<!-- chunk {"id": "body-0203", "role": "body", "section": "Square swish (squish)", "weight": 1.0} -->

Another example of the family of activation functions based on the square operator is the square swish (squish), which is an AF inspired by the swish and GELU (see section 3.3.1). It uses the square non-linearity in order to achieve good computational efficiency: While the squish was inspired by the swish and GELU activation functions, it is an approximation of neither.

<!-- chunk {"id": "body-0204", "role": "body", "section": "Square REU (SqREU)", "weight": 1.0} -->

Similarly as REU (see section 3.6.49) is a combination of the ReLU and swish activation functions, the square REU (SqREU) is a combination of ReLU and squish: 30 SQNL is not an abbreviation but rather a name given by Wuraola and Patel.

<!-- chunk {"id": "body-0205", "role": "body", "section": "Square softmax (SQMAX)", "weight": 1.0} -->

The square softmax (SQMAX) is a square-based replacement for the softmax, which is exponential-based. It is defined as where f (z j) is the output of a neuron j in a softmax layer consisting of N neurons and c = 4 is a predefined constant.

<!-- chunk {"id": "body-0206", "role": "body", "section": "Linear quadratic activation", "weight": 1.0} -->

Another square-based AF called linear quadratic activation (LinQ) was proposed. where a is a fixed parameter controlling the slope of the function's linear parts.

<!-- chunk {"id": "body-0207", "role": "body", "section": "Inverse square root linear unit (ISRLU)", "weight": 1.0} -->

Inverse square root linear unit (ISRLU) is an activation function similar to the ELU (see section 3.6.48). It has similar properties and a shape as ELU; however, it is faster to compute, leading to more efficient training and inference. It is defined as where a is a hyperparameter controlling the value to which the ISRLU saturates for negative inputs. While the authors state that the hyperparameter a could be trainable for each neuron i, only the non-trainable variant was analyzed. Carlile et al. analysed ISRLU with a = 1 and a = 3.

<!-- chunk {"id": "body-0208", "role": "body", "section": "Inverse square root unit (ISRU)", "weight": 1.0} -->

ISRU is an activation function meant to replace sigmoidal activation functions. It is defined as where a si a fixed hyperparameter controlling the saturation values; the parameter could be trainable similarly as in the ISRLU (see section 3.8.9) but only the nonadaptive variant was used.

<!-- chunk {"id": "body-0209", "role": "body", "section": "Modified Elliott function (MEF)", "weight": 1.0} -->

The modified Elliott function (MEF) is an AF inspired by the Elliott function (see section 3.2.15); it can also be considered to be a translated special case of the ISRU (see section 3.8.10) with a = 1. It is defined as

<!-- chunk {"id": "body-0210", "role": "body", "section": "Square-root-based activation function (SQRT)", "weight": 1.0} -->

A square-root-based activation function (SQRT) is a monotonically increasing, unbounded activation function proposed in with a similar structure as the earlier proposed logarithmic activation function (LAF) but with the square root function instead of the natural logarithm used in LAF. It is defined as The SQRT activation function was found to outperform both tanh and ReLU activation functions on the CIFAR-10 dataset in experiments.

<!-- chunk {"id": "body-0211", "role": "body", "section": "Square-root-based activation function (SQRT)", "weight": 1.0} -->

A parametric variant of the SQRT called S-shaped activation function (SSAF) was proposed independently. It is defined as √ where a is a fixed parameter.

<!-- chunk {"id": "body-0212", "role": "body", "section": "Bent identity", "weight": 1.0} -->

The bent identity is an AF approximating the ReLU; it can be seen as a fixed variant of the bendable linear unit (BLU) (see section 4.2.37) with a i = 1 2. It is defined as

<!-- chunk {"id": "body-0213", "role": "body", "section": "Saha-Bora activation function (SBAF)", "weight": 1.0} -->

A Saha-Bora activation function (SBAF) was proposed in to be used for the habitability classification of exoplanets. It employs two non-trainable parameters α and k, which were set to k = 0. 98 and α = 0. 5, where authors determined a stable fixed point.

<!-- chunk {"id": "body-0214", "role": "body", "section": "Logarithmic activation function", "weight": 1.0} -->

The logarithmic activation function (LAF) was proposed in (ref. from). According to, it is defined as The LAF was independently proposed under the name symlog.

<!-- chunk {"id": "body-0215", "role": "body", "section": "Logarithmic activation function", "weight": 1.0} -->

31 The AF was unnamed in the original papers; however, the work named it using the name of the original author. We keep the naming in this work.

<!-- chunk {"id": "body-0216", "role": "body", "section": "Symexp", "weight": 1.0} -->

The symexp is an activation function that is inverse of the logmoid activation unit (LAU). It is defined as

<!-- chunk {"id": "body-0217", "role": "body", "section": "Scaled polynomial constant unit (SPOCU)", "weight": 1.0} -->

The scaled polynomial constant unit (SPOCU) is a polynomial-based AF proposed. It is defined as and a > 0, b ∈, c > 0, and d ∈ [1, ∞) are fixed parameters satisfying additional conditions listed.

<!-- chunk {"id": "body-0218", "role": "body", "section": "Polynomial universal activation function (PUAF)", "weight": 1.0} -->

Similarly as the universal activation function (UAF) (see section 4.22), the polynomial (PUAF) 32 is able to approximate popular AFs such as the logistic sigmoid, ReLU, and swish. It is defined as where a, b and c are fixed parameters. The PUAF becomes the ReLU with a = 1, b = 0, and c = 0; the logistic sigmoid is approximated with a = 0, b = 5, and c = 10; finally, the swish is approximated using a = 1, b = 5, and c = 10.

<!-- chunk {"id": "body-0219", "role": "body", "section": "Softplus", "weight": 1.0} -->

The softplus function was proposed in and is defined as The softplus was used as an activation function in where it was used alongside with a ReLU. The advantage of softplus over ReLU is that it is smooth and it has a non-zero gradient for negative inputs; thus, it does not suffer from the phenomenon of dying out neurons that is common in networks with ReLU activations. The softplus was found to outperform ReLU for certain applications and architectures. A noisy variant was used for spiking neural networks.

<!-- chunk {"id": "body-0220", "role": "body", "section": "Parametric softplus (PSoftplus)", "weight": 1.0} -->

Parametric softplus (PSoftplus) is a softplus variant that allows for scaling and shifting using two additional parameters. The PSoftplus is defined as where a and b are fixed predetermined hyperparameters. The creation of the softplus was motivated by the assumption that activations with mean outputs close to zero can improve the performance of a neural network; since the output of the softplus is always positive, a shift parameter b was introduced to shift the mean output closer to zero. The slope controlling parameter a is used to adjust the function and the gradient disappearance or overflow during training. The recommended values are a = 1. 5 and b = ln.

<!-- chunk {"id": "body-0221", "role": "body", "section": "Parametric softplus (PSoftplus)", "weight": 1.0} -->

32 Hwang and Kim named the function only as the universal activation function but this name is already taken by the UAF by Yuen et al..

<!-- chunk {"id": "body-0222", "role": "body", "section": "Soft++", "weight": 1.0} -->

Another softplus extension Soft++ is a multiparametric nonsaturating nonlinear activation function proposed. It is defined as where a and b are fixed predetermined hyperparameters; however, Ciuparu, Nagy-D˘ abâcan, and Mure¸ san proposed they could be adaptable in future works. Multiple values of the parameters were used in the experiments, but a = 1 and b = 2 were found to work well; nevertheless, a hyperparameter optimization is recommended.

<!-- chunk {"id": "body-0223", "role": "body", "section": "Rand softplus (RSP)", "weight": 1.0} -->

A softplus variant rand softplus (RSP) introduces a stochastic parameter a l that is determined by the noise level of the input data. The RSP is defined as where a l is adapting to the input noise levels of each layer l -the exact procedure is described.

<!-- chunk {"id": "body-0224", "role": "body", "section": "Aranda-Ordaz", "weight": 1.0} -->

The Aranda-Ordaz AF was used in NNs. It is defined as where a > 0 is a fixed parameter. Essai Ali, Abdel-Raman, and Badry used a = 2 in their work.

<!-- chunk {"id": "body-0225", "role": "body", "section": "Bi-firing activation function (bfire)", "weight": 1.0} -->

A bi-firing activation function (bfire) was proposed in and is defined as where a is a predefined smoothing hyperparameter. The bfire is basically a smoothed variant of the later proposed vReLU (see section 3.6.25) as it becomes vReLU as a → 0.

<!-- chunk {"id": "body-0226", "role": "body", "section": "Bounded bi-firing activation function (bbfire)", "weight": 1.0} -->

A bounded variant of the bi-firing (bfire) activation function (see section 3.21) called bbfire was proposed; similarly as BReLU and BLReLU bounds ReLU and LReLU respectively (see sections 3.6.16 and 3.6.24), the bounded bi-firing function (bbfire) is defined as where a and b are predefined hyperparameters. The is symmetrical about the origin and has a near inverse-bellshaped activation curve. While authors of the original bfire solved potential numerical instabilities caused by the unboundedness by imposing a small L 1 penalty on the hidden activation values, the bbfire alleviates this problem explicitly without any need for such penalty.

<!-- chunk {"id": "body-0227", "role": "body", "section": "Piecewise Mexican-hat activation function (PMAF)", "weight": 1.0} -->

The piecewise Mexican-hat activation function (PMAF) was used; it is defined as where a is a fixed parameter - Liu, Zeng, and Wang used a = 4.

<!-- chunk {"id": "body-0228", "role": "body", "section": "Piecewise radial basis function (PRBF)", "weight": 1.0} -->

The piecewise (PRBF) was used; it is defined as where a and b are fixed parameters - Liu, Zeng, and Wang used a = 3 and b = 1.

<!-- chunk {"id": "body-0229", "role": "body", "section": "Comb-H-sine", "weight": 1.0} -->

A comb-H-sine is an activation function that was found using an evolutionary approach. It is defined as where sinh(x) is the hyperbolic sine, sinh -1 (x) is its inverse, and a is a predefined hyperparameter. This function was found to outperform ReLU, tanh, logistic sigmoid, and several other activation functions in LSTM models.

<!-- chunk {"id": "body-0230", "role": "body", "section": "Modified arcsinh", "weight": 1.0} -->

The modified arcsinh (m-arcsinh) AF was proposed in and is defined as Interestingly, the m-arcsinh can be used either as an AF in a NN or as a kernel function in the support vector machine (SVM).

<!-- chunk {"id": "body-0231", "role": "body", "section": "hyper-sinh", "weight": 1.0} -->

The hyper-sinh is an AF that uses the sinh and cubic functions; it is defined as

<!-- chunk {"id": "body-0232", "role": "body", "section": "Arctid", "weight": 1.0} -->

The arctid is an arctan-based AF used; it is defined as

<!-- chunk {"id": "body-0233", "role": "body", "section": "Sine", "weight": 1.0} -->

The sine with inputs scaled by π was used as an activation: It was, for example, used recently with a data-driven determination of a network's biases. Just the sine function without any scaling was used as an activation.

<!-- chunk {"id": "body-0234", "role": "body", "section": "Sine", "weight": 1.0} -->

Scaled sine with vertical shift was used; the used AF is defined as where a is a fixed parameter; a ∈ { 0. 2, 0. 8, 1. 2, 1. 8, 4 }.

<!-- chunk {"id": "body-0235", "role": "body", "section": "Cosine", "weight": 1.0} -->

A cosine activation was used in simulations; it was defined as

<!-- chunk {"id": "body-0236", "role": "body", "section": "Cosid", "weight": 1.0} -->

The cosid is one of the AFs listed. It is defined as

<!-- chunk {"id": "body-0237", "role": "body", "section": "Sinp", "weight": 1.0} -->

A parametric AF similar to the cosid was proposed in under the name sinp. 33 It is defined as where a is a fixed parameter. Chan et al. used a ∈ { 1, 1. 5, 2 }.

<!-- chunk {"id": "body-0238", "role": "body", "section": "Growing cosine unit (GCU)", "weight": 1.0} -->

Another cosine-based AF is the growing cosine unit (GCU) proposed. It is defined as Empirical evaluation of the performance of GCU compared to ReLU, PReLU, and mish is available; its brief evaluation with respect to the generation of NFTs is available.

<!-- chunk {"id": "body-0239", "role": "body", "section": "Amplifying sine unit (ASU)", "weight": 1.0} -->

The amplifying sine unit (ASU) is the sine equivalent of the GCU

<!-- chunk {"id": "body-0240", "role": "body", "section": "Sinc", "weight": 1.0} -->

The sinc is an older AF proposed. It is defined as A shifted variant was proposed under the name shifted sine unit (SSU). It is defined as

<!-- chunk {"id": "body-0241", "role": "body", "section": "Decaying sine unit (DSU)", "weight": 1.0} -->

The decaying sine unit (DSU) is a sinc based AF proposed. It is defined as

<!-- chunk {"id": "body-0242", "role": "body", "section": "Hyperbolic cosine linearized squashing function (HcLSH)", "weight": 1.0} -->

The hyperbolic cosine linearized squashing function (HcLSH) is an AF proposed; it is defined as

<!-- chunk {"id": "body-0243", "role": "body", "section": "Polyexp", "weight": 1.0} -->

The polyexp is an AF combining quadratic function and an exponential function; 34 it is defined as where a, b, c, and d are fixed parameters.

<!-- chunk {"id": "body-0244", "role": "body", "section": "Polyexp", "weight": 1.0} -->

33 Technically, the full name used by Chan et al. is SinP[ N ] but we ommited the parameter from the name of the AF.

<!-- chunk {"id": "body-0245", "role": "body", "section": "Polyexp", "weight": 1.0} -->

34 The is referenced as the origin of polyexp in but we have not seen the definition there.

<!-- chunk {"id": "body-0246", "role": "body", "section": "Exponential", "weight": 1.0} -->

The exponential was used as an AF. The AF was defined as

<!-- chunk {"id": "body-0247", "role": "body", "section": "E-Tanh", "weight": 1.0} -->

An AF named E-Tanh combining the exponential and tanh functions was proposed. It is defined as where a is a fixed scaling parameter.

<!-- chunk {"id": "body-0248", "role": "body", "section": "Evolved combination of tanh and ReLU", "weight": 1.0} -->

The combination of tanh and ReLU was found using neuroevolution in - while Vijayaprabakaran and Sathiyamurthy also mentioned other AFs, this combination led to the best performance on the HAR dataset using the long short-term memory (LSTM) units. The best-performing recurrent AF was See for evaluation details and for other top AFs.

<!-- chunk {"id": "body-0249", "role": "body", "section": "Wave", "weight": 1.0} -->

The wave is an AF combining quadratic function and an exponential function; 35 similarly as the polyexp but only with a single parameter; it is defined as and the regular AF was where a is a fixed parameter.

<!-- chunk {"id": "body-0250", "role": "body", "section": "Non-monotonic cubic unit (NCU)", "weight": 1.0} -->

A simple AF based on a third-degree polynomial was proposed. It is named non-monotonic cubic unit (NCU) and is defined as

<!-- chunk {"id": "body-0251", "role": "body", "section": "Triple", "weight": 1.0} -->

Another AF based on a third-degree polynomial called triple was proposed. It is defined as where a is a fixed parameter. Chen et al. tested values of a ∈ { 0. 1, 0. 5, 1, 2 } and observed that a = 1 reaches the best results.

<!-- chunk {"id": "body-0252", "role": "body", "section": "Shifted quadratic unit (SQU)", "weight": 1.0} -->

The shifted quadratic unit (SQU) is a simple non-monotonic AF defined as 35 The is referenced as the origin of wave in but we have not seen the definition there.

<!-- chunk {"id": "body-0253", "role": "body", "section": "Knowledge discovery activation function (KDAC)", "weight": 1.0} -->

Wang et al. proposed a special AF for knowledge discovery. This function named knowledge discovery activation function (KDAC) has two adaptive parameters a > 0 and b > 0 and one fixed parameter c. It is defined 36 as Wang et al. used fixed c = 0. 01.

<!-- chunk {"id": "body-0254", "role": "body", "section": "K-winner-takes-all activation function (k-WTA)", "weight": 1.0} -->

The k-winner-take-all (k-WTA) AF was used to improve adversarial robustness. It is defined as where f (z): R N → R N is the k-WTA AF and f (z) j its j -th element, z is the input to the AF, and k a fixed parameter.

<!-- chunk {"id": "body-0255", "role": "body", "section": "Volatility-based activation function (VBAF)", "weight": 1.0} -->

The volatility-based activation function (VBAF) 37 is an AF with multiple intputs proposed. It is meant for time-series forecasting and was used in a LSTM NN. It is defined as n is the number of time-series samples in the given period. Unfortunately, no more details about the application of the VBAF were provided; thus, it remains unclear whether the VBAF was applied only directly to the inputs, or it was used on intermediary representations of a NN.

<!-- chunk {"id": "body-0256", "role": "body", "section": "Chaotic activation functions", "weight": 1.0} -->

The chaotic activation functions (CAFs) listed in this work are AFs that use a recursive definition to produce a chaotic behavior.

<!-- chunk {"id": "body-0257", "role": "body", "section": "Chaotic activation functions", "weight": 1.0} -->

36 The original code by Wang et al. is available.

<!-- chunk {"id": "body-0258", "role": "body", "section": "Chaotic activation functions", "weight": 1.0} -->

37 Kayim and Yilmaz named the function originally only volatility activation function.

<!-- chunk {"id": "body-0259", "role": "body", "section": "Hybrid chaotic activation function", "weight": 1.0} -->

The hybrid chaotic activation function (HCAF) is a multi-output type of AF proposed. Neuron i in layer l takes an input z l i, applies the logistic sigmoid AF and then maps the outputs using logistic map function to individual outputs going to the neurons in layer l +1. Therefore, a single neuron in layer l emits a different activation value to each neuron in the layer l +1.

<!-- chunk {"id": "body-0260", "role": "body", "section": "Hybrid chaotic activation function", "weight": 1.0} -->

For a neuron i, the HCAF first applies the logistic sigmoid function to produce activation a i then the first value going to the neuron 1 in the following layer is calculated as and the output values going to the other neurons in the following layer are calculated recursively as where j is the number of a neuron in a following layer and r represents an excitatory rate in a neuron. Reid and Ferens used r = 4 as this value produces a chaotic behavior of the logistic map; generally, values below 0 or above 4 lead to the output to become unbounded, values between 0 and 1 lead to convergence toward the zero, values between 1 and 3 lead to convergence to a fixed number, values between 3 and 3.5 lead to a periodic solution and only values between 3.5 and 4 produce chaotic behavior.

<!-- chunk {"id": "body-0261", "role": "body", "section": "Fusion of chaotic activation function (FCAF)", "weight": 1.0} -->

Similarly as HCAF, also the fusion of chaotic activation function (FCAF) uses a recursive definition for computing the output of a neuron. The FCAF is defined 38 for hidden units as 39 and for the output units as where r, a, b, c, and d are fixed parameters; the suitable values for the parameter r are discussed in section 3.48.1 where an equivalent parameter is used.

<!-- chunk {"id": "body-0262", "role": "body", "section": "Cascade chaotic activation function (CCAF)", "weight": 1.0} -->

The cascade chaotic activation function (CCAF) was introduced in and is recursively defined for the neuron i +1 in a given layer using the preceding neuron i from the same layer as where a and b are two fixed parameter from the interval.

<!-- chunk {"id": "body-0263", "role": "body", "section": "Adaptive activation functions", "weight": 1.0} -->

The activation function introduces non-linearities to neural networks and is crucial for network's performance. Even though it might be suboptimal, the same activation function is usually used for the whole network or at least for all neurons in a single layer. Over the last few decades, there have been several attempts to use activation functions that might differ across neurons (e.g., ). The adaptive activation functions - i.e., functions that have a trainable parameter that changes their shape - have been receiving more attention recently (e.g., ) and might become a new standard in the field. One of the first descriptions of the general AAF approach is available in where Wu, Zhao, and Ding described an AF 40 that has one or more trainable parameters that are trained together with the rest of the network's weights. The simplest forms just add a parameter to a particular neural network that controls one of its properties (e.g., slope), while the more complex ones allow for the learning of a large number of activation functions (e.g., adaptive spline activation functions in ).

<!-- chunk {"id": "body-0264", "role": "body", "section": "Adaptive activation functions", "weight": 1.0} -->

38 Kabir et al. did not explicitly defined what the index i denotes but most likely it denotes the i -th neuron in a given layer.

<!-- chunk {"id": "body-0265", "role": "body", "section": "Adaptive activation functions", "weight": 1.0} -->

39 The formula given in probably missed a minus sign after the parameter a.

<!-- chunk {"id": "body-0266", "role": "body", "section": "Adaptive activation functions", "weight": 1.0} -->

40 The authors used the name trainable activation function (TAF) rather than the adaptive activation function (AAF) that is used throughout this work.

<!-- chunk {"id": "body-0267", "role": "body", "section": "Transformative adaptive activation function (TAAF)", "weight": 1.0} -->

The transformative adaptive activation function (TAAF) is a family of AFs that adds four adaptive parameters for scaling and translation of any given AF - as such, the TAAFs represent a simple framework with a small set of additional parameters that generalizes a lot of AAFs that are listed in this work. While there are even more general approaches such as the adaptive blending unit (ABU) (see section 4.48) that allows for a combination of several different activation functions, the TAAFs are conceptually simpler and add only four additional parameters. The TAAF is defined as where z i input to the AF, α i, β i, γ i, and δ i, are adaptive parameters for each neuron i. Therefore, the output of a neuron with TAAF with inputs x i is: where x i are individual inputs, w i are its weights, and n is the number of incoming connections. If there is no unit x i, then the parameter γ is equivalent to the bias term of the neuron. It was shown in that each of the four adaptive parameters statistically significantly improve the performance of the AF - this is not surprising as many of the AFs presented in this work use subset of these parameters.

<!-- chunk {"id": "body-0268", "role": "body", "section": "Transformative adaptive activation function (TAAF)", "weight": 1.0} -->

For example, equivalent of α is used in the positive PReLU (see section 4.2.2), equivalent of β in the swish (see section 4.4.1), and equivalent of γ and δ in the FReLU (see section 4.2.15).

<!-- chunk {"id": "body-0269", "role": "body", "section": "The ReLU-based family of adaptive functions", "weight": 1.0} -->

The are numerous ReLU extensions that are adaptive. Some of the adaptive activations have a non-adaptive counterpart - e.g., PReLU (see section 4.2.1), which is basically a LReLU with an adaptive parameter of leakiness.

<!-- chunk {"id": "body-0270", "role": "body", "section": "Parametric rectified linear unit (PReLU)", "weight": 1.0} -->

However, AAFs might be very useful even in the simplest form with a single added parameter - an AAF called PReLU was used to obtain a state-of-the-art result on the ImageNet Classification in 2015, the first surpassing human-level performance. The PReLU generalize the ReLU by adding a parameter that controls the slope of the activation function for negative inputs (the ReLU is constant at zero for negative inputs) that is learned with other weights: where a i is an optimized parameter for each neuron/filter i. The LReLU is essentially a PReLU but with the parameter a i fixed and not trainable (see section 3.6.2 for LReLU details). PReLUs are better than ReLUs for verification-friendly NNs.

<!-- chunk {"id": "body-0271", "role": "body", "section": "Positive parametric rectified linear unit (PReLU + )", "weight": 1.0} -->

The positive PReLU is an adaptive variant of the SlReLU (see section 3.6.5) proposed; it is also a special case of, for example, DPReLU, Dual Line, and piecewise linear unit (PiLU). It is defined as where a i is a trainable parameter.

<!-- chunk {"id": "body-0272", "role": "body", "section": "Margin Relu", "weight": 1.0} -->

The margin (MarReLU) 41 is an adaptive variant of the Shifted ReLU where the shift a i is determined as the channelby-channel expectation value of the negative response. It is defined as 41 Heo et al. abbreviated it as MReLU, but this abbreviation is used for the mirrored rectified linear unit (see section 3.6.28) in this work.

<!-- chunk {"id": "body-0273", "role": "body", "section": "Funnel parametric rectified linear unit (FunPReLU)", "weight": 1.0} -->

The funnel rectified linear unit (FunReLU) 42 and funnel (FunPReLU) are 2D AFs proposed. The FunReLU and FunPReLU introduce a spatial context into the AF by comparing the input to a funnel condition instead of the zero that is used as the threshold in ReLU and PReLU. The FunReLU is defined as where z c,m,n is the input on the c -th channel at the 2D spatial position m,n and t (z c,m,n) is the spatial context from a 3 × 3 window 43 and p c,h,w denotes the coefficients on this window. The FunPReLU is defined similarly. The FunReLU was, for example, used.

<!-- chunk {"id": "body-0274", "role": "body", "section": "React-PReLU (RPReLU)", "weight": 1.0} -->

The react- (RPReLU) is an adaptive variant of the PReLU with vertical and horizontal shifts; it is defined as where a c, b c, and c c are trainable parameters for each channel c and z i denotes the input to the neuron i in the channel c; a c controls the horizontal shift, b c controls the vertical shift, and c c is the slope parameter for negative inputs as in the original PReLU.

<!-- chunk {"id": "body-0275", "role": "body", "section": "Smooth activation unit (SAU)", "weight": 1.0} -->

The smooth activation unit (SAU) is a smoothed variant of the PReLU 44 using the convolution operation with the Gaussian function. It is defined as where ∗ is the convolution operation, PReLU a i is the PReLU 45 parametrized by a i 46 and ϕ b i (x) is the Gaussian function parameterized by b i inversely controlling the deviation of the function. The resulting AF is then where a i and b i are either fixed or trainable parameters.

<!-- chunk {"id": "body-0276", "role": "body", "section": "Smooth maximum unit (SMU)", "weight": 1.0} -->

The smooth maximum unit (SMU) is an AAF that uses a smooth approximation of the absolute value function. The SMU is defined as where a i and b i are learnable parameters. This smooth approximation of the absolute value function using the Gaussian error function could be used to create a whole class of AFs similarly as in section 4.55.

<!-- chunk {"id": "body-0277", "role": "body", "section": "Leaky Learnable ReLU (LeLeLU)", "weight": 1.0} -->

An adaptive LReLU variant named leaky learnable ReLU (LeLeLU) was proposed. It is a LReLU with learnable scaling parameter: where a i is a trainable parameter for each neuron i.

<!-- chunk {"id": "body-0278", "role": "body", "section": "Leaky Learnable ReLU (LeLeLU)", "weight": 1.0} -->

42 Ma, Zhang, and Sun originally named the unit FReLU but its abbreviation would collide with the flexible ReLU.

<!-- chunk {"id": "body-0279", "role": "body", "section": "Leaky Learnable ReLU (LeLeLU)", "weight": 1.0} -->

43 Other sizes were also tested in but Ma, Zhang, and Sun found 3 × 3 to work the best.

<!-- chunk {"id": "body-0280", "role": "body", "section": "Leaky Learnable ReLU (LeLeLU)", "weight": 1.0} -->

44 The principle could be, however, applied to other AFs.

<!-- chunk {"id": "body-0281", "role": "body", "section": "Leaky Learnable ReLU (LeLeLU)", "weight": 1.0} -->

45 Biswas et al. used the LReLU in the definition of the SAU but since they consider the parameter a i trainable, we stick to the usage of PReLU in the defintion.

<!-- chunk {"id": "body-0282", "role": "body", "section": "Leaky Learnable ReLU (LeLeLU)", "weight": 1.0} -->

46 To conform to the used definition of the PReLU unit, we will use the slope scaling by 1 a i even though authors originally used the a i for slope scaling of negative inputs.

<!-- chunk {"id": "body-0283", "role": "body", "section": "Parametric rectified exponential unit (PREU)", "weight": 1.0} -->

Similarly as PReLU extends the ReLU (see section 4.2.1), the PREU extends the swish and ELU inspired REU. It is defined as where a i and b i are trainable parameters for each neuron/filter i. The advantage of PREU is that it uses the negative information near zero - unlike the ReLU.

<!-- chunk {"id": "body-0284", "role": "body", "section": "Randomly translational PReLU (RT-PReLU)", "weight": 1.0} -->

A randomly translational PReLU (RT-PReLU) an equivalent extension to PReLU as is RT-ReLU to ReLU (see section 3.6.11). It is defined as where a i is a trainable parameter and b i is a stochastic parameter for each neuron i randomly sampled from the Gaussian distribution at each iteration, b i ∼ N (0, σ 2), where σ 2 is the variance of the Gaussian distribution. The offset b i is set to zero during the test phase. The authors Cao et al. set the σ 2 = 0. 75 2 for their experiments. It is also possible to have the parameter b i sampled for each neuron i, but the a i is shared by all neurons in a channel c.

<!-- chunk {"id": "body-0285", "role": "body", "section": "Probabilistic activation (ProbAct)", "weight": 1.0} -->

A probabilistic class of activation functions ProbAct that adds a random noise to any activation function. It is defined as where g (z) is any function (either fixed or trainable) defining the mean of the probabilistic activation, e ∼ N is a random value sampled from a standard normal distribution, and σ is either fixed or learnable parameter controlling the range of the perturbation. σ can be either a global learnable parameter or different for each neuron i. The ProbAct used in is a ReLU based ProbAct defined as which resembles NReLU (see section 3.6.6) that adds random noise for output values for the positive inputs z. A similar concept for sigmoid and tanh activation was used in (see section 4.18).

<!-- chunk {"id": "body-0286", "role": "body", "section": "Probabilistic activation (ProbAct)", "weight": 1.0} -->

The chaotic injections presented in represent a similar approach; however, the injections are not stochastic but rather defined using the chaos theory. Furthermore, Reid, Ferens, and Kinsner discuss several approaches for injections of a chaotic value s n into a ReLU: ReLU( z + s n ), ReLU( z · s n ), ReLU( z + z · s n ), ReLU( z ) + s n, ReLU( z ) · s n, ReLU( z ) + zs n, and ReLU( z ) + ReLU( z ) · s n.

<!-- chunk {"id": "body-0287", "role": "body", "section": "Adaptive offset activation function (AOAF)", "weight": 1.0} -->

Another ReLU variant with adaptive shift termed adaptive offset activation function (AOAF) was defined. The AOAF introduces two hyperparameters and one data-dependent adaptive parameter; it is defined as where b and c are predefined, fixed parameters and a i is the mean value of the inputs of neuron i. The recommended values for the parameters b and c are b = c = 0. 17 as it yielded the best image classification accuracy in the experiments.

<!-- chunk {"id": "body-0288", "role": "body", "section": "Dynamic leaky ReLU (DLReLU)", "weight": 1.0} -->

An error based dynamic leaky ReLU (DLReLU) was proposed in (under the name of Dynamic ReLU - DReLU -but this naming collides with DReLU established; see section 4.2.14 and section 4.56.3). The DLReLU is a LReLU where the leakiness depends on the test error from the previous epoch where a ∈ is a predefined parameter controlling the leakiness similarly as in LReLU (see section 3.6.2) and b t is a dynamic parameter computed for current training epoch t as the test erroch from the previous epoch t -1, i.e., b t = MSE t -1.

<!-- chunk {"id": "body-0289", "role": "body", "section": "Dynamic leaky ReLU (DLReLU)", "weight": 1.0} -->

A version exp-DLReLU was proposed to deal with deeper networks with more than seven hidden layers in order to avoid too large error values causing the training to fail: where c t = exp(-b t) = exp (MSE t -1).

<!-- chunk {"id": "body-0290", "role": "body", "section": "Dynamic leaky ReLU (DLReLU)", "weight": 1.0} -->

The advantage of DLReLU and exp-DLReLU is that the changes in leakiness are big at the beginning of the training due to higher test error and diminish towards the end. A similar effect could be obtained by a schedule of the leakiness parameter in the LReLU.

<!-- chunk {"id": "body-0291", "role": "body", "section": "Dynamic ReLU (DReLU)", "weight": 1.0} -->

Similar approach to the ABReLU is presented by the DReLU (not to be confused with identically named activations in), where a i is a threshold value that is computed as the midpoint of the range of input values for each batch; e.g., if the values range from -4 to 8, then a i = -4+8 2 = 2. The DReLU can be considered to be a variant of DisReLU (see section 3.6.44) with data-dependent determination of the shifting point.

<!-- chunk {"id": "body-0292", "role": "body", "section": "Flexible ReLU (FReLU)", "weight": 1.0} -->

The FReLU is a ReLU extension with zero-like property and the ability to capture negative information. The zero-like property is the ability to push activation means closer to zero as this might speed up learning. The FReLU builds on the ability to shift the AF where a i and b i would be optimized parameters. However, since the parameter a i can be learned by the bias term of the neuron to whose output is the activation function applied, the authors Qiu, Xu, and Cai formulate the FReLU as where b i is a trainable parameter.

<!-- chunk {"id": "body-0293", "role": "body", "section": "Adaptive shifted ReLU (ShiLU)", "weight": 1.0} -->

An adaptive shifted ReLU (ShiLU) is another adaptive variant of the ReLU activation; it is a variant that adds a trainable slope and a vertical shift: where a i and b i are trainable parameters for each neuron i. They used the name shifted ReLU, but that name is already taken by the non-adaptive Shifted ReLU; hence, the full name is adaptive shifted ReLU throughout this work to avoid confusion.

<!-- chunk {"id": "body-0294", "role": "body", "section": "StarReLU", "weight": 1.0} -->

The StarReLU is an adaptive version of the RePU of power 2 using a similar approach as the ShiLU; it is defined as where a i and b i are trainable parameters for each neuron i. If the parameters are not used in an adaptive manner, Yu et al. recommend setting a i = 0. 8944 and b i = -0. 4472.

<!-- chunk {"id": "body-0295", "role": "body", "section": "Adaptive HardTanh", "weight": 1.0} -->

An adaptive variant of HardTanh was used; it is defined as where a t is a scale factor for each epoch t such that 1 ≤ a 1 ≤ a 2 ≤... ≤ a t ≤... ≤ a T, T is the total number of training epochs and b is an adaptive parameter trained using BP with other parameters of the NN. The parameters a t are set such that the function starts in a similar shape as a regular HardTanh (see section 3.6.18) and gradually approaches the sign function. This allows for training a network that will gradually become a binary NN where each activation is the sign function which can be used for speeding the inference.

<!-- chunk {"id": "body-0296", "role": "body", "section": "Attention-based ReLU (AReLU)", "weight": 1.0} -->

Attention-based ReLU (AReLU) is a adaptive ReLU variant that uses ELSA - element-wise attention mechanism proposed. It is defined as where a l and b l are learnable parameters for each layer l, σ (x) is the logistic sigmoid function, C (x) is a function that clips the input into [0. 01, 0. 99]. The derivative of C (a l) is handled by just not using the BP when a l < 0. 01 or a l > 0. 99. While Chen, Li, and Xu observe that the parameters a l and b l are insensitive to the initialization, they recommend initializing a l = 0. 9 and b l = 2. 0 as a larger initial value of b l can speed up the convergence.

<!-- chunk {"id": "body-0297", "role": "body", "section": "Attention-based ReLU (AReLU)", "weight": 1.0} -->

The AReLU was found to outperform CELU, ELU, GELU, LReLU, Maxout, Relu, RReLU, SELU, sigmoid, softplus, swish, tanh, adaptive piece-wise linear unit (APLU), Padé activation unit (PAU), PReLU, and self-learnable activation function (SLAF) in experiments with various learning rates. The performance of AReLU was validated under different settings.

<!-- chunk {"id": "body-0298", "role": "body", "section": "Dual parametric ReLU (DPReLU) and Dual Line activation function", "weight": 1.0} -->

A DPReLU extends the concept of PReLU even further: where a i and b i are trainable parameters for each neuron i; these are initialized the same as PReLU a i = 1, b i = 0. 01. The DPReLU was also later proposed independently in under the name fully parametric ReLU and the abbreviation FReLU (which is already used in the literature for the flexible ReLU; see section 4.2.15).

<!-- chunk {"id": "body-0299", "role": "body", "section": "Dual Line", "weight": 1.0} -->

The DPReLU was further extended into a Dual Line activation function that adds a shift parameter where a i and b i are trainable parameters for each neuron i the same as in DPReLU and m i is an additional trainable shift parameter for each neuron or filter i; m i was initialized to m i = -0. 22.

<!-- chunk {"id": "body-0300", "role": "body", "section": "Piecewise linear unit (PiLU)", "weight": 1.0} -->

An AF very similar to the Dual Line is the piecewise linear unit (PiLU) proposed; it just extends the Dual Line concept by adding horizontal shifts. It is defined as where a i, b i, and c i are adaptive parameters for each neuron i. The PiLU geneneralizes, for example, ReLU, LReLU, PReLU, SlReLU, DPReLU, and Dual Line.

<!-- chunk {"id": "body-0301", "role": "body", "section": "Dual parametric family of activation functions", "weight": 1.0} -->

The DPReLU approach (see section 4.2.20) can be extended to a general concept transforming any activation function g (z): where g (z i) is any activation function and a i and m i are trainable parameters for each neuron i. The functions of this family are called dual parametric activation functions (DPAFs) throughout this text.

<!-- chunk {"id": "body-0302", "role": "body", "section": "Fully parameterized activation function (FPAF)", "weight": 1.0} -->

Similar approach to DPAF (see section 4.2.23) was proposed under the name of fully parameterized activation function (FPAF); the FPAF is defined as where a i and b i are trainable parameters for each neuron i and g 1 (z i) and g 2 (z i) can be any function. The FPAF, in contrast to the family of DPAFs, has no trainable shift but allows for learnable slopes for both parts of the piecewise function.

<!-- chunk {"id": "body-0303", "role": "body", "section": "Elastic PReLU (EPReLU)", "weight": 1.0} -->

The same as EReLU extends the concept of ReLU (see section 3.6), the Elastic (EPReLU) extends the PReLU it adds a varying coefficient to the positive part of the PReLU: where a i is the optimized parameter, k i is a sampled for each epoch and neuron i from the uniform distribution: a i ∼ U (1 -α, 1 + α) where α ∈. A modified training procedure for EPReLU is also proposed - the neuron weights and the trainable parameter a i are updated with k i = 1 in odd epochs, while in even epochs, the a i is kept fixed, the parameter k i is sampled from the uniform distribution, and only the neuron weights are updated. It was shown that the EPReLU leads to improved performance over the ReLU, PReLU, EReLU, APLU, network in network (NIN), and maxout unit networks on several datasets.

<!-- chunk {"id": "body-0304", "role": "body", "section": "Paired ReLU", "weight": 1.0} -->

A paired ReLU is a concept similar to CReLU (see section 3.6.34), but it introduces four trainable parameters. It is defined as where a i, b i, c i, and d i are trainable parameters for each neuron i. The parameters a i and c i are scale parameters and b i and d i are trainable thresholds; the inital values of scale parameters are a i = 0. 5 and c i = -0. 5.

<!-- chunk {"id": "body-0305", "role": "body", "section": "Tent", "weight": 1.0} -->

The tent is a ReLU-based AF proposed; it is defined as where a i is a trainable parameter. Rozsa and Boult recommend using batch normalization and initializing a i = 1. Also, having a weight decay on the parameter a i during training proved beneficial for certain tasks.

<!-- chunk {"id": "body-0306", "role": "body", "section": "Hat", "weight": 1.0} -->

The hat is an AAF very similar to the tent AF - the only difference is that the tent AF is centered around zero while the hat is positive only for positive inputs. The hat AF is defined as where a i is can be either fixed or trainable parameter. Wang, Xu, and Zhu used a i = 2 for the fixed variant; this value was also used.

<!-- chunk {"id": "body-0307", "role": "body", "section": "ReLU memristor-like activation function (RMAF)", "weight": 1.0} -->

The ReLU memristor-like activation function (RMAF) is an activation function similar to the swish AF (see section 4.4.1) and it also attempts to leverage the negative values. It is defined as where a i is a trainable parameter initialized a i = 1 for each neuron i or it is a fixed hyperparameter and b and c are fixed hyperparameters.

<!-- chunk {"id": "body-0308", "role": "body", "section": "Parametric tanh linear unit (PTELU)", "weight": 1.0} -->

A parametric tanh linear unit (PTELU) is an adaptive function that, for positive inputs, behaves just as a ReLU; however, the negative part is parameterized tanh function. It can also be seen as an extension of the PReLU (see section 4.2.1). It is an adaptive variant of ThLU (see section 3.7.1). It is defined as where a i and b i are trainable parameters for each neuron i; a i ≥ 0 and b i ≥ 0. It has output range of [-a i, ∞). The parameter a i controls the saturation value, and the parameter b i controls the convergence rate. While the AF resembles an adaptive extension of an ELU activation functions, the author Gupta and Duggal decided to use tanh function for the negative inputs because it gives a higher gradient for small negative inputs and saturates earlier than exp(z) -1 and thus the noise-robust deactivation state earlier and faster. The nonadaptive variant of PTELU with a i = 1 and b i = 1 was proposed.

<!-- chunk {"id": "body-0309", "role": "body", "section": "Tangent linear unit (TaLU)", "weight": 1.0} -->

The tanh linear unit (TaLU) is an AF similar to the PTELU. The TaLU is defined as where a i < 0 is either a learnable 47 or fixed parameter.

<!-- chunk {"id": "body-0310", "role": "body", "section": "PTaLU", "weight": 1.0} -->

The PTaLU 48 is a variant of TaLU with another learnable parameter. It is defined as where a i and b i are trainable parameters. Mercioni and Holban used initial values a i = -0. 75 and b i = 1.

<!-- chunk {"id": "body-0311", "role": "body", "section": "TanhLU", "weight": 1.0} -->

The tanhLU 49 is a parametric combination of the tanh and a linear function proposed. It is defined as where a i, b i, and c i are trainable parameters for each neuron i.

<!-- chunk {"id": "body-0312", "role": "body", "section": "TanhLU", "weight": 1.0} -->

47 The variant with the adaptive parameter was named TaLU learnable by the authors.

<!-- chunk {"id": "body-0313", "role": "body", "section": "TanhLU", "weight": 1.0} -->

48 Not an abbreviation but a name given by Mercioni and Holban.

<!-- chunk {"id": "body-0314", "role": "body", "section": "TanhLU", "weight": 1.0} -->

49 Not an abbreviation but a name given by Shen et al..

<!-- chunk {"id": "body-0315", "role": "body", "section": "TeLU", "weight": 1.0} -->

Despite the similar name, the tanh exponential linear unit (TeLU) 50 is quite different from the PTELU. The TeLU is closely related to the mish and TanhExp activations, but, unlike these two AFs, it also has an additional adaptive parameter. It is defined as where a i is either learnable or fixed scaling parameter.

<!-- chunk {"id": "body-0316", "role": "body", "section": "Tanh based ReLU (TReLU)", "weight": 1.0} -->

ATReLUwas proposed; however, it is is only a special case of previously proposed PTELU (see section 4.2.30). It is defined as where b i is a trainable parameter for each neuron i. This function is identical to the PTELU with its parameter a i fixed to a i = 1. Another special case of PTELU was proposed in also under the name of TReLU - this time, the parameter a i becomes a predefined fixed parameter, and b i becomes fixed to b i = 1. This function is denoted TReLU variant 2 (TReLU2) in this work and is defined as where a is fixed 51 parameter.

<!-- chunk {"id": "body-0317", "role": "body", "section": "Rectified linear tanh (ReLTanh)", "weight": 1.0} -->

A ReLTanh is a piecewise adaptive activation function that improves traditional tanh activation function - it replaces the positive and negative saturated regions of the tanh activation functions with straight lines whose slopes are identical to the slope of the tanh at the thresholds. It is defined as where tanh ′ (x) is the derivative of the tanh function and a i ∈ [a low, a high] and b i ∈ [b low, b high] are two trainable parameters that may be defined for each neuron i but are rather recommended to be shared by a whole layer l in order to decrease computational burden. The limits a low, a high, b low, and b high for the parameters are to constraint the learnable range and are predefined hyperparameters. Wang et al. used a low = -∞, a high = -1. 5, b low = 0, and b high = 0. 5 in their work. The initial values were set to a i = -1. 5 and b i = 0 for all layers (the parameters were shared layer-wise) in order to speed up the training process in early stages by the larger gradients.

<!-- chunk {"id": "body-0318", "role": "body", "section": "Bendable linear unit (BLU)", "weight": 1.0} -->

A BLU is an adaptive function that allows for any interpolation between the identity function and a rectifier. It is defined as where a i ∈ is a trainable parameter for each neuron or filter. One of the main advantages of the BLU is that it can model an identity function; the identity function is useful because its gradient cannot vanish or explode, and it also allows for a layer to be "skipped" - it is one of the reasons of why ResNets became so popular 50 used the TeLU as the name and not as an abbreviation; nevertheless, the long name tanh exponential linear unit fits the usual naming convention and, therefore, it is used in this work.

<!-- chunk {"id": "body-0319", "role": "body", "section": "Bendable linear unit (BLU)", "weight": 1.0} -->

51 While Nakhua et al. used the parameter fixed during their experiments, they also speculated that making it learnable might improve the performance. as it is rather hard to learn an identity transformation using conventional neural network and the architecture with skip connections allows for easy learning of the identity mapping. Unless the magnitude | a i | is exactly 1, the derivative of BLU is non-zero for both positive and negative inputs (similarly to LReLU and in contrast to vanilla ReLU and ELU). BLU has a slope higher than 1 for positive inputs for a i approaching 1 (or for negative inputs for a i approaching -1); this property helps to avoid vanishing gradient problems. Another useful benefit is that BLU are C ∞ continuous, which can be theoretically exploited for speeding up the optimization, e.g.,. It was also shown that smooth activation functions provide better signal propagation.

<!-- chunk {"id": "body-0320", "role": "body", "section": "Rectified BLU (ReBLU)", "weight": 1.0} -->

Avariant of the BLU (see section 4.2.37) was proposed in under the name rectified BLU (ReBLU). It is defined as, where a i is a trainable parameter.

<!-- chunk {"id": "body-0321", "role": "body", "section": "DELU", "weight": 1.0} -->

The DELU 52 activation function is a ReLU variation that utilizes the SiLU function (see section 3.3). It is defined as where a i is a trainable parameter for each neuron i and σ (z i) is the logistic sigmoid function.

<!-- chunk {"id": "body-0322", "role": "body", "section": "Soft clipping mish", "weight": 1.0} -->

A ReLU variant called soft clipping mish (SC-mish) was proposed. It adds soft clipping to the positive inputs using the mish AF; it is defined as where a i is a fixed parameter; Mercioni and Holban used a i = 1. It also has a variant where the parameter a i is trainable. Such a variant is called soft clipping learnable mish (SCL-mish). When using the SCL-mish, Mercioni and Holban initalized the parameter a i = 0. 25.

<!-- chunk {"id": "body-0323", "role": "body", "section": "Soft clipping swish", "weight": 1.0} -->

Yet another AF proposed by Mercioni and Holban is the soft clipping swish (SC-swish). This function is very similar to SC-mish and is defined as where σ (z) is the logistic sigmoid.

<!-- chunk {"id": "body-0324", "role": "body", "section": "Parametric swish (p-swish)", "weight": 1.0} -->

The parametric swish (p-swish) is another AF proposed by Mercioni and Holban. It is defined as where a i, b i, and c i are either trainable or fixed parameters (or combination thereof). The parameters were initialized to a i = 1, b i = 1 and c i = 0 in experiments. An AF named R\_S similar to the p-swish was independently proposed; it is equivalent to a p-swish with fixed a i = 1.

<!-- chunk {"id": "body-0325", "role": "body", "section": "Parametric swish (p-swish)", "weight": 1.0} -->

52 DELU is not an abbreviation but rather a name given by Pishchik.

<!-- chunk {"id": "body-0326", "role": "body", "section": "Parametric exponential linear unit (PELU)", "weight": 1.0} -->

Similarly as PReLU extends the concept of ReLU, the parametric exponential linear unit (PELU) extends the concept of ELU (see section 3.6.48). The PELU builds on a parameterization that separately controls the saturation point, the decay, and the slope: where a i, b i, and c i are trainable parameter for each neuron i. However, the PELU introduces only two new parameters a i controlling the saturation point, and b i controlling the decay - to control the shape of the activation function; the slope is not controlled separately through another parameter as it could lead to non-differentiability at z i = 0; therefore the slope is set such that the derivatives on both sides of zero are equal which leads to c i = a i b i and therefore the PELU is defined as The PELU combined with mixing different activation functions which use an adaptive linear combination or hierarchical gated combination of activation function was shown to perform well - see section 4.2.45.

<!-- chunk {"id": "body-0327", "role": "body", "section": "Extended exponential linear unit (EDELU)", "weight": 1.0} -->

An adaptive function called extended exponential linear unit (EDELU) 53 was proposed. This function is the same as the PELU, but it omits the vertical scaling for positive inputs, adds a parameter controlling the threshold, and uses inverse definitions of the parameters present in the PELU. It is defined as where a i ≥ 0 54 and b i ≥ 0 55 are trainable PELU parameters and c i ≥ 0 is the novel parameter for controlling the threshold that has to satisfy the relationship while the c i = 0 is always a solution of the equation, there are other solutions for b i > a i > 0.

<!-- chunk {"id": "body-0328", "role": "body", "section": "Adaptive combination of PELU and PReLU", "weight": 1.0} -->

Two different activation functions can be mixed together, as shown. One such example of mixed activation function is where a i is a combination coefficient that might be learned from the data. Another mixing approach was shown for combining PReLU and PELU: where σ (x) is the logistic sigmoid. Qian et al. also proposed other mixing schemes such as hierarchical activation, winner-take-all selection whose performance were shown on the MNIST, CIFAR-10 and CIFAR-100 datasets; see for details.

<!-- chunk {"id": "body-0329", "role": "body", "section": "Fast exponential linear unit (FELU)", "weight": 1.0} -->

An ELU variant called fast exponential linear unit (FELU) aiming at efficient training and network inference was proposed in - it is inspired by fast approximation of the exponential function proposed in to replace the exponential in the ELU: where a i is a trainable parameter controlling the soft saturation region.

<!-- chunk {"id": "body-0330", "role": "body", "section": "Fast exponential linear unit (FELU)", "weight": 1.0} -->

53 Authors called the function extendeD ELU resulting in an abbreviation DELU but that name is already taken by an AF proposed a few months earlier.

<!-- chunk {"id": "body-0331", "role": "body", "section": "P+FELU", "weight": 1.0} -->

Adem proposed variant of the FELU function named P+FELU; this variant has an added parameter and is defined as where a i is a trainable parameter same as the original FELU and b is the added trainable parameter.

<!-- chunk {"id": "body-0332", "role": "body", "section": "Multiple parametric exponential linear unit (MPELU)", "weight": 1.0} -->

A PELU extension, multiple parametric exponential linear unit (MPELU), uses two trainable parameters to allow for a combination of a ReLU and ELU. The multiple parametric exponential linear unit (MPELU) is defined as where a i and b i are trainable parameters for each neuron i. The ReLU, certain parameterizations of PELU, and ELU are special cases of the MPELU. A special method for weight initialization of neurons with MPELU units was also proposed; depending on a particular initialization, the method can become the initialization for ELU networks or for ReLU networks. The MSRA 56 filler approach can be considered as a special case of the MPELU initialization. The MPLU initialization is a similar approach to LSUV initialization, but unlike the LSUV initialization, it provides an analytic solution for ELU and MPELU and therefore it has lower computational costs. It was also shown that the MPELU works better with batch normalization compared to the vanilla ELU.

<!-- chunk {"id": "body-0333", "role": "body", "section": "Multiple parametric exponential linear unit (MPELU)", "weight": 1.0} -->

The performance of the MPELU was empirically shown on the CIFAR-10 and CIFAR-100 datasets using multiple neural network architectures, e.g. nine-layer deep NIN or even a ResNet with 1001 layers.

<!-- chunk {"id": "body-0334", "role": "body", "section": "P-E2-ReLU", "weight": 1.0} -->

The AAF named P-E2-ReLU is combining two ELUs and a ReLU using two adaptive parameters. It is defined as where a i and b i are trainable parameters for each neuron i. The parameters were initialized to a i = 0. 4 and b i = 0. 3 in experiments. Jie et al. mentioned that other combinations could be considered and called this family P-E2-XU. One such combination is denoted P-E2-Id and is defined as and another is named P-E2-ReLU-1 whera a i is a trainable parameter in both AAFs. The parameter was initialized to a i = 0. 5 in experiments.

<!-- chunk {"id": "body-0335", "role": "body", "section": "Soft exponential", "weight": 1.0} -->

The soft exponential activation function is an adaptive activation function that is able to interpolate between logarithmic, linear, and exponential functions. It is defined as where a i is a trainable parameter. The soft exponential activation functions is continuously differentiable with respect to z i and also with respect to a i; furthermore, for any constant a i, the function is monotonic. When a i = -1, the function becomes f (z i) = ln(z i), while for a i = 0 it becomes linear function f (z i) = z i and for a i = 1, it is the exponential function f (z i) = exp(z i).

<!-- chunk {"id": "body-0336", "role": "body", "section": "Soft exponential", "weight": 1.0} -->

56 The initialization method was unnamed in the original paper but was later named Microsoft Research Asia (MSRA) filler.

<!-- chunk {"id": "body-0337", "role": "body", "section": "Continuously differentiable ELU (CELU)", "weight": 1.0} -->

A CELU was proposed; CELU is very similar to the original parameterization of ELU but reformulated such that the derivative at z i = 0 is 1 for all values of a i. CELU is defined as where a i is a learnable parameter for each neuron i. Its main advantages are that its derivative with respect to z i is bounded and that it contains both the linear transfer function and ReLU.

<!-- chunk {"id": "body-0338", "role": "body", "section": "Erf-based ReLU (ErfReLU)", "weight": 1.0} -->

The Erf-based ReLU (ErfReLU) is an AAF similar to the ELU. It is defined as where a i is a learnable parameter for each neuron i and erf (z i) is the Gauss error function.

<!-- chunk {"id": "body-0339", "role": "body", "section": "Parametric scaled exponential linear unit (PSELU)", "weight": 1.0} -->

Aparametric scaled exponential linear unit (PSELU) is basically a SELU (see section 3.7.11) where the parameters a and b controlling the behavior are trainable. It is defined as where a i and b i are trainable parameters for each neuron i.

<!-- chunk {"id": "body-0340", "role": "body", "section": "Leaky parametric scaled exponential linear unit (LPSELU)", "weight": 1.0} -->

Aleaky parametric scaled exponential linear unit (LPSELU) is a leaky extension of the PSELU (see section 4.2.53) to avoid small gradients hindering the learning process: where a i and b i are trainable parameters for each neuron i and c i is either a predefined constant or a trainable parameter.

<!-- chunk {"id": "body-0341", "role": "body", "section": "Leaky parametric scaled exponential linear unit with reposition parameter (LPSELU\\_RP)", "weight": 1.0} -->

The LPSELU can be extended by a reposition parameter similarly as FReLU extends ReLU (see section 4.2.15); such function is called LPSELU\_RP and is defined as where a i and b i are trainable parameters for each neuron i, and c i is either a predefined constant or a trainable parameter the same as for LPSELU (see section 4.2.54) and m i is a trainable reposition parameter. It was empirically observed that the shift parameter m i converges to a small negative value, which supports the hypothesis that the negative output of activation functions is important.

<!-- chunk {"id": "body-0342", "role": "body", "section": "Shifted ELU family", "weight": 1.0} -->

A family of several activation functions, shifted exponential linear unit, was proposed; functions in this family have either vertical or horizontal shift of an ELU activation function that can be either constant or trainable. An ELU with fixed horizontal shift is ShELU, with fixed vertical SvELU and PELU (see section 4.2.43) with trainable horizontal shift is PShELU. The ShELU is defined as where a is a fixed parameter similarly as in the vanilla ELU and b is novel, preset parameter controlling the horizontal shift. The SvELU is defined similarly: where a is a fixed parameter similarly as in the vanilla ELU and b is novel, preset parameter controlling the vertical shift. Grelsson and Felsberg define also a variant of PELU with horizontal shift called PSheLU: where a i and b i are trainable parameters of the original PELU, and c i is a novel trainable parameter controlling the horizontal shift for each neuron i.

<!-- chunk {"id": "body-0343", "role": "body", "section": "Shifted ELU family", "weight": 1.0} -->

For some reason, Grelsson and Felsberg did not propose a PELU with vertical shift (PSvELU), but it could be defined in a similar manner where a i, b i are trainable parameters of the original PELU and c i is a novel trainable parameter controlling the vertical shift. Note that the shifted activation functions with horizontal shifts are equivalent to non-shifted variants with biases that are individual for each neuron and not shared in the same tiling pattern as the convolutional kernel.

<!-- chunk {"id": "body-0344", "role": "body", "section": "Tunable swish (T-swish)", "weight": 1.0} -->

The tunable swish (T-swish) proposed in is an AAF combining the ELU, E-swish (see section 4.4.4) and swish (see section 4.4.1) as it has trainable parameters for both horizontal and vertical scaling for negative inputs. It is defined as where a i, b i, and c i are either fixed or trainable parameters for each neuron i.

<!-- chunk {"id": "body-0345", "role": "body", "section": "Rectified parametric sigmoid unit (RePSU)", "weight": 1.0} -->

The rectified parametric sigmoid unit (RePSU) is an AAF proposed; it consists of a linear combination of two components - rectified parametric sigmoid shrinkage unit (RePSKU) and rectified parametric sigmoid stretchage unit (RePSHU). It is defined as and a i, b i, c i, d i, and e i are parameters (common for both RePSKU b i,c i,d i,e i (z i) and RePSHU b i, c i, d i, e i (z i)). The RePSU is a generalization of the smooth sigmoid-based shrinkage (SSBS) function used for image denoising.

<!-- chunk {"id": "body-0346", "role": "body", "section": "Parametric deformable exponential linear unit (PDELU)", "weight": 1.0} -->

An adaptive activation function parametric deformable exponential linear unit (PDELU) is based on the premise that shifting the mean value of the output closer to zero speeds up the learning. The PDELU is defined as where a i is a trainable parameter for each neuron i and b is a fixed hyperparameter controlling the degree of deformation. The Cheng et al. recommend setting b = 0. 9. The authors found that the MSRA initialization method is consistent with PDELU. The performance of PDELU was empirically shown on the CIFAR-10 and CIFAR-100 datasets and on the ImageNet dataset where it outperformed ReLU, APLU, LReLU, PReLU, SReLU, ELU, MPELU (and other) activation functions.

<!-- chunk {"id": "body-0347", "role": "body", "section": "Elastic exponential linear unit (EELU)", "weight": 1.0} -->

An adaptive variant of the ELU function that has a stochastic component was proposed in - the elastic exponential linear unit (EELU). The EELU combines EReLU (see section 3.6.38) and MPELU (see section 4.2.48) and is defined as where a c and b c are trainable parameters shared among all neurons of a channel c and k c i is a randomly sampled noise parameter for each neuron i in channel c during the training stage and set to 1 during the testing stage. The k c i is sampled coefficient from Gaussian distribution with a random standard deviation that is truncated from 0 to 2; k c i is therefore sampled as where N (1, σ 2) is Gaussian distribution with mean 1 and variance σ 2, U denotes the uniform distribution. The ϵ is a hyperparameter; the authors recommend smaller values, e.g., 0.1 or 0.2.

<!-- chunk {"id": "body-0348", "role": "body", "section": "Elastic exponential linear unit (EELU)", "weight": 1.0} -->

The training algorithm is also modified and works in two steps - first, the EELU parameter and the weights are updated with fixed k c i = 1, and then weights are updated with random k c i and fixed EELU parameters. The authors also recommend using the MPELU initialization method.

<!-- chunk {"id": "body-0349", "role": "body", "section": "Parametric first power linear unit with sign (PFPLUS)", "weight": 1.0} -->

The parametric first power linear unit with sign (PFPLUS) is an AAF proposed. It is defined as where H(z i) is Heaviside step function (see section 3.1) and a i > 0 and b i > 0 are trainable parameters for each neuron i. For example, the PFPLUS is similar to the ReLU when a i = 0. 2 and b i = 10 and similar to a linear mapping when a i = 5 and b i = 0. 1.

<!-- chunk {"id": "body-0350", "role": "body", "section": "Parametric variational linear unit (PVLU)", "weight": 1.0} -->

The parametric variational linear unit (PVLU) is an adaptive variant of the VLU proposed. It is defined as where a i and b i are trainable parameters.

<!-- chunk {"id": "body-0351", "role": "body", "section": "Sigmoid-based adaptive functions", "weight": 1.0} -->

Many different adaptive activation functions based on the sigmoid family were proposed in the literature, one of the earliest examples is a logistic sigmoid activation function with shape autotuning. The function proposed by Yamada and Yabuta uses a single parameter controlling both the amplitude and the slope of the activation function. The proposed adaptive function is defined as where a ∈ (0, ∞) is a learnable parameter.

<!-- chunk {"id": "body-0352", "role": "body", "section": "Generalized hyperbolic tangent", "weight": 1.0} -->

The generalized hyperbolic tangent introduces two trainable parameters that control the scale of the activation function: where a i and b i are trainable parameters for each neuron i. A non-adaptive version with fixed parameters was used for document recognition in in order to improve convergence toward the end of the learning session (see section 3.2.3).

<!-- chunk {"id": "body-0353", "role": "body", "section": "Trainable amplitude", "weight": 1.0} -->

A more general approach was introduced, which used networks with a trainable amplitude of activation functions; the same approach was later used for recurrent neural networks. The class of adaptive functions with a trainable amplitude is defined as where a i and b i are trainable parameters for each neuron i. The a i determines the trainable amplitude and the b i trainable offset. These parameters can be either different for each neuron or may be shared by a whole layer or even a whole network.

<!-- chunk {"id": "body-0354", "role": "body", "section": "Adaptive slope sigmoidal function (ASSF)", "weight": 1.0} -->

A adaptive slope sigmoidal function (ASSF) based on the work of Yamada and Yabuta, Yamada and Yabuta was used. It is defined as where σ is the logistic sigmoid and a is a global trainable parameter. The ASSF was also rediscovered by Mercioni, Tiron, and Holban.

<!-- chunk {"id": "body-0355", "role": "body", "section": "Slope varying activation function (SVAF)", "weight": 1.0} -->

A slope varying activation function (SV AF) was proposed in where a is a global trainable parameter. The slope varying activation function was proposed together with a BP modification that has two different learning rates. The slope varying activation function was implemented as a modification of the BP algorithm rather; a different example of modification of the BP algorithm resulting in an adaptive activation function is presented.

<!-- chunk {"id": "body-0356", "role": "body", "section": "TanhSoft", "weight": 1.0} -->

The TanhSoft is a family of AAFs proposed in that combine the softplus and tanh that contains three notable cases - TanhSoft-1, TanhSoft-2, and TanhSoft-3.

<!-- chunk {"id": "body-0357", "role": "body", "section": "TanhSoft", "weight": 1.0} -->

The general TanhSoft is defined as where a i, b i, c i, and d i are either trainable or fixed parameters; a i ∈ (-∞, 1], b i ∈ [0, ∞), c i ∈ (0, ∞), and d i ∈.

<!-- chunk {"id": "body-0358", "role": "body", "section": "TanhSoft", "weight": 1.0} -->

The first AF, named TanhSoft-1, is defined as where a i is a trainable parameter; it can be obtained from the general TanhSoft by setting b i = 0 and d i = 1. The second AF, TanhSoft-2, is defined as where b i and c i are trainable parameters. The TanhSoft-2 can be obtained from the general TanhSoft by setting a i = 0 and d i = 0. The last AF, TanhSoft-3, is defined as where a i is a trainable parameter. It can be obtained from the general TanhSoft by setting b i = 0 and d i = 1.

<!-- chunk {"id": "body-0359", "role": "body", "section": "Parametric sigmoid (psigmoid)", "weight": 1.0} -->

An adaptive variant of logistic sigmoid named parametric sigmoid (psigmoid) 57 was proposed. 58 Similarly as in generalized hyperbolic tangent, it introduces two scaling parameters to a logistic sigmoid: where a i is a trainable parameter for each neuron or channel i and b is a global trainable parameter.

<!-- chunk {"id": "body-0360", "role": "body", "section": "Parametric sigmoid function (PSF)", "weight": 1.0} -->

A parametric sigmoid function (PSF) is a continuous, differentiable, and bounded function proposed in 59 and is defined as where m is a global trainable parameter. The parameter m controls the slope of the sigmoid and the position of the maximum derivative; the envelope of the relevant derivatives for different values of m is also a sigmoid function. The larger values of m improve the gradient flow. The PSF is only one instance of a larger class of activation functions proposed.

<!-- chunk {"id": "body-0361", "role": "body", "section": "Slope and threshold adaptive activation function with tanh function (STAC-tanh)", "weight": 1.0} -->

The slope and threshold adaptive activation function function with tanh function (STAC-tanh) was proposed. It is basically a tanh based equivalent of the improved logistic sigmoid with adaptive parameters. It is defined as where a i and b i are trainable parameters.

<!-- chunk {"id": "body-0362", "role": "body", "section": "Generalized Riccati activation (GRA)", "weight": 1.0} -->

The generalized Riccati activation (GRA) is an adaptive variant of a sigmoid AF proposed. It is defined as where a i, b i, and c i are adaptive parameters b i > 0 and c i > 0.

<!-- chunk {"id": "body-0363", "role": "body", "section": "Adaptive sigmoid-weighted linear units", "weight": 1.0} -->

There are several AFs that are based on the SiLU but have an adaptive parameter; the most common example is the swish AF, but there are also other popular functions based on the same principle.

<!-- chunk {"id": "body-0364", "role": "body", "section": "Swish", "weight": 1.0} -->

A swish activation function is an adaptive variant of the SiLU (see section 3.3); it is also the member of the LAAF class (see section 4.16): where σ (z) is the logistic sigmoid, a i is either a fixed hyperparameter or a trainable parameter. The swish has an output range of (-∞, ∞). The parameter a i controls the amount of non-linearity the swish activation has. The swish might also be considered a member of the family of activate or not activation functions (ACONs); it is then named ACON-A. The parametric SiLU (PSiLU) is another name for the swish activation used.

<!-- chunk {"id": "body-0365", "role": "body", "section": "Swish", "weight": 1.0} -->

57 Not to be confused with parametric sigmoid function (PSF) from section 4.3.7.

<!-- chunk {"id": "body-0366", "role": "body", "section": "Swish", "weight": 1.0} -->

58 It seems that this AAF was first proposed in 2010 in and then independently in 2021.

<!-- chunk {"id": "body-0367", "role": "body", "section": "Swish", "weight": 1.0} -->

59 contains the definition equivalent to f ( z ) = PSF ( z 2 ).

<!-- chunk {"id": "body-0368", "role": "body", "section": "Adaptive hybrid activation function (AHAF)", "weight": 1.0} -->

A swish variant with vertical scaling was proposed in under the name adaptive hybrid activation function (AHAF). It is defined as where a i and b i are trainable parameters.

<!-- chunk {"id": "body-0369", "role": "body", "section": "Parametric shifted SiLU (PSSiLU)", "weight": 1.0} -->

The parametric shifted SiLU (PSSiLU) is a swish based AAF proposed. It is defined as where a i and b i are trainable parameters.

<!-- chunk {"id": "body-0370", "role": "body", "section": "E-swish", "weight": 1.0} -->

E-swish is an AAF inspired by the swish activation function (see section 4.4.1); the E-swish has a scaling parameter that allows for vertical scaling of the activation function. The name of the activation function is not chosen well as the E-swish is rather extending the SiLU (see section 3.3) and not swish which is its adaptive variant. 60 The function is defined as where σ (z) is the logistic sigmoid and a is a preset parameter - however, the parameter a is considered to be trainable in review. Alcaide recommends setting a ∈ to avoid exploding gradients that are hypothesized to more likely occur for higher values of a. The E-swish was found to outperform the SiLU (called swish in the paper) on the the MNIST, CIFAR-10 and CIFAR-100 datasets using the Wide ResNet (WRN) architecture.

<!-- chunk {"id": "body-0371", "role": "body", "section": "ACON-B", "weight": 1.0} -->

The ACON family conists of swish AF and several extensions; one is named ACON-B and is defined as where a i and b i are trainable parameters. The b i is initalized to 0.25 and a i to 1. 61

<!-- chunk {"id": "body-0372", "role": "body", "section": "ACON-C", "weight": 1.0} -->

The ACON-C is another member of the ACON family. It is defined as where a i, b i, and c i are trainable parameters. Ma et al. used initial values a i = 1, b i = 0, and c i = 1.

<!-- chunk {"id": "body-0373", "role": "body", "section": "ACON-C", "weight": 1.0} -->

Ma et al. also proposed a general extension to the ACON family named MetaACON which uses a small NN to determine the value of the parameter a i; they used the variant ACON-C for the experiments with MetaACON resulting in MetaACON-C 62. The MetaACON was used to improve YOLOv7. Kan et al. extented the ACON AFs into an AF they named CBAC 63. The ACONs were used, for example,. The 1Dmeta-ACON is a MetaACON extension proposed.

<!-- chunk {"id": "body-0374", "role": "body", "section": "Parameterized self-circulating gating unit (PSGU)", "weight": 1.0} -->

The Parameterized self-circulating gating unit (PSGU) is related to the LiSHT and GTU activation functions as it is basically a LiSHT with gated input with learnable scaling parameter. It is defined as 60 Calling the SiLU as swish is quite common in the literature, e.g., exponential swish, generalized swish, and TS-swish.

<!-- chunk {"id": "body-0375", "role": "body", "section": "Parameterized self-circulating gating unit (PSGU)", "weight": 1.0} -->

61 There is no initial value for a i in ACON-B mentioned explicitly; however, there is one for its extension ACON-C.

<!-- chunk {"id": "body-0376", "role": "body", "section": "Parameterized self-circulating gating unit (PSGU)", "weight": 1.0} -->

62 The implementation of MetaACON-C and other AFs from the ACON family is available at con.

<!-- chunk {"id": "body-0377", "role": "body", "section": "Parameterized self-circulating gating unit (PSGU)", "weight": 1.0} -->

63 No further description is provided. where a i is a learnable parameter and σ (z) is the logistic sigmoid function. Li et al. also propose a novel initialization method for NNs with the PSGU AF and show that it is more suitable for the use with PSGU than other common methods. The PSGU is shown to outperform ReLU, mish, swish, PATS and GELU using various NIN and ResNet architectures. The PSGU was also proposed in under the name TSReLU learnable (TSReLUl) as the adaptive variant of TSReLU. Mercioni, Tat, and Holban used a i = 0. 5 as the initial value.

<!-- chunk {"id": "body-0378", "role": "body", "section": "Tangent-bipolar-sigmoid ReLU learnable (TBSReLUl)", "weight": 1.0} -->

Similarly as TSReLUl is an adaptive variant of TSReLU, the TBSReLU learnable (TBSReLUl) is an adaptive variant of TBSReLU. This variant is defined as where a i is a trainable parameter. Mercioni, Tat, and Holban used a i = 0. 5 as the initial value.

<!-- chunk {"id": "body-0379", "role": "body", "section": "PATS", "weight": 1.0} -->

The AF named PATS 64 is very similar to PSGU, but it uses arctan and a random scaling parameter instead of the tanh and the adaptive parameter in PSGU. It is defined as where σ (z) is the logistic sigmoid function and is sampled during training 65 from the uniform distribution with bounds l and u such that 0 < l < u < 1. The authors experimented with fixed, deterministic values of a i ∈ { 1 4, 1 2, 5 8, 3 4 } -the value 5 8 led to lowest test error on the CIFAR-10; they also deemed that suitable values for l and u are 1 2 and 34 respectively. However, only fixed variant with a i = 5 8 was used in the follow-up works such as.

<!-- chunk {"id": "body-0380", "role": "body", "section": "Adaptive quadratic linear unit (AQuLU)", "weight": 1.0} -->

The adaptive quadratic linear unit (AQuLU) is an adaptive SiLU variant proposed; it is defined as where a i and b i are trainable parameters for each neuron i.

<!-- chunk {"id": "body-0381", "role": "body", "section": "Sinu-sigmoidal linear unit (SinLU)", "weight": 1.0} -->

Another adaptive SiLU variant is the sinu-sigmoidal linear unit (SinLU), which adds an adaptive term using the sine function to the linear part of the SiLU. The SinLU is defined as where σ (z i) is the logistic sigmoid function and a i and b i are trainable parameters for each neuron i.

<!-- chunk {"id": "body-0382", "role": "body", "section": "ErfAct", "weight": 1.0} -->

An AAF based on the Gauss error function was proposed. The AAF is named ErfAct and is defined as where a i and b i are trainable parameters for each neuron i and erf(x) is the Gauss error function.

<!-- chunk {"id": "body-0383", "role": "body", "section": "ErfAct", "weight": 1.0} -->

65 Unfortunately, the author did not specify what happens during the test phase, one can only assume that the expected value is used.

<!-- chunk {"id": "body-0384", "role": "body", "section": "Parametric serf (pserf)", "weight": 1.0} -->

An adaptive version of the serf AF named parametric serf (pserf) was proposed. It is defined as where a i and b i are trainable parameters for each neuron i and erf(x) is the Gauss error function.

<!-- chunk {"id": "body-0385", "role": "body", "section": "Swim", "weight": 1.0} -->

The swim is an adaptive variant of the PFLU (see section 3.7.7) independently proposed. It is defined as where a i is either fixed or trainable parameter for each neuron i. Abdool and Dear used fixed a i = 0. 5 in their experiments.

<!-- chunk {"id": "body-0386", "role": "body", "section": "Tuned softmax (tsoftmax)", "weight": 1.0} -->

A softmax (see section 3.5) variant named tuned softmax (tsoftmax) was proposed; it is defined as where f (z j) is the output of a neuron j in a softmax layer consisting of N neurons and c is an adaptive parameter.

<!-- chunk {"id": "body-0387", "role": "body", "section": "Generalized Lehmer softmax (glsoftmax)", "weight": 1.0} -->

The generalized Lehmer softmax (glsoftmax) is a softmax variant proposed. It is defined as where LNORM(z j) is a generalized Lehmer-based Z-score-like normalization with four trainable parameters a i, b i, c i, and d i defined: x is a vector of elements x k, k = 1,..., N and z -M a i,b i represents a vector with elements z k -M a i,b i, k = 1,..., N.

<!-- chunk {"id": "body-0388", "role": "body", "section": "Generalized power softmax (gpsoftmax)", "weight": 1.0} -->

The generalized power softmax (gpsoftmax) is another softmax variant proposed. It is defined as where PNORM(z j) is a generalized power-based Z-score-like normalization with four trainable parameters a i, b i, c i, and d i defined: x is a vector of elements x k, k = 1,..., N and z -M a i,b i represents a vector with elements z k -M a i,b i, k = 1,..., N.

<!-- chunk {"id": "body-0389", "role": "body", "section": "Adaptive radial basis function (ARBF)", "weight": 1.0} -->

The adaptive (ARBF) was used. It is defined as where a i and b i are adaptive parameters for each neuron i. The parameter a i controls the center while the parameter b i controls the width.

<!-- chunk {"id": "body-0390", "role": "body", "section": "Parametric Gaussian error linear unit (PGELU)", "weight": 1.0} -->

The AAF named parametric Gaussian error linear unit (PGELU) was proposed in as the result of noise injection. It is an GELU (see section 3.3.1) adaptive variant defined as where Φ(z) is the standard Gaussian CDF and a is a global learnable parameter representing the root mean square (RMS) noise.

<!-- chunk {"id": "body-0391", "role": "body", "section": "Parametric flatted-T swish (PFTS)", "weight": 1.0} -->

A parametric flatted-T swish (PFTS) is an adaptive extension of the FTS (see section 3.6.46); PFTS is identical to FTS except for that the parameter T is adaptive - i.e.: where T i is a trainable parameter for each neuron i; the parameter T i is initialized to the value -0.20.

<!-- chunk {"id": "body-0392", "role": "body", "section": "Parametric flatten-p mish (PFPM)", "weight": 1.0} -->

The parametric flatten-p mish (PFPM) is an AAF proposed; it is defined as where p i is a trainable parameter.

<!-- chunk {"id": "body-0393", "role": "body", "section": "Gaussian error unit (GEU)", "weight": 1.0} -->

The AAF named Gaussian error unit (GEU) was proposed in as the result of noise injection. It is defined as where Φ(z) is the standard Gaussian CDF and a is a global learnable parameter representing the RMS noise. The GEU multiplied by z becomes the PGELU (see section 4.9).

<!-- chunk {"id": "body-0394", "role": "body", "section": "Scaled-gamma-tanh activation function (SGT)", "weight": 1.0} -->

The scaled-gamma-tanh (SGT) AF is a piecewise polynomial function proposed. It is defined as where a and c are fixed, predefined parameters and b i and c i are trainable parameters for each neuron or filter i.

<!-- chunk {"id": "body-0395", "role": "body", "section": "RSign", "weight": 1.0} -->

An adaptive variant of the sign function was used. It is called react-sign (RSign) and is defined as where a c is an adaptive threshold for each channel. An extension was used, where Ding, Liu, and Zhou used multiple RSign functions for each channel.

<!-- chunk {"id": "body-0396", "role": "body", "section": "P-SIG-RAMP", "weight": 1.0} -->

An AAF combining the logistic sigmoid and ReLU was proposed in under the name P-SIG-RAMP. The P-SIG-RAMP is defined as where a i ∈ and b i are trainable parameters.

<!-- chunk {"id": "body-0397", "role": "body", "section": "Locally adaptive activation function (LAAF)", "weight": 1.0} -->

A general class of slope varying functions called locally adaptive activation function (LAAF) was proposed: where a i is a trainable parameter for each neuron i and g is any activation function; Jagtap, Kawaguchi, and Karniadakis used logistic sigmoid, tanh, ReLU, and LReLU as g in their LAAFs. The corresponding activations are thus given by where b is the LReLU leakiness parameter. To accelerate the convergence, Jagtap, Kawaguchi, and Karniadakis add additional fixed parameter to the expression: where n > 1 is a fixed parameter. It was found that this additional parameter improves both the convergence rate and the solution accuracy.

<!-- chunk {"id": "body-0398", "role": "body", "section": "Adaptive slope hyperbolic tangent", "weight": 1.0} -->

A tanh activation function with adaptive slope was used in an multi-layer perceptron (MLP) architecture. The used activation function is defined as where a i is a trainable parameter for each neuron i.

<!-- chunk {"id": "body-0399", "role": "body", "section": "Parametric scaled hyperbolic tangent (PSTanh)", "weight": 1.0} -->

A parametric activation function similar to the swish but based on the tanh function instead of the logistic sigmoid called parametric scaled hyperbolic tangent (PSTanh) was proposed. It is defined as where a i and b i are trainable parameters for each neuron i. The function is also very similar to the PTELU (see section 4.2.30) as for z i > 0 and a i ≈ 1, the output is close to z i (the exact distance depends on the parameters a i and b i).

<!-- chunk {"id": "body-0400", "role": "body", "section": "Scaled sine-hyperbolic function (SSinH)", "weight": 1.0} -->

An AF similar to PSTanh is the scaled sine-hyperbolic function (SSinH); it is defined as where a i and b i are trainable scaling parameters and sinh is the hyperbolic sine.

<!-- chunk {"id": "body-0401", "role": "body", "section": "Scaled exponential function (SExp)", "weight": 1.0} -->

Husain, Ong, and Bober also proposed scaled exponential function (SExp) along with the SSinH. It is defined as where a i and b i are trainable scaling parameters and sinh is the hyperbolic sine.

<!-- chunk {"id": "body-0402", "role": "body", "section": "Logmoid activation unit (LAU)", "weight": 1.0} -->

A learnable LAU was proposed; which utilise two learnable parameters a l and b l for each network layer l where z i,l is the output of the neuron i in layer l without the activation function and σ is the logistic sigmoid. The author used initial values of the parameters a l = b l = 1 for each network's layer l and trained these parameters together with the rest of the network's weights.

<!-- chunk {"id": "body-0403", "role": "body", "section": "Cosinu-sigmoidal linear unit (CosLU)", "weight": 1.0} -->

The cosinu-sigmoidal linear unit (CosLU) is an adaptive activation function proposed in that is based on the logistic sigmoid. It is defined as where a i and b i are trainable parameters for neuron i and σ (z i) is the logistic sigmoid function. The cosine amplitude is controlled by the parameter a i, whereas its frequency is controlled by the parameter b i.

<!-- chunk {"id": "body-0404", "role": "body", "section": "Adaptive Gumbel (AGumb)", "weight": 1.0} -->

An activation function adaptive Gumbel (AGumb) is based approach of viewing activation functions as a combination of unbounded and bounded components where the bounded component is based upon a cumulative distribution function of a continuous distribution. While the logistic sigmoid activation is a CDF of the symmetric logistic distribution, the AGumb is based on the Gumbel distribution. It is defined as where a i ∈ R + is trainable parameter for each neuron i.

<!-- chunk {"id": "body-0405", "role": "body", "section": "Shape autotuning adaptive activation function (SAAAF)", "weight": 1.0} -->

The shape autotuning adaptive activation function (SAAAF) 66 is an AAF proposed. It is defined as where a i ≥ 0 and b i ≥ 0 are trainable parameters for neuron i and 0 < b i a i < e.

<!-- chunk {"id": "body-0406", "role": "body", "section": "Noisy activation functions", "weight": 1.0} -->

Stochastic variants of saturing activation functions such as the logistic sigmoid or hyperbolic tangent were proposed in where an additional noise is injected to the activation function when it operates in the saturation regimes. The noisy activation function is defined as where h(z i) is any saturating activation function such as hard-tanh or hard-sigmoid, u(z i) is its linearization using first-order Taylor expansion around zero, c is a hyperparameter changing the scale of the standard deviation of the noise, p i is a trainable parameter adjusting the magnitude of the noise for each neuron i, a is a hyperparameter influencing the mean of the added term, and σ (x) is the logistic sigmoid function. ϵ is the added noise; it is defined as ϵ = | ξ | 66 Zhou et al. named the function as shape autotuning activation function but the resulting abbreviation SAAF is already taken by smooth adaptive activation function (see section 4.29). Since the proposed function is an AAF, we term it as such to avoid the abbreviation collision.

<!-- chunk {"id": "body-0407", "role": "body", "section": "Noisy activation functions", "weight": 1.0} -->

if the noise term ξ is sampled from half-normal distribution and as ϵ = ξ if the noise term ξ is sampled from normal distribution with mean 0 and variance 1.

<!-- chunk {"id": "body-0408", "role": "body", "section": "Noisy activation functions", "weight": 1.0} -->

Gulcehre et al. also experimented with adding noise to the input of the activation function, resulting in an activation function defined as where s (z i) is either fixed parameter s (z i) = b or it is a trainable term where the meaning of c, σ, p i, h(z i), and u(z i) is same as in eq..

<!-- chunk {"id": "body-0409", "role": "body", "section": "Noisy activation functions", "weight": 1.0} -->

A similar concept in ReLU settings is the ProbAct activation function (see section 4.2.11).

<!-- chunk {"id": "body-0410", "role": "body", "section": "Fractional adaptive activation functions", "weight": 1.0} -->

Fractional adaptive activation functions (FAAFs) were proposed in as a generalization of several activation functions using the fractional calculus (see for a general introduction to the fractional calculus). Generally, for any activation function f (z), its generalization g (z) using fractional derivatives is defined as the a -th fractional derivative of f: where a can be a learnable 67 parameter. The FAAFs proposed in were further evaluated.

<!-- chunk {"id": "body-0411", "role": "body", "section": "Fractional ReLU", "weight": 1.0} -->

The fractional ReLU (FracReLU) is defined as which is then computed as which is then computed as where Γ(x) is the Gamma function and a i is a trainable parameter. The FracReLU was later independently proposed in under the name FReLU (but this abbreviation is already taken by flexible ReLU).

<!-- chunk {"id": "body-0412", "role": "body", "section": "Fractional softplus", "weight": 1.0} -->

The fractional softplus (FracSoftplus) is using the softplus function to generalize sigmoid-like functions through fractional derivatives. It is defined as where a i is a trainable parameter. Particularly interesting cases are when a i = 0 as it is the softplus function, a i = 1 logistic sigmoid, and a i = 2 which leads to a bell-like shape.

<!-- chunk {"id": "body-0413", "role": "body", "section": "Fractional hyperbolic tangent", "weight": 1.0} -->

The fractional tanh (FracTanh) is another fractional generalization proposed; it is defined as where a i is a trainable parameter. The function becomes the tanh for a i = 0 and the quadratic hyperbolic secant function for a i = 1.

<!-- chunk {"id": "body-0414", "role": "body", "section": "Fractional hyperbolic tangent", "weight": 1.0} -->

67 did not specified whether the parameter is trainable but explicitly uses a trainable a.

<!-- chunk {"id": "body-0415", "role": "body", "section": "Fractional adaptive linear unit", "weight": 1.0} -->

The fractional adaptive linear unit (FALU) is yet another AAF based on fractional calculus 68 It can be seen as the fractional generalization using the a i -th fractional derivative of the swish function: where a i and b i are trainable parameters and σ is the logistic sigmoid function. The fractional derivative is then calculated as However, as this calculation is not practical, Zamora-Esquivel, Rhodes, and Nachman use following approximation for a i ∈ and b i ∈: and a i and b i are the two previously mentioned trainable parameters. The FALU was shown to outperform ReLU, GELU, ELU, SELU, and kernel activation function (KAF) on the MNIST, CIFAR-10, ImageNet, and Fashion MNIST datasets for several tested architectures.

<!-- chunk {"id": "body-0416", "role": "body", "section": "Fractional leaky ReLU (FracLReLU)", "weight": 1.0} -->

The fractional LReLU (FracLReLU) is the fractional variant of the LReLU (see section 3.6.2) proposed. It is defined using fractional calculus as where a i ∈ is a fixed parameter. The fractional derivative is then calculated as

<!-- chunk {"id": "body-0417", "role": "body", "section": "Fractional parametric ReLU (FracPReLU)", "weight": 1.0} -->

The fractional PReLU (FracPReLU) is the fractional variant of the PReLU (see section 4.2.1) proposed. It is defined using fractional calculus as where a i ∈ is a fixed parameter and b i is a trainable parameter. The fractional derivative is then calculated as

<!-- chunk {"id": "body-0418", "role": "body", "section": "Fractional ELU (FracELU)", "weight": 1.0} -->

The fractional ELU (FracELU) is the fractional variant of the ELU (see section 3.6.48) proposed. It is defined using fractional calculus as where a i ∈ and b are fixed parameters. The fractional derivative is then calculated as 68 The FALU was published in without any links to even though it was proposed by the same first author and it uses the same principles.

<!-- chunk {"id": "body-0419", "role": "body", "section": "Fractional SiLU (FracSiLU)", "weight": 1.0} -->

The fractional SiLU (FracSiLU) is the fractional variant of the SiLU (see section 3.3) proposed. It is defined using fractional calculus as While Job et al. intended the fractional SiLU (FracSiLU) to be the fractional variant of the SiLU (see section 3.3), they used a wrong definition of the SiLU. Here we present both the FracSiLU from the and the FracSiLU that fit the definition of SiLU - the definition from will be denoted as FracSiLU variant 1 (FracSiLU1) whereas the variant we derived as FracSiLU variant 1 (FracSiLU2). The Job et al. used this definition 69 of SiLU: Then the FracSiLU1 is defined as where σ (z i) is the logistic sigmoid. The fractional derivative is then calculated as where B n is n-th Bernoulli's number.

<!-- chunk {"id": "body-0420", "role": "body", "section": "Fractional SiLU (FracSiLU)", "weight": 1.0} -->

When using the SiLU definition from section 3.3, the FracSiLU2 is then defined as Since Job et al. made no assumption about the sign of z i, the fractional derivative of FracSiLU2 is computed as where B n is n-th Bernoulli's number.

<!-- chunk {"id": "body-0421", "role": "body", "section": "Fractional GELU (FracGELU)", "weight": 1.0} -->

Similarly as for FracSiLU, Job et al. intended the fractional GELU (FracGELU) to be the fractional variant of the GELU (see section 3.3.1), but they used a wrong definition of the GELU. Here we present both the FracGELU from the and the FracGELU that fit the definition of GELU - the definition from will be denoted as FracGELU variant 1 (FracGELU1) whereas the variant we derived as FracGELU variant 1 (FracGELU2). The Job et al. used this definition 70 of GELU: where Φ(z) is the standard Gaussian CDF.

<!-- chunk {"id": "body-0422", "role": "body", "section": "Fractional GELU (FracGELU)", "weight": 1.0} -->

Then the FracGELU1 is defined as The fractional derivative of FracGELU1 is then calculated as When using the GELU definition from section 3.3.1, the FracGELU2 is then defined as Since Job et al. made no assumption about the sign of z i, the fractional derivative of FracGELU2 is computed as 69 Job et al. referenced for their definition of SiLU; however, the contains the SiLU definition from section 3.3 and does not mention SiLU at all.

<!-- chunk {"id": "body-0423", "role": "body", "section": "Fractional GELU (FracGELU)", "weight": 1.0} -->

70 Job et al. referenced for their definition of SiLU; however, neither nor contains a definition of GELU.

<!-- chunk {"id": "body-0424", "role": "body", "section": "Scaled softsign", "weight": 1.0} -->

An activation function called scaled softsign is an adaptive variant of the softsign activation (see section 3.2.13) with variable amplitude. It is defined as where a i and b i are trainable parameters for each neuron i. The parameter a i controls the range of the output while the parameter b i controls the rate of transition between signs.

<!-- chunk {"id": "body-0425", "role": "body", "section": "Parameterized softplus (s+2L)", "weight": 1.0} -->

Parameterized softplus is an adaptive variant of a softplus activation function that allows for vertical shifts. It is defined as where a i ∈ is a trainable parameter for each neuron i. Vargas et al. also proposed a non-adaptive variant with fixed a i that is denoted as s + 2.

<!-- chunk {"id": "body-0426", "role": "body", "section": "Universal activation function (UAF)", "weight": 1.0} -->

The so-called universal activation function (UAF) is a softplus based AAF proposed. It is defined as where a i, b i, c i, d i, and e i are trainable parameter for each neuron i. For example, the UAF is able to well approximate the step function, logistic sigmoid, tanh, ReLU, LReLU, and Gaussian function.

<!-- chunk {"id": "body-0427", "role": "body", "section": "Learnable extended activation function (LEAF)", "weight": 1.0} -->

The learnable extended activation function (LEAF) is an AAF proposed in that is able to replace several existing AFs. It is defined as where σ (x) is the logistic sigmoid and a i, b i, c i, and d i are trainable parameters for each neuron i. The table 1 contains a list of AFs that are equivalent to a particular LEAF parameterization.

<!-- chunk {"id": "body-0428", "role": "body", "section": "Generalized ReLU (GReLU)", "weight": 1.0} -->

Theb generalized ReLU (GReLU) is an AF based on the UAF (see section 4.22). It is defined as where a i and b i are trainable parameters.

<!-- chunk {"id": "body-0429", "role": "body", "section": "Multiquadratic activation function (MAF)", "weight": 1.0} -->

The multiquadratic activation function (MAF) was used. It is defined as where a i and b i are trainable parameters a i is the slope coefficient and b i is the bias coefficient.

<!-- chunk {"id": "body-0430", "role": "body", "section": "EIS activation functions", "weight": 1.0} -->

The EIS 71 is a family of AAFs proposed in with three notable examples EIS-1, EIS-2, and EIS-3.

<!-- chunk {"id": "body-0431", "role": "body", "section": "EIS activation functions", "weight": 1.0} -->

The general EIS is defined as where a i, b i, c i, d i, and e i are either trainable parameters or fixed hyperparameters; a i ∈, b i ∈ [0, ∞), c i ∈ [0, ∞), d i ∈ [0, ∞), e i ∈ [0, ∞) and b i, c i, and d i cannot be equal to zero at the same time.

<!-- chunk {"id": "body-0432", "role": "body", "section": "EIS activation functions", "weight": 1.0} -->

The EIS-1 is defined as where d i and e i are trainable parameters. It can be obtained from the general EIS by setting a i = 1, b i = 0, c i = 1.

<!-- chunk {"id": "body-0433", "role": "body", "section": "EIS activation functions", "weight": 1.0} -->

The EIS-2 is defined as where b i is a trainable parameter. It can be obtained from the general EIS by setting a i = 1, d i = 0; however, the EIS-2 from also fixes c i = 1.

<!-- chunk {"id": "body-0434", "role": "body", "section": "EIS activation functions", "weight": 1.0} -->

And finally, the EIS-3 is defined as where d i and e i are trainable parameters; it can be obtained from the general EIS by setting a i = 0, b i = 1, c i = 0.

<!-- chunk {"id": "body-0435", "role": "body", "section": "EIS activation functions", "weight": 1.0} -->

The EIS family contains the softplus, swish, and ISRU as special cases.

<!-- chunk {"id": "body-0436", "role": "body", "section": "Linear combination of parameterized softplus and ELU (ELUs+2L)", "weight": 1.0} -->

A linear combination of parameterized softplus and ELU (ELUs + 2L) is an adaptive activation function combining ELUs and parameterized softplus activation functions. It is defined as where b i is a trainable parameter for each neuron i, ELU(z i) is the ELU activation function and s + 2L(z i) is the parameterized softplus activation function. The variant with non-adaptive parameterized softplus is denoted as ELUs + 2.

<!-- chunk {"id": "body-0437", "role": "body", "section": "Global-local neuron (GLN)", "weight": 1.0} -->

The global-local neuron (GLN) is an AAF that is a convex combination of two AFs proposed. It is defined as where a l and b l are trainable weights for each layer l and global(z l) and local(z l) are AFs capable of identifying the global and local characteristics respectively; the authors used global(z l) sin (z l) and local(z l) = tanh(z l).

<!-- chunk {"id": "body-0438", "role": "body", "section": "Neuron-adaptive activation function", "weight": 1.0} -->

A similar approach to trainable amplitude and generalized hyperbolic tangent is the so-called neuron-adaptive activation function (NAF), which comprises of a linear combination of two activation functions with scalable amplitude: where a, b, c, and d are trainable parameters that are shared by the whole network. The NAF was shown to perform superiorly on a few regression tasks.

<!-- chunk {"id": "body-0439", "role": "body", "section": "Neuron-adaptive activation function", "weight": 1.0} -->

71 The EIS is a name given by Biswas et al.; it is not an abbreviation.

<!-- chunk {"id": "body-0440", "role": "body", "section": "Scaled logistic sigmoid", "weight": 1.0} -->

A scaling variant of logistic sigmoid called scaled logistic sigmoid was proposed. The function is defined as where a i and b i are trainable parameters for each neuron i. Note that this activation is identical to the second part of the previously proposed NAF (see section 4.28).

<!-- chunk {"id": "body-0441", "role": "body", "section": "Scaled logistic sigmoid", "weight": 1.0} -->

A variant combining scaled logistic sigmoid with scaled sine (SLS-SS) was also used; it has four trainable parameters and is defined as where a i, b i, c i, and d i are trainable parameters. This activation function is a special case of another variant of NAF: where a i, b i, c i, d i, e i and f i are trainable parameters.

<!-- chunk {"id": "body-0442", "role": "body", "section": "Adaptive piece-wise linear unit (APLU)", "weight": 1.0} -->

Another generalization of ReLU is the adaptive piece-wise linear unit (APLU), which uses the sum of hinge-shaped functions as the activation function. An approach extending APLU is smooth adaptive activation function (SAAF) with piece-wise polynomial form and was specifically designed for regression and allows for bias-variance trade-off using a regularization term. where S is the number of hinges, i is the number of neurons, and a s i, b s i, s ∈ 1,..., S are trainable parameters per unit. However, the optimizer might choose very large values of a s i and balance them by very small weights, which could lead to numerical instabilities; therefore, an L 2 penalty is added to the parameters a s i, b s i scaled by 0.001. Another adaptive piecewise linear function was proposed, where a weighted combination of ReLUs with additional parameters was used.

<!-- chunk {"id": "body-0443", "role": "body", "section": "Simple piecewise linear and adaptive function with symmetric hinges (SPLASH)", "weight": 1.0} -->

The simple piecewise linear and adaptive function with symmetric hinges (SPLASH) is an approach similar to the APLU. It is defined as where S is an odd number, b l,s and -b l,s are hinge parameters and a + l,s and a -l,s are scaling parameters for each layer l; these max functions form S +1 continuous line segments with hinges at b l,s and -b l,s. While Tavakoli, Agostinelli, and Baldi tried different values for S, they found that using S = 7 usually works well.

<!-- chunk {"id": "body-0444", "role": "body", "section": "Multi-bias activation (MBA)", "weight": 1.0} -->

An approach similar to APLU and paired ReLU (see section 4.2.26) termed multi-bias activation (MBA) uses the same activation but with multiple biases, which allows to learn more complex activations; in this it resembles paired ReLU as one input map leads to several output maps with activation with different biases. The weights that will be given to the output maps in the next layer are similar to the weights in the APLU; however, the MBA is able to provide cross-channel information due to multiple outputs for each activation. The MBA is defined as where b i,k, k = 1, 2,..., K are trainable biases and g (x) is any non-linear activation function; Li, Ouyang, and Wang used ReLU as the activation function g (x).

<!-- chunk {"id": "body-0445", "role": "body", "section": "Mexican ReLU (MeLU)", "weight": 1.0} -->

A Mexican ReLU (MeLU) is an activation function with a similar approach as the APLU, but it does not need any L 2 penalty. The MeLU is defined as where a i,j are trainable parameters for each neuron/filter i, and k is the total number of trainable parameters (k -1 for the sum and one for the PReLU), b j and c j are fixed constants that are chosen recursively (more details in); ϕ b j c j (z i) is defined as Maguolo, Nanni, and Ghidoni used k = 4 and k = 8 for their experiments; the trainable parameters a i,j were all initialized to zero which helps the training at the early stages by exploiting the properties of the ReLU (e.g., the MeLU is convex for many iterations at the beginning). The advantage of the MeLU over the APLU is that it needs only half of the parameters while retaining the same representation power when the parameters are jointly optimized with the network's weights and biases.

<!-- chunk {"id": "body-0446", "role": "body", "section": "Modified Mexican ReLU (MMeLU)", "weight": 1.0} -->

The modified Mexican ReLU (MMeLU) is an MeLU inspired AF proposed. It is defined as where a i, b i, and c i are adaptive parameters estimated using Bayesian procedure outlined; a i ∈, b i ∈ R +, and c i ∈ R.

<!-- chunk {"id": "body-0447", "role": "body", "section": "Gaussian ReLU (GaLU)", "weight": 1.0} -->

The Gaussian ReLU (GaLU) is a MeLU-inspired AAF proposed. It uses the same basic form as MeLU has in eq. but it uses following ϕ b j c j (z i): where b j and c j are similar parameters is in the original MeLU; more details about the parameters is available.

<!-- chunk {"id": "body-0448", "role": "body", "section": "Hard-Swish", "weight": 1.0} -->

The Hard-Swish is an adaptive variant of a scaled Hard sigmoid activation. It is defined as where b i is either trainable or fixed parameter. For b i →∞, the Hard-Swish approaches the ReLU. The Hard-Swish outperformed the logistic sigmoid, tanh, ReLU, LReLU, and swish on the MNIST dataset. The ResNet, wide residual network (WRN), and DenseNet with glshardswish outperformed their variants with ReLU and swish on the CIFAR-10 dataset.

<!-- chunk {"id": "body-0449", "role": "body", "section": "S-shaped rectified linear activation unit (SReLU)", "weight": 1.0} -->

A S-shaped ReLU (SReLU) consists of three piecewise linear functions that are controlled by four trainable parameters that are learned jointly with the whole network. The SReLU is able to learn both convex and non-convex functions; in particular, it is able to learn both ReLU and also sigmoidlike functions. It is similar to APLU (see section 4.29), but APLU approximates non-convex functions, and it requires the rightmost linear function to have a unit slope and bias of zero. SReLU is defined as where t r i, t l i, a r i, and a l i are trainable parameters for each neuron i (or channel i in case of convolutional neural networks). The parameters t r i and t l i determine thresholds of an interval outside which the slope of the linear parts is controlled by parameters a r i and a l i, respectively. The authors Jin et al. show that the SReLU outperformed the ReLU, LReLU, PReLU, APLU, maxout unit and plain NIN on several visual tasks.

<!-- chunk {"id": "body-0450", "role": "body", "section": "S-shaped rectified linear activation unit (SReLU)", "weight": 1.0} -->

The authors also recommend to initialize the parameters of SReLU to t i ∈ R, a r i:= 1, t l i:= 0, and a l i ∈ which degenerates the SReLU into a LReLU and then keep these parameter fixed during several initial training epochs. The SReLU can be seen as a more general concept to the later proposed piecewise linear unit (PLU) (see section 4.35) and to the BLReLU (see section 3.6.24).

<!-- chunk {"id": "body-0451", "role": "body", "section": "N-activation", "weight": 1.0} -->

The N-activation is activation very similar to a special case of SReLU 72 proposed. The N-activation with trainable parameters a i, and b i is defined as

<!-- chunk {"id": "body-0452", "role": "body", "section": "ALiSA", "weight": 1.0} -->

A special case of SReLU was later proposed under the name adaptive LiSA (ALiSA); it can be obtained by setting t r i:= 1 and t l i:== 0: where a r i and a l i are adaptive parameters. Its nonadaptive variant is called simply linearized sigmoidal activation (LiSA) and has parameters a r i and a l i fixed.

<!-- chunk {"id": "body-0453", "role": "body", "section": "Alternated left ReLU (All-ReLU)", "weight": 1.0} -->

The alternated left ReLU (All-ReLU) was proposed in for usage in sparse neural networks. It is inspired by the SReLU. It is defined as where a is a fixed parameter controlling the slope for negative inputs, l is the number of layers, and % is the modulo operation.

<!-- chunk {"id": "body-0454", "role": "body", "section": "Piecewise linear unit (PLU)", "weight": 1.0} -->

A PLU resembles two earlier proposed activation functions - the SReLU (see section 4.33) and adaptive piece-wise linear unit (see section 4.29); it can be even seen as a special case of the SReLU. where a i is either a trainable parameter or a predefined constant and b is a predefined constant; a variant with a = 0. 1 and b = 1 was shown. The advantage of the PLU compared to the SReLU is that it produces an invertible function (which is not always the case for the more general SReLU).

<!-- chunk {"id": "body-0455", "role": "body", "section": "Piecewise linear unit (PLU)", "weight": 1.0} -->

72 It would be a special case of SReLU if the the thresholds were directly trainable and not determined using the min and max functions.

<!-- chunk {"id": "body-0456", "role": "body", "section": "Adaptive linear unit (AdaLU)", "weight": 1.0} -->

The adaptive linear unit (AdaLU) is yet another piecewise linear AAF. It is defined as where a i, b i, c i, d i, and e i are trainable parameters for each neuron i. The parameters a i and b i control the offsets; c i and d i control the slope of each linear part, and e i is the saturation value.

<!-- chunk {"id": "body-0457", "role": "body", "section": "Trapezoid-shaped activation function (TSAF)", "weight": 1.0} -->

The trapezoid-shaped activation function (TSAF) (ref. from) is an AF consisting of four ReLUs. It is defined as where a i, b i, and c i are parameters 73 such that a i < b i and c i ∈ (0, 1].

<!-- chunk {"id": "body-0458", "role": "body", "section": "Adaptive Richard's curve weighted activation (ARiA)", "weight": 1.0} -->

Another function motivated by the swish activation function is the Adaptive Richard's curve weighted activation (ARiA), which replaces the logistic sigmoid in the swish by Richard's curve. Richard's curve is a generalization of the logistic sigmoid that is controlled by several hyperparameters. The Richard's curve is defined as: where A is the lower asymptote, K is the upper asymptote, C is a constant (typically equal to 1), υ > 0 controls the direction of growth and B is the exponential growth rate, Q controls the initial value of the function. The ARiA is defined as where σ R (x) is the Richard's curve from eq.. As such, the ARiA has five hyperparameters controlling its behavior.

<!-- chunk {"id": "body-0459", "role": "body", "section": "Adaptive Richard's curve weighted activation (ARiA)", "weight": 1.0} -->

To reduce the number of the hyperparameters, Adaptive Richard's curve weighted activation 2 (ARiA2) was also proposed that is defined by only two hyperparameters a and b The swish activation function is a special case of ARiA with A = 1, K = 0, B = 1, υ = 1, C = 1, and Q = a i, where a i is the parameter of the swish activation function (see section 4.4.1 for details). The ARiA2 is a special case of ARiA with K = 0, B = 1, υ = 1, C = 1 a, and Q = b, where a and b are the ARiA2 hyperparameters. Patwardhan, Ingalhalikar, and Walambe reached best accuracy on the MNIST dataset with a custom CNN using ARiA2 with a = 1. 5 and b = 2; the best parameters for the DenseNet were a = 1. 75 and b = 1. While the parameters were fixed in the experiments, they can also be trainable as is in the special case of the swish activation function.

<!-- chunk {"id": "body-0460", "role": "body", "section": "Modified Weibull function", "weight": 1.0} -->

A modified Weibull function (MWF) is an Weibull-function-based AF proposed. It is defined as where a i, b i, c i, and d i are trainable parameters. The parameter b i determines the location of the peak of the AF. The polynomial term dominates for small input values while the exponential starts to dominate with larger values which reduces the output value as the input value further increases.

<!-- chunk {"id": "body-0461", "role": "body", "section": "Modified Weibull function", "weight": 1.0} -->

73 Pan et al. do not state whether they are used in trainable or fixed form.

<!-- chunk {"id": "body-0462", "role": "body", "section": "Sincos", "weight": 1.0} -->

The sincos is another older AF proposed. It is defined as where a, b, c, and d are adaptive parameters.

<!-- chunk {"id": "body-0463", "role": "body", "section": "Combination of sine and logistic sigmoid (CSS)", "weight": 1.0} -->

The combination of sine and logistic sigmoid (CSS) 74 is an AAF proposed. It is defined as where a, b, c, and d are adaptive parameters.

<!-- chunk {"id": "body-0464", "role": "body", "section": "Catalytic activation function (CatAF)", "weight": 1.0} -->

The catalytic activation function (CatAF) is an AAF that uses sinusoidal mixing of any AF and the identity to produce the final activation. It is defined as where a i is a trainable parameter and g (z i) is any AF such as the ReLU.

<!-- chunk {"id": "body-0465", "role": "body", "section": "Expcos", "weight": 1.0} -->

An AAF combining an exponential function with the cosine was proposed. It is called expcos in this work 75 and is defined as where a and b are adaptive parameters.

<!-- chunk {"id": "body-0466", "role": "body", "section": "Multi-bin trainable linear unit (MTLU)", "weight": 1.0} -->

The multi-bin trainable linear unit (MTLU) can be seen as a conceptual extension of the SReLU (see section 4.33) into more than three segments: where a i, 0,..., a i,K, and b i, 0,..., b i,K are trainable parameters for each neuron/filter and K and c i, 0,..., c i,K -1 are predefined hyperparameters. The authors used unifromly distributed anchors c i, 0,..., c i,K -1. The main disadvantage besides the higher number of additional parameters is the higher number of non-differentiable points. The MTLU was also named continuous piecewise nonlinear activation function (CPN)m. The CPNmc is a MTLU variant with continuity constraint proposed.

<!-- chunk {"id": "body-0467", "role": "body", "section": "Multi-bin trainable linear unit (MTLU)", "weight": 1.0} -->

An AF with the same form as the MTLU with only minor differences was proposed in under the name piecewise linear unit (PWLU); Zhu et al. also proposed its 2D extension. Unlike the MTLU, it uses a uniformly spaced demarcation points c i,k. Another PWLU variant named non-uniform piecewise linear unit (N-PWLU) allows for learnable intervals on which the function is piecewise linear, and also it leverages cumulative definition for efficient learning. Multistability analysis of such piecewise linear AFs is analyzed. An analysis of a number of regions of piecewise linear NNs is available.

<!-- chunk {"id": "body-0468", "role": "body", "section": "Multi-bin trainable linear unit (MTLU)", "weight": 1.0} -->

74 The function was unnamed; we used this abbreviation to distinguish it from SinSig.

<!-- chunk {"id": "body-0469", "role": "body", "section": "Multi-bin trainable linear unit (MTLU)", "weight": 1.0} -->

75 The function was originally unnamed.

<!-- chunk {"id": "body-0470", "role": "body", "section": "Continuous piecewise nonlinear activation function CPN", "weight": 1.0} -->

A variant of the MTLU named CPN where the c i,k was used. It is defined as where a i, 0,..., a i,K, b i, 0,..., b i,K, c i, 0,..., d i,K -1 are trainable parameters for each neuron/filter, g (z i) is a non-linear function such as the logistic sigmoid and K and c i, 0,..., d i,K -1 are predefined hyperparameters.

<!-- chunk {"id": "body-0471", "role": "body", "section": "Continuous piecewise nonlinear activation function CPN", "weight": 1.0} -->

Gao et al. also proposed a variant named CPNnl, which introduces a non-linear term for each small interval and does not enforce the uniform division of the activation space. It is defined as where K is the number of functions and a i,k, b i,k, and c i,k are learnable coefficients for k = 0, 1,..., K.

<!-- chunk {"id": "body-0472", "role": "body", "section": "Look-up table unit (LuTU)", "weight": 1.0} -->

A piecewise activation function look-up table unit (LuTU) is a learnable activation function that consists of several points defining the function; the values between the points are obtained using either linear interpolation or smoothing with single period cosine mask function. Similar adaptive activation function using linear interpolation was used. A look-up table of anchor points { a i,j, b i,j }, j = 0, 1,..., n that are uniformly spaced with step s, a i,j = a 0 + s · j, controls the shape of the activation functions. The step s, anchor points a 0, and n are predetermined hyperparameters, and therefore a i,j are predetermined values for which the output values b i,j are learnable parameters. Linear-interpolation-based function is defined as where a i,j are hyperparameters defined by the step s and initial point a 0 shared for all points and b i,j are trainable parameters for each neuron i. Wang, Liu, and Foroosh used a 0 = -12, step s = 0.

<!-- chunk {"id": "body-0473", "role": "body", "section": "Look-up table unit (LuTU)", "weight": 1.0} -->

1 and n = 240 to cover the interval using 241 anchor poiints for each neuron. Therefore, for any input value between a i,j and a i,j +1, the output is linearly interpolated from b i,j and b i,j +1. However, such a definition might lead to unstable gradients; therefore, a variant of LuTU with cosine smoothing was also proposed. The smoothing function is defined as where τ is a hyperparameter controlling the period (2 τ) of the cosine function. The smoothed variant of the LuTU is then defined as where t is an integer defining the ration between τ and s. The formula in eq. can be further simplified as it is not necessary to sum over all j ∈ { 0, 1,..., n } as the smoothing function has a truncated input domain, more details.

<!-- chunk {"id": "body-0474", "role": "body", "section": "Maxout unit", "weight": 1.0} -->

Maxout unit returns the maximum of multiple linear functions per each unit i: where where K is the number of linear functions. The maxout unit can also be used directly on inputs of the neuron as shown in (by replacing w k i z i with x T i w k i where x i ∈ R d is the vector of individual inputs to a neuron i and w ∈ R d are trainable weights) but the equation presented here uses only the hidden state for simplicity. The advantage of maxout unit is that it is a universal approximator of a convex function; however, it cannot learn non-convex functions and introduces a high number of additional parameters per neuron. While some works show that maxout unit perform superiorly, other experiments show that ReLU, which is a special case of maxout, performs better. Furthermore, since the maxout unit is more complex than regular ReLU, the training is relatively slower.

<!-- chunk {"id": "body-0475", "role": "body", "section": "Maxout unit", "weight": 1.0} -->

Empirical comparison of the maxout unit with ReLU, LReLU, SELU and tanh is available; with ReLU, tanh, sigmoid and VLReLU.

<!-- chunk {"id": "body-0476", "role": "body", "section": "Adaptive blending unit (ABU)", "weight": 1.0} -->

An approach mixing several activation functions was described in where ABU was introduced. The ABU is a weighted sum of several predefined activations. It is defined as where g j (z l) is an activation function from a pool of n activation functions and a j,l is a weighting parameter that is trained for each layer l and activation function g j (z l). The ABU was first proposed as a special case of a general framework called TAF already in 1997. The blending weights a j,l are initialized to 1 n but are then trained alongside the weights of the NN. Sütfeld et al. used tanh, ELU, ReLU, swish, and the identity as the pool of activation functions g j but they admit that no exhaustive search was performed to select this set and that there might be other pools that perform better. This approach was also used in where ReLU, logistic sigmoid, tanh, and softsign activation functions were used.

<!-- chunk {"id": "body-0477", "role": "body", "section": "Adaptive blending unit (ABU)", "weight": 1.0} -->

However, similar approach was already proposed in where Wang, Liu, and Foroosh inspired by the mixture of Gaussian unit (MoGU) (see section 4.48.10) generalized the concept to mixing several different activation functions where g j (z i) is an activation function from a pool of n activation functions, a i,j is a trainable weighting parameter of the function g j (z i) and b i,j is a trainable parameter controlling the vertical shift of the function g j (z i) for each neuron i. Furthermore, if g j (z i) already contains a way for controlling its scale or shift, the parameters a i,j and b i,j can be discarded. This approach is identical to the ABU from if b i,j = 0 and the parameters are shared by all neurons in the same layer and not learned for each neuron separately.

<!-- chunk {"id": "body-0478", "role": "body", "section": "Adaptive blending unit (ABU)", "weight": 1.0} -->

A very similar approach was proposed, where Manessi and Rozza use a linear combination of activation functions from a selected pool as the final activation function. The difference from the ABU is that the weights are constrained such that they sum up to 1. Manessi and Rozza uses analyses the linear combination of identity, ReLU, and tanh activation functions. Sütfeld et al. analyzed the performance of unconstrained ABUs and ABUs with various constraints such as ∑ n j =0 a j,l = 1, ∑ n j =0 | a j,l | = 1, and two approaches enforcing ∑ n j =0 a j,l = 1 and a j,l > 0 -clipping of negative values a j,l before normalization and softmax normalization. It was found that the unconstrained ABU works the best on average on the selected tasks; however, some of the constrained variants performed better than the unconstrained ABU for particular tasks.

<!-- chunk {"id": "body-0479", "role": "body", "section": "Adaptive blending unit (ABU)", "weight": 1.0} -->

Another variant of ABU (called by Klabjan and Harmon activation ensemble) was proposed in - the final activation is a weighted sum of activation functions; the weighting coefficients has to sum-up to 1 (similarly to). However, unlike in the work, the individual activation functions are scaled before the weighting to the interval using min-max scaling: where g j are individual activation functions, ϵ is a small number and k goes through all training samples in a minibatch.The final output is where a j,i is a weight for each neuron i and activation function j, n is the total number of the individual activation functions in the ABU; the weights a j,i ∈ are constrained such that

<!-- chunk {"id": "body-0480", "role": "body", "section": "Trainable compound activation function (TCA)", "weight": 1.0} -->

The trained compound activation function (TCA) is an AAF similar to the ABU and especially to its variant with the bias (see eq.); however, unlike the form from eq. it uses horizontal scaling instead of the vertical. It was defined in as where k is the number of mixed functions and a i,j and b i,j, j = 1,..., k, are scaling and translation trainable parameters for each neuron i and function j. The TCA was found to improve the performance of restricted Boltzmann machines (RBMs) and deep belief networks (DBNs).

<!-- chunk {"id": "body-0481", "role": "body", "section": "Trainable compound activation function (TCA)", "weight": 1.0} -->

Later, Baggenstoss introduced a TCA also with vertical scaling parameters. This slightly different variant is denoted as trained compound activation function variant 2 (TCAv2) throughout this work. TCAv2 is defined as where k is the number of mixed functions and a i,j, b i,j and c i,j, j = 1,..., k, are scaling and translation trainable parameters for each neuron i and function j.

<!-- chunk {"id": "body-0482", "role": "body", "section": "Average of a pool of activation functions (APAF)", "weight": 1.0} -->

An average of a pool of activation functions (APAF) was used; the output is defined as Liao used the ReLU, logistic sigmoid, tanh, and the linear functions as the candidate functions in the pool. This approach was also used.

<!-- chunk {"id": "body-0483", "role": "body", "section": "Gating adaptive blending unit (GABU)", "weight": 1.0} -->

Yet another approach previously proposed employs a gated linear combination of activation functions for each neuron - the variant is called gating adaptive blending unit (GABU) throughout this work. This allows each neuron to choose which activation function (from an existing pool) it may use to minimize the error. A similar method uses just binary indicators instead of the gates. The gating variant of ABU from is defined as where σ (a j,i) is the logistic sigmoid function acting as gating function and a j,i is a trainable parameter controlling the weight of the activation function g j for each neuron i.

<!-- chunk {"id": "body-0484", "role": "body", "section": "Deep Kronecker neural networks", "weight": 1.0} -->

The concept of ABUs was further generalized in the framework of Deep Kronecker neural networks (DKNNs), which provides an efficient way of constructing wide networks with adaptive activation functions while keeping the number of parameters low. DKNNs are equivalent to the feed-forward neural networks with an adaptive activation function f defined as where z l is a preactivation of a neuron from a layer l, a l,j and b l,j are either trainable or fixed parameters and g j, j = 1,..., n are fixed activation functions.

<!-- chunk {"id": "body-0485", "role": "body", "section": "Rowdy activation functions", "weight": 1.0} -->

Rowdy activation functions are a general class of activation functions that is a special case of DKNNs (see section 4.48.4). A rowdy activation function is a DKNNs with any activation function (e.g., ReLU) that is the function g 0 from eq. and n other functions that are defined as where c ≥ 1 is a fixed scaling factor and j = 1,..., n. The rowdy activation functions introduce highly fluctuating, non-monotonic terms that remove saturation regions from the output of each layer in the network similarly as does the stochastic noise.

<!-- chunk {"id": "body-0486", "role": "body", "section": "Self-learnable activation function (SLAF)", "weight": 1.0} -->

The SLAF can be considered to be a special case of the ABU where the function g j (z i) are increasing powers of z i: where a i,j are learnable parameters for each neuron i and k is a hyperparameter defining the number of elements in the polynomial expression. However, since the gradient is proportional to z i and its powers, Goyal, Goyal, and Lall used mean-variance normalization over the training sample to avoid exploding or vanishing gradients. A similar concept was analyzed, where it was applied to the output neuron only. A similar approach was used independently, where authors used the equivalent of SLAF with k = 6. A quadratic variant (i.e., SLAF with k = 2) was used.

<!-- chunk {"id": "body-0487", "role": "body", "section": "Chebyshev polynomial-based activation function (ChPAF)", "weight": 1.0} -->

A Chebyshev polynomial-based activation function (ChPAF) was proposed. The function is defined as where a j, j = 0,..., k are learnable parameters shared by a whole network, k is a fixed hyperparameter denoting the maximum order of used Chebyshev polynomials, and C j (z) is a Chebyshev polynomial of order j defined as with starting values C 0 (z) = 1 and C 1 (z) = z. Deepthi, Vikram, and Venkatappareddy used polynomials of a maximum order of 3 in their experiments. The Chebyshev activation function was found to outperform several activation functions including ReLU, ELU, mish and swish while retaining fast convergence using the CIFAR-10 dataset as shown in experiments.

<!-- chunk {"id": "body-0488", "role": "body", "section": "Legendre polynomial-based activation function (LPAF)", "weight": 1.0} -->

A Legendre polynomial-based activation function (LPAF) was used for the study of approximations of several nonlinearities. The activation is a linear combination of Legendre polynomials and is defined as where a j, j = 0,..., k are learnable parameters shared by a whole network, k is a fixed hyperparameter denoting the maximum order of used Legendre polynomials, and G j (z) is a Legendre polynomial of order j defined as with starting values G 0 (z) = 1 and G 1 (z) = z. The LPAF was found to outperform ELU, ReLU, LReLU, and softplus on the MNIST and Fashion MNIST datasets.

<!-- chunk {"id": "body-0489", "role": "body", "section": "Hermite polynomial-based activation function (HPAF)", "weight": 1.0} -->

The Hermite polynomial-based activation function (HPAF) is an AAF similar to ChPAF and LPAF but it used the Hermite polynomials instead. It is defined as where a j is a trainable parameter and H j (z) is the Hermite polynomial

<!-- chunk {"id": "body-0490", "role": "body", "section": "Mixture of Gaussian unit (MoGU)", "weight": 1.0} -->

The mixture of Gaussian unit (MoGU) was proposed in as a byproduct of analysis of the behavior of the LuTU unit (see section 4.46) as the shape of learned activation units with the cosine smoothing mostly composed of a few peaks and valleys. The MoGU is defined as where a i,j, σ i,j, and µ i,j are trainable parameters for each neuron i and Gaussian j from the mixture. The parameter a i,j controls the scale, σ i,j controls the standard deviation, and µ i,j controls the mean of the Gaussian j for neuron i.

<!-- chunk {"id": "body-0491", "role": "body", "section": "Fourier series activation", "weight": 1.0} -->

The Fourier series activation (FSA) was proposed. It is defined as where a i, b i,j, c i,j, d i are trainable parameters for each neuron i, and r is a fixed hyperparameter denoting the rank of the Fourier series; Liao used r = 5 throughout his experiments.

<!-- chunk {"id": "body-0492", "role": "body", "section": "Padé activation unit (PAU)", "weight": 1.0} -->

Padé activation units (PAUs) are adaptive activations based on the Padé approximant. The PAU is defined as where m and n are hyperparameters denoting the order of the polynomials and a j, j = 0,..., m and b k, k = 1,..., n are trainable parameters that are globaly shared by all units. While the Padé approximation could be used to approximate particular activation function, the parameters a j and b k are optimized freely with other weights of the neural network. This PAU variant was for reinforcement learning in where Delfosse et al. observed that rational functions might replace some of the residual blocks in ResNets. To avoid numerical instabilities, a safe PAU ensures that the polynomial in the denominator cannot be zero; it is defined as The hyperparameters were set to m = 5 and n = 4 in experiments. The notion of using rational functions in activations was further analyzed in where authors used activation function equivalent to eq.

<!-- chunk {"id": "body-0493", "role": "body", "section": "Padé activation unit (PAU)", "weight": 1.0} -->

with distinct parameters for each layer to learn rational neural networks; the safe variant of PAU (eq.) was not used as it results in non-smooth activation function and expensive calculation of gradient during training. Boulle, Nakatsukasa, and Townsend used low degrees m = 3 and n = 2 in their work; this is in contrast to where rational functions of higher orders were used in a graph neural networkss.

<!-- chunk {"id": "body-0494", "role": "body", "section": "Randomized Padé activation unit (RPAU)", "weight": 1.0} -->

The PAU can be extended similarly as RReLU extends ReLU, resulting in randomized Padé activation unit (RPAU). Let C = { a 0,..., a m, b 0,..., b n } be coefficients of PAU activation (see section 4.49). Then an additive noise is introduced into each coefficient c j ∈ C during training for every input z k such that c j,k = c j + z j,k, where z j,k ∼ U(l j, u j), l j = (1 -a) c j and u j = (1 + a) c j. This results in RPAU: where z k is output of a unit for training input k.

<!-- chunk {"id": "body-0495", "role": "body", "section": "Enhanced rational activation (ERA)", "weight": 1.0} -->

The enhanced rational activation (ERA) function is very similar to the original PAU (see section 4.49); however, Trimmel et al. note similarly as Boulle, Nakatsukasa, and Townsend that the safe version of PAU is costly to compute whereas the original PAU has undefined values on poles (values of z where the denominator in PAU is equal to zero). To avoid both the poles and the use of absolute value, a modified rational function without the poles is used. The ERA is defined as where a j, j = 0,..., m, c k, and d k, k = 1,..., n are trainable parameters for each layer and ϵ > 0 is a small number helping to avoid numerical instabilities when d k are small. In practice, Trimmel et al. used ϵ = 10 -6. The ERA in eq. can be rewritten using partial fractions, which reduces the number of operations and, therefore, leads to more efficient computation. Trimmel et al. used m = 5 and n = 4 for their experiments.

<!-- chunk {"id": "body-0496", "role": "body", "section": "Orthogonal Padé activation unit (OPAU)", "weight": 1.0} -->

The orthogonal Padé activation unit (OPAU) is an extension of the PAU proposed. It is defined as where a j, j = 0,..., m and b k, k = 1,..., n are trainable weights, m and n are fixed parameters, and r j (z) belongs to a set of orthogonal polynomials. The sage OPAU is defined 76 as with identical parameters as the OPAU from eq.. Biswas, Banerjee, and Pandey used six bases for orthogonal polynomials - Chebyshev polynomials (two variants), Hermite polynomials (also two variants), Laguerre, and Legendre polynomials - as shown in table 2.

<!-- chunk {"id": "body-0497", "role": "body", "section": "Spline interpolating activation functions", "weight": 1.0} -->

More complex approaches include spline interpolating activation functions (SAFs), which facilitate the training of a wide variety of activation functions using interpolation. One common example is the cubic spline interpolation that was used. The SAFs are controlled by a vector q ∈ R k of internal parameters called knots, which are a sampling of the AF over k representative points. The output is computed using a spline interpolation using the closest knot and its p rightmost neighbors; p = 3 results in cubic interpolation. Spline-based activation functions were also used in the ExSpliNet - an interpretable approach combining neural networks and ensembles of probabilistic trees. A set of fixed but highly redundant knots for spline interpolation was used, where the authors then relied on the sparsifying effect of L 1 regularization to nullify the coefficients that are not needed. Spline flexible activation functions were used for sound synthesis. The usage of splines led to the creation of b-spline-based neural networks, e.g.,.

<!-- chunk {"id": "body-0498", "role": "body", "section": "Spline interpolating activation functions", "weight": 1.0} -->

Similar to the SAF is the piecewise polynomial activation function (PPAF) that is also defined by a number of points where the function switches from one polynomial to another. López-Rubio et al. used zeroth-order, List of polynomial bases used in the OPAU taken. The Chebyshev polynomials and the Laguerre polynomial have recurrent definitions; whereas the Legendre and the Hermite polynomials are defined by a single expression.

<!-- chunk {"id": "body-0499", "role": "body", "section": "Spline interpolating activation functions", "weight": 1.0} -->

76 Using notation as described in the original article by Biswas, Banerjee, and Pandey.

<!-- chunk {"id": "body-0500", "role": "body", "section": "Spline interpolating activation functions", "weight": 1.0} -->

If there are no constrains and the AF is limited to linear splines, the AF can be also defined using one hidden layer with ReLUs: where K ∈ N and a i,k, b i,k, and c i,k are trainable parameters.

<!-- chunk {"id": "body-0501", "role": "body", "section": "Truncated Gaussian unit (TruG)", "weight": 1.0} -->

A truncated gaussian unit (TruG) is a unit in a probabilistic framework that is able to well approximate sigmoid, tanh, and ReLU. It is controlled by truncation points ξ 1 and ξ 2 and under the probabilistic framework described in is defined as where ϕ (x) is the probability density function (PDF) of a univariate Gaussian distribution with mean z and variance σ 2 and Φ(x) its CDF. The truncation points can be either selected manually or tuned with the rest of the weights.

<!-- chunk {"id": "body-0502", "role": "body", "section": "Mollified square root function (MSRF) family", "weight": 1.0} -->

Pan et al. used a smoothing approach on piecewise linear AFs to create a whole new family of AFs. The approach is based on the mollified square root function (MSRF) method. This smoothing approach was first used in and then in the SquarePlus AF, which inspired Pan et al. in the creation of the MSRF family of AFs.

<!-- chunk {"id": "body-0503", "role": "body", "section": "Mollified square root function (MSRF) family", "weight": 1.0} -->

For example, the absolute value | x | is not differentiable at x = 0, but it can be regularized by mollification as where ϵ is a small positive parameter and lim ϵ → 0 + | x | ϵ = | x |.

<!-- chunk {"id": "body-0504", "role": "body", "section": "SquarePlus", "weight": 1.0} -->

The SquarePlus is the first AF that used the mollification procedure described in section 4.55 above. It is defined as The SquarePlus is very similar to the softplus (see section 3.17) for ϵ = 4(ln) 2 and they produce identical outputs at z = 0.

<!-- chunk {"id": "body-0505", "role": "body", "section": "StepPlus", "weight": 1.0} -->

As the SquarePlus approximates the ReLU, the StepPlus approximates the step function (see section 3.1) similarly as the logistic sigmoid does. It is defined as The sign function is smoothed into the BipolarPlus AF

<!-- chunk {"id": "body-0506", "role": "body", "section": "LReLUPlus", "weight": 1.0} -->

A smoothed variant of the LReLU called LReLUPlus is defined as where | x | ϵ is the MSRF procedure described in section 4.55 and a i is a fixed or trainable parameter.

<!-- chunk {"id": "body-0507", "role": "body", "section": "LReLUPlus", "weight": 1.0} -->

A function equivalent to the LReLUPlus was independently proposed in under the name SMU-1. The only difference was that Biswas et al. used parameter µ that is the square root of ϵ from section 4.55: ϵ = µ 2.

<!-- chunk {"id": "body-0508", "role": "body", "section": "vReLUPlus", "weight": 1.0} -->

The vReLUPlus is a MSRF smoothed variant of the vReLU (see section 3.6.25); it is defined as

<!-- chunk {"id": "body-0509", "role": "body", "section": "SoftshrinkPlus", "weight": 1.0} -->

The smoothed variant of the Softshrink (see section 3.6.23) is named SoftshrinkPlus 77 and is defined as where a is a fixed parameter similar to the original Softshrink's thresholding parameter.

<!-- chunk {"id": "body-0510", "role": "body", "section": "PanPlus", "weight": 1.0} -->

The MSRF procedure can be also used to smooth the pan AF (see section 3.6.26); the resulting PanPlus is defined as where a is a fixed thresholding parameter of the pan function.

<!-- chunk {"id": "body-0511", "role": "body", "section": "BReLUPlus", "weight": 1.0} -->

The BReLUPlus is a MSRF smoothed variant of the BReLU (see section 3.6.16) defined as 77 Pan et al. named the function STFPlus originally.

<!-- chunk {"id": "body-0512", "role": "body", "section": "SReLUPlus", "weight": 1.0} -->

Another smoothed AF is the SReLUPlus which is the smoothed variant of the SReLU (see section 4.33); it is defined as where a i has similar role as in the original SReLU and t i is a parameter for symmetric variant of SReLU with t i = t r i = t l i.

<!-- chunk {"id": "body-0513", "role": "body", "section": "HardTanhPlus", "weight": 1.0} -->

Similarly, the smoothed variant of the HardTanh (see section 3.6.18) named HardTanhPlus is defined as

<!-- chunk {"id": "body-0514", "role": "body", "section": "HardshrinkPlus", "weight": 1.0} -->

The smoothed variant of the Hardshrink (see section 3.6.22) is named HardshrinkPlus 78; it is defined as where a is a fixed parameter with a similar function as in the Hardshrink.

<!-- chunk {"id": "body-0515", "role": "body", "section": "MeLUPlus", "weight": 1.0} -->

Pan et al. also provided a smoothed variant of the MeLU (see section 4.32); however, the formula written in is not the MeLU AF but rather its single component ϕ b j c j (z i). Nevertheless, the full smoothed MeLUPlus can be obtained easily as the combination of the LReLUPlus and the smoothed ϕ Plus b j c j (z i) defined as where b j and c j are the same parameters as in the MeLU.

<!-- chunk {"id": "body-0516", "role": "body", "section": "TSAFPlus", "weight": 1.0} -->

The smoothed variant of the TSAF (see section 4.37) named TSAFPlus is defined as where a i, b i, and c i have a similar role as in the original TSAF.

<!-- chunk {"id": "body-0517", "role": "body", "section": "ELUPlus", "weight": 1.0} -->

Even the ELU (see section 3.6.48) can be mollified into a "smoothed" variant named ELUPlus. The smoothed variant is defined as where a is a fixed parameter 79 with a similar function as in the ELU.

<!-- chunk {"id": "body-0518", "role": "body", "section": "SwishPlus", "weight": 1.0} -->

The mollified variant of the swish (see section 4.4.1) named SwishPlus is defined using the smoothed step function instead of the logistic sigmoid; it is, therefore, defined as 78 Pan et al. named the function HTFPlus originally.

<!-- chunk {"id": "body-0519", "role": "body", "section": "SwishPlus", "weight": 1.0} -->

79 Pan et al. used variant with inverse parameter 1 a; we have used the same parameter variant as in the original ELU.

<!-- chunk {"id": "body-0520", "role": "body", "section": "MishPlus", "weight": 1.0} -->

The mollified variant of the swish (see section 3.3.29) named MishPlus is defined using the BipolarPlus and SquarePlus as

<!-- chunk {"id": "body-0521", "role": "body", "section": "LogishPlus", "weight": 1.0} -->

The mollified variant of the logish (see section 3.3.11) named LogishPlus is defined as

<!-- chunk {"id": "body-0522", "role": "body", "section": "SoftsignPlus", "weight": 1.0} -->

The mollified variant of the softsign (see section 3.2.13) named SoftsignPlus is defined as

<!-- chunk {"id": "body-0523", "role": "body", "section": "SignReLUPlus", "weight": 1.0} -->

Pan et al. provide a mollified version for an approximation of the SignReLU 80 (see section 3.6.32). They approximate the SignReLU as Using the approximation, they then define the SignReLUPlus as

<!-- chunk {"id": "body-0524", "role": "body", "section": "Complex approaches", "weight": 1.0} -->

The network in network (NIN), which uses a micro neural network as an adaptive activation function, represents a different approach. A combination of the NIN and maxout units called maxout-in-network (MIN) was shown to have good performance. A similar approach is the wide hidden expansion (WHE) layer, which is a sparselly connected layer with several activation functions that is used in place of a traditional activation function.

<!-- chunk {"id": "body-0525", "role": "body", "section": "Complex approaches", "weight": 1.0} -->

Adaptive activation functions called NPF that are learned nonparametrically were proposed in where a Fourier series basis expansion is used for nonparametric estimation. Only one NPF is learned per filter in CNNs while different activation is learned in each neuron of a fully connected layer; the learning is in two stages where the network is first learned with ReLUs in the convolution layers and NPF in all others and only then the network is learned with all activation functions being the NPF.

<!-- chunk {"id": "body-0526", "role": "body", "section": "Complex approaches", "weight": 1.0} -->

Yet another approach is learning activation functions using hypernetworks resting in hyperactivations. The hyperactivation consists of two parts - a shallow feed-forward neural network called activation network and a hypernetwork, which is a type of neural network that produces weights for another network. The hypernetwork is used for the normalization of the activation network. A single hyperactivation is learned for each layer in the neural network. A NN with a combination of more activation functions was used.

<!-- chunk {"id": "body-0527", "role": "body", "section": "Complex approaches", "weight": 1.0} -->

The adaptive activation function might also be trained in a semi-supervised manner.

<!-- chunk {"id": "body-0528", "role": "body", "section": "Variable activation function (VAF)", "weight": 1.0} -->

Similarly to NIN, the variable activation function (VAF) subnetwork approach uses simple activation functions to produce more complex behavior; the activation is replaced by a small subnetwork with one hidden layer with k neurons and only one input and one output neuron. Specifically, V AF is defined as 80 Pan et al. call it DLU throughout their work. where a l, 0, a l,j, b l,j, and c l,j, j = 1,..., k, are trainable parameters for each layer l and g(x) is an activation function such as tanh or ReLU that were used in experiments with VAF. The same concept of using subnetwork to learn the activation function was also proposed under the name of activation function unit (AFU).

<!-- chunk {"id": "body-0529", "role": "body", "section": "Flexible activation bag (FAB)", "weight": 1.0} -->

The flexible activation bag (FAB) is an approach similar to NIN and VAF as it uses a subnetwork to learn the AF for each layer l using a pool of K activations f k (z l, a l,k). It uses a shallow network with double head with ReLU activation in the first layer; then there are two separate heads. The first head predicts the parameters a l,k of the individual AFs f k (z l, a l,k) in the bag squashed by a sigmoid AF, then the parameters are mapped into a valid range of each of the parameters. The second head is a selective head for selecting an appropriate AF by producing a score s l,k -it can be either discrete or continuous resulting in soft or hard selection. Klopries and Schwung used five selection methods - all of the functions are used (s l,k = 1), hard selection, soft selection using logistic sigmoids, softmax selection, and Gumber-Softmax selection.

<!-- chunk {"id": "body-0530", "role": "body", "section": "Flexible activation bag (FAB)", "weight": 1.0} -->

The bag of activations used in the FAB consists of a constant function, linear function, exponential function, step function, ReLU, step function, sine function, tanh, logistic sigmoid, and Gaussian function (see for exact definitions with the adaptive parameters). Then the output of FAB is assembled as where s l,k are the selection scores of f k; the a l,k consists of parameters of the function f k (the used AFs have from one to three parameters) and the f k are the individual AFs from the bag of K functions.

<!-- chunk {"id": "body-0531", "role": "body", "section": "Dynamic parameter ReLU (DY-ReLU)", "weight": 1.0} -->

The dynamic parameter ReLU (DY-ReLU) (proposed under the name of dynamic ReLU in but that collides with previously proposed DReLUs in) is an activation function whose parameters are input dependent. The concept of DY-ReLU is similar to the WHE in and hyperactivations in as the DY-ReLU is an example of a hyperactivation. The dynamic activation function has two components - hyperfunction that computes parameters for the activation function and the activation function itself. The DY-ReLU piecewise linear function is computed as the maximum of multiple linear functions. It is defined as where K is a hyperparameter and a i,k and b i,k are coefficients determined by the hyper function θ (z) using all inputs z i. The hyperfunction θ (z) is a light-weight neural network. The parameters generated by the hyperfunction θ (z) can be different for each filter i, or they can be shared in the whole layer. The DY-ReLU can be considered as a dynamic and efficient variant of Maxout (see section 4.47).

<!-- chunk {"id": "body-0532", "role": "body", "section": "Random NNs with trainable activation functions", "weight": 1.0} -->

A very different approach based on adaptive activation functions is presented in where a neural network with random weights is initialized, and the weights are not trained, but the activation functions are trained instead. The activation functions in are polynomial activation functions and are trained separately for each hidden neuron with random weights first; only then the weights of the output layer are estimated. Ertu˘ grul used five different adaptive variants of activation functions: where a i and b i are trainable parameters.

<!-- chunk {"id": "body-0533", "role": "body", "section": "Kernel activation function (KAF)", "weight": 1.0} -->

A kernel activation function (KAF) is a non-parametric function that uses kernel expansion together with a dictionary to make the activation flexible. The KAF uses a weighted sum of kernel terms: where D is a fixed hyperparameter, a i,j are mixing coefficients and d j, j = 1,..., D are called dictionary elements and κ (z i, d j): R × R → R is 1D kernel function - Scardapane et al. consider only a i,j trainable and the dictionary elements d j are uniformly spaced around zero. This has the advantage that the resulting model is linear in its parameters and, therefore, can efficiently optimized.

<!-- chunk {"id": "body-0534", "role": "body", "section": "Kernel activation function (KAF)", "weight": 1.0} -->

The kernel function κ (z, d j) used in is the 1D Gaussian kernel defined as where γ ∈ R is a fixed parameter called the kernel bandwith. Scardapane et al. recommend setting the kernel bandwidth to where ∆ is the distance betwen the grid points as adapting γ through back-propagation did not yield any gain in accuracy. The mixing coefficients a i,j can be initialized either randomly from a normal distribution - this provided good diversity for the optimization process - or using kernel ridge regression to approximate an activation function of choice. Scardapane et al. also proposed 2D-KAF that works over all possible pairs of incoming values and uses 2D Gaussian kernel.

<!-- chunk {"id": "body-0535", "role": "body", "section": "Kernel activation function (KAF)", "weight": 1.0} -->

An extension of the KAF approach was presented in where activation function used was the sum of the KAF and RSigELU (see section 3.7.15) or KAF and RSigELUD (see section 3.7.19). Kernel methods are becoming more common in deep learning - e.g., fully kernected layers are replacing fully connected layers with a kernel-based approach.

<!-- chunk {"id": "body-0536", "role": "body", "section": "SAVE-inspired activation functions", "weight": 1.0} -->

Brad produced several AF that are, supposedly, motivated by human behavior. These AFs were created using the SAVE method and are mostly variations of the AFs listed above. For completeness' sake, a list of these AFs is included in our work in table 3 also with the real-life motivations listed in - however, no deeper analysis or objective evaluation of these AFs was not provided.

<!-- chunk {"id": "body-0537", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper provides an extensive survey of 400 neural network activation functions. Despite all its scope, it has some limitations and focuses on the largest family of real-valued activation functions categorized into two main classes: fixed activation functions and adaptive activation functions. The fixed activation functions that we also refer to as classical are predetermined mathematical functions that apply the same transformation to all inputs regardless of their values. Each neuron within a layer typically applies the same activation function to its inputs. Examples include logistic sigmoid, hyperbolic tangent, and ReLU functions. On the other hand, adaptive activation functions learn their parameters based on the input data and may thus change their shape. This feature allows for more flexibility and leads to faster convergence during training and improved performance. Examples of adaptive activation functions include PReLU, PELU, swish, and TAAF.

<!-- chunk {"id": "body-0538", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The profound impact of activation functions on network performance is undeniable, and the absence of a consolidated resource often results in redundant proposals and wasteful reinvention. By offering this comprehensive compilation, we aim to prevent the unnecessary duplication of established activation functions. While recognizing the limitations of our work in not conducting extensive benchmarks or in-depth analyses, we believe this exhaustive list will be a valuable reference for researchers. Even though this list will never be complete due to ongoing proposals of new activation functions, we believe it establishes a solid foundation for future research.
