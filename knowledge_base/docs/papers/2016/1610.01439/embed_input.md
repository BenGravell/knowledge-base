<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Nonlinear Systems Identification Using Deep Dynamic Neural Networks

Topics include System identification, Neural networks, Classification, Datasets, Online algorithms, Control, Deep neural networks, Nonlinear systems.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Neural networks are known to be effective function approximators. Recently, deep neural networks have proven to be very effective in pattern recognition, classification tasks and human-level control to model highly nonlinear realworld systems. This paper investigates the effectiveness of deep neural networks in the modeling of dynamical systems with complex behavior. Three deep neural network structures are trained on sequential data, and we investigate the effectiveness of these networks in modeling associated characteristics of the underlying dynamical systems. We carry out similar evaluations on select publicly available system identification datasets. We demonstrate that deep neural networks are effective model estimators from input-output data

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Methods for the adaptive identification and control of linear, time invariant systems with unknown parameters are well-established and documented in linear systems theory, with stable adaptive laws for the adjustment of parameters that demonstrate global stability of the overall system. Being universal approximators, neural networks (NNs) have witnessed a flurry of use in modeling various nonlinear phenomena in the past three decades. Three broad classes of NNs that have received attention recently include 1) multilayer perceptrons, 2) recurrent neural networks, and 3) convolutional neural networks. Multilayer networks have been used in identification and control of static and dynamic simple nonlinear systems, while recurrent networks (and its variants) have been used as associative memories for the solution of time-series/sequential optimization problems, and in the dynamic identification and control of nonlinear systems,. Convolutional networks, on the other hand, have been successfully used in pattern recognition, supervised classification tasks and image processing problems,.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In complicated real-world systems, deep neural networks (DNNs) have proven very effective for classification problems related with patterns in complicated systems such as image processing, speech processing, language models, handwriting recognition and sequential data,. These networks are termed 'deep' because they are constructed by stacking multiple layers of non-linear operations (such as NNs) atop one another with many hidden layers. They are analogous to complicated formulae that reuse many sub-formulae in abstracting real-world representations with their parameters (or weights).

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

*This work was supported by the Radiation Oncology Department, UT Southwestern, Dallas, Texas, USA 1 Olalekan Ogunmolu and Nicholas Gans are with the Department of Electrical Engineering, University of Texas at Dallas, Richardson, TX 75080, USA { olalekan.ogunmolu, ngans } @utdallas.edu 2 Xuejun Gu and Steve Jiang are with the Department of Radiation Oncology, University of Texas Southwestern Medical Center, Dallas TX 75390, USA { Xuejun.Gu, Steve.Jiang } @utsouthwestern.edu The work discussed in this paper is largely motivated by the problem discussed in recent investigations of the identification and control of soft-robots for head and neck motion alignment during cancer radiotherapy (RT),. Here we design self-organizing networks, connected in a DNN fashion, to enable the development of efficient and synaptic adaptive rules for arbitrarily connected NNs; this facilitates the development of an internal structure that is appropriate for a system identification and control learning task.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This work presents NN-based Hammerstein models evaluated on SISO and MIMO datasets. The modeling procedure for approximating systems such as the ones we present in this work is a complicated task with highly nonlinear dynamics that may be too complicated to model with closedform equations. We extend the development of NNs for abstracting complex nonlinear real-world systems in the pattern recognition field over the past 2 decades to solving a recursive identification, parameter estimation and control problem of a complex system.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Three specific NN architectures are investigated namely the multilayer network, simple recurrent NN and its long short-term memory (LSTM) variants, encoded in various suitable architectures appropriate to our learning task To demonstrate the applicability and extensibility of this identification methods, we conduct separate identification experiments to test the effectiveness of these modeling procedures on select SISO- and MIMO-system identification datasets from DaISy 1.

<!-- chunk {"id": "body-0008", "role": "body", "section": "SUPERVISED LEARNING WITH NEURAL NETWORKS", "weight": 1.0} -->

To allow an arbitrarily connected NN to develop selfadaptive learning rules that model an unknown system based on a finite data set, Z N (consisting of input-output pair, { u 1, u 2, · · · u N, y 1 · · ·, y N } ), we use a network topology that learns rules for adjusting the network weights W i in order to make the predicted outputs ˆ y i ( k ) approximate the desired outputs y i ( k ) to a sufficient degree, ϵ. Cybenko and Funahashi have shown that a single hidden layer is sufficient as a universal function approximator with the ability to approximate any Borel measurable function from one finite dimensional space to another. A single hidden layer can achieve a sufficient degree of accuracy with no theoretical constraint on the network's learning ability. The presence of noise in data can make a NN optimization get stuck in local minima during backpropagation but deep networks are better at identifying model structure in data in spite of noise in data.

