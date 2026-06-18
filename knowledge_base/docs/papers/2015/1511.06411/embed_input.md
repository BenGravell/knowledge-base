<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Training Deep Neural Networks via Direct Loss Minimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Supervised training of deep neural nets typically relies on minimizing cross-entropy. However, in many domains, we are interested in performing well on metrics specific to the application. In this paper we propose a direct loss minimization approach to train deep neural networks, which provably minimizes the application-specific loss function. This is often non-trivial, since these functions are neither smooth nor decomposable and thus are not amenable to optimization with standard gradient-based methods. We demonstrate the effectiveness of our approach in the context of maximizing average precision for ranking problems. Towards this goal, we develop a novel dynamic programming algorithm that can efficiently compute the weight updates. Our approach proves superior to a variety of baselines in the context of action classification and object detection, especially in the presence of label noise.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Standard supervised neural network training involves computing the gradient of the loss function with respect to the parameters of the model, and therefore requires the loss function to be differentiable. Many interesting loss functions are, however, non-differentiable with respect to the output of the network. Notable examples are functions based on discrete outputs, as is common in labeling and ranking problems. In many cases these losses are also non-decomposable, in that they cannot be expressed as simple sums over the output units of the network.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the context of structured prediction problems, in which the output is multi-dimensional, researchers have developed max-margin training methods that are capable of minimizing an upper bound on non-decomposable loss functions. Standard learning in this paradigm involves changing the parameters such that the model assigns a higher score to the groundtruth output than to any other output. This is typically encoded by a constraint, enforcing that the groundtruth score should be higher than that of a selected, contrastive output. The latter is defined as the result of inference performed using a modified score function which combines the model score and the task loss, representing the metric that we care about for the application. This modified scoring function encodes the fact that we should penalize higher scoring configurations that are inferior in terms of the task loss. Various efficient methods have been proposed for incorporating complex discrete loss functions into this max-margin approach. Importantly, however, this form of learning does not directly optimize the task loss, but rather an upper bound.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

An alternative approach, frequently used in deep neural networks, is to train with a surrogate loss that can be easily optimized, *e.g*., cross-entropy. The problem of this procedure is that for many application domains the task loss differs significantly from the surrogate loss.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The seminal work of McAllester et al. showed how to compute the gradient of complex non-differentiable loss functions when dealing with linear models. In this paper we extend their theorem to the non-linear case. This is important in practice as it provides us with a new learning algorithm to train deep neural networks end-to-end to minimize the application specific loss function. As shown in our experiments on action classification and object detection, this is very beneficial, particularly when dealing with noisy labels.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Direct Loss Minimization for Neural Networks", "weight": 1.0} -->

In this section we present a novel formulation for learning neural networks by minimizing the task loss. Towards this goal, our first main result is a theorem extending the direct loss minimization framework of to non-linear models.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Direct Loss Minimization for Neural Networks", "weight": 1.0} -->

A neural network can be viewed as defining a composite scoring function $F{(x,y,w)}$, which depends on the input data $x \in \mathcal{X}$, some parameters $w \in {\mathbb{R}}^{A}$, and the output $y \in \mathcal{Y}$. Inference is then performed by picking the output with maximal score, *i.e*.:

<!-- chunk {"id": "body-0009", "role": "body", "section": "Direct Loss Minimization for Neural Networks", "weight": 1.0} -->

Given a dataset of input-output pairs $\mathcal{D} = {\{{(x,y)}\}}$, a standard machine learning approach is to optimize the parameters $w$ of the scoring function $F$ by optimizing cross-entropy. This is equivalent to maximizing the likelihood of the data, where the probability over each output configuration is given by the output of a softmax function, attached to the last layer of the network.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Direct Loss Minimization for Neural Networks", "weight": 1.0} -->

However, in many practical applications, we want prediction to succeed in an application-specific metric. This metric is typically referred to as the task loss, ${L{(y,y_{w})}} \geq 0$, which measures the compatibility between the annotated configuration $y$ and the prediction $y_{w}$. For learning, in this paper, we are thus interested in minimizing the task loss

<!-- chunk {"id": "body-0011", "role": "body", "section": "Direct Loss Minimization for Neural Networks", "weight": 1.0} -->

