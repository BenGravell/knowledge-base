<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting

Topics include Transformers, Attention mechanisms, Datasets, Planning, Informer, LSTF.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Many real-world applications require the prediction of long sequence time-series, such as electricity consumption planning. Long sequence time-series forecasting (LSTF) demands a high prediction capacity of the model, which is the ability to capture precise long-range dependency coupling between output and input efficiently. Recent studies have shown the potential of Transformer to increase the prediction capacity. However, there are several severe issues with Transformer that prevent it from being directly applicable to LSTF, including quadratic time complexity, high memory usage, and inherent limitation of the encoder-decoder architecture. To address these issues, we design an efficient transformer-based model for LSTF, named Informer, with three distinctive characteristics: (i) a ProbSparse self-attention mechanism, which achieves O(L log L) in time complexity and memory usage, and has comparable performance on sequences' dependency alignment. (ii) the self-attention distilling highlights dominating attention by halving cascading layer input, and efficiently handles extreme long input sequences.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

(iii) the generative style decoder, while conceptually simple, predicts the long time-series sequences at one forward operation rather than a step-by-step way, which drastically improves the inference speed of long-sequence predictions. Extensive experiments on four large-scale datasets demonstrate that Informer significantly outperforms existing methods and provides a new solution to the LSTF problem.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Time-series forecasting is a critical ingredient across many domains, such as sensor network monitoring, energy and smart grid management, economics and finance, and disease propagation analysis. In these scenarios, we can leverage a substantial amount of time-series data on past behavior to make a forecast in the long run, namely long sequence time-series forecasting (LSTF). However, existing methods are mostly designed under short-term problem setting, like predicting 48 points or less. The increasingly long sequences strain the models' prediction capacity to the point where this trend is holding the research on LSTF. As an empirical example, Fig. shows the forecasting results on a real dataset, where the LSTM network predicts the hourly temperature of an electrical transformer station from the short-term period (12 points, 0.5 days) to the long-term period (480 points, 20 days). The overall performance gap is substantial when the prediction length is greater than 48 points (the solid star in Fig.(1b)), where the MSE rises to unsatisfactory performance, the inference speed gets sharp drop, and the LSTM model starts to fail.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The major challenge for LSTF is to enhance the prediction capacity to meet the increasingly long sequence demand, which requires (a) extraordinary long-range alignment ability and (b) efficient operations on long sequence inputs and outputs. Recently, Transformer models have shown superior performance in capturing long-range dependency than RNN models. The self-attention mechanism can reduce the maximum length of network signals traveling paths into the theoretical shortest $\mathcal{O}{}$ and avoid the recurrent structure, whereby Transformer shows great potential for the LSTF problem. Nevertheless, the self-attention mechanism violates requirement (b) due to its $L$-quadratic computation and memory consumption on $L$-length inputs/outputs. Some large-scale Transformer models pour resources and yield impressive results on NLP tasks, but the training on dozens of GPUs and expensive deploying cost make theses models unaffordable on real-world LSTF problem. The efficiency of the self-attention mechanism and Transformer architecture becomes the bottleneck of applying them to LSTF problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Thus, in this paper, we seek to answer the question: *can we improve Transformer models to be computation, memory, and architecture efficient, as well as maintaining higher prediction capacity?*

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The quadratic computation of self-attention. The atom operation of self-attention mechanism, namely canonical dot-product, causes the time complexity and memory usage per layer to be $\mathcal{O}{(L^{2})}$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The memory bottleneck in stacking layers for long inputs. The stack of $J$ encoder/decoder layers makes total memory usage to be $\mathcal{O}{({J \cdot L^{2}})}$, which limits the model scalability in receiving long sequence inputs.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The speed plunge in predicting long outputs. Dynamic decoding of vanilla Transformer makes the step-by-step inference as slow as RNN-based model (Fig.(1b)).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are some prior works on improving the efficiency of self-attention. The Sparse Transformer, LogSparse Transformer, and Longformer all use a heuristic method to tackle limitation 1 and reduce the complexity of self-attention mechanism to $\mathcal{O}{({L{\log L}})}$, where their efficiency gain is limited. Reformer also achieves $\mathcal{O}{({L{\log L}})}$ with locally-sensitive hashing self-attention, but it only works on extremely long sequences. More recently, Linformer claims a linear complexity $\mathcal{O}{(L)}$, but the project matrix can not be fixed for real-world long sequence input, which may have the risk of degradation to $\mathcal{O}{(L^{2})}$. Transformer-XL and Compressive Transformer use auxiliary hidden states to capture long-range dependency, which could amplify limitation 1 and be adverse to break the efficiency bottleneck. All these works mainly focus on limitation 1, and the limitation 2&3 remains unsolved in the LSTF problem.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

