Green AI

Topics include Green artificial intelligence, Sustainable artificial intelligence, Machine learning efficiency, Deep learning, Carbon footprint, Computational cost, Model evaluation, Energy efficiency, Research incentives, Artificial intelligence accessibility.

Schwartz, Dodge, Smith, and Etzioni introduce the Green AI framing, arguing that machine learning research should report and optimize computational efficiency rather than rewarding accuracy at any compute cost. The paper is influential because it gives the community a compact vocabulary for the environmental and equity costs of deep learning, and it helped make compute, energy, and financial cost routine considerations in later AI evaluation and reporting work.

The computations required for deep learning research have been doubling every few months, resulting in an estimated 300,000x increase from 2012 to 2018. These computations have a surprisingly large carbon footprint. Ironically, deep learning was inspired by the human brain, which is remarkably energy efficient. Moreover, the financial cost of the computations can make it difficult for academics, students, and researchers, in particular those from emerging economies, to engage in deep learning research. This position paper advocates a practical solution by making efficiency an evaluation criterion for research alongside accuracy and related measures. In addition, we propose reporting the financial cost or "price tag" of developing, training, and running models to provide baselines for the investigation of increasingly efficient methods. Our goal is to make AI both greener and more inclusive - enabling any inspired undergraduate with a laptop to write high-quality research papers.

## Introduction and Motivation

Since 2012, the field of artificial intelligence has reported remarkable progress on a broad range of capabilities including object recognition, game playing, machine translation, and more. This progress has been achieved by increasingly large and computationally-intensive deep learning models.^11^1For brevity, we refer to AI throughout this paper, but our focus is on AI research that relies on deep learning methods. Figure 1 reproduced from plots training cost increase over time for state-of-the-art deep learning models starting with AlexNet in 2012 to AlphaZero in 2017....

Figure 1: The amount of compute used to train deep learning models has increased 300,000x in 6 years. Figure taken from.

Data efficiency has received significant attention over the years. Modern research in vision and NLP often involves first pretraining a model on large ''raw'' (unannotated) data then fine-tuning it to a task of interest through supervised learning. A strong result in this area often involves achieving similar performance to a baseline with fewer training examples or fewer gradient steps. Most recent work has addressed fine-tuning data, but pretraining efficiency is also important. In either case, one simple technique to improve in this area is to simply report performance with different amounts of training data....

Finally, the total number of experiments run to get a final result is often underreported and underdiscussed. The few instances researchers have of full reporting of the hyperparameter search, architecture evaluations, and ablations that went into a reported experimental result have surprised the community. While many hyperparameter optimization algorithms exist which can reduce the computational expense required to reach a given level of performance, simple improvements here can have a large impact. For example, stopping training early for models which are clearly underperforming can lead to great savings.

### Carbon emission

The use of massive data creates barriers for many researchers for reproducing the results of these models, or training their own models on the same setup (especially as training for multiple epochs is standard). For example, the June 2019 Common Crawl contains 242 TB of uncompressed data,^1212^12[ so even storing the data is expensive....
