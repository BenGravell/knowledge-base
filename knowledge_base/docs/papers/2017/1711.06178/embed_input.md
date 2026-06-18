<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Beyond Sparsity: Tree Regularization of Deep Models for Interpretability

Topics include Accuracy, Decision trees.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The lack of interpretability remains a key barrier to the adoption of deep models in many applications. In this work, we explicitly regularize deep models so human users might step through the process behind their predictions in little time. Specifically, we train deep time-series models so their class-probability predictions have high accuracy while being closely modeled by decision trees with few nodes. Using intuitive toy examples as well as medical tasks for treating sepsis and HIV, we demonstrate that this new tree regularization yields models that are easier for humans to simulate than simpler L1 or L2 penalties without sacrificing predictive power.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep models have become the de-facto approach for prediction in a variety of applications such as image classification (e.g. (?)) and machine translation (e.g. (?; ?)). However, many practitioners are reluctant to adopt deep models because their predictions are difficult to interpret. In this work, we seek a specific form of interpretability known as *human-simulability*. A human-simulatable model is one in which a human user can "take in input data together with the parameters of the model and in reasonable time step through every calculation required to produce a prediction" (?). For example, small decision trees with only a few nodes are easy for humans to simulate and thus understand and trust. In contrast, even simple deep models like multi-layer perceptrons with a few dozen units can have far too many parameters and connections for a human to easily step through. Deep models for sequences are even more challenging. Of course, decision trees with too many nodes are also hard to simulate. Our key research question is: can we create deep models that are well-approximated by compact, human-simulatable models?

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The question of creating accurate yet human-simulatable models is an important one, because in many domains simulatability is paramount. For example, despite advances in deep learning for clinical decision support (e.g. (?; ?; ?)), the clinical community remains skeptical of machine learning systems (?). Simulatability allows clinicians to audit predictions easily. They can manually inspect changes to outputs under slightly-perturbed inputs, check substeps against their expert knowledge, and identify when predictions are made due to systemic bias in the data rather than real causes. Similar needs for simulatability exist in many decision-critical domains such as disaster response or recidivism prediction.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this need for interpretability, a number of works have been developed to assist in the interpretation of already-trained models. ? (?) train decision trees that mimic the predictions of a fixed, pretrained neural network, but do not train the network itself to be simpler. Other post-hoc interpretations typically typically evaluate the sensitivity of predictions to local perturbations of inputs or the input gradient (?; ?; ?; ?; ?). In parallel, research efforts have emphasized that simple lists of (perhaps locally) important features are not sufficient: ? (?) provide explanations in the form of programs; ? (?) learn decision sets and show benefits over other rule-based methods.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

These techniques focus on understanding already learned models, rather than finding models that are more interpretable. However, it is well-known that deep models often have multiple optima of similar predictive accuracy (?), and thus one might hope to find more interpretable models with equal predictive accuracy. However, the field of *optimizing* deep models for interpretability remains nascent. ? (?) penalize input sensitivity to features marked as less relevant. ? (?) train deep models that make predictions from text and simultaneously highlight contiguous subsets of words, called a "rationale," to justify each prediction. While both works optimize their deep models to expose relevant features, lists of features are not sufficient to *simulate* the prediction.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contributions", "weight": 1.0} -->

In this work, we take steps toward *optimizing* deep models for human-simulatability via a new model complexity penalty function we call *tree regularization*. Tree regularization favors models whose decision boundaries can be well-approximated by small decision-trees, thus penalizing models that would require many calculations to simulate predictions. We first demonstrate how this technique can be used to train simple multi-layer perceptrons to have tree-like decision boundaries. We then focus on time-series applications and show that gated recurrent unit (GRU) models trained with strong tree-regularization reach a high-accuracy-at-low-complexity sweet spot that is not possible with any strength of L1 or L2 regularization. Prediction quality can be further boosted by training new hybrid models -- GRU-HMMs -- which explain the residuals of interpretable discrete HMMs via tree-regularized GRUs. We further show that the approximate decision trees for our tree-regularized deep models are useful for human simulation and interpretability.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

