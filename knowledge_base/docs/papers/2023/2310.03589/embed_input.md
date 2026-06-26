<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

TimeGPT-1

Topics include Uncertainty, Deep learning, Foundation models, Time series, Datasets, Learning, Machine learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we introduce TimeGPT, the first foundation model for time series, capable of generating accurate predictions for diverse datasets not seen during training. We evaluate our pre-trained model against established statistical, machine learning, and deep learning methods, demonstrating that TimeGPT zero-shot inference excels in performance, efficiency, and simplicity. Our study provides compelling evidence that insights from other domains of artificial intelligence can be effectively applied to time series analysis. We conclude that large-scale time series models offer an exciting opportunity to democratize access to precise predictions and reduce uncertainty by leveraging the capabilities of contemporary advancements in deep learning.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Uncertainty is an intrinsic aspect of life, a constant element that humans have tirelessly sought to navigate and comprehend. From the traditions established by ancient civilizations to the sophisticated research endeavors in our contemporary world, brilliant minds have ceaselessly strived to anticipate the distribution of possible future events, crafting systematic approaches to unveil the prospective future.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The aspiration to predict potential outcomes, foundational across a multitude of disciplines, reflects a deep-seated human tendency to anticipate, strategize, and mitigate risks. The goal to reduce uncertainty about what will come next maps to numerous real-world applications: from understanding economic cycles and trends to discerning consumer consumption patterns; from optimizing electricity demand for energy production and grid management to aligning capacity and infrastructure for servers, workers, and machines.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Time series---data ordered chronologically---constitutes the underlying fabric of systems, enterprises, and institutions. Its impact spans from measuring ocean tides to tracking the daily closing value of the Dow Jones. This type of data representation is indispensable in sectors such as finance, healthcare, meteorology, social sciences, and others, where discerning temporal patterns, trends, and cyclical variations is crucial for forecasting future values and informing decision-making processes.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, the current theoretical and practical understanding of time series hasn't yet achieved a level of consensus among practitioners that mirrors the widespread acclaim for generative models in other fundamental domains of the human condition, like language and perception. Our field is still divided in their assessment of the efficacy of deep learning for forecasting tasks. Efforts in forecasting science have fallen short of fulfilling the promises of genuinely universal pre-trained models.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we embark on a novel path and introduce TimeGPT, the first pre-trained foundation model for time series forecasting that can produce accurate predictions across a diverse array of domains and applications without additional training. A general pre-trained model constitutes a groundbreaking innovation that opens the path to a new paradigm for the forecasting practice that is more accessible and accurate, less time-consuming, and drastically reduces computational complexity.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Literature Review", "weight": 1.0} -->

(a) Single series forecasting (b) Multiple series forecasting Figure 1: Illustration of single series forecasting and multiple series forecasting Deep Learning forecasting models have become a prominent area of research, driven by their success in recent famous competitions, including, and their applicability to large-scale tasks in the industry. presents a comprehensive review and taxonomy of neural forecasting models and their applications.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Literature Review", "weight": 1.0} -->

Initial Deep Learning time series forecasting successes stemmed from the adaptation of established architectures, namely Recurrent Neural Networks (RNN) and Convolution Neural Networks (CNN), initially designed for natural language processing (NLP) and computer vision (CV), respectively. RNNs served as the backbone for popular models like DeepAR for probabilistic forecasting and the ESRNN, winner of the M4 Competition. CNNs demonstrated superior performance than RNNs in multiple tasks on sequential data, as shown. They now constitute a popular building block, as models like DPMN and TimesNet use. Feed-forward networks, due to their low computational costs and efficiency, are also frequently used, with notable examples including the N-BEATS and NHITS.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Literature Review", "weight": 1.0} -->

Transformer-based models are gaining popularity in recent years, as they are demonstrating remarkable performance in large-scale settings and complex tasks, such as long sequence forecasting. The earlier examples include the TFT and MQTransformer, both with multi-quantile capabilities. The Informer introduced Transformers for long sequence forecasting through the Prob-sparse self-attention mechanism. This concept has since been further refined through various forms of inductive bias and attention mechanisms in models like the Autoformer, FEDformer, and PatchTST.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Literature Review", "weight": 1.0} -->

