<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Time Series Embedding Methods for Classification Tasks: A Review

Topics include Deep learning, Classification, Time series, Datasets, Learning, Tasks.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Time series analysis has become crucial in various fields, from engineering and finance to healthcare and social sciences. Due to their multidimensional nature, time series often need to be embedded into a fixed-dimensional feature space to enable processing with various machine learning algorithms. In this paper, we present a comprehensive review and quantitative evaluation of time series embedding methods for effective representations in machine learning and deep learning models. We introduce a taxonomy of embedding techniques, categorizing them based on their theoretical foundations and application contexts. Our work provides a quantitative evaluation of representative methods from each category by assessing their performance on downstream classification tasks across diverse real-world datasets. Our experimental results demonstrate that the performance of embedding methods varies significantly depending on the dataset and classification algorithm used, highlighting the importance of careful model selection and extensive experimentation for specific applications. To facilitate further research and practical applications, we provide an open-source code repository implementing these embedding methods. This study contributes to the field by offering a systematic comparison of time series embedding techniques, guiding practitioners in selecting appropriate methods for their specific applications, and providing a foundation for future advancements in time series analysis.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Time series embedding is a technique used to represent time series data in the form of vector embeddings. Today, time series analysis methods have emerged as a fundamental element across a vast amount of applications ranging from finance, as in the work of Zhu and Huang, to healthcare, as demonstrated in Nejedly et al.; Morid et al.; Chen et al.; Lee and Hauskrecht; Soenksen et al., engineering applications such as machine health monitoring, predictive maintenance, and fault detection Zhao et al.; Li et al., and social sciences, explored by Santosh et al.. As machine learning and deep learning techniques continue to advance, there is a growing need for effective methods to represent and analyze time series data in these models. Tasks such as anomaly detection, classification, pattern recognition, prediction, and decision-making now heavily rely on robust methods that could accurately embed these often high-dimensional data into scalable yet informative representations.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The importance of studying and evaluating different time series embedding methods stems from several key factors: *Dimensionality reduction*: Time series data often has high dimensionality, which can lead to computational challenges and the curse of dimensionality. Effective embedding methods can reduce the dimensionality while preserving essential temporal patterns and relationships.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Feature extraction*: Embeddings can automatically extract relevant features from raw time series data, potentially capturing complex temporal dependencies that may not be apparent in the original representation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Improved model performance*: Well-designed embeddings can lead to significant improvements in the performance of downstream machine learning tasks, such as classification, clustering, and forecasting.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Transfer learning*: Embeddings learned from large datasets can be transferred to smaller, related datasets, enabling more effective learning in scenarios with limited data.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Interpretability*: Some embedding methods can provide insights into the underlying structure and patterns of time series data, aiding in data exploration and understanding.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Handling irregularities*: Many real-world time series datasets are characterized by irregular sampling, missing values, or varying lengths. Certain embedding methods can address these challenges more effectively than others.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

As the field of time series analysis continues to evolve, a wide array of embedding methods has been proposed, each with its own strengths and limitations. These methods range from classical approaches like delay embeddings and Fourier transforms to more recent techniques leveraging deep learning architectures such as recurrent neural networks and transformer models. Given the diversity of available methods and their potential impact on downstream applications, a comprehensive evaluation and comparison of time series embedding techniques is crucial. This survey aims to provide an overview of the current landscape of time series embedding methods, assess their representation strength when combined with various classification algorithms, and offer insights into selecting appropriate embedding techniques for specific applications.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Creating a taxonomy for time series embedding methods can be approached in several different ways, depending on the criteria or perspectives one chooses to emphasize. Those can be based on the theoretical foundations or mathematical principles used, domain of information captured, model complexity and computational requirements, scalability and data requirements, nature of time series data (uni-/muti-variate), application context, etc. In this work, we choose to categorize embeddings mainly based on their theoretical foundations and application context, creating a taxonomy of different categories as depicted in Figure 1 and in more detail in Table 1.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

DFT: Transforms the series into frequency components, using dominant frequencies as embeddings. DWT: Captures time and frequency characteristics using wavelet coefficients.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hand-Crafted: Statistical: Extracts mean, variance, skewness, etc. Time-Domain: Identifies peaks, troughs, zero-crossings. Frequency-Domain: Captures spectral power, dominant freqs.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Automated: TSFRESH: Extracts a wide range of features automatically. catch22: Provides 22 efficient time series characteristics.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

AR/ARMA/ARIMA: Uses past values and moving averages to model the series. HMM: Represents the series as a sequence of hidden states with probabilistic transitions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

KPCA: Extends PCA with kernel methods for non-linear relationships. DTW Kernel: Measures similarity between series, accounting for temporal distortions.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Visibility Graphs: Converts data into a graph, with embeddings from graph properties. Recurrence Networks: Uses recurrence plots to construct networks for embedding.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

Manifold Learning and Nonlinear Dimensionality Reduction t-SNE: Preserves local structure in lower-dimensional embeddings. UMAP: Provides non-linear embeddings while preserving structure. Isomap: Captures intrinsic geometry by preserving geodesic distances. LLE: Maps the series onto a lower-dimensional manifold, preserving local structure.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

Persistence Homology: Captures topological features across scales using persistence diagrams. Sliding Window with TDA: Applies TDA on time-delay embeddings to capture dynamics. Mapper Algorithm: Constructs a topological network representing the data’s shape. Takens’ Embedding with TDA: Reconstructs the phase space and applies TDA.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autoencoders: Compress and reconstruct series, with embeddings from the bottleneck layer. RNNs: Capture temporal dependencies using hidden state embeddings. CNNs: Extract local patterns through convolution, creating feature embeddings. Attention-Based Models: Focus on relevant parts of the series for embedding.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