<!-- chunk {"id": "body-0009", "role": "body", "section": "SUPERVISED LEARNING WITH NEURAL NETWORKS", "weight": 1.0} -->

In a typical feedforward NN, the input data is fed into an input layer that distributes the data to hidden layer(s), consisting of neurons that connect to the neurons of other layers; the NN may contain more than one hidden layer, but the signals from the last hidden layer must flow toward that of the output layer. The parameters of the network are chosen to minimize a global loss function Q (z, ˆ y) = l (ˆ y, y), which measures the cost of predicting the ˆ y when the true output y is a function over the training set. For regression problems encountered in system identification tasks, it is typical to use the mean-squared error as a cost to be minimized, i.e., using the basic backpropagation algorithm for a feedforward network or the popular backpropagation through time for a recurrent NN.

<!-- chunk {"id": "body-0010", "role": "body", "section": "SUPERVISED LEARNING WITH NEURAL NETWORKS", "weight": 1.0} -->

is a special case of the leastsquares method, with n being the total number of training examples; l (ˆ y, y) is minimized over the training examples using gradient descent so that at each iteration, we update the parameters w i based on the gradient of Q (z, ˆ y) i.e., where η is the momentum that speeds up the optimization along directions of low but persistent reduction in training error, α is a sufficiently small learning rate, and ∇ w Q (z, w k) is the derivative of Q with respect to w. If ∇ w Q (z, w k) = 0, then for sufficiently small and positive definite α, η w k -α 1 n n ∑ i =1 ∇ w Q (z i, w k) < w 0. Therefore, has linear convergence under sufficient regularity assumptions when the starting point w 0 is close enough to the minimum value of the loss.

<!-- chunk {"id": "body-0011", "role": "body", "section": "SUPERVISED LEARNING WITH NEURAL NETWORKS", "weight": 1.0} -->

In practice, a simplification of, termed stochastic gradient descent (SGD), is used in computing an estimate of the gradient based on a single randomly picked example z k where ∇ w Q k (·) is the average over the k -th batch of ∇ w Q. randomly samples from the training set during each epoch and directly optimizes l (ˆ y, y). SGD has the advantage of minimizing training time by computing an approximation to the gradient over each mini-batch of samples.

<!-- chunk {"id": "body-0012", "role": "body", "section": "LEARNING WITH DEEP DYNAMIC NNS", "weight": 1.0} -->

The datasets considered in this work are sequential in nature, some with temporal correlation in the evolution of inputs. We therefore propose NN architectures that are adept at learning the nonlinearity in time-series data. Specifically, we consider feedforward multilayer networks, simple recurrent networks, long short-term memory and gated recurrent units.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Multilayer Networks", "weight": 1.0} -->

Fig. 1 shows the schematic representation of a multilayer NN (MLP) with synchronous signals that flow in a forward direction, U → H → Y. Joining the weights and biases of the network completely parameterizes the system it is trained. During training, the estimated outputs are compared with the true outputs to calculate the error signal in the network.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Multilayer Networks", "weight": 1.0} -->

The errors are back-propagated through the network to obtain the ordered derivatives for learning. The 'goodness' of the trained model can be measured by evaluating how well the training data generalizes to testing data which is separated from the training set.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Recurrent Neural Networks", "weight": 1.0} -->

Recurrent Neural Networks (RNNs) are modeled from the behavior of many cells in nature with content-addressable memory, capable of capturing an entire information sequence given portions of the overall sequence. Whereas, the forward networks 'fire' their neurons in a single direction, RNNs employ a strong back-coupling U ⇄ H ⇆ Y ⇄ U such that signal strengths can flow asynchronously between nodes even when a node signal is delayed. The architecture of a simple RNN is similar to that of a MLP, except that there is a self-feedback of neurons in the hidden layer(s) (see Fig. 2). RNNs model nonlinear dynamical systems whose phase space dynamics is determined by a significant number of locally stable nodes to which it is attracted.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Recurrent Neural Networks", "weight": 1.0} -->

