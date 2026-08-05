<!-- arxiv-full-text:v1 {"arxiv_id": "2402.09092", "source": "arxiv-pdf"} -->

## Introduction

Neural networks - and deep learning in particular - have exhibited remarkable success in addressing diverse challenges across various fields. They stand as state-of-the-art approaches, showcasing their prowess in solving complex and intricate problems. At the heart of these networks, activation functions (AFs) play an important role by introducing nonlinearity to neural network layers. In the absence of nonlinear AFs, typical neural networks would only model a weighted sum of inputs, limiting their capacity to capture intricate relationships within the data.

The choice of activation functions profoundly influences a network's ability to learn and generalize, directly impacting its performance across a spectrum of tasks. Effective activation functions possess several key properties, as outlined by Dubey, Singh, and Chaudhuri : a) introducing non-linear curvature to enhance training convergence within the optimization landscape; b) maintaining an unobstructed gradient flow during training; c) ensuring a minimal increase in the computational complexity of the model; and d) preserving the distribution of data to optimize the network's training.

There are many activation functions proposed in the literature in the last three decades - some more computationally complex or with higher performance than others. However, further research of the activation functions is hampered by the absence of a consolidated list. This gap leads to the inadvertent reinvention of existing activation functions and the independent proposal of identical or very similar ones, resulting in a wasteful consumption of research resources. Even comprehensive surveys and reviews, such as those by Dubey, Singh, and Chaudhuri and Apicella et al., often omit numerous activation functions present in the literature; furthermore, these reviews are also a bit older and many new activation functions emerged since then. This oversight can lead to instances where an AF is redundantly proposed as novel, despite its prior introduction in the literature - e.g., rectified power unit (RePU) (section 3.6.39), dual parametric ReLU (DPReLU) (section 4.2.20), truncated rectified (TRec) (section 3.6.21), ReLU-Swish (section 3.6.46), and bounded ReLU (BReLU) (section 3.6.16). By providing a more extensive list of available activation functions, we aim to avoid such redundancy and promote faster advances in the research of activation functions in neural networks.

To address this issue, we strive to provide an extensive and consolidated list of available AFs. This survey aims to prevent redundancy, eliminate the reinvention of established AFs to promote innovation, and accelerate the advancement of research in the field of neural networks. By offering a comprehensive resource, we aim to promote efficiency and innovation in the exploration of AFs within the field.

It is important to note that our contribution primarily focuses on providing a comprehensive list of AFs rather than conducting extensive benchmarks or in-depth analyses. The breadth of the compilation encompasses a wide array of AFs, making a detailed benchmark or a deeper analysis beyond the scope of this work. Our aim is to provide researchers with a foundational resource that facilitates informed decision-making in selecting AFs for neural networks, recognizing that a more exhaustive exploration or detailed analysis would necessitate a dedicated and focused effort beyond the scope of this comprehensive listing. The presented overview is limited to real-valued activation functions; complex-valued neural networks (e.g. brief overview available in), bicomplex-valued neural networks (e.g.,), quaternion-valued neural networks (e.g.,), photonic neural networks (e.g.,), fuzzy neural networks (e.g.,), AFs for probabilistic boolean logic (e.g.,), quantum AFs (e.g.,) and others are out of the scope of this work. 1 We have chosen to categorize AFs into two main classes: fixed AFs (section 3) and adaptive activation functions (AAFs) (section 4), the latter having a parameter that is trained alongside the other weights in a network. Although instances exist where AFs are virtually identical, differing only in the presence of a particular adaptive parameter (e.g., swish (see section 4.4.1) and SiLU (see section 3.3)), this classification proves valuable. AAFs, by virtue of their parameterization, offer an added layer of flexibility in capturing complex relationships within the data during the training process.

## Literature review

There are several reviews of AFs available in the literature; however, most of them encompass only the most commonly known AFs. While this is sufficient for an overview for newcomers to the field, it does not allow for efficient research of AFs themselves. Probably the most extensive review is the from 2022, which lists over 70 AFs and provides a benchmark for 18 of them. Other reviews works containing list of AFs include.

While there are several existing works that offer benchmarks and empirical comparisons of various AFs, it is unfortunate that these studies are often constrained by a limited selection of AFs. Typically, the focus is centered on the most well-known and widely used functions, neglecting the broader spectrum of AFs available in the literature.

To avoid the manual selection of AFs, many researchers resort to various optimization approaches to find the optimal AF for their problems. e.g. an evolutionary approach was used to evolve the optimal activation function in and grid search using artificial data was used . Another search for the optimal activation functions was presented in where several simple activation functions were found to perform remarkably well. These automatic approaches might be used for evolving the activation functions (e.g., ) or for selecting the optimal activation function for a given neuron (e.g., ). While evolved activation function may perform well for a given problem, they also might be very complex - e.g., evolved activation functions . The complexity of an activation function is also important characteristic as it significantly influences the computational efficiency of a neural network; however, this might be mitigated by efficient implementations (including hardware implementations) of such activation functions (e.g., ). An empirical analysis of computational efficiency and power consumption of various AFs is available .

## Classical activation functions

First, our discussion delves into fixed activation functions, devoid of adaptive parameters. This category of activation functions represents the basic type that was predominantly employed in the initial neural network architectures and continues to be prevalent today. Fixed activation functions, such as the logistic sigmoid and hyperbolic tangent, are characterized by their predetermined mathematical formulations, where the activation output solely depends on the input without the introduction of any trainable parameters.

1 While these kinds of neural networks (NNs) are not discussed throughout this work, some of these approaches will use AFs presented in this work.

## Binary activation function

The binary activation function (binary AF) - also called a step function - is a simple yet important activation function used in neural networks. It assigns an output value of 1 if the input is positive or zero and an output value of 0 if the input is negative. Mathematically, it can be defined as follows: Similar to binary activation function is the sign function, which produces an output value of -1 if the input is negative and 1 if it is positive (and 0 for outputs that are exactly zero). Since the sign and the binary activation functions have nearly exact properties from the point of view of neural networks, only the binary activation function is mentioned, but the points hold similarly for the sign activation function.

The main advantage of the binary activation function is that it is straightforward and computationally efficient to implement. It does not involve complex mathematical operations, making it suitable for networks with low computational resources or for hardware implementations. However, the binary activation function has one glaring disadvantage - the lack of differentiability. The binary activation function is not differentiable at the point of discontinuity (x = 0) and is zero elsewhere. This poses challenges for optimization algorithms that rely on gradients, such as backpropagation (BP), since the gradient is noninformative. Since the gradient-based methods are used predominantly, the binary activation function is used very rarely and is important mainly for historical reasons as it was used in the original perceptron.

## Sigmoid family of activation functions

Various smoothed variants of the binary activation functions (sigmoids) are commonly used; the most common is the logistic function - the standard logistic sigmoid function was dominant in the field prior the introduction of rectified linear unit (ReLU) (see section 3.6), the logistic function is often called just sigmoid in the literature which is also used throughout this work for brevity (unless specified otherwise, sigmoid is equivalent to standard logistic function in the text). Standard logistic function is defined as The logistic sigmoid was a popular choice since its output values can interpreted as the probability that a binary variable is 1 since it squashes the input to the interval. The problem of sigmoid activation functions is that they saturate - they saturate when their input z is either a large positive number or a large negative number, which makes gradient-based learning difficult; therefore their use in feedforward networks is usually discouraged. Another option, albeit significantly less popular in artificial neural networks (ANNs), is the probit AF, which is just the cumulative standard normal distribution function used as an AF.

Another popular sigmod function is the hyperbolic tangent (tanh) activation function which is just scaled and shifted logistic sigmoid Similarly as the logistic sigmoid, the tanh also squashes the inputs; however, it squashes them to the interval (-1, 1). The tanh function is often advantageous over the logistic sigmoid function because it is centered around zero and it is similar to the identity function near zero, which makes training of a network easier if the activations are kept small. Nevertheless, the tanh function saturates similarly as does the logistic sigmoid and therefore similarly suffers from the vanishing gradients. Computationally efficient approximation of the tanh activation functions based on splines were proposed in tanh36 based on approximation relying on 36 equidistant points and tanh3 using only 3 points. Scaled variant tanh (z 2) was used. The linearized unit (LRTanh) is a tanh variant used together with modified BP that substitutes a different activation function derivative proposed. There are also approximations of the logistic sigmoid and tanh that are meant to speed up the computations; e.g., pRPPSG and other similar piecewise approximations.

A scaled version of the logistic sigmoid function was proposed in with the motivation to have the same linear regimes as the tanh and relu activation functions when initialized with the popular normalized initialized method proposed. The scaled version used fixed parameters A more complicated variant named n-sigmoid was proposed; however, it seems that the formula presented in the paper is not as the authors intended and, therefore, we omit this AF from the list.

## Shifted and scaled sigmoid (SSS)

The shifted and scaled sigmoid (SSS) was used; it is the logistic sigmoid with horizontal scaling and translation defined as where a and b are predetermined parameters; Arai and Imamura used a = 0. 02 and b = 600.

## Variant sigmoid function (VSF)

The variant sigmoid function (VSF) is an older parametric variant of the logistic sigmoid proposed. It is defined as where a, b, and c are predetermined parameters.

## Scaled hyperbolic tangent

A parametric version called scaled hyperbolic tangent (stanh) was used: where a and b are fixed hyperparameters that control the scaling of the function. Lecun et al. proposed using a = 1. 7159 and b = 2 3 A similar concept was analyzed in where sigmoids with bi-modal derivatives were used as activation functions. An example of such a function is where b is a hyperparameter; similarly, additional three activation functions with bi-modal derivates were proposed.

## Arctan

The arctangent (arctan) function and its variation were used as activation functions: The arctan resembles a logistic sigmoid activation, however, it covers wider range (-π 2, π 2). The arctan and several its variation were compared with the tanh, ReLU, leaky ReLU (LReLU), logistic sigmoid activation, and swish; the best-performing functions in the presented experiments were the arctan and its variation arctanGR. Interestingly, the arctan was used as an AF twenty years earlier. The arctanGR is a scaled version of the arctan and is defined as Other scaling variants such as division by the π, 1+ √ 5 2, or the Euler number are presented.

## Sigmoid-Algebraic activation function

The Sigmoid-Algebraic is a sigmoid variant defined . It is defined as

## Triple-state sigmoid

The triple-state sigmoid unit (TS-sigmoid) is a cascaded AF similar to TS-swish (see section 3.3.6); it is defined as where a and b are fixed parameters.

## Improved logistic sigmoid

The improved logistic sigmoid is yet another sigmoid based activation function designed to deal with the vanishing gradient problem where a and b are fixed parameters; a controls the slope and b is a thresholding parameter. The authors recommend a bound on the slope parameter a: Even though the parameters are fixed during the training of a network, a procedure for preseting them based on the network and data was proposed. The output range of the sigmoid-weighted linear unit (SiLU) is (-∞, ∞). The authors Qin, Wang, and Zou also showed that the improved logistic sigmoid AF has a higher convergence speed than the logistic sigmoid AF.

## Combination of the sigmoid and linear activation (SigLin)

A SigLin 2 was used as an AF. The SigLin is defined as where σ (z) is the logistic sigmoid AF and a is a fixed parameter; however, this AF was used only in a modified optimization procedure. Roodschild, Gotay Sardiñas, and Will experimented with a ∈ { 0, 0. 05, 0. 1, 0. 15 }.

## Penalized hyperbolic tangent

A penalized hyperbolic tangent (ptanh) the LReLU (see section 3.6) but uses the tanh function instead of the linear function: where a ∈ (1, ∞). This function has similar values near 0 as the LReLU with identical parameter a as they both share the same Taylor expansion up to the first order; however this function saturates to -1 a for z →-∞ and to 1 for z →∞. The ptanh AF was found to perform consistently well for various natural language processing (NLP) tasks compared to ReLU, LReLU and several other activation functions.

## Soft-root-sign (SRS)

A soft-root-sign (SRS) activation function is a parametric, smooth, non-monotonic, and bounded activation function. It is defined as where a and b are predetermined parameters; the authors Li and Zhou propose using a = 2 and b = 3 whereas the parameters are said to be learnable. The output range of SRS is [ab b -a e, a]. The performance of the SRS was demonstrated using hte CIFAR-10 and CIFAR-100 task in comparison with the ReLU (see section 3.6 for the description of the ReLU family of AFs), LReLU, parametric rectified linear unit (PReLU), softplus, exponential linear unit (ELU), scaled ELU (SELU), and swish.

2 This abbreviation is used only in this work; Roodschild, Gotay Sardiñas, and Will did not name the function .

## Soft clipping (SC)

The soft clipping (SC) AF is another bounded AF; it is approximatelly piecewise linear in the range z ∈ and it is defined as where a is a fixed parameter.

## Hexpo

The Hexpo activation function was proposed in order to minimize the problem of vanishing gradient; it resembles a tanh activation function with scaled gradients: where a, b, c, and d are fixed parameters. While the parameters could be trainable in theory, it is not recommended as it would lead to the vanishing gradient problem. The Hexpo functions allow for control over the gradient by tunning the parameters a, b, c, and d and the ratios a b and c d -with increasing the ratios a b or c d, the rate of gradient decay to zero decreases; increasing only a and c scales the gradient around the origin up.

## Softsign

A softsign activation function is a smooth activation function similar to the tanh activation; however, it is less prone to vanishing gradients. It is defined as where | z | denotes the absolute value of z.

## Smooth step

The smooth step is a sigmoid AF; it is defined as where a is a fixed hyperparameter.

## Elliott activation function

Elliott activation function is one of the earliest proposed activation functions to replace to replace the logistic sigmoid or tanh activation functions; the Elliott AF is a scaled and translated softsign AF. It is defined as The output of the Elliott activation functions is in range. The main advantage of the Elliott AF is that it can be calculated much faster than the logistic sigmoid.

## Sinc-Sigmoid

The Sinc-Sigmoid is a sigmoid-based AF proposed. It is defined as where sinc (x) is the unnormalized 3 sinc function.

3 Koçak and Üstünda˘ g ¸ Siray did not specify whether it is the normalized or unnormalized variant. Still, they provided the derivative of the Sinc-Sigmoid, which suggests that the unnormalized variant was used.

## Sigmoid-Gumbel activation function

The Sigmoid-Gumbel (SG) is a non-adaptive AF proposed recently ; it is defined as

## NewSigmoid

The NewSigmoid is a sigmoid variant proposed . It is defined as

## Root2sigmoid

The root2sigmoid is another sigmoid variant proposed . It is defined 4 as

## LogLog

The LogLog is a simple AF proposed; it is defined as The LogLog, cLogLog (see section 3.2.21) were used in NNs for forecasting financial time-series.

## Complementary Log-Log (cLogLog)

The complementary LogLog (cLogLog) is another simple AF proposed in complementing the LogLog (see section 3.2.20); it is defined as The variant called modified cLogLog (cLogLogm) was also proposed:

## SechSig

The SechSig is another AF utilizing the logistic sigmoid in its definition; it is defined as Közkurt et al. also proposed a parametric version which we will call parametric SechSig (pSechSig): where a is a fixed parameter.

## TanhSig

The TanhSig is an AF similar to SechSig; it is defined as Közkurt et al. also proposed a parametric version which we will call parametric TanhSig (pTanhSig): where a is a fixed parameter.

4 The author had probably a typo in the definition in the original paper; we present the formula we think Kumar and Sodhi intended to write - it resembles the NewSigmoid and fits the numerical values given in the paper.

## Multistate activation function (MSAF)

The multistate activation function (MSAF) is a logistic sigmoid based AF proposed. The general MSAF is defined as where a and b k, k = 1,..., N are fixed parameters; a ∈ R, N ∈ N +, b k ∈ R +, and b 1 < b 2 <... < b N. If a = 0, it is named as N -order 5 MSAF.

There is also a special case called symmetrical MSAF (SymMSAF) defined as where a is required to be significantly smaller than 0

## Rootsig and others

The rootsig is one of the activations listed. It is defined as where a is a parameter. This function is called rootsig in where the authors list a variant with a = 1.

There are also several other unnamed sigmoids :

## Sigmoid and tanh combinations

Guevraa et al. proposed several activations mostly combining the logistic sigmoid, tanh, and linear function. The general approach is where g (z) and h (z) are two different AFs. The authors used the following pairs { g (z), h (z) }: { σ 2 (z), tanh(z) }, { σ 2 (z), tanh(z) }, { σ 2 (z), 0 }, { tanh(z), 0 }, { σ 2 (z), az }, and { tanh(z), az }, where a > 0 is a fixed parameter and Guevraa et al. also proposed an AF we termed SigLU (see section 3.6.52) and nonadaptive variant of PTELU.

## Class of sigmoid-weighted linear units

The SiLU is the most common example of a larger class of sigmoidal units defined as where s (z) is any sigmoidal function; it becomes the SiLU if the logistic sigmoid function is used. The SiLU is thus defined as 5 This does not exactly fit into the exemplar MSAF of order two presented; it is possible that authors intended another constraint b 1 = 0 for such case. where σ (z) is the logistic sigmoid. The SiLU has the output range of (-0. 5, ∞) and was first used for reinforcement learning tasks such as SZ-Tetris and Tetris. The SiLU was also found to work well for the CIFAR-10/100 and ImageNet tasks. The adaptive variant of the SiLU is called swish (see section 4.4.1).

For the purposes of this work, we also consider any squashing functions s ( z ) and not necessarily only sigmoids - for example, we classify rectified hyperbolic secant (see section 3.3.27) as a member of this class. We also list functions that are closely based on the SiLU and its variants.

A similar approach named weighted sigmoid gate unit (WiG) was proposed, where the AF was used only for gating each of the raw inputs: where x denotes the vector of raw inputs, w i the weights of neuron i and b i its bias

## Gaussian error linear unit (GELU)

Gaussian error linear unit (GELU) is an activation function based on the standard Gaussian cumulative distribution function, and it weights inputs by their value rather than gating them as ReLUs do. It is defined as where Φ(z) is the standard Gaussian cumulative distribution function (CDF) and erf (x) is the Gauss error function. It is similar to the SiLU but it uses Φ(z) instead of the σ (z). However, due to the complicated formula, the GELU can be approximated as if the performance gains are worth the loss of exactness. The function is similar to SiLU (see section 3.3), it only uses Gaussian CDF Φ(z) instead of the logistic distribution CDF σ (z). GELU was found to outperform many competitors (e.g., ReLU, ELU, SELU, continuously differentiable exponential linear unit (CELU), sigmoid, tanh). Hendrycks and Gimpel also proposed to parameterize the GELU by µ and σ 2 -the parameters defining mean and variance of the Gaussian distribution whose CDF is used in the GELU, however, only the standard Gaussian distribution was used in experiments. Replacing ReLUs with GELUs led to better performance. More details about GELU are available.

## Symmetrical Gaussian error linear unit (SGELU)

A symmetric variant of GELU called symmetrical Gaussian error linear unit (SGELU) was proposed. It is defined as where a is a fixed hyperparameter. The symmetrical nature of the SGELU also leads to more symmetrically distributed weights of the neural network compared to SGELU; it is believed that normal distribution of the weights can make the network more rational, accurate, and robust.

## Cauchy linear unit (CaLU)

Another function related to the GELU and SiLU is the Cauchy linear unit (CaLU) which uses the CDF of the standard Cauchy distribution instead of the Gaussian CDF in GELU and logistic sigmoid in SiLU. It is defined as where Φ Cauchy (z) is the CDF of the standard Cauchy distribution.

## Laplace linear unit (LaLU)

Another function related to the GELU and SiLU is the Laplace linear unit (LaLU) which uses the CDF of the Laplace distribution; it is defined as where Φ Laplace (z) is the CDF of the Laplace distribution.

## Collapsing linear unit (LaLU)

The Collapsing linear unit (CoLU) is an AF similar to the SiLU proposed . It is defined as

## Triple-state swish

The triple-state swish unit (TS-swish) 6 is a cascaded AF similar to TS-sigmoid (see section 3.2.6); it is defined as where a and b are fixed parameters.

## Generalized swish

A SiLU variant called generalized swish 7 was proposed . It is defined as

## Exponential swish

Another SiLU variant called exponential swish 8 was proposed . It is defined as

## Derivative of sigmoid function

The derivative of logistic sigmoid was used as an AF . Koçak and Üstünda˘ g ¸ Siray formulate the AF using the following form

## Gish

Gish is another SiLU variant; the gish is defined as Kaytan, Aydilek, and Yero˘ glu found that gish outperformed logistic sigmoid, softplus, ReLU, LReLU, ELU, swish, mish, logish, and smish on the MNIST and CIFAR-10 datasets.

## Logish

Logish is yet another SiLU variant; it is defined as 6 Koçak and Üstünda˘ g ¸ Siray called the function swish but it is actually based on the SiLU.

7 Also based on the SiLU instead of its adaptive variant swish.

8 Again, based on the SiLU instead of its adaptive variant swish.

## LogLogish

LogLogish is a SiLU variant based on the LogLog (see section 3.2.20); it is defined as