where ${\mathbb{E}}\lbrack \cdot \rbrack$ denotes an expectation taken over the underlying distribution behind the given dataset.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Direct Loss Minimization for Neural Networks", "weight": 1.0} -->

Solving this program is non-trivial, as many loss functions of interest are non-decomposable and non-smooth, and thus are not amenable to gradient-based methods. Examples of such metrics include average precision (AP) from information retrieval, intersection-over-union which is used in image labeling, and normalized discounted cumulative gain (NDCG) which is popular in ranking. In general many metrics are discrete, are not simple sums over the network outputs, and are not readily differentiable.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Direct Loss Minimization for Neural Networks", "weight": 1.0} -->

During training of a classifier it is hence common to employ a surrogate error metric, such as cross-entropy or hinge-loss, where one can directly compute the gradients with respect to the parameters. In the context of structured prediction models, several approaches have been developed to effectively optimize the structured hinge loss with non-decomposable task losses. While these methods include the task loss in the objective, they are not directly minimizing it, and hence these surrogate losses are at best highly correlated with the desired metric. Finding efficient techniques to directly minimize the metric of choice is therefore desirable.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Direct Loss Minimization for Neural Networks", "weight": 1.0} -->

McAllester et al. showed that it is possible to asymptotically optimize the task-loss when the function $F$ is linear in the parameters *i.e*., ${F{(x,y,w)}} = {w^{\top}\phi{(x,y)}}$. This work has produced encouraging results. For example, McAllester et al. used this technique for phoneme-to-speech alignment on the TIMIT dataset optimizing the $\tau$-alignment loss and the $\tau$-insensitive loss, while Keshet et al. illustrated applicability of the method to hidden Markov models for speech. Direct loss minimization was also shown to work well for inverse optimal control by Doerr et al..

<!-- chunk {"id": "body-0015", "role": "body", "section": "Direct Loss Minimization for Neural Networks", "weight": 1.0} -->

The first contribution of our work is to generalize this theorem to arbitrary scoring functions, *i.e*., non-linear and non-convex functions. This allows us to derive a new training algorithm for deep neural networks which directly minimizes the task loss.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Direct Loss Minimization for Average Precision", "weight": 1.0} -->

In order to directly optimize the task-loss we are required to compute the gradient defined in Eq. (2. ‣ 2 Direct Loss Minimization for Neural Networks ‣ Training Deep Neural Networks via Direct Loss Minimization")). As mentioned above, we need to solve both the standard inference task as well as the loss-augmented inference problem given in Eq. (3. ‣ 2 Direct Loss Minimization for Neural Networks ‣ Training Deep Neural Networks via Direct Loss Minimization")). While the former is typically assumed to be solvable, the latter depends on $L$ and might be very complex to solve, *e.g*., when the loss is not decomposable.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Direct Loss Minimization for Average Precision", "weight": 1.0} -->

In this paper we consider ranking problems, where the desired task loss $L$ is average precision (AP), a concrete example of a non-decomposable and non-smooth target loss function. For the linear setting, efficient algorithms for positive loss-augmented inference with AP loss were proposed by Yue et al. and Mohapatra et al.. Their results can be extended to the non-linear setting only in the positive case, where $y_{direct} = {{{{\arg\max}_{\hat{y} \in \mathcal{Y}}F}{(x,\hat{y},w)}} + {\epsilonL{(y,\hat{y})}}}$. For the negative setting inequalities required in their proof do not hold and thus their method is not applicable. In this section we propose a more general algorithm that can handle both cases with the same time complexity as, while being more intuitive to prove and understand.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Direct Loss Minimization for Average Precision", "weight": 1.0} -->

Alternatives to optimizing average precision are methods such as RankNet, LambdaRank and LambdaMART. For an overview, we refer the reader to Burges and references therein. Our goal here is simply to show direct loss minimization of AP as an example of our general framework.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Direct Loss Minimization for Average Precision", "weight": 1.0} -->