To enhance the prediction capacity, we tackle all these limitations and achieve improvement beyond efficiency in the proposed Informer.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, our work delves explicitly into these three issues. We investigate the sparsity in the self-attention mechanism, make improvements of network components, and conduct extensive experiments.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose Informer to successfully enhance the prediction capacity in the LSTF problem, which validates the Transformer-like model's potential value to capture individual long-range dependency between long sequence time-series outputs and inputs.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose *ProbSparse* self-attention mechanism to efficiently replace the canonical self-attention. It achieves the $\mathcal{O}{({L{\log L}})}$ time complexity and $\mathcal{O}{({L{\log L}})}$ memory usage on dependency alignments.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose self-attention distilling operation to privilege dominating attention scores in $J$-stacking layers and sharply reduce the total space complexity to be $\mathcal{O}{({{({2 - \epsilon})}L{\log L}})}$, which helps receiving long sequence input.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose generative style decoder to acquire long sequence output with only one forward step needed, simultaneously avoiding cumulative error spreading during the inference phase.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Preliminary", "weight": 1.0} -->

Encoder-decoder architecture Many popular models are devised to "encode" the input representations $\mathcal{X}^{t}$ into a hidden state representations $\mathcal{H}^{t}$ and "decode" an output representations $\mathcal{Y}^{t}$ from $\mathcal{H}^{t} = {\{\mathbf{h}_{1}^{t},\ldots,\mathbf{h}_{L_{h}}^{t}\}}$. The inference involves a step-by-step process named "dynamic decoding", where the decoder computes a new hidden state $\mathbf{h}_{k + 1}^{t}$ from the previous state $\mathbf{h}_{k}^{t}$ and other necessary outputs from $k$-th step then predict the $({k + 1})$-th sequence $\mathbf{y}_{k + 1}^{t}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Preliminary", "weight": 1.0} -->

Input Representation A uniform input representation is given to enhance the global positional context and local temporal context of the time-series inputs. To avoid trivializing description, we put the details in Appendix B.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Methodology", "weight": 1.0} -->

Existing methods for time-series forecasting can be roughly grouped into two categories^11^1Related work is in Appendix A due to space limitation.. Classical time-series models serve as a reliable workhorse for time-series forecasting, and deep learning techniques mainly develop an encoder-decoder prediction paradigm by using RNN and their variants. Our proposed Informer holds the encoder-decoder architecture while targeting the LSTF problem. Please refer to Fig. for an overview and the following sections for details.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Efficient Self-attention Mechanism", "weight": 1.0} -->

Some previous attempts have revealed that the distribution of self-attention probability has potential sparsity, and they have designed "selective" counting strategies on all $p{(\left. \mathbf{k}_{j} \middle| \mathbf{q}_{i} \right.)}$ without significantly affecting the performance. The Sparse Transformer incorporates both the row outputs and column inputs, in which the sparsity arises from the separated spatial correlation. The LogSparse Transformer notices the cyclical pattern in self-attention and forces each cell to attend to its previous one by an exponential step size. The Longformer extends previous two works to more complicated sparse configuration. However, they are limited to theoretical analysis from following heuristic methods and tackle each multi-head self-attention with the same strategy, which narrows their further improvement.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Efficient Self-attention Mechanism", "weight": 1.0} -->

To motivate our approach, we first perform a qualitative assessment on the learned attention patterns of the canonical self-attention. The "sparsity" self-attention score forms a long tail distribution (see Appendix C for details), i.e., a few dot-product pairs contribute to the major attention, and others generate trivial attention. Then, the next question is how to distinguish them?

<!-- chunk {"id": "body-0022", "role": "body", "section": "Efficient Self-attention Mechanism", "weight": 1.0} -->

Query Sparsity Measurement From Eq., the $i$-th query's attention on all the keys are defined as a probability $p{(\left. \mathbf{k}_{j} \middle| \mathbf{q}_{i} \right.)}$ and the output is its composition with values $\mathbf{v}$. The dominant dot-product pairs encourage the corresponding query's attention probability distribution away from the uniform distribution. If $p{(\left. \mathbf{k}_{j} \middle| \mathbf{q}_{i} \right.)}$ is close to a uniform distribution ${q{(\left. \mathbf{k}_{j} \middle| \mathbf{q}_{i} \right.)}} = {1/L_{K}}$, the self-attention becomes a trivial sum of values $\mathbf{V}$ and is redundant to the residential input. Naturally, the "likeness" between distribution $p$ and $q$ can be used to distinguish the "important" queries.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Efficient Self-attention Mechanism", "weight": 1.0} -->