We demonstrate our approach on a speech recognition task and two medical treatment prediction tasks for patients with sepsis in the intensive care unit (ICU) and for patients with human immunodeficiency virus (HIV). Throughout, we also show that standalone decision trees as a baseline are noticeably less accurate than our tree-regularized deep models. We have released an open-source Python toolbox to allow others to experiment with tree regularization ^11^1

<!-- chunk {"id": "body-0009", "role": "body", "section": "Simple neural networks", "weight": 1.0} -->

A multi-layer perceptron (MLP) makes predictions ${\hat{y}}_{n}$ of the target $y_{n}$ via a function ${\hat{y}}_{n}{(x_{n},W)}$, where the vector $W$ represents all parameters of the network. Given a data set $\{{(x_{n},y_{n})}\}$, our goal is to learn the parameters $W$ to minimize the objective

<!-- chunk {"id": "body-0010", "role": "body", "section": "Simple neural networks", "weight": 1.0} -->

For binary targets $y_{n}$, the logistic loss (binary cross entropy) is an effective choice. The regularization term $\Psi{(W)}$ can represent L1 or L2 penalties (e.g. (?; ?; ?)) or our new regularization.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Recurrent Neural Networks with Gated Recurrent Units", "weight": 1.0} -->

A recurrent neural network (RNN) takes as input an arbitrary length sequence $x_{n} = {\lbrack{x_{n1}\ldotsx_{nT_{n}}}\rbrack}$ and produces a "hidden state" sequence $h_{n} = {\lbrack{h_{n1}\ldotsh_{nT_{n}}}\rbrack}$ of the same length as the input. Each hidden state vector at timestep $t$ represents a location in a (possibly low-dimensional) "state space" with $K$ dimensions: $h_{nt} \in {\mathbb{R}}^{K}$. RNNs perform sequential *nonlinear* embedding of the form $h_{nt} = {f{(x_{nt},h_{{nt} - 1})}}$ in hope that the state space location $h_{nt}$ is a useful summary statistic for making predictions of the target $y_{nt}$ at timestep $t$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Recurrent Neural Networks with Gated Recurrent Units", "weight": 1.0} -->

Many different variants of the transition function architecture $f$ have been proposed to solve the challenge of capturing long-term dependencies. In this paper, we use gated recurrent units (GRUs) (?), which are simpler than other alternatives such as long short-term memory units (LSTMs) (?). While GRUs are convenient, any differentiable RNN architecture is compatible with our new tree-regularization approach.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Recurrent Neural Networks with Gated Recurrent Units", "weight": 1.0} -->

Below we describe the evolution of a single GRU sequence, dropping the sequence index $n$ for readability.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Recurrent Neural Networks with Gated Recurrent Units", "weight": 1.0} -->

The internal network nodes include candidate state gates $\overset{\sim}{h}$, update gates $z$ and reset gates $r$ which have the same cardinalty as the state vector $h$. Reset gates allow the network to forget past state vectors when set near zero via the logistic sigmoid nonlinearity $\sigma{( \cdot )}$. Update gates allow the network to either pass along the previous state vector unchanged or use the new candidate state vector instead. This architecture is diagrammed in Figure 1.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Recurrent Neural Networks with Gated Recurrent Units", "weight": 1.0} -->

Here, weight vector $w \in {\mathbb{R}}^{K}$ represents the parameters of this output layer. We denote the parameters for the entire GRU-RNN model as $W = {(w,U,V)}$, concatenating all component parameters.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Recurrent Neural Networks with Gated Recurrent Units", "weight": 1.0} -->

where again $\Psi{(W)}$ defines a regularization cost.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Tree Regularization for Deep Models", "weight": 1.0} -->

We now propose a novel *tree regularization* function $\Omega{(W)}$ for the parameters of a differentiable model which attempts to penalize models whose predictions are not easily *simulatable*. Of course, it is difficult to measure "simulatability" directly for an arbitrary network, so we take inspiration from decision trees. Our chosen method has two stages: first, find a single binary decision tree which accurately reproduces the network's thresholded binary predictions ${\hat{y}}_{n}$ given input $x_{n}$. Second, measure the complexity of this decision tree as the output of $\Omega{(W)}$. We measure complexity as the *average decision path length*---the average number of decision nodes that must be touched to make a prediction for an input example $x_{n}$. We compute the *average* with respect to some designated reference dataset of example inputs $D = {\{ x_{n}\}}$ from the training set. While many ways to measure complexity exist, we find average path length is most relevant to our notion of *simulatability*.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Tree Regularization for Deep Models", "weight": 1.0} -->

