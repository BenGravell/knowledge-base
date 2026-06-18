<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Hierarchical Reasoning Model

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Reasoning, the process of devising and executing complex goal-oriented action sequences, remains a critical challenge in AI. Current large language models (LLMs) primarily employ Chain-of-Thought (CoT) techniques, which suffer from brittle task decomposition, extensive data requirements, and high latency. Inspired by the hierarchical and multi-timescale processing in the human brain, we propose the Hierarchical Reasoning Model (HRM), a novel recurrent architecture that attains significant computational depth while maintaining both training stability and efficiency. HRM executes sequential reasoning tasks in a single forward pass without explicit supervision of the intermediate process, through two interdependent recurrent modules: a high-level module responsible for slow, abstract planning, and a low-level module handling rapid, detailed computations. With only 27 million parameters, HRM achieves exceptional performance on complex reasoning tasks using only 1000 training samples. The model operates without pre-training or CoT data, yet achieves nearly perfect performance on challenging tasks including complex Sudoku puzzles and optimal path finding in large mazes. Furthermore, HRM outperforms much larger models with significantly longer context windows on the Abstraction and Reasoning Corpus (ARC), a key benchmark for measuring artificial general intelligence capabilities.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

These results underscore HRM's potential as a transformative advancement toward universal computation and general-purpose reasoning systems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep learning, as its name suggests, emerged from the idea of stacking more layers to achieve increased representation power and improved performance ^,\ ^. However, despite the remarkable success of large language models, their core architecture is paradoxically shallow ^^. This imposes a fundamental constraint on their most sought-after capability: reasoning. The fixed depth of standard Transformers places them in computational complexity classes such as $AC^{0}$ or $TC^{0}$ ^^, preventing them from solving problems that require polynomial time ^,\ ^. LLMs are not Turing-complete and thus they cannot, at least in a purely end-to-end manner, execute complex algorithmic reasoning that is necessary for deliberate planning or symbolic manipulation tasks ^,\ ^. For example, our results on the Sudoku task show that increasing Transformer model depth can improve performance,^11^1Simply increasing the model width does not improve performance here. but performance remains far from optimal even with very deep models (see Figure˜2), which supports the conjectured limitations of the LLM scaling paradigm ^^.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The LLMs literature has relied largely on Chain-of-Thought (CoT) prompting for reasoning ^^. CoT externalizes reasoning into token-level language by breaking down complex tasks into simpler intermediate steps, sequentially generating text using a shallow model ^^. However, CoT for reasoning is a crutch, not a satisfactory solution. It relies on brittle, human-defined decompositions where a single misstep or a misorder of the steps can derail the reasoning process entirely ^,\ ^. This dependency on explicit linguistic steps tethers reasoning to patterns at the token level. As a result, CoT reasoning often requires significant amount of training data and generates a large number of tokens for complex reasoning tasks, resulting in slow response times. A more efficient approach is needed to minimize these data requirements ^^.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Towards this goal, we explore "latent reasoning", where the model conducts computations within its internal hidden state space ^,\ ^. This aligns with the understanding that language is a tool for human communication, not the substrate of thought itself ^^; the brain sustains lengthy, coherent chains of reasoning with remarkable efficiency in a latent space, without constant translation back to language. However, the power of latent reasoning is still fundamentally constrained by a model's effective computational depth. Naively stacking layers is notoriously difficult due to vanishing gradients, which plague training stability and effectiveness ^^, ^^. Recurrent architectures, a natural alternative for sequential tasks, often suffer from early convergence, rendering subsequent computational steps inert, and rely on the biologically implausible, computationally expensive and memory intensive Backpropagation Through Time (BPTT) for training ^^.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The human brain provides a compelling blueprint for achieving the effective computational depth that contemporary artificial models lack. It organizes computation hierarchically across cortical regions operating at different timescales, enabling deep, multi-stage reasoning ^^, ^^, ^^. Recurrent feedback loops iteratively refine internal representations, allowing slow, higher-level areas to guide, and fast, lower-level circuits to execute---subordinate processing while preserving global coherence ^^, ^^, ^^. Notably, the brain achieves such depth without incurring the prohibitive credit-assignment costs that typically hamper recurrent networks from backpropagation through time ^^, ^^.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inspired by this hierarchical and multi-timescale biological architecture, we propose the Hierarchical Reasoning Model (HRM). HRM is designed to significantly increase the effective computational depth. It features two coupled recurrent modules: a high-level (H) module for abstract, deliberate reasoning, and a low-level (L) module for fast, detailed computations. This structure avoids the rapid convergence of standard recurrent models through a process we term "hierarchical convergence." The slow-updating H-module advances only after the fast-updating L-module has completed multiple computational steps and reached a local equilibrium, at which point the L-module is reset to begin a new computational phase.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, we propose a one-step gradient approximation for training HRM, which offers improved efficiency and eliminates the requirement for BPTT. This design maintains a constant memory footprint ($O{}$ compared to BPTT's $O{(T)}$ for $T$ timesteps) throughout the backpropagation process, making it scalable and more biologically plausible.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Leveraging its enhanced effective depth, HRM excels at tasks that demand extensive search and backtracking. Using only 1,000 input-output examples, without pre-training or CoT supervision, HRM learns to solve problems that are intractable for even the most advanced LLMs. For example, it achieves near-perfect accuracy in complex Sudoku puzzles (Sudoku-Extreme Full) and optimal pathfinding in 30x30 mazes, where state-of-the-art CoT methods completely fail (0% accuracy).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the Abstraction and Reasoning Corpus (ARC) AGI Challenge ^,\,\ ^ - a benchmark of inductive reasoning - HRM, trained from scratch with only the official dataset (\~1000 examples), with only 27M parameters and a 30x30 grid context (900 tokens), achieves a performance of 40.3%, which substantially surpasses leading CoT-based models like o3-mini-high (34.5%) and Claude 3.7 8K context (21.2%), despite their considerably larger parameter sizes and context lengths, as shown in Figure˜1. This represents a promising direction toward the development of next-generation AI reasoning systems with universal computational capabilities.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Hierarchical Reasoning Model", "weight": 1.0} -->

Hierarchical processing: The brain processes information across a hierarchy of cortical areas. Higher-level areas integrate information over longer timescales and form abstract representations, while lower-level areas handle more immediate, detailed sensory and motor processing ^^, ^^, ^^.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Hierarchical Reasoning Model", "weight": 1.0} -->

Temporal Separation: These hierarchical levels in the brain operate at distinct intrinsic timescales, reflected in neural rhythms (e.g., slow theta waves, 4--8 Hz and fast gamma waves, 30--100 Hz) ^^, ^^. This separation allows for stable, high-level guidance of rapid, low-level computations ^^, ^^.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Hierarchical Reasoning Model", "weight": 1.0} -->

Recurrent Connectivity: The brain features extensive recurrent connections. These feedback loops enable iterative refinement, yielding more accurate and context-sensitive representations at the cost of additional processing time. Additionally, the brain largely avoids the problematic deep credit assignment problem associated with BPTT ^^.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Hierarchical Reasoning Model", "weight": 1.0} -->

The HRM model consists of four learnable components: an input network $f_{I}{( \cdot;\theta_{I})}$, a low-level recurrent module $f_{L}{( \cdot;\theta_{L})}$, a high-level recurrent module $f_{H}{( \cdot;\theta_{H})}$, and an output network $f_{O}{( \cdot;\theta_{O})}$. The model's dynamics unfold over $N$ high-level cycles of $T$ low-level timesteps each^22^2While inspired by temporal separation in the brain, our model's "high-level" and "low-level" modules are conceptual abstractions and do not map directly to specific neural oscillation frequencies.. We index the total timesteps of one forward pass by $i = {1,\ldots,{N \times T}}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Hierarchical Reasoning Model", "weight": 1.0} -->

The HRM maps an input vector $x$ to an output prediction vector $\hat{y}$ as follows.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Hierarchical Reasoning Model", "weight": 1.0} -->

At each timestep $i$, the L-module updates its state conditioned on its own previous state, the H-module's current state (which remains fixed throughout the cycle), and the input representation. The H-module only updates once per cycle (i.e.,

<!-- chunk {"id": "body-0018", "role": "body", "section": "Hierarchical Reasoning Model", "weight": 1.0} -->

This entire $NT$-timestep process represents a single forward pass of the HRM. A halting mechanism (detailed later in this section) determines whether the model should terminate, in which case $\hat{y}$ will be used as the final prediction, or continue with an additional forward pass.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Hierarchical convergence", "weight": 1.0} -->

Although convergence is crucial for recurrent networks, standard RNNs are fundamentally limited by their tendency to converge too early. As the hidden state settles toward a fixed point, update magnitudes shrink, effectively stalling subsequent computation and capping the network's effective depth. To preserve computational power, we actually want convergence to proceed very slowly--but engineering that gradual approach is difficult, since pushing convergence too far edges the system toward instability.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Hierarchical convergence", "weight": 1.0} -->

HRM is explicitly designed to counteract this premature convergence through a process we term hierarchical convergence. During each cycle, the L-module (an RNN) exhibits stable convergence to a local equilibrium. This equilibrium, however, depends on the high-level state $z_{H}$ supplied during that cycle. After completing the $T$ steps, the H-module incorporates the sub-computation's outcome (the final state $z_{L}$) and performs its own update. This $z_{H}$ update establishes a fresh context for the L-module, essentially "restarting" its computational path and initiating a new convergence phase toward a different local equilibrium.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Hierarchical convergence", "weight": 1.0} -->

This process allows the HRM to perform a sequence of distinct, stable, nested computations, where the H-module directs the overall problem-solving strategy and the L-module executes the intensive search or refinement required for each step. Although a standard RNN may approach convergence within $T$ iterations, the hierarchical convergence benefits from an enhanced effective depth of $NT$ steps. As empirically shown in Figure˜3, this mechanism allows HRM both to maintain high computational activity (forward residual) over many steps (in contrast to a standard RNN, whose activity rapidly decays) and to enjoy stable convergence. This translates into better performance at any computation depth, as illustrated in Figure˜2.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Approximate gradient", "weight": 1.0} -->

Recurrent models typically use BPTT to compute gradients. However, BPTT requires storing the hidden states from the forward pass and then combining them with gradients during the backward pass, which demands $O{(T)}$ memory for T timesteps. This heavy memory burden forces smaller batch sizes and leads to poor GPU utilization, especially for large-scale networks. Additionally, because retaining the full history trace through time is biologically implausible, it is unlikely that the brain implements BPTT ^^.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Approximate gradient", "weight": 1.0} -->

Fortunately, if a recurrent neural network converges to a fixed point, we can avoid unrolling its state sequence by applying backpropagation in a single step at that equilibrium point. Moreover, such a mechanism could plausibly be implemented in the brain using only local learning rules ^,\ ^. Based on this finding, we propose a one-step approximation of the HRM gradient--using the gradient of the last state of each module and treating other states as constant. The gradient path is, therefore,

<!-- chunk {"id": "body-0024", "role": "body", "section": "Approximate gradient", "weight": 1.0} -->

> Output head → final state of the H-module → final state of the L-module → input embedding

<!-- chunk {"id": "body-0025", "role": "body", "section": "Approximate gradient", "weight": 1.0} -->

The above method needs $O{}$ memory, does not require unrolling through time, and can be easily implemented with an autograd framework such as PyTorch, as shown in Figure˜4. Given that each module only needs to back-propagate errors through its most recent local synaptic activity, this approach aligns well with the perspective that cortical credit assignment relies on short-range, temporally local mechanisms rather than on a global replay of activity patterns.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Approximate gradient", "weight": 1.0} -->

with torch.no_grad:
## 1-step grad
return (zH, zL), output_head(zH)
## Deep Supervision
for x, y_true in train_dataloader:
for step in range(N_supervision):
loss = softmax_cross_entropy(y_hat, y_true)
opt.zero_grad
Figure 4: Top: Diagram of HRM with approximate gradient. Bottom: Pseudocode of HRM with deep supervision training in PyTorch.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Approximate gradient", "weight": 1.0} -->

The one-step gradient approximation is theoretically grounded in the mathematics of Deep Equilibrium Models (DEQ) ^^ which employs the Implicit Function Theorem (IFT) to bypass BPTT, as detailed next. Consider an idealized HRM behavior where, during high-level cycle $k$, the L-module repeatedly updates until its state $z_{L}$ converges to a local fixed point $z_{L}^{\star}$. This fixed point, given the current high-level state $z_{H}^{k - 1}$, can be expressed as

<!-- chunk {"id": "body-0028", "role": "body", "section": "Approximate gradient", "weight": 1.0} -->

Let $J_{\mathcal{F}} = \frac{\partial\mathcal{F}}{\partial z_{H}}$ be the Jacobian of $\mathcal{F}$, and assume that the matrix $I - J_{\mathcal{F}}$ is invertible at $z_{H}^{\star}$ and that the mapping $\mathcal{F}$ is continuously differentiable.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Approximate gradient", "weight": 1.0} -->

Calculating the above gradient requires evaluating and inverting matrix $({I - J_{\mathcal{F}}})$ that can be computationally expensive. Given the Neumann series expansion,

<!-- chunk {"id": "body-0030", "role": "body", "section": "Approximate gradient", "weight": 1.0} -->

the so-called 1-step gradient ^^ approximates the series by considering only its first term, i.e.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Approximate gradient", "weight": 1.0} -->

By substituting Equation˜3 back into Equation˜2, we arrive at the final simplified gradients.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Approximate gradient", "weight": 1.0} -->

Before defining our loss function, we must first introduce two key elements of our proposed method: deep supervision and adaptive computational time.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Deep supervision", "weight": 1.0} -->

Inspired by the principle that periodic neural oscillations regulate when learning occurs in the brain ^^, we incorporate a deep supervision mechanism into HRM, as detailed next.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Deep supervision", "weight": 1.0} -->

Given a data sample $(x,y)$, we run multiple forward passes of the HRM model, each of which we refer to as a segment. Let $M$ denote the total number of segments executed before termination. For each segment $m \in {\{ 1,\ldots,M\}}$, let $z^{m} = {(z_{H}^{mNT},z_{L}^{mNT})}$ represent the hidden state at the conclusion of segment $m$, encompassing both high-level and low-level state components.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Deep supervision", "weight": 1.0} -->

The crucial aspect of this procedure is that the hidden state $z^{m}$ is "detached" from the computation graph before being used as the input state for the next segment. Consequently, gradients from segment $m + 1$ do not propagate back through segment $m$, effectively creating a 1-step approximation of the gradient of the recursive deep supervision process ^^, ^^. This approach provides more frequent feedback to the H-module and serves as a regularization mechanism, demonstrating superior empirical performance and enhanced stability in deep equilibrium models when compared to more complex, Jacobian-based regularization techniques ^^, ^^. Figure˜4 shows pseudocode of deep supervision training.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Adaptive computational time (ACT)", "weight": 1.0} -->

The brain dynamically alternates between automatic thinking ("System 1") and deliberate reasoning ("System 2") ^^. Neuroscientific evidence shows that these cognitive modes share overlapping neural circuits, particularly within regions such as the prefrontal cortex and the default mode network ^^, ^^. This indicates that the brain dynamically modulates the "runtime" of these circuits according to task complexity and potential rewards ^^, ^^.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Adaptive computational time (ACT)", "weight": 1.0} -->

Inspired by the above mechanism, we incorporate an adaptive halting strategy into HRM that enables "thinking, fast and slow". This integration leverages deep supervision and uses the Q-learning algorithm ^^ to adaptively determine the number of segments.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Adaptive computational time (ACT)", "weight": 1.0} -->

where $\sigma$ denotes the sigmoid function applied element-wise. The halt or continue action is chosen using a randomized strategy as detailed next. Let $M_{\max}$ denote the maximum number of segments (a fixed hyperparameter) and $M_{\min}$ denote the minimum number of segments (a random variable). The value of $M_{\min}$ is determined stochastically: with probability $\varepsilon$, it is sampled uniformly from the set $\{ 2,\cdots,M_{\max}\}$ (to encourage longer thinking), and with probability $1 - \varepsilon$, it is set to 1. The halt action is selected under two conditions: when the segment count surpasses the maximum threshold $M_{\max}$, or when the estimated halt value ${\hat{Q}}_{\text{halt}}$ exceeds the estimated continue value ${\hat{Q}}_{\text{continue}}$ and the segment count has reached at least the minimum threshold $M_{\min}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Adaptive computational time (ACT)", "weight": 1.0} -->

The Q-head is updated through a Q-learning algorithm, which is defined on the following episodic Markov Decision Process (MDP). The state of the MDP at segment $m$ is $z^{m}$, and the action space is $\{\text{halt},\text{continue}\}$. Choosing the action "halt" terminates the episode and returns a binary reward indicating prediction correctness, i.e., $\mathbf{1}{\{{{\hat{y}}^{m} = y}\}}$. Choosing "continue" yields a reward of 0 and the state transitions to $z^{m + 1}$. Thus, the Q-learning targets for the two actions ${\hat{G}}^{m} = {({\hat{G}}_{\text{halt}}^{m},{\hat{G}}_{\text{continue}}^{m})}$ are given by

<!-- chunk {"id": "body-0040", "role": "body", "section": "Adaptive computational time (ACT)", "weight": 1.0} -->

We can now define the loss function of our learning procedure.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Adaptive computational time (ACT)", "weight": 1.0} -->

Minimizing the above loss enables both accurate predictions and nearly optimal stopping decisions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Adaptive computational time (ACT)", "weight": 1.0} -->

Selecting the "halt" action ends the supervision loop. In practice, sequences are processed in batches, which can be easily handled by substituting any halted sample in the batch with a fresh sample from the dataloader.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Adaptive computational time (ACT)", "weight": 1.0} -->

Figure˜5 ‣ 2 Hierarchical Reasoning Model ‣ Hierarchical Reasoning Model") presents a performance comparison between two HRM variants: one incorporating ACT and another employing a fixed computational step count equivalent to ACT's $M_{\max}$ parameter. It shows that ACT effectively adapts its computational resources based on task complexity, achieving significant computational savings with minimal impact on performance.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Inference-time scaling", "weight": 1.0} -->

