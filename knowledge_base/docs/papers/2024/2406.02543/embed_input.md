<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

To Believe or Not to Believe Your LLM

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We explore uncertainty quantification in large language models (LLMs), with the goal to identify when uncertainty in responses given a query is large. We simultaneously consider both epistemic and aleatoric uncertainties, where the former comes from the lack of knowledge about the ground truth (such as about facts or the language), and the latter comes from irreducible randomness (such as multiple possible answers). In particular, we derive an information-theoretic metric that allows to reliably detect when only epistemic uncertainty is large, in which case the output of the model is unreliable. This condition can be computed based solely on the output of the model obtained simply by some special iterative prompting based on the previous responses. Such quantification, for instance, allows to detect hallucinations (cases when epistemic uncertainty is high) in both single- and multi-answer responses. This is in contrast to many standard uncertainty quantification strategies (such as thresholding the log-likelihood of a response) where hallucinations in the multi-answer case cannot be detected. We conduct a series of experiments which demonstrate the advantage of our formulation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Further, our investigations shed some light on how the probabilities assigned to a given output by an LLM can be amplified by iterative prompting, which might be of independent interest.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

> *Who's talking?* I asked, peering behind the mirror. Many dead spiders and a lot of dust were there. Then I pressed my left eye with my index finger. This was an old formula for detecting hallucinations, which I had read in To Believe or Not to Believe?, the gripping book by B. B. Bittner. It is sufficient to press on the eyeball, and all the real objects, in contradistinction to the hallucinated, will double. The mirror promptly divided into two and my worried and sleep-dulled face appeared in it.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

---\"Monday Starts on Saturday\" by A. and B. Strugatsky Like the protagonist of the novel, language models too occasionally suffer from *hallucinations*, or responses with low truthfulness, that do not match our own common or textbook knowledge. At the same time, since LLMs work by modeling a probability distribution over texts, it is natural to view the problem of truthfulness through the lens of statistical uncertainty. In this paper we explore uncertainty quantification in LLMs. We distinguish between two sources of uncertainty: *epistemic* and *aleatoric*. Epistemic uncertainty arises from the lack of knowledge about the ground truth (e.g., facts or grammar in the language), stemming from various reasons such as insufficient amount of training data or model capacity. Aleatoric uncertainty comes from irreducible randomness in the prediction problem, such as multiple valid answers to the same query. Hence, truthfulness can be directly analyzed via looking at the epistemic uncertainty of a model in the sense that when the epistemic uncertainty is low, the model predictions must be close to the ground truth.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Rigorously identifying when (either) uncertainty is small^11^1For instance, by saying that predictions live in a confidence set with high probability. is notoriously hard, especially in deep neural networks. This is because we generally lack guarantees about learning the ground truth (consistency), or even a weaker guarantee about how large the variance of a learning algorithm is. At the same time, there exist many heuristic approaches for uncertainty quantification based on simply looking at the log-likelihood of responses, estimating entropy, ensembling, or sometimes even more principled formulations, such as conformal prediction (which however come with strong assumptions).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To the best of our knowledge, a common limitation of these approaches is that they are only meaningful in problems where there exists a *single* correct response (e.g. label) as they aim for detecting if one response is dominant (or multiple responses with the same meaning), that is, if there is only little uncertainty in the prediction. On the other hand, when multiple responses are correct, that is, there is *aleatoric uncertainty* in the ground truth, simply estimating the amount of uncertainty in the LLM's output is insufficient, as the perfect (ground-truth) predictor may have large aleatoric uncertainty and no epistemic uncertainty, while a completely useless predictor may have large epistemic uncertainty only, but the total amount of uncertainty of the two predictors might be the same.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

In this paper we address the above problem directly, and design methods to *decouple epistemic and aleatoric uncertainty*, allowing us to effectively deal with multi-response queries. Rather than trying to quantify how small epistemic uncertainty can be, we aim to identify when only the *epistemic uncertainty is large*, in which case we can suspect that the response is hallucinated.^22^2In technical terms this corresponds to giving a lower bound, rather than an upper bound, on the quantity capturing the uncertainty.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

As a starting point we make a simple observation: If multiple responses are obtained to the same query from the ground truth (the language), they should be independent from each other, that is, in probabilistic interpretation, the joint distribution of these multiple responses, for a fixed query, must be a product distribution.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

This observation can be used to measure how *far* the language model can be from the ground truth. The sequential model implemented by a language model allows us to construct a joint distribution over multiple responses, which is done through *iterative prompting of an LLM based on its previous responses* and the application of the chain rule of probability: first we ask the model to provide a response given a query, then to provide another response given the query and the first response, then a third one given the query and the first two responses, an so. This is in contrast to some of the earlier works that approached decoupling epistemic and aleatoric uncertainty for classification problems by training the model with pairs (or tuples) of labels.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