Remember that for us, human simulation requires stepping through every calculation required to make a prediction. Average path length exactly counts the number of true-or-false boolean calculations needed to make an average prediction, assuming the model is a decision tree. Total number of nodes could be used as a metric, but might penalize more accurate trees that have short paths for most examples but need more involved logic for few outliers.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Tree Regularization for Deep Models", "weight": 1.0} -->

Our true-average-path-length cost function $\Omega{(W)}$ is detailed in Alg. 1. It requires two subroutines, TrainTree and PathLength. TrainTree trains a binary decision tree to accurately reproduce the provided labeled examples $\{ x_{n},{\hat{y}}_{n}\}$. We use the DecisionTree module distributed in Python's scikit-learn (?) with post-pruning to simplify the tree. These trees can give probabilistic predictions at each leaf. (Complete decision-tree training details are in the supplement.) Next, PathLength counts how many nodes are needed to make a specific input to an output node in the provided decision tree. In our evaluations, we will apply our average-decision-tree-path-length regularization, or simply "tree regularization," to several neural models.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Tree Regularization for Deep Models", "weight": 1.0} -->

2:ŷ (⋅,W): binary prediction function, with parameters W
3:D = {xn}n = 1N: reference dataset with N examples
6: return $\frac{1}{N}{\sum_{n}{\text{PathLength}{(\text{tree},x_{n})}}}$
Algorithm 1 Average-Path-Length Cost Function

<!-- chunk {"id": "body-0021", "role": "body", "section": "Tree Regularization for Deep Models", "weight": 1.0} -->

Alg. 1 defines our average-path-length cost function $\Omega{(W)}$, which can be plugged into the abstract regularization term $\Psi{(W)}$ in the objectives in equations 1 and 4.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Making the Decision-Tree Loss Differentiable", "weight": 1.0} -->

Training decision trees is not differentiable, and thus $\Omega{(W)}$ as defined in Alg. 1 is not differentiable with respect to the network parameters $W$ (unlike standard regularizers such as the L1 or L2 norm). While one could resort to derivative-free optimization techniques (?), gradient descent has been an extremely fast and robust way of training networks (?).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Making the Decision-Tree Loss Differentiable", "weight": 1.0} -->

A key technical contribution of our work is introducing and training a *surrogate* regularization function ${\hat{\Omega}{(W)}}:{{\text{supp}{(W)}}\rightarrow{\mathbb{R}}_{+}}$ to map each candidate neural model parameter vector $W$ to an *estimate* of the average-path-length. Our approximate function $\hat{\Omega}$ is implemented as a standalone multi-layer perceptron network and is thus *differentiable*. Let vector $\xi$ of size $k$ denote the parameters of this chosen MLP approximator.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Making the Decision-Tree Loss Differentiable", "weight": 1.0} -->

where $W_{j}$ are the *entire* set of parameters for our model, $\epsilon > 0$ is a regularization strength, and we assume we have a dataset of $J$ known parameter vectors and their associated true path-lengths: ${\{ W_{j},{\Omega{(W_{j})}}\}}_{j = 1}^{J}$. This dataset can be assembled using the candidate $W$ vectors obtained while training our target neural model $\hat{y}{( \cdot,W)}$, as well as by evaluating $\Omega{(W)}$ for randomly generated $W$. Importantly, one can train the surrogate function $\hat{\Omega}$ in parallel with our network. In the supplement, we show evidence that our surrogate predictor $\hat{\Omega}{( \cdot )}$ tracks the true average path length as we train the target predictor $\hat{y}{( \cdot,W)}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Training the Surrogate Loss", "weight": 1.0} -->

Even moderately-sized GRUs can have parameter vectors $W$ with thousands of dimensions. Our labeled dataset for surrogate training -- ${\{ W_{j},{\Omega{(W_{j})}}\}}_{j = 1}^{J}$---will only have one $W_{j}$ example from each target network training iteration. Thus, in early iterations, we will have only few examples from which to learn a good surrogate function $\hat{\Omega}{(W)}$. We resolve this challenge via *augmenting* our training set with additional examples: We randomly sample weight vectors $W$ and calculate the true average path length $\Omega{(W)}$, and we also perform several random restarts on the unregularized GRU and use those weights in our training set.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Training the Surrogate Loss", "weight": 1.0} -->

