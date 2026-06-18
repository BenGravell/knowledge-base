<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Activation Functions: Comparison of Trends in Practice and Research for Deep Learning

Topics include Activation functions, Deep learning, Neural networks, Survey analysis, ReLU activations, Deployment, Survey.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

This survey frames activation functions through the gap between research proposals and functions actually used in deployed deep-learning architectures. It is less exhaustive than later catalogs, but it is useful for understanding which nonlinearities had practical uptake around the early post-ReLU period.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Deep neural networks have been successfully used in diverse emerging domains to solve real world complex problems with may more deep learning (DL) architectures, being developed to date. To achieve these state-of-the-art performances, the DL architectures use activation functions (AFs), to perform diverse computations between the hidden layers and the output layers of any given DL architecture. This paper presents a survey on the existing AFs used in deep learning applications and highlights the recent trends in the use of the activation functions for deep learning applications. The novelty of this paper is that it compiles majority of the AFs used in DL and outlines the current trends in the applications and usage of these functions in practical deep learning deployments against the state-of-the-art research results. This compilation will aid in making effective decisions in the choice of the most suitable and appropriate activation function for any given application, ready for deployment. This paper is timely because most research papers on AF highlights similar works and results while this paper will be the first, to compile the trends in AF applications in practice against the research results from literature, found in deep learning research to date.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep learning algorithms are multi-level representation learning techniques that allows simple non-linear modules to transform representations from the raw input into the higher levels of abstract representations, with many of these transformations producing learned complex functions. The deep learning research was inspired by the limitations of the conventional learning algorithms especially being limited to processing data in raw form, and the human learning techniques by changing the weights of the simulated neural connections on the basis of experiences, obtained from past data.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The use of representation learning, which is the technique that allow machines to discover relationships from raw data, needed to perform certain tasks likes classification and detection. Deep learning, a subfield of machine learning, is more recently being referred to as representation learning in some literature. The direct relationships between deep learning and her associated fields can be shown using the relationship Venn diagram in Figure 1.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Over the past six decades, machine learning field, a branch of artificial intelligence started rapid expansion and research in the field gained momentum to diversify into different aspects of human existence. Machine learning is a field of study that uses the statistics and computer science principles, to create statistical models, used to perform major tasks like predictions and inference. These models are sets of mathematical relationships between the inputs and outputs of a given system. The learning process is the process of estimating the models parameters such that the model can perform the specified task. For machines, the learning process tries to give machines the ability to learn without being programmed explicitly.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The typical artificial neural networks (ANN) are biologically inspired computer programmes, designed by the inspiration of the workings of the human brain. These ANNs are called networks because they are composed of different functions, which gathers knowledge by detecting the relationships and patterns in data using past experiences known as training examples in most literature. The learned patterns in data are modified by an appropriate activation function and presented as the output of the neuron as shown in Figure 2

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The early deep learning algorithms used for recognition tasks had few layers in their entire architecture, with LeNet5, having just five layers. These network layers have witnessed depth increases since then, with AlexNet having twelve layers, VGGNet having sixteen and nineteen layers in its two variants, twenty-two layers in GoogleNet, one hundred and fifty-two layers in the largest ResNet architecture and over one thousand two hundred layers in Stochastic Depth networks, already trained successfully, with the layers still increasing to date. With the networks getting deeper, the need to understand the makeup of the hidden layers and the successive actions taking place within the layers becomes inevitable.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, the major issue of using deep neural network architectures is the difficulty of developing the algorithms to effectively learn the patterns in data and studies on these issues associated with the training of neural networks, have been a key research area to date.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To improve the performance of these learning algorithms, Turian et al., 2009 highlighted that three key areas are usually of interest namely: to improve the model, to engineer better features, and to improve inference. The use of better feature models has worked in many deep learning applications to obtain good model feature for the applications alongside the improvement of models but the key interest area lies in inference improvement of models for deep learning applications.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Several techniques for model improvement for deep learning algorithms exist in literature which include the use of batch-normalization and regularization dropout, proper initialization, good choice of activation function to mention a few. These different techniques offer one form of improvement in results or training improvement but our interest lies in the activation functions used in deep learning algorithms, their applications and the benefits of each function introduced in literature.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

A common problem for most learning based systems is, how the gradient flows within the network, owing to the fact that some gradients are sharp in specific directions and slow or even zero in some other directions thereby creating a problem for an optimal selection techniques of the learning parameters.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

The gradients contribute to the main issues of activation function outlined in most literature include the vanishing and exploding gradients among others, and to remedy these issues, an understanding of the activation functions, which is one of the parameters used in neural network computation, alongside other hyperparameters drives our interest, since these functions are important for better learning and generalisation. The hyperparameters of the neural network are variables of the networks that are set, prior to the optimisation of the network. Other examples of typical hyperparameters of the network include filter size, learning rate, strength of regularisation and position of quantisation level, with Bergstra et al. outlining that these parameters affect the overall performance of the network.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, these advances in configuration of the DL architectures brings new challenges specially to select the right activation functions to perform in different domains from object classification, segmentation, scene description, machine translation, cancer detection, weather forecast, self-driving cars and other adaptive systems to mention a few. With these challenges in mind, the comparison of the current trends in the application of AFs used in DL, portrays a gap in literature as the only similar research paper compared the AFs used in general regression and classification problems in ANNs, with the results reported in Turkish language, which makes it difficult to understand the research results by non Turkish scholars.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We summarize the trends in the application of existing AFs used in DL and highlight our findings as follows. This compilation is organized into six sections with the first four sections introducing deep learning, activation functions, the summary of AFs used in deep learning and the application trends of AFs in deep architectures respectively. Section five discusses these functions and section six provides the conclusion, alongside some future research direction.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Activation Functions", "weight": 1.0} -->