The hidden nodes h = (h 1,..., h N) and output nodes y = (y 1,..., y N) are determined by looping through the equations from k = 1 to N where the W terms are the weight matrices (e.g. W uh would be the input-to-hidden weight matrix), the b terms represent the vectorized bias terms (e.g. b h would be the hidden bias vector) and H is the hidden layer function, applied as an Hadamard operator. The loss is a cummulative loss of each time-step losses and the gradients are computed through backpropagation through time (BPTT,) whereby parameters are updated after a complete sequence of forward and backward passes are completed or real-time recurrent learning (RTRL).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Long Short Term Memory (LSTM) Cells", "weight": 1.0} -->

For long-term context memorization, the gradients of RNNs can become intractable, as they use their backcoupling connections to memorize the structure of recent inputs (i.e. short-term memory as compared against longterm memory). As a result, backpropagated error signals in time can become infinitely high (causing oscillating weights), or vanish (causing complexity in computing slow varying weights) to the extent that the evolution in time of the backpropagated errors exponentially depend on the size of the weights,. Horchreiter et al. proposed the LSTM remedy that truncates gradients in the network where it is innocuous by enforcing constant error flows through constant error carousels within special multiplicative units (MUs). Constant error flow is regulated by nonlinear MUs that learn to open or close gates in the network. LSTMs therefore approximate long-term information with significant delays by solving RNN algorithms faster. For an LSTM cell with N memory units, at each time step, the evolution of its parameters are determined by Fig. 2: A simple recurrent neural network.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Long Short Term Memory (LSTM) Cells", "weight": 1.0} -->

Fig. 3: Long Short-term Memory Cell. Reprinted. where the W u q and W h q terms are the respective rectangular input and square recurrent weight matrices, W c q are peephole weight vectors from the cell to each of the gates (see Fig. 3), σ denotes sigmoid activation functions (applied element-wise) and the i t, f t and o t equations denote the input, forget and output gates respectively; z t is the input to the cell c t. The output of the LSTM cell is o t and ⊙ denote point-wise vector products. The bias terms for the gates are initialized to a large value at the beginning of training in order to allow learning long-term context. The forget gate facilitates resetting the state of the LSTM, while the peephole connections from the cell to the gates enable accurate learning of timings.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Fast LSTM", "weight": 1.0} -->

This is a faster version of the LSTM architecture of Fig. 3, with the input, forget and the output gates of the LSTM cell computed without using the connections from the peepholes. The fast LSTM algorithm is computed as follows

<!-- chunk {"id": "body-0020", "role": "body", "section": "Gated Recurrent Units (GRU)", "weight": 1.0} -->

GRUs are simpler versions of LSTMs albeit with simpler computation of hidden states. They consist of two RNN systems acting in an encoder-decoder fashion: one RNN encodes a source sequence into a fixed-length vector representation, and the other RNN transforms the representations into a variable-length sequence whilst being jointly trained to maximize the conditional probability of a target sequence given an input sequence. The GRU has a hidden state, h t, that encodes the input sequence as a summary, c, while the decoder predicts the output sequence conditioned on previous outputs, y t -i, and c i.e. where f (·) and g (·) are appropriate activation functions. Similar to the LSTM, the GRU has a hidden state that can forget previous information based on the state of a reset gate as the following equations show where f (·) is a sigmoid activation function while g (·) can be activation functions that maps to probability spaces (e.g. soft-max).