An effective neural model should exploit additional computational resources during inference to enhance performance. As illustrated in Figure˜5 ‣ 2 Hierarchical Reasoning Model ‣ Hierarchical Reasoning Model")-(c), HRM seamlessly achieves inference-time scaling by simply increasing the computational limit parameter, $M_{\max}$ without requiring further training or architectural modifications.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Inference-time scaling", "weight": 1.0} -->

Additional compute is especially effective for tasks that demand deeper reasoning. On Sudoku---a problem that often requires long-term planning---HRM exhibits strong inference-time scaling. On the other hand, we find that extra computational resources yield minimal gains in ARC-AGI challenge, as solutions generally require only a few transformations.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Stability of Q-learning in ACT", "weight": 1.0} -->

The deep Q-learning that underpins our ACT mechanism is known to be prone to instability, often requiring stabilization techniques such as replay buffers and target networks ^^, which are absent in our design. Our approach, however, achieves stability through the intrinsic properties of our model and training procedure. Recent theoretical work by Gallici et al. ^^ shows that Q-learning can achieve convergence if network parameters are bounded, weight decay is incorporated during training, and post-normalization layers are implemented. Our model satisfies these conditions through its Post-Norm architecture that employs RMSNorm (a layer normalization variant) and the AdamW optimizer. AdamW has been shown to solve an $L_{\infty}$-constrained optimization problem, ensuring that model parameters remain bounded by $1/\lambda$ ^^.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Architectural details", "weight": 1.0} -->