Activation functions are functions used in neural networks to computes the weighted sum of input and biases, of which is used to decide if a neuron can be fired or not. It manipulates the presented data through some gradient processing usually gradient descent and afterwards produce an output for the neural network, that contains the parameters in the data. These AFs are often referred to as a transfer function in some literature.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Activation Functions", "weight": 1.0} -->

Activation function can be either linear or non-linear depending on the function it represents, and are used to control the outputs of out neural networks, across different domains from object recognition and classification, to speech recognition, segmentation, scene understanding and description, machine translation test to speech systems, cancer detection systems, finger print detection, weather forecast, self-driving cars, and other domains to mention a few, with early research results, validating categorically that a proper choice of activation function improves results in neural network computing.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Activation Functions", "weight": 1.0} -->

For a linear model, a linear mapping of an input function to an output, as performed in the hidden layers before the final prediction of class score for each label is given by the affine transformation in most cases. The input vectors x transformation is given by

<!-- chunk {"id": "body-0019", "role": "body", "section": "Activation Functions", "weight": 1.0} -->

Furthermore, the neural networks produce linear results from the mappings from equation (1.1) and the need for the activation function arises, first to convert these linear outputs into non-linear output for further computation, especially to learn patterns in data. The output of these models are given by

<!-- chunk {"id": "body-0020", "role": "body", "section": "Activation Functions", "weight": 1.0} -->

These outputs of each layer is fed into the next subsequent layer for multilayered networks like deep neural networks until the final output is obtained, but they are linear by default. The expected output determines the type of activation function to be deployed in a given network.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Activation Functions", "weight": 1.0} -->

However, since the output are linear in nature, the nonlinear activation functions are required to convert these linear inputs to non-linear outputs. These AFs are transfer functions that are applied to the outputs of the linear models to produce the transformed non-linear outputs, ready for further processing. The non-linear output after the application of the AF is given by

<!-- chunk {"id": "body-0022", "role": "body", "section": "Activation Functions", "weight": 1.0} -->

Where $\alpha$ is the activation function.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Activation Functions", "weight": 1.0} -->

The need for these AFs include to convert the linear input signals and models into non-linear output signals, which aids the learning of high order polynomials beyond one degree for deeper networks. A special property of the non-linear activation functions is that they are differentiable else they cannot work during backpropagation of the deep neural networks.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Activation Functions", "weight": 1.0} -->

The deep neural network is a neural network with multiple hidden layers and output layer. An understanding of the makeup of the multiple hidden layers and output layer is our interest. A typical block diagram of a deep learning model is shown in Figure 3, which shows the three layers that make up a DL based system with some emphasis on the positions of activation functions, represented by the dark shaded region in the respective blocks.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Activation Functions", "weight": 1.0} -->

The input layer accepts the data for training the neural network which comes in various formats from images, videos, texts, speech, sounds, or numeric data, while the hidden layers are made up of mostly the convolutional and pooling layers, of which the convolutional layers detect the local the patterns and features in data from the previous layers, presented in array-like forms for images while the pooling layers semantically merges similar features into one. The output layer presents the network results which are often controlled by AFs, specially to perform classifications or predictions, with associated probabilities.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Activation Functions", "weight": 1.0} -->

The position of an AF in a network structure depends on its function in the network thus when the AF is placed after the hidden layers, it converts the learned linear mappings into non-linear forms for propagation while in the output layer, it performs predictions.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Activation Functions", "weight": 1.0} -->

The deep architectures are composed of several processing layers with each, involving both linear and non-linear operations, that are learned together to solve a given task. These deeper networks come with better performances though common issues likes vanishing gradients and exploding gradient arises, as a result of the derivative terms which are usually less than 1. With successive multiplication of this derivative terms, the value becomes smaller and smaller and tends to zero, thus the gradient vanishes. Consequently, if the values are greater than 1, successive multiplication will increase the values and the gradient tends to infinity thereby exploding the gradient. Thus, the AFs maintains the values of these gradients to specific limits. These are achieved using different mathematical functions and some of the early proposals of activation functions, used for neural network computing were explored by Elliott, 1993 as he studied the usage of the AFs in neural network.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Activation Functions", "weight": 1.0} -->

The compilation of the existing activation functions is outlined with the advantages offered by most of the respective functions as highlighted by the authors as found in the literature.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Summary of Activation Functions", "weight": 1.0} -->

This section highlights the different types of AFs and their evolution over the years. The AF research and applications in deep architectures, used in different applications has been a core research field to date. The state-of -the -art research results are outlined as follows though, It is worthy to state categorically that this summary of the AFs are not reported in chronological order but arranged with the main functions first, and their improvements following as their variants.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Sigmoid Function", "weight": 1.0} -->

The Sigmoid AF is sometimes referred to as the logistic function or squashing function in some literature. The Sigmoid function research results have produced three variants of the sigmoid AF, which are used in DL applications. The Sigmoid is a non-linear AF used mostly in feedforward neural networks. It is a bounded differentiable real function, defined for real input values, with positive derivatives everywhere and some degree of smoothness. The Sigmoid function is given by the relationship

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Sigmoid Function", "weight": 1.0} -->