where the first term is the Log-Sum-Exp (LSE) of $\mathbf{q}_{i}$ on all the keys, and the second term is the arithmetic mean on them. If the $i$-th query gains a larger $M{(\mathbf{q}_{i},\mathbf{K})}$, its attention probability $p$ is more "diverse" and has a high chance to contain the dominate dot-product pairs in the header field of the long tail self-attention distribution.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Efficient Self-attention Mechanism", "weight": 1.0} -->

where $\overline{\mathbf{Q}}$ is a sparse matrix of the same size of $\mathbf{q}$ and it only contains the Top-$u$ queries under the sparsity measurement $M{(\mathbf{q},\mathbf{K})}$. Controlled by a constant sampling factor $c$, we set $u = {c \cdot {\ln L_{Q}}}$, which makes the *ProbSparse* self-attention only need to calculate $\mathcal{O}{({\ln L_{Q}})}$ dot-product for each query-key lookup and the layer memory usage maintains $\mathcal{O}{({L_{K}{\ln L_{Q}}})}$. Under the multi-head perspective, this attention generates different sparse query-key pairs for each head, which avoids severe information loss in return.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Efficient Self-attention Mechanism", "weight": 1.0} -->

However, the traversing of all the queries for the measurement $M{(\mathbf{q}_{i},\mathbf{K})}$ requires calculating each dot-product pairs, i.e., quadratically $\mathcal{O}{({L_{Q}L_{K}})}$, besides the LSE operation has the potential numerical stability issue. Motivated by this, we propose an empirical approximation for the efficient acquisition of the query sparsity measurement.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Encoder: Allowing for Processing Longer Sequential Inputs under the Memory Usage Limitation", "weight": 1.0} -->

The encoder is designed to extract the robust long-range dependency of the long sequential inputs. After the input representation, the $t$-th sequence input $\mathcal{X}^{t}$ has been shaped into a matrix $\mathbf{X}_{\text{en}}^{t} \in {\mathbb{R}}^{L_{x} \times d_{\text{model}}}$. We give a sketch of the encoder in Fig. for clarity.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Encoder: Allowing for Processing Longer Sequential Inputs under the Memory Usage Limitation", "weight": 1.0} -->

Self-attention Distilling As the natural consequence of the *ProbSparse* self-attention mechanism, the encoder's feature map has redundant combinations of value $\mathbf{V}$. We use the distilling operation to privilege the superior ones with dominating features and make a focused self-attention feature map in the next layer. It trims the input's time dimension sharply, seeing the $n$-heads weights matrix (overlapping red squares) of Attention blocks in Fig..

<!-- chunk {"id": "body-0028", "role": "body", "section": "Encoder: Allowing for Processing Longer Sequential Inputs under the Memory Usage Limitation", "weight": 1.0} -->

where ${\lbrack \cdot \rbrack}_{\text{AB}}$ represents the attention block. It contains the Multi-head *ProbSparse* self-attention and the essential operations, where $\text{Conv1d}{( \cdot )}$ performs an 1-D convolutional filters (kernel width=3) on time dimension with the $\text{ELU}{( \cdot )}$ activation function. We add a max-pooling layer with stride 2 and down-sample $\mathbf{X}^{t}$ into its half slice after stacking a layer, which reduces the whole memory usage to be $\mathcal{O}{({{({2 - \epsilon})}L{\log L}})}$, where $\epsilon$ is a small number. To enhance the robustness of the distilling operation, we build replicas of the main stack with halving inputs, and progressively decrease the number of self-attention distilling layers by dropping one layer at a time, like a pyramid in Fig., such that their output dimension is aligned.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Encoder: Allowing for Processing Longer Sequential Inputs under the Memory Usage Limitation", "weight": 1.0} -->

Thus, we concatenate all the stacks' outputs and have the final hidden representation of encoder.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Decoder: Generating Long Sequential Outputs Through One Forward Procedure", "weight": 1.0} -->

We use a standard decoder structure in Fig., and it is composed of a stack of two identical multi-head attention layers. However, the generative inference is employed to alleviate the speed plunge in long prediction. We feed the decoder with the following vectors as