We employ a sequence-to-sequence architecture for HRM. Both input and output are represented as token sequences: $x = {(x_{1},\ldots,x_{l})}$ and $y = {(y_{1},\ldots,y_{l^{\prime}})}$ respectively. The model includes an embedding layer $f_{I}$ that converts discrete tokens into vector representations, and an output head ${f_{O}{(z;\theta_{O})}} = {\text{softmax}{({\theta_{O}z})}}$ that transforms hidden states into token probability distributions $\hat{y}$. For small-sample experiments, we replace softmax with stablemax ^^ to improve generalization performance.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Architectural details", "weight": 1.0} -->

The sequence-to-sequence loss is averaged over all tokens, ${\text{Loss}{(\hat{y},y)}} = {\frac{1}{l^{\prime}}{\sum_{i = 1}^{l^{\prime}}{{\log p}{(y_{i})}}}}$, where $p{(y_{i})}$ is the probability that distribution ${\hat{y}}_{i}$ assigns to token $y_{i}$. The initial hidden states $z^{0}$ are initialized by sampling from a truncated normal distribution with standard deviation of 1, truncation of 2, and kept fixed throughout training.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Architectural details", "weight": 1.0} -->

Both the low-level and high-level recurrent modules $f_{L}$ and $f_{H}$ are implemented using encoder-only Transformer ^^ blocks with identical architectures and dimensions. These modules take multiple inputs, and we use straightforward element-wise addition to combine them, though more sophisticated merging techniques such as gating mechanisms could potentially improve performance and is left for future work. For all Transformer blocks in this work---including those in the baseline models---we incorporate the enhancements found in modern LLMs. These improvements include Rotary Positional Encoding ^^, Gated Linear Units ^^, RMSNorm ^^, and the removal of bias terms from linear layers.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Architectural details", "weight": 1.0} -->

