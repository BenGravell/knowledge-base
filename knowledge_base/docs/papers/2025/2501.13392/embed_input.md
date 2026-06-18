Time Series Embedding Methods for Classification Tasks: A Review

Topics include Deep learning, Classification, Time series, Datasets, Learning, Tasks.

Time series analysis has become crucial in various fields, from engineering and finance to healthcare and social sciences. Due to their multidimensional nature, time series often need to be embedded into a fixed-dimensional feature space to enable processing with various machine learning algorithms. In this paper, we present a comprehensive review and quantitative evaluation of time series embedding methods for effective representations in machine learning and deep learning models. We introduce a taxonomy of embedding techniques, categorizing them based on their theoretical foundations and application contexts. Our work provides a quantitative evaluation of representative methods from each category by assessing their performance on downstream classification tasks across diverse real-world datasets. Our experimental results demonstrate that the performance of embedding methods varies significantly depending on the dataset and classification algorithm used, highlighting the importance of careful model selection and extensive experimentation for specific applications.

## Introduction

Time series embedding is a technique used to represent time series data in the form of vector embeddings. Today, time series analysis methods have emerged as a fundamental element across a vast amount of applications ranging from finance, as in the work of Zhu and Huang, to healthcare, as demonstrated in Nejedly et al.; Morid et al.; Chen et al.; Lee and Hauskrecht; Soenksen et al., engineering applications such as machine health monitoring, predictive maintenance, and fault detection Zhao et al.; Li et al., and social sciences, explored by Santosh et al..

The

Previous surveys on time series embeddings, such as the one published by Tjøstheim et al., have provided a qualitative categorization of the various methods but have not quantitatively evaluated the representation capability of each method on real-world data. In this work, we evaluate popular time series embedding methods by using the formed embeddings on downstream classification tasks, which provides a crucial perspective on their effectiveness and generalization capabilities. Classification tasks serve as an excellent proxy for assessing how well embeddings capture discriminative features and preserve relevant temporal patterns.

The remainder of this paper is organized as follows. In section, we provide a brief overview of the different time series embedding categories that form our taxonomy as a background. In section, we detail the machine learning pipeline that we followed to evaluate each method quantitatively as well as a more detailed theoretical description of each embedding method evaluated in this study. In section, we present the experimental results along with a discussion of our observations. Finally, section concludes this paper.

## Conclusion

This comprehensive study evaluates various time series embedding methods across different datasets and classification tasks, revealing important insights into their relative strengths and limitations. Our analysis demonstrates that while embedding method performance varies significantly based on dataset characteristics and downstream tasks, classical methods like PCA and Fourier transforms consistently offer robustness and interpretability for datasets with prominent global patterns.