So, if the response to a prompt containing the query and previous responses is insensitive to the previous responses, we have the desired independence and the LLM-derived joint distribution can be arbitrarily close to the ground truth. On the other hand, if the responses within the context heavily influence new responses from the model then, intuitively speaking, the LLM has low confidence about the knowledge stored in its parameters, and so the LLM-derived joint distribution *cannot be close* to the ground truth. As more responses are added to the prompt, this dependence can be made more apparent, allowing to detect *epistemic uncertainty via our iterative prompting procedure*.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contributions", "weight": 1.0} -->

Interestingly, as we will see in Section 3, we can force an LLM to provide a desired (possibly incorrect) response by adding this response repeatedly to the prompt. This phenomenon is then further investigated from the viewpoint of a transformer LLM architecture in Section 3.1.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contributions", "weight": 1.0} -->

The iterative prompting procedure then leads to the following main contributions: *(i)* Based on the above iterative prompting procedure, we derive an *information-theoretic metric of epistemic uncertainty* in LLMs (Section 4), which quantifies the gap between the LLM-derived distribution over responses and the ground truth. This gap is insensitive to aleatoric uncertainty, and therefore we can quantify epistemic uncertainty even in cases where there are multiple valid responses.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Contributions", "weight": 1.0} -->

*(ii)* We derive a computable lower bound on this metric, which turns out to be a *mutual information* (MI) of an LLM-derived joint distribution over responses,^33^3Here MI is understood as a functional of a joint distribution (see Section 2). and propose a finite-sample estimator for it. We prove that this finite-sample MI estimator sometimes suffers only a negligible error even though LLMs and their derived joint distributions are defined over potentially infinite supports (all possible strings in a language).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Contributions", "weight": 1.0} -->

*(iii)* We discuss an algorithm for hallucination detection based on thresholding a finite-sample MI estimator, where the threshold is computed automatically through a *calibration* procedure. We show experimentally on closed-book open-domain question-answering benchmarks (such as TriviaQA, AmbigQA, and a dataset synthesized from WordNet) that when the data is mostly composed of either single-label or multi-label queries, our MI-based hallucination detection method surpasses a naive baseline (which is based on the likelihood of the response), and achieves essentially similar performance to that of a more advanced baseline which is based on the entropy of the output as a proxy for uncertainty. However, on datasets which contain both single- and multi-label samples at the same time, our method also significantly outperforms the entropy-based baseline, by achieving a much higher recall rate on samples with high output entropy while maintaining similar error rates.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Contributions", "weight": 1.0} -->

*(iv)* Focusing on a single self-attention head, we identify a simple mechanistic explanation for how the model output can be changed through iterative prompting using previous responses, as discussed earlier. Suppose that the prompt is composed from a query and a repeated element (e.g., a possibly wrong answer). If the query lies within the space spanned by the large principal components of a key-query matrix product, then the output will be generated according to the knowledge extracted from the training data (now stored in a value matrix). On the other hand, if the query has little overlap with the large principal components, then the repeated element is likely to be copied from the prompt.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Conditional distributions and prompting", "weight": 1.0} -->