The sigmoid function appears in the output layers of the DL architectures, and they are used for predicting probability based output and has been applied successfully in binary classification problems, modeling logistic regression tasks as well as other neural network domains, with Neal highlighting the main advantages of the sigmoid functions as, being easy to understand and are used mostly in shallow networks. Moreover, Glorot and Bengio, 2010 suggesting that the Sigmoid AF should be avoided when initializing the neural network from small random weights.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Sigmoid Function", "weight": 1.0} -->

However, the Sigmoid AF suffers major drawbacks which include sharp damp gradients during backpropagation from deeper hidden layers to the input layers, gradient saturation, slow convergence and non-zero centred output thereby causing the gradient updates to propagate in different directions. Other forms of AF including the hyperbolic tangent function was proposed to remedy some of these drawbacks suffered by the Sigmoid AF.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A1 Hard Sigmoid Function", "weight": 1.0} -->

The hard sigmoid activation is another variant of the sigmoid activation function and this function is given by

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A1 Hard Sigmoid Function", "weight": 1.0} -->

The equation(1.5) can be re-written in the form

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A1 Hard Sigmoid Function", "weight": 1.0} -->

A comparison of the hard sigmoid with the soft sigmoid shows that the hard sigmoid offer lesser computation cost when implemented both in a specialized hardware or software form as outlined, and the authors highlighted that it showed some promising results on DL based binary classification tasks.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A2 Sigmoid-Weighted Linear Units (SiLU)", "weight": 1.0} -->

The Sigmoid-Weighted Linear Units is a reinforcement learning based approximation function. The SiLU was proposed by Elfwing et al., 2017 and the SiLU function is computed as Sigmoid multiplied by its input. The AF $a_{k}$ of a SiLU is given by

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A2 Sigmoid-Weighted Linear Units (SiLU)", "weight": 1.0} -->

where s = input vector, $z_{k}$= input to hidden units k. The input to the hidden layers is given by

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-A2 Sigmoid-Weighted Linear Units (SiLU)", "weight": 1.0} -->

Where $b_{k}$ is the bias and $w_{ik}$ is the weight connecting to the hidden units k respectively.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-A2 Sigmoid-Weighted Linear Units (SiLU)", "weight": 1.0} -->

The SiLU function can only be used in the hidden layers of the deep neural networks and only for reinforcement learning based systems. The authors also reported that the SiLU outperformed the ReLU function as seen in the response in Figure 4 ‣ III-A Sigmoid Function ‣ III Summary of Activation Functions ‣ Activation Functions: Comparison of Trends in Practice and Research for Deep Learning").

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-A3 Derivative of Sigmoid-Weighted Linear Units (dSiLU)", "weight": 1.0} -->

The derivative of the Sigmoid-Weighted Linear Units is the gradient of the SiLU function and referred to as dSiLU. The dSiLU is used for gradient-descent learning updates for the neural network weight parameters, and the dSiLU is given by

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-A3 Derivative of Sigmoid-Weighted Linear Units (dSiLU)", "weight": 1.0} -->

The dSiLU function response looks like an overshooting Sigmoid function as shown in Figure 4 ‣ III-A Sigmoid Function ‣ III Summary of Activation Functions ‣ Activation Functions: Comparison of Trends in Practice and Research for Deep Learning"). The authors highlighted that the dSiLU outperformed the standard Sigmoid function significantly.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-B Hyperbolic Tangent Function (Tanh)", "weight": 1.0} -->

The hyperbolic tangent function is another type of AF used in DL and it has some variants used in DL applications. The hyperbolic tangent function known as tanh function, is a smoother zero-centred function whose range lies between -1 to 1, thus the output of the tanh function is given by

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-B Hyperbolic Tangent Function (Tanh)", "weight": 1.0} -->

The tanh function became the preferred function compared to the sigmoid function in that it gives better training performance for multi-layer neural networks. However, the tanh function could not solve the vanishing gradient problem suffered by the sigmoid functions as well. The main advantage provided by the function is that it produces zero centred output thereby aiding the back-propagation process.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-B Hyperbolic Tangent Function (Tanh)", "weight": 1.0} -->

A property of the tanh function is that it can only attain a gradient of 1, only when the value of the input is 0, that is when x is zero. This makes the tanh function produce some dead neurons during computation. The dead neuron is a condition where the activation weight, rarely used as a result of zero gradient. This limitation of the tanh function spurred further research in activation functions to resolve the problem, and it birthed the rectified linear unit (ReLU) activation function.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-B Hyperbolic Tangent Function (Tanh)", "weight": 1.0} -->

The tanh functions have been used mostly in recurrent neural networks for natural language processing and speech recognition tasks.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-B1 Hard Hyperbolic Function", "weight": 1.0} -->

The hard hyperbolic function known as the Hardtanh function is another variant of the tanh activation function used in deep learning applications. The Hardtanh represents a cheaper and more computational efficient version of tanh. The Hardtanh function lies within the range of -1 to 1 and it is given by

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-B1 Hard Hyperbolic Function", "weight": 1.0} -->

The hardtanh function has been applied successfully in natural language processing, with the authors reporting that it provided both speed and accuracy improvements.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-C Softmax Function", "weight": 1.0} -->

The Softmax function is another types of activation function used in neural computing. It is used to compute probability distribution from a vector of real numbers. The Softmax function produces an output which is a range of values between 0 and 1, with the sum of the probabilities been equal to 1. The Softmax function is computed using the relationship

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-C Softmax Function", "weight": 1.0} -->