Furthermore, both HRM and recurrent Transformer models implement a Post-Norm architecture with weights initialized via truncated LeCun Normal initialization ^,\,\ ^, while the scale and bias parameters are excluded from RMSNorm. All parameters are optimized using the Adam-atan2 optimizer ^^, a scale-invariant variant of Adam ^^, combined with a constant learning rate that includes linear warm-up.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Results", "weight": 1.0} -->

This section begins by describing the ARC-AGI, Sudoku, and Maze benchmarks, followed by an overview of the baseline models and their results. Figure˜6-(a,b,c) presents a visual representation of the three benchmark tasks, which are selected to evaluate various reasoning abilities in AI models.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

ARC-AGI Challenge The ARC-AGI benchmark evaluates general fluid intelligence through IQ-test-like puzzles that require inductive reasoning ^^. The initial version, ARC-AGI-1, presents challenges as input-label grid pairs that force AI systems to extract and generalize abstract rules from just a few examples. Each task provides a few input--output demonstration pairs (usually 2--3) and a test input. An AI model has two attempts to produce the correct output grid. Although some believe that mastering ARC-AGI would signal true artificial general intelligence, its primary purpose is to expose the current roadblocks in AGI progress. In fact, both conventional deep learning methods and CoT techniques have faced significant challenges with ARC-AGI-1, primarily because it requires the ability to generalize to entirely new tasks ^^.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

