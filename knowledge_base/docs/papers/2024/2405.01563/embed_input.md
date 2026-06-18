Mitigating LLM Hallucinations via Conformal Abstention

We develop a principled procedure for determining when a large language model (LLM) should abstain from responding (e.g., by saying "I don't know") in a general domain, instead of resorting to possibly "hallucinating" a non-sensical or incorrect answer. Building on earlier approaches that use self-consistency as a more reliable measure of model confidence, we propose using the LLM itself to self-evaluate the similarity between each of its sampled responses for a given query. We then further leverage conformal prediction techniques to develop an abstention procedure that benefits from rigorous theoretical guarantees on the hallucination rate (error rate). Experimentally, our resulting conformal abstention method reliably bounds the hallucination rate on various closed-book, open-domain generative question answering datasets, while also maintaining a significantly less conservative abstention rate on a dataset with long responses (Temporal Sequences) compared to baselines using log-probability scores to quantify uncertainty, while achieveing comparable performance on a dataset with short answers (TriviaQA)....

## Introduction

Large language models are excellent at next word prediction. At the same time, however, they are also prone to *hallucination*---that is, confidently generate responses that may look plausible on the surface, but that are actually incorrect or even nonsensical Ji et al., Maynez et al.. Unfortunately, hallucinations are difficult to detect, especially when users are not able to easily verify the factuality of an LLM's responses by themselves. In generation tasks in particular, it can be challenging to discriminate between hallucinations that present false facts, and any of the many other viable ways of expressing correct information....

In this work, we develop a principled abstention policy that mitigates LLM hallucination by simply choosing to either produce a single response from the model that is likely to be hallucination-free, or otherwise abstain from producing a response altogether (e.g., by saying "I don't know"). The quality of such a policy can be measured by two quantities: the expected proportion of time the method chooses to abstain, and the expected proportion of unfiltered hallucinations in the responses; we will henceforth refer to these as the *abstention rate* and the hallucination *risk*, respectively.

## Conclusions and future directions

We proposed a conformal calibration and similarity scoring procedure which enables LLMs to abstain in a principled way. In particular, one of our main contributions is a novel procedure to generate match scores to count the number of similar responses to a query. When combined with conformal calibration, this scoring procedure achieves a good trade-off between abstention rate and test performance. Importantly, in experiments over two question-answering datasets, our proposed procedure surpasses the simple baseline scoring procedure of using log-probabilities of the predictor (once more suggesting that LLMs are not well-calibrated)....

## Calibrating the match function $m$

The proof is based on and. In particular, for some $\gamma > 0$, consider the following probability:

Manakul et al. study a black-box approach to detecting hallucinations by generating multiple responses, and measuring similarity of a reference response and the set of generated responses. They consider various measures of similarity, including LLM self-prompting....