<!-- chunk {"id": "body-0021", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

We develop and train models on the soft-robot dataset, and extend the results by training on select DaISy dataset.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Data and Baseline Systems", "weight": 1.0} -->

For the soft-robot actuator dataset, we had a mannequin head lying in a supine position on a table that simulated our proposed motion alignment correction set-up during cancer RT. A soft-robot actuator in the form of an inflatable air bladder (IAB) moved the mannequin head based on supplied air pressure. This corrected for non-rigid motions during treatment. The IAB was actuated by current-driven proportional pneumatic valves; the experimental set-up is described, but the change in head motion is recorded by a motion capture (mocap) system instead of an RGB-D camera system. The mocap is capable of measuring head position with less than 1 mm error. This is a SISO system with input as current (generated from pseudo-random binary sequences) in mA and outputs as head height in mm. We collected 10, 070 samples of input-output data offline, and in all experiments, we separate the dataset in a 60:40% ratio for training and testing purposes.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Data and Baseline Systems", "weight": 1.0} -->

A mini-batch of 100 samples from the { u ( k ), y ( k ) } data was used for a total of 50 epochs, where we loop over each mini-batch 10, 000 times and all training was performed on an NVIDIA CUDA-capable GPU.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Data and Baseline Systems", "weight": 1.0} -->

In a separate experiments, we conducted training on the glassfurnace dataset which we downloaded from the DaISy file server. The glassfurnace dataset consists of 3 inputs and 6 outputs. The inputs are made up of two heating and a cooling signal, while the outputs are the readings from 6 temperature sensors in a cross-section of the furnace.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Data and Baseline Systems", "weight": 1.0} -->

We examine the ability of deep dynamic NNs to model the underlying system dynamics using deep NN structures appropriate to the learning task guided by our knowledge of each system. We map a single input (being actuation current to the inlet pneumatic valve) to the pitch motion of the manikin head and allow the mass of the patient's head to naturally deflate the air bladder. For more complicated networks that we develop, such as recurrent and dynamic feedforward network Hammerstein models, we adopt dropout techniques during training since the large number of parameters in the network could potentially lead to overfitting. The code for replicating most of the experiments in this work can be found in 3

<!-- chunk {"id": "body-0026", "role": "body", "section": "Multilayer network", "weight": 1.0} -->

1) Soft-Robot: The current from the pneumatic valve was mapped to a hidden layer with six neurons, followed by a ReLU nonlinearity that was then fully connected to the output layer ( i.e. mocap measurements) (Fig. 1). We conduct experiments with the current -pitch data-pair (because the soft-robot directly controls the head pitch motion).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Multilayer network", "weight": 1.0} -->

The soft-robot multilayer network has 19 parameters; through cross-validation, we found a step size, α = 1 1000 to work well. We initially tried batch normalization of the hidden layer neurons and dropout regularization but these produced no noticeable speed-up in training time for the MLP network. 2) GlassFurnace: The model structure is similar to that of the SISO soft-robot system except that we use 3 input linear layers and we reshape the output layer to 6. The performance is shown in the top chart of Fig. 8.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Multilayer network", "weight": 1.0} -->

3 Soft-Robot models are on the soft-robot branch; glassfurnace models are on the glassfurnace branch. An extensive discussion of the training procedure for other DaIsY datasets shall be posted on the author's blog at Fig. 4: Training of soft-robot system using a six-hidden layer MLP. Fit to estimation data: SISO = 99.8%, SIMO = 87.5 % Fig. 5: The Hammerstein model structure

<!-- chunk {"id": "body-0029", "role": "body", "section": "Recurrent Neural Network Structure", "weight": 1.0} -->

1) Soft-Robot: From our previous investigations of the soft-robot network, we had noticed a nonlinearity from input to states that the LTI models we earlier studied did not sufficiently capture. We conjecture that a nonlinearity from input to system states followed by a dynamic linearity from states to head pitch motion would be favorable by feeding back interior nodes in the network as recurrent regressors. We propose a Hammerstein model consisting of a recurrent NN nonlinear element followed by a multilayer network to better model the overall system nonlinearity. The forward connections of the multilayer network would model the linear dynamic system from states to output (see Fig. 5). We employ this model structure with the three different recurrent network models discussed in section section V, and we map the valve current to head pitch motion. In the Hammerstein model of Fig. 5, the g (·) block represents the static nonlinearity that integrates the input sequence, and nonlinearly transforms the inputs to the system states. The neurons at this layer develop internal dynamics by their associative memory for q steps back in time and weighted connections with the feedback connections from other neurons.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Recurrent Neural Network Structure", "weight": 1.0} -->

The G (z -1) block maps the linear dynamics of the system states to the sensors' measurements. We assume g (·) is continuous and bounded, and the linear dynamical system is causal and asymptotically stable. In all our models, we found a backpropagation in time by 5 steps (i.e. q = 5) to be sufficient for approximating the system dynamics. We model the head motion of the patient as where A (q -1) and B (q -1) are regressive polynomials given by The g (·) and G (z -1) networks are stacked on one another in a deep modular approach with weights updated along the negative gradients of the MSE cost function, l (n). The parameters of the linear dynamic submodule, ˆ a k (n), ˆ b k (n), and the weight vector of the nonlinear element are updated according to with η being the learning rate. The top graph of Fig. 6 shows the performance of the RNN and feedforward multilayer Hammerstein network on the soft-robot dataset.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Recurrent Neural Network Structure", "weight": 1.0} -->

This model performs faster and quickly integrates the mean-square error to reach the desired minimum compared to the forward network of the previous section. 2) Glassfurnace Data: We adopt the same structure as the soft-robot network except that we reshape the input and output layers of the network model to accommodate the widths of the glassfurnace data. The training performance is depicted in Fig. 8