## ExpExpish

ExpExpish is a SiLU variant; it is defined as

## Self arctan

The self arctan is an AF proposed in whose formula resembles the SiLU. The self arctan is defined as where tan -1 (z) is the arctangent function.

## Parametric logish

Zhu et al. also proposed a parametric variant of logish - we will call it parametric logish (pLogish) in this work. It is defined as where a and b are fixed parameters; Zhu et al. used a = 1 and b = 10.

## Phish

Phish is a SiLU variant combining GELU and tanh; it is defined as The phish was found to outperform GELU, tanh, logistic sigmoid, and ReLU; it performed similarly as the mish and swish in the experiments.

## Suish

The suish was proposed as an alternative to the swish AF . It is defined as

## Tangent-sigmoid ReLU (TSReLU)

The tangent-sigmoid ReLU (TSReLU) is an AF very similar to phish, mish, and TanhExp - it just uses the logistic sigmoid instead of the GELU in phish, softplus in mish, and the exponential in TanhExp. It is defined as

## Tangent-bipolar-sigmoid ReLU (TBSReLU)

The tangent-bipolar-sigmoid ReLU (TBSReLU) is a variant of TSReLU proposed . It is defined as

## Log-sigmoid

A logarithm of the logistic sigmoid is sometimes used as an activation function. It is defined as

## Derivative of sigmoid-weighted linear unit (dSiLU)

The derivative of sigmoid-weighted linear unit (dSiLU) can also be used as an activation function resembling a sigmoid. It is defined as where σ (z) is the logistic sigmoid. The dSiLU has a maximum value of around 1.1, and the minimum is approximately -0.1.

## Double sigmoid-weighted linear unit (DoubleSiLU)

The double sigmoid-weighted linear unit (DoubleSiLU) 9 is an AF proposed. It is defined as where σ (z) is the logistic sigmoid.

## Modified sigmoid-weighted linear unit (MSiLU)

A modified sigmoid-weighted linear unit (MSiLU) is a variant of the SiLU that has faster convergence than the SiLU. It is defined as where σ (z) is the logistic sigmoid.

## Hyperbolic tangent sigmoid-weighted linear unit (TSiLU)

Another SiLU variant is the hyperbolic tangent sigmoid-weighted linear unit (TSiLU), which combines the tanh and SiLU. It is defined 10 as

## Arctan sigmoid-weighted linear unit (ASiLU)

Arctan sigmoid-weighted linear unit (ATSiLU) is yet another SiLU variant proposed ; it is defined as

## SwAT

Verma, Chug, and Singh proposed an AF named SwAT combining the SiLU and arctan . This function is defined as

## Rectified hyperbolic secant

Arectified hyperbolic secant activation function was proposed. This function is totally differentiable, symmetric about the origin, and is approaching zero for inputs going to positive or negative infinity: where sech(z) is the hyperbolic secant function.

9 Verma, Chug, and Singh termed the unit as DSiLU but that would collide with the dSiLU (see section 3.3.21) proposed earlier by Elfwing, Uchibe, and Doya.

10 The formula in was wrong as it evaluated to 2 x 0, we present the formula we think authors intented.

## Linearly scaled hyperbolic tangent (LiSHT)

A linearly scaled hyperbolic tangent (LiSHT) activation function was proposed in to address the problem of vanishing gradients and the non-utilization of large negative input values. The LiSHT function is defined as The output range of LiSHT function is [0, ∞].The output of LiSHT is close to the ReLU (see section 3.6) and swish for large positive values; however, unlike the aforementioned AFs, the output is symmetric, and, therefore, it behaves identically for large negative values. While the LiSHT is symmetric, the fact that its output is unbounded and non-negative could be considered a disadvantage. The effectiveness of the LiSHT activation function was tested on several different architectures ranging from multilayer perceptron (MLP) and residual neural networks to LSTM-based networks and on various tasks - the Iris dataset, the MNIST, CIFAR-10 and CIFAR-100 and the sentiment140 dataset from Twitter for sentiment analysis.

A parametric version of LiSHT named SoftModulusT (see section 3.6.31) was proposed .

## Mish

A popular activation function mish is a combination of the tanh and softplus activation function; the function resembles swish activation (see section 4.4.1). It is defined as Mish was found to outperform swish; it performed similarly to f (z) = z · ln (1 + tanh (exp (z))) but this activation function was found to often lead to unstable training. The mish was found to outperform swish and ReLU for many architectures such as various ResNet architectures, Inception v3, DenseNet-121, and others. Detailed comparison with other activation functions was run using the Squeeze Net where it outperformed swish, GELU, ReLU, ELU, LReLU, SELU, softplus, S-shaped ReLU (SReLU), inverse square root unit (ISRU), tanh, and randomized leaky ReLU (RReLU). The mish activation function was, for example, used in the YOLOv4 and its variant Scaled-YOLOv4.

## Smish

The smish is a variant of the mish where the exponential function is replaced by the logistic sigmoid. It is, therefore, defined as where a and b are parameters; however, Wang, Ren, and Wang recommend a = 1 and b = 1 based on a small parameter search.

## TanhExp

Similarly as the mish is the combination of tanh and softplus, the TanhExp is a combination of tanh and the exponential function. It is defined as

## Serf

The serf is an AF similar to the mish; however, it uses the error function instead of the tanh. It is defined as where erf is the Gauss error function. It was found to outperform mish, GELU, and ReLU for various architectures on Multi30K, ImageNet, the CIFAR-10, and CIFAR-100 datasets; see for details.

## Efficient asymmetric nonlinear activation function (EANAF)

An activation function combining tanh and softplus called efficient asymmetric nonlinear activation function (EANAF) was proposed. The function is defined as where h(z) is the softplus function and g(z) = tanh (z 2), which can be simplified to The EANAF is continuously differentiable. The EANAF is very similar to swish with similar amount of computation but Chai et al. found that it performs better than swish and several other activation functions in RetinaNet and YOLOv4 architectures on object detection tasks.

## SinSig

SinSig is a self-gated non-monotonic activation function defined as where σ (z) is the logistic sigmoid function. While SinSig is similar to swish and mish, it outperformed them in experiments in as the number of layers in a neural network increased. It was also shown that the SinSig converges faster. The SinSig outperformed ReLU and mish on several deep architectures including ResNet 20 v2, ResNet 110 v2, SqueezeNet, and ShuffleNet among others on the CIFAR-100 task in experiments.

## Gaussian error linear unit with sigmoid activation function (SiELU)

The with sigmoid activation function (SiELU) was proposed ; it is defined as

## Gated linear unit (GLU)

A gated activation called gated linear unit (GLU) similar to SiLU (see section 3.3) for use in recurrent neural networks (RNNs) was proposed. The GLU is defined as where ⊗ is the element-wise product and z and z ′ are two learned linear transformations of input vector x.

## Gated tanh unit (GTU)

A gated activation called gated tanh unit (GTU) similar to GLU (see section 3.4) for use in RNNs was proposed. The GTU is defined as where ⊗ is the element-wise product and z and z ′ are two learned linear transformations of input vector x.

## Gated ReLU (ReGLU)

Another GLU extension is the gated (ReGLU). The ReGLU is defined as where ⊗ is the element-wise product and z and z ′ are two learned linear transformations of input vector x.

## Gated GELU (GEGLU)

A GELU-based GLU extension is the gated (GEGLU); it is defined as where ⊗ is the element-wise product and z and z ′ are two learned linear transformations of input vector x.

## Swish GELU (SwiGLU)

A swish-based GLU extension is the gated swish (SwiGLU); it is defined as where ⊗ is the element-wise product, z and z ′ are two learned linear transformations of input vector x, and swish is the swish with its own trainable parameter.

## Softmax

The softmax is not a usual type of AF taking in a single value, but it takes all the output value of the unit i and, also, the output values of other units in order to compute a soft argmax of the values. It is defined as where f (z j) is the output of a neuron j in a softmax layer consisting of N neurons.

## β -softmax

The β -softmax is a softmax extension proposed; it is defined as where f (z j) is the output of a neuron j in a softmax layer consisting of N neurons and b takes random value from N + 11.

## Rectified linear function (ReLU)

The rectified linear unit (ReLU) is widely regarded as the most popular activation function in modern feedforward networks due to its simplicity and improved performance. It has been observed that ReLUs can significantly expedite the convergence of stochastic gradient descent. Additionally, traditional ReLUs are computationally less expensive compared to activation functions like the logistic or tanh functions. ReLUs often outperform sigmoidal activation functions. However, a drawback of ReLUs is the potential for neurons to become "dead" or "disabled" during training. This means that they may never activate again for any input, resulting in a permanently zero output gradient. This issue can occur after a weight update when a large gradient flows through the unit. This might happen after a weight update after a large gradient flows through the unit. However, ReLUs often lead to faster convergence than for sigmoid activation, as shown . It can also be shown that ReLUs and rational function efficiently approximate each other. The ReLU was used as an example of the more general class of piecewise affine AFs for neural network verification 12 using theorem provers .

A ReLU is mathematically defined as the maximum of zero and the input value: ReLU is commonly recommended as the default choice for feedforward networks due to its usually superior performance compared to sigmoidal functions and its computational efficiency; furthermore, it works comparably to its modifications. Many popular NN models utilize ReLU as the activation function of choice, e.g.,.

Many ReLU modification and derivations were proposed - e.g. leaky ReLU (LReLU), very leaky ReLU (VLReLU), parametric ReLU, randomized leaky ReLU (RReLU) or S-shaped ReLU. Smoothed modifications are, for example, exponential linear unit and softplus. Most of the modifications solve the problem of dying out neurons as they allow for gradient flows for any input.

## Shifted ReLU

A Shifted ReLU is a simple translation of a ReLU and is defined as 11 No further specification was provided.

12 More details are out of the scope of this work, see for more details.

## Leaky ReLU (LReLU)

Leaky ReLU (LReLU) is defined as where a ∈ (1, ∞) is set to large number; 13 the recommended setting from is a = 100.

LReLU solves the problem of dying neurons when neurons have permanently zero output gradient in classical ReLU by "leaking" the information for z < 0 instead of outputting exact zero. Both ReLU and LReLU can be considered to be a special case of the maxout unit (see section 4.47). A theoretical analysis of the ReLU and LReLU is available .

Very leaky ReLU (VLReLU) is almost identical to the LReLU but has much higher slope when the z is negative for faster training by setting a i = 3. While it can be considered as a special case of LReLU, some researchers consider it as a separate case, e.g.,.

The so-called optimized leaky ReLU (OLReLU) propose another reformulation of LReLU and calculation of the slope parameter a that is inspired by the RReLU (see section 3.6.3): where u and l are hyperparameters of the bounds of the RReLU.

## Randomized leaky ReLU (RReLU)

RReLU is a leaky ReLU where the leakiness is stochastic during the training, i.e.: where a i is a sampled for each epoch and neuron i from the uniform distribution: a i ∼ U (l, u) where l < u and l, u ∈ (0, ∞). Similarly as in the dropout approach, an average over all a i over is taken during inference phase - the a i is set to l + u 2: Recommended distribution is U for sampling the a i.

## Softsign randomized leaky ReLU (S-RReLU)

The softsign randomized leaky ReLU (S-RReLU) 14 is a RReLU combined with the softsign proposed. It is defined as where a i is a sampled for each epoch and neuron i from the uniform distribution: a i ∼ U (l, u) where l < u and l, u ∈ (0, ∞). Elakkiya and Dejey used l = 1 8 and u = 1 3.

13 Depending on the source, researchers use either this form z a or the inverted form az for the negative inputs.

14 Elakkiya and Dejey used S-RReLU as a name and not an abbreviation; however, since S-RReLU is a combination of the softsign and RReLU, we feel that using it as an abbreviation is appropriate.

## Sloped ReLU (SlReLU)

A Sloped ReLU (SlReLU) is similar to the LReLU - whereas the LReLU parameterizes the slope for negative inputs, the SlReLU parameterizes the slope of ReLU for positive inputs. It is, therefore, defined as where a is a fixed, predetermined parameter. Seo, Lee, and Kim recommended a ∈ based on their experiments.

## Noisy ReLU (NReLU)

A stochastic variant of the ReLU called noisy ReLU (NReLU) was proposed: where a is a stochastic parameter a ∼ N(0, σ (z)), N (0, σ 2) is the Gaussian distribution with zero mean and variance σ 2 and σ (z) is the standard deviation of the inputs z. The NReLU was designed for use with Restricted Boltzmann machines. More details about the NReLU is available.

## SineReLU

The SineReLU is a ReLU based activation that uses trigonometric functions for negative inputs. It is defined as where a is a fixed parameter.

## Minsin

The minsin is a ReLU-based AF used . It is defined as

## Variational linear unit (VLU)

The variational linear unit (VLU) is an AF combining the ReLU and sine functions proposed. It is defined as where a and b are fixed parameters.

## Spatial context-aware activation (SCAA)

The spatial context-aware activation (SCAA) is a ReLU extension proposed. The ReLU performs an elementwise max operation on the feature map X: where ReLU(X) is the ReLU in the matrix notation and 0 is a matrix of zeroes with the same shape as X. The SCAA first applies a depth-wise convolution on X to produce spatial context aggregated feature map denoted f DW (X) and then proceeds with the elementwise max operation; the SCAA is, therefore, defined as

## Randomly translational ReLU (RT-ReLU)

A randomly translational ReLU (RT-ReLU) is a ReLU with a randomly added jitter during each iteration of the training process. It is defined as where a i is stochastic parameter for each neuron i randomly sampled from the Gaussian distribution at each iteration, a i ∼ N (0, σ 2), where σ 2 is the variance of the Gaussian distribution. The authors Cao et al. set the σ 2 = 0. 75 2 for their experiments. The a i is set to 0 during the test phase.

## Natural-Logarithm-ReLU (NLReLU)

The natural-logarithm-ReLU (NLReLU) introduces non-linearity to ReLU similarly as rectified linear tanh (ReLTanh) (see section 4.2.36) but only for positive part of the activation function: where a is a predefined constant.

## Softplus linear unit (SLU)

An activation function softplus linear unit (SLU) combining the ReLU with the softplus activation function was proposed; the function is based around the assumption that zero mean activations improve learning performance. The SLU is defined as where a i, b i, and c i are predefined parameters; however, to ensure that the function is continuous, differentiable at zero and to avoid vanishing or exploding gradients, its parameters are set to a = 1, b = 2, and c = 2ln. The SLU is therefore equal to

## Rectified softplus (ReSP)

Another activation function combining ReLU and softplus called rectified softplus (ReSP) was proposed. The function is defined as where a is a fixed hyperparameter controlling the slope. Larger values of a between 1.4 and 2.0 were found to work well.

## Parametric rectified non-linear unit (PReNU)

A ReLU variant called parametric rectified non-linear unit (PReNU) replaces the linear part of the ReLU for positive inputs by a non-linear function similarly to RePU (see section 3.6.39). It is defined as where a is a fixed hyperparameter - however, this parameter could be adaptive similarly as in PReLU (see section 4.2.1) that PReNU extends since Jaafari, Ellahyani, and Charfi thought of the PReLU as non-adaptive function for some reason.

## Bounded ReLU (BReLU)

A BReLU is a variant of ReLU that limits the output as the unlimited output of the original ReLU might lead to an instability. It is defined as where a is a predefined parameter. The BReLU appeared later in the literature under the name ReLUN, where it seems that it was independently proposed.

## Hard sigmoid

A Hard sigmoid is very similar to BReLU; it is a very crude approximation of the logistic sigmoid and is commonly defined as Other definitions are sometimes used; e.g. variant from is defined as While the Hard sigmoid is not as commonly used as the logistic sigmoid, it can be used, for example, in binarized neural network with stochastic activation functions - the binaryized neural networks can lead to much faster inference than regular neural networks, e.g., Courbariaux et al. reached up to 7 × speed up without any loss in classification accuracy (however, even better speed-ups can be obtained using, for example, field-programmable gate array (FPGA) implementations as in).

## HardTanh

The HardTanh is another piecewise linear function; it is very similar to Hard sigmoid, but it approximates the tanh instead of the logistic sigmoid. It is defined as where a and b are fixed parameters; Liu et al. used a = -1 and b = 11. NNs with HardTanhs are more suitable for linear predictive control than NNs with ReLUs as they usually require less hidden layers and neurons for representing identical min-max maps.

## Shifted HardTanh

Kim et al. proposed HardTanh variants with vertical and horizontal shifts. The SvHardTanh 15 is defined as where a is a fixed parameter. Kim et al. used HardTanh variant with thresholds -1 and 1; a more general variant with parametric thresholds from eq. could be defined similarly.

The SvHardTanh is defined as where a is a fixed parameter.

The ShHardTanh is defined as where a is a fixed parameter.

Kim et al. used HardTanh variant with thresholds -1 and 1; more general variants of SvHardTanh and ShHardTanh with parametric thresholds from eq. could be defined similarly.

## Hard swish

A linearized variant of the swish AF (see section 4.4.1) was proposed. It is defined as The linearization allows for more efficient computation.

15 Both SvHardTanh and ShHardTanh are named using the same convention as shifted ELUs (see section 4.2.56) for the purposes of this work.

## Truncated rectified (TRec) activation function

The truncated rectified (TRec) AF is a truncated variant of the ReLU. It resembles onesided variant of the Hardshrink (see section 3.6.22) - it is defined as where a is a fixed parameter. Konda, Memisevic, and Krueger used a = 1 for most of their experiments.

## Hardshrink

The Hardshrink (named thresholded linear AF in 16) is very similar to Hard sigmoid, TRec, and other piecewise linear functions; it is defined as where a > 0 is a fixed parameter.

## Softshrink

The Softshrink is an AF similar to the Hardshrink used. It is defined as where a > 0 is a fixed thresholding parameter.

## Bounded leaky ReLU (BLReLU)

Similarly as the BReLU is a bounded variant of the ReLU, the bounded leaky ReLU (BLReLU) is a bounded variant of LReLU (see section 3.6.2). It is defined as where a and b are predefined parameters and c is computed such that b = ab + c, i.e. c = (1 -a) b. The parameter a controls the leakiness, the parameter b is the threshold of saturation, and c is computed such that the function is continuous.

## V-shaped ReLU (vReLU)

A V-shaped variant of ReLU called V-shaped ReLU (vReLU) is proposed in and tackles the problem of dying neurons that is present with ReLUs. The vReLU is identical to the absolute value function and is defined as The output range of vReLU is [0, ∞). The modulus activation function later proposed in the literature by Vallés-Pérez et al. in is identical to the vReLU. The absolute value function was used as an AF also.

## Pan function

The pan function is an AF similar to the vReLU and Softshrink. It is defined as where a is a fixed boundary parameter.

16 Konda, Memisevic, and Krueger proposed it as a novel AF but it was already proposed .

## Absolute linear unit (AbsLU)

The absolute linear unit (AbsLU) is a ReLU-based AF similar to the vReLU. It is defined as where a ∈ is a fixed hyperparameter.

## Mirrorer rectified linear unit (mReLU)

The mirrored rectified linear unit (mReLU) is a bounded AF that suppresses the output for unusual inputs. It is defined as

## Leaky single-peaked triangle linear unit (LSPTLU)

An AF similar to vReLU, AbsLU, and tent activation named leaky single-peaked triangle linear unit (LSPTLU) was proposed. It is defined as where a is a fixed parameter. An identical AF was proposed under the name leaky rectified triangle linear unit (LRTLU).

## SoftModulusQ

The SoftModulusQ is a quadratic approximation of the vReLU proposed . The SoftModulusQ is defined as

## SoftModulusT

While the SoftModulusQ (see section 3.6.30) is a quadratic approximation of the vReLU (see section 3.6.25), the SoftModulusT is a tanh based approximation of the vReLU. It is basically a parametric version of the LiSHT activation function (see section 3.3.28): where a is a predetermined parameter; the authors Vallés-Pérez et al. used a = 0. 01 in their experiments. When a = 1, the SoftModulusT becames the LiSHT activation function.

## SignReLU

The combination of ReLU and softsign resulted in SignReLU that improves the convergence rate and alleviates the vanishing gradient problem. The SignReLU is defined as where a is a fixed parameter; the SignReLU becomes ReLU for a = 0. The SignReLU was independently proposed under the name DLU; 17 this name is sometimes used in the literature - e.g.,.

## Li-ReLU

Elakkiya and Dejey proposed a combination of a linear function and the ReLU; they named the function Li-ReLU 18 and it is defined as where a i is a fixed parameter.

## Concatenated ReLU (CReLU)

A concatenated ReLU (CReLU) is an adaptation of the ReLU function proposed based on the observation that filters in convolutional neural networks (CNNs) in the lower layers form pairs consisting of filters with opposite phase. The CReLU conserves both negative and positive linear responses after convolution by concatenating the output of two ReLUs (hence the name). The CReLU is a function R → R 2 and is defined as with the output range of [0, ∞) for both output elements.

## Negative CReLU (NCReLU)