A second challenge occurs later in training: as the model parameters $W$ shift away from their initial values, those early parameters may not be as relevant in characterizing the current decision function of the GRU. To address this, for each epoch, we use examples only from the past $E$ epochs (in addition to augmentation), where in practice, $E$ is empirically chosen. Using examples from a fixed window of epochs also speeds up training. The supplement shows a comparison of the importance of these heuristics for efficient and accurate training---empirically, data augmentation for stabilizing surrogate training allows us to scale to GRUs with 100s of nodes. GRUs of this size are sufficient for many real problems, such as those we encounter in healthcare domains.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Training the Surrogate Loss", "weight": 1.0} -->

Typically, we use $J = 50$ labeled pairs for surrogate training for toy datasets and $J = 100$ for real world datasets. Optimization of our surrogate objective is done via gradient descent. We use Autograd to compute gradients of the loss in Eq. with respect to $\xi$, then use Adam to compute descent directions with step sizes set to 0.01 for toy datasets and 0.001 for real world datasets.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Tree-Regularized MLPs: A Demonstration", "weight": 1.0} -->

While time-series models are the main focus of this work, we first demonstrate tree regularization on a simple binary classification task to build intuition. We call this task the 2D Parabola problem, because as Fig. 2(a) shows, the training data consists of 2D input points whose two-class decision boundary is roughly shaped like a parabola. The true decision function is defined by $y = {{5 \ast {({x - 0.5})}^{2}} + 0.4}$. We sampled 500 input points $x_{n}$ uniformly within the unit square ${\lbrack 0,1\rbrack} \times {\lbrack 0,1\rbrack}$ and labeled those above the decision function as positive. To make it easy for models to overfit, we flipped 10% of the points in a region near the boundary. A random 30% were held out for testing.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Tree-Regularized MLPs: A Demonstration", "weight": 1.0} -->

For the classifier $\hat{y}$, we train a 3-layer MLP with 100 first layer nodes, 100 second layer nodes, and 10 third layer nodes. This MLP is intentionally overly expressive to encourage overfitting and expose the impact of different forms of regularization: our proposed tree regularization ${\Psi{(W)}} = {\hat{\Omega}{(W)}}$ and two baselines: an L2 penalty on the weights ${\Psi{(W)}} = {\| W\|}_{2}$, and an L1 penalty on the weights ${\Psi{(W)}} = {\| W\|}_{1}$. For each regularization function, we train models at many different regularization strengths $\lambda$ chosen to explore the full range of decision boundary complexities possible under each technique.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Tree-Regularized MLPs: A Demonstration", "weight": 1.0} -->

For our tree regularization, we model our surrogate $\hat{\Omega}{(W)}$ with a 1-hidden layer MLP with 25 units. We find this simple architecture works well, but certainly more complex MLPs could could be used on more complex problems. The objective in equation 1 was optimized via Adam gradient descent (?) using a batch size of 100 and a learning rate of 1e-3 for 250 epochs, and hyperparameters were set via cross validation using grid search (see supplement for full experimental details).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Tree-Regularized MLPs: A Demonstration", "weight": 1.0} -->

Fig. 2 (b) shows the each trained model as a single point in a 2D fitness space: the x-axis measures model complexity via our average-path-length metric, and the y-axis measures AUC prediction performance. These results show that simple L1 or L2 regularization does *not* produce models with both small node count and good predictions at *any* value of the regularization strength $\lambda$. As expected, large $\lambda$ values for L1 and L2 only produce far-too-simple linear decision boundaries with poor accuracies. In contrast, our proposed tree regularization directly optimizes the MLP to have simple tree-like boundaries at high $\lambda$ values which can still yield good predictions.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Tree-Regularized MLPs: A Demonstration", "weight": 1.0} -->

The lower panes of Fig. 2 shows these boundaries. Our tree regularization is uniquely able to create axis-aligned functions, because decision trees prefer functions that are axis-aligned splits. These axis-aligned functions require very few nodes but are more effective than L1 and L2 counterparts. The L1 boundary is more sharp, whereas the L2 is more round.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Tree-Regularized MLPs: A Demonstration", "weight": 1.0} -->