The Softmax function is used in multi-class models where it returns probabilities of each class, with the target class having the highest probability. The Softmax function mostly appears in almost all the output layers of the deep learning architectures, where they are used.

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-C Softmax Function", "weight": 1.0} -->

The main difference between the Sigmoid and Softmax AF is that the Sigmoid is used in binary classification while the Softmax is used for multivariate classification tasks.

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-D Softsign", "weight": 1.0} -->

The Softsign is another type of AF that is used in neural network computing. The Softsign function was introduced by Turian et al., 2009 and the Softsign is another non-linear AF used in DL applications. The Softsign function is a quadratic polynomial, given by

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-D Softsign", "weight": 1.0} -->

Where $|x|$ = absolute value of the input.

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-D Softsign", "weight": 1.0} -->

The main difference between the Softsign function and the tanh function is that the Softsign converges in polynomial form unlike the tanh function which converges exponentially.

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-D Softsign", "weight": 1.0} -->

The Softsign has been used mostly in regression computation problems but has also been applied to DL based test to speech systems, with the authors reporting some promising results using the Softsign function.

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-E Rectified Linear Unit (ReLU) Function", "weight": 1.0} -->

The rectified linear unit (ReLU) activation function was proposed by Nair and Hinton 2010, and ever since, has been the most widely used activation function for deep learning applications with state-of-the-art results to date. The ReLU is a faster learning AF, which has proved to be the most successful and widely used function. It offers the better performance and generalization in deep learning compared to the Sigmoid and tanh activation functions. The ReLU represents a nearly linear function and therefore preserves the properties of linear models that made them easy to optimize, with gradient-descent methods.

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-E Rectified Linear Unit (ReLU) Function", "weight": 1.0} -->

The ReLU activation function performs a threshold operation to each input element where values less than zero are set to zero thus the ReLU is given by

<!-- chunk {"id": "body-0057", "role": "body", "section": "III-E Rectified Linear Unit (ReLU) Function", "weight": 1.0} -->

This function rectifies the values of the inputs less than zero thereby forcing them to zero and eliminating the vanishing gradient problem observed in the earlier types of activation function. The ReLU function has been used within the hidden units of the deep neural networks with another AF, used in the output layers of the network with typical examples found in object classification and speech recognition applications.

<!-- chunk {"id": "body-0058", "role": "body", "section": "III-E Rectified Linear Unit (ReLU) Function", "weight": 1.0} -->

The main advantage of using the rectified linear units in computation is that, they guarantee faster computation since it does not compute exponentials and divisions, with overall speed of computation enhanced. Another property of the ReLU is that it introduces sparsity in the hidden units as it squishes the values between zero to maximum. However, the ReLU has a limitation that it easily overfits compared to the sigmoid function although the dropout technique has been adopted to reduce the effect of overfitting of ReLUs and the rectified networks improved performances of the deep neural networks.

<!-- chunk {"id": "body-0059", "role": "body", "section": "III-E Rectified Linear Unit (ReLU) Function", "weight": 1.0} -->

The ReLU and its variants have been used in different architectures of deep learning, which include the restricted Boltzmann machines and the convolutional neural network architectures, although outlined that the ReLU has been used in numerous architectures because of its simplicity and reliability.

<!-- chunk {"id": "body-0060", "role": "body", "section": "III-E Rectified Linear Unit (ReLU) Function", "weight": 1.0} -->

The ReLU has a significant limitation that it is sometimes fragile during training thereby causing some of the gradients to die. This leads to some neurons being dead as well, thereby causing the weight updates not to activate in future data points, thereby hindering learning as dead neurons gives zero activation. To resolve the dead neuron issues, the leaky ReLU was proposed.

<!-- chunk {"id": "body-0061", "role": "body", "section": "III-E1 Leaky ReLU (LReLU)", "weight": 1.0} -->

The leaky ReLU, proposed in 2013 as an AF that introduce some small negative slope to the ReLU to sustain and keep the weight updates alive during the entire propagation process. The alpha parameter was introduced as a solution to the ReLUs dead neuron problems such that the gradients will not be zero at any time during training. The LReLU computes the gradient with a very small constant value for the negative gradient $\alpha$ in the range of 0.01 thus the LReLU AF is computed as

<!-- chunk {"id": "body-0062", "role": "body", "section": "III-E1 Leaky ReLU (LReLU)", "weight": 1.0} -->

The LReLU has an identical result when compared to the standard ReLU with an exception that it has non-zero gradients over the entire duration thereby suggesting that there no significant result improvement except in sparsity and dispersion when compared to the standard ReLU and tanh functions. The LReLU was tested on automatic speech recognition dataset.

<!-- chunk {"id": "body-0063", "role": "body", "section": "III-E2 Parametric Rectified Linear Units (PReLU)", "weight": 1.0} -->

The parametric ReLU known as PReLU is another variant of the ReLU AF proposed by He et al., 2015, and the PReLU has the negative part of the function, being adaptively learned while the positive part is linear. The PReLU is given by

<!-- chunk {"id": "body-0064", "role": "body", "section": "III-E2 Parametric Rectified Linear Units (PReLU)", "weight": 1.0} -->

Where $a_{i}$ is the negative slope controlling parameter and its learnable during training with back-propagation. If the term $a_{i} = \;0$ the PReLU becomes ReLU.

