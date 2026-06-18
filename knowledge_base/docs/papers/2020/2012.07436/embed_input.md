Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting

Topics include Transformers, Attention mechanisms, Datasets, Planning, Informer, LSTF.

Many real-world applications require the prediction of long sequence time-series, such as electricity consumption planning. Long sequence time-series forecasting (LSTF) demands a high prediction capacity of the model, which is the ability to capture precise long-range dependency coupling between output and input efficiently. Recent studies have shown the potential of Transformer to increase the prediction capacity. However, there are several severe issues with Transformer that prevent it from being directly applicable to LSTF, including quadratic time complexity, high memory usage, and inherent limitation of the encoder-decoder architecture. To address these issues, we design an efficient transformer-based model for LSTF, named Informer, with three distinctive characteristics: (i) a ProbSparse self-attention mechanism, which achieves O(L log L) in time complexity and memory usage, and has comparable performance on sequences' dependency alignment. (ii) the self-attention distilling highlights dominating attention by halving cascading layer input, and efficiently handles extreme long input sequences....

## Introduction

Time-series forecasting is a critical ingredient across many domains, such as sensor network monitoring, energy and smart grid management, economics and finance, and disease propagation analysis. In these scenarios, we can leverage a substantial amount of time-series data on past behavior to make a forecast in the long run, namely long sequence time-series forecasting (LSTF). However, existing methods are mostly designed under short-term problem setting, like predicting 48 points or less. The increasingly long sequences strain the models' prediction capacity to the point where this trend is holding the research on LSTF....

Figure 1: (a) LSTF can cover an extended period than the short sequence predictions, making vital distinction in policy-planning and investment-protecting. (b) The prediction capacity of existing methods limits LSTF’s performance. E.g., starting from length=48, MSE rises unacceptably high, and the inference speed drops rapidly.

## Conclusion

In this paper, we studied the long-sequence time-series forecasting problem and proposed Informer to predict long sequences. Specifically, we designed the *ProbSparse* self-attention mechanism and distilling operation to handle the challenges of quadratic time complexity and quadratic memory usage in vanilla Transformer. Also, the carefully designed generative decoder alleviates the limitation of traditional encoder-decoder architecture. The experiments on real-world data demonstrated the effectiveness of Informer for enhancing the prediction capacity in LSTF problem.

Generative Inference Start token is efficiently applied in NLP's "dynamic decoding", and we extend it into a generative way. Instead of choosing specific flags as the token, we sample a $L_{\text{token}}$ long sequence in the input sequence, such as an earlier slice before the output sequence. Take predicting 168 points as an example (7-day temperature prediction in the experiment section), we will take the known 5 days before the target sequence as "start-token", and feed the generative-style inference decoder with $\mathbf{X}_{\text{de}} = {\{\mathbf{X}_{5d},\mathbf{X}_{\mathbf{0}}\}}$....

where the first term is the Log-Sum-Exp (LSE) of $\mathbf{q}_{i}$ on all the keys, and the second term is the arithmetic mean on them....