Let $\mathcal{X}$ be the space of finite text sequences, that is $\mathcal{X} \subset \Sigma^{\ast}$ where $\Sigma$ is a finite alphabet (and $\Sigma^{\ast} = {\bigcup_{n = 1}^{\infty}\Sigma^{n}}$). Moreover, consider a family of conditional distributions $\mathcal{P} = {\{\mu:\mathcal{X}\rightarrow{\lbrack 0,1\rbrack} \mid \sum_{x \in \mathcal{X}}\mu{(x \mid x')} = 1\mspace{21mu}\forall x' \in \mathcal{X}\}}$. In the following, we let $P \in \mathcal{P}$ be the ground-truth conditional probability distribution over text sequences (responses) given a prompt, and we let $Q \in \mathcal{P}$ be the learned language model.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Probability amplification by iteratively prompting", "weight": 1.0} -->

In this section we demonstrate that, as mentioned in the introduction, repeating possible responses several times in a prompt can have pronounced effects on the output of a language model. Consider $x =$*"What is the capital of the UK?"* and $Y_{1} = \cdots = Y_{t} =$*"Another answer to question Q is Paris."* Here we can repeat the sentence *"Another answer to question Q is Paris."* an arbitrary number of times. Although the number of repetitions changes the behavior of the LLM, the correct response maintains a significant probability: as Figure 2 shows, the conditional normalized probability^55^5To obtain conditional normalized probabilities, we consider the probabilities of the two responses, and normalize them so that they add to 1.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Probability amplification by iteratively prompting", "weight": 1.0} -->

of the correct response, *"London"*, reduces from approximately 1 to about 96% as we increase the number of repetitions of the incorrect response to 100. Figure 2 shows 3 more examples where, with initially low epistemic uncertainty in the response to the query (the aleatoric uncertainty is also low as we consider single-response queries), the correct response maintains a significant or non-negligible probability even in the presence of repetitions of incorrect information, while the probability of predicting the latter is increased.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Probability amplification by iteratively prompting", "weight": 1.0} -->

Q: What is the capital of the UK? A: London ( ≈ 1.0) and Paris (1.29 × 10−10).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Probability amplification by iteratively prompting", "weight": 1.0} -->

Q: Who was the first US president? A: George Washington (0.999) and Abraham Lincoln (3.1 × 10−06).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Probability amplification by iteratively prompting", "weight": 1.0} -->

Q: Who is the author of The Grapes of Wrath? A: John Steinbeck ( ≈ 1.0) and Ernest Hemingway (1.34 × 10−10).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Probability amplification by iteratively prompting", "weight": 1.0} -->

Q: What is the largest country in the world? A: Russia (0.999) and United Kingdom (9.02 × 10−06).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Probability amplification by iteratively prompting", "weight": 1.0} -->

Q: What is the national instrument of Ireland? A: The harp (0.936) and Uilleann pipes (0.063).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Probability amplification by iteratively prompting", "weight": 1.0} -->

Q: Which actor became M in the Bond film Skyfall? A: Ralph Fiennes (0.651) and Judi Dench (0.348).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Probability amplification by iteratively prompting", "weight": 1.0} -->

Q: Which can last longer with out water a camel or a rat? A: A rat (0.538) and A camel (0.461).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Probability amplification by iteratively prompting", "weight": 1.0} -->

Q: If Monday’s child is fair of face what is Saturday’s child? A: Work hard for a living (0.093) and Full of grace (0.906).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Probability amplification by iteratively prompting", "weight": 1.0} -->

Next, we consider a queries for which the model is more uncertain. For the prompt *"What is the national instrument of Ireland?"*, we observe that responses *"The harp"* and *"Uilleann pipes"* both have significant probabilities (the first answer is the correct one). This time, by incorporating the incorrect response in the prompt multiple times, the probability of the correct answer quickly collapses to near zero, as shown in Figure 2, together with three more examples with significant epistemic uncertainty.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Probability amplification by iteratively prompting", "weight": 1.0} -->

Finally, we consider multi-label queries for which the LLM confidently knows a correct answer. This time, by incorporating a potential response in the prompt, the probabilities of other correct answers stay relatively large. Figure 3 shows four such examples.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Probability amplification by iteratively prompting", "weight": 1.0} -->

Q: Name a city in the UK A: London (0.958) and Manchester (0.041).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Probability amplification by iteratively prompting", "weight": 1.0} -->

Q: Name a yellow fruit A: Banana (0.715) and Lemon (0.284).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Probability amplification by iteratively prompting", "weight": 1.0} -->

Q: Name an alcoholic drink, A: Wine (0.685) and Beer (0.314).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Probability amplification by iteratively prompting", "weight": 1.0} -->

Q: Name a ball game that is played by more than 5 players A: Volleyball (0.542) and Soccer (0.457).

<!-- chunk {"id": "body-0034", "role": "body", "section": "In-context learning vs. in-weight learning", "weight": 1.0} -->

The sensitivity of the response of an LLM to extra in-context information, as observed above, can already be observed in a single attention head as explained next.

<!-- chunk {"id": "body-0035", "role": "body", "section": "In-context learning vs. in-weight learning", "weight": 1.0} -->

We consider an idealized attention mechanism as follows. Let $\mathbf{Z} \in^{n \times d'}$ be an input matrix comprised of $n$ semantic feature vectors each of dimension $d'$. Each row is meant to represent a complete statement (such as *"What is the capital of the UK?"* or *"One answer to the question is Paris."*, etc.) rather than a single token. Let $X^{\top} \in^{1 \times d'}$ be the first row of $\mathbf{Z}$, which represents the *query* of interest, such as *"What is the capital of the UK?"*. Let $E^{\top} \in^{1 \times d'}$ be a special vector indicating the end of the input. The matrix $\mathbf{Z} \smallsetminus X$, denoting the $\mathbf{Z}$ matrix without its first row, represents the *in-context* information.

<!-- chunk {"id": "body-0036", "role": "body", "section": "In-context learning vs. in-weight learning", "weight": 1.0} -->

We assume the ground-truth distribution $P$ is such that a query vector is mapped to its response, but a statement is simply copied. For example, for $V =$*"What is the capital of the UK?"*, $P{( \cdot \mid V)}$ would be a distribution with support on *"London"* and its variations, while for $V' =$*"What is the capital of the UK? One answer to the question is Paris."*, $P{( \cdot \mid V')}$ returns the same distribution. We assume a parameter matrix $\mathbf{W}^{\mathbf{V}}$ is learned such that $V^{\top}\mathbf{W}^{\mathbf{V}}$ estimates $P{( \cdot \mid V)}$ for vector $V$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "In-context learning vs. in-weight learning", "weight": 1.0} -->