A CReLU extension named negative CReLU (NCReLU) was proposed; while it is very similar to CReLU, it multiplies the second element by -1: Very similar AF was proposed concurrently in under the name bipolar activation function (BAF). Unlike the NCReLU, it does not produce a vector output but is applied in an alternating manner similar to All-ReLU (see section 4.34) but for neurons instead of layers. It is defined for the i -th neuron as where g (z i) is any ReLU family AF and % is the modulo operation.

## DualReLU

Where CReLU activation functions takes a single value and outputs a vector of two values, the DualReLU takes two values as an input and outputs a single value. The DualReLU is a two-dimensional activation function meant as a replacement of the tanh activation function for Quasi-Recurrent neural networks. It is defined as

## Orthogonal permutation liner unit

The orthogonal permutation liner unit (OPLU) is not applied to a single neuron but always to a pair of neurons. First, the neurons are grouped into pairs of neurons { i, j } and the OPLU takes two inputs z i and z j of neurons i and j and produces the output for neuron i and

## Elastic ReLU (EReLU)

Another extension is the elastic ReLU (EReLU), which slightly randomly changes the slope of the positive part of the ReLU during the training. The EReLU is defined as where k i is a sampled for each epoch and neuron i from the uniform distribution: a i ∼ U (1 -α, 1+ α) where α ∈ is a parameter controlling the degree of response fluctuations. The EReLU thus complements the principle of RReLU, which randomly changes the leakiness during the training while keeping the positive part fixed, while the EReLU changes the positive part and keeps the output constantly zero for negative inputs. The EReLU sets the k i its expected value E(k i) which is equal to one - the EReLU becomes the ReLU during the test phase.

## Power activation functions & rectified power units (RePU)

A power activation function extending ReLU together with a training scheme for better generalization was proposed. This activation function was later independently proposed under the name RePU. The RePU is defined as where a is a fixed parameter. The RePU is a generalization of several activation functions - it becomes the Heaviside step function for a = 0 and ReLU for a = 1; the case a = 2 is called rectified quadratic unit (ReQU) in and squared ReLU; finally, the case a = 3 is called rectified cubic unit (ReCU). The disadvantage of RePU is its unbounded and asymmetric nature and that it is prone to vanishing gradient. Theoretical analysis of the RePU is available.

However, Berradi recommends alternating using a = b and a = 1 b each epoch; i.e.: Then the activation function f 1 (z) is used during odd epochs and f 2 (z) during even epochs; their mean is used during the test phase. The value b > 1 was used in the experiments in b ∈ { 1. 05, 1. 1, 1. 15, 1. 20, 1. 25 }.

## Approximate ReLU (AppReLU)

The approximate ReLU (AppReLU) 19 is the RePU with aditional scaling parameter; it is defined as

## Power linear activation function (PLAF)

The power linear activation function (PLAF) 20 is a class of two similar AFs proposed. The first, even power linear activation function (EPLAF), is defined as 19 Saha et al. used the abbreviation AReLU but this is already used for the Attention-based ReLU in this work.

20 Originally, Nasiri and Ghiasi-Shirazi named PLAF as PowerLinear AF. Also, its variants EPLAF and OPLAF were named as EvenPowLin and OddPowLin. and where d is a fixed parameter. Similarly, the second AF - odd power linear activation function (OPLAF) - is defined as where d is a fixed parameter. Nasiri and Ghiasi-Shirazi focused on the EPLAF in their work and showed that EPLAF with d = 2 performed similarly as the ReLU for some of the tasks but it performed significantly better for other tasks; the OPLAF was not experimentally validated.

## Average biased ReLU (ABReLU)

Similarly as the RT-ReLU (see section 3.6.11), the average biased ReLU (ABReLU) uses horizontal shifting in order to handle negative values. It is defined as where a i is the average of input activation map to the neuron/filter i, which makes the function data dependent and adjusts the threshold based on the positive and negative data dominance. The output range is [0, ∞).

## Delay ReLU (DRLU)

The delay ReLU (DRLU) 21 is a function that also adds a horizontal shift to the ReLU; however, the DRLU uses a fixed, predetermined shift whereas RT-ReLU uses stochastic shifts (see section 3.6.11) and ABReLU computes the shift as the average of input activation map (see section 3.6.42). The DRLU is defined as where a is a fixed, predetermined parameter. Shan, Li, and Chen also add a constraint a > 0 and they used a ∈ { 0. 06, 0. 08, 0. 10 } in their experiments.

## Displaced ReLU (DisReLU)

Very similar to the flexible ReLU (FReLU) (see section 4.2.15) and dynamic ReLU (DReLU) (see section 4.2.14) is the displaced ReLU (DisReLU) 22 as it also shifts the ReLU: where a is a predefined hyperparameter. A Shifted ReLU (see section 3.6.1) is a special case of DisReLU with a = 1. The VGG-19 with DisReLUs outperform the ReLU, LReLU, PReLU, and ELU activation functions with a statistically significant difference in performance on the CIFAR-10 and CIFAR-100 datasets as shown.

## Modified LReLU

Inspired by the DisReLU, Yang et al. proposed the modified LReLU (MLReLU). The MLReLU is a translated LReLU and is defined as where a is a fixed parameter controlling both the slope and the threshold.

21 Authors termed the function DRLU; however, the usual notation in this work would be DReLU. Since such notation would collide with the dynamic ReLU, we will use the original notation from despite the inconsistency.

22 Macêdo et al. originally abbreviated the displaced ReLU as DReLU but that is already taken by dynamic ReLU from section 4.2.14.

## Flatted-T swish

An activation function flatted-T swish (FTS) combines ReLU and the logistic sigmoid activation function; it is defined as where T is a predefined hyperparameter, the recommended value is T = -0. 20. The FTS is identical to a shifted swish for the positive z. The FTS was shown to outperform ReLU, LReLU, swish, ELU, and FReLU activation functions. The special case with T = 0 was proposed independently under the name of ReLU-Swish.

## Optimal activation function (OAF)

The so-called Optimal Activation Functio (OAF) is a combination of ReLU and swish activations proposed . It is defined as

## Exponential linear unit (ELU)

An ELU is an extension of LReLU where the function employs an exponential function for the negative inputs, which speeds up the learning process: where a is a hyperparameter; the authors Clevert, Unterthiner, and Hochreiter used a = 1 in their work. The a determines the value to which an ELU saturates for inputs going to negative infinity.

## Rectified exponential unit (REU)

A rectified exponential unit (REU) is an activation function inspired by the ELU and swish (see sections 3.6.48 and 4.4.1) and is based on the assumption that the success of the swish activation functions is due to the non-monotonic property in the negative quadrant. The REU is defined as A parametric version called parametric rectified exponential unit (PREU) was also proposed; see section 4.2.9 for details.

## Apical dendrite activation (ADA)

A biologically inspired AF named apical dendrite activation (ADA) was proposed. It is similar to the ELU, but it applies an exponential function for positive inputs. It is defined as where a and b are fixed parameters.

## Leaky apical dendrite activation (LADA)

As LReLU extends the ReLU, the leaky apical dendrite activation (LADA) extends the ADA. where a, b, and c ∈ are fixed parameters. Georgescu et al. used c = 0. 01 in their experiments.

## Sigmoid linear unit (SigLU)

The sigmoid linear unit (SigLU) 23 is an ELU alternative that uses a modified logistic sigmoid instead of the exponential. It is defined as

## Swish and ReLU activation (SaRa)

The swish and ReLU activation (SaRa) is an AF combining the swish and ReLU AFs proposed. It is defined 24 as where a and b are fixed parameters; Qureshi and Sarosh Umar recommend a = 0. 5 and b = 0. 7.

## Maxsig

The maxsig is one of the AFs listed. The maxsig is similar to the SigLU (see section 3.6.52) and is defined as where σ (z) is the logistic sigmoid.

## Tanh linear unit (ThLU)

The tanh linear unit (ThLU) 25 is an AF combining tanh and ReLU. It is defined as The ThLU is a special case of the tanh based ReLU (TReLU) with b i = 1 2. Similar AF was used under the name maxtanh in - it just omitted the scaling factor. The maxtanh can also be written as f (z) = max(z, tanh (z)).

## DualELU

The DualELU is equivalent of DualReLU (see section 3.6.36) for ELUs and are defined as where f EL (z) is the ELU activation function applied to an input z.

## Difference ELU (DiffELU)

An ELU variant named difference exponential linear unit (DiffELU) 26 was proposed. It is defined as where a and b ∈ are fixed parameters. Hu et al. also tested setting the parameters to be trainable but that led to worse performance. The recommended setting is a = 0. 3 and b = 0. 1.

23 The AF is unnamed in the original work.

24 The formula in is malformed; we believe that this is the intended case. It is possible that authors intended that the SaRa is actually only the part that is defined for the negative inputs in eq. - however, we think that it is less likely as that would be only a swish (see section 4.4.1) AF with some fixed scaling of the output or the AHAF (see section 4.4.2) with fixed parameters.

25 The ref is not the original work with ThLUs; it references another work but that uses pure tanh as the AFs.

26 Hu et al. used the abbreviation DELU but this name is used for the AF proposed by Pishchik in throughout this work.

## Polynomial linear unit (PolyLU)

The polynomial linear unit (PolyLU) is an AF similar to the ELU proposed. It is defined as Despite the similarity with the ELU, Feng and Yang have shown that the PolyLU outperformed the ELU on the CIFAR-10/100 and Dogs vs. Cats datasets. The PolyLU was also proposed under the name first power linear unit with sign (FPLUS) 27.

## Inverse polynomial linear unit (IpLU)

The polynomial linear unit (IpLU) was proposed; it is defined as where a > 0 is a fixed hyperparameter guaranteeing a small slope for negative inputs.

## Power linear unit (PoLU)

The power linear unit (PoLU) is an AF similar to the ELU. It is defined as where a is a fixed parameter. Li, Ding, and Li used a ∈ { 1, 1. 5, 2 } in their experiments.

## Power function linear unit (PFLU)

The power function linear unit (PFLU) is an AF proposed ; it is defined as

## Faster power function linear unit (FPFLU)

The faster power function linear unit (FPFLU) is an AF proposed in that resembles the IpLU (see section 3.7.5) It is defined as

## Elastic adaptively parametric compounded unit (EACU)

The elastic adaptively parametric compounded unit (EACU) is a stochastic AF. It is defined as where b i is stochastically sampled during training as and a i is an adaptive parameter for each neuron or channel i.

27 Duan, Yang, and Dai used the equivalent definition f ( z ) = (sgn ( z ) · z +1) sgn( z ) -1 , hence the name.

## Lipschitz ReLU (L-ReLU)

A L-ReLU is a piecewise linear activation function. The slope of the negative part is selected with respect to a data-dependent Lipschitz constant. It builds on a proposed piecewise function that treats the positive z > 0 and negative values (z ≤ 0) separately: where ϕ (z) and µ (z) can be any function f: R → R. This makes the positive part of the piecewise lay in the first quadrant of the Cartesian coordinate system and the negative part in the third quadrant.

## Scaled exponential linear unit (SELU)

A SELU was proposed in order to make the network self-normalize by automatically converging towards zero mean and unit variance. The ELU was chosen as the basis for self-normalizing neural networks (SNNs) because these cannot be derived with ReLUs, sigmoid, and tanh units or even LReLUs - the activation function has to have negative and positive values for controlling the mean, saturation region where derivatives approach zero in order to dampen the variance if it is too large, a slope larger than one in order to increase the variance if it is too small, and a continuous curve to ensure a fixed point where the variance dampening is balanced out by the variance increasing. The SELU is defined as where a > 1 and b are predefined parameters; the recommended values are a ≈ 1. 05078 and b ≈ 1. 6733.

## Leaky scaled exponential linear unit (LSELU)

A leaky variant of SELU called leaky scaled exponential linear unit (LSELU) was proposed in and is defined as where a > 1 and b are predefined parameters of the original SELU (see section 3.7.11), and c is a new, predefined parameter controlling the leakiness of the unit.

## Scaled exponentially-regularized linear unit (SERLU)

The scaled exponentially-regularized linear unit (SERLU) is a modification of the SELU proposed; it is defined as where a > 0 and b > 0 are predefined parameters. An extension of this approach named ASERLU for bidirectional long short-term memory (BiLSTM) architectures was proposed.

## Scaled scaled exponential linear unit (sSELU)

Additional scaling of the negative pre-activations was introduced in the scaled scaled exponential linear unit (sSELU): where a > 1 and b are predefined parameters of the original SELU (see section 3.7.11), and c is a new, predefined parameter controlling the scaling of the negative inputs to the unit.

## RSigELU

A parametric ELU variant called RSigELU is defined as where a is a predefined parameter, Kiliçarslan and Celik used 0 < a < 1 in their work. For a = 0, the RSigELU becomes ReLU. The RSigELU was shown to outperform ReLU, LReLU, softsign, swish, ELU, SEU, GELU, LISA, Hexpo and softplus on the MNIST dataset, Fashion MNIST and the IMDB Movie dataset; it still outperformed these activation functions on the CIFAR-10 dataset but it was outperformed by its variant RSigELUD.

## HardSReLUE

Another AF proposed by Kiliçarslan is the HardSReLUE. Kiliçarslan defined the AF as where a is a fixed slope parameter.

## Exponential linear sigmoid squashing (ELiSH)

An activation function exponential linear sigmoid squashing (ELiSH) combines the swish (see section 4.4.1) and the ELU function. It is defined as

## Hard exponential linear sigmoid squashing (HardELiSH)

As ELiSH (see section 3.7.17) combines swish with ELU and linear function, the hard exponential linear sigmoid squashing (HardELiSH) combines the Hard sigmoid with ELU and linear function. It is defined as

## RSigELUD

The RSigELUD is a double parameter variant of the RSigELU (see section 3.7.15) that is defined as where a and b are predefined parameters, Kiliçarslan and Celik used 0 < a < 1 and 0 < b < 1 in their work. For a = b = 0, the RSigELUD becomes the ReLU the same as the RSigELU; however, for a = 0 and positive b, the function resembles the vanilla ELU.

## LS-ReLU

The LS-ReLU 28 is a ReLU-inspired AF proposed. It is defined as where a and b are fixed 29 parameters.

29 Wang et al. do not specify whether the parameters are trainable or fixed.

## Square-based activation functions

Several square-based activation functions were proposed in for better computational efficiency, especially on low-power devices. The approach uses the square function to replace the potentially costly exponential function. These function leads to significantly more efficient computation when there is no hardware implementation of the exponential function. The efficiency gains can be further improved with a custom hardware operator which can be used for efficient hardware implementation of all of the activation functions of the square-based family. The usage of the AFs from the family can lead to performance gains of one order of magnitude compared to traditional AFs for both forward and backward passes (depends on the particular activation function and the usage of fixed or floating point representations).

## SQNL

Acomputationally efficient activation function was proposed; unlike many other sigmoidal functions, it uses the square operator instead of the exponential function in order to achieve better computational efficiency. The derivative of the function is linear, which leads to a less computationally costly computation of the gradient. The function is defined in (the original paper had several mistakes in the definition) as The SQNL 30 has bounded range. The performance of the SQNL was verified on several datasets from the UCI Machine Learning Repository and on the MNIST dataset; more details available.

## Square linear unit (SQLU)

Similarly as the SQNL (see section 3.8.1) uses square function to form a sigmoidal function to approximate tanh, the square linear unit (SQLU) uses square function to form a ELU-like activation function that is computationally efficient: The SQLU basically uses the negative part of the SQNL and replaces the positive part with a linear function.

## Square swish (squish)

Another example of the family of activation functions based on the square operator is the square swish (squish), which is an AF inspired by the swish and GELU (see section 3.3.1). It uses the square non-linearity in order to achieve good computational efficiency: While the squish was inspired by the swish and GELU activation functions, it is an approximation of neither.

## Square REU (SqREU)

Similarly as REU (see section 3.6.49) is a combination of the ReLU and swish activation functions, the square REU (SqREU) is a combination of ReLU and squish: 30 SQNL is not an abbreviation but rather a name given by Wuraola and Patel.

## Square softplus (SqSoftplus)

A square softplus (SqSoftplus) is another square-based computationally efficient replacement of an activation function -softplus:

## Square logistic sigmoid (LogSQNL)

While the SQNL replaces the tanh AF, the square logistic sigmoid (LogSQNL) is a square-based replacement for the logistic sigmoid:

## Square softmax (SQMAX)

The square softmax (SQMAX) is a square-based replacement for the softmax, which is exponential-based. It is defined as where f (z j) is the output of a neuron j in a softmax layer consisting of N neurons and c = 4 is a predefined constant.

## Linear quadratic activation

Another square-based AF called linear quadratic activation (LinQ) was proposed. where a is a fixed parameter controlling the slope of the function's linear parts.

## Inverse square root linear unit (ISRLU)

Inverse square root linear unit (ISRLU) is an activation function similar to the ELU (see section 3.6.48). It has similar properties and a shape as ELU; however, it is faster to compute, leading to more efficient training and inference. It is defined as where a is a hyperparameter controlling the value to which the ISRLU saturates for negative inputs. While the authors state that the hyperparameter a could be trainable for each neuron i, only the non-trainable variant was analyzed. Carlile et al. analysed ISRLU with a = 1 and a = 3.

## Inverse square root unit (ISRU)

ISRU is an activation function meant to replace sigmoidal activation functions. It is defined as where a si a fixed hyperparameter controlling the saturation values; the parameter could be trainable similarly as in the ISRLU (see section 3.8.9) but only the nonadaptive variant was used.

## Modified Elliott function (MEF)

The modified Elliott function (MEF) is an AF inspired by the Elliott function (see section 3.2.15); it can also be considered to be a translated special case of the ISRU (see section 3.8.10) with a = 1. It is defined as

## Square-root-based activation function (SQRT)

A square-root-based activation function (SQRT) is a monotonically increasing, unbounded activation function proposed in with a similar structure as the earlier proposed logarithmic activation function (LAF) but with the square root function instead of the natural logarithm used in LAF. It is defined as The SQRT activation function was found to outperform both tanh and ReLU activation functions on the CIFAR-10 dataset in experiments.

A parametric variant of the SQRT called S-shaped activation function (SSAF) was proposed independently. It is defined as √ where a is a fixed parameter.

## Bent identity

The bent identity is an AF approximating the ReLU; it can be seen as a fixed variant of the bendable linear unit (BLU) (see section 4.2.37) with a i = 1 2. It is defined as

## Mishra activation function

The Mishra 31 AF is defined as

## Saha-Bora activation function (SBAF)

A Saha-Bora activation function (SBAF) was proposed in to be used for the habitability classification of exoplanets. It employs two non-trainable parameters α and k, which were set to k = 0. 98 and α = 0. 5, where authors determined a stable fixed point. It is defined as:

## Logarithmic activation function

The logarithmic activation function (LAF) was proposed in (ref. from). According to, it is defined as The LAF was independently proposed under the name symlog.

31 The AF was unnamed in the original papers; however, the work named it using the name of the original author. We keep the naming in this work.

## Symexp

The symexp is an activation function that is inverse of the logmoid activation unit (LAU). It is defined as

## Scaled polynomial constant unit (SPOCU)

The scaled polynomial constant unit (SPOCU) is a polynomial-based AF proposed. It is defined as and a > 0, b ∈, c > 0, and d ∈ [1, ∞) are fixed parameters satisfying additional conditions listed.

## Polynomial universal activation function (PUAF)

Similarly as the universal activation function (UAF) (see section 4.22), the polynomial (PUAF) 32 is able to approximate popular AFs such as the logistic sigmoid, ReLU, and swish. It is defined as where a, b and c are fixed parameters. The PUAF becomes the ReLU with a = 1, b = 0, and c = 0; the logistic sigmoid is approximated with a = 0, b = 5, and c = 10; finally, the swish is approximated using a = 1, b = 5, and c = 10.

## Softplus

The softplus function was proposed in and is defined as The softplus was used as an activation function in where it was used alongside with a ReLU. The advantage of softplus over ReLU is that it is smooth and it has a non-zero gradient for negative inputs; thus, it does not suffer from the phenomenon of dying out neurons that is common in networks with ReLU activations. The softplus was found to outperform ReLU for certain applications and architectures. A noisy variant was used for spiking neural networks.

## Parametric softplus (PSoftplus)

Parametric softplus (PSoftplus) is a softplus variant that allows for scaling and shifting using two additional parameters. The PSoftplus is defined as where a and b are fixed predetermined hyperparameters. The creation of the softplus was motivated by the assumption that activations with mean outputs close to zero can improve the performance of a neural network; since the output of the softplus is always positive, a shift parameter b was introduced to shift the mean output closer to zero. The slope controlling parameter a is used to adjust the function and the gradient disappearance or overflow during training. The recommended values are a = 1. 5 and b = ln.

32 Hwang and Kim named the function only as the universal activation function but this name is already taken by the UAF by Yuen et al. .

## Soft++