Classical + Deep Learning: Combines traditional methods with deep learning for robust embeddings. Multi-View Embeddings: Integrates multiple perspectives, transformations, or models.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our experimental evaluation shows that the representation capabilities of various embedding methods can vary across different datasets and classification algorithms. This emphasizes the need for extensive experimentation and model selection to highlight the best combination of embedding and classification algorithms for the particular task at hand. Along with this evaluation, we provide an open-source suite that implements these embedding methods for use by the research community.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows. In section 2, we provide a brief overview of the different time series embedding categories that form our taxonomy as a background. In section 3, we detail the machine learning pipeline that we followed to evaluate each method quantitatively as well as a more detailed theoretical description of each embedding method evaluated in this study. In section 4, we present the experimental results along with a discussion of our observations. Finally, section 6 concludes this paper.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Statistical Methods", "weight": 1.0} -->

Statistical methods have been fundamental to time series analysis for decades. Principal Component Analysis (PCA), as established in the foundational works of Pearson; Hotelling, is one of the earliest techniques that reduces dimensionality by identifying orthogonal axes with maximum variance, allowing for a compact representation of time series data. Building on this work, research by Comon introduced Independent Component Analysis (ICA), which extends this by decomposing time series into statistically independent components, particularly useful in fields like neuroscience and signal processing, where uncovering hidden sources is essential. The work of Hotelling developed Canonical Correlation Analysis (CCA), which identifies linear relationships between two sets of variables, making it valuable for capturing common patterns across multiple time series. As demonstrated in the work of Klein, these methods provide robust, interpretable embeddings that serve as a strong foundation for more complex analyses or as standalone tools for time series exploration.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Transformation-Based Methods", "weight": 1.0} -->

Transformation-based methods like the Fourier Transform (FT) and Wave-let Transform (WT) have been instrumental in revealing patterns within time series data that are not visible in the time domain alone, as shown in the work of Michau et al.. According to the analysis of Sneddon, the Fourier Transform decomposes a series into its constituent frequencies, making it suitable for analyzing periodic components. However, it assumes stationarity, limiting its effectiveness for non-stationary data. The seminal works of Morlet et al.; Grossman and Morlet; Meyer introduced the Wavelet Transform as a more versatile alternative, capturing both time and frequency information, making it more suitable for analyzing non-stationary and transient signals.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Feature-Based Methods", "weight": 1.0} -->

Feature-based methods involve extracting key characteristics from time series data, either manually or automatically. Hand-crafted features can include statistical measures like mean and variance, or more complex time-domain and frequency-domain features. Recent advances such as TSFRESH by Christ et al. and catch22 by Lubba et al. provide a more systematic approach to feature extraction, offering a wide range of features tailored to different types of time series data Christ et al.; Lubba et al.. These methods are particularly useful in scenarios where domain knowledge is limited, allowing for the extraction of informative features without manual intervention.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Model-Based Methods", "weight": 1.0} -->

Model-based methods represent time series as sequences of states or as outputs of generative models. As explored in the works of Buxton et al.; Harvey, Autoregressive (AR) and ARIMA models are traditional examples, while more complex methods like Hidden Markov Models (HMMs) capture the probabilistic transitions between different states in the series. Even though autoregressive methods are often classified as statistical processes, due to the fact that they are built on statistical concepts like autocorrelation and moving averages, these methods explicitly model the underlying process generating the time series, assuming a specific structure for the data-generating process and creating a mathematical model of the time series for forecasting and analysis. These models are powerful for time series with underlying state-based dynamics but require assumptions about the underlying processes, which may not always hold.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Kernel-Based Methods", "weight": 1.0} -->

Kernel-based methods extend classical statistical techniques like PCA to capture non-linear relationships within time series data. The foundational work of Schölkopf et al. introduced Kernel PCA, which projects data into a higher-dimensional space where linear separation becomes possible. Building on this approach, research by Berndt and Clifford developed techniques like the Dynamic Time Warping (DTW) kernel to measure similarity between time series by accounting for temporal distortions, making them robust to variations in speed and amplitude. These methods are effective in capturing complex, non-linear structures in the data but can be computationally intensive.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Graph-Based Methods", "weight": 1.0} -->

Graph-based methods, including Visibility Graphs and Recurrence Networks, convert time series data into graphical representations where the nodes represent data points, and edges represent relationships between them. As demonstrated by Lacasa et al., these methods leverage graph theory to analyze the structural properties of time series, offering insights that traditional methods may overlook. According to the work of Donner et al.; Lacasa et al., visibility graphs transform a time series into a graph by connecting nodes based on their visibility, while recurrence networks analyze the recurrence of states within the series. Recent work by Kutluana and Türker has used these concepts for studying complex time series data, discussing how methods such as visibility graphs appear to be robust to noise. As shown by Liu et al., contrary to other embedding methods, the visibility graph formation does not require the tuning of its parameters. These methods are also particularly useful in studying the underlying dynamics of complex systems.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Manifold Learning and Nonlinear Dimensionality Reduction", "weight": 1.0} -->

Manifold learning methods, as developed by Roweis and Saul, der Maaten and Hinton, Tenenbaum et al., and McInnes et al., including approaches like Locally Linear Embedding (LLE), t-SNE, Isomap, and UMAP, are designed to uncover the underlying structure of high-dimensional time series data by preserving local and global geometric properties in a lower-dimensional space Roweis and Saul; der Maaten and Hinton; Tenenbaum et al.; McInnes et al.. These methods are particularly effective for visualizing high-dimensional data and for capturing complex, non-linear relationships that traditional linear methods cannot handle. However, they may require careful tuning of parameters and are sensitive to noise and uneven sampling.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Topological Methods", "weight": 1.0} -->

Topological Data Analysis (TDA) offers a unique perspective by capturing the shape of data. As explored in the works of Edelsbrunner et al.; Singh et al., techniques like Persistent Homology and the Mapper Algorithm focus on identifying topological features that are stable across different scales of analysis. These methods are valuable for understanding the global structure of time series data, particularly in applications where the shape of data plays a crucial role, such as in dynamical systems and complex networks.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Deep Learning-Based Methods", "weight": 1.0} -->