<!-- chunk {"id": "body-0031", "role": "body", "section": "Decoder: Generating Long Sequential Outputs Through One Forward Procedure", "weight": 1.0} -->

where $\mathbf{X}_{\text{token}}^{t} \in {\mathbb{R}}^{L_{\text{token}} \times d_{\text{model}}}$ is the start token, $\mathbf{X}_{\mathbf{0}}^{t} \in {\mathbb{R}}^{L_{y} \times d_{\text{model}}}$ is a placeholder for the target sequence (set scalar as 0). Masked multi-head attention is applied in the *ProbSparse* self-attention computing by setting masked dot-products to $- \infty$. It prevents each position from attending to coming positions, which avoids auto-regressive. A fully connected layer acquires the final output, and its outsize $d_{y}$ depends on whether we are performing a univariate forecasting or a multivariate one.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Decoder: Generating Long Sequential Outputs Through One Forward Procedure", "weight": 1.0} -->

Generative Inference Start token is efficiently applied in NLP's "dynamic decoding", and we extend it into a generative way. Instead of choosing specific flags as the token, we sample a $L_{\text{token}}$ long sequence in the input sequence, such as an earlier slice before the output sequence. Take predicting 168 points as an example (7-day temperature prediction in the experiment section), we will take the known 5 days before the target sequence as "start-token", and feed the generative-style inference decoder with $\mathbf{X}_{\text{de}} = {\{\mathbf{X}_{5d},\mathbf{X}_{\mathbf{0}}\}}$. The $\mathbf{X}_{\mathbf{0}}$ contains target sequence's time stamp, i.e., the context at the target week. Then our proposed decoder predicts outputs by one forward procedure rather than the time consuming "dynamic decoding" in the conventional encoder-decoder architecture. A detailed performance comparison is given in the computation efficiency section.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Decoder: Generating Long Sequential Outputs Through One Forward Procedure", "weight": 1.0} -->

Loss function We choose the MSE loss function on prediction w.r.t the target sequences, and the loss is propagated back from the decoder's outputs across the entire model.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Datasets", "weight": 1.0} -->

We extensively perform experiments on four datasets, including 2 collected real-world datasets for LSTF and 2 public benchmark datasets.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Datasets", "weight": 1.0} -->

ETT (Electricity Transformer Temperature)^22^2We collected the ETT dataset and published it at The ETT is a crucial indicator in the electric power long-term deployment. We collected 2-year data from two separated counties in China. To explore the granularity on the LSTF problem, we create separate datasets as {ETTh~1~, ETTh~2~} for 1-hour-level and ETTm~1~ for 15-minute-level. Each data point consists of the target value "oil temperature" and 6 power load features. The train/val/test is 12/4/4 months.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Datasets", "weight": 1.0} -->

ECL (Electricity Consuming Load)^33^3ECL dataset was acquired at It collects the electricity consumption (Kwh) of 321 clients. Due to the missing data, we convert the dataset into hourly consumption of 2 years and set 'MT_320' as the target value. The train/val/test is 15/3/4 months.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Datasets", "weight": 1.0} -->

Weather ^44^4Weather dataset was acquired at This dataset contains local climatological data for nearly 1,600 U.S. locations, 4 years from 2010 to 2013, where data points are collected every 1 hour. Each data point consists of the target value "wet bulb" and 11 climate features. The train/val/test is 28/10/10 months.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experimental Details", "weight": 1.0} -->

We briefly summarize basics, and more information on network components and setups are given in Appendix E.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experimental Details", "weight": 1.0} -->

Baselines: We have selected five time-series forecasting methods as comparison, including ARIMA, Prophet, LSTMa, LSTnet and DeepAR. To better explore the *ProbSparse* self-attention's performance in our proposed Informer, we incorporate the canonical self-attention variant (Informer^†^), the efficient variant Reformer and the most related work LogSparse self-attention in the experiments. The details of network components are given in Appendix E.1.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experimental Details", "weight": 1.0} -->

Hyper-parameter tuning: We conduct grid search over the hyper-parameters, and detailed ranges are given in Appendix E.3. Informer contains a 3-layer stack and a 1-layer stack (1/4 input) in the encoder, and a 2-layer decoder. Our proposed methods are optimized with Adam optimizer, and its learning rate starts from $1e^{- 4}$, decaying two times smaller every epoch. The total number of epochs is 8 with proper early stopping. We set the comparison methods as recommended, and the batch size is 32. Setup: The input of each dataset is zero-mean normalized. Under the LSTF settings, we prolong the prediction windows size $L_{y}$ progressively, i.e., {1d, 2d, 7d, 14d, 30d, 40d} in {ETTh, ECL, Weather}, {6h, 12h, 24h, 72h, 168h} in ETTm.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experimental Details", "weight": 1.0} -->