The potential of foundation models, namely large-scale models pre-trained on a large dataset and later fine-tuned for specific tasks, remains relatively under-explored for time series forecasting tasks. There are, however, early indicators of the possibility of forecasting foundational models. For instance, showed that pre-trained models can be transferred between tasks without performance degradation. Additionally, provided evidence on the existence of scaling laws on data and model sizes for Transformer architectures on time series forecasting tasks.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Foundation model for time series", "weight": 1.0} -->

Foundation models rely on their capabilities to generalize across domains, particularly in new datasets that were not available during training. We understand, accordingly, transfer learning as the capacity to apply knowledge gleaned from one task to solve new tasks. Next, we explain the concept of transfer learning, building upon previous studies in time series forecasting.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Foundation model for time series", "weight": 1.0} -->

The forecasting task objective is to estimate the following conditional distribution: Transfer-learning refers to pre-training a model on a (usually large) source dataset $D_{s} = \left. \{{(\mathbf{X},\mathbf{y})} \middle| {{\mathbf{X} \in \mathcal{X}},{\mathbf{y} \in \mathcal{Y}}}\} \right.$, to improve its performance on a new forecasting task with target dataset $D_{t}$. This paper considers two cases of transfer learning: zero-shot learning and fine-tuning. In the first case, the pre-trained model is directly transferred to solve the new forecasting task without re-training its parameters $\theta$ on the new dataset. Conversely, in fine-tuning, the model is further trained on the new dataset (starting from pre-trained parameters).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Foundation model for time series", "weight": 1.0} -->

The core idea of the presented foundation model is to leverage these principles by training it on the largest publicly available time series dataset to date, leveraging scaling laws on the dataset and model sizes. A diverse dataset, in terms of breadth and depth, allows TimeGPT to glean insights from an unprecedented array of temporal patterns across multiple domains.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Architecture", "weight": 1.0} -->

TimeGPT is a Transformer-based time series model with self-attention mechanisms based. TimeGPT takes a window of historical values to produce the forecast, adding local positional encoding to enrich the input. The architecture consists of an encoder-decoder structure with multiple layers, each with residual connections and layer normalization. Finally, a linear layer maps the decoder's output to the forecasting window dimension. The general intuition is that attention-based mechanisms are able to capture the diversity of past events and correctly extrapolate potential future distributions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Architecture", "weight": 1.0} -->

The development of a generalized global model for time series entails numerous challenges, primarily due to the complex task of handling signals derived from a broad set of underlying processes. Characteristics such as frequency, sparsity, trend, seasonality, stationarity, and heteroscedasticity present distinct complications for both local and global models. Therefore, any foundational forecasting model must possess the ability to manage such heterogeneity. Our model, TimeGPT, is engineered to process time series of varied frequencies and characteristics while accommodating different input sizes and forecasting horizons. This adaptability is largely attributable to the underlying transformer-based architecture upon which TimeGPT is built.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Architecture", "weight": 1.0} -->

It should be noted that TimeGPT is not based on an existing large language model (LLM). While TimeGPT follows the same principle of training a large transformer model on a vast dataset, its architecture is specialized in handling time series data and trained to minimize the forecasting error.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Training dataset", "weight": 1.0} -->

TimeGPT was trained, to our knowledge, the largest collection of publicly available time series, collectively encompassing over 100 billion data points. This training set incorporates time series from a broad array of domains, including finance, economics, demographics, healthcare, weather, IoT sensor data, energy, web traffic, sales, transport, and banking. Due to this diverse set of domains, the training dataset contains time series with a wide range of characteristics.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Training dataset", "weight": 1.0} -->

In terms of temporal patterns, the training dataset contains series with multiple number of seasonalities, cycles of different lengths, and various types of trends. In addition to the temporal patterns, the dataset also varies in terms of noise and outliers, offering a robust training environment. Some series contain clean, regular patterns, while others feature significant noise or unexpected events, providing a broad spectrum of scenarios for the model to learn. Most of the time series were included in their raw form; the processing was limited to format standardization and filling in missing values to ensure data completeness.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Training dataset", "weight": 1.0} -->