Deep learning methods have revolutionized time series embedding by leveraging neural networks to learn complex, hierarchical representations. The work of Hochreiter and Schmidhuber introduced Recurrent Neural Networks (RNNs) and their variants like Long Short-Term Memory (LSTM) networks, which are particularly suited for capturing temporal dependencies. As shown by Krizhevsky et al., Convolutional Neural Networks (CNNs), originally designed for image processing, have also been adapted for time series by treating the series as a one-dimensional grid. More recently, research by Vaswani et al. demonstrated how attention-based models like Transformers show promise in modeling long-range dependencies in time series data. These methods excel in tasks where large amounts of labeled data are available but may suffer from overfitting and require significant computational resources.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Hybrid Methods", "weight": 1.0} -->

Hybrid methods combine the strengths of multiple embedding techniques to address the limitations of individual methods. As demonstrated by Li et al., combining statistical methods with deep learning can enhance interpretability while retaining the powerful feature extraction capabilities of neural networks. Other approaches integrate multiple perspectives, such as combining time-domain and frequency-domain features, or using graph-based embeddings alongside traditional machine learning models. Hybrid methods are often tailored to specific applications, making them versatile but potentially complex to implement.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Hybrid Methods", "weight": 1.0} -->

The diverse landscape of time series embedding methods offers a rich toolkit for researchers and practitioners. Each category of methods has its strengths and limitations, making the choice of embedding technique highly dependent on the specific characteristics of the data and the requirements of the downstream task. As the field continues to evolve, new methods and hybrid approaches are likely to emerge, further expanding our ability to extract meaningful representations from time series data.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Evaluation Methodology", "weight": 1.0} -->

In this section, we detail the methodology used to evaluate the effectiveness of various time series embedding methods. Our approach involves systematically comparing the most popular of these methods across different datasets and classification tasks to assess their ability to capture and represent the essential characteristics of temporal data. The evaluation is conducted through a machine learning pipeline, encompassing data preprocessing, embedding generation, and subsequent model training and validation. The following subsections detail each component of our evaluation process, including the datasets utilized, and the machine learning pipeline implemented to assess classification performance and theoretical definition of the specific embedding methods examined.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Data", "weight": 1.0} -->

This paper explores a variety of time series with different characteristics. Table 2 presents the properties of the datasets used to evaluate the embedding methods discussed in this research. Data was sourced from various open repositories, such as the Time Series Classification Repository Aeon-Toolkit and the UC Irvine Machine Learning Repository Kelly et al..

<!-- chunk {"id": "body-0037", "role": "body", "section": "Data", "weight": 1.0} -->

*Sleep:* Originally from PhysioNet's "Sleep EDF" database, this dataset comprises 153 whole-night single-lead EEG recordings (100 Hz) from 82 healthy subjects. Recordings are segmented into non-overlapping 178-sample epochs labeled as five sleep stages (Wake, N1, N2, N3, REM). We use the split of 478,785 train+validation and 90,315 test, noting class imbalance across partitions.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Data", "weight": 1.0} -->

*ElectricDevices:* Drawn from the UCR Time Series Classification Archive, these series capture appliance power consumption sampled every two minutes over one month in 251 UK households. Each of the 8,926 training and 7,711 test series is 96 samples long and classified into seven usage profiles.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Data", "weight": 1.0} -->

*MelbournePedestrian:* From the City of Melbourne's automated pedestrian counting system, this dataset contains 24 hourly counts per day at ten locations during 2017. We treat each 24-sample day as one series, using 1,194 days for training and 2,439 for testing, with class labels corresponding to sensor sites.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Data", "weight": 1.0} -->

*RacketSports:* Recorded at 10 Hz via a wrist-worn Sony SmartWatch 3, each 30-sample series encodes accelerometer (x,y,z) then gyroscope (x,y,z) readings over a 3 s racket stroke. There are 151 train and 152 test instances labeled as one of four actions (badminton clear/smash, squash forehand/backhand).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Data", "weight": 1.0} -->

*SharePriceIncrease:* Formatted from daily NASDAQ-100 closing prices, each 60-day series records percentage change from the prior day. The binary label indicates whether the stock rose more than 5% after its next quarterly earnings release (0 = no, 1 = yes). We have 965 train and 965 test series.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Data", "weight": 1.0} -->

*SelfRegulationSCP1:* A slow cortical potentials BCI dataset recorded at 256 Hz over six EEG channels during a cursor-control task. Each 896-sample trial (3.5 s feedback window) comprises 268 train and 293 test trials, labeled by intentional cortical positivity vs. negativity.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Data", "weight": 1.0} -->

*UniMiB-SHAR:* Collected via a smartphone accelerometer at 50 Hz, this dataset contains 4,601 training and 1,524 testing tri-axial series, each 151 samples long, capturing nine daily activities and falls from 30 subjects (ages 18--60).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Data", "weight": 1.0} -->

*EMGGestures:* Recorded by a nine-channel EMG armband at 50 Hz, this dataset comprises 1,800 train and 450 test signals of length 30, classified into eight hand gestures (e.g., fist, wave-, pinch).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Data", "weight": 1.0} -->

*Mill:* From NASA's milling-machine sensor suite, each 64-sample series contains readings from six sensors (acoustic emission, vibration, current) under varying cutting conditions. There are 7 751 train and 1,910 test instances across three tool-wear classes.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Data", "weight": 1.0} -->

*ECG5000:* A pre-processed subset of PhysioNet's BIDMC CHF Database ("chf07"), where individual heartbeats were extracted from a 20 h ECG and interpolated to 140 samples. We select 500 train and 4,500 test beats, labeled into five heartbeat-type classes.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Data", "weight": 1.0} -->

These diverse datasets allow us to evaluate the performance of our embedding methods across different domains and time series characteristics.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Machine Learning Pipeline", "weight": 1.0} -->

We consider a dataset $\mathcal{D} = {\{{(X_{i},Y_{i})}\}}_{i = 1}^{N}$, where each $X_{i} \in {\mathbb{R}}^{T_{i} \times C}$ is a multi-channel, continuous time series with $T_{i}$ time steps and $C$ channels. Associated with each time series $X_{i}$ is a sequence of labels $Y_{i} \in \mathcal{L}^{T_{i}}$, with $\mathcal{L}$ representing the set of possible labels. The dataset is suitable for supervised learning tasks involving time series classification, applicable to diverse scenarios such as physiological data, air quality monitoring, and activity recognition using wearable devices. The machine learning pipeline we follow to evaluate our embedding methods is summarized in Figure 2 and described in detail in the following subsections.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Data Splitting", "weight": 1.0} -->