Metrics: We use two evaluation metrics, including $\text{MSE} = {\frac{1}{n}{\sum_{i = 1}^{n}{({\mathbf{y} - \hat{\mathbf{y}}})}^{2}}}$ and $\text{MAE} = {\frac{1}{n}{\sum_{i = 1}^{n}{|{\mathbf{y} - \hat{\mathbf{y}}}|}}}$ on each prediction window (averaging for multivariate prediction), and roll the whole set with $\text{stride} = 1$. Platform: All the models were trained/tested on a single Nvidia V100 32GB GPU. The source code is available at

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experimental Details", "weight": 1.0} -->

Informer† uses the canonical self-attention mechanism.
The ‘-’ indicates failure for the out-of-memory.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experimental Details", "weight": 1.0} -->

The LSTnet is hard to present in a closed form.
The ⋆ denotes applying our proposed decoder.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Results and Analysis", "weight": 1.0} -->

Table 1 and Table 2 summarize the univariate/multivariate evaluation results of all the methods on 4 datasets. We gradually prolong the prediction horizon as a higher requirement of prediction capacity, where the LSTF problem setting is precisely controlled to be tractable on one single GPU for each method. The best results are highlighted in boldface.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Results and Analysis", "weight": 1.0} -->

Univariate Time-series Forecasting Under this setting, each method attains predictions as a single variable over time series. From Table 1, we can observe that: The proposed model Informer significantly improves the inference performance (wining-counts in the last column) across all datasets, and their predict error rises smoothly and slowly within the growing prediction horizon, which demonstrates the success of Informer in enhancing the prediction capacity in the LSTF problem. The Informer beats its canonical degradation Informer^†^ mostly in wining-counts, i.e., 32$>$`<!-- -->`{=html}12, which supports the query sparsity assumption in providing a comparable attention feature map. Our proposed method also out-performs the most related work LogTrans and Reformer. We note that the Reformer keeps dynamic decoding and performs poorly in LSTF, while other methods benefit from the generative style decoder as nonautoregressive predictors. The Informer model shows significantly better results than recurrent neural networks LSTMa.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Results and Analysis", "weight": 1.0} -->

Our method has a MSE decrease of 26.8% (at 168), 52.4% (at 336) and 60.1% (at 720). This reveals a shorter network path in the self-attention mechanism acquires better prediction capacity than the RNN-based models. The proposed method outperforms DeepAR, ARIMA and Prophet on MSE by decreasing 49.3% (at 168), 61.1% (at 336), and 65.1% (at 720) in average. On the ECL dataset, DeepAR performs better on shorter horizons ($\leq 336$), and our method surpasses on longer horizons. We attribute this to a specific example, in which the effectiveness of prediction capacity is reflected with the problem scalability.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Results and Analysis", "weight": 1.0} -->

Multivariate Time-series Forecasting Within this setting, some univariate methods are inappropriate, and LSTnet is the state-of-art baseline. On the contrary, our proposed Informer is easy to change from univariate prediction to multivariate one by adjusting the final FCN layer. From Table 2, we observe that: The proposed model Informer greatly outperforms other methods and the findings 1 & 2 in the univariate settings still hold for the multivariate time-series. The Informer model shows better results than RNN-based LSTMa and CNN-based LSTnet, and the MSE decreases 26.6% (at 168), 28.2% (at 336), 34.3% (at 720) in average. Compared with the univariate results, the overwhelming performance is reduced, and such phenomena can be caused by the anisotropy of feature dimensions' prediction capacity. It is beyond the scope of this paper, and we will explore it in the future work.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Results and Analysis", "weight": 1.0} -->

LSTF with Granularity Consideration We perform an additional comparison to explore the performance with various granularities. The sequences {96, 288, 672} of ETTm~1~ (minutes-level) are aligned with {24, 48, 168} of ETTh~1~ (hour-level). The Informer outperforms other baselines even if the sequences are at different granularity levels.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Parameter Sensitivity", "weight": 1.0} -->