Another softplus extension Soft++ is a multiparametric nonsaturating nonlinear activation function proposed. It is defined as where a and b are fixed predetermined hyperparameters; however, Ciuparu, Nagy-D˘ abâcan, and Mure¸ san proposed they could be adaptable in future works. Multiple values of the parameters were used in the experiments, but a = 1 and b = 2 were found to work well; nevertheless, a hyperparameter optimization is recommended.

## Rand softplus (RSP)

A softplus variant rand softplus (RSP) introduces a stochastic parameter a l that is determined by the noise level of the input data. The RSP is defined as where a l is adapting to the input noise levels of each layer l -the exact procedure is described.

## Aranda-Ordaz

The Aranda-Ordaz AF was used in NNs. It is defined as where a > 0 is a fixed parameter. Essai Ali, Abdel-Raman, and Badry used a = 2 in their work.

## Bi-firing activation function (bfire)

A bi-firing activation function (bfire) was proposed in and is defined as where a is a predefined smoothing hyperparameter. The bfire is basically a smoothed variant of the later proposed vReLU (see section 3.6.25) as it becomes vReLU as a → 0.

## Bounded bi-firing activation function (bbfire)

A bounded variant of the bi-firing (bfire) activation function (see section 3.21) called bbfire was proposed; similarly as BReLU and BLReLU bounds ReLU and LReLU respectively (see sections 3.6.16 and 3.6.24), the bounded bi-firing function (bbfire) is defined as where a and b are predefined hyperparameters. The is symmetrical about the origin and has a near inverse-bellshaped activation curve. While authors of the original bfire solved potential numerical instabilities caused by the unboundedness by imposing a small L 1 penalty on the hidden activation values, the bbfire alleviates this problem explicitly without any need for such penalty.

## Piecewise Mexican-hat activation function (PMAF)

The piecewise Mexican-hat activation function (PMAF) was used; it is defined as where a is a fixed parameter - Liu, Zeng, and Wang used a = 4.

## Piecewise radial basis function (PRBF)

The piecewise (PRBF) was used; it is defined as where a and b are fixed parameters - Liu, Zeng, and Wang used a = 3 and b = 1.

## Comb-H-sine

A comb-H-sine is an activation function that was found using an evolutionary approach. It is defined as where sinh(x) is the hyperbolic sine, sinh -1 (x) is its inverse, and a is a predefined hyperparameter. This function was found to outperform ReLU, tanh, logistic sigmoid, and several other activation functions in LSTM models.

## Modified arcsinh

The modified arcsinh (m-arcsinh) AF was proposed in and is defined as Interestingly, the m-arcsinh can be used either as an AF in a NN or as a kernel function in the support vector machine (SVM).

## hyper-sinh

The hyper-sinh is an AF that uses the sinh and cubic functions; it is defined as

## Arctid

The arctid is an arctan-based AF used ; it is defined as

## Sine

The sine with inputs scaled by π was used as an activation: It was, for example, used recently with a data-driven determination of a network's biases. Just the sine function without any scaling was used as an activation.

Scaled sine with vertical shift was used; the used AF is defined as where a is a fixed parameter; a ∈ { 0. 2, 0. 8, 1. 2, 1. 8, 4 }.

## Cosine

A cosine activation was used in simulations ; it was defined as

## Cosid

The cosid is one of the AFs listed . It is defined as

## Sinp

A parametric AF similar to the cosid was proposed in under the name sinp. 33 It is defined as where a is a fixed parameter. Chan et al. used a ∈ { 1, 1. 5, 2 }.

## Growing cosine unit (GCU)

Another cosine-based AF is the growing cosine unit (GCU) proposed. It is defined as Empirical evaluation of the performance of GCU compared to ReLU, PReLU, and mish is available; its brief evaluation with respect to the generation of NFTs is available.

## Amplifying sine unit (ASU)

The amplifying sine unit (ASU) is the sine equivalent of the GCU

## Sinc

The sinc is an older AF proposed. It is defined as A shifted variant was proposed under the name shifted sine unit (SSU). It is defined as

## Decaying sine unit (DSU)

The decaying sine unit (DSU) is a sinc based AF proposed . It is defined as

## Hyperbolic cosine linearized squashing function (HcLSH)

The hyperbolic cosine linearized squashing function (HcLSH) is an AF proposed ; it is defined as

## Polyexp

The polyexp is an AF combining quadratic function and an exponential function; 34 it is defined as where a, b, c, and d are fixed parameters.

33 Technically, the full name used by Chan et al. is SinP[ N ] but we ommited the parameter from the name of the AF.

34 The is referenced as the origin of polyexp in but we have not seen the definition there.

## Exponential

The exponential was used as an AF . The AF was defined as

## E-Tanh

An AF named E-Tanh combining the exponential and tanh functions was proposed. It is defined as where a is a fixed scaling parameter.

## Evolved combination of tanh and ReLU

The combination of tanh and ReLU was found using neuroevolution in - while Vijayaprabakaran and Sathiyamurthy also mentioned other AFs, this combination led to the best performance on the HAR dataset using the long short-term memory (LSTM) units. The best-performing recurrent AF was See for evaluation details and for other top AFs.

## Wave

The wave is an AF combining quadratic function and an exponential function; 35 similarly as the polyexp but only with a single parameter; it is defined as and the regular AF was where a is a fixed parameter.

## Non-monotonic cubic unit (NCU)

A simple AF based on a third-degree polynomial was proposed . It is named non-monotonic cubic unit (NCU) and is defined as

## Triple

Another AF based on a third-degree polynomial called triple was proposed. It is defined as where a is a fixed parameter. Chen et al. tested values of a ∈ { 0. 1, 0. 5, 1, 2 } and observed that a = 1 reaches the best results.

## Shifted quadratic unit (SQU)

The shifted quadratic unit (SQU) is a simple non-monotonic AF defined as 35 The is referenced as the origin of wave in but we have not seen the definition there.

## Knowledge discovery activation function (KDAC)

Wang et al. proposed a special AF for knowledge discovery. This function named knowledge discovery activation function (KDAC) has two adaptive parameters a > 0 and b > 0 and one fixed parameter c. It is defined 36 as Wang et al. used fixed c = 0. 01.

## K-winner-takes-all activation function (k-WTA)

The k-winner-take-all (k-WTA) AF was used to improve adversarial robustness. It is defined as where f (z): R N → R N is the k-WTA AF and f (z) j its j -th element, z is the input to the AF, and k a fixed parameter.

## Volatility-based activation function (VBAF)

The volatility-based activation function (VBAF) 37 is an AF with multiple intputs proposed. It is meant for time-series forecasting and was used in a LSTM NN. It is defined as n is the number of time-series samples in the given period. Unfortunately, no more details about the application of the VBAF were provided; thus, it remains unclear whether the VBAF was applied only directly to the inputs, or it was used on intermediary representations of a NN.

## Chaotic activation functions

The chaotic activation functions (CAFs) listed in this work are AFs that use a recursive definition to produce a chaotic behavior.

36 The original code by Wang et al. is available .

37 Kayim and Yilmaz named the function originally only volatility activation function.

## Hybrid chaotic activation function

The hybrid chaotic activation function (HCAF) is a multi-output type of AF proposed . Neuron i in layer l takes an input z l i, applies the logistic sigmoid AF and then maps the outputs using logistic map function to individual outputs going to the neurons in layer l +1. Therefore, a single neuron in layer l emits a different activation value to each neuron in the layer l +1.

For a neuron i, the HCAF first applies the logistic sigmoid function to produce activation a i then the first value going to the neuron 1 in the following layer is calculated as and the output values going to the other neurons in the following layer are calculated recursively as where j is the number of a neuron in a following layer and r represents an excitatory rate in a neuron. Reid and Ferens used r = 4 as this value produces a chaotic behavior of the logistic map; generally, values below 0 or above 4 lead to the output to become unbounded, values between 0 and 1 lead to convergence toward the zero, values between 1 and 3 lead to convergence to a fixed number, values between 3 and 3.5 lead to a periodic solution and only values between 3.5 and 4 produce chaotic behavior.

## Fusion of chaotic activation function (FCAF)

Similarly as HCAF, also the fusion of chaotic activation function (FCAF) uses a recursive definition for computing the output of a neuron. The FCAF is defined 38 for hidden units as 39 and for the output units as where r, a, b, c, and d are fixed parameters; the suitable values for the parameter r are discussed in section 3.48.1 where an equivalent parameter is used.

## Cascade chaotic activation function (CCAF)

The cascade chaotic activation function (CCAF) was introduced in and is recursively defined for the neuron i +1 in a given layer using the preceding neuron i from the same layer as where a and b are two fixed parameter from the interval.

## Adaptive activation functions

The activation function introduces non-linearities to neural networks and is crucial for network's performance. Even though it might be suboptimal, the same activation function is usually used for the whole network or at least for all neurons in a single layer. Over the last few decades, there have been several attempts to use activation functions that might differ across neurons (e.g., ). The adaptive activation functions - i.e., functions that have a trainable parameter that changes their shape - have been receiving more attention recently (e.g., ) and might become a new standard in the field. One of the first descriptions of the general AAF approach is available in where Wu, Zhao, and Ding described an AF 40 that has one or more trainable parameters that are trained together with the rest of the network's weights. The simplest forms just add a parameter to a particular neural network that controls one of its properties (e.g., slope), while the more complex ones allow for the learning of a large number of activation functions (e.g., adaptive spline activation functions in ).

38 Kabir et al. did not explicitly defined what the index i denotes but most likely it denotes the i -th neuron in a given layer.

39 The formula given in probably missed a minus sign after the parameter a.

40 The authors used the name trainable activation function (TAF) rather than the adaptive activation function (AAF) that is used throughout this work.

## Transformative adaptive activation function (TAAF)

The transformative adaptive activation function (TAAF) is a family of AFs that adds four adaptive parameters for scaling and translation of any given AF - as such, the TAAFs represent a simple framework with a small set of additional parameters that generalizes a lot of AAFs that are listed in this work. While there are even more general approaches such as the adaptive blending unit (ABU) (see section 4.48) that allows for a combination of several different activation functions, the TAAFs are conceptually simpler and add only four additional parameters. The TAAF is defined as where z i input to the AF, α i, β i, γ i, and δ i, are adaptive parameters for each neuron i. Therefore, the output of a neuron with TAAF with inputs x i is: where x i are individual inputs, w i are its weights, and n is the number of incoming connections. If there is no unit x i, then the parameter γ is equivalent to the bias term of the neuron. It was shown in that each of the four adaptive parameters statistically significantly improve the performance of the AF - this is not surprising as many of the AFs presented in this work use subset of these parameters. For example, equivalent of α is used in the positive PReLU (see section 4.2.2), equivalent of β in the swish (see section 4.4.1), and equivalent of γ and δ in the FReLU (see section 4.2.15).

## The ReLU-based family of adaptive functions

The are numerous ReLU extensions that are adaptive. Some of the adaptive activations have a non-adaptive counterpart - e.g., PReLU (see section 4.2.1), which is basically a LReLU with an adaptive parameter of leakiness.

## Parametric rectified linear unit (PReLU)

However, AAFs might be very useful even in the simplest form with a single added parameter - an AAF called PReLU was used to obtain a state-of-the-art result on the ImageNet Classification in 2015, the first surpassing human-level performance. The PReLU generalize the ReLU by adding a parameter that controls the slope of the activation function for negative inputs (the ReLU is constant at zero for negative inputs) that is learned with other weights: where a i is an optimized parameter for each neuron/filter i. The LReLU is essentially a PReLU but with the parameter a i fixed and not trainable (see section 3.6.2 for LReLU details). PReLUs are better than ReLUs for verification-friendly NNs.

## Positive parametric rectified linear unit (PReLU + )

The positive PReLU is an adaptive variant of the SlReLU (see section 3.6.5) proposed; it is also a special case of, for example, DPReLU, Dual Line, and piecewise linear unit (PiLU). It is defined as where a i is a trainable parameter.

## Margin Relu

The margin (MarReLU) 41 is an adaptive variant of the Shifted ReLU where the shift a i is determined as the channelby-channel expectation value of the negative response. It is defined as 41 Heo et al. abbreviated it as MReLU, but this abbreviation is used for the mirrored rectified linear unit (see section 3.6.28) in this work.

## Funnel parametric rectified linear unit (FunPReLU)

The funnel rectified linear unit (FunReLU) 42 and funnel (FunPReLU) are 2D AFs proposed. The FunReLU and FunPReLU introduce a spatial context into the AF by comparing the input to a funnel condition instead of the zero that is used as the threshold in ReLU and PReLU. The FunReLU is defined as where z c,m,n is the input on the c -th channel at the 2D spatial position m,n and t (z c,m,n) is the spatial context from a 3 × 3 window 43 and p c,h,w denotes the coefficients on this window. The FunPReLU is defined similarly. The FunReLU was, for example, used.

## React-PReLU (RPReLU)

The react- (RPReLU) is an adaptive variant of the PReLU with vertical and horizontal shifts; it is defined as where a c, b c, and c c are trainable parameters for each channel c and z i denotes the input to the neuron i in the channel c; a c controls the horizontal shift, b c controls the vertical shift, and c c is the slope parameter for negative inputs as in the original PReLU.

## Smooth activation unit (SAU)

The smooth activation unit (SAU) is a smoothed variant of the PReLU 44 using the convolution operation with the Gaussian function. It is defined as where ∗ is the convolution operation, PReLU a i is the PReLU 45 parametrized by a i 46 and ϕ b i (x) is the Gaussian function parameterized by b i inversely controlling the deviation of the function. The resulting AF is then where a i and b i are either fixed or trainable parameters.

## Smooth maximum unit (SMU)

The smooth maximum unit (SMU) is an AAF that uses a smooth approximation of the absolute value function. The SMU is defined as where a i and b i are learnable parameters. This smooth approximation of the absolute value function using the Gaussian error function could be used to create a whole class of AFs similarly as in section 4.55.

## Leaky Learnable ReLU (LeLeLU)

An adaptive LReLU variant named leaky learnable ReLU (LeLeLU) was proposed. It is a LReLU with learnable scaling parameter: where a i is a trainable parameter for each neuron i.

42 Ma, Zhang, and Sun originally named the unit FReLU but its abbreviation would collide with the flexible ReLU.

43 Other sizes were also tested in but Ma, Zhang, and Sun found 3 × 3 to work the best.

44 The principle could be, however, applied to other AFs.

45 Biswas et al. used the LReLU in the definition of the SAU but since they consider the parameter a i trainable, we stick to the usage of PReLU in the defintion.

46 To conform to the used definition of the PReLU unit, we will use the slope scaling by 1 a i even though authors originally used the a i for slope scaling of negative inputs.

## Parametric rectified exponential unit (PREU)

Similarly as PReLU extends the ReLU (see section 4.2.1), the PREU extends the swish and ELU inspired REU. It is defined as where a i and b i are trainable parameters for each neuron/filter i. The advantage of PREU is that it uses the negative information near zero - unlike the ReLU.

## Randomly translational PReLU (RT-PReLU)

A randomly translational PReLU (RT-PReLU) an equivalent extension to PReLU as is RT-ReLU to ReLU (see section 3.6.11). It is defined as where a i is a trainable parameter and b i is a stochastic parameter for each neuron i randomly sampled from the Gaussian distribution at each iteration, b i ∼ N (0, σ 2), where σ 2 is the variance of the Gaussian distribution. The offset b i is set to zero during the test phase. The authors Cao et al. set the σ 2 = 0. 75 2 for their experiments. It is also possible to have the parameter b i sampled for each neuron i, but the a i is shared by all neurons in a channel c.

## Probabilistic activation (ProbAct)

A probabilistic class of activation functions ProbAct that adds a random noise to any activation function. It is defined as where g (z) is any function (either fixed or trainable) defining the mean of the probabilistic activation, e ∼ N is a random value sampled from a standard normal distribution, and σ is either fixed or learnable parameter controlling the range of the perturbation. σ can be either a global learnable parameter or different for each neuron i. The ProbAct used in is a ReLU based ProbAct defined as which resembles NReLU (see section 3.6.6) that adds random noise for output values for the positive inputs z. A similar concept for sigmoid and tanh activation was used in (see section 4.18).

The chaotic injections presented in represent a similar approach; however, the injections are not stochastic but rather defined using the chaos theory. Furthermore, Reid, Ferens, and Kinsner discuss several approaches for injections of a chaotic value s n into a ReLU: ReLU( z + s n ), ReLU( z · s n ), ReLU( z + z · s n ), ReLU( z ) + s n, ReLU( z ) · s n, ReLU( z ) + zs n, and ReLU( z ) + ReLU( z ) · s n.

## Adaptive offset activation function (AOAF)

Another ReLU variant with adaptive shift termed adaptive offset activation function (AOAF) was defined. The AOAF introduces two hyperparameters and one data-dependent adaptive parameter; it is defined as where b and c are predefined, fixed parameters and a i is the mean value of the inputs of neuron i. The recommended values for the parameters b and c are b = c = 0. 17 as it yielded the best image classification accuracy in the experiments.

## Dynamic leaky ReLU (DLReLU)

An error based dynamic leaky ReLU (DLReLU) was proposed in (under the name of Dynamic ReLU - DReLU -but this naming collides with DReLU established; see section 4.2.14 and section 4.56.3). The DLReLU is a LReLU where the leakiness depends on the test error from the previous epoch where a ∈ is a predefined parameter controlling the leakiness similarly as in LReLU (see section 3.6.2) and b t is a dynamic parameter computed for current training epoch t as the test erroch from the previous epoch t -1, i.e., b t = MSE t -1.

A version exp-DLReLU was proposed to deal with deeper networks with more than seven hidden layers in order to avoid too large error values causing the training to fail: where c t = exp(-b t) = exp (MSE t -1).

The advantage of DLReLU and exp-DLReLU is that the changes in leakiness are big at the beginning of the training due to higher test error and diminish towards the end. A similar effect could be obtained by a schedule of the leakiness parameter in the LReLU.

## Dynamic ReLU (DReLU)

Similar approach to the ABReLU is presented by the DReLU (not to be confused with identically named activations in), where a i is a threshold value that is computed as the midpoint of the range of input values for each batch; e.g., if the values range from -4 to 8, then a i = -4+8 2 = 2. The DReLU can be considered to be a variant of DisReLU (see section 3.6.44) with data-dependent determination of the shifting point.

## Flexible ReLU (FReLU)

The FReLU is a ReLU extension with zero-like property and the ability to capture negative information. The zero-like property is the ability to push activation means closer to zero as this might speed up learning. The FReLU builds on the ability to shift the AF where a i and b i would be optimized parameters. However, since the parameter a i can be learned by the bias term of the neuron to whose output is the activation function applied, the authors Qiu, Xu, and Cai formulate the FReLU as where b i is a trainable parameter.

## Adaptive shifted ReLU (ShiLU)

An adaptive shifted ReLU (ShiLU) is another adaptive variant of the ReLU activation; it is a variant that adds a trainable slope and a vertical shift: where a i and b i are trainable parameters for each neuron i. They used the name shifted ReLU, but that name is already taken by the non-adaptive Shifted ReLU; hence, the full name is adaptive shifted ReLU throughout this work to avoid confusion.

## StarReLU

The StarReLU is an adaptive version of the RePU of power 2 using a similar approach as the ShiLU; it is defined as where a i and b i are trainable parameters for each neuron i. If the parameters are not used in an adaptive manner, Yu et al. recommend setting a i = 0. 8944 and b i = -0. 4472.

## Adaptive HardTanh

An adaptive variant of HardTanh was used; it is defined as where a t is a scale factor for each epoch t such that 1 ≤ a 1 ≤ a 2 ≤... ≤ a t ≤... ≤ a T, T is the total number of training epochs and b is an adaptive parameter trained using BP with other parameters of the NN. The parameters a t are set such that the function starts in a similar shape as a regular HardTanh (see section 3.6.18) and gradually approaches the sign function. This allows for training a network that will gradually become a binary NN where each activation is the sign function which can be used for speeding the inference.

## Attention-based ReLU (AReLU)

Attention-based ReLU (AReLU) is a adaptive ReLU variant that uses ELSA - element-wise attention mechanism proposed. It is defined as where a l and b l are learnable parameters for each layer l, σ (x) is the logistic sigmoid function, C (x) is a function that clips the input into [0. 01, 0. 99]. The derivative of C (a l) is handled by just not using the BP when a l < 0. 01 or a l > 0. 99. While Chen, Li, and Xu observe that the parameters a l and b l are insensitive to the initialization, they recommend initializing a l = 0. 9 and b l = 2. 0 as a larger initial value of b l can speed up the convergence. The AReLU was found to outperform CELU, ELU, GELU, LReLU, Maxout, Relu, RReLU, SELU, sigmoid, softplus, swish, tanh, adaptive piece-wise linear unit (APLU), Padé activation unit (PAU), PReLU, and self-learnable activation function (SLAF) in experiments with various learning rates. The performance of AReLU was validated under different settings.

## Dual parametric ReLU (DPReLU) and Dual Line activation function