The selection of such a diverse training set is critical for developing a robust foundational model. This diversity encompasses the complex realities of non-stationary real-world data, where trends and patterns can shift over time due to a multitude of factors. Training TimeGPT on this rich dataset equips it to handle a wide range of scenarios, enhancing its robustness and generalization capabilities. This effectively enables TimeGPT to forecast unseen time series accurately while eliminating the need for individual model training and optimization.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Training TimeGPT", "weight": 1.0} -->

TimeGPT underwent a multi-day training period on a cluster of NVIDIA A10G GPUs. During this process, we carried out extensive hyperparameter exploration to optimize learning rates, batch sizes, and other related parameters. We observed a pattern in alignment with findings, where a larger batch size and a smaller learning rate proved beneficial. Implemented in PyTorch, TimeGPT was trained using the Adam with a learning rate decay strategy that reduced the rate to 12% of its initial value.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Uncertainty quantification", "weight": 1.0} -->

Probabilistic forecasting refers to estimating a model's uncertainty around the predictions. Correctly assessing a forecasting model's calibration enables risk assessment and informed decision-making. Conformal prediction, a non-parametric framework, offers a compelling approach to generating prediction intervals with a pre-specified level of coverage accuracy. Unlike traditional methods, conformal prediction does not require strict distributional assumptions, making it more flexible and agnostic to the model or time series domain. During the inference of a new time series, we perform rolling forecasts on the latest available data to estimate the model's errors in forecasting the particular target time series.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Classically, forecasting performance evaluation is based on splitting each time series of the dataset into train and test sets based on a defined cutoff. Such a principle, even in its cross-validation version, is not strict enough to asses a foundation model because its main property is the capability to accurately predict completely novel series.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In this section, we explore TimeGPT's capabilities as a forecasting foundation model by testing it in a large and diverse set of time series that were never seen by the model during training. The test set includes over 300 thousand time series from multiple domains, including finance, web traffic, IoT, weather, demand, and electricity.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

The evaluation is performed in the last forecasting window of each time series, varying in length by the sampling frequency. TimeGPT uses the previous historical values as inputs, as shown in Figure 3, without re-training its weights (zero-shot). We specify a different forecasting horizon based on the frequency to represent common practical applications: 12 for monthly, 1 for weekly, 7 for daily, and 24 for hourly data. ^33^3Future work would profit from expanding and varying this testing set.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

TimeGPT was benchmarked against a broad spectrum of baseline, statistical, machine learning, and neural forecasting models to provide a comprehensive performance analysis. Baselines and statistical models are individually trained on each time series of the test set, utilizing the historical values preceding the last forecasting window. We opted for a global model approach for machine learning and deep learning methods for each frequency, leveraging all time series in the test set. Some popular models like Prophet and ARIMA were excluded from the analysis due to their prohibitive computational requirements and extensive training times.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Our selected evaluation metrics include the relative Mean Absolute Error (rMAE) and the relative Root Mean Square Error (rRMSE), both normalized against the performance of the Seasonal Naive model. This choice is justified by the additional insights offered by these relative errors, as they show performance gains in relation to a known baseline, improving the interpretability of our results. The relative error metrics bring the additional benefit of scale independence, enabling comparisons across the results for each frequency. To ensure both robust numerical stability and consistency in evaluation, we apply this normalization at a global scale for each comprehensive dataset. The specific computations for these metrics, applicable to a dataset with $n$ time series and a forecast horizon of $h$, are described in Equation 2.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Zero-shot inference", "weight": 1.0} -->

We first test TimeGPT capabilities on zero-shot inference, meaning that no additional fine-tuning is performed on the test set. Table 1 presents the zero-shot results. Remarkably, TimeGPT outperforms a comprehensive collection of battle-tested statistical models and SoTA deep learning approaches, ranking among the top-3 performers across frequencies.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Zero-shot inference", "weight": 1.0} -->

It must be noted that the validity of a forecasting model can only be assessed relative to its performance against competing alternatives. Although accuracy is commonly seen as the only relevant metric, computational cost and implementation complexity are key factors for practical applications. In this regard, it is noteworthy that the reported results of TimeGPT are the result of a simple and extremely fast invocation of the prediction method of a pre-trained model. In comparison, other models require a complete pipeline for training and then predicting.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Fine Tuning", "weight": 1.0} -->