(a) Training Data and Binary Class Labels for 2D Parabola

<!-- chunk {"id": "body-0034", "role": "body", "section": "Tree-Regularized MLPs: A Demonstration", "weight": 1.0} -->

(b) Prediction quality and complexity as reg. strength λ varies

<!-- chunk {"id": "body-0035", "role": "body", "section": "Tree-Regularized Time-Series Models", "weight": 1.0} -->

We now evaluate our tree-regularization approach on time-series models. We focus on GRU-RNN models, with some later experiments on new hybrid GRU-HMM models. As with the MLP, each regularization technique (tree, L2, L1) can be applied to the output node of the GRU across a range of strength parameters $\lambda$. Importantly, Algorithm 1 can compute the average-decision-tree-path-length for any fixed deep model given its parameters, and can hence be used to measure decision boundary complexity under any regularization, including L1 or L2. This means that when training any model, we can track both the predictive performance (as measured by area-under-the-ROC-curve (AUC); higher values mean better predictions), as well as the complexity of the decision tree required to explain each model (as measured by our average path length metric; lower values mean more interpretable models). We also show results for a baseline standalone decision tree classifier without any associated deep model, sweeping a range of parameters controlling leaf size to explore how this baseline trades off path length and prediction quality.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Tree-Regularized Time-Series Models", "weight": 1.0} -->

Further details of our experimental protocol are in the supplement, as well as more extensive results with additional baselines.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Synthetic Task: Signal-and-noise HMM", "weight": 1.0} -->

We generated a toy dataset of $N = 100$ sequences, each with $T = 50$ timesteps. Each timestep has a data vector $x_{nt}$ of 14 binary features and a single binary output label $y_{nt}$. The data comes from two separate HMM processes. First, a "signal" HMM generates the first 7 data dimensions from 5 well-separated states. Second, an independent "noise" HMM generates the remaining 7 data dimensions from a different set of 5 states. Each timestep's output label $y_{nt}$ is produced by a rule involving *both* the signal data and the signal hidden state: the target is 1 at timestep $t$ only if both the first signal state is active and the first observation is turned. We deliberately designed the generation process so that neither logistic regression with $x$ as features nor an RNN model that makes predictions from hidden states alone can perfectly separate this data.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Real-World Tasks", "weight": 1.0} -->

We tested our approach on several real tasks: predicting medical outcomes of hospitalized septic patients, predicting HIV therapy outcomes, and identifying stop phonemes in English speech recordings. To normalize scales, we independently standardized features $x$ via z-scoring.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Real-World Tasks", "weight": 1.0} -->

Sepsis Critical Care: We study time-series data for 11 786 septic ICU patients from the public MIMIC III dataset (?). We observe at each hour $t$ a data vector $x_{nt}$ of 35 vital signs and lab results as well as a label vector $y_{nt}$ of 5 binary outcomes. Hourly data $x_{nt}$ measures continuous features such as respiration rate (RR), blood oxygen levels (paO~2~), fluid levels, and more. Hourly binary labels $y_{nt}$ include whether the patient died in hospital and if mechanical ventilation was applied. Models are trained to predict all 5 output dimensions concurrently from one shared embedding. The average sequence length is 15 hours. 7 070 patients are used in training, 1 769 for validation, and 294 for test.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Real-World Tasks", "weight": 1.0} -->

HIV Therapy Outcome (HIV): We use the EuResist Integrated Database (?) for 53 236 patients diagnosed with HIV. We consider 4-6 month intervals (corresponding to hospital visits) as time steps. Each data vector $x_{nt}$ has 40 features, including blood counts, viral load measurements and lab results. Each output vector $y_{nt}$ has 15 binary labels, including whether a therapy was successful in reducing viral load to below detection limits, if therapy caused CD4 blood cell counts to drop to dangerous levels (indicating AIDS), or if the patient suffered adherence issues to medication. The average sequence length is 14 steps. 37 618 patients are used for training; 7 986 for testing, and 7 632 for validation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Real-World Tasks", "weight": 1.0} -->