A DPReLU extends the concept of PReLU even further: where a i and b i are trainable parameters for each neuron i; these are initialized the same as PReLU a i = 1, b i = 0. 01. The DPReLU was also later proposed independently in under the name fully parametric ReLU and the abbreviation FReLU (which is already used in the literature for the flexible ReLU; see section 4.2.15).

## Dual Line

The DPReLU was further extended into a Dual Line activation function that adds a shift parameter where a i and b i are trainable parameters for each neuron i the same as in DPReLU and m i is an additional trainable shift parameter for each neuron or filter i; m i was initialized to m i = -0. 22.

## Piecewise linear unit (PiLU)

An AF very similar to the Dual Line is the piecewise linear unit (PiLU) proposed; it just extends the Dual Line concept by adding horizontal shifts. It is defined as where a i, b i, and c i are adaptive parameters for each neuron i. The PiLU geneneralizes, for example, ReLU, LReLU, PReLU, SlReLU, DPReLU, and Dual Line.

## Dual parametric family of activation functions

The DPReLU approach (see section 4.2.20) can be extended to a general concept transforming any activation function g (z): where g (z i) is any activation function and a i and m i are trainable parameters for each neuron i. The functions of this family are called dual parametric activation functions (DPAFs) throughout this text.

## Fully parameterized activation function (FPAF)

Similar approach to DPAF (see section 4.2.23) was proposed under the name of fully parameterized activation function (FPAF); the FPAF is defined as where a i and b i are trainable parameters for each neuron i and g 1 (z i) and g 2 (z i) can be any function. The FPAF, in contrast to the family of DPAFs, has no trainable shift but allows for learnable slopes for both parts of the piecewise function.

## Elastic PReLU (EPReLU)

The same as EReLU extends the concept of ReLU (see section 3.6), the Elastic (EPReLU) extends the PReLU it adds a varying coefficient to the positive part of the PReLU: where a i is the optimized parameter, k i is a sampled for each epoch and neuron i from the uniform distribution: a i ∼ U (1 -α, 1 + α) where α ∈. A modified training procedure for EPReLU is also proposed - the neuron weights and the trainable parameter a i are updated with k i = 1 in odd epochs, while in even epochs, the a i is kept fixed, the parameter k i is sampled from the uniform distribution, and only the neuron weights are updated. It was shown that the EPReLU leads to improved performance over the ReLU, PReLU, EReLU, APLU, network in network (NIN), and maxout unit networks on several datasets.

## Paired ReLU

A paired ReLU is a concept similar to CReLU (see section 3.6.34), but it introduces four trainable parameters. It is defined as where a i, b i, c i, and d i are trainable parameters for each neuron i. The parameters a i and c i are scale parameters and b i and d i are trainable thresholds; the inital values of scale parameters are a i = 0. 5 and c i = -0. 5.

## Tent

The tent is a ReLU-based AF proposed; it is defined as where a i is a trainable parameter. Rozsa and Boult recommend using batch normalization and initializing a i = 1. Also, having a weight decay on the parameter a i during training proved beneficial for certain tasks.

## Hat

The hat is an AAF very similar to the tent AF - the only difference is that the tent AF is centered around zero while the hat is positive only for positive inputs. The hat AF is defined as where a i is can be either fixed or trainable parameter. Wang, Xu, and Zhu used a i = 2 for the fixed variant; this value was also used.

## ReLU memristor-like activation function (RMAF)

The ReLU memristor-like activation function (RMAF) is an activation function similar to the swish AF (see section 4.4.1) and it also attempts to leverage the negative values. It is defined as where a i is a trainable parameter initialized a i = 1 for each neuron i or it is a fixed hyperparameter and b and c are fixed hyperparameters.

## Parametric tanh linear unit (PTELU)

A parametric tanh linear unit (PTELU) is an adaptive function that, for positive inputs, behaves just as a ReLU; however, the negative part is parameterized tanh function. It can also be seen as an extension of the PReLU (see section 4.2.1). It is an adaptive variant of ThLU (see section 3.7.1). It is defined as where a i and b i are trainable parameters for each neuron i; a i ≥ 0 and b i ≥ 0. It has output range of [-a i, ∞). The parameter a i controls the saturation value, and the parameter b i controls the convergence rate. While the AF resembles an adaptive extension of an ELU activation functions, the author Gupta and Duggal decided to use tanh function for the negative inputs because it gives a higher gradient for small negative inputs and saturates earlier than exp(z) -1 and thus the noise-robust deactivation state earlier and faster. The nonadaptive variant of PTELU with a i = 1 and b i = 1 was proposed.

## Tangent linear unit (TaLU)

The tanh linear unit (TaLU) is an AF similar to the PTELU. The TaLU is defined as where a i < 0 is either a learnable 47 or fixed parameter.

## PTaLU

The PTaLU 48 is a variant of TaLU with another learnable parameter. It is defined as where a i and b i are trainable parameters. Mercioni and Holban used initial values a i = -0. 75 and b i = 1.

## TanhLU

The tanhLU 49 is a parametric combination of the tanh and a linear function proposed. It is defined as where a i, b i, and c i are trainable parameters for each neuron i.

47 The variant with the adaptive parameter was named TaLU learnable by the authors.

48 Not an abbreviation but a name given by Mercioni and Holban .

49 Not an abbreviation but a name given by Shen et al. .

## TeLU

Despite the similar name, the tanh exponential linear unit (TeLU) 50 is quite different from the PTELU. The TeLU is closely related to the mish and TanhExp activations, but, unlike these two AFs, it also has an additional adaptive parameter. It is defined as where a i is either learnable or fixed scaling parameter.

## Tanh based ReLU (TReLU)

ATReLUwas proposed; however, it is is only a special case of previously proposed PTELU (see section 4.2.30). It is defined as where b i is a trainable parameter for each neuron i. This function is identical to the PTELU with its parameter a i fixed to a i = 1. Another special case of PTELU was proposed in also under the name of TReLU - this time, the parameter a i becomes a predefined fixed parameter, and b i becomes fixed to b i = 1. This function is denoted TReLU variant 2 (TReLU2) in this work and is defined as where a is fixed 51 parameter.

## Rectified linear tanh (ReLTanh)

A ReLTanh is a piecewise adaptive activation function that improves traditional tanh activation function - it replaces the positive and negative saturated regions of the tanh activation functions with straight lines whose slopes are identical to the slope of the tanh at the thresholds. It is defined as where tanh ′ (x) is the derivative of the tanh function and a i ∈ [a low, a high] and b i ∈ [b low, b high] are two trainable parameters that may be defined for each neuron i but are rather recommended to be shared by a whole layer l in order to decrease computational burden. The limits a low, a high, b low, and b high for the parameters are to constraint the learnable range and are predefined hyperparameters. Wang et al. used a low = -∞, a high = -1. 5, b low = 0, and b high = 0. 5 in their work. The initial values were set to a i = -1. 5 and b i = 0 for all layers (the parameters were shared layer-wise) in order to speed up the training process in early stages by the larger gradients.

## Bendable linear unit (BLU)

A BLU is an adaptive function that allows for any interpolation between the identity function and a rectifier. It is defined as where a i ∈ is a trainable parameter for each neuron or filter. One of the main advantages of the BLU is that it can model an identity function; the identity function is useful because its gradient cannot vanish or explode, and it also allows for a layer to be "skipped" - it is one of the reasons of why ResNets became so popular 50 used the TeLU as the name and not as an abbreviation; nevertheless, the long name tanh exponential linear unit fits the usual naming convention and, therefore, it is used in this work.

51 While Nakhua et al. used the parameter fixed during their experiments, they also speculated that making it learnable might improve the performance. as it is rather hard to learn an identity transformation using conventional neural network and the architecture with skip connections allows for easy learning of the identity mapping. Unless the magnitude | a i | is exactly 1, the derivative of BLU is non-zero for both positive and negative inputs (similarly to LReLU and in contrast to vanilla ReLU and ELU). BLU has a slope higher than 1 for positive inputs for a i approaching 1 (or for negative inputs for a i approaching -1); this property helps to avoid vanishing gradient problems. Another useful benefit is that BLU are C ∞ continuous, which can be theoretically exploited for speeding up the optimization, e.g.,. It was also shown that smooth activation functions provide better signal propagation.

## Rectified BLU (ReBLU)

Avariant of the BLU (see section 4.2.37) was proposed in under the name rectified BLU (ReBLU). It is defined as, where a i is a trainable parameter.

## DELU

The DELU 52 activation function is a ReLU variation that utilizes the SiLU function (see section 3.3). It is defined as where a i is a trainable parameter for each neuron i and σ (z i) is the logistic sigmoid function.

## Soft clipping mish

A ReLU variant called soft clipping mish (SC-mish) was proposed. It adds soft clipping to the positive inputs using the mish AF; it is defined as where a i is a fixed parameter; Mercioni and Holban used a i = 1. It also has a variant where the parameter a i is trainable. Such a variant is called soft clipping learnable mish (SCL-mish). When using the SCL-mish, Mercioni and Holban initalized the parameter a i = 0. 25.

## Soft clipping swish

Yet another AF proposed by Mercioni and Holban is the soft clipping swish (SC-swish). This function is very similar to SC-mish and is defined as where σ (z) is the logistic sigmoid.

## Parametric swish (p-swish)

The parametric swish (p-swish) is another AF proposed by Mercioni and Holban. It is defined as where a i, b i, and c i are either trainable or fixed parameters (or combination thereof). The parameters were initialized to a i = 1, b i = 1 and c i = 0 in experiments. An AF named R\_S similar to the p-swish was independently proposed; it is equivalent to a p-swish with fixed a i = 1.

52 DELU is not an abbreviation but rather a name given by Pishchik.

## Parametric exponential linear unit (PELU)

Similarly as PReLU extends the concept of ReLU, the parametric exponential linear unit (PELU) extends the concept of ELU (see section 3.6.48). The PELU builds on a parameterization that separately controls the saturation point, the decay, and the slope: where a i, b i, and c i are trainable parameter for each neuron i. However, the PELU introduces only two new parameters a i controlling the saturation point, and b i controlling the decay - to control the shape of the activation function; the slope is not controlled separately through another parameter as it could lead to non-differentiability at z i = 0; therefore the slope is set such that the derivatives on both sides of zero are equal which leads to c i = a i b i and therefore the PELU is defined as The PELU combined with mixing different activation functions which use an adaptive linear combination or hierarchical gated combination of activation function was shown to perform well - see section 4.2.45.

## Extended exponential linear unit (EDELU)

An adaptive function called extended exponential linear unit (EDELU) 53 was proposed. This function is the same as the PELU, but it omits the vertical scaling for positive inputs, adds a parameter controlling the threshold, and uses inverse definitions of the parameters present in the PELU. It is defined as where a i ≥ 0 54 and b i ≥ 0 55 are trainable PELU parameters and c i ≥ 0 is the novel parameter for controlling the threshold that has to satisfy the relationship while the c i = 0 is always a solution of the equation, there are other solutions for b i > a i > 0.

## Adaptive combination of PELU and PReLU

Two different activation functions can be mixed together, as shown. One such example of mixed activation function is where a i is a combination coefficient that might be learned from the data. Another mixing approach was shown for combining PReLU and PELU: where σ (x) is the logistic sigmoid. Qian et al. also proposed other mixing schemes such as hierarchical activation, winner-take-all selection whose performance were shown on the MNIST, CIFAR-10 and CIFAR-100 datasets; see for details.

## Fast exponential linear unit (FELU)

An ELU variant called fast exponential linear unit (FELU) aiming at efficient training and network inference was proposed in - it is inspired by fast approximation of the exponential function proposed in to replace the exponential in the ELU: where a i is a trainable parameter controlling the soft saturation region.

53 Authors called the function extendeD ELU resulting in an abbreviation DELU but that name is already taken by an AF proposed a few months earlier .

54 The PELU equivalent would be 1 b i.

55 The PELU equivalent would be 1 a i.

## P+FELU

Adem proposed variant of the FELU function named P+FELU; this variant has an added parameter and is defined as where a i is a trainable parameter same as the original FELU and b is the added trainable parameter.

## Multiple parametric exponential linear unit (MPELU)

A PELU extension, multiple parametric exponential linear unit (MPELU), uses two trainable parameters to allow for a combination of a ReLU and ELU. The multiple parametric exponential linear unit (MPELU) is defined as where a i and b i are trainable parameters for each neuron i. The ReLU, certain parameterizations of PELU, and ELU are special cases of the MPELU. A special method for weight initialization of neurons with MPELU units was also proposed; depending on a particular initialization, the method can become the initialization for ELU networks or for ReLU networks. The MSRA 56 filler approach can be considered as a special case of the MPELU initialization. The MPLU initialization is a similar approach to LSUV initialization, but unlike the LSUV initialization, it provides an analytic solution for ELU and MPELU and therefore it has lower computational costs. It was also shown that the MPELU works better with batch normalization compared to the vanilla ELU. The performance of the MPELU was empirically shown on the CIFAR-10 and CIFAR-100 datasets using multiple neural network architectures, e.g. nine-layer deep NIN or even a ResNet with 1001 layers.

## P-E2-ReLU

The AAF named P-E2-ReLU is combining two ELUs and a ReLU using two adaptive parameters. It is defined as where a i and b i are trainable parameters for each neuron i. The parameters were initialized to a i = 0. 4 and b i = 0. 3 in experiments. Jie et al. mentioned that other combinations could be considered and called this family P-E2-XU. One such combination is denoted P-E2-Id and is defined as and another is named P-E2-ReLU-1 whera a i is a trainable parameter in both AAFs. The parameter was initialized to a i = 0. 5 in experiments.

## Soft exponential

The soft exponential activation function is an adaptive activation function that is able to interpolate between logarithmic, linear, and exponential functions. It is defined as where a i is a trainable parameter. The soft exponential activation functions is continuously differentiable with respect to z i and also with respect to a i; furthermore, for any constant a i, the function is monotonic. When a i = -1, the function becomes f (z i) = ln(z i), while for a i = 0 it becomes linear function f (z i) = z i and for a i = 1, it is the exponential function f (z i) = exp(z i).

56 The initialization method was unnamed in the original paper but was later named Microsoft Research Asia (MSRA) filler.

## Continuously differentiable ELU (CELU)

A CELU was proposed; CELU is very similar to the original parameterization of ELU but reformulated such that the derivative at z i = 0 is 1 for all values of a i. CELU is defined as where a i is a learnable parameter for each neuron i. Its main advantages are that its derivative with respect to z i is bounded and that it contains both the linear transfer function and ReLU.

## Erf-based ReLU (ErfReLU)

The Erf-based ReLU (ErfReLU) is an AAF similar to the ELU. It is defined as where a i is a learnable parameter for each neuron i and erf (z i) is the Gauss error function.

## Parametric scaled exponential linear unit (PSELU)

Aparametric scaled exponential linear unit (PSELU) is basically a SELU (see section 3.7.11) where the parameters a and b controlling the behavior are trainable. It is defined as where a i and b i are trainable parameters for each neuron i.

## Leaky parametric scaled exponential linear unit (LPSELU)

Aleaky parametric scaled exponential linear unit (LPSELU) is a leaky extension of the PSELU (see section 4.2.53) to avoid small gradients hindering the learning process: where a i and b i are trainable parameters for each neuron i and c i is either a predefined constant or a trainable parameter.

## Leaky parametric scaled exponential linear unit with reposition parameter (LPSELU\_RP)

The LPSELU can be extended by a reposition parameter similarly as FReLU extends ReLU (see section 4.2.15); such function is called LPSELU\_RP and is defined as where a i and b i are trainable parameters for each neuron i, and c i is either a predefined constant or a trainable parameter the same as for LPSELU (see section 4.2.54) and m i is a trainable reposition parameter. It was empirically observed that the shift parameter m i converges to a small negative value, which supports the hypothesis that the negative output of activation functions is important.

## Shifted ELU family

A family of several activation functions, shifted exponential linear unit, was proposed; functions in this family have either vertical or horizontal shift of an ELU activation function that can be either constant or trainable. An ELU with fixed horizontal shift is ShELU, with fixed vertical SvELU and PELU (see section 4.2.43) with trainable horizontal shift is PShELU. The ShELU is defined as where a is a fixed parameter similarly as in the vanilla ELU and b is novel, preset parameter controlling the horizontal shift. The SvELU is defined similarly: where a is a fixed parameter similarly as in the vanilla ELU and b is novel, preset parameter controlling the vertical shift. Grelsson and Felsberg define also a variant of PELU with horizontal shift called PSheLU: where a i and b i are trainable parameters of the original PELU, and c i is a novel trainable parameter controlling the horizontal shift for each neuron i. For some reason, Grelsson and Felsberg did not propose a PELU with vertical shift (PSvELU), but it could be defined in a similar manner where a i, b i are trainable parameters of the original PELU and c i is a novel trainable parameter controlling the vertical shift. Note that the shifted activation functions with horizontal shifts are equivalent to non-shifted variants with biases that are individual for each neuron and not shared in the same tiling pattern as the convolutional kernel.

## Tunable swish (T-swish)

The tunable swish (T-swish) proposed in is an AAF combining the ELU, E-swish (see section 4.4.4) and swish (see section 4.4.1) as it has trainable parameters for both horizontal and vertical scaling for negative inputs. It is defined as where a i, b i, and c i are either fixed or trainable parameters for each neuron i.

## Rectified parametric sigmoid unit (RePSU)

The rectified parametric sigmoid unit (RePSU) is an AAF proposed; it consists of a linear combination of two components - rectified parametric sigmoid shrinkage unit (RePSKU) and rectified parametric sigmoid stretchage unit (RePSHU). It is defined as and a i, b i, c i, d i, and e i are parameters (common for both RePSKU b i,c i,d i,e i (z i) and RePSHU b i, c i, d i, e i (z i)). The RePSU is a generalization of the smooth sigmoid-based shrinkage (SSBS) function used for image denoising.

## Parametric deformable exponential linear unit (PDELU)

An adaptive activation function parametric deformable exponential linear unit (PDELU) is based on the premise that shifting the mean value of the output closer to zero speeds up the learning. The PDELU is defined as where a i is a trainable parameter for each neuron i and b is a fixed hyperparameter controlling the degree of deformation. The Cheng et al. recommend setting b = 0. 9. The authors found that the MSRA initialization method is consistent with PDELU. The performance of PDELU was empirically shown on the CIFAR-10 and CIFAR-100 datasets and on the ImageNet dataset where it outperformed ReLU, APLU, LReLU, PReLU, SReLU, ELU, MPELU (and other) activation functions.

## Elastic exponential linear unit (EELU)

An adaptive variant of the ELU function that has a stochastic component was proposed in - the elastic exponential linear unit (EELU). The EELU combines EReLU (see section 3.6.38) and MPELU (see section 4.2.48) and is defined as where a c and b c are trainable parameters shared among all neurons of a channel c and k c i is a randomly sampled noise parameter for each neuron i in channel c during the training stage and set to 1 during the testing stage. The k c i is sampled coefficient from Gaussian distribution with a random standard deviation that is truncated from 0 to 2; k c i is therefore sampled as where N (1, σ 2) is Gaussian distribution with mean 1 and variance σ 2, U denotes the uniform distribution. The ϵ is a hyperparameter; the authors recommend smaller values, e.g., 0.1 or 0.2.

The training algorithm is also modified and works in two steps - first, the EELU parameter and the weights are updated with fixed k c i = 1, and then weights are updated with random k c i and fixed EELU parameters. The authors also recommend using the MPELU initialization method.

## Parametric first power linear unit with sign (PFPLUS)

The parametric first power linear unit with sign (PFPLUS) is an AAF proposed. It is defined as where H(z i) is Heaviside step function (see section 3.1) and a i > 0 and b i > 0 are trainable parameters for each neuron i. For example, the PFPLUS is similar to the ReLU when a i = 0. 2 and b i = 10 and similar to a linear mapping when a i = 5 and b i = 0. 1.

## Parametric variational linear unit (PVLU)

The parametric variational linear unit (PVLU) is an adaptive variant of the VLU proposed. It is defined as where a i and b i are trainable parameters.

## Sigmoid-based adaptive functions

Many different adaptive activation functions based on the sigmoid family were proposed in the literature, one of the earliest examples is a logistic sigmoid activation function with shape autotuning. The function proposed by Yamada and Yabuta uses a single parameter controlling both the amplitude and the slope of the activation function. The proposed adaptive function is defined as where a ∈ (0, ∞) is a learnable parameter.

## Generalized hyperbolic tangent

The generalized hyperbolic tangent introduces two trainable parameters that control the scale of the activation function: where a i and b i are trainable parameters for each neuron i. A non-adaptive version with fixed parameters was used for document recognition in in order to improve convergence toward the end of the learning session (see section 3.2.3).

## Trainable amplitude

A more general approach was introduced, which used networks with a trainable amplitude of activation functions; the same approach was later used for recurrent neural networks. The class of adaptive functions with a trainable amplitude is defined as where a i and b i are trainable parameters for each neuron i. The a i determines the trainable amplitude and the b i trainable offset. These parameters can be either different for each neuron or may be shared by a whole layer or even a whole network.