We perform the sensitivity analysis of the proposed Informer model on ETTh1 under the univariate setting. Input Length: In Fig.(4a), when predicting short sequences (like 48), initially increasing input length of encoder/decoder degrades performance, but further increasing causes the MSE to drop because it brings repeat short-term patterns. However, the MSE gets lower with longer inputs in predicting long sequences (like 168). Because the longer encoder input may contain more dependencies, and the longer decoder token has rich local information. Sampling Factor: The sampling factor controls the information bandwidth of *ProbSparse* self-attention in Eq.. We start from the small factor (=3) to large ones, and the general performance increases a little and stabilizes at last in Fig.(4b). It verifies our query sparsity assumption that there are redundant dot-product pairs in the self-attention mechanism. We set the sample factor $c = 5$ (the red line) in practice.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Parameter Sensitivity", "weight": 1.0} -->

The Combination of Layer Stacking: The replica of Layers is complementary for the self-attention distilling, and we investigate each stack {L, L/2, L/4}'s behavior in Fig.(4c). The longer stack is more sensitive to the inputs, partly due to receiving more long-term information. Our method's selection (the red line), i.e., joining L and L/4, is the most robust strategy.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Ablation Study: How well Informer works?", "weight": 1.0} -->

We also conducted additional experiments on ETTh~1~ with ablation consideration.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Ablation Study: How well Informer works?", "weight": 1.0} -->

Informer‡ removes the self-attention distilling from Informer†.
The ‘-’ indicates failure for the out-of-memory.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Ablation Study: How well Informer works?", "weight": 1.0} -->

Informer§ replaces our decoder with dynamic decoding one in Informer‡.
The ‘-’ indicates failure for the unacceptable metric results.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Ablation Study: How well Informer works?", "weight": 1.0} -->

The performance of *ProbSparse* self-attention mechanism In the overall results Table 1 & 2, we limited the problem setting to make the memory usage feasible for the canonical self-attention. In this study, we compare our methods with LogTrans and Reformer, and thoroughly explore their extreme performance. To isolate the memory efficient problem, we first reduce settings as {batch size=8, heads=8, dim=64}, and maintain other setups in the univariate case. In Table 4, the *ProbSparse* self-attention shows better performance than the counterparts. The LogTrans gets OOM in extreme cases because its public implementation is the mask of the full-attention, which still has $\mathcal{O}{(L^{2})}$ memory usage. Our proposed *ProbSparse* self-attention avoids this from the simplicity brought by the query sparsity assumption in Eq., referring to the pseudo-code in Appendix E.2, and reaches smaller memory usage.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Ablation Study: How well Informer works?", "weight": 1.0} -->

The performance of self-attention distilling In this study, we use Informer^†^ as the benchmark to eliminate additional effects of *ProbSparse* self-attention. The other experimental setup is aligned with the settings of univariate Time-series. From Table 5, Informer^†^ has fulfilled all the experiments and achieves better performance after taking advantage of long sequence inputs. The comparison method Informer^‡^ removes the distilling operation and reaches OOM with longer inputs ($> 720$). Regarding the benefits of long sequence inputs in the LSTF problem, we conclude that the self-attention distilling is worth adopting, especially when a longer prediction is required.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Ablation Study: How well Informer works?", "weight": 1.0} -->

The performance of generative style decoder In this study, we testify the potential value of our decoder in acquiring a "generative" results. Unlike the existing methods, the labels and outputs are forced to be aligned in the training and inference, our proposed decoder's predicting relies solely on the time stamp, which can predict with offsets. From Table 6, we can see that the general prediction performance of Informer^‡^ resists with the offset increasing, while the counterpart fails for the dynamic decoding. It proves the decoder's ability to capture individual long-range dependency between arbitrary outputs and avoid error accumulation.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Computation Efficiency", "weight": 1.0} -->

With the multivariate setting and all the methods' current finest implement, we perform a rigorous runtime comparison in Fig.. During the training phase, the Informer (red line) achieves the best training efficiency among Transformer-based methods. During the testing phase, our methods are much faster than others with the generative style decoding. The comparisons of theoretical time complexity and memory usage are summarized in Table 4. The performance of Informer is aligned with the runtime experiments. Note that the LogTrans focus on improving the self-attention mechanism, and we apply our proposed decoder in LogTrans for a fair comparison (the $\star$ in Table 4).

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we studied the long-sequence time-series forecasting problem and proposed Informer to predict long sequences. Specifically, we designed the *ProbSparse* self-attention mechanism and distilling operation to handle the challenges of quadratic time complexity and quadratic memory usage in vanilla Transformer. Also, the carefully designed generative decoder alleviates the limitation of traditional encoder-decoder architecture. The experiments on real-world data demonstrated the effectiveness of Informer for enhancing the prediction capacity in LSTF problem.