We define the output to be composed of pairwise comparisons, with $y_{i,j} = 1$ if sample $i$ is ranked higher than sample $j$, $y_{i,i} = 0$, and $y_{i,j} = {- 1}$ otherwise. We subsumed all these pairwise comparisons in $y = {(\ldots,y_{i,j},\ldots)}$. Similarly $x = {(x_{1},\ldots,x_{N})}$ contains all inputs, and $N = {{|\mathcal{P}|} + {|\mathcal{N}|}}$ refers to the total number of data points in the training set. In addition, we assume the ranking across all samples $y$ to be complete, *i.e*., consistent. During inference we obtain a ranking by predicting scores $\phi{(x_{i},w)}$ for all data samples $x_{i}$ which are easily sorted afterwards.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Direct Loss Minimization for Average Precision", "weight": 1.0} -->

For learning we generalize the feature function defined by Yue et al. and Mohapatra et al. to a non-linear scoring function, using

<!-- chunk {"id": "body-0021", "role": "body", "section": "Direct Loss Minimization for Average Precision", "weight": 1.0} -->

where $\phi{(x_{i},w)}$ is the output of the deep neural network when using the $i$-th example as input.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Direct Loss Minimization for Average Precision", "weight": 1.0} -->

AP is unfortunately a non-decomposable loss function, *i.e*., it does not decompose into functions dependent only on the individual $y_{i,j}$. To define the non-decomposable AP loss formally, we construct a vector $\hat{p} = {{rank}{(\hat{y})}} \in {\{ 0,1\}}^{{|\mathcal{P}|} + {|\mathcal{N}|}}$ by sorting the data points according to the ranking defined by the configuration $\hat{y}$. This vector contains a $1$ for each positive sample and a value $0$ for each negative element. In applications such as object detection, an example is said to be positive if the intersection over union of its bounding box and the ground truth box is bigger than a certain threshold (typically 50%). Using the $rank$ operator we obtain the AP loss by comparing two vectors $p = {{rank}{(y)}}$ and $\hat{p} = {{rank}{(\hat{y})}}$ via

<!-- chunk {"id": "body-0023", "role": "body", "section": "Direct Loss Minimization for Average Precision", "weight": 1.0} -->

where ${Prec}@j$ is the percentage of relevant samples in the prediction $\hat{p}$ that are ranked above position $j$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Direct Loss Minimization for Average Precision", "weight": 1.0} -->

To solve the loss-augmented inference task we have to solve the following program

<!-- chunk {"id": "body-0025", "role": "body", "section": "Direct Loss Minimization for Average Precision", "weight": 1.0} -->

In the following we derive a dynamic programming algorithm that can handle both the positive and negative case and has the same complexity as. Towards this goal, we first note that Observation 1 of Yue et al. holds for both the positive and the negative case. For completeness, we repeat their observation here and adapt it to our notation.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Observation 1 (Yue et al. )", "weight": 1.0} -->

Consider rankings which are constrained by fixing the relevance at each position in the ranking (*e.g*., the 3rd sample in the ranking must be relevant). Every ranking satisfying the same set of constraints will have the same $L_{AP}$. If the positive samples are sorted by their scores in descending order, and the irrelevant samples are likewise sorted by their scores, then the interleaving of the two sorted lists satisfying the constraints will maximize Eq. for that constrained set of rankings.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Observation 1 (Yue et al. )", "weight": 1.0} -->

Observation 1 means that we only need to consider the interleaving of two sorted lists of $\mathcal{P}$ and $\mathcal{N}$ to solve the program given in Eq.. From now on we therefore assume that the elements of $\mathcal{P}$ and $\mathcal{N}$ are sorted in descending order of their predicted score.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Observation 1 (Yue et al. )", "weight": 1.0} -->

where $L_{AP}^{i,j}$ refers to the AP loss restricted to subsets of $i$ positive and $j$ negative elements.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

To evaluate the performance of our approach we perform experiments on both synthetic and real datasets. We compare the positive and negative version of our direct loss minimization approach to a diverse set of baselines.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Dataset", "weight": 1.0} -->

We generate synthetic data via a neural network which assigns scalar scores to input vectors. The neural network consists of four layers of rectified linear units with parameters randomly drawn from independent Gaussians with zero mean and unit variance. The input for a training example is drawn from a 10 dimensional Gaussian, and the output produced by the network is its score. We generate 20,000 examples, and sort them in descending order based on their scores. The top $20\%$ of the samples are assigned to the positive set $\mathcal{P}$ and the remaining examples to the negative set. We then randomly divide the generated data into a training set containing 10,000 elements and a test set containing the rest. We compare various loss functions in terms of their ability to train the network to effectively reproduce the original scoring function. To ensure that we do not suffer from model mis-specification we employ the same network structure when training the parameters from random initializations. This synthetic experiment provides a good test environment to compare these training methods, as the mapping from input to scores is fairly complex yet deterministic.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Algorithms", "weight": 1.0} -->