## Adaptive slope sigmoidal function (ASSF)

A adaptive slope sigmoidal function (ASSF) based on the work of Yamada and Yabuta, Yamada and Yabuta was used. It is defined as where σ is the logistic sigmoid and a is a global trainable parameter. The ASSF was also rediscovered by Mercioni, Tiron, and Holban.

## Slope varying activation function (SVAF)

A slope varying activation function (SV AF) was proposed in where a is a global trainable parameter. The slope varying activation function was proposed together with a BP modification that has two different learning rates. The slope varying activation function was implemented as a modification of the BP algorithm rather; a different example of modification of the BP algorithm resulting in an adaptive activation function is presented.

## TanhSoft

The TanhSoft is a family of AAFs proposed in that combine the softplus and tanh that contains three notable cases - TanhSoft-1, TanhSoft-2, and TanhSoft-3.

The general TanhSoft is defined as where a i, b i, c i, and d i are either trainable or fixed parameters; a i ∈ (-∞, 1], b i ∈ [0, ∞), c i ∈ (0, ∞), and d i ∈.

The first AF, named TanhSoft-1, is defined as where a i is a trainable parameter; it can be obtained from the general TanhSoft by setting b i = 0 and d i = 1. The second AF, TanhSoft-2, is defined as where b i and c i are trainable parameters. The TanhSoft-2 can be obtained from the general TanhSoft by setting a i = 0 and d i = 0. The last AF, TanhSoft-3, is defined as where a i is a trainable parameter. It can be obtained from the general TanhSoft by setting b i = 0 and d i = 1.

## Parametric sigmoid (psigmoid)

An adaptive variant of logistic sigmoid named parametric sigmoid (psigmoid) 57 was proposed. 58 Similarly as in generalized hyperbolic tangent, it introduces two scaling parameters to a logistic sigmoid: where a i is a trainable parameter for each neuron or channel i and b is a global trainable parameter.

## Parametric sigmoid function (PSF)

A parametric sigmoid function (PSF) is a continuous, differentiable, and bounded function proposed in 59 and is defined as where m is a global trainable parameter. The parameter m controls the slope of the sigmoid and the position of the maximum derivative; the envelope of the relevant derivatives for different values of m is also a sigmoid function. The larger values of m improve the gradient flow. The PSF is only one instance of a larger class of activation functions proposed.

## Slope and threshold adaptive activation function with tanh function (STAC-tanh)

The slope and threshold adaptive activation function function with tanh function (STAC-tanh) was proposed. It is basically a tanh based equivalent of the improved logistic sigmoid with adaptive parameters. It is defined as where a i and b i are trainable parameters.

## Generalized Riccati activation (GRA)

The generalized Riccati activation (GRA) is an adaptive variant of a sigmoid AF proposed. It is defined as where a i, b i, and c i are adaptive parameters b i > 0 and c i > 0.

## Adaptive sigmoid-weighted linear units

There are several AFs that are based on the SiLU but have an adaptive parameter; the most common example is the swish AF, but there are also other popular functions based on the same principle.

## Swish

A swish activation function is an adaptive variant of the SiLU (see section 3.3); it is also the member of the LAAF class (see section 4.16): where σ (z) is the logistic sigmoid, a i is either a fixed hyperparameter or a trainable parameter. The swish has an output range of (-∞, ∞). The parameter a i controls the amount of non-linearity the swish activation has. The swish might also be considered a member of the family of activate or not activation functions (ACONs); it is then named ACON-A. The parametric SiLU (PSiLU) is another name for the swish activation used.

57 Not to be confused with parametric sigmoid function (PSF) from section 4.3.7.

58 It seems that this AAF was first proposed in 2010 in and then independently in 2021 .

59 contains the definition equivalent to f ( z ) = PSF ( z 2 ).

## Adaptive hybrid activation function (AHAF)

A swish variant with vertical scaling was proposed in under the name adaptive hybrid activation function (AHAF). It is defined as where a i and b i are trainable parameters.

## Parametric shifted SiLU (PSSiLU)

The parametric shifted SiLU (PSSiLU) is a swish based AAF proposed. It is defined as where a i and b i are trainable parameters.

## E-swish

E-swish is an AAF inspired by the swish activation function (see section 4.4.1); the E-swish has a scaling parameter that allows for vertical scaling of the activation function. The name of the activation function is not chosen well as the E-swish is rather extending the SiLU (see section 3.3) and not swish which is its adaptive variant. 60 The function is defined as where σ (z) is the logistic sigmoid and a is a preset parameter - however, the parameter a is considered to be trainable in review. Alcaide recommends setting a ∈ to avoid exploding gradients that are hypothesized to more likely occur for higher values of a. The E-swish was found to outperform the SiLU (called swish in the paper) on the the MNIST, CIFAR-10 and CIFAR-100 datasets using the Wide ResNet (WRN) architecture.

## ACON-B

The ACON family conists of swish AF and several extensions; one is named ACON-B and is defined as where a i and b i are trainable parameters. The b i is initalized to 0.25 and a i to 1. 61

## ACON-C

The ACON-C is another member of the ACON family. It is defined as where a i, b i, and c i are trainable parameters. Ma et al. used initial values a i = 1, b i = 0, and c i = 1.

Ma et al. also proposed a general extension to the ACON family named MetaACON which uses a small NN to determine the value of the parameter a i; they used the variant ACON-C for the experiments with MetaACON resulting in MetaACON-C 62. The MetaACON was used to improve YOLOv7 . Kan et al. extented the ACON AFs into an AF they named CBAC 63. The ACONs were used, for example, . The 1Dmeta-ACON is a MetaACON extension proposed .

## Parameterized self-circulating gating unit (PSGU)

The Parameterized self-circulating gating unit (PSGU) is related to the LiSHT and GTU activation functions as it is basically a LiSHT with gated input with learnable scaling parameter. It is defined as 60 Calling the SiLU as swish is quite common in the literature, e.g., exponential swish, generalized swish, and TS-swish.

61 There is no initial value for a i in ACON-B mentioned explicitly ; however, there is one for its extension ACON-C.

62 The implementation of MetaACON-C and other AFs from the ACON family is available at con.

63 No further description is provided. where a i is a learnable parameter and σ (z) is the logistic sigmoid function. Li et al. also propose a novel initialization method for NNs with the PSGU AF and show that it is more suitable for the use with PSGU than other common methods. The PSGU is shown to outperform ReLU, mish, swish, PATS and GELU using various NIN and ResNet architectures. The PSGU was also proposed in under the name TSReLU learnable (TSReLUl) as the adaptive variant of TSReLU. Mercioni, Tat, and Holban used a i = 0. 5 as the initial value.

## Tangent-bipolar-sigmoid ReLU learnable (TBSReLUl)

Similarly as TSReLUl is an adaptive variant of TSReLU, the TBSReLU learnable (TBSReLUl) is an adaptive variant of TBSReLU. This variant is defined as where a i is a trainable parameter. Mercioni, Tat, and Holban used a i = 0. 5 as the initial value.

## PATS

The AF named PATS 64 is very similar to PSGU, but it uses arctan and a random scaling parameter instead of the tanh and the adaptive parameter in PSGU. It is defined as where σ (z) is the logistic sigmoid function and is sampled during training 65 from the uniform distribution with bounds l and u such that 0 < l < u < 1. The authors experimented with fixed, deterministic values of a i ∈ { 1 4, 1 2, 5 8, 3 4 } -the value 5 8 led to lowest test error on the CIFAR-10; they also deemed that suitable values for l and u are 1 2 and 34 respectively. However, only fixed variant with a i = 5 8 was used in the follow-up works such as.

## Adaptive quadratic linear unit (AQuLU)

The adaptive quadratic linear unit (AQuLU) is an adaptive SiLU variant proposed; it is defined as where a i and b i are trainable parameters for each neuron i.

## Sinu-sigmoidal linear unit (SinLU)

Another adaptive SiLU variant is the sinu-sigmoidal linear unit (SinLU), which adds an adaptive term using the sine function to the linear part of the SiLU. The SinLU is defined as where σ (z i) is the logistic sigmoid function and a i and b i are trainable parameters for each neuron i.

## ErfAct

An AAF based on the Gauss error function was proposed. The AAF is named ErfAct and is defined as where a i and b i are trainable parameters for each neuron i and erf(x) is the Gauss error function.

65 Unfortunately, the author did not specify what happens during the test phase , one can only assume that the expected value is used.

## Parametric serf (pserf)

An adaptive version of the serf AF named parametric serf (pserf) was proposed. It is defined as where a i and b i are trainable parameters for each neuron i and erf(x) is the Gauss error function.

## Swim

The swim is an adaptive variant of the PFLU (see section 3.7.7) independently proposed. It is defined as where a i is either fixed or trainable parameter for each neuron i. Abdool and Dear used fixed a i = 0. 5 in their experiments.

## Tuned softmax (tsoftmax)

A softmax (see section 3.5) variant named tuned softmax (tsoftmax) was proposed; it is defined as where f (z j) is the output of a neuron j in a softmax layer consisting of N neurons and c is an adaptive parameter.

## Generalized Lehmer softmax (glsoftmax)

The generalized Lehmer softmax (glsoftmax) is a softmax variant proposed. It is defined as where LNORM(z j) is a generalized Lehmer-based Z-score-like normalization with four trainable parameters a i, b i, c i, and d i defined: x is a vector of elements x k, k = 1,..., N and z -M a i,b i represents a vector with elements z k -M a i,b i, k = 1,..., N.

## Generalized power softmax (gpsoftmax)

The generalized power softmax (gpsoftmax) is another softmax variant proposed. It is defined as where PNORM(z j) is a generalized power-based Z-score-like normalization with four trainable parameters a i, b i, c i, and d i defined: x is a vector of elements x k, k = 1,..., N and z -M a i,b i represents a vector with elements z k -M a i,b i, k = 1,..., N.

## Adaptive radial basis function (ARBF)

The adaptive (ARBF) was used. It is defined as where a i and b i are adaptive parameters for each neuron i. The parameter a i controls the center while the parameter b i controls the width.

## Parametric Gaussian error linear unit (PGELU)

The AAF named parametric Gaussian error linear unit (PGELU) was proposed in as the result of noise injection. It is an GELU (see section 3.3.1) adaptive variant defined as where Φ(z) is the standard Gaussian CDF and a is a global learnable parameter representing the root mean square (RMS) noise.

## Parametric flatted-T swish (PFTS)

A parametric flatted-T swish (PFTS) is an adaptive extension of the FTS (see section 3.6.46); PFTS is identical to FTS except for that the parameter T is adaptive - i.e.: where T i is a trainable parameter for each neuron i; the parameter T i is initialized to the value -0.20.

## Parametric flatten-p mish (PFPM)

The parametric flatten-p mish (PFPM) is an AAF proposed; it is defined as where p i is a trainable parameter.

## Gaussian error unit (GEU)

The AAF named Gaussian error unit (GEU) was proposed in as the result of noise injection. It is defined as where Φ(z) is the standard Gaussian CDF and a is a global learnable parameter representing the RMS noise. The GEU multiplied by z becomes the PGELU (see section 4.9).

## Scaled-gamma-tanh activation function (SGT)

The scaled-gamma-tanh (SGT) AF is a piecewise polynomial function proposed. It is defined as where a and c are fixed, predefined parameters and b i and c i are trainable parameters for each neuron or filter i.

## RSign

An adaptive variant of the sign function was used. It is called react-sign (RSign) and is defined as where a c is an adaptive threshold for each channel. An extension was used, where Ding, Liu, and Zhou used multiple RSign functions for each channel.

## P-SIG-RAMP

An AAF combining the logistic sigmoid and ReLU was proposed in under the name P-SIG-RAMP. The P-SIG-RAMP is defined as where a i ∈ and b i are trainable parameters.

## Locally adaptive activation function (LAAF)

A general class of slope varying functions called locally adaptive activation function (LAAF) was proposed: where a i is a trainable parameter for each neuron i and g is any activation function; Jagtap, Kawaguchi, and Karniadakis used logistic sigmoid, tanh, ReLU, and LReLU as g in their LAAFs. The corresponding activations are thus given by where b is the LReLU leakiness parameter. To accelerate the convergence, Jagtap, Kawaguchi, and Karniadakis add additional fixed parameter to the expression: where n > 1 is a fixed parameter. It was found that this additional parameter improves both the convergence rate and the solution accuracy.

## Adaptive slope hyperbolic tangent

A tanh activation function with adaptive slope was used in an multi-layer perceptron (MLP) architecture. The used activation function is defined as where a i is a trainable parameter for each neuron i.

## Parametric scaled hyperbolic tangent (PSTanh)

A parametric activation function similar to the swish but based on the tanh function instead of the logistic sigmoid called parametric scaled hyperbolic tangent (PSTanh) was proposed. It is defined as where a i and b i are trainable parameters for each neuron i. The function is also very similar to the PTELU (see section 4.2.30) as for z i > 0 and a i ≈ 1, the output is close to z i (the exact distance depends on the parameters a i and b i).

## Scaled sine-hyperbolic function (SSinH)

An AF similar to PSTanh is the scaled sine-hyperbolic function (SSinH); it is defined as where a i and b i are trainable scaling parameters and sinh is the hyperbolic sine.

## Scaled exponential function (SExp)

Husain, Ong, and Bober also proposed scaled exponential function (SExp) along with the SSinH. It is defined as where a i and b i are trainable scaling parameters and sinh is the hyperbolic sine.

## Logmoid activation unit (LAU)

A learnable LAU was proposed; which utilise two learnable parameters a l and b l for each network layer l where z i,l is the output of the neuron i in layer l without the activation function and σ is the logistic sigmoid. The author used initial values of the parameters a l = b l = 1 for each network's layer l and trained these parameters together with the rest of the network's weights.

## Cosinu-sigmoidal linear unit (CosLU)

The cosinu-sigmoidal linear unit (CosLU) is an adaptive activation function proposed in that is based on the logistic sigmoid. It is defined as where a i and b i are trainable parameters for neuron i and σ (z i) is the logistic sigmoid function. The cosine amplitude is controlled by the parameter a i, whereas its frequency is controlled by the parameter b i.

## Adaptive Gumbel (AGumb)

An activation function adaptive Gumbel (AGumb) is based approach of viewing activation functions as a combination of unbounded and bounded components where the bounded component is based upon a cumulative distribution function of a continuous distribution. While the logistic sigmoid activation is a CDF of the symmetric logistic distribution, the AGumb is based on the Gumbel distribution. It is defined as where a i ∈ R + is trainable parameter for each neuron i.

## Shape autotuning adaptive activation function (SAAAF)

The shape autotuning adaptive activation function (SAAAF) 66 is an AAF proposed. It is defined as where a i ≥ 0 and b i ≥ 0 are trainable parameters for neuron i and 0 < b i a i < e.

## Noisy activation functions

Stochastic variants of saturing activation functions such as the logistic sigmoid or hyperbolic tangent were proposed in where an additional noise is injected to the activation function when it operates in the saturation regimes. The noisy activation function is defined as where h(z i) is any saturating activation function such as hard-tanh or hard-sigmoid, u(z i) is its linearization using first-order Taylor expansion around zero, c is a hyperparameter changing the scale of the standard deviation of the noise, p i is a trainable parameter adjusting the magnitude of the noise for each neuron i, a is a hyperparameter influencing the mean of the added term, and σ (x) is the logistic sigmoid function. ϵ is the added noise; it is defined as ϵ = | ξ | 66 Zhou et al. named the function as shape autotuning activation function but the resulting abbreviation SAAF is already taken by smooth adaptive activation function (see section 4.29). Since the proposed function is an AAF, we term it as such to avoid the abbreviation collision. if the noise term ξ is sampled from half-normal distribution and as ϵ = ξ if the noise term ξ is sampled from normal distribution with mean 0 and variance 1.

Gulcehre et al. also experimented with adding noise to the input of the activation function, resulting in an activation function defined as where s (z i) is either fixed parameter s (z i) = b or it is a trainable term where the meaning of c, σ, p i, h(z i), and u(z i) is same as in eq..

A similar concept in ReLU settings is the ProbAct activation function (see section 4.2.11).

## Fractional adaptive activation functions

Fractional adaptive activation functions (FAAFs) were proposed in as a generalization of several activation functions using the fractional calculus (see for a general introduction to the fractional calculus). Generally, for any activation function f (z), its generalization g (z) using fractional derivatives is defined as the a -th fractional derivative of f: where a can be a learnable 67 parameter. The FAAFs proposed in were further evaluated.

## Fractional ReLU

The fractional ReLU (FracReLU) is defined as which is then computed as which is then computed as where Γ(x) is the Gamma function and a i is a trainable parameter. The FracReLU was later independently proposed in under the name FReLU (but this abbreviation is already taken by flexible ReLU).

## Fractional softplus

The fractional softplus (FracSoftplus) is using the softplus function to generalize sigmoid-like functions through fractional derivatives. It is defined as where a i is a trainable parameter. Particularly interesting cases are when a i = 0 as it is the softplus function, a i = 1 logistic sigmoid, and a i = 2 which leads to a bell-like shape.

## Fractional hyperbolic tangent

The fractional tanh (FracTanh) is another fractional generalization proposed; it is defined as where a i is a trainable parameter. The function becomes the tanh for a i = 0 and the quadratic hyperbolic secant function for a i = 1.

67 did not specified whether the parameter is trainable but explicitly uses a trainable a.

## Fractional adaptive linear unit

The fractional adaptive linear unit (FALU) is yet another AAF based on fractional calculus 68 It can be seen as the fractional generalization using the a i -th fractional derivative of the swish function: where a i and b i are trainable parameters and σ is the logistic sigmoid function. The fractional derivative is then calculated as However, as this calculation is not practical, Zamora-Esquivel, Rhodes, and Nachman use following approximation for a i ∈ and b i ∈: and a i and b i are the two previously mentioned trainable parameters. The FALU was shown to outperform ReLU, GELU, ELU, SELU, and kernel activation function (KAF) on the MNIST, CIFAR-10, ImageNet, and Fashion MNIST datasets for several tested architectures.

## Fractional leaky ReLU (FracLReLU)

The fractional LReLU (FracLReLU) is the fractional variant of the LReLU (see section 3.6.2) proposed. It is defined using fractional calculus as where a i ∈ is a fixed parameter. The fractional derivative is then calculated as

## Fractional parametric ReLU (FracPReLU)

The fractional PReLU (FracPReLU) is the fractional variant of the PReLU (see section 4.2.1) proposed. It is defined using fractional calculus as where a i ∈ is a fixed parameter and b i is a trainable parameter. The fractional derivative is then calculated as

## Fractional ELU (FracELU)

The fractional ELU (FracELU) is the fractional variant of the ELU (see section 3.6.48) proposed. It is defined using fractional calculus as where a i ∈ and b are fixed parameters. The fractional derivative is then calculated as 68 The FALU was published in without any links to even though it was proposed by the same first author and it uses the same principles.

## Fractional SiLU (FracSiLU)

The fractional SiLU (FracSiLU) is the fractional variant of the SiLU (see section 3.3) proposed. It is defined using fractional calculus as While Job et al. intended the fractional SiLU (FracSiLU) to be the fractional variant of the SiLU (see section 3.3), they used a wrong definition of the SiLU. Here we present both the FracSiLU from the and the FracSiLU that fit the definition of SiLU - the definition from will be denoted as FracSiLU variant 1 (FracSiLU1) whereas the variant we derived as FracSiLU variant 1 (FracSiLU2). The Job et al. used this definition 69 of SiLU: Then the FracSiLU1 is defined as where σ (z i) is the logistic sigmoid. The fractional derivative is then calculated as where B n is n-th Bernoulli's number.

When using the SiLU definition from section 3.3, the FracSiLU2 is then defined as Since Job et al. made no assumption about the sign of z i, the fractional derivative of FracSiLU2 is computed as where B n is n-th Bernoulli's number.

## Fractional GELU (FracGELU)

Similarly as for FracSiLU, Job et al. intended the fractional GELU (FracGELU) to be the fractional variant of the GELU (see section 3.3.1), but they used a wrong definition of the GELU. Here we present both the FracGELU from the and the FracGELU that fit the definition of GELU - the definition from will be denoted as FracGELU variant 1 (FracGELU1) whereas the variant we derived as FracGELU variant 1 (FracGELU2). The Job et al. used this definition 70 of GELU: where Φ(z) is the standard Gaussian CDF. Then the FracGELU1 is defined as The fractional derivative of FracGELU1 is then calculated as When using the GELU definition from section 3.3.1, the FracGELU2 is then defined as Since Job et al. made no assumption about the sign of z i, the fractional derivative of FracGELU2 is computed as 69 Job et al. referenced for their definition of SiLU; however, the contains the SiLU definition from section 3.3 and does not mention SiLU at all.

70 Job et al. referenced for their definition of SiLU; however, neither nor contains a definition of GELU.

## Scaled softsign