<!-- chunk {"id": "body-0065", "role": "body", "section": "III-E2 Parametric Rectified Linear Units (PReLU)", "weight": 1.0} -->

The PReLU can be written in compact form as

<!-- chunk {"id": "body-0066", "role": "body", "section": "III-E2 Parametric Rectified Linear Units (PReLU)", "weight": 1.0} -->

The authors reported that the performance of PReLU was better than ReLU in large scale image recognition and these results from the PReLU was the first to surpass human-level performance on visual recognition challenge.

<!-- chunk {"id": "body-0067", "role": "body", "section": "III-E3 Randomized Leaky ReLU (RReLU)", "weight": 1.0} -->

The randomized leaky ReLU is a dynamic variant of leaky ReLU where a random number sampled from a uniform distribution $U(l,u)$ is used to train the network. The randomized ReLU is given by

<!-- chunk {"id": "body-0068", "role": "body", "section": "III-E3 Randomized Leaky ReLU (RReLU)", "weight": 1.0} -->

The test phase uses an averaging technique of all $a_{ji}$ as in the training, without the dropout used in the learned parameter to a deterministic value, obtained as ${a_{ji} = \frac{l + u}{2}}.$ Thus, the real test output is obtained using the following relationship.

<!-- chunk {"id": "body-0069", "role": "body", "section": "III-E3 Randomized Leaky ReLU (RReLU)", "weight": 1.0} -->

The RReLU has been tested on standard classification datasets and compared against the other variants of the ReLU AF and Xu et al., 2015 validated that LReLU, RReLU and PReLU performs better than the ReLU on classification tasks.

<!-- chunk {"id": "body-0070", "role": "body", "section": "III-E4 S-shaped ReLU (SReLU)", "weight": 1.0} -->

The S-shaped ReLU is another variant of the ReLU AF used to learn both convex and non-convex functions, inspired by the laws of neural sciences and psychophysics. This SReLU AF was proposed by Jin et al., 2015, and it consists of three-piece wise linear functions, formulated by four learnable parameters, which are learned during training of the deep neural network using backpropagation.

<!-- chunk {"id": "body-0071", "role": "body", "section": "III-E4 S-shaped ReLU (SReLU)", "weight": 1.0} -->

The SReLU is defined by the following mapping relationship

<!-- chunk {"id": "body-0072", "role": "body", "section": "III-E4 S-shaped ReLU (SReLU)", "weight": 1.0} -->

${where{}_{}^{}},{{}_{}^{}and{}_{}^{}}$ are learnable parameters of the network and $i$indicates that the SReLU can vary in different channels. The parameter ${}_{}^{}$ represents slope of the right line with input above the set threshold ${}_{}^{}$ and ${}_{}^{}$ are thresholds in positive and negative directions respectively.

<!-- chunk {"id": "body-0073", "role": "body", "section": "III-E4 S-shaped ReLU (SReLU)", "weight": 1.0} -->

The authors highlighted that SReLU was tested on some of the award-winning CNN architectures, the Network in Network architecture alongside GoogLeNet, for on image recognition tasks specifically CIFAR-10, ImageNet, and MNIST standard datasets, and it showed improved results, compared to the other AFs.

<!-- chunk {"id": "body-0074", "role": "body", "section": "III-F Softplus Function", "weight": 1.0} -->

The Softplus AF is a smooth version of the ReLU function which has smoothing and nonzero gradient properties, thereby enhancing the stabilization and performance of deep neural network designed with softplus units.

<!-- chunk {"id": "body-0075", "role": "body", "section": "III-F Softplus Function", "weight": 1.0} -->

The Softplus was proposed by Dugas et al., 2001, and the Softplus function is a primitive of the sigmoid function, given by the relationship

<!-- chunk {"id": "body-0076", "role": "body", "section": "III-F Softplus Function", "weight": 1.0} -->

The Softplus function has been applied in statistical applications mostly however, a comparison of the Softplus function with the ReLU and Sigmoid functions by Zheng et al., 2015, showed an improved performance with lesser epochs to convergence during training, using the Softplus function.

<!-- chunk {"id": "body-0077", "role": "body", "section": "III-F Softplus Function", "weight": 1.0} -->

The Softplus has been used in speech recognition systems, of which the ReLU and sigmoid functions have been the dominant AFs, used to achieve auto speech recognition.

<!-- chunk {"id": "body-0078", "role": "body", "section": "III-G Exponential Linear Units (ELUs)", "weight": 1.0} -->

The exponential linear units (ELUs) is another type of AF proposed by Clevert et al., 2015, and they are used to speed up the training of deep neural networks. The main advantage of the ELUs is that they can alleviate the vanishing gradient problem by using identity for positive values and also improves the learning characteristics. They have negative values which allows for pushing of mean unit activation closer to zero thereby reducing computational complexity thereby improving learning speed. The ELU represents a good alternative to the ReLU as it decreases bias shifts by pushing mean activation towards zero during training.

<!-- chunk {"id": "body-0079", "role": "body", "section": "III-G Exponential Linear Units (ELUs)", "weight": 1.0} -->

The exponential linear unit (ELU) is given by

<!-- chunk {"id": "body-0080", "role": "body", "section": "III-G Exponential Linear Units (ELUs)", "weight": 1.0} -->

The derivative or gradient of the ELU equation is given as

<!-- chunk {"id": "body-0081", "role": "body", "section": "III-G Exponential Linear Units (ELUs)", "weight": 1.0} -->