Addressing the limitations identified in ARC-AGI-1, ARC-AGI-2 significantly expands the benchmark by providing a more comprehensive and carefully refined collection of tasks. These new tasks emphasize deeper compositional reasoning, multi-step logic, contextual rule application, and symbolic abstraction. Human calibration studies show these tasks are challenging but doable for people, while being much harder for current AI systems, offering a clearer measure of general reasoning abilities ^^.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

Sudoku-Extreme Sudoku is a 9$\times$`<!-- -->`{=html}9 logic puzzle, requiring each row, column, and 3$\times$`<!-- -->`{=html}3 block to contain the digits 1--9 exactly once. A prediction is considered correct if it exactly matches the puzzle's unique solution. Sudoku's complex logical structure makes it a popular benchmark for evaluating logical reasoning in machine learning ^^, ^^, ^^.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

The most frequently used Sudoku dataset in research, namely the Kaggle dataset ^^, can be fully solved using elementary single-digit techniques ^^. The minimal 17-clue puzzles ^^, another widely-used collection, might seem more challenging due to its small number of clues. However, this perception is misleading---since 17 represents the minimum number of clues required to guarantee a unique Sudoku solution, these hints need to be highly orthogonal to each other. This orthogonal arrangement leads to many direct, easily-resolved solution paths ^^.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

Easy puzzles compiled from Kaggle, 17-clue, plus unbiased samples from the Sudoku puzzle distribution ^^: totaling $1\, 149\, 158$ puzzles.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

Challenging puzzles compiled from Magictour 1465, Forum-Hard and Forum-Extreme subsets: totaling $3\, 104\, 157$ puzzles.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

