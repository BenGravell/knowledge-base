Action Chunking and Exploratory Data Collection Yield Exponential Improvements in Behavior Cloning for Continuous Control

Topics include Imitation learning, Robotics, Stability analysis, Benchmarks, Control, Learning.

This paper presents a theoretical analysis of two of the most impactful interventions in modern learning from demonstration in robotics and continuous control: the practice of action-chunking (predicting sequences of actions in open-loop) and exploratory augmentation of expert demonstrations. Though recent results show that learning from demonstration, also known as imitation learning (IL), can suffer errors that compound exponentially with task horizon in continuous settings, we demonstrate that action chunking and exploratory data collection circumvent exponential compounding errors in different regimes. Our results identify control-theoretic stability as the key mechanism underlying the benefits of these interventions. On the empirical side, we validate our predictions and the role of control-theoretic stability through experimentation on popular robot learning benchmarks....

## Introduction

Imitation learning (IL) is the problem of learning complex behaviors from data labeled with actions from an expert demonstrator policy. This methodology encompasses both some of the earliest examples and most recent state-of-the-art in control for autonomous robotic systems (Pomerleau Ross and Bagnell Bojarski et al. Teng et al. Zhao et al., ). Following the rise of large language models (LLMs), IL has also become increasingly prevalent in settings where an agent predicts *discrete tokens*, such as words in a sentence, lines in a proof, or positions on a chessboard....

The recent and dramatic successes of imitation learning in continuous control applications has coincided with a range of algorithmic interventions which appear essential to ensure strong performance: 1. the prediction of open-loop sequences, or "chunks" of actions by the control policy, called *action-chunking* (AC), 2. the careful curation of expert data to be imitated and 3. the adoption of *generative* neural architectures (e.g. conditional diffusion models ) as parameterizations of learned policies. While the benefits of 3....

## Discussion and Limitations

Our action-chunking guarantees rely on a structural assumption of ${(\hat{},\hat{f})} \in \mathcal{P}$ being an EISS pair. We believe either explicitly enforcing this, e.g., via regularization (Sindhwani et al. Mehta et al., ) or hierarchy, or attaining it indirectly via implicit biases, are interesting directions of inquiry. We assume smoothness in Section˜4, which is not strictly satisfied in some applications, such as in model-predictive control. We remark our lower bound Proposition˜4.1....

## Noise Injection Mitigates Compounding Error under Smooth, Unstable Dynamics

### Practice 1 (Learning over Chunked Policies)

Though the Gramian provides a notion of local exploration, fully realizing its benefits requires certain crucial subtleties not captured in prior literature.

In this work, we provide the first theoretical guarantees justifying the practices of AC and exploratory data augmentation during expert data collection (defined formally below) in the minimal setting of imitation of an expert in a state-based continuous-control problem....