Where $\alpha$= ELU hyperparameter that controls the saturation point for negative net inputs which is usually set to 1.0

<!-- chunk {"id": "body-0082", "role": "body", "section": "III-G Exponential Linear Units (ELUs)", "weight": 1.0} -->

The ELUs has a clear saturation plateau in it negative regime thereby learning more robust representations, and they offer faster learning and better generalisation compared to the ReLU and LReLU with specific network structure especially above five layers and guarantees state-of-the-art results compared to ReLU variants. However, a critical limitation of the ELU is that the ELU does not centre the values at zero, and the parametric ELU was proposed to address this issue.

<!-- chunk {"id": "body-0083", "role": "body", "section": "III-G1 Parametric Exponential Linear Unit (PELU)", "weight": 1.0} -->

The parametric ELU is another parameterized version of the exponential linear unit (ELUs), which tries to address the zero centre issue found in the ELUs. The PELU was proposed by Trottier et al., 2017, and it uses the PELU in the context of vanishing gradient to provide some gradient-based optimization framework used to reduce bias shifts while maintaining the zero centre of values.

<!-- chunk {"id": "body-0084", "role": "body", "section": "III-G1 Parametric Exponential Linear Unit (PELU)", "weight": 1.0} -->

The PELU has two additional parameters compared to the ELU and the modified ELU is given by

<!-- chunk {"id": "body-0085", "role": "body", "section": "III-G1 Parametric Exponential Linear Unit (PELU)", "weight": 1.0} -->

Where a, b, and c \> 0 and c causes a change in the slope in the positive quadrant, b controls the scale of the exponential decay, and $\alpha$ controls the saturation in the negative quadrant.

<!-- chunk {"id": "body-0086", "role": "body", "section": "III-G1 Parametric Exponential Linear Unit (PELU)", "weight": 1.0} -->

Solving the equation of the modified ELU by constraining the projection during training given the parametric ELU which is given by the relationship

<!-- chunk {"id": "body-0087", "role": "body", "section": "III-G1 Parametric Exponential Linear Unit (PELU)", "weight": 1.0} -->

${when\alphaandb} > \;0$. In compact form, the PELU is given by

<!-- chunk {"id": "body-0088", "role": "body", "section": "III-G1 Parametric Exponential Linear Unit (PELU)", "weight": 1.0} -->

Thus, setting the values of a, b, and c = 1 recovers the original ELU activation function.

<!-- chunk {"id": "body-0089", "role": "body", "section": "III-G1 Parametric Exponential Linear Unit (PELU)", "weight": 1.0} -->

The PELU promises to be a good option for applications that requires less bias shifts and vanishing gradients like the CNNs.

<!-- chunk {"id": "body-0090", "role": "body", "section": "III-G2 Scaled Exponential Linear Units (SELU)", "weight": 1.0} -->

The scaled exponential linear units(SELU) is another variant of the ELUs, proposed by Klambauer et al., 2017. The SELU was introduced as a self-normalising neural network that has a peculiar property of inducing self-normalising properties. It has a close to zero mean and unit variance that converges towards zero mean and unit variance when propagated through multiple layers during network training, thereby making it suitable for deep learning application, and with strong regularisation, learns robust features efficiently.

<!-- chunk {"id": "body-0091", "role": "body", "section": "III-G2 Scaled Exponential Linear Units (SELU)", "weight": 1.0} -->

Where $\tau$ is the scale factor. The approximate values of the parameters of the SELU function are ${\alpha \approx {\;1.6733and\lambda} \approx \;1.0507}.$

<!-- chunk {"id": "body-0092", "role": "body", "section": "III-G2 Scaled Exponential Linear Units (SELU)", "weight": 1.0} -->

The SELUs are not affected by vanishing and exploding gradient problems and the authors have reported that they allow the construction of mappings with properties leading to self normalizing neural networks which cannot be derived using ReLU, scaled ReLU, sigmoid, LReLU and even tanh functions.

<!-- chunk {"id": "body-0093", "role": "body", "section": "III-G2 Scaled Exponential Linear Units (SELU)", "weight": 1.0} -->

The SELU has been applied successfully to classification tasks alongside some deep genetic mutation computation.

<!-- chunk {"id": "body-0094", "role": "body", "section": "III-H Maxout Function", "weight": 1.0} -->

The Maxout AF is a function where non-linearity is applied as a dot product between the weights of a neural network and data. The Maxout, proposed by Goodfellow et al., 2013, generalizes the leaky ReLU and ReLU where the neuron inherits the properties of ReLU and leaky ReLU where no dying neurons or saturation exist in the network computation. The Maxout function is given by

<!-- chunk {"id": "body-0095", "role": "body", "section": "III-H Maxout Function", "weight": 1.0} -->

The Maxout function has been tested successfully in phone recognition applications.

<!-- chunk {"id": "body-0096", "role": "body", "section": "III-H Maxout Function", "weight": 1.0} -->

The major drawback of the Maxout function is that it is computationally expensive as it doubles the parameters used in all neurons thereby increasing the number of parameters to compute by the network.

<!-- chunk {"id": "body-0097", "role": "body", "section": "III-I Swish Function", "weight": 1.0} -->

The Swish AF is one of the first compound AF proposed by the combination of the sigmoid AF and the input function, to achieve a hybrid AF. The Swish activation was proposed by Ramachandran et al., 2017, and it uses the reinforcement learning based automatic search technique to compute the function. The properties of the Swish function include smoothness, non-monotonic, bounded below and unbounded in the upper limits. The smoothness property makes the Swish function produce better optimization and generalization results when used in training deep learning architectures.