Before processing, the dataset $\mathcal{D}$ is divided into training ($\mathcal{D}_{\text{train}}$), validation ($\mathcal{D}_{\text{val}}$), and test ($\mathcal{D}_{\text{test}}$) subsets. This split is performed to ensure that the data from a single entity (e.g., a specific subject or period) is exclusively contained within one of these subsets, maintaining complete independence between the training, validation, and test sets.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Time Series Segmentation", "weight": 1.0} -->

After the dataset is split, each subset ($\mathcal{D}_{\text{train}}$, $\mathcal{D}_{\text{val}}$, $\mathcal{D}_{\text{test}}$) undergoes a segmentation process. Let $\tau$ be the window size and $\omega$ the overlap between consecutive windows, both defined as hyperparameters. For each time series $X_{i}$ in a subset, we segment it into windows: The corresponding labels for each segment $s_{i,j}$ are determined by an aggregation function applied to $Y_{i}$ over the window: In this work, the label aggregation function used was based on the mode of the label of the data in that segment.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Data Normalization", "weight": 1.0} -->

Each segment $s_{i,j}$ from $\mathcal{D}_{\text{train}}$, $\mathcal{D}_{\text{val}}$, and $\mathcal{D}_{\text{test}}$ is preprocessed through a normalization function $f$. The normalized segment is denoted as ${\overset{\sim}{s}}_{i,j}$. That normalization is commonly a standardization to zero mean and unit variance: where $\mu_{c}$ and $\sigma_{c}$ are the mean and standard deviation of channel (or feature) $c$ computed over the training segments.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Data Normalization", "weight": 1.0} -->

Alternatively, a min-max scaling can be applied. This is calculated through: where $\min_{c}$ and $\max_{c}$ are the minimum and maximum values of channel $c$ in the training set.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Time Series Embedding", "weight": 1.0} -->

After preprocessing, each segment ${\overset{\sim}{s}}_{i,j}$ is transformed into an embedding vector $v_{i,j}$ using a predefined embedding function $g$: Each embedding vector $v_{i,j} \in {\mathbb{R}}^{d}$ is then used as an input instance to the machine learning classification algorithm.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Model Training, Validation, and Testing", "weight": 1.0} -->

The embedded vectors $\{ v_{i,j}\}$ from each subset are used to train, validate, and test a machine learning model. The training set $\mathcal{D}_{\text{train}}$ is used for model learning, while the validation set $\mathcal{D}_{\text{val}}$ assists in hyperparameter tuning. The model's performance is subsequently evaluated using the embedded test set $\mathcal{D}_{\text{test}}$, with outcomes measured by metrics such as classification accuracy.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Model Training, Validation, and Testing", "weight": 1.0} -->

We have applied classical and neural network-based time series classification methods to explore the classification results. In particular, Logistic Regression, Decision Trees, Random Forest, K-Nearest Neighbors (KNN), XGBoost, Support Vector Machines (SVM), Naive Bayes, and Multi-Layer Perceptron (MLP) classification methods have been used to study the performance and accuracy of the embedding methods discussed in the paper.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Embedding Methods Evaluated", "weight": 1.0} -->

In this subsection, we examine in more detail the embedding methods that were selected for comprehensive evaluation. These methods were selected based on their popularity while representing as many of the different categories from our taxonomy as possible. To keep the embedding process independent of the downstream classification task, we opted for using only unsupervised techniques for creating the embeddings, i.e. no labels were used during the mapping of the raw time series data into an embedding vector. Labels were used only when training the final classifier on the previously created embedding vectors.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Principal Component Analysis (PCA)", "weight": 1.0} -->

PCA is a technique that transforms a set of correlated variables into a smaller set of uncorrelated variables called principal components. The first principal component captures the most variance in the data, the second principal component captures the second most variance, and so. The formula for PCA is: $X = {U\Sigma V^{\top}}$, where $X$ is the input data matrix, $U$ contains the left singular vectors, $\Sigma$ is a diagonal matrix of singular values, and $V^{\top}$ contains the right singular vectors.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Principal Component Analysis (PCA)", "weight": 1.0} -->

The embedding process with PCA operates as follows: The normalized segments ${\overset{\sim}{s}}_{i,j}$ are vectorized (flattened) into one-dimensional vectors: ${\overset{\sim}{\mathbf{s}}}_{i,j} = {\text{vec}{({\overset{\sim}{s}}_{i,j})}} \in {\mathbb{R}}^{\tau C}$ These vectors are organized into a data matrix $X \in {\mathbb{R}}^{{n_{s} \times \tau}C}$, where each row corresponds to a vectorized segment, and $n_{s}$ is the total number of segments in the training set.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Principal Component Analysis (PCA)", "weight": 1.0} -->

PCA is applied to $X$ to obtain the projection matrix $W \in {\mathbb{R}}^{{\tau C} \times d}$, whose columns are the top $d$ principal components.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Principal Component Analysis (PCA)", "weight": 1.0} -->

Each segment is transformed into its embedding using the PCA embedding function: $v_{i,j} = {g{({\overset{\sim}{s}}_{i,j})}} = {W^{\top}{\overset{\sim}{\mathbf{s}}}_{i,j}}$ The resulting vectors $v_{i,j} \in {\mathbb{R}}^{d}$ serve as the embedded representations of the original time series segments.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Principal Component Analysis (PCA)", "weight": 1.0} -->

Other embedding methods follow a similar process, and the embedding steps will be omitted for brevity.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Fourier Transform (FFT)", "weight": 1.0} -->

The Fourier Transform decomposes a time series into its constituent frequencies. For each normalized segment ${\overset{\sim}{s}}_{i,j}$, we apply the Discrete Fourier Transform (DFT) to obtain its frequency representation. For a univariate time series $x_{n}$, the DFT and its inverse are given: where $x_{n}$ is the input signal at time step $n$, $X_{k}$ is the DFT coefficient at frequency $k$, $N$ is the length of the signal, and $i$ is the imaginary unit.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Fourier Transform (FFT)", "weight": 1.0} -->