We evaluate the positive and negative versions of our direct loss minimization when using two different task losses: AP and 0-1 loss. For the latter we predict for each sample $x_{i}$ whether it is a member of the set $\mathcal{P}$ or whether it is part of the set $\mathcal{N}$. We named these algorithms, "pos-AP," "neg-AP," "pos-01," and "neg-01." We also evaluate training the network using hinge loss, when employing AP and 0-1 loss as the task losses. We called these baselines "hinge-AP" and "hinge-01." Note that "hinge-AP" is equivalent to the approach of Yue et al. Yue et al.. We use the perceptron updates as additional baselines, which we call "per-AP" and "per-01." Finally, the last baseline uses maximum-likelihood (*i.e*., cross entropy) to train the network.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Algorithms", "weight": 1.0} -->

We call this approach "x-ent." The parameters of all algorithms are individually determined via grid search to produce the best AP on the training set.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Results", "weight": 1.0} -->

Fig. 3 shows AP results on the test set. We observe that the perceptron update does not perform well, since it does not take the task loss into account and has convergence issues. Contrary to the claim in for linear models, the negative update for direct loss is not competitive in our setting (*i.e*., non-linear models). This might be due to the fact that it tends to overly correct the classifier in noisy situations. Note the resemblance of the perceptron method and the negative direct loss minimization update: they are both trying to move "towards better." Therefore we expect the negative update to behave similarly to the perceptron, *i.e*., more vulnerable to noisy data. This resemblance also explains their strong performance on the TIMIT dataset, which is relatively easy and can be handled well with linear models. For the same reason, we expect the negative update to lead to better performance in less noisy situations, *e.g*., if the data is nearly linearly separable. To further examine this hypothesis we provide additional experimental results in the supplementary material.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Results", "weight": 1.0} -->

The direct loss minimization of 0-1 loss does not work well. It is likely that the sharp changes of the 0-1 loss result in a ragged energy landscape that is hard to optimize, while smoothing as performed by AP loss or surrogate costs helps in this setting.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Results", "weight": 1.0} -->

The hinge-AP algorithm of Yue et al. performs slightly better than other algorithms based on 0-1 loss. This shows that taking the AP loss into consideration helps improve the performance measured by AP. It is also important to note that when employing positive updates our direct loss minimization outperforms all baselines by a large margin. Note the resemblance between the structural SVM update and positive direct loss minimization: they are both moving "away from worse." We believe that hinge loss does not deal with label noise well as the update depends on the ground truth more than the direct loss update. Another possible reason is that the hinge loss upper bound is looser in this case. Taking the 0-1 loss as an example, the hinge loss of each outlier is much larger than the cost measured by the 0-1 loss (which is at most 1) in noisy case. This illustrates why the gap between hinge loss and target loss is large in noisy situations in general.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Results", "weight": 1.0} -->

To further examine the performance of pos-AP and hinge-AP, we performed another small scale synthetic experiment. We hypothesize that when the data contains outliers, and more generally the labels are noisy, hinge loss will become a worse approximation. We control the noise level in the data as a way of testing this hypothesis. We randomly generate 1000 10-dimensional data from $\mathcal{N}{}$. Datum sample $x$ is assigned to be positive when $\left. \parallel x\parallel \right._{2}^{2} > 1200$ and negative when $\left. \parallel x\parallel \right._{2}^{2} < 1000$. The noise is incorporated by randomly flipping a fixed percentage of labels. We use the same neural network structure for this task, tune the parameters on the training set, and report their results on the independent test set. As shown in Fig. 3 our method, pos-AP, is more robust to noise.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Results", "weight": 1.0} -->

Based on the results obtained from the synthetic experiments, during the experimental evaluation on real datasets we focus on comparing the positive non-linear direct loss minimization (pos-AP) to the strong baseline of hinge-AP Yue et al., as well as the standard approach of training based on cross-entropy.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Dataset", "weight": 1.0} -->