<!-- chunk {"id": "body-0098", "role": "body", "section": "III-I Swish Function", "weight": 1.0} -->

The authors highlighted that the main advantages of the Swish function is the simplicity and improved accuracy as the Swish does not suffer vanishing gradient problems but provides good information propagation during training and reported that the Swish AF outperformed the ReLU activation function on deep learning classification tasks.

<!-- chunk {"id": "body-0099", "role": "body", "section": "III-J ELiSH", "weight": 1.0} -->

The Exponential linear Squashing AF known as the ELiSH function is one of the most recent AF, proposed by Basirat and Roth, 2018. The ELiSH shares common properties with the Swish function. The ELiSH function is made up of the ELU and Sigmoid functions and it is given by

<!-- chunk {"id": "body-0100", "role": "body", "section": "III-J ELiSH", "weight": 1.0} -->

The properties of the ELiSH function varies in both the negative and positive parts as defined by the limits. The Sigmoid part of the ELiSH function improves information flow while the Linear parts eliminates the vanishing gradient issues. The ELiSH function has been applied successfully on ImageNet dataset using different deep convolutional architectures.

<!-- chunk {"id": "body-0101", "role": "body", "section": "III-J1 HardELiSH", "weight": 1.0} -->

The HardELiSH is the hard variant of the ELiSH activation function. The HardELiSH is a multiplication of the HardSigmoid and ELU in the negative part and a multiplication of the Linear and the HardSigmoid in the positive part. The HardELiSH is given by

<!-- chunk {"id": "body-0102", "role": "body", "section": "III-J1 HardELiSH", "weight": 1.0} -->

The HardELiSH function was tested on ImageNet classification dataset.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Comparison of the Trends in Activation Functions Used in Deep Learning Architectures", "weight": 1.0} -->

The search for the AFs are based on the published research results of the winners of ImageNet Image Large Scale Visual recognition Challenge (ILSVRC) competitions alongside some cited research output from the AF research results found in literature. The ImageNet competition was chosen for trend comparison because it is the competition that produced the first deep learning success. These forms the core basis for both the search of the functions outlined in this paper and the current trends in the use of AFs, although the scope of the trends goes beyond image recognition as other applications that birthed new DL AFs were included like the natural language processing

<!-- chunk {"id": "body-0104", "role": "body", "section": "Comparison of the Trends in Activation Functions Used in Deep Learning Architectures", "weight": 1.0} -->

The Image Large Scale Visual Recognition Challenge (ILSVRC) also known as ImageNet is a database of images used for visual recognition competitions. The ImageNet competition is an annual competition where researchers and their teams evaluate developed algorithms on specific datasets, to review improvements in achieved accuracy in visual recognition challenges.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Comparison of the Trends in Activation Functions Used in Deep Learning Architectures", "weight": 1.0} -->

The deep learning architectures are the architectures that has more than one hidden layer, often referred to as multilayer perceptron. These architectures are numerous which include deep feedforward neural networks, convolutional neural networks, long short term memory, recurrent neural networks and the deep generative models like deep Boltzmann machines, deep belief networks, generative adversarial networks and so. The use of the architectures of DL includes to learn patterns in data, map some input function to outputs and many more, and these can only be achieved with specialized architectures.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Comparison of the Trends in Activation Functions Used in Deep Learning Architectures", "weight": 1.0} -->

The AFs used in DL architectures dates back from the beginning of the adoption of the deeper architectures for neural network computations. Prior to 2012, image recognition challenges used shallow architectures and had few AFs embedded in them. The adoption of the deeper architectures for neural computing was first explored by Krizhevsky et al., 2012 in the Image Large Scale Visual Recognition Challenge (ILSVRC), which is an annual event that started in 2010. Since then, the use of the deeper architectures has witnessed huge research advances in optimization techniques for training the deeper architectures, since the deeper the network, the more difficult to train and optimize, though the better the performance guarantee.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Comparison of the Trends in Activation Functions Used in Deep Learning Architectures", "weight": 1.0} -->

The AF is a key component for training and optimization of neural networks, implemented on different layers of DL architectures, is used across domains including natural language processing, object detection, classification and segmentation etc.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Comparison of the Trends in Activation Functions Used in Deep Learning Architectures", "weight": 1.0} -->

The trends of DL architectures that emerged as the winning architectures of ImageNet competition and other remarkable architectures include: AlexNet; winner of ILSVRC 2012, ZFNet; the 2013 ILSVRC competition winner, NiN; the Network in Network architecture, GoogleNet; the winner of 2015 ILSVRC classification challenge, and architectures which emerged as second in classification, winner in localization tasks in 2015 ILSVRC, Network in Network(NiN), ResNet; the 2016 winner of both the ILSVRC & COCO competitions, Squeeze and Excitation Network(SeNet); the latest winner of the ILSVRC 2017 competition alongside SegNet, DenseNet, FractalNet, ResNeXt architecture, and the modified networks like SqueezeNet architectures, which had multiple AFs embedded in it.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Comparison of the Trends in Activation Functions Used in Deep Learning Architectures", "weight": 1.0} -->