Phonetic Speech (TIMIT): We have recordings of 630 speakers of eight major dialects of American English reading ten phonetically rich sentences (?). Each sentence contains time-aligned transcriptions of 60 phonemes. We focus on distinguishing stop phonemes (those that stop the flow of air, such as "b" or "g") from non-stops. Each timestep has one binary label $y_{nt}$ indicating if a stop phoneme occurs or not. Each input $x_{nt}$ has 26 continuous features: the acoustic signal's Mel-frequency cepstral coefficients and derivatives. There are 6 303 sequences, split into 3 697 for training, 925 for validation, and 1 681 for testing. The average length is 614.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Results", "weight": 1.0} -->

The major conclusions of our experiments comparing GRUs with various regularizations are outlined below.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Tree-regularized models have fewer nodes than other forms of regularization", "weight": 1.0} -->

Across tasks, we see that in the target regime of small decision trees (low average-path lengths), our proposed tree-regularization achieves higher prediction quality (higher AUCs). In the signal-and-noise HMM task, tree regularization (green line in Fig. 3(d)) achieves AUC values near 0.9 when its trees have an average path length of 10. Similar models with L1 or L2 regularization reach this AUC only with trees that are nearly double in complexity (path length over 25). On the Sepsis task (Fig. 4) we see AUC gains of 0.05-0.1 at path lengths of 2-10. On the TIMIT task (Fig. 5(a)), we see AUC gains of 0.05-0.1 at path lengths of 20-30. Finally, on the HIV CD4 blood cell count task in Fig. 5(b), we see AUC differences of between 0.03 and 0.15 for path lengths of 10-15.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Tree-regularized models have fewer nodes than other forms of regularization", "weight": 1.0} -->

The HIV adherence task in Fig. 5(d) has AUC gains of between 0.03 and 0.05 in the path length range of 19 to 25 while at smaller paths all methods are quite poor, indicating the problem's difficulty. Overall, these AUC gains are particularly useful in determining how to administer subsequent HIV therapies.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Tree-regularized models have fewer nodes than other forms of regularization", "weight": 1.0} -->

We emphasize that our tree-regularization usually achieves a sweet spot of high AUCs at short path lengths not possible with standalone decision trees (orange lines), L1-regularized deep models (red lines) or L2-regularized deep models (blue lines). In unshown experiments, we also tested elastic net regularization (?), a linear combination of L1 and L2 penalities. We found elastic nets to follow the same trend lines as L1 and L2, with no visible differences. In domains where human-simulatability is required, increases in prediction accuracy in the small-complexity regime can mean the difference between models that provide value on a task and models that are unusable, either because performance is too poor or predictions are uninterpretable.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Our learned decision tree proxies are interpretable", "weight": 1.0} -->

Across all tasks, the decision trees which mimic the predictions of tree-regularized deep models are small enough to simulate by hand (path length $\leq 25$) and help users grasp the model's nonlinear prediction logic. Intuitively, the trees for our synthetic task in Fig. 3(a)-(c) decrease in size as the strength $\lambda$ increases. The logic of these trees also matches the true labeling process: even the simplest tree (c) checks a relevant subset of input dimensions necessary to verify that both the first state and the first output dimension are active.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Our learned decision tree proxies are interpretable", "weight": 1.0} -->

In Fig. 4, we show decision tree proxies for our deep models on two sepsis prediction tasks: mortality and need for ventilation. We consulted a clinical expert on sepsis treatment, who noted that the trees helped him understand what the models might be doing and thus determine if he would trust the deep model. For example, he said that using FiO~2~, RR, CO~2~ and paO~2~ to predict need for mechanical ventilation (Fig. 4(d)) was sensible, as these all measure breathing quality. In contrast, the in-hospital mortality tree (Fig. 4(b)) predicts that some young patients with no organ failure have high mortality rates while other young patients with organ failure have low mortality. These counter-intuitive results led to hypotheses about how uncaptured variables impact the training process. Such reasoning would not be possible from simple sensitivity analyses of the deep model.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Our learned decision tree proxies are interpretable", "weight": 1.0} -->