In the next experiment we use the PASCAL VOC2012 action classification dataset provided by Everingham et al.. The dataset contains 4588 images and 6278 "trainval" person bounding boxes. For each of the 10 target classes, we divide the trainval dataset into equal-sized training, validation and test sets. We tuned the learning rate, regularization weight, and $\epsilon$ for all the algorithms based on their performance on the validation dataset, and report the results on the test set. For all algorithms we used the entire available training set in a single batch and performed 300 iterations.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Algorithms", "weight": 1.0} -->

We train our non-linear direct loss minimization as well as all the baselines individually for each class. As baselines we again use a deep network trained with cross entropy and also consider the structured SVM method proposed by Yue et al.. The deep network used in these experiments follows the architecture of Krizhevsky et al., with the top dimension adjusted to a single output. We initialize the parameters using the weights trained on ILSVRC2012. Inspired by the RCNN, we cropped the regions of each image with a padding of 16 pixels and interpolated them to a size of $227 \times 227 \times 3$ to fit the input data dimension of the network. All the algorithms we compare to as well as our approach use raw pixels as input.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Results", "weight": 1.0} -->

Intuitively we expect direct loss minimization to outperform surrogate loss functions whenever there is a significant number of outliers in the data. To evaluate this hypothesis, we conduct experiments by randomly flipping a fixed number of labels. Our experiments shown in Tab. 1 and Fig. 4 confirm our intuitions, and direct loss works much better than hinge loss in the presence of label noise. When there is no noise, both algorithms perform similarly.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Dataset", "weight": 1.0} -->

For object detection we use the PASCAL VOC2012 object detection dataset collected by Everingham et al.. The dataset contains 5717 images for training, 5823 images for validation and 10991 images for test. For each image, we use the fast mode of selective search by Uijlings et al. to produce around 2000 bounding boxes. We train algorithms on the training set and report results on the validation set.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Algorithms", "weight": 1.0} -->

On this dataset we follow the RCNN paradigm. We adjust the dimension of the top layer of the network to be one and fine-tune using weights pre-trained on ILSVRC2012. We train direct loss minimization for all 20 classes separately. In contrast to the action classification task, we cannot calculate the overall AP in each iteration, due to the large number of bounding boxes. Instead, we use the AP on each mini-batch to approximate the overall AP. We find that using a batch size of 512 balances computational complexity and performance, though using a larger batch size generally results in better performance. For our final results, we use a learning rate of 0.1, a regularization parameter of $1 \cdot 10^{- 7}$, and $\epsilon = 0.1$ for all classes.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Algorithms", "weight": 1.0} -->

As baselines, we evaluate a network which uses cross-entropy and is trained separately for each class. Again, the network structure was chosen to be identical and we use the parameters provided by Krizhevsky et al. for initialization. In addition, we consider the structured SVM algorithm, which optimizes a surrogate of the AP loss. This structured SVM was trained using the same batch size as our direct loss minimization. We use a learning rate of 1, and a regularization parameter of $1 \cdot 10^{- 7}$ for all classes. As usual, we compare hinge-AP and pos-AP in the presence of 20% label noise.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Results", "weight": 1.0} -->

Tab. 2 shows competitive results of stochastic direct loss minimization, outperforming the strongest baseline by $0.9$. Our direct loss minimization performs better than hinge loss in this case. This is because the data for training detectors are slightly noisier compared to the action classification task, which is likely due to the common method of data augmentation based on intersection-over-union thresholds. To our astonishment, it becomes so hard for hinge-AP to learn well with noise in this detection task that it barely learns anything, while pos-AP only suffers from a reasonable decrease.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper we have proposed a direct loss minimization approach to train deep neural networks. We have demonstrated the effectiveness of our approach in the context of maximizing average precision for ranking problems. This involves minimizing a non-smooth and non-decomposable loss. Towards this goal we have proposed a dynamic programming algorithm that can efficiently compute the weight updates. Our experiments showed that this is beneficial when compared to a large variety of baselines in the context of action classification and object detection, particularly in the presence of noisy labels. In the future, we plan to investigate direct loss minimization in the context of other non-decomposable losses, such as intersection over union for semantic segmentation and shortest-path predictions in graphs.