The compiled data then undergo a strict 90/10 train-test split, ensuring that the test set puzzles cannot be derived through equivalent transformations of any training samples. Sudoku-Extreme is a down-sampled subset of this data containing 1000 training examples. We use Sudoku-Extreme in our main experiments (Figure˜1), which focuses on small-sample learning scenarios. To guarantee convergence and control overfitting effects in our analysis experiments (Figures˜2, and ‣ 2 Hierarchical Reasoning Model ‣ Hierarchical Reasoning Model")), we use the complete training data, Sudoku-Extreme-Full, containing $3\, 831\, 994$ examples.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

We measure puzzle difficulty by counting the number of search backtracks ("guesses") required by a smart Sudoku solver program tdoku, which uses propositional logic to reduce the number of guesses ^^. Our Sudoku-Extreme dataset exhibits a mean difficulty of $22$ backtracks per puzzle, significantly higher than existing datasets, including recent handmade puzzles Sudoku-Bench ^^ which average just $0.45$ backtracks per puzzle. These subset complexity levels are shown in Figure˜6-(d).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

Maze-Hard This task involves finding the optimal path in a 30$\times$`<!-- -->`{=html}30 maze, making it interpretable and frequently used for training LLMs in search tasks ^^, ^^, ^^. We adopt the instance generation procedure of Lehnert et al. ^^, but introduce an additional filter to retain only those instances whose difficulty exceeds 110. Here, "difficulty" is defined as the length of the shortest path, which aligns with the linear time complexity of the wavefront breadth-first search algorithm on GPUs ^^. A path is considered correct if it is valid and optimal---that is, the shortest route from the start to the goal. The training and test set both include 1000 examples.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Evaluation Details", "weight": 1.0} -->

For all benchmarks, HRM models were initialized with random weights and trained in the sequence-to-sequence setup using the input-output pairs. The two-dimensional input and output grids were flattened and then padded to the maximum sequence length. The resulting performance is shown in Figure˜1. Remarkably, HRM attains these results with just \~1000 training examples per task---and without pretraining or CoT labels.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Evaluation Details", "weight": 1.0} -->

For ARC-AGI challenge, we start with all demonstration and test input-label pairs from the training set, and all demonstration pairs along with test inputs from the evaluation set. The dataset is augmented by applying translations, rotations, flips, and color permutations to the puzzles. Each task example is prepended with a learnable special token that represents the puzzle it belongs to. At test time, we proceed as follows for each test input in the evaluation set: Generate and solve 1000 augmented variants and, for each, apply the inverse‐augmentation transform to obtain a prediction. Choose the two most popular predictions as the final outputs.^33^3The ARC-AGI allows two attempts for each test input. All reported results are obtained by comparing the outputs with the withheld test labels from the evaluation set.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Evaluation Details", "weight": 1.0} -->

We augment Sudoku puzzles by applying band and digit permutations, while data augmentation is disabled for Maze tasks. Both tasks undergo only a single inference pass.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Evaluation Details", "weight": 1.0} -->

For ARC-AGI, the scores of the CoT models are taken from the official leaderboard ^^, while for Sudoku and Maze, the scores are obtained by evaluating through the corresponding API.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Evaluation Details", "weight": 1.0} -->

In Figure˜1, the baselines are grouped based on whether they are pre-trained and use CoT, or neither. The "Direct pred" baseline means using "direct prediction without CoT and pre-training", which retains the exact training setup of HRM but swaps in a Transformer architecture. Interestingly, on ARC-AGI-1, "Direct pred" matches the performance of Liao and Gu ^^, who built a carefully designed, domain-specific equivariant network for learning the ARC-AGI task from scratch, without pre-training. By substituting the Transformer architecture with HRM's hierarchical framework and implementing ACT, we achieve more than a twofold performance improvement.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Evaluation Details", "weight": 1.0} -->

On the Sudoku-Extreme and Maze-Hard benchmarks, the performance gap between HRM and the baseline methods is significant, as the baselines almost never manage to solve the tasks. These benchmarks that demand lengthy reasoning traces are particularly difficult for CoT-based methods. With only 1000 training examples, the "Direct pred" baseline---which employs an 8-layer Transformer identical in size to HRM---fails entirely on these challenging reasoning problems. When trained on the larger Sudoku-Extreme-Full dataset, however, "Direct pred" can solve some easy Sudoku puzzles and reaches $16.9\%$ accuracy (see Figure˜2). Lehnert et al. ^^ showed that a large vanilla Transformer model with 175M parameters, trained on 1 million examples across multiple trials, achieved only marginal success on 30x30 Maze tasks, with accuracy below $20\%$ using the $pass@64$ evaluation metric.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Visualization of intermediate timesteps", "weight": 1.0} -->

Although HRM demonstrates strong performance on complex reasoning tasks, it raises an intriguing question: what underlying reasoning algorithms does the HRM neural network actually implement? Addressing this question is important for enhancing model interpretability and developing a deeper understanding of the HRM solution space.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Visualization of intermediate timesteps", "weight": 1.0} -->

While a definitive answer lies beyond our current scope, we begin our investigation by analyzing state trajectories and their corresponding solution evolution. More specifically, at each timestep $i$ and given the low-level and high-level state pair ($z_{L}^{i}$ and $z_{H}^{i}$) we perform a preliminary forward pass through the H-module to obtain ${\overline{z}}^{i} = {f_{H}{(z_{H}^{i},z_{L}^{i};\theta_{H})}}$ and its corresponding decoded prediction ${\overline{y}}^{i} = {f_{O}{({\overline{z}}^{i};\theta_{O})}}$. The prediction ${\overline{y}}^{i}$ is then visualized in Figure˜7.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Visualization of intermediate timesteps", "weight": 1.0} -->

In the Maze task, HRM appears to initially explore several potential paths simultaneously, subsequently eliminating blocked or inefficient routes, then constructing a preliminary solution outline followed by multiple refinement iterations. In Sudoku, the strategy resembles a depth-first search approach, where the model appears to explore potential solutions and backtracks when it hits dead ends. HRM uses a different approach for ARC tasks, making incremental adjustments to the board and iteratively improving it until reaching a solution. Unlike Sudoku, which involves frequent backtracking, the ARC solution path follows a more consistent progression similar to hill-climbing optimization.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Visualization of intermediate timesteps", "weight": 1.0} -->

Importantly, the model shows that it can adapt to different reasoning approaches, likely choosing an effective strategy for each particular task. Further research is needed to gain more comprehensive insights into these solution strategies.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Brain Correspondence", "weight": 1.0} -->

A key principle from systems neuroscience is that a brain region's functional repertoire---its ability to handle diverse and complex tasks---is closely linked to the dimensionality of its neural representations ^^, ^^. Higher-order cortical areas, responsible for complex reasoning and decision-making, must handle a wide variety of tasks, demanding more flexible and context-dependent processing ^^. In dynamical systems, this flexibility is often realized through higher-dimensional state-space trajectories, which allow for a richer repertoire of potential computations ^^. This principle gives rise to an observable *dimensionality hierarchy*, where a region's position in the processing hierarchy correlates with its *effective dimensionality*. To quantify this phenomenon, we can examine the Participation Ratio (PR), which serves as a standard measure of the effective dimensionality of a high-dimensional representation ^^. The PR is calculated using the formula

<!-- chunk {"id": "body-0072", "role": "body", "section": "Brain Correspondence", "weight": 1.0} -->

where $\{\lambda_{i}\}$ are the eigenvalues of the covariance matrix of neural trajectories. Intuitively, a higher PR value signifies that variance is distributed more evenly across many dimensions, corresponding to a higher-dimensional representation. Conversely, a lower PR value indicates that variance is concentrated in only a few principal components, reflecting a more compact, lower-dimensional structure.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Brain Correspondence", "weight": 1.0} -->

The dimensionality hierarchy can be observed, for example, in the mouse cortex, where the PR of population activity increases monotonically from low-level sensory areas to high-level associative areas, supporting this link between dimensionality and functional complexity ^^ (Figure˜8 (a,b)).

<!-- chunk {"id": "body-0074", "role": "body", "section": "Brain Correspondence", "weight": 1.0} -->

We evaluated whether HRM reproduces this neuroscientific principle by calculating the PR for both recurrent modules after training on the Sudoku-Extreme Full dataset. The PR computation used the covariance matrix derived from neural states gathered across multiple Sudoku-solving trajectories. The results show a striking parallel to the biological findings. The low-level module's state ($z_{L}$) occupies a relatively small subspace with a participation ratio of 30.22, whereas the high-level module's state ($z_{H}$) operates in a substantially larger subspace with a participation ratio of 89.95, as shown in Figure˜8(c). Furthermore, Figure˜8(d) shows that increasing the number of unique tasks (trajectories) from 10 to 100 causes $z_{H}$ dimensionality to scale up accordingly, while $z_{L}$ dimensionality remains stable. These results suggest an *emergent* separation of representational capacity between the modules that parallels their functional roles.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Brain Correspondence", "weight": 1.0} -->

To confirm that this hierarchical organization is an emergent property of training, and not an artifact of the network's architecture, we performed a control analysis using an identical but untrained network with random weights.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Brain Correspondence", "weight": 1.0} -->

We initialized an identical HRM architecture with random weights and, without any training, measured the PR of its modules as the network processed the same task-specific inputs given to the trained model.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Brain Correspondence", "weight": 1.0} -->

The results, shown in Figure˜8(e,f), reveal a stark contrast: the high-level and low-level modules of the untrained network exhibit no hierarchical separation, with their PR values remaining low and nearly indistinguishable from each other. This control analysis validates that the dimensionality hierarchy is an *emergent property* that arises as the model learns to perform complex reasoning.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Brain Correspondence", "weight": 1.0} -->

The high-to-low PR ratio in HRM (${z_{H}/z_{L}} \approx 2.98$) closely matches that measured in the mouse cortex ($\approx 2.25$). In contrast, conventional deep networks often exhibit *neural collapse*, where last-layer features converge to a low-dimensional subspace ^^, ^^, ^^. HRM therefore departs from the collapse pattern and instead fosters a high-dimensional representation in its higher module. This is significant because such representations are considered crucial for cognitive flexibility and are a hallmark of higher-order brain regions like the prefrontal cortex (PFC), which is central to complex reasoning.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Brain Correspondence", "weight": 1.0} -->

This structural parallel suggests the model has discovered a fundamental organizational principle. By learning to partition its representations into a high-capacity, high-dimensional subspace ($z_{H}$) and a more specialized, low-dimensional one ($z_{L}$), HRM autonomously discovers an organizational principle that is thought to be fundamental for achieving robust and flexible reasoning in biological systems. This provides a potential mechanistic explanation for the model's success on complex, long-horizon tasks that are intractable for models lacking such a differentiated internal structure. We emphasize, however, that this evidence is correlational. While a causal link could be tested via intervention (e.g., by constraining the H-module's dimensionality), such methods are difficult to interpret in deep learning due to potential confounding effects on the training process itself. Thus, the causal necessity of this emergent hierarchy remains an important question for future investigation.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Reasoning and algorithm learning", "weight": 1.0} -->

