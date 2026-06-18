Training Verifiers to Solve Math Word Problems

State-of-the-art language models can match human performance on many tasks, but they still struggle to robustly perform multi-step mathematical reasoning. To diagnose the failures of current models and support research, we introduce GSM8K, a dataset of 8.5K high quality linguistically diverse grade school math word problems. We find that even the largest transformer models fail to achieve high test performance, despite the conceptual simplicity of this problem distribution. To increase performance, we propose training verifiers to judge the correctness of model completions. At test time, we generate many candidate solutions and select the one ranked highest by the verifier. We demonstrate that verification significantly improves performance on GSM8K, and we provide strong empirical evidence that verification scales more effectively with increased data than a finetuning baseline.

## Introduction

In recent years, large language models have demonstrated impressive skills across many diverse tasks. Kaplan et al. describe the consistent benefits of increasing model size, characterizing scaling trends that hold across many orders of magnitude. However, even the largest models falter when required to perform multi-step mathematical reasoning. Model samples frequently contain catastrophic mistakes, even after the model has been appropriately finetuned. Mathematical reasoning thus reveals a critical weakness in modern language models.

One significant challenge in mathematical reasoning is the high sensitivity to individual mistakes. When generating a solution, autoregressive models have no mechanism to correct their own errors. Solutions that veer off-course quickly become unrecoverable. If we rely purely on generative methods and extrapolate from current trends, we will require an exorbitant parameter count to achieve even moderate performance on distributions as challenging as the MATH dataset. This evidence strongly motivates the search for methods with more favorable scaling laws.

We propose training verifiers to evaluate the correctness of model generated solutions, similar to concurrent work by Shen et al.. At test time, we sample a fixed number of candidate solutions and select the solution ranked highest by the verifier. Verifiers benefit both from their inherent optionality and from verification being a simpler task than generation in general.

We present a curated dataset of 8.5K grade school math questions and natural language solutions, useful for probing the informal reasoning ability of large language models.

## Conclusion

We have seen that verification provides a significant performance boost relative to a finetuning baseline. On the full dataset, 6B verification slightly outperforms a finetuned 175B model, thereby offering a boost approximately equivalent to a 30x model size increase. We have also seen that token-level verifiers are less prone to overfitting than solution-level verifiers, and that all methods benefit from regularization with residual dropout. We expect verification to scale well to problem distributions that require more complex mathematical reasoning, and we hope GSM8K supports the development of new methods that scale even better.