Fine-tuning is a critical step in effectively utilizing foundation models and transformer-based architectures. Foundation models are pre-trained on vast amounts of data, capturing wide-ranging and generic features. However, these models often need to be specialized for specific contexts or domains. By fine-tuning, we adjust the model parameters on a task-specific dataset, allowing the model to tailor its vast pre-existing knowledge toward the requirements of the new task. This process ensures that the model retains its broad understanding and excels at the specific tasks at hand. Due to their inherent flexibility and capacity for learning complex patterns, transformer-based architectures particularly benefit from fine-tuning, enhancing their performance in domain-specific applications. Fine-tuning thus serves as a crucial bridge, linking foundation models' broad capabilities to the target tasks' specificities. Figure 5 presents results on the accuracy improvements of TimeGPT against the number of fine-tuning steps for a subset of time series on the test set.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Time Comparison", "weight": 1.0} -->

For zero-shot inference, our internal tests recorded an average GPU inference speed of 0.6 milliseconds per series for TimeGPT, which nearly mirrors that of the simple Seasonal Naive. As points of comparison, we consider parallel computing-optimized statistical methods, which, when complemented with Numba compiling, averaged a speed of 600 milliseconds per series for training and inference. On the other hand, global models such as LGBM, LSTM, and NHITS demonstrated a more prolonged average of 57 milliseconds per series, considering both training and inference. Due to its zero-shot capabilities, TimeGPT outperforms traditional statistical methods and global models with total speed by orders of magnitude.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Discussion and Future Research", "weight": 1.5} -->

Current forecasting practice usually involves a complex pipeline, encompassing multiple steps from data processing to model training and selection. TimeGPT greatly simplifies this process by reducing pipelines to the inference step, substantially reducing complexity and time investment while still achieving state-of-the-art performance. Perhaps most significantly, TimeGPT democratizes the advantages of large transformers models, nowadays restricted to organizations with vast amounts of data, computational resources, and technical expertise. We believe that foundational models are set to profoundly impact the forecasting field and can redefine current practices.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Discussion and Future Research", "weight": 1.5} -->

The introduction of a foundation model in time series that resembles other fields and opens the possible path for future improvements could be considered an important milestone in the time series field. However, this work must be understood as part of a larger academic tradition with a plethora of open questions. While we believe that TimeGPT displays amazing results presenting for the first time a general global modal capable of accurately predicting unseen series, there are still many important limitations and open questions. We hope this assessment is of help to current and future researchers.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Discussion and Future Research", "weight": 1.5} -->

Our results align with previous intuitions regarding the expected performance of large time series models. This is consistent with findings from Zalando, OpenAI, Alibaba, and Amazon. These outcomes validate the scaling laws correlating model size, dataset size, and Transformer performance. These laws elucidate why simpler models might outperform Transformers on smaller datasets, as observed in studies such as. The relevance of Transformers is, therefore, context-dependent, and they often become more beneficial as dataset sizes increase. These laws offer important practical insights, guiding model selection for specific tasks. In situations where there are limitations on the availability of large datasets or computational resources, simpler models might be more fitting.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Discussion and Future Research", "weight": 1.5} -->

Looking forward, we identify two primary areas for future exploration: Informed forecasting: that incorporates knowledge about the underlying processes, such as physical laws, economic principles, or medical facts.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Discussion and Future Research", "weight": 1.5} -->

Time Series Embedding: While traditionally practitioners have hypothesized that series from the same categories like retail or finance would have greater similarity than those across domains, a robust metric to measure similarity between series could significantly benefit the field. This work suggests that certain assumptions around the taxonomy of time series warrant further examination.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Discussion and Future Research", "weight": 1.5} -->

Furthermore, adjacent questions about foundation models for time series classification and the integration of truly multimodal (text, video) and multi-temporal foundation models promise to be engaging areas for future study. These areas will not only extend our understanding of time series data but also improve our ability to develop more powerful and generalized models for forecasting.