The Table I highlights some of the state-of-the-art architectures of deep neural networks that emerged as a significant improvement to the existing architectures, used for large scale image recognition challenge (ILSVRC), showing the positions of the activation functions used in those architectures.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Comparison of the Trends in Activation Functions Used in Deep Learning Architectures", "weight": 1.0} -->

The AFs used in more recent DL architectures have the ReLU activation function embedded in them which include the DenseNet, MobileNets, a mobile version of the convolutional networks, ResNeXt as well as the softmax function used in FractalNet, and many some other architectures.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Comparison of the Trends in Activation Functions Used in Deep Learning Architectures", "weight": 1.0} -->

From Table Iabove, it is evident that the ReLU and the Softmax activation functions are the dormant AFs used in practical DL applications. Furthermore, the Softmax function is used in the output layer of most common practice DL applications however, the most recent DL architecture used the sigmoid function to achieve it prediction at the output layer, while the ReLU units are used in the hidden layers.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Comparison of the Trends in Activation Functions Used in Deep Learning Architectures", "weight": 1.0} -->

In choosing the state-o-the-art architecture for recognition tasks, it is handy from Table I to select the current and most recent architecture and understand the architectural make-up of the network. The SeNet architecture is the current state-of-the-art architecture for recognition tasks as found in literature.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Comparison of the Trends in Activation Functions Used in Deep Learning Architectures", "weight": 1.0} -->

A summary table of all the discussed AFs used in DL is shown in Table II, with their respective equations, used in computation of these AFs.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Discussions", "weight": 1.0} -->

We have identified the key AFs used in deep learning applications and from the literature, we have outlined that there are four variants of the rectified linear units (ReLU), apart from the original ReLU. Furthermore, the Sigmoid has three variants, two variants for the exponential linear units(ELU) functions, with the Hyperbolic tangent and ELiSH functions having their respective hard versions as their only variants. The Softmax, Softsign, Softplus, Maxout and Swish functions has no variants.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Discussions", "weight": 1.0} -->

The summary of the various AFs include the Sigmoid with HardSigmoid, SiLU and dSiLU variants, the ELU having the PELU and SELU as its variants, the ReLU with LReLU, PReLU, RReLU and SReLU as its variants.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Discussions", "weight": 1.0} -->

Perhaps, the DL architectures have multiple AFs embedded to every given network and it is noteworthy to highlight that these multiple AFs are used at different layers, to perform gradient computations in a single network, thereby obtaining an effective learning and characterisation of the presented inputs.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Discussions", "weight": 1.0} -->

The linear units of AF are the most studied types of AF with the rectified and exponential variants, providing eight different variants of activation functions, used in DL applications and these eight linear variants include ReLU, LReLU, PReLU, RReLU, SReLU, ELU, PELU and SELU.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Discussions", "weight": 1.0} -->

A summary of the AFs used across various domains is shown in Table 2 alongside the formulae for the computation of these AFs, used in DL applications.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Discussions", "weight": 1.0} -->

The ELU's has been highlighted as a faster learning AF compared to their ReLU counterpart, and this assertion has been validated by Pedamonti, 2018, after an extensive comparison of some variants of the ELU and ReLU AF on the MNIST recognition dataset.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Discussions", "weight": 1.0} -->

The PELU and PReLU are two different parametric AFs which are developed using exponential and linear units but both have learnable parameters. It is also evident that there are other AFs that performs better than the ReLU, which has been the most consistent AF for DL applications since invention. Xu et al., 2015 validated that the other variants of the ReLU, including LRELU, PReLU and RReLU performs better than the ReLU but some of these functions lack theoretical justifications to support their state-of-the-art results.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Discussions", "weight": 1.0} -->

Furthermore, the parametric AFs have been a development in emerging applications where the AF was used as a learnable parameter from the dataset, thus looks to be a promising approach in the new functions developed most recently as observed in SReLU, PELU and PReLU.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Discussions", "weight": 1.0} -->

Apart from the ReLU and SiLU AFs that were developed on restricted Boltzmann machines, and LReLU developed with neural network acoustic models, almost all the other AFs were developed on convolutional neural networks and tested on classification datasets. This further demonstrated that deep learning tasks are thriving mostly in classification tasks, using convolutional neural networks.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Discussions", "weight": 1.0} -->

The most notable observation on the use of AFs for DL applications is that the newer activation functions seem to outperform the older AFs like the ReLU, yet even the latest DL architectures rely on the ReLU function. This is evident in SeNet where the hidden layers had the ReLU activation function and the Sigmoid output. However, current practices does not use the newly developed state-of-the-art AFs but depends on the tested and proven AFs, thereby underlining the fact that the newer activation functions are rarely used in practice.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper provides a comprehensive summary of AFs used in deep learning and most importantly, highlights the current trends in the use of these functions in practice against the state -of-the-art research results, which until now, has not been published in any literature.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We first presented a brief introduction to deep learning and activation functions, and then outlined the different types of activation functions discussed, with some specific applications where these functions were used in the development of deep learning based architectures and systems.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The AFs have the capability to improve the learning of the patterns in data thereby automating the process of features detection and justifying their use in the hidden layers of the neural networks, and usefulness for classification purposes across domains.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Conclusion", "weight": 1.5} -->

These activation functions have developed over the years with the compounded activation functions looking towards the future of activation functions research. Furthermore, it is also worthy to state that there are other activation functions that have not been discussed in this literature as we focused was on the activation functions, used in deep learning applications. A future work would be to compare all these state-of-th-art functions on the award-winning architectures, using standard datasets to observe if there would be improved performance results.