For multivariate time series segments ${\overset{\sim}{s}}_{i,j} \in {\mathbb{R}}^{\tau \times C}$, we apply the DFT independently to each channel $c$ to obtain the frequency components $X_{i,j}^{(c)}$. The embedding vector $v_{i,j}$ is then formed by concatenating the magnitudes (or other features) of the DFT coefficients from each channel: where $g$ is the embedding function, and $|X_{i,j}^{(c)}|$ denotes the magnitude spectrum of channel $c$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Wavelet Transform", "weight": 1.0} -->

The Wavelet Transform decomposes a time series into time-frequency representations at different scales. For each normalized segment ${\overset{\sim}{s}}_{i,j}$, we apply the Continuous Wavelet Transform (CWT) to capture both time and frequency information. The CWT of a signal $x{(t)}$ is defined as: where $\psi{(t)}$ is the mother wavelet, $a$ is the scale parameter, $b$ is the translation parameter, and $\psi^{\ast}$ denotes the complex conjugate of $\psi$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Wavelet Transform", "weight": 1.0} -->

For multivariate segments ${\overset{\sim}{s}}_{i,j}$, the CWT is applied independently to each channel $c$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Locally Linear Embedding (LLE)", "weight": 1.0} -->

Locally Linear Embedding (LLE) is a technique that preserves the local linear structure of the data. For our vectorized normalized segments ${\overset{\sim}{\mathbf{s}}}_{i,j} = {\text{vec}{({\overset{\sim}{s}}_{i,j})}} \in {\mathbb{R}}^{\tau C}$, LLE operates by reconstructing each segment from its nearest neighbors.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Locally Linear Embedding (LLE)", "weight": 1.0} -->

The steps are as follows: Find the set of $K$ nearest neighbors $\mathcal{N}_{i,j}$ for each segment ${\overset{\sim}{\mathbf{s}}}_{i,j}$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Locally Linear Embedding (LLE)", "weight": 1.0} -->

Compute weights $W_{i,j,k}$ that minimize the reconstruction error: Compute the embeddings $v_{i,j} \in {\mathbb{R}}^{d}$ by minimizing: This process results in embeddings that preserve local neighborhood structures of the original data.

<!-- chunk {"id": "body-0069", "role": "body", "section": "UMAP", "weight": 1.0} -->

Uniform Manifold Approximation and Projection (UMAP) is a dimensionality reduction technique that maps high-dimensional data into a lower-dimensional space while preserving both local and global structures. For the vectorized segments ${\overset{\sim}{\mathbf{s}}}_{i,j}$, UMAP operates as follows: Compute the fuzzy simplicial set representation of the high-dimensional data based on a distance metric $d{({\overset{\sim}{\mathbf{s}}}_{i,j},{\overset{\sim}{\mathbf{s}}}_{k})}$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "UMAP", "weight": 1.0} -->

Optimize the low-dimensional embeddings $v_{i,j} \in {\mathbb{R}}^{d}$ by minimizing the cross-entropy between the fuzzy simplicial sets of the high-dimensional and low-dimensional representations.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Graph Embedding", "weight": 1.0} -->

Graph Embedding learns low-dimensional representations of graphs by capturing their structural properties. For time series data, we construct a Visibility Graph (VG) from each segment ${\overset{\sim}{s}}_{i,j}$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Graph Embedding", "weight": 1.0} -->

In a Natural Visibility Graph (NVG), an edge between nodes $n_{i}$ and $n_{j}$ exists if: The weight of the edge is: $w_{ij} = \left| \frac{{x{(t_{j})}} - {x{(t_{i})}}}{t_{j} - t_{i}} \right|$ From the constructed graph $G_{i,j} = {(N_{i,j},E_{i,j})}$, we extract features such as degree distributions, clustering coefficients, or apply graph embedding techniques like node2vec to obtain the embedding $v_{i,j}$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Persistent Homology", "weight": 1.0} -->

Persistent Homology captures topological features by analyzing the birth and death of homological features across different scales. For each segment ${\overset{\sim}{s}}_{i,j}$, we combine properties from Visibility Graphs and persistence diagrams.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Persistent Homology", "weight": 1.0} -->

The Horizontal Visibility Graph (HVG) condition is: We compute persistence diagrams $D_{i,j}$ from sublevel filtrations of ${\overset{\sim}{s}}_{i,j}$. Features extracted include: Bottleneck distance to a reference diagram; $p$-Wasserstein distances; Betti curves: ${B_{i,j}{(x)}} = {\sum_{{(b_{k},d_{k})} \in D_{i,j}}{\delta_{\lbrack b_{k},d_{k}\rbrack}{(x)}}}$; Persistence entropy; Norms of the persistence landscape.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Persistent Homology", "weight": 1.0} -->

These features are combined with those from the visibility graphs to form the embedding $v_{i,j}$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Contrastive Learning CNN Embedding (CL-CNN)", "weight": 1.0} -->

Each normalized segment ${\overset{\sim}{s}}_{i,j}$ is transformed into an embedding vector $v_{i,j}$ using a one-dimensional Convolutional Neural Network (1D-CNN). The CNN applies convolutional filters across the time dimension to extract temporal features.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Contrastive Learning CNN Embedding (CL-CNN)", "weight": 1.0} -->

The embedding process is defined as: where CNN includes convolutional layers, activation functions, and pooling layers designed to capture hierarchical patterns in the data.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Contrastive Learning RNN Embedding (CL-RNN)", "weight": 1.0} -->

Each normalized segment ${\overset{\sim}{s}}_{i,j}$ is processed using a Recurrent Neural Network (RNN) to capture temporal dependencies. The RNN updates its hidden state $h_{i,j,k}$ at each time step $k$: with $h_{i,j,0}$ initialized appropriately. The final hidden state after processing the entire segment serves as the embedding: $v_{i,j} = h_{i,j,\tau}$. This embedding captures sequential information from the entire window ${\overset{\sim}{s}}_{i,j}$. In this work, an LSTM-based backbone was used as a recurrent neural network.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Contrastive Learning RNN Embedding (CL-RNN)", "weight": 1.0} -->