Given the central role of reasoning problems and their close relation to algorithms, researchers have long explored neural architectures that enable algorithm learning from training instances. This line of work includes Neural Turing Machines (NTM) ^^, the Differentiable Neural Computer (DNC) ^^, and Neural GPUs ^^--all of which construct iterative neural architectures that mimic computational hardware for algorithm execution, and are trained to learn algorithms from data. Another notable work in this area is Recurrent Relational Networks (RRN) ^^, which executes algorithms on graph representations through graph neural networks.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Reasoning and algorithm learning", "weight": 1.0} -->

Recent studies have integrated algorithm learning approaches with Transformer-based architectures. Universal Transformers extend the standard Transformer model by introducing a recurrent loop over the layers and implementing an adaptive halting mechanism. Geiping et al. ^^ demonstrate that looped Transformers can generalize to a larger number of recurrent steps during inference than what they were trained. Shen et al. ^^ propose adding continuous recurrent reasoning tokens to the Transformer. Finally, TransNAR ^^ combine recurrent graph neural networks with language models.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Reasoning and algorithm learning", "weight": 1.0} -->

Building on the success of CoT-based reasoning, a line of work have introduced fine-tuning methods that use reasoning paths from search algorithms (like A\*) as SFT targets ^,\,\ ^.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Reasoning and algorithm learning", "weight": 1.0} -->

We also mention adaptive halting mechanisms designed to allocate additional computational resources to more challenging problems. This includes the Adaptive Computation Time (ACT) for RNNs ^^ and follow-up research like PonderNet ^^, which aims to improve the stability of this allocation process.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Reasoning and algorithm learning", "weight": 1.0} -->