An activation function called scaled softsign is an adaptive variant of the softsign activation (see section 3.2.13) with variable amplitude. It is defined as where a i and b i are trainable parameters for each neuron i. The parameter a i controls the range of the output while the parameter b i controls the rate of transition between signs.

## Parameterized softplus (s+2L)

Parameterized softplus is an adaptive variant of a softplus activation function that allows for vertical shifts. It is defined as where a i ∈ is a trainable parameter for each neuron i. Vargas et al. also proposed a non-adaptive variant with fixed a i that is denoted as s + 2.

## Universal activation function (UAF)

The so-called universal activation function (UAF) is a softplus based AAF proposed. It is defined as where a i, b i, c i, d i, and e i are trainable parameter for each neuron i. For example, the UAF is able to well approximate the step function, logistic sigmoid, tanh, ReLU, LReLU, and Gaussian function.

## Learnable extended activation function (LEAF)

The learnable extended activation function (LEAF) is an AAF proposed in that is able to replace several existing AFs. It is defined as where σ (x) is the logistic sigmoid and a i, b i, c i, and d i are trainable parameters for each neuron i. The table 1 contains a list of AFs that are equivalent to a particular LEAF parameterization.

Table 1: AF equivalent to LEAF parameterizations The list of AFs that have an equivalent LEAF parameterization.

## Generalized ReLU (GReLU)

Theb generalized ReLU (GReLU) is an AF based on the UAF (see section 4.22). It is defined as where a i and b i are trainable parameters.

## Multiquadratic activation function (MAF)

The multiquadratic activation function (MAF) was used. It is defined as where a i and b i are trainable parameters a i is the slope coefficient and b i is the bias coefficient.

## EIS activation functions

The EIS 71 is a family of AAFs proposed in with three notable examples EIS-1, EIS-2, and EIS-3.

The general EIS is defined as where a i, b i, c i, d i, and e i are either trainable parameters or fixed hyperparameters; a i ∈, b i ∈ [0, ∞), c i ∈ [0, ∞), d i ∈ [0, ∞), e i ∈ [0, ∞) and b i, c i, and d i cannot be equal to zero at the same time.

The EIS-1 is defined as where d i and e i are trainable parameters. It can be obtained from the general EIS by setting a i = 1, b i = 0, c i = 1.

The EIS-2 is defined as where b i is a trainable parameter. It can be obtained from the general EIS by setting a i = 1, d i = 0; however, the EIS-2 from also fixes c i = 1.

And finally, the EIS-3 is defined as where d i and e i are trainable parameters; it can be obtained from the general EIS by setting a i = 0, b i = 1, c i = 0.

The EIS family contains the softplus, swish, and ISRU as special cases.

## Linear combination of parameterized softplus and ELU (ELUs+2L)

A linear combination of parameterized softplus and ELU (ELUs + 2L) is an adaptive activation function combining ELUs and parameterized softplus activation functions. It is defined as where b i is a trainable parameter for each neuron i, ELU(z i) is the ELU activation function and s + 2L(z i) is the parameterized softplus activation function. The variant with non-adaptive parameterized softplus is denoted as ELUs + 2.

## Global-local neuron (GLN)

The global-local neuron (GLN) is an AAF that is a convex combination of two AFs proposed. It is defined as where a l and b l are trainable weights for each layer l and global(z l) and local(z l) are AFs capable of identifying the global and local characteristics respectively; the authors used global(z l) sin (z l) and local(z l) = tanh(z l).

## Neuron-adaptive activation function

A similar approach to trainable amplitude and generalized hyperbolic tangent is the so-called neuron-adaptive activation function (NAF), which comprises of a linear combination of two activation functions with scalable amplitude: where a, b, c, and d are trainable parameters that are shared by the whole network. The NAF was shown to perform superiorly on a few regression tasks.

71 The EIS is a name given by Biswas et al.; it is not an abbreviation.

## Scaled logistic sigmoid

A scaling variant of logistic sigmoid called scaled logistic sigmoid was proposed. The function is defined as where a i and b i are trainable parameters for each neuron i. Note that this activation is identical to the second part of the previously proposed NAF (see section 4.28).

A variant combining scaled logistic sigmoid with scaled sine (SLS-SS) was also used; it has four trainable parameters and is defined as where a i, b i, c i, and d i are trainable parameters. This activation function is a special case of another variant of NAF: where a i, b i, c i, d i, e i and f i are trainable parameters.

## Adaptive piece-wise linear unit (APLU)

Another generalization of ReLU is the adaptive piece-wise linear unit (APLU), which uses the sum of hinge-shaped functions as the activation function. An approach extending APLU is smooth adaptive activation function (SAAF) with piece-wise polynomial form and was specifically designed for regression and allows for bias-variance trade-off using a regularization term. where S is the number of hinges, i is the number of neurons, and a s i, b s i, s ∈ 1,..., S are trainable parameters per unit. However, the optimizer might choose very large values of a s i and balance them by very small weights, which could lead to numerical instabilities; therefore, an L 2 penalty is added to the parameters a s i, b s i scaled by 0.001. Another adaptive piecewise linear function was proposed, where a weighted combination of ReLUs with additional parameters was used.

## Simple piecewise linear and adaptive function with symmetric hinges (SPLASH)

The simple piecewise linear and adaptive function with symmetric hinges (SPLASH) is an approach similar to the APLU. It is defined as where S is an odd number, b l,s and -b l,s are hinge parameters and a + l,s and a -l,s are scaling parameters for each layer l; these max functions form S +1 continuous line segments with hinges at b l,s and -b l,s. While Tavakoli, Agostinelli, and Baldi tried different values for S, they found that using S = 7 usually works well.

## Multi-bias activation (MBA)

An approach similar to APLU and paired ReLU (see section 4.2.26) termed multi-bias activation (MBA) uses the same activation but with multiple biases, which allows to learn more complex activations; in this it resembles paired ReLU as one input map leads to several output maps with activation with different biases. The weights that will be given to the output maps in the next layer are similar to the weights in the APLU; however, the MBA is able to provide cross-channel information due to multiple outputs for each activation. The MBA is defined as where b i,k, k = 1, 2,..., K are trainable biases and g (x) is any non-linear activation function; Li, Ouyang, and Wang used ReLU as the activation function g (x).

## Mexican ReLU (MeLU)

A Mexican ReLU (MeLU) is an activation function with a similar approach as the APLU, but it does not need any L 2 penalty. The MeLU is defined as where a i,j are trainable parameters for each neuron/filter i, and k is the total number of trainable parameters (k -1 for the sum and one for the PReLU), b j and c j are fixed constants that are chosen recursively (more details in); ϕ b j c j (z i) is defined as Maguolo, Nanni, and Ghidoni used k = 4 and k = 8 for their experiments; the trainable parameters a i,j were all initialized to zero which helps the training at the early stages by exploiting the properties of the ReLU (e.g., the MeLU is convex for many iterations at the beginning). The advantage of the MeLU over the APLU is that it needs only half of the parameters while retaining the same representation power when the parameters are jointly optimized with the network's weights and biases.

## Modified Mexican ReLU (MMeLU)

The modified Mexican ReLU (MMeLU) is an MeLU inspired AF proposed. It is defined as where a i, b i, and c i are adaptive parameters estimated using Bayesian procedure outlined; a i ∈, b i ∈ R +, and c i ∈ R.

## Gaussian ReLU (GaLU)

The Gaussian ReLU (GaLU) is a MeLU-inspired AAF proposed. It uses the same basic form as MeLU has in eq. but it uses following ϕ b j c j (z i): where b j and c j are similar parameters is in the original MeLU; more details about the parameters is available.

## Hard-Swish

The Hard-Swish is an adaptive variant of a scaled Hard sigmoid activation. It is defined as where b i is either trainable or fixed parameter. For b i →∞, the Hard-Swish approaches the ReLU. The Hard-Swish outperformed the logistic sigmoid, tanh, ReLU, LReLU, and swish on the MNIST dataset. The ResNet, wide residual network (WRN), and DenseNet with glshardswish outperformed their variants with ReLU and swish on the CIFAR-10 dataset.

## S-shaped rectified linear activation unit (SReLU)

A S-shaped ReLU (SReLU) consists of three piecewise linear functions that are controlled by four trainable parameters that are learned jointly with the whole network. The SReLU is able to learn both convex and non-convex functions; in particular, it is able to learn both ReLU and also sigmoidlike functions. It is similar to APLU (see section 4.29), but APLU approximates non-convex functions, and it requires the rightmost linear function to have a unit slope and bias of zero. SReLU is defined as where t r i, t l i, a r i, and a l i are trainable parameters for each neuron i (or channel i in case of convolutional neural networks). The parameters t r i and t l i determine thresholds of an interval outside which the slope of the linear parts is controlled by parameters a r i and a l i, respectively. The authors Jin et al. show that the SReLU outperformed the ReLU, LReLU, PReLU, APLU, maxout unit and plain NIN on several visual tasks. The authors also recommend to initialize the parameters of SReLU to t i ∈ R, a r i:= 1, t l i:= 0, and a l i ∈ which degenerates the SReLU into a LReLU and then keep these parameter fixed during several initial training epochs. The SReLU can be seen as a more general concept to the later proposed piecewise linear unit (PLU) (see section 4.35) and to the BLReLU (see section 3.6.24).

## N-activation

The N-activation is activation very similar to a special case of SReLU 72 proposed . The N-activation with trainable parameters a i, and b i is defined as

## ALiSA

A special case of SReLU was later proposed under the name adaptive LiSA (ALiSA); it can be obtained by setting t r i:= 1 and t l i:== 0: where a r i and a l i are adaptive parameters. Its nonadaptive variant is called simply linearized sigmoidal activation (LiSA) and has parameters a r i and a l i fixed.

## Alternated left ReLU (All-ReLU)

The alternated left ReLU (All-ReLU) was proposed in for usage in sparse neural networks. It is inspired by the SReLU. It is defined as where a is a fixed parameter controlling the slope for negative inputs, l is the number of layers, and % is the modulo operation.

## Piecewise linear unit (PLU)

A PLU resembles two earlier proposed activation functions - the SReLU (see section 4.33) and adaptive piece-wise linear unit (see section 4.29); it can be even seen as a special case of the SReLU. where a i is either a trainable parameter or a predefined constant and b is a predefined constant; a variant with a = 0. 1 and b = 1 was shown. The advantage of the PLU compared to the SReLU is that it produces an invertible function (which is not always the case for the more general SReLU).

72 It would be a special case of SReLU if the the thresholds were directly trainable and not determined using the min and max functions.

## Adaptive linear unit (AdaLU)

The adaptive linear unit (AdaLU) is yet another piecewise linear AAF. It is defined as where a i, b i, c i, d i, and e i are trainable parameters for each neuron i. The parameters a i and b i control the offsets; c i and d i control the slope of each linear part, and e i is the saturation value.

## Trapezoid-shaped activation function (TSAF)

The trapezoid-shaped activation function (TSAF) (ref. from) is an AF consisting of four ReLUs. It is defined as where a i, b i, and c i are parameters 73 such that a i < b i and c i ∈ (0, 1].

## Adaptive Richard's curve weighted activation (ARiA)

Another function motivated by the swish activation function is the Adaptive Richard's curve weighted activation (ARiA), which replaces the logistic sigmoid in the swish by Richard's curve. Richard's curve is a generalization of the logistic sigmoid that is controlled by several hyperparameters. The Richard's curve is defined as: where A is the lower asymptote, K is the upper asymptote, C is a constant (typically equal to 1), υ > 0 controls the direction of growth and B is the exponential growth rate, Q controls the initial value of the function. The ARiA is defined as where σ R (x) is the Richard's curve from eq.. As such, the ARiA has five hyperparameters controlling its behavior. To reduce the number of the hyperparameters, Adaptive Richard's curve weighted activation 2 (ARiA2) was also proposed that is defined by only two hyperparameters a and b The swish activation function is a special case of ARiA with A = 1, K = 0, B = 1, υ = 1, C = 1, and Q = a i, where a i is the parameter of the swish activation function (see section 4.4.1 for details). The ARiA2 is a special case of ARiA with K = 0, B = 1, υ = 1, C = 1 a, and Q = b, where a and b are the ARiA2 hyperparameters. Patwardhan, Ingalhalikar, and Walambe reached best accuracy on the MNIST dataset with a custom CNN using ARiA2 with a = 1. 5 and b = 2; the best parameters for the DenseNet were a = 1. 75 and b = 1. While the parameters were fixed in the experiments, they can also be trainable as is in the special case of the swish activation function.

## Modified Weibull function

A modified Weibull function (MWF) is an Weibull-function-based AF proposed. It is defined as where a i, b i, c i, and d i are trainable parameters. The parameter b i determines the location of the peak of the AF. The polynomial term dominates for small input values while the exponential starts to dominate with larger values which reduces the output value as the input value further increases.

73 Pan et al. do not state whether they are used in trainable or fixed form.

## Sincos

The sincos is another older AF proposed. It is defined as where a, b, c, and d are adaptive parameters.

## Combination of sine and logistic sigmoid (CSS)

The combination of sine and logistic sigmoid (CSS) 74 is an AAF proposed. It is defined as where a, b, c, and d are adaptive parameters.

## Catalytic activation function (CatAF)

The catalytic activation function (CatAF) is an AAF that uses sinusoidal mixing of any AF and the identity to produce the final activation. It is defined as where a i is a trainable parameter and g (z i) is any AF such as the ReLU.

## Expcos

An AAF combining an exponential function with the cosine was proposed. It is called expcos in this work 75 and is defined as where a and b are adaptive parameters.

## Multi-bin trainable linear unit (MTLU)

The multi-bin trainable linear unit (MTLU) can be seen as a conceptual extension of the SReLU (see section 4.33) into more than three segments: where a i, 0,..., a i,K, and b i, 0,..., b i,K are trainable parameters for each neuron/filter and K and c i, 0,..., c i,K -1 are predefined hyperparameters. The authors used unifromly distributed anchors c i, 0,..., c i,K -1. The main disadvantage besides the higher number of additional parameters is the higher number of non-differentiable points. The MTLU was also named continuous piecewise nonlinear activation function (CPN)m. The CPNmc is a MTLU variant with continuity constraint proposed.

An AF with the same form as the MTLU with only minor differences was proposed in under the name piecewise linear unit (PWLU); Zhu et al. also proposed its 2D extension . Unlike the MTLU, it uses a uniformly spaced demarcation points c i,k. Another PWLU variant named non-uniform piecewise linear unit (N-PWLU) allows for learnable intervals on which the function is piecewise linear, and also it leverages cumulative definition for efficient learning. Multistability analysis of such piecewise linear AFs is analyzed . An analysis of a number of regions of piecewise linear NNs is available .

74 The function was unnamed ; we used this abbreviation to distinguish it from SinSig.

75 The function was originally unnamed .

## Continuous piecewise nonlinear activation function CPN

A variant of the MTLU named CPN where the c i,k was used. It is defined as where a i, 0,..., a i,K, b i, 0,..., b i,K, c i, 0,..., d i,K -1 are trainable parameters for each neuron/filter, g (z i) is a non-linear function such as the logistic sigmoid and K and c i, 0,..., d i,K -1 are predefined hyperparameters.

Gao et al. also proposed a variant named CPNnl, which introduces a non-linear term for each small interval and does not enforce the uniform division of the activation space. It is defined as where K is the number of functions and a i,k, b i,k, and c i,k are learnable coefficients for k = 0, 1,..., K.

## Look-up table unit (LuTU)

A piecewise activation function look-up table unit (LuTU) is a learnable activation function that consists of several points defining the function; the values between the points are obtained using either linear interpolation or smoothing with single period cosine mask function. Similar adaptive activation function using linear interpolation was used. A look-up table of anchor points { a i,j, b i,j }, j = 0, 1,..., n that are uniformly spaced with step s, a i,j = a 0 + s · j, controls the shape of the activation functions. The step s, anchor points a 0, and n are predetermined hyperparameters, and therefore a i,j are predetermined values for which the output values b i,j are learnable parameters. Linear-interpolation-based function is defined as where a i,j are hyperparameters defined by the step s and initial point a 0 shared for all points and b i,j are trainable parameters for each neuron i. Wang, Liu, and Foroosh used a 0 = -12, step s = 0. 1 and n = 240 to cover the interval using 241 anchor poiints for each neuron. Therefore, for any input value between a i,j and a i,j +1, the output is linearly interpolated from b i,j and b i,j +1. However, such a definition might lead to unstable gradients; therefore, a variant of LuTU with cosine smoothing was also proposed. The smoothing function is defined as where τ is a hyperparameter controlling the period (2 τ) of the cosine function. The smoothed variant of the LuTU is then defined as where t is an integer defining the ration between τ and s. The formula in eq. can be further simplified as it is not necessary to sum over all j ∈ { 0, 1,..., n } as the smoothing function has a truncated input domain, more details.

## Maxout unit

Maxout unit returns the maximum of multiple linear functions per each unit i: where where K is the number of linear functions. The maxout unit can also be used directly on inputs of the neuron as shown in (by replacing w k i z i with x T i w k i where x i ∈ R d is the vector of individual inputs to a neuron i and w ∈ R d are trainable weights) but the equation presented here uses only the hidden state for simplicity. The advantage of maxout unit is that it is a universal approximator of a convex function; however, it cannot learn non-convex functions and introduces a high number of additional parameters per neuron. While some works show that maxout unit perform superiorly, other experiments show that ReLU, which is a special case of maxout, performs better. Furthermore, since the maxout unit is more complex than regular ReLU, the training is relatively slower.

Empirical comparison of the maxout unit with ReLU, LReLU, SELU and tanh is available ; with ReLU, tanh, sigmoid and VLReLU .

## Adaptive blending unit (ABU)

An approach mixing several activation functions was described in where ABU was introduced. The ABU is a weighted sum of several predefined activations. It is defined as where g j (z l) is an activation function from a pool of n activation functions and a j,l is a weighting parameter that is trained for each layer l and activation function g j (z l). The ABU was first proposed as a special case of a general framework called TAF already in 1997. The blending weights a j,l are initialized to 1 n but are then trained alongside the weights of the NN. Sütfeld et al. used tanh, ELU, ReLU, swish, and the identity as the pool of activation functions g j but they admit that no exhaustive search was performed to select this set and that there might be other pools that perform better. This approach was also used in where ReLU, logistic sigmoid, tanh, and softsign activation functions were used.

However, similar approach was already proposed in where Wang, Liu, and Foroosh inspired by the mixture of Gaussian unit (MoGU) (see section 4.48.10) generalized the concept to mixing several different activation functions where g j (z i) is an activation function from a pool of n activation functions, a i,j is a trainable weighting parameter of the function g j (z i) and b i,j is a trainable parameter controlling the vertical shift of the function g j (z i) for each neuron i. Furthermore, if g j (z i) already contains a way for controlling its scale or shift, the parameters a i,j and b i,j can be discarded. This approach is identical to the ABU from if b i,j = 0 and the parameters are shared by all neurons in the same layer and not learned for each neuron separately.

A very similar approach was proposed , where Manessi and Rozza use a linear combination of activation functions from a selected pool as the final activation function. The difference from the ABU is that the weights are constrained such that they sum up to 1. Manessi and Rozza uses analyses the linear combination of identity, ReLU, and tanh activation functions. Sütfeld et al. analyzed the performance of unconstrained ABUs and ABUs with various constraints such as ∑ n j =0 a j,l = 1, ∑ n j =0 | a j,l | = 1, and two approaches enforcing ∑ n j =0 a j,l = 1 and a j,l > 0 -clipping of negative values a j,l before normalization and softmax normalization. It was found that the unconstrained ABU works the best on average on the selected tasks; however, some of the constrained variants performed better than the unconstrained ABU for particular tasks.

Another variant of ABU (called by Klabjan and Harmon activation ensemble) was proposed in - the final activation is a weighted sum of activation functions; the weighting coefficients has to sum-up to 1 (similarly to). However, unlike in the work, the individual activation functions are scaled before the weighting to the interval using min-max scaling: where g j are individual activation functions, ϵ is a small number and k goes through all training samples in a minibatch.The final output is where a j,i is a weight for each neuron i and activation function j, n is the total number of the individual activation functions in the ABU; the weights a j,i ∈ are constrained such that

## Trainable compound activation function (TCA)

The trained compound activation function (TCA) is an AAF similar to the ABU and especially to its variant with the bias (see eq.); however, unlike the form from eq. it uses horizontal scaling instead of the vertical. It was defined in as where k is the number of mixed functions and a i,j and b i,j, j = 1,..., k, are scaling and translation trainable parameters for each neuron i and function j. The TCA was found to improve the performance of restricted Boltzmann machines (RBMs) and deep belief networks (DBNs).

Later, Baggenstoss introduced a TCA also with vertical scaling parameters. This slightly different variant is denoted as trained compound activation function variant 2 (TCAv2) throughout this work. TCAv2 is defined as where k is the number of mixed functions and a i,j, b i,j and c i,j, j = 1,..., k, are scaling and translation trainable parameters for each neuron i and function j.