Let ${\mathbf{W}^{\mathbf{Q}},\mathbf{W}^{\mathbf{K}},\mathbf{W}^{\mathbf{V}}} \in^{d' \times d}$ be the query, key, and value matrices. A self-attention head with query $X$ and context $\mathbf{Z} \smallsetminus X$ is defined as where the output of the softmax is a row vector of length $n$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "In-context learning vs. in-weight learning", "weight": 1.0} -->

If $X$ has appeared many times in the training data, then parameters $\mathbf{W}^{\mathbf{Q}}$ and $\mathbf{W}^{\mathbf{K}}$ could be learned such that $E^{\top}\mathbf{W}^{\mathbf{Q}}{(\mathbf{W}^{\mathbf{K}})}^{\top}X$ is large, that is, $X$ is within the space spanned by the large principal components of the key-query matrix product. Then, no matter what in-context information appears in $\mathbf{Z}$, the probability assigned to $X$ will dominate the softmax, and we will have and therefore $f{(\mathbf{Z};\mathbf{W}^{\mathbf{Q}},\mathbf{W}^{\mathbf{K}},\mathbf{W}^{\mathbf{V}})} \approx P{(\cdot \mid X)}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "In-context learning vs. in-weight learning", "weight": 1.0} -->

On the other hand, consider the case that $X$ has not appeared many times in the training data, and vector $Y$ is copied in many rows of $\mathbf{Z}$. Then $E^{\top}\mathbf{W}^{\mathbf{Q}}{(\mathbf{W}^{\mathbf{K}})}^{\top}X$ could be small as $X$ is not in the span of the large principal components of the key-query matrix product.

<!-- chunk {"id": "body-0040", "role": "body", "section": "In-context learning vs. in-weight learning", "weight": 1.0} -->

Therefore ${f{(\mathbf{Z};\mathbf{W}^{\mathbf{Q}},\mathbf{W}^{\mathbf{K}},\mathbf{W}^{\mathbf{V}})}} \approx Y$ since Even if $X$ is in the span, repeating $Y$ $t$ times in $\mathbf{Z}$ would give a $t$-times increased total weight to $Y$ inside the softmax, which can dominate the weight assigned to $X$ when $t$ is large enough, also resulting in $Y$ as the answer.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Metric of epistemic uncertainty and its estimation", "weight": 1.0} -->

In this section we apply iterative prompting to estimate the epistemic uncertainty of a language model about responding to some query. The idea is to utilize the different behavior patterns observed in Section 3, which can be used to differentiate between two modes of high uncertainty: when the aleatoric uncertainty is high vs. when only the epistemic uncertainty is high. We then apply our new uncertainty metric to design a score-based hallucination detection algorithm.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Metric of epistemic uncertainty and its estimation", "weight": 1.0} -->

We will first present the uncertainty metric and its estimate for a distribution defined on the direct outputs of an LLM, and then in Section 4.2, we discuss the changes needed to take semantic equivalences of language into account.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Metric of epistemic uncertainty and its estimation", "weight": 1.0} -->

Recall the family of prompts $\mathcal{F}$ defined in Section 2.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Assumption 4.1 (Ground truth independence assumption)", "weight": 1.0} -->

The ground-truth satisfies Note that the above assumption is heavily dependent on our prompt construction. Without embedding $Y_{1},\ldots,Y_{t - 1}$ in the prompt, the independence assumption would not hold, for example, if $Y_{1},\ldots,Y_{t}$ were partial answers, such as a step of an algorithm or a part of a story, because in such a case $Y_{t}$ might indeed depend on the previous outputs $Y_{1},\ldots,Y_{t - 1}$. Roughly speaking, the assumption tells that the response distribution is insensitive to a query based on previously sampled responses. For example, for query $x =$*"A city in the UK:"*, the probability of $Y_{2} =$*"Manchester"* does not change if a city is $Y_{1} =$*"London"*.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 4.3 (Sampling from $\\overset{\\sim}{Q}$)", "weight": 1.0} -->

In the rest of the paper we drop subscripts in joint distributions and conditioning on query $x$ (which is understood implicitly), for example, $\overset{\sim}{P} \equiv {\overset{\sim}{P}}_{{Y_{1}\cdots Y_{n}} \mid x}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 4.3 (Sampling from $\\overset{\\sim}{Q}$)", "weight": 1.0} -->

To measure epistemic uncertainty, we need to quantify how far the estimated pseudo joint distribution $\overset{\sim}{Q}$ is from the ground truth $\overset{\sim}{P}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "A computable lower bound on epistemic uncertainty", "weight": 1.0} -->

Theorem 4.5 gives a lower bound on the epistemic uncertainty by the mutual information. However, to compute the mutual information term, in practice we need to evaluate $\overset{\sim}{Q}$ on its entire support, which is potentially infinite. Practically speaking, it is impossible to observe probabilities of all strings under the language model and so we must rely on a finite sample. Therefore, we replace $\overset{\sim}{Q}$ with an empirical distribution with a finite support; in the following we show that the error induced by such an approximation is controlled. To estimate the MI we employ the method given in Algorithm 1; for generality it is presented for an arbitrary (pseudo) joint distribution $\mu$, but we keep in mind that our case of interest is $\mu = \overset{\sim}{Q}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "A computable lower bound on epistemic uncertainty", "weight": 1.0} -->

