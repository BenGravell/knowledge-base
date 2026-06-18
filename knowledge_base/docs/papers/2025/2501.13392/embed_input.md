Time Series Embedding Methods for Classification Tasks: A Review

Topics include Deep learning, Classification, Time series, Datasets, Learning, Tasks.

Time series analysis has become crucial in various fields, from engineering and finance to healthcare and social sciences. Due to their multidimensional nature, time series often need to be embedded into a fixed-dimensional feature space to enable processing with various machine learning algorithms. In this paper, we present a comprehensive review and quantitative evaluation of time series embedding methods for effective representations in machine learning and deep learning models. We introduce a taxonomy of embedding techniques, categorizing them based on their theoretical foundations and application contexts. Our work provides a quantitative evaluation of representative methods from each category by assessing their performance on downstream classification tasks across diverse real-world datasets. Our experimental results demonstrate that the performance of embedding methods varies significantly depending on the dataset and classification algorithm used, highlighting the importance of careful model selection and extensive experimentation for specific applications....

## Introduction

Time series embedding is a technique used to represent time series data in the form of vector embeddings. Today, time series analysis methods have emerged as a fundamental element across a vast amount of applications ranging from finance, as in the work of Zhu and Huang, to healthcare, as demonstrated in Nejedly et al.; Morid et al.; Chen et al.; Lee and Hauskrecht; Soenksen et al., engineering applications such as machine health monitoring, predictive maintenance, and fault detection Zhao et al.; Li et al., and social sciences, explored by Santosh et al.....

The importance of studying and evaluating different time series embedding methods stems from several key factors:

The selection between classical and complex embedding methods inherently involves trade-offs between simplicity, interpretability, computational efficiency, and pattern-capturing ability. Our findings emphasize the importance of adopting a tailored approach that carefully considers the specific characteristics of the data and intended analysis goals. The varying effectiveness of topological and graph-based methods across different applications suggests promising avenues for future development, particularly in handling complex, multi-dimensional time series data.

Through the provision of an open-source suite implementing these embedding methods, we aim to facilitate further advancements in time series analysis across various fields. Future research directions include developing hybrid and adaptive embedding methods, improving interpretability of complex techniques, and extending the evaluation to other domains, ultimately contributing to the broader understanding and application of these tools.

where $x_{n}$ is the input signal at time step $n$, $X_{k}$ is the DFT coefficient at frequency $k$, $N$ is the length of the signal, and $i$ is the imaginary unit.

These diverse datasets allow us to evaluate the performance of our embedding methods across different domains and time series characteristics.

Each normalized segment ${\overset{\sim}{s}}_{i,j}$ is processed using a Recurrent Neural Network (RNN) to capture temporal dependencies. The RNN updates its hidden state $h_{i,j,k}$ at each time step $k$:

*Dimensionality reduction*: Time series data often has high dimensionality, which can lead to computational challenges and the curse of dimensionality....