Note: To obtain *unsupervised embeddings* using CNN and RNN-based models, we implement the *nearest neighbor contrastive learning (NNCLR)* approach introduced by Dwibedi et al., adapted for time series data. Therefore, we use the abbreviations *CL-CNN* and *CL-RNN* to refer to these embedding methods.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Classification Algorithms", "weight": 1.0} -->

To evaluate the effectiveness of the various embedding methods in capturing useful representations, we employ a range of widely used classification algorithms, as implemented in the Scikit-Learn library, introduced by Pedregosa et al.. These algorithms were chosen to represent different approaches to classification, allowing us to assess how well the embeddings perform across various learning paradigms. The classification algorithms used in this study are: Logistic Regression (LR): A linear model that estimates the probability of an instance belonging to a particular class.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Classification Algorithms", "weight": 1.0} -->

Decision Trees (DT): A non-parametric method that creates a model that predicts the target variable by learning simple decision rules inferred from the data features.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Classification Algorithms", "weight": 1.0} -->

Random Forest (RF): An ensemble learning method that operates by constructing multiple decision trees during training and outputting the class that is the mode of the classes of the individual trees.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Classification Algorithms", "weight": 1.0} -->

K-Nearest Neighbors (KNN): A non-parametric method that classifies a data point based on how its neighbors are classified.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Classification Algorithms", "weight": 1.0} -->

XGBoost (XGB): An optimized distributed gradient boosting library designed to be highly efficient, flexible, and portable.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Classification Algorithms", "weight": 1.0} -->

Support Vector Machines (SVM): A method that finds a hyperplane in an N-dimensional space that distinctly classifies the data points.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Classification Algorithms", "weight": 1.0} -->

Naive Bayes (NB): A probabilistic classifier based on applying Bayes' theorem with strong (naive) independence assumptions between the features.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Classification Algorithms", "weight": 1.0} -->

Multi-Layer Perceptron (MLP): A class of feedforward artificial neural networks that consist of at least three layers of nodes: an input layer, a hidden layer, and an output layer. An MLP, also known as a fully connected or dense neural network, usually forms the last few layers of a classification neural network (a.k.a., classification head), whereas previous layers act as complex feature extractors or feature learners. Using an MLP to classify an embedding essentially simulates this behavior.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Classification Algorithms", "weight": 1.0} -->

Each of these classification algorithms was applied to the embedded representations of the time series data produced by the various embedding methods. We used standard implementations of these algorithms in their respective libraries. To ensure that the best results per dataset and embedding method are considered for comparison, we used the Optuna library in Python, introduced by Akiba et al., to tune the most important parameters of the classification methods.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Classification Algorithms", "weight": 1.0} -->

As shown, the results indicate the average and standard deviation as a result of running the experiments for each time series embedding method and relative dataset.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Results", "weight": 1.0} -->

Our experimental evaluation encompasses ten distinct time series embedding methods tested across eleven diverse datasets using various classification algorithms. The classification accuracies are presented in Table 3, with averaged performance across all classifiers for each embedding method and dataset combination. The table also shows the average rank of each method. The rank was computed by our experimental evaluation, which encompasses ten distinct time series embedding methods tested across eleven diverse datasets using various classification algorithms. The classification accuracies are presented in Table 3, with averaged performance across all classifiers for each embedding method and dataset combination. The table also shows the average rank of each method. The rank was computed by first ranking the embedding methods within each dataset based on their classification accuracy, where rank 1 corresponds to the highest accuracy and rank 10 to the lowest. For each dataset, ties in accuracy received the same rank, and the subsequent rank was adjusted accordingly (e.g., if two methods tied for rank 1, the next best method would receive rank 3). The average rank for each embedding method was then calculated by taking the arithmetic mean of its ranks across all eleven datasets.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Results", "weight": 1.0} -->

This ranking approach provides a robust measure of overall performance that accounts for the relative effectiveness of each embedding method across diverse signal types and application domains, with lower average ranks indicating better overall performance.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Overall Performance", "weight": 1.0} -->

The experimental results demonstrate that embedding method performance varies significantly across different datasets and classification algorithms. PCA consistently delivers strong performance (average rank 2.6), while Wavelet Transform (average rank 2.2) and FFT (average rank 1.9) show the best overall performance across all datasets. Advanced methods like TDA and Graph Embedding show competitive performance on specific datasets but exhibit higher variability. Among the deep learning approaches, C-CNN (average rank 5.5) outperforms C-RNN (average rank 9.5) across most datasets, suggesting that convolutional architectures may be more effective at capturing relevant temporal patterns for classification tasks when applied directly to raw data. The overall low ranking of deep-learning-based methods can be justified by the fact that self-supervised learning methods, such as the NNCLR Dwibedi et al. method used in this study, require large amounts of data and extensive hyperparameter tuning to be trained effectively.

<!-- chunk {"id": "body-0093", "role": "body", "section": "UMAP projection", "weight": 1.0} -->

For an initial visual qualitative overview of the embeddings produced by each method, we have plotted their UMAP projections on the UniMiB SHAR dataset in Figure 3. The data points are color-coded by their class label. Better visual separation of the data points from different classes likely means that the downstream classifier will have an easier time correctly classifying the data. However, it should be noted that the separability also depends on the ability of the UMAP projection to preserve the embedding properties when projecting from d-dimensions to two dimensions.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Dataset Complexity Analysis", "weight": 1.0} -->

The effectiveness of embedding methods shows a strong correlation with dataset characteristics, particularly dimensionality and sequence length. For datasets with high dimensionality (more than 5 channels) such as EMGGestures and RacketSports, Wavelet Transform consistently outperforms other methods, achieving accuracies of 66.8% and 72.8% respectively. This suggests that Wavelet's multi-resolution capabilities are particularly beneficial for capturing complex relationships across multiple channels. Conversely, for univariate time series such as ECG5000 and ElectricDevices, FFT and PCA demonstrate superior performance, with accuracies reaching 92.7% and 57.2% respectively.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Bioelectrical Signals", "weight": 1.0} -->