1: Input: μ ∈ ℳ1(𝒳n) any (pseudo-) joint distribution over 𝒳n k ∈ ℕ sample size γ1, γ2 ≥ 0 stabilization parameters (typically selected as 1/k) 2: Independently sample tuples X1, …, Xk ∼ μ ∈ ℳ1(𝒳n) 3: Construct a set of indices of unique elements U = {i ∈ [k]: Xi ≠ Xj ∀j < i} 4: Construct empirical distributions: for all i ∈ U, ${= {\frac{\mu{(X_{i})}}{Z},\text{where}}}\quad{Z = {\sum\limits_{j \in U}{\mu{(X_{j})}}}}$ $= {\prod\limits_{j = 1}^{n}{\sum\limits_{{t \in U}:{X_{t,j} =

<!-- chunk {"id": "body-0049", "role": "body", "section": "A computable lower bound on epistemic uncertainty", "weight": 1.0} -->

Adding $\gamma_{1}$ and $\gamma_{2}$ in the estimator ${\hat{I}}_{k}{(\gamma_{1},\gamma_{2})}$ is intended to account for the total probability of missing observations, not included while constructing $\hat{\mu}$ and ${\hat{\mu}}^{\otimes}$, making sure the estimate is bounded. Similar ideas are well-know in probability and information theory, such as in universal coding, Laplace smoothing and Good-Turing smoothing. In Section 4.2, we show an extension of the algorithm that takes semantic equivalences into account, and in the experiments section, we will present a version of the algorithm that takes advantage of the available log-likelihood function in LLMs and constructs the empirical joint and product distributions in a slightly different way. As we will show in the experiments section, $n = 2$ is sufficient to have an effective hallucination detection method for the benchmarks that we consider.

<!-- chunk {"id": "body-0050", "role": "body", "section": "A computable lower bound on epistemic uncertainty", "weight": 1.0} -->

The bias introduced by $(\gamma_{1},\gamma_{2})$ in the last equation allows us to rigorously bound the error in estimating $I{(\mu)}$ via ${\hat{I}}_{k}{(\gamma_{1},\gamma_{2})}$, which is explored next. In particular, in Theorem 4.6 we prove a high-probability lower bound on $I{(\mu)}$ in terms of ${\hat{I}}_{k}$. The core of controlling the estimation error is in accounting for the *missing mass*, or in other words, how much of $\mu$ we miss out by only observing a finite sample. In Appendix E, we present a more complete discussion and the proof of the bound on the estimation error for mutual information. Here we adapt this result to our particular case.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Taking semantic equivalences into account", "weight": 1.0} -->

Although Theorem 4.5 and Theorem 4.6 provide a lower bound for the divergence between the LLM distribution $Q$ and the ground-truth $P$, the bound might be loose as it ignores the semantic equivalences between texts. Given a semantic equivalence definition, we propose constructing new ground-truth $P'$ and LLM distribution $Q'$, where the probability of a cluster is the sum of probabilities of all semantically equivalent texts in that cluster. We use a similarity function $s$ to define semantic equivalences: two texts are considered equivalent if their similarity is greater than a given threshold $\tau$. Our choices for similarity functions in the experiments are described in Section 6. We assume the similarity function and the similarity threshold induce a clustering of the space $\mathcal{X}$, i.e. ${s{(Y,Y')}} \geq \tau$ if and only if they are in the same cluster.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Taking semantic equivalences into account", "weight": 1.0} -->

In practice, rather than constructing the aforementioned distribution $Q'$ explicitly, we can draw samples from $Q'$ by sampling from $Q$ and aggregating samples according to their clusters. The modified uncertainty estimating algorithm is shown in Algorithm 2.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Taking semantic equivalences into account", "weight": 1.0} -->

1: Input: μ ∈ ℳ1(𝒳n) any (pseudo-) joint distribution over 𝒳n k ∈ ℕ sample size γ1, γ2 ≥ 0 stabilization parameters (typically selected as 1/k) s: 𝒳n × 𝒳n→ a similarity function τ∈ a similarity threshold 2: Independently sample tuples X1, …, Xk ∼ μ ∈ ℳ1(𝒳n) 3: Construct a set of indices of unique elements U = {i ∈ [k]: Xi ≠ Xj ∀j < i} 4: Construct cluster centers S ⊂ U according to the similarity function: for all i, t ∈ S, we have s(Xi, Xt) < τ and cluster associated with Xi is D(i) = {j ∈ U: s(Xi, Xj) ≥ τ}.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Taking semantic equivalences into account", "weight": 1.0} -->

The estimator is constructed using only (semantically) equivalent elements in the sample (the indices of these representative elements are collected in $S$), that is, we do not account for duplicate samples and we aggregate probabilities of samples that are lexically different but semantically equivalent. Algorithm 2 works with the *aggregated* probability distribution $\mu' = {\overset{\sim}{Q}}'$ (line 4) by summing over cumulative probabilities over clusters. Note that ${D_{KL}{(\mu)}} \geq {D_{KL}{(\mu')}}$ by monotonicity property of KL-divergence (this is because $\mu'$ is defined on a smaller support). Therefore, Theorem 4.6 implicitly gives a bound on $I{(\mu')}$, and eventually we have ${I{(\mu)}} \geq {I{(\mu')}}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Score-based hallucination tests", "weight": 1.0} -->

Let ${{\hat{I}}_{k}{(\gamma,x)}} \equiv {{\hat{I}}_{k}{(\gamma)}}$ computed as in Algorithm 1 for $\mu = \overset{\sim}{Q}$, to emphasize the explicit dependence on the query $x$. The uncertainty estimate ${\hat{I}}_{k}{(\gamma,x)}$ derived above can be used as a score indicating the strength of our belief that the LLM hallucinates for the given query $x$. Such a score can then be used to design *abstention* policies: if the response is deemed to be hallucinated, the system abstains from responding, while a response is provided otherwise. Score-based abstention methods usually compute a score chosen by the user (such as the response likelihood or the estimator $\hat{I}{(\gamma)}$ discussed earlier), and declare hallucination if the score is above or below a threshold, which is determined through calibration.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Score-based hallucination tests", "weight": 1.0} -->

To detect hallucinations successfully, the threshold can be adjusted through *calibration* on a given task using a hold-out (ground-truth) sample, see, for instance, the paper of Yadkori et al. where this calibration is discussed in detail.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Score-based hallucination tests", "weight": 1.0} -->

Given our estimated lower bound on the epistemic uncertainty, we can define an *abstention policy* (a policy which decides when the LLM should abstain from prediction) as where $\lambda > 0$ is a threshold parameter tuned on a hold-out sample of some particular task. This policy abstains (${a_{\lambda}{(x)}} = 1$) when the epistemic uncertainty in the prediction (response) is large. When the policy does not abstain (${a_{\lambda}{(x)}} = 0$), any prediction from $\hat{Q}$ can be served.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Score-based hallucination tests", "weight": 1.0} -->

In the experiments, we compare a number of scoring functions for detecting hallucinations, including $\hat{I}{(\gamma)}$, the probability of the greedy (temperature zero) response, and an estimate of the entropy of the response distribution.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section we evaluate our abstention method derived based on the MI estimate in Section 5 on a variety of closed-book open-domain question-answering tasks.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Experiments", "weight": 1.0} -->

Language model. We used a Gemini 1.0 Pro model to generate outputs and scores.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Experiments", "weight": 1.0} -->

Datasets. We consider three different datasets and their combinations: As base datasets, we consider *(i)* a random subset of $50,000$ datapoints from the TriviaQA dataset, and *(ii)* the entire AmbigQA dataset (with $12038$ datapoints). These datasets mostly contain single-label queries, and only contain a few multi-label ones.^77^7Note that the multi-label queries in these datasets typically behave as single-label ones in the sense that the LLM assigns overwhelming probability to a dominant response. Moreover, we created a multi-label dataset based on the WordNet dataset: We extracted all datapoints from WordNet at depth $4$ or more of the physical_entity subtree. For each datapoint (entity, children) in WordNet, we constructed a query of the form *"Name a type of entity."* and children are considered target labels.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Experiments", "weight": 1.0} -->

Comparison of responses and computing the output distributions.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Experiments", "weight": 1.0} -->

We use the F1 score^88^8 In this context, the F1 score is calculated based on token inclusion: for two sequences $a = {(a_{1},\ldots,a_{n})}$ and $b = {(b_{1},\ldots,b_{m})}$, defining $p = {{|{a \cap b}|}/n}$ and $r = {{|{a \cap b}|}/m}$ (where $|{a \cap b}|$ is the size of the intersection of $a$ and $b$, in which for repetitions of an element $y$, we consider the minimum number of repetitions in $a$ and $b$, i.e., $\min_{c \in {\{ a,b\}}}{|{\{ i:{c_{i} = y}\}}|}$, in calculating the size of the intersection) we define ${F1} = {{2pr}/{({p + r})}}$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Experiments", "weight": 1.0} -->

Relating to the standard definition of the F1 score, $p$ and $r$ play the role of precision and recall, respectively, if $a$ is thought of as a prediction of $b$. thresholded at $0.25$ to decide if two text sequences match. When multiple responses are sampled, we approximate the output distribution of an LLM in a semantically meaningful way by collapsing matching responses into a single response: we sample $k = 10$ responses at temperature $0.9$ for each query, and after eliminating repetitions, all those that match (according to the F1 score) are considered identical and their probabilities are aggregated. We only consider queries for which the greedy (temperature zero) and at least one of the random responses are shorter than $20$ characters. This is because the F1 score (as a match function) and log-probabilities (as a measure of uncertainty) are less reliable for longer sequences. After this filtering, we are left with $38870$ datapoints for TriviaQA, $5315$ datapoints for AmbigQA, and $3296$ datapoints for WordNet.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Experiments", "weight": 1.0} -->

As shown in prior works (e.g. Kuhn et al., Yadkori et al. ), we can use LLM self-prompting to obtain more reliable text comparisons specially for longer outputs. Such an approach however is computationally much more expensive.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Experiments", "weight": 1.0} -->

1: Input: μ ∈ ℳ1(𝒳) any distribution over 𝒳 k ∈ ℕ sample size γ1, γ2 ≥ 0 stabilization parameters (typically selected as 1/k) s: 𝒳 × 𝒳→ a similarity function τ∈ a similarity threshold 2: Independently sample outputs X1, …, Xk ∼ μ ∈ ℳ1(𝒳) 3: Construct a set of indices of unique elements U = {i ∈ [k]: Xi ≠ Xj ∀j < i} 4: Construct cluster centers S ⊂ U according to the similarity function: for all i, t ∈ S, we have s(Xi, Xt) < τ and cluster associated with Xi is D(i) = {j ∈ U: s(Xi, Xj) ≥ τ}. Aggregated probabilities: for all i, t ∈ S, ${{\mu_{1}'{(X_{i})}} = {\sum\limits_{j \in {D{(i)}}}{\mu{(X_{j})}}}},{{\mu_{2}'{(\left.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Experiments", "weight": 1.0} -->

The first three are as follows: *(i)* the probability of the greedy response (denoted by $T0$); *(ii)* the semantic-entropy method of Kuhn et al. whose score is the entropy of $k = 10$ generated samples (denoted by S.E.). To calculate entropy, we first aggregate probabilities of equivalent responses and normalize the probabilities so that they sum to 1 (as described above); and *(iii)* our proposed mutual information score as defined in Section 4 (and denoted by M.I.) with the choices of $k = 10$, $n = 2$, and $\gamma_{1} = \gamma_{2} = 0$ (the latter choice approximates the case that the number of potential responses can be very large in which case the theoretical choice of $\gamma_{1}$ and $\gamma_{2}$ would be very small). To calculate the mutual information, as shown in Algorithm 3, we first generate $k = 10$ random samples.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Experiments", "weight": 1.0} -->

Then for any response $Y$, we calculate the probability of all generated responses given the prompt $F_{1}{(x,Y)}$. We construct estimates $\hat{Q}{(Y)}$ and $\hat{Q}{(\left. Y' \middle| Y \right.)}$ by aggregating probabilities of equivalent responses, and normalizing the probabilities so that they sum to 1.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Experiments", "weight": 1.0} -->

The calculation of the mutual information is slightly different than the algorithms presented in Algorithm 1 and Algorithm 2 and takes advantage of the available log-likelihood function in LLMs. Notice that the input $\mu$ in Algorithm 3 is LLM distribution $Q$ as opposed to being the pseudo joint distribution $\overset{\sim}{Q}$ in Algorithm 1. Another difference is that the similarity function $s$ now takes two texts as input (as opposed to taking two $n$-dimensional arrays of texts as inputs in Algorithm 2). As explained earlier, we use the F1 score as the similarity function and we use $\tau = 0.25$ as the similarity threshold.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Experiments", "weight": 1.0} -->

Each baseline also has a default choice which is taken when the relevant score is above a threshold, and hence the method does not abstain. For $T0$, the default choice is the greedy (temperature zero) response. For S.E., the default choice is the response with the highest (aggregate) probability among the generated random responses. For the M.I. method, the default choice is the sampled response with the highest probability according to the marginalized pseudo joint distribution.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Experiments", "weight": 1.0} -->

We also consider a version of the self-verification method of Kadavath et al. (denoted by S.V.) that, for a query $x$, first finds $Y_{1}$, the element with the largest (aggregated) probability (which is the default choice of S.E. method), and then calculates the probability of token *"True"* (normalized for the two tokens *"True"* and *"False"*) for the following query: *"Consider the following question: Q: $x$. One answer to question Q is $Y_{1}$. Is the above answer to question Q correct? Answer True or False. A:"*. The default choice of this baseline is the same as the default choice of the S.E. method. By this design, our intention is to construct a score that (unlike the first-order scores^99^9The scores $T0$ and S.E. are first order because they only consider the marginal distribution of a single response, unlike our uncertainty score which is based on MI estimation by considering (pseudo) joint distributions over multiple responses.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Experiments", "weight": 1.0} -->

we consider) is not sensitive to the size of the label set.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Experiments", "weight": 1.0} -->

In our experiments we either sweep through all abstention thresholds (Figure 5), or optimize the threshold on some calibration data, as explained in the description of the relevant experiment (Figure 6).

<!-- chunk {"id": "body-0074", "role": "body", "section": "Experiments", "weight": 1.0} -->

Results. We consider the precision-recall (PR) trade-off for the various methods on the different datasets. Here, *recall* is the percentage of queries where the method does not abstain, and *precision* is the percentage of correct decisions among these queries.^1010^10In some figures, for better illustration, we show the *error rate* which is one minus the precision. Figure 5ab show PR-curves for the baselines and the proposed method on TriviaQA and AmbigQA. As can be seen, our method is better than the $T0$ and S.V. baselines, but performs similarly to the S.E. method. This is because the TriviaQA and AmbigQA datasets contain mostly single-label queries, and therefore a first-order method such as S.E. is sufficient to detect hallucinations.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Experiments", "weight": 1.0} -->

The AmbigQA dataset contains a few multi-label queries, but upon closer inspection, we observe that the LLM has low entropy on most of these queries.^1111^11Such a case can also be seen in the query *"Name a city in the UK."* in Figure 3 where the response *"London"* has probability $0.958$. Therefore, a first-order method can perform as well as our method on such queries. Our proposed method, as well as the baselines, make no mistakes on the WordNet dataset (as the prediction of the LLM is always correct), hence we omit those results. The S.V. baseline performs significantly worse than the other methods when the recall is not high (is below about 0.8).

<!-- chunk {"id": "body-0076", "role": "body", "section": "Experiments", "weight": 1.0} -->

The similar performance for the S.E. and M.I. methods shown in Figure 5ab is due to the fact that the LLM has low entropy on most multi-label queries. However, ideally, an LLM should have higher entropy on multi-label queries (which would demonstrate broader knowledge, not focusing on a single possible answer). To include such queries, we mix the TriviaQA and AmbigQA datasets with our WordNet-based dataset with "truely" multi-label queries as constructed above. To enhance the intended effect, we filter our WordNet dataset by keeping only queries with entropy higher than $0.7$ (approximately the entropy of the uniform distribution over two atoms). Then we have $842$ remaining datapoints in WordNet. Note that when considered in isolation, both our proposed method and the semantic entropy method rarely make mistakes on this dataset. Then we create two new datasets by combining our $842$ WordNet datapoints with $842$ randomly selected datapoints from TriviaQA and AmbigQA, respectively, resulting in the TriviaQA+WordNet and AmbigQA+WordNet datasets.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Experiments", "weight": 1.0} -->

Figure 5cd show PR-curves for the S.E. and M.I. methods on these two combined datasets. Apart from low recall values, the performance of the S.E. method degrades noticeably with the addition of extra multi-label data. This precision/recall curve might look somewhat strange (with precision sometimes increasing with recall); this is due to the fact that both methods are always correct on the large number of high-entropy WordNet queries, where the LLM's default predictions are correct.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Experiments", "weight": 1.0} -->

The hardness with the combined datasets is that the predominantly single-label datasets (TriviaQA, AmbigQA) might need a different calibration threshold than the multi-label WordNet dataset, and this is better handled by our proposed method than by S.E. To better illustrate the improved abstention properties of our method, we examine how the two methods handle when the output of the LLM is diverse (i.e., has high entropy). In order to do this, we perform the following experiment: We create a calibration dataset by adding $500$ random datapoints from the WordNet dataset to $500$ random datapoints from TriviaQA, and another such random dataset for test. We determine the abstention thresholds on the calibration dataset for both the S.E. and the M.E. methods,^1212^12This is done by fixing the target loss rates of 0.05 for TriviaQA and 0.15 for AmbigQA, and finding threshold parameters that lead to these rates on the calibration set.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Experiments", "weight": 1.0} -->

and measure the performance (error rate, i.e., 1 minus precision, and recall) of the resulting abstention policies on the test set. We repeat this process $10$ times and report mean values and 95% confidence intervals with Gaussian approximation. We perform a similar evaluation process for mixtures of AmbigQA and WordNet datasets. Figure 6 show that while the S.E. method has similar recall and error rates to those of the proposed method on low-entropy queries, its recall values are much lower for queries with higher entropy, while the M.E. method makes only few mistakes on these queries.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper we considered *epistemic* uncertainty as a proxy for the truthfulness of LLMs. We proposed a mutual-information-based uncertainty estimator that admits a provable lower bound on the epistemic uncertainty of the LLM's response to a query. That we consider joint distributions of multiple answers allows us to disentangle epistemic and aleatoric uncertainty, which makes it possible to better detect hallucination than first order methods, which can only tackle uncertainty as a whole, not epistemic uncertainty alone. This approach yielded an abstention method that performs significantly better on mixed single-label/multi-label datasets than first-order methods. While earlier methods for classification that aim to quantify epistemic uncertainty are usually based on a modified training method using response-tuples, utilizing the sequential nature of LLMs, our method does not need to change the training procedure, but needs to prompt the model iteratively with multiple responses generated by the LLM for the same query.