## Average of a pool of activation functions (APAF)

An average of a pool of activation functions (APAF) was used; the output is defined as Liao used the ReLU, logistic sigmoid, tanh, and the linear functions as the candidate functions in the pool. This approach was also used.

## Gating adaptive blending unit (GABU)

Yet another approach previously proposed employs a gated linear combination of activation functions for each neuron - the variant is called gating adaptive blending unit (GABU) throughout this work. This allows each neuron to choose which activation function (from an existing pool) it may use to minimize the error. A similar method uses just binary indicators instead of the gates. The gating variant of ABU from is defined as where σ (a j,i) is the logistic sigmoid function acting as gating function and a j,i is a trainable parameter controlling the weight of the activation function g j for each neuron i.

## Deep Kronecker neural networks

The concept of ABUs was further generalized in the framework of Deep Kronecker neural networks (DKNNs), which provides an efficient way of constructing wide networks with adaptive activation functions while keeping the number of parameters low. DKNNs are equivalent to the feed-forward neural networks with an adaptive activation function f defined as where z l is a preactivation of a neuron from a layer l, a l,j and b l,j are either trainable or fixed parameters and g j, j = 1,..., n are fixed activation functions.

## Rowdy activation functions

Rowdy activation functions are a general class of activation functions that is a special case of DKNNs (see section 4.48.4). A rowdy activation function is a DKNNs with any activation function (e.g., ReLU) that is the function g 0 from eq. and n other functions that are defined as where c ≥ 1 is a fixed scaling factor and j = 1,..., n. The rowdy activation functions introduce highly fluctuating, non-monotonic terms that remove saturation regions from the output of each layer in the network similarly as does the stochastic noise.

## Self-learnable activation function (SLAF)

The SLAF can be considered to be a special case of the ABU where the function g j (z i) are increasing powers of z i: where a i,j are learnable parameters for each neuron i and k is a hyperparameter defining the number of elements in the polynomial expression. However, since the gradient is proportional to z i and its powers, Goyal, Goyal, and Lall used mean-variance normalization over the training sample to avoid exploding or vanishing gradients. A similar concept was analyzed, where it was applied to the output neuron only. A similar approach was used independently, where authors used the equivalent of SLAF with k = 6. A quadratic variant (i.e., SLAF with k = 2) was used.

## Chebyshev polynomial-based activation function (ChPAF)

A Chebyshev polynomial-based activation function (ChPAF) was proposed. The function is defined as where a j, j = 0,..., k are learnable parameters shared by a whole network, k is a fixed hyperparameter denoting the maximum order of used Chebyshev polynomials, and C j (z) is a Chebyshev polynomial of order j defined as with starting values C 0 (z) = 1 and C 1 (z) = z. Deepthi, Vikram, and Venkatappareddy used polynomials of a maximum order of 3 in their experiments. The Chebyshev activation function was found to outperform several activation functions including ReLU, ELU, mish and swish while retaining fast convergence using the CIFAR-10 dataset as shown in experiments.

## Legendre polynomial-based activation function (LPAF)

A Legendre polynomial-based activation function (LPAF) was used for the study of approximations of several nonlinearities. The activation is a linear combination of Legendre polynomials and is defined as where a j, j = 0,..., k are learnable parameters shared by a whole network, k is a fixed hyperparameter denoting the maximum order of used Legendre polynomials, and G j (z) is a Legendre polynomial of order j defined as with starting values G 0 (z) = 1 and G 1 (z) = z. The LPAF was found to outperform ELU, ReLU, LReLU, and softplus on the MNIST and Fashion MNIST datasets.

## Hermite polynomial-based activation function (HPAF)

The Hermite polynomial-based activation function (HPAF) is an AAF similar to ChPAF and LPAF but it used the Hermite polynomials instead. It is defined as where a j is a trainable parameter and H j (z) is the Hermite polynomial

## Mixture of Gaussian unit (MoGU)

The mixture of Gaussian unit (MoGU) was proposed in as a byproduct of analysis of the behavior of the LuTU unit (see section 4.46) as the shape of learned activation units with the cosine smoothing mostly composed of a few peaks and valleys. The MoGU is defined as where a i,j, σ i,j, and µ i,j are trainable parameters for each neuron i and Gaussian j from the mixture. The parameter a i,j controls the scale, σ i,j controls the standard deviation, and µ i,j controls the mean of the Gaussian j for neuron i.

## Fourier series activation

The Fourier series activation (FSA) was proposed. It is defined as where a i, b i,j, c i,j, d i are trainable parameters for each neuron i, and r is a fixed hyperparameter denoting the rank of the Fourier series; Liao used r = 5 throughout his experiments.

## Padé activation unit (PAU)

Padé activation units (PAUs) are adaptive activations based on the Padé approximant. The PAU is defined as where m and n are hyperparameters denoting the order of the polynomials and a j, j = 0,..., m and b k, k = 1,..., n are trainable parameters that are globaly shared by all units. While the Padé approximation could be used to approximate particular activation function, the parameters a j and b k are optimized freely with other weights of the neural network. This PAU variant was for reinforcement learning in where Delfosse et al. observed that rational functions might replace some of the residual blocks in ResNets. To avoid numerical instabilities, a safe PAU ensures that the polynomial in the denominator cannot be zero; it is defined as The hyperparameters were set to m = 5 and n = 4 in experiments. The notion of using rational functions in activations was further analyzed in where authors used activation function equivalent to eq. with distinct parameters for each layer to learn rational neural networks; the safe variant of PAU (eq.) was not used as it results in non-smooth activation function and expensive calculation of gradient during training. Boulle, Nakatsukasa, and Townsend used low degrees m = 3 and n = 2 in their work; this is in contrast to where rational functions of higher orders were used in a graph neural networkss.

## Randomized Padé activation unit (RPAU)

The PAU can be extended similarly as RReLU extends ReLU, resulting in randomized Padé activation unit (RPAU). Let C = { a 0,..., a m, b 0,..., b n } be coefficients of PAU activation (see section 4.49). Then an additive noise is introduced into each coefficient c j ∈ C during training for every input z k such that c j,k = c j + z j,k, where z j,k ∼ U(l j, u j), l j = (1 -a) c j and u j = (1 + a) c j. This results in RPAU: where z k is output of a unit for training input k.

## Enhanced rational activation (ERA)

The enhanced rational activation (ERA) function is very similar to the original PAU (see section 4.49); however, Trimmel et al. note similarly as Boulle, Nakatsukasa, and Townsend that the safe version of PAU is costly to compute whereas the original PAU has undefined values on poles (values of z where the denominator in PAU is equal to zero). To avoid both the poles and the use of absolute value, a modified rational function without the poles is used. The ERA is defined as where a j, j = 0,..., m, c k, and d k, k = 1,..., n are trainable parameters for each layer and ϵ > 0 is a small number helping to avoid numerical instabilities when d k are small. In practice, Trimmel et al. used ϵ = 10 -6. The ERA in eq. can be rewritten using partial fractions, which reduces the number of operations and, therefore, leads to more efficient computation. Trimmel et al. used m = 5 and n = 4 for their experiments.

## Orthogonal Padé activation unit (OPAU)

The orthogonal Padé activation unit (OPAU) is an extension of the PAU proposed. It is defined as where a j, j = 0,..., m and b k, k = 1,..., n are trainable weights, m and n are fixed parameters, and r j (z) belongs to a set of orthogonal polynomials. The sage OPAU is defined 76 as with identical parameters as the OPAU from eq.. Biswas, Banerjee, and Pandey used six bases for orthogonal polynomials - Chebyshev polynomials (two variants), Hermite polynomials (also two variants), Laguerre, and Legendre polynomials - as shown in table 2.

## Spline interpolating activation functions

More complex approaches include spline interpolating activation functions (SAFs), which facilitate the training of a wide variety of activation functions using interpolation. One common example is the cubic spline interpolation that was used . The SAFs are controlled by a vector q ∈ R k of internal parameters called knots, which are a sampling of the AF over k representative points. The output is computed using a spline interpolation using the closest knot and its p rightmost neighbors; p = 3 results in cubic interpolation. Spline-based activation functions were also used in the ExSpliNet - an interpretable approach combining neural networks and ensembles of probabilistic trees. A set of fixed but highly redundant knots for spline interpolation was used , where the authors then relied on the sparsifying effect of L 1 regularization to nullify the coefficients that are not needed. Spline flexible activation functions were used for sound synthesis . The usage of splines led to the creation of b-spline-based neural networks, e.g.,.

Similar to the SAF is the piecewise polynomial activation function (PPAF) that is also defined by a number of points where the function switches from one polynomial to another. López-Rubio et al. used zeroth-order, List of polynomial bases used in the OPAU taken. The Chebyshev polynomials and the Laguerre polynomial have recurrent definitions; whereas the Legendre and the Hermite polynomials are defined by a single expression.

76 Using notation as described in the original article by Biswas, Banerjee, and Pandey.

Table 2: Polynomial bases used in OPAU first-order, and third-order polynomials for the piecewise function; for example, zeroth-order PPAF uses step function and is defined as where m -1 is the number of controlling points q i,k of a neuron i, k ∈ { 1, 2,..., m -1 }. The position of control points is determined using the learning procedure outlined.

If there are no constrains and the AF is limited to linear splines, the AF can be also defined using one hidden layer with ReLUs: where K ∈ N and a i,k, b i,k, and c i,k are trainable parameters.

## Truncated Gaussian unit (TruG)

A truncated gaussian unit (TruG) is a unit in a probabilistic framework that is able to well approximate sigmoid, tanh, and ReLU. It is controlled by truncation points ξ 1 and ξ 2 and under the probabilistic framework described in is defined as where ϕ (x) is the probability density function (PDF) of a univariate Gaussian distribution with mean z and variance σ 2 and Φ(x) its CDF. The truncation points can be either selected manually or tuned with the rest of the weights.

## Mollified square root function (MSRF) family

Pan et al. used a smoothing approach on piecewise linear AFs to create a whole new family of AFs . The approach is based on the mollified square root function (MSRF) method. This smoothing approach was first used in and then in the SquarePlus AF , which inspired Pan et al. in the creation of the MSRF family of AFs.

For example, the absolute value | x | is not differentiable at x = 0, but it can be regularized by mollification as where ϵ is a small positive parameter and lim ϵ → 0 + | x | ϵ = | x |.

## SquarePlus

The SquarePlus is the first AF that used the mollification procedure described in section 4.55 above. It is defined as The SquarePlus is very similar to the softplus (see section 3.17) for ϵ = 4(ln) 2 and they produce identical outputs at z = 0.

## StepPlus

As the SquarePlus approximates the ReLU, the StepPlus approximates the step function (see section 3.1) similarly as the logistic sigmoid does. It is defined as The sign function is smoothed into the BipolarPlus AF

## LReLUPlus

A smoothed variant of the LReLU called LReLUPlus is defined as where | x | ϵ is the MSRF procedure described in section 4.55 and a i is a fixed or trainable parameter.

A function equivalent to the LReLUPlus was independently proposed in under the name SMU-1. The only difference was that Biswas et al. used parameter µ that is the square root of ϵ from section 4.55: ϵ = µ 2.

## vReLUPlus

The vReLUPlus is a MSRF smoothed variant of the vReLU (see section 3.6.25); it is defined as

## SoftshrinkPlus

The smoothed variant of the Softshrink (see section 3.6.23) is named SoftshrinkPlus 77 and is defined as where a is a fixed parameter similar to the original Softshrink's thresholding parameter.

## PanPlus

The MSRF procedure can be also used to smooth the pan AF (see section 3.6.26); the resulting PanPlus is defined as where a is a fixed thresholding parameter of the pan function.

## BReLUPlus

The BReLUPlus is a MSRF smoothed variant of the BReLU (see section 3.6.16) defined as 77 Pan et al. named the function STFPlus originally.

## SReLUPlus

Another smoothed AF is the SReLUPlus which is the smoothed variant of the SReLU (see section 4.33); it is defined as where a i has similar role as in the original SReLU and t i is a parameter for symmetric variant of SReLU with t i = t r i = t l i.

## HardTanhPlus

Similarly, the smoothed variant of the HardTanh (see section 3.6.18) named HardTanhPlus is defined as

## HardshrinkPlus

The smoothed variant of the Hardshrink (see section 3.6.22) is named HardshrinkPlus 78; it is defined as where a is a fixed parameter with a similar function as in the Hardshrink.

## MeLUPlus

Pan et al. also provided a smoothed variant of the MeLU (see section 4.32); however, the formula written in is not the MeLU AF but rather its single component ϕ b j c j (z i). Nevertheless, the full smoothed MeLUPlus can be obtained easily as the combination of the LReLUPlus and the smoothed ϕ Plus b j c j (z i) defined as where b j and c j are the same parameters as in the MeLU.

## TSAFPlus

The smoothed variant of the TSAF (see section 4.37) named TSAFPlus is defined as where a i, b i, and c i have a similar role as in the original TSAF.

## ELUPlus

Even the ELU (see section 3.6.48) can be mollified into a "smoothed" variant named ELUPlus. The smoothed variant is defined as where a is a fixed parameter 79 with a similar function as in the ELU.

## SwishPlus

The mollified variant of the swish (see section 4.4.1) named SwishPlus is defined using the smoothed step function instead of the logistic sigmoid; it is, therefore, defined as 78 Pan et al. named the function HTFPlus originally.

79 Pan et al. used variant with inverse parameter 1 a; we have used the same parameter variant as in the original ELU.

## MishPlus

The mollified variant of the swish (see section 3.3.29) named MishPlus is defined using the BipolarPlus and SquarePlus as

## LogishPlus

The mollified variant of the logish (see section 3.3.11) named LogishPlus is defined as

## SoftsignPlus

The mollified variant of the softsign (see section 3.2.13) named SoftsignPlus is defined as

## SignReLUPlus

Pan et al. provide a mollified version for an approximation of the SignReLU 80 (see section 3.6.32). They approximate the SignReLU as Using the approximation, they then define the SignReLUPlus as

## Complex approaches

The network in network (NIN), which uses a micro neural network as an adaptive activation function, represents a different approach. A combination of the NIN and maxout units called maxout-in-network (MIN) was shown to have good performance . A similar approach is the wide hidden expansion (WHE) layer, which is a sparselly connected layer with several activation functions that is used in place of a traditional activation function.

Adaptive activation functions called NPF that are learned nonparametrically were proposed in where a Fourier series basis expansion is used for nonparametric estimation. Only one NPF is learned per filter in CNNs while different activation is learned in each neuron of a fully connected layer; the learning is in two stages where the network is first learned with ReLUs in the convolution layers and NPF in all others and only then the network is learned with all activation functions being the NPF.

Yet another approach is learning activation functions using hypernetworks resting in hyperactivations. The hyperactivation consists of two parts - a shallow feed-forward neural network called activation network and a hypernetwork, which is a type of neural network that produces weights for another network. The hypernetwork is used for the normalization of the activation network. A single hyperactivation is learned for each layer in the neural network. A NN with a combination of more activation functions was used .

The adaptive activation function might also be trained in a semi-supervised manner.

## Variable activation function (VAF)

Similarly to NIN, the variable activation function (VAF) subnetwork approach uses simple activation functions to produce more complex behavior; the activation is replaced by a small subnetwork with one hidden layer with k neurons and only one input and one output neuron. Specifically, V AF is defined as 80 Pan et al. call it DLU throughout their work. where a l, 0, a l,j, b l,j, and c l,j, j = 1,..., k, are trainable parameters for each layer l and g(x) is an activation function such as tanh or ReLU that were used in experiments with VAF. The same concept of using subnetwork to learn the activation function was also proposed under the name of activation function unit (AFU).

## Flexible activation bag (FAB)

The flexible activation bag (FAB) is an approach similar to NIN and VAF as it uses a subnetwork to learn the AF for each layer l using a pool of K activations f k (z l, a l,k). It uses a shallow network with double head with ReLU activation in the first layer; then there are two separate heads. The first head predicts the parameters a l,k of the individual AFs f k (z l, a l,k) in the bag squashed by a sigmoid AF, then the parameters are mapped into a valid range of each of the parameters. The second head is a selective head for selecting an appropriate AF by producing a score s l,k -it can be either discrete or continuous resulting in soft or hard selection. Klopries and Schwung used five selection methods - all of the functions are used (s l,k = 1), hard selection, soft selection using logistic sigmoids, softmax selection, and Gumber-Softmax selection. The bag of activations used in the FAB consists of a constant function, linear function, exponential function, step function, ReLU, step function, sine function, tanh, logistic sigmoid, and Gaussian function (see for exact definitions with the adaptive parameters). Then the output of FAB is assembled as where s l,k are the selection scores of f k; the a l,k consists of parameters of the function f k (the used AFs have from one to three parameters) and the f k are the individual AFs from the bag of K functions.

## Dynamic parameter ReLU (DY-ReLU)

The dynamic parameter ReLU (DY-ReLU) (proposed under the name of dynamic ReLU in but that collides with previously proposed DReLUs in) is an activation function whose parameters are input dependent. The concept of DY-ReLU is similar to the WHE in and hyperactivations in as the DY-ReLU is an example of a hyperactivation. The dynamic activation function has two components - hyperfunction that computes parameters for the activation function and the activation function itself. The DY-ReLU piecewise linear function is computed as the maximum of multiple linear functions. It is defined as where K is a hyperparameter and a i,k and b i,k are coefficients determined by the hyper function θ (z) using all inputs z i. The hyperfunction θ (z) is a light-weight neural network. The parameters generated by the hyperfunction θ (z) can be different for each filter i, or they can be shared in the whole layer. The DY-ReLU can be considered as a dynamic and efficient variant of Maxout (see section 4.47).

## Random NNs with trainable activation functions

A very different approach based on adaptive activation functions is presented in where a neural network with random weights is initialized, and the weights are not trained, but the activation functions are trained instead. The activation functions in are polynomial activation functions and are trained separately for each hidden neuron with random weights first; only then the weights of the output layer are estimated. Ertu˘ grul used five different adaptive variants of activation functions: where a i and b i are trainable parameters.

## Kernel activation function (KAF)

A kernel activation function (KAF) is a non-parametric function that uses kernel expansion together with a dictionary to make the activation flexible. The KAF uses a weighted sum of kernel terms: where D is a fixed hyperparameter, a i,j are mixing coefficients and d j, j = 1,..., D are called dictionary elements and κ (z i, d j): R × R → R is 1D kernel function - Scardapane et al. consider only a i,j trainable and the dictionary elements d j are uniformly spaced around zero. This has the advantage that the resulting model is linear in its parameters and, therefore, can efficiently optimized.

The kernel function κ (z, d j) used in is the 1D Gaussian kernel defined as where γ ∈ R is a fixed parameter called the kernel bandwith. Scardapane et al. recommend setting the kernel bandwidth to where ∆ is the distance betwen the grid points as adapting γ through back-propagation did not yield any gain in accuracy. The mixing coefficients a i,j can be initialized either randomly from a normal distribution - this provided good diversity for the optimization process - or using kernel ridge regression to approximate an activation function of choice. Scardapane et al. also proposed 2D-KAF that works over all possible pairs of incoming values and uses 2D Gaussian kernel.

An extension of the KAF approach was presented in where activation function used was the sum of the KAF and RSigELU (see section 3.7.15) or KAF and RSigELUD (see section 3.7.19). Kernel methods are becoming more common in deep learning - e.g., fully kernected layers are replacing fully connected layers with a kernel-based approach .

## SAVE-inspired activation functions

Brad produced several AF that are, supposedly, motivated by human behavior . These AFs were created using the SAVE method and are mostly variations of the AFs listed above. For completeness' sake, a list of these AFs is included in our work in table 3 also with the real-life motivations listed in - however, no deeper analysis or objective evaluation of these AFs was not provided .

Table 3: SAVE-inspired activations | formula | parameters | principle from | The list of SA VE-inspired AFs.

## Conclusion

This paper provides an extensive survey of 400 neural network activation functions. Despite all its scope, it has some limitations and focuses on the largest family of real-valued activation functions categorized into two main classes: fixed activation functions and adaptive activation functions. The fixed activation functions that we also refer to as classical are predetermined mathematical functions that apply the same transformation to all inputs regardless of their values. Each neuron within a layer typically applies the same activation function to its inputs. Examples include logistic sigmoid, hyperbolic tangent, and ReLU functions. On the other hand, adaptive activation functions learn their parameters based on the input data and may thus change their shape. This feature allows for more flexibility and leads to faster convergence during training and improved performance. Examples of adaptive activation functions include PReLU, PELU, swish, and TAAF.

The profound impact of activation functions on network performance is undeniable, and the absence of a consolidated resource often results in redundant proposals and wasteful reinvention. By offering this comprehensive compilation, we aim to prevent the unnecessary duplication of established activation functions. While recognizing the limitations of our work in not conducting extensive benchmarks or in-depth analyses, we believe this exhaustive list will be a valuable reference for researchers. Even though this list will never be complete due to ongoing proposals of new activation functions, we believe it establishes a solid foundation for future research.