In EEG datasets (Sleep, SelfRegulationSCP1), Wavelet Transform demonstrates optimal performance, achieving accuracies of 71.5% and 78.2% respectively. LLE also performs strongly on SelfRegulationSCP1 (70.5%), while PCA (68.5%) and FFT (69.8%) show competitive performance on Sleep data. For ECG data (ECG5000), FFT achieves the highest accuracy (92.7%), closely followed by Wavelet Transform (92.5%) and PCA (92.3%). These results suggest that frequency-domain representations are particularly effective for capturing the quasi-periodic components characteristic of bioelectrical signals.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Biomechanical and Motion Signals", "weight": 1.0} -->

For biomechanical signals (UniMiB-SHAR, RacketSports, EMGGestures), Wavelet Transform achieves the highest accuracies (77.7% for UniMiB-SHAR, 72.8% for RacketSports, 66.8% for EMGGestures respectively). The multi-resolution capability of wavelets appears particularly beneficial for analyzing the hierarchical temporal patterns in human movement data. UMAP also performs strongly on these datasets, indicating that manifold learning approaches can effectively capture the underlying nonlinear dynamics of biomechanical systems. Graph Embedding (62.2% for EMGGestures) demonstrates moderate effectiveness in representing the structural relationships in muscle activation patterns, while deep learning approaches struggle to match the performance of classical methods in this domain.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Electrical and Mechanical System Signals", "weight": 1.0} -->

For electrical system datasets (ElectricDevices) and mechanical system datasets (Mill), FFT and PCA demonstrate superior performance, with FFT achieving the highest accuracy on Mill data (90.9%). This confirms the efficacy of frequency-domain analysis for systems with characteristic spectral signatures and harmonic components. PCA's strong performance (89.9% for Mill) suggests that linear subspace projection methods can effectively capture the dominant modes of variation in mechanical system signals. Graph Embedding also shows competitive performance on electrical system data (54.8% for ElectricDevices), indicating that structural approaches can effectively represent the temporal state transitions in these systems. The relative underperformance of topological methods (76.6% for Mill) suggests limitations in capturing the specific periodicity and harmonic structures of mechanical systems through persistence features alone.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Economic and Environmental Signals", "weight": 1.0} -->

For economic signals (SharePriceIncrease) and environmental signals (MelbournePedestrian), PCA achieves the highest accuracy for financial data (69.5%), while FFT performs best for pedestrian traffic (68.5%). The effectiveness of linear methods for economic time series suggests that dimensional reduction techniques can effectively isolate the latent factors driving financial markets. Graph Embedding shows comparable performance on financial data (67.9%), potentially capturing the complex state transitions and regime shifts characteristic of economic systems. For traffic flow signals, which exhibit both periodic and stochastic components, the frequency-domain representation offered by FFT appears particularly effective at isolating seasonal and daily patterns. The overall modest performance across methods for these domains highlights the inherent challenge in modeling systems with both deterministic and stochastic components.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Computational Efficiency Analysis", "weight": 1.0} -->

While the representational power of embedding methods is a primary consideration, computational efficiency is also a critical factor for practical signal processing applications. Our analysis reveals significant variations in computational requirements across methods. Classical methods like PCA and FFT are highly efficient, requiring minimal computational resources even for long sequences. In contrast, manifold learning methods (LLE, UMAP) and deep learning approaches incur substantially higher computational costs, with self-supervised deep learning methods requiring up to 1,600$\times$ longer training times than PCA for the electricDevices dataset. Table 4 demonstrates the computational trade-offs across embedding methods on the ElectricDevices dataset, revealing that while deep learning models achieve excellent inference speeds (0.14-0.15s), they require substantial training investments of approximately 11-12 minutes each. Graph Embedding and TDA methods show moderate to high computational requirements but process all data identically without traditional training/inference distinctions.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Classification Algorithm Impact", "weight": 1.0} -->

The effectiveness of embedding methods as shown in table 5 varies significantly depending on the downstream classification algorithm, highlighting the importance of considering the entire signal processing pipeline. Tree-based methods (Random Forest and XGBoost) consistently outperform other classifiers across most embedding methods, with Random Forest achieving particularly strong results on frequency-domain embeddings (FFT) with an average rank of 1.9. SVM also demonstrates competitive performance, particularly with manifold learning embeddings like LLE and UMAP. These results highlight the importance of considering the entire pipeline when selecting embedding methods for time series classification tasks.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Impact of Signal Characteristics", "weight": 1.0} -->

Our comprehensive analysis reveals that the effectiveness of embedding methods is fundamentally influenced by time series characteristics, particularly their dimensionality, sequence length, and application domain. For high-dimensional multivariate signals (or time series), Wavelet Transform consistently excels, likely due to its ability to capture both time and frequency information across multiple channels simultaneously. The multi-resolution nature of wavelets enables the representation of temporal patterns at different scales, which is particularly valuable for complex physiological signals and human activity data.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Impact of Signal Characteristics", "weight": 1.0} -->

Conversely, for univariate or low-dimensional signals, simpler methods like PCA and FFT often achieve comparable or superior performance to more complex approaches. This suggests that for datasets with simpler structures, the additional complexity of advanced embedding methods may not translate to proportionate performance gains. The strong performance of FFT across multiple domains indicates that frequency-domain representations remain highly effective for a wide range of time series classification tasks, particularly those involving periodic or quasi-periodic signals.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Impact of Signal Characteristics", "weight": 1.0} -->

The relationship between time series length and embedding method effectiveness also reveals important patterns. For longer time series (or signals), methods that can effectively compress information, such as PCA and Wavelet Transform, demonstrate advantages over methods that struggle with the curse of dimensionality. This pattern becomes particularly evident in datasets like SelfRegulationSCP1, where dimensionality reduction becomes essential for effective classification.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Methodological Considerations", "weight": 1.0} -->