<!-- chunk {"id": "body-0032", "role": "body", "section": "LSTM Model Architecture", "weight": 1.0} -->

Exploiting the architecture of the recurrent network further, we replace the RNN nonlinear element of Fig. 5 with the vanilla LSTM architecture discussed in subsection VC. Our training model consists of three nonlinear LSTM modules, each decorated with dropout activation functions in their output layers, and the last layer being fully connected to a linear dynamic module. Note that this is a replication of the Hammerstein block-structured model. This is then fed to the vector of head motion measurements from the mocap system.

<!-- chunk {"id": "body-0033", "role": "body", "section": "LSTM Model Architecture", "weight": 1.0} -->

Through model exploration, we found the following NN structure to work well with our dataset: Altogether, the soft-robot network (SR) has 45, 236 while the glassfurnace dataset has 45989 parameters. The SR Fig. 6: RNN/Vanilla LSTM Hammerstein model performance on soft-robot dataset. performanace is shown in Fig. 6; this network handles input delay better given its capacity for modeling long-term dependencies as well as adapting its parameters to capture the temporal evolution of the underlying system. Training with the LSTM architecture takes a slightly longer time compared to the MLP or RNN-MLP architecture due to its highly recurrent nature and complexity in computing gradients.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Fast LSTM Architecture", "weight": 1.0} -->

To minimize the complexity of the model structure whilst preserving the effectiveness of the model, we remove the peephole connections of Fig. 3 and carry out the same procedure as in § VI-D with the soft-robot and glassfurnace network. We achieve approximately the same level of convergence (Fig. 7) using less parameters in less time (see tables I & II).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Gated Recurrent Units Structure", "weight": 1.0} -->

The final model structure is the gated recurrent architecture described inV-E. Like the LSTM models, the structure consists of three nonlinear GRU elements, each followed by 0. 35 drop-out probabilities (to prevent the co-adaptations in training data); this has been shown to lead to better generalization of the NN models. The last layer of the GRU structure is a linear dynamic layer that maps the nonlinear states of the system to the head pitch motion. The training algorithm is, Fig. 7: SISO soft-robot training with FastLSTM/GRU Hammerstein model.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Gated Recurrent Units Structure", "weight": 1.0} -->

Fig. 8: RNN/Multilayer FeedForward Model Performance on Glassfurnace.

<!-- chunk {"id": "body-0037", "role": "body", "section": "RESULTS AND ANALYSES", "weight": 1.0} -->

In Table I & II, the models are characterized by properties that suggest good fit to training data and mean-square losses that are generally acceptable on the given noisy dataset. It is noteworthy that we do not pre-process these datasets nor carry out batch normalization of layers of the network during training. While the multilayer network fits the two datasets well and takes very little time to train, it should be noted that their ability to approximate sequential data may not be robust to model uncertainties and stochastic disturbances as correlated inputs, and self-feedback of input or output information in the dataset are not taken into account by nature of its structure.

<!-- chunk {"id": "body-0038", "role": "body", "section": "RESULTS AND ANALYSES", "weight": 1.0} -->

The fit to estimation data was calculated from where ¯ y is the channel-wise mean and ‖·‖ is the 2 -norm operator. The mean-square error was calculated according to.

<!-- chunk {"id": "body-0039", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

This work has shown the adaptability of supervised deep network architectures for the identification of nonlinear dynamical systems that are otherwise complicated to model using hand-coded features. Deep networks are easy to train compared to the expert knowledge required in identifying nonlinear regressive models, and they scale well in modeling complicated relationship between input-output data. We designed strictly feedforward and nonlinear Hammerstein model structures for identifying the dynamic relationship between input-output datasets: one gathered from a soft-robot actuator for a motion-alignment correction system in clinical cancer radiotherapy and the other tested on a multi-input and multi-output dataset from DaISy. Through proper hyperparameters selection, model choice and weights tuning that is appropriate for the learning tasks presented, we demonstrate that complex hand-coding of features characteristic of classical identification can be discarded with deep network-based models.

<!-- chunk {"id": "body-0040", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

With the availability of unit-tested deep network frameworks such as Torch, Tensorflow and Theano, researchers can train datasets with DNNs and generate models that are robust to modeling uncertainties despite complicated structure in data. In future investigations, we will use these models in the real-time identification and control of our proposed softrobot motion alignment correction systems for H&N cancer radiotherapy treatments as well as other complex nonlinear phenomena that we are concurrently working.