HRM further pushes the boundary of algorithm learning through a brain-inspired computational architecture that achieves exceptional data efficiency and model expressiveness, successfully discovering complex and diverse algorithms from just 1000 training examples.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Brain-inspired reasoning architectures", "weight": 1.0} -->

Developing a model with the reasoning power of the brain has long been a goal in brain-inspired computing. Spaun ^^ is one notable example, which uses spiking neural networks to create distinct modules corresponding to brain regions like the visual cortex and prefrontal cortex. This design enables an architecture to perform a range of cognitive tasks, from memory recall to simple reasoning puzzles. However, its reasoning relies on hand-designed algorithms, which may limit its ability to learn new tasks. Another significant model is the Tolman-Eichenbaum Machine (TEM) ^^, which is inspired by the hippocampal-entorhinal system's role in spatial and relational memory tasks. TEM proposes that medial entorhinal cells create a basis for structural knowledge, while hippocampal cells link this basis to sensory information. This allows TEM to generalize and explains the emergence of various cell types like grid, border, and place cells. Another approach involves neural sampling models ^^, which view the neural signaling process as inference over a distribution, functioning similarly to a Boltzmann machine. These models often require hand-made rules to be set up for solving a specific reasoning task.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Brain-inspired reasoning architectures", "weight": 1.0} -->

In essence, while prior models are restricted to simple reasoning problems, HRM is designed to solve complex tasks that are hard for even advanced LLMs, without pre-training or task-specific manual design.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Hierarchical memory", "weight": 1.0} -->

The hierarchical multi-timescale structure also plays an important role in how the brain processes memory. Models such as Hierarchical Sequential Models ^^ and Clockwork RNN ^^ use multiple recurrent modules that operate at varying time scales to more effectively capture long-range dependencies within sequences, thereby mitigating the forgetting issue in RNNs.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Hierarchical memory", "weight": 1.0} -->

Similar mechanisms have also been adopted in linear attention methods for memorizing long contexts (see the Discussions section). Since HRM focuses on reasoning, full attention is applied for simplicity. Incorporating hierarchical memory into HRM could be a promising future direction.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Turing-completeness of HRM", "weight": 1.0} -->

Like earlier neural reasoning algorithms including the Universal Transformer ^^, HRM is computationally universal when given sufficient memory and time constraints. In other words, it falls into the category of models that can simulate any Turing machine, overcoming the computational limitations of standard Transformers discussed previously in the introduction. Given that earlier neural algorithm reasoners were trained as recurrent neural networks, they suffer from premature convergence and memory intensive BPTT. Therefore, in practice, their effective computational depth remains limited, though still deeper than that of a standard Transformer. By resolving these two challenges and being equipped with adaptive computation, HRM could be trained on long reasoning processes, solve complex puzzles requiring intensive depth-first search and backtracking, and move closer to practical Turing-completeness.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Reinforcement learning with chain-of-thought", "weight": 1.0} -->

Beyond fine-tuning using human-annotated CoT, reinforcement learning (RL) represents another widely adopted training methodology. However, recent evidence suggests that RL primarily unlocks existing CoT-like capabilities rather than discovering fundamentally new reasoning mechanisms ^^, ^^, ^^, ^^. Additionally, CoT-training with RL is known for its instability and data inefficiency, often requiring extensive exploration and careful reward design. In contrast, HRM takes feedback from dense gradient-based supervision rather than relying on a sparse reward signal. Moreover, HRM operates naturally in a continuous space, which is biologically plausible and avoids allocating same computational resources to each token, even though tokens vary in their reasoning and planning complexity ^^.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Linear attention", "weight": 1.0} -->

Recurrence has been explored not only for its capability in universal computation, but also as a means to replace the attention mechanism in Transformers, which suffers from quadratic time and memory complexity ^^. Recurrent alternatives offer a more efficient design by processing input tokens sequentially and predicting the next token at each time step, similar to early RNN-based language models.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Linear attention", "weight": 1.0} -->

Some linear-attention variants, such as Log-linear Attention ^^, share an RNN-like state-update that can be interpreted as propagating multi-timescale summary statistics, thereby retaining long-range context without the quadratic memory growth of standard self-attention. However, substituting the attention mechanism alone does not change the fact that Transformers are still fixed-depth, and require CoT as a compensatory mechanism. Notably, linear attention can operate with a reduced key-value cache over extended contexts, making them more suitable for deployment on resource-constrained edge devices.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This work introduces the Hierarchical Reasoning Model, a brain-inspired architecture that leverages hierarchical structure and multi-timescale processing to achieve substantial computational depth without sacrificing training stability or efficiency. With only 27M parameters and training on just 1000 examples, HRM effectively solves challenging reasoning problems such as ARC, Sudoku, and complex maze navigation--tasks that typically pose significant difficulties for contemporary LLM and chain-of-thought models.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Although the brain relies heavily on hierarchical structures to enable most cognitive processes, these concepts have largely remained confined to academic literature rather than being translated into practical applications. The prevailing AI approach continues to favor non-hierarchical models. Our results challenge this established paradigm and suggest that the Hierarchical Reasoning Model represents a viable alternative to the currently dominant chain-of-thought reasoning methods, advancing toward a foundational framework capable of Turing-complete universal computation.