Finally, we have verified that the decision tree proxies of our tree-regularized deep models of the HIV task in Fig. 5(d) are interpretable for understanding why a patient has trouble adhering to a prescription; that is, taking drugs regularly as directed. Our clinical collaborators confirm that the baseline viral load and number of prior treatment lines, which are prominent attributes for the decisions in Fig. 5(d), are useful predictors of a patient with adherence issues. Several medical studies (?; ?) suggest that patients with higher baseline viral loads tend to have faster disease progression, and hence have to take several drug cocktails to combat resistance. Juggling many drugs typically makes it difficult for these patients to adhere as directed. We hope interpretable predictive models for adherence could help assess a patient's overall prognosis (?) and offer opportunities for intervention (e.g. with alternative single-tablet regimens).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Decision trees trained to mimic deep models make faithful predictions", "weight": 1.0} -->

Across datasets, we find that each tree-regularized deep time-series model has predictions that agree with its corresponding decision tree proxy in about 85-90% of test examples. Table 1 shows exact fidelty scores for each dataset. Thus, the simulatable paths of the decision tree will be trustworthy in a majority of cases.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Practical runtimes for tree regularization are less than twice that of simpler L2", "weight": 1.0} -->

While our tree-regularized GRU with 10 states takes 3977 seconds per epoch on TIMIT, a similar L2-regularized GRU takes 2116 seconds per epoch. Thus, our new method has cost less than twice the baseline *even when the surrogate is serially computed*. Because the surrogate $\hat{\Omega}{(W)}$ will in general be a much smaller model than the predictor $\hat{y}{(x,W)}$, we expect one could get faster per-epoch times by parallelizing the creation of $(W,{\Omega{(W)}})$ training pairs and the training of the surrogate $\hat{\Omega}{(W)}$. Additionally, 3977 seconds includes the time needed to train the surrogate. In practice, we do this sparingly, only once every 25 epochs, yielding an amortized per-epoch cost of 2191 seconds (more runtime results are in the supplement).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Decision trees are stable over multiple optimization runs", "weight": 1.0} -->

When tree regularization is strong (high $\lambda$), the decision trees trained to match the predictions of deep models are stable. For both signal-and-noise and sepsis tasks, multiple runs from different random restarts have nearly identical tree shape and size, perhaps differing by a few nodes. This stability is crucial to building trust in our method. On the signal-and-noise task ($\lambda = 7000$), 7 of 10 independent runs with random initializations resulted in trees of exactly the same structure, and the others closely resembled those sharing the same subtrees and features (more details in supplement).

<!-- chunk {"id": "body-0052", "role": "body", "section": "The deep residual GRU-HMM achieves high AUC with less complexity", "weight": 1.0} -->

So far, we have focused on regularizing standard deep models, such as MLPs or GRUs. Another option is to use a deep model as a residual on another model that is already interpretable: for example, discrete HMMs partition timesteps into clusters, each of which can be inspected, but its predictions might have limited accuracy. In Fig. 6, we show the performance of jointly training a *GRU-HMM*, a new model which combines an HMM with a tree-regularized GRU to improve its predictions (details and further results in the supplement). Here, the ideal path length is zero, indicating only the HMM makes predictions. For small average-path-lengths, the GRU-HMM improves the original HMM's predictions *and* has simulatability gains over earlier GRUs. On the mechanical ventilation task, the GRU-HMM requires an average path length of only 28 to reach AUC of 0.88, while the GRU alone with the same number of states requires a path length of 60 to reach the same AUC. This suggests that jointly-trained deep residual models may provide even better interpretability.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

We have introduced a novel tree-regularization technique that encourages the complex decision boundaries of any differentiable model to be well-approximated by human-simulatable functions, allowing domain experts to quickly understand and approximately *compute* what the more complex model is doing. Overall, our training procedure is robust and efficient; future work could continue to explore and increase the stability of the learned models as well as identify ways to apply our approach to situations in which the inputs are not inherently interpretable (e.g. pixels in an image).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Across three complex, real-world domains -- HIV treatment, sepsis treatment, and human speech processing -- our tree-regularized models provide gains in prediction accuracy in the regime of simpler, approximately human-simulatable models. Future work could apply tree regularization to local, example-specific approximations of a loss (?) or to representation learning tasks (encouraging embeddings with simple boundaries). More broadly, our general training procedure could apply tree-regularization or other procedure-regularization to a wide class of popular models, helping us move beyond sparsity toward models humans can easily simulate and thus trust.