The comparative analysis across embedding categories reveals distinct advantages and limitations that have important implications for method selection. Classical methods (PCA, FFT, Wavelet Transform) offer robust performance, computational efficiency, and interpretability, making them valuable baseline approaches for many applications. Their consistent performance across diverse datasets suggests that they should be considered as strong candidates before implementing more complex methods.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Methodological Considerations", "weight": 1.0} -->

Machine learning-based methods (LLE, UMAP) excel at capturing non-linear relationships and complex manifold structures, but their performance varies significantly across datasets. These methods show particular promise for datasets with complex underlying geometries, such as human activity recognition, but may struggle with noisy or irregularly sampled time series. Their higher computational requirements also present challenges for large-scale applications.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Methodological Considerations", "weight": 1.0} -->

Structural and topological methods (Graph Embedding, TDA) show mixed results, with performance varying substantially across signal types. Graph-based approaches demonstrate particular strengths for signals with distinct state transitions or regime shifts, suggesting potential applications in anomaly detection and change point analysis. However, their overall performance lags behind classical methods for standard classification tasks, indicating that structural features alone may not provide sufficient discriminative power for many signal types.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Methodological Considerations", "weight": 1.0} -->

Deep learning-based methods show surprisingly modest performance, with even the best-performing approach (C-CNN) generally not matching classical techniques. This finding suggests that self-supervised representation learning, while theoretically promising, may face practical challenges in extracting discriminative features from time series without extensive architecture optimization and large training datasets. The substantial gap between C-CNN and C-RNN performance indicates that architectural choices significantly impact representation quality, with convolutional approaches better suited to capturing the relevant temporal patterns for many signal types when applied directly to raw time series. In practice, hybrid architectures, which include convolutional layers closer to the input and recurrent or Transformer layers deeper in the network, may be the best approach.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Classification Algorithm Synergies", "weight": 1.0} -->

The interaction between embedding methods and classification algorithms reveals important synergistic effects that significantly impact overall system performance. The consistently strong performance of tree-based methods across multiple embedding types suggests that these classifiers possess intrinsic advantages for time series classification, likely stemming from their ability to identify discriminative features from diverse representations and their robustness to irrelevant or noisy dimensions.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Classification Algorithm Synergies", "weight": 1.0} -->

The particular synergy between manifold embeddings and SVM classification highlights the value of geometric preservation in the embedded space. By maintaining the topological structure of the original signal manifold, methods like LLE and UMAP provide representations that align well with SVM's margin-based optimization, resulting in superior classification boundaries. This geometric perspective offers valuable insights for signal classification system design, suggesting that preserving the intrinsic structure of the signal manifold may be more important than maximizing variance or minimizing reconstruction error.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Classification Algorithm Synergies", "weight": 1.0} -->

These synergistic relationships highlight the importance of considering the entire signal processing pipeline when developing classification systems. Rather than evaluating embedding methods in isolation, optimal performance requires joint optimization of both representation and classification components, with particular attention to their mutual compatibility. This system-level perspective aligns with modern signal processing frameworks that emphasize end-to-end optimization rather than individual component excellence.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Practical Guidelines for Signal Processing Applications", "weight": 1.0} -->

Based on our comprehensive evaluation, we propose the following practical guidelines for selecting time series embedding methods in signal processing applications: Prioritize classical methods for most applications: For the majority of time series classification tasks, classical methods like Wavelet Transform, FFT, and PCA should be evaluated first due to their robust performance, computational efficiency, and interpretability. These methods provide strong baselines that more complex approaches must justify surpassing.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Practical Guidelines for Signal Processing Applications", "weight": 1.0} -->

Select methods based on signal characteristics: For signals with strong harmonic components or clear spectral signatures (e.g., ECG, mechanical vibrations), FFT typically provides optimal results. For non-stationary signals with transient features (e.g., EEG, speech), Wavelet Transform offers superior performance. For signals with complex nonlinear dynamics (e.g., human motion, fluid dynamics), consider manifold learning approaches despite their higher computational costs.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Practical Guidelines for Signal Processing Applications", "weight": 1.0} -->

Match techniques to application domains: For bioelectrical signal processing, wavelet-based representations consistently excel. For mechanical and electrical system analysis, frequency-domain representations (FFT) and principal component analysis (PCA) provide the most effective embeddings. For biomechanical signal analysis, consider combined approaches that capture both spectral and geometric properties.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Practical Guidelines for Signal Processing Applications", "weight": 1.0} -->

Optimize the full processing pipeline: Consider both embedding method and classification algorithm when designing signal processing systems. Tree-based methods (Random Forest, XGBoost) offer robust performance across most embedding approaches. For manifold embeddings, SVM typically provides superior classification. For wavelet embeddings, neural network classifiers show particular promise.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Practical Guidelines for Signal Processing Applications", "weight": 1.0} -->

These guidelines aim to assist signal processing practitioners in navigating the complex landscape of time series embedding methods, enabling more informed decisions based on specific signal characteristics and application requirements.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This comprehensive study evaluates various time series embedding methods across different datasets and classification tasks, revealing important insights into their relative strengths and limitations. Our analysis demonstrates that while embedding method performance varies significantly based on dataset characteristics and downstream tasks, classical methods like PCA and Fourier transforms consistently offer robustness and interpretability for datasets with prominent global patterns. In contrast, complex methods such as deep learning-based embeddings excel at capturing non-linear patterns in datasets with intricate structures, though at higher computational costs.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The selection between classical and complex embedding methods inherently involves trade-offs between simplicity, interpretability, computational efficiency, and pattern-capturing ability. Our findings emphasize the importance of adopting a tailored approach that carefully considers the specific characteristics of the data and intended analysis goals. The varying effectiveness of topological and graph-based methods across different applications suggests promising avenues for future development, particularly in handling complex, multi-dimensional time series data.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Through the provision of an open-source suite implementing these embedding methods, we aim to facilitate further advancements in time series analysis across various fields. Future research directions include developing hybrid and adaptive embedding methods, improving interpretability of complex techniques, and extending the evaluation to other domains, ultimately contributing to the broader understanding and application of these tools.
