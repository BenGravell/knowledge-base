To Believe or Not to Believe Your LLM

We explore uncertainty quantification in large language models (LLMs), with the goal to identify when uncertainty in responses given a query is large. We simultaneously consider both epistemic and aleatoric uncertainties, where the former comes from the lack of knowledge about the ground truth (such as about facts or the language), and the latter comes from irreducible randomness (such as multiple possible answers). In particular, we derive an information-theoretic metric that allows to reliably detect when only epistemic uncertainty is large, in which case the output of the model is unreliable. This condition can be computed based solely on the output of the model obtained simply by some special iterative prompting based on the previous responses. Such quantification, for instance, allows to detect hallucinations (cases when epistemic uncertainty is high) in both single- and multi-answer responses. This is in contrast to many standard uncertainty quantification strategies (such as thresholding the log-likelihood of a response) where hallucinations in the multi-answer case cannot be detected....

## Introduction

> *Who's talking?* I asked, peering behind the mirror. Many dead spiders and a lot of dust were there. Then I pressed my left eye with my index finger. This was an old formula for detecting hallucinations, which I had read in To Believe or Not to Believe?, the gripping book by B. B. Bittner. It is sufficient to press on the eyeball, and all the real objects, in contradistinction to the hallucinated, will double. The mirror promptly divided into two and my worried and sleep-dulled face appeared in it.

---\"Monday Starts on Saturday\" by A. and B. Strugatsky

## Conclusions

In this paper we considered *epistemic* uncertainty as a proxy for the truthfulness of LLMs. We proposed a mutual-information-based uncertainty estimator that admits a provable lower bound on the epistemic uncertainty of the LLM's response to a query. That we consider joint distributions of multiple answers allows us to disentangle epistemic and aleatoric uncertainty, which makes it possible to better detect hallucination than first order methods, which can only tackle uncertainty as a whole, not epistemic uncertainty alone....

The above is a *pseudo* joint distribution since the standard conditioning in the chain-rule is replaced with prompt functions of the conditioning variables. In the following we focus on $\overset{\sim}{Q}$ derived from the LLM and $\overset{\sim}{P}$ derived from the ground truth.

Q: Name a yellow fruit A: Banana (0.715) and Lemon (0.284).

Arguably, in practice, such situations are rare, as in natural languages we will not encounter all possible strings. To this end, we consider an optimistic scenario where the *effective* support of $\mu$, denoted by $\overset{\sim}{\mathcal{X}}$, is small with high probability. In this case, we can replace the size of the support for strings of length $n$, ${|\mathcal{X}|}^{n}$, in the first bound with the effective support size $|\overset{\sim}{\mathcal{X}}|$, and we only pay essentially a factor $\ln{({1 + {k{|\overset{\sim}{\mathcal{X}}|}}})}$ instead of $n{\ln{({1 + {k{|\mathcal{X}|}}})}}$....

Like the protagonist of the novel, language models too occasionally suffer from *hallucinations*, or responses with low truthfulness, that do not match our own common or textbook knowledge (Bubeck et al. Gemini Team, Google, )....
