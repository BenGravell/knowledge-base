<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Implicit and Explicit Regularization Effects of Dropout

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Dropout is a widely-used regularization technique, often required to obtain state-of-the-art for a number of architectures. This work demonstrates that dropout introduces two distinct but entangled regularization effects: an explicit effect (also studied in prior work) which occurs since dropout modifies the expected training objective, and, perhaps surprisingly, an additional implicit effect from the stochasticity in the dropout training update. This implicit regularization effect is analogous to the effect of stochasticity in small mini-batch stochastic gradient descent. We disentangle these two effects through controlled experiments. We then derive analytic simplifications which characterize each effect in terms of the derivatives of the model and the loss, for deep neural networks. We demonstrate these simplified, analytic regularizers accurately capture the important aspects of dropout, showing they faithfully replace dropout in practice.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Dropout is a commonly used regularization technique for neural nets. In NLP, dropout is the norm on both small and large models, as it is much more effective than methods such as $\ell_{2}$ regularization. In vision, dropout is often used to train extremely large models such as EfficientNet-B7.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

At training time, dropout sets a random subset of activations to zero, perturbing the network output with a remarkable amount of noise. Testing is performed on the full model, and it is somewhat mysterious that dropout works so well despite this difference between train and test. The esoteric nature of dropout has inspired a large body of work studying its regularization effects: Wager et al.; Helmbold & Long; Cavazza et al.; Mianjy et al.; Mianjy & Arora study dropout for linear models, matrix factorization, and linearized networks; Arora et al. study deep networks with dropout only at the last layer. These works primarily study simpler settings than those used in practice, and, as we demonstrate, there is an implicit regularization effect of dropout that is not adressed by prior work.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A large body of recent work has studied implicit, or algorithmic regularization in deep learning, defined to be a regularization effect imposed by the training algorithm, not by the objective (see for example and references therein). One notable example of this is in comparing the generalization performance of SGD vs GD: the implicit regularization effect of stochasticity in SGD has been empirically studied in the context of small v.s. large batch training Keskar et al., where it is observed that noisier small-batch SGD converges to "flatter" local minima which generalize better, whereas large-batch SGD converges "sharper" local minima which generalize more poorly. The starting point of this work is observing that in practice, dropout also introduces an implicit source of regularization because it adds noise to the gradient updates (somewhat analogous to the small v.s. large batch training). Prior studies of dropout only analyze its explicit regularization effect, focusing on how it modifies the expected loss.^11^1Prior work refers to this as the "implicit bias" of dropout.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We refer to this as explicit regularization and reserve the term "implicit" to mean algorithmic regularization effect which does not change the objective. Understanding dropout in practical settings requires studying both regularization effects.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper focuses on a sharp characterization of the regularization effects in dropout, where we: disentangle and analytically characterize the explicit and implicit regularization effects of dropout. derive simplified, analytical, and interpretable regularizers which completely replace dropout for language modeling tasks.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

More concretely, this work makes the following contributions: 1\. This work empirically shows that dropout provides both explicit and implicit regularization effects. Dropout modifies the expected training objective, and it is natural to define the explicit regularizer as the difference between the expected training objective and the standard objective, as follows: Here $F_{\text{drop}}$ denotes the dropout model and drop denotes the randomness from dropout. Moreover, the optimization uses a stochastic approximation of the expected training loss by sampling the dropout noise, which gives rise to an implicit regularization effect.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In practice, the two regularization effects are entangled and easy to conflate. Section 3 provides results of experiments which disentangle these effects.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

2\. We then distill these two regularization effects, providing simpler and more interpretable regularizers that depend on the derivatives of the model and loss (Section 4). Intuitively, dropout regularizes the stability of the model and loss output evaluated on each training datapoint. Theoretically (in Section 4.3), we provide a generalization bound which helps justify the dependencies of these regularizers on the loss derivatives.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

3\. Empirically, detailed experiments are provided in Section 5 showing that these simplified, analytical regularizers can faithfully match and replace dropout for both LSTM and Transformer architectures, on the Penn Treebank, Wikitext-2, and Wikitext-103 datasets. To our knowledge, these are the most accurate empirical demonstrations of theory matching practice with regards to the analysis of dropout.^22^2Our code is available at 4\. Finally, the form of the derived explicit regularizer provides detailed intuition on how to regularize the stability of a deep model. When the number of output classes (i.e. vocabulary in language modeling) is large, dropout regularizes most heavily the stability of predictions corresponding to classes to which the model assigns a prediction probability that is not too certain (i.e., not close to either 0 or 1). Our ablation experiments in Section 5.2 reveal this is critical for the effectiveness of dropout, and our theory in Section 4.3 offers additional justification for this perspective.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

More generally, we hope that the precise methodological derivations that we provide can inform the future study and derivation of data-dependent regularizers in deep learning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Disentangling Explicit and Implicit Regularization in Dropout", "weight": 1.0} -->

We now present an experimental study designed to disentangle the two regularization effects, which confirms the existence of implicit regularization in dropout. Furthermore, this approach allows us to study each effect in isolation.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Disentangling Explicit and Implicit Regularization in Dropout", "weight": 1.0} -->

Let ${L{(F)}} \triangleq {{\mathbb{E}}_{x}{\lbrack{\ell{({F{(x)}})}}\rbrack}}$ denote the population loss without dropout. This is the test criterion regardless of whether dropout is used during training. However, dropout modifies the expected training objective even conditioned on a fixed example $x$. The training loss of an example $x$ averaged over the dropout noise $\eta$ (defined in Section 2) is Consequently, the expected training objective also differs from $L{(F)}$: Figure 2: Confirming implicit regularization effect. Validation perplexity vs. epoch of LSTMs trained with Dropout1, Dropout4, and Dropout4 with noise added via the procedure in Section 3.1. By adding noise to Dropout4, we recover the performance of Dropout1. Thus, the noise we add has an implicit regularization effect. Left: Penn Treebank. Right: WikiText-2.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Disentangling Explicit and Implicit Regularization in Dropout", "weight": 1.0} -->

It is natural to define the explicit regularizer as the difference between the expected training objective (averaged over both $x$ and $\eta$) and the standard objective, i.e.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Disentangling Explicit and Implicit Regularization in Dropout", "weight": 1.0} -->

Due to the fact that in practice, we only have access to a finite training sample (and not the population), it is helpful to define explicit regularizer on a single example as follows: Previous work studies the analytical forms or properties of these regularizers for various models. However, in practice, $\ell_{\text{drop}}{(F,x)}$ (and its gradient ${\nabla_{W}\ell_{\text{drop}}}{(F,x)}$) are only stochastically estimated by sampling a single $\eta$ and computing $\ell{({F{(x,\eta)}})}$ (and ${\nabla_{W}\ell}{({F{(x,\eta)}})}$ respectively). For example, SGD (with mini-batch size $1$), performs the update: where $\gamma$ is the stepsize, $x$ is a randomly sampled datapoint, and $\eta$ is a randomly sampled dropout noise variable.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Disentangling Explicit and Implicit Regularization in Dropout", "weight": 1.0} -->

We demonstrate that the stochasticity from sampling $\eta$ provides an implicit regularization effect which contributes to the test-time effectiveness of dropout.^33^3There is also an implicit regularization effect from sampling the SGD minibatch. As the minibatch size is fixed in our experiments, this is distinct from the implicit regularization effect of dropout demonstrated in Figure 1, and studying it is orthogonal to our work. Our strategy for disentangling the regularization effects is simple: we remove noise from the gradient estimate by optimizing a more accurate estimate of $\ell_{\text{drop}}{(F,x)}$ than $\ell{({F{(x,\eta)}})}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Disentangling Explicit and Implicit Regularization in Dropout", "weight": 1.0} -->

Formally, we can perform "mini-batch" dropout by averaging the loss over $k$ samples of the noise ${\{\eta_{i}\}}_{i = 1}^{k}$: For training, we now use the stochastic gradient $\nabla_{W}{\hat{\ell}}_{\text{drop},k}$, reducing the gradient covariance by a factor of $k$. We refer to the mini-batched dropout update by $\text{Dropout}_{k}$ as shorthand and formally describe it in Algorithm 1.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Disentangling Explicit and Implicit Regularization in Dropout", "weight": 1.0} -->

If there were no implicit regularization from the stochasticity of dropout, then we would expect $\text{Dropout}_{k}$ to have similar test performance to $\text{Dropout}_{1}$, which is equivalent to standard dropout. In Figure 1, we plot the validation accuracy vs. training steps for models trained using $\text{Dropout}_{k}$ for various values of $k$. Figure 1 shows that, perhaps surprisingly, performance degrades quite sharply for larger choices of $k$. However, the explicit regularizer is still helpful, as $\text{Dropout}_{32}$ does not overfit as severely as the model trained without dropout (for Penn Treebank, the best perplexity without dropout is around 120, which is outside the bounds of the graph). $\text{Dropout}_{k}$ and $\text{Dropout}_{1}$ optimize the same expected objective, so the change in algorithm must be the cause of these performance discrepancies.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Injecting Dropout Noise Fixes $\\text{Dropout}_{k}$", "weight": 1.0} -->

Our proposed explanation for Figure 1 is that the gradient noise induced by dropout provides an implicit regularization effect. We verify this constructively by adding noise to the $\text{Dropout}_{k}$ updates in order to recover the performance of standard dropout. Let $\xi_{\text{drop}}$ denote the fluctuation of the stochastic dropout gradient around its mean: Note that $\xi_{\text{drop}}$ is exactly the gradient noise in standard dropout. Furthermore, we have ${\text{Cov}{({\nabla_{W}{\hat{\ell}}_{\text{drop},k}})}} = {\frac{1}{k}\text{Cov}{(\xi_{\text{drop}})}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Injecting Dropout Noise Fixes $\\text{Dropout}_{k}$", "weight": 1.0} -->

In Figure 2, we verify that this correction procedure recovers the test performance of $\text{Dropout}_{1}$. Thus, we have constructed a (complicated) implicit regularizer which explains the discrepancy between $\text{Dropout}_{k}$ and $\text{Dropout}_{1}$. In Section 4.2, we will explore its simplifications.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Characterizing the Dropout Regularizers", "weight": 1.0} -->

Having disentangled the explicit and implicit regularization effects of dropout, we will now study them separately. In this section, we adapt the analysis tools of to study both regularization effects for neural networks. We derive analytic simplifications for both regularizers in terms of the model and loss derivatives. At a high level, our derivations show that dropout regularizes the data-dependent stability of the model and loss on the training examples. This demonstrates a key difference between dropout and $\ell_{2}$ regularization, which is agnostic to the data.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Characterizing the Dropout Regularizers", "weight": 1.0} -->

In Section 4.1, we present and derive our explicit regularizer. In Section 4.2, we derive an update noise distribution which captures the implicit regularization effect in dropout. In Section 4.3, we prove a generalization bound for the cross-entropy loss which further justifies our stability-based regularizers. In Section 5, we empirically demonstrate that our derivations accurately capture the regularization effects in dropout -- we can match the performance of dropout for language modeling tasks by using only our regularizers.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Characterizing the Explicit Regularizer", "weight": 1.0} -->

Single-layer Dropout. For simplicity, we start by considering node dropout applied to a single layer $i$ of the network. For the rest of the paper, we use $h_{i}$ to denote the $i$-th hidden layer of the network and let $F_{i}$ denote the composition of the layers after $h_{i}$, that is, the function that takes in $h_{i}$ as input, and outputs the model prediction. (Thus, ${F_{i}{(h_{i})}} = {F{(x)}}$).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Characterizing the Explicit Regularizer", "weight": 1.0} -->

We rewrite the loss after applying dropout on $h_{i}$ by ${\ell{({F{(x,\eta)}})}} = {\ell{({F_{i}{({{h_{i}{(x)}} + \delta})}})}}$, where $\delta \triangleq {{\eta_{i} \odot h_{i}}{(x)}}$ is the perturbation to the $i$-th layer. We can apply Taylor expansion to analyze the effect of this perturbation.^44^4Taylor expansion typically requires a small level of perturbation, which may not hold if the dropout probability is large. In Section A.2, we argue that performing Taylor expansion around the next layer could remedy this issue. As it does not change the final result, we omit this analysis here.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Characterizing the Explicit Regularizer", "weight": 1.0} -->

We apply Taylor expansion around $\delta = \overset{\rightarrow}{0}$: This provides an approximate version of the dropout explicit regularizer $R_{\text{drop}}$: Here the expectation over the linear term in (4.1) vanished because $\delta = {{\eta_{i} \odot h_{i}}{(x)}}$ is a mean-zero vector. Next we take expectation over $\delta$: where $q$ is the dropout probability and we used the fact that ${{\mathbb{E}}{\lbrack{\delta\delta^{\top}}\rbrack}} = {\frac{q}{q - 1}\text{diag}{({h_{i}{(x)}^{\odot 2}})}}$ because $\delta = {{\eta_{i} \odot h_{i}}{(x)}}$ and the coordinates of $\eta_{i}$ are independent.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Characterizing the Explicit Regularizer", "weight": 1.0} -->

We obtain an analytical approximation for the explicit regularizer $R_{\text{drop}}{(F,x)}$ by combining the equations above. Next we will rewrite the RHS of (4.2) in a more interpretable form by further dropping some terms.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Characterizing the Explicit Regularizer", "weight": 1.0} -->

For notational simplicity, let $J_{F,i}{(x)}$ be the Jacobians of the network output with respect to the hidden layers, and $H_{\text{out}}{(x)}$ be the Hessian of the loss with respect to the network outputs: We claim that $R_{\text{drop}}{(F,x)}$ (or the RHS of (4.2)) can be replaced by the following analytical form Readers may find this reminiscent of the decomposition of the Hessian of neural nets loss LeCun et al.; Sagun et al.. Indeed, we decompose $D_{{\mathbf{h}}_{\mathbf{i}}}^{2}{({\ell \circ F_{i}})}{\lbrack h_{i}\rbrack}$ into two terms, and drop the non-PSD term that depends on the Hessian of the model (which is less suitable as a regularizer and has been argued to be less important empirically Sagun et al.).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Characterizing the Explicit Regularizer", "weight": 1.0} -->

A full derivation and justification is given in Section A.1 ‣ Appendix A Full Derivations in Section 4 ‣ The Implicit and Explicit Regularization Effects of Dropout").

<!-- chunk {"id": "body-0030", "role": "body", "section": "Characterizing the Explicit Regularizer", "weight": 1.0} -->

Multi-layer Dropout. To deal with dropout on all layers, we simply take Taylor expansion with all the $\delta$'s at every layer. Cross terms cancel because the masks of different layers are independent, and the resulting regularizer is a sum of equation (4.3) over $i$, giving our analytical explicit regularizer: Interpretation. Our regularizer ensures that the Jacobians and hidden layers of the model output are small when measured in the norm of $H_{\text{out}}$. We note that for cross entropy loss, ${H_{\text{out}}{(x)}} = {{\text{diag}{(p)}} - {pp^{\top}}} \succcurlyeq 0$, where $p$ is the probability vector predicted by the model encoding the distribution over output class labels. As the diagonal entries take the form $p_{k}{({1 - p_{k}})}$, this Hessian places stronger emphasis on output classes which the model believes are plausible but not certain.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Characterizing the Explicit Regularizer", "weight": 1.0} -->

Our experiments in Section 5.2 demonstrate that this particular weighting is an important factor for the success of dropout -- alternative ways to weight the stability of each output class in the regularizer do not perform as well.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Characterizing the Explicit Regularizer", "weight": 1.0} -->

Keskar et al.; Yao et al.; Jastrzebski et al. study the relationship between SGD batch size and notions of "flatness" of local minima via metrics related to the magnitudes of the eigenvalues of the second derivative of the loss with respect to the model parameters. They observe that flatter local minima tend to correlate with better generalization. Our regularizer encourages a notion of flatness that depends on the second derivative of the loss with respect to the hidden layers (see (4.2) in our derivation). These quantities are closely related. For example, consider weight matrix $Z$ parametrizing some linear transformation layer, such that ${F{(x)}} = {F'{({Zh{(x)}})}}$, where $h$, $F'$ denote the compositions of the layers before and after the application of $Z$. Then defining ${h'{(x)}} = {Zh{(x)}}$, we have Thus, the loss derivatives with respect to model parameters can be expressed in terms of those with respect to the hidden layers.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Characterizing the Explicit Regularizer", "weight": 1.0} -->

We emphasize that one benefit of $R_{\text{approx}}{(F,x)}$ is that it provides an interpretable and detailed characterization of the explicit regularization effect of dropout. We hope this can help provide theoreticians and practictioners alike with precise intuitions on why dropout works, and, more broadly, how to design effective stability regularizers in practice.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Characterizing the Implicit Regularization Effect", "weight": 1.0} -->

In this section, we derive a gradient noise distribution which can replace the mean-zero gradient noise in dropout, $\xi_{\text{drop}}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Characterizing the Implicit Regularization Effect", "weight": 1.0} -->

Single Layer Dropout. As before, we start by considering the single-layer case. Instead of directly approximating $\xi_{\text{drop}}$, which involves the intractable term ${\nabla_{W}\ell_{\text{drop}}}{(F,x)}$, we aim to approximate the noise ${\overset{\sim}{\xi}}_{\text{drop}}$ defined in Section 3.1 which we showed to be able to replace $\xi_{\text{drop}}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Characterizing the Implicit Regularization Effect", "weight": 1.0} -->

We apply Taylor expansion to approximate ${\overset{\sim}{\xi}}_{\text{drop}}$, only keeping the mean-zero linear terms. Letting $\delta_{1} = {{\eta_{i}^{} \odot h_{i}}{(x)}}$ and $\delta_{2} = {{\eta_{i}^{} \odot h_{i}}{(x)}}$ denote two different perturbations to the $i$-th layer, we have^55^5As the subscript has been used to index the layer, we use the superscript to index the different dropout noise samples.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Characterizing the Implicit Regularization Effect", "weight": 1.0} -->

where $J_{\text{loss},i}{(x)}$ denotes the Jacobian of the loss with respect to the hidden layers: ${{J_{\text{loss},i}{(x)}} \triangleq {D_{{\mathbf{h}}_{\mathbf{i}}}{({\ell \circ F_{i}})}{\lbrack{h_{i}{(x)}}\rbrack}}}.$ Now we can replace the difference $\eta_{i}^{} - \eta_{i}^{}$ by $\eta_{i}\sqrt{2}$, as the covariance is unchanged. After adjusting the scaling to match the covariance of $\xi_{\text{drop}}$, we obtain the following analytic form for update noise: Multi-layer Dropout.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Characterizing the Implicit Regularization Effect", "weight": 1.0} -->

To handle multi-layer dropout, we Taylor expand over all the layers, obtaining a sum of (4.5) over the layers:^66^6To make tuning slightly simpler, we compute the noise by sampling the coordinates of $\eta_{i}$ uniformly from $\{{- 1},{+ 1}\}$ and scaling by $\sqrt{\frac{q}{q - 1}}$, as this preserves the covariance.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Characterizing the Implicit Regularization Effect", "weight": 1.0} -->

To replace the implicit effect of dropout, we add the mean-zero noise $\xi_{\text{approx}}$ to the gradients of the objective.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Characterizing the Implicit Regularization Effect", "weight": 1.0} -->

Interpretation: It is a major open question in deep learning theory to understand the regularization effects of noise. For example, it is even unclear why mini-batch noise in SGD empirically helps in general. Prior works have (heuristically) suggested that the noise encourages the algorithm to find a solution that minimizes the trace of the covariance of the noise. As the covariance of $\xi_{\text{approx}}$ is some function of ${\{ J_{\text{loss},i}\}},{\{ h_{i}\}}$, and their gradients with respect to $W$, the induced regularizer controls some data-dependent stability of the model. Note the conceptual difference with the explicit regularizer, which multiplies the model Jacobian with the loss Hessian, whereas $\xi_{\text{approx}}$ multiplies the model Jacobian with the loss Jacobian. More precise interpretations are left for future work.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Characterizing the Implicit Regularization Effect", "weight": 1.0} -->

In Section 5, we demonstrate that a combination of our explicit and implicit regularizer can successfully replace dropout. The general update rule which applies these regularizers in lieu of dropout is described in Algorithm 2.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Theoretical Support for Stability-based Regularization", "weight": 1.0} -->

Recent works support our stability-based regularization by bounding generalization of the model in terms of its Jacobian norms on the training data. These bounds align with the Jacobian terms in the regularization (4.4). However, they miss a crucial aspect of the regularizers derived in Section 4.1 as they only consider derivatives of the model output, ignoring the loss derivatives (the $H_{\text{out}}{(x)}$ term in equation (4.4)). Though this is a subtle distinction, in Section 5.2 we demonstrate that the loss derivatives are necessary on language modeling tasks.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Theoretical Support for Stability-based Regularization", "weight": 1.0} -->

In this section, we prove a new generalization bound for cross entropy loss on linear models. Our bound helps further justify the forms of our regularizers in (4.4) and (4.6), as every term in our bound is scaled by a derivative of the loss.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Theoretical Support for Stability-based Regularization", "weight": 1.0} -->

Let $\ell_{y}^{\text{ce}}$ denote the standard cross-entropy loss on $c$ classes with true label $y$. For linear models parameterized by weight matrix $W$, we compute the loss by Let $\overline{\ell^{\text{ce}}} = {\min{\{ B,\ell^{\text{ce}}\}}}$ denote the truncation of the cross-entropy loss to some fixed bound $B > 0$. For matrix $M$, define the following $\parallel \cdot \parallel_{2,1}$-norm of $M$: ${\| M\|}_{2,1} \triangleq {\sum_{j}\sqrt{\sum_{i}{(M_{ij}^{2})}}}$. Let $P$ denote the population data distribution and $P_{n}$ the distribution over training samples.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we empirically confirm that our derivations in Section 4 provide accurate characterizations of dropout. Our focus is on language modeling tasks using the LSTM and Transformer architectures.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Our Derived Regularizers can Replace Dropout", "weight": 1.0} -->

In this section, we show that the regularizers derived in Section 4 can replace dropout for LSTMs on language modeling tasks. We work with Penn Treebank, a corpus of 887,521 tokens and Wikitext-2, a corpus of 2,088,628 tokens. In Section 5.3, we study whether our findings can also scale to larger datasets and architectures such as Transformer-XL.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Our Derived Regularizers can Replace Dropout", "weight": 1.0} -->

For the experiments in this section, we base our model and code on Merity et al.. For the dropout-trained models, we use node dropout on the output, hidden, and embedding layers as well as DropConnect on the weight matricess. We fix the dropout probability to $q = 0.4$ for these experiments. To compute the update gradients for our regularizers, we follow the general rule described in Algorithm 2. We specify additional hyperparameters in Section D.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Our Derived Regularizers can Replace Dropout", "weight": 1.0} -->

We study three settings described in detail below: our explicit regularizer $R_{\text{approx}}$ only, adding our noise $\xi_{\text{approx}}$ to $\text{Dropout}_{k}$ updates, and combining our explicit and implicit regularizers. Tables 3 and Tables 4 in Section D summarize the experimental results on our regularizers for the Penn Treebank and Wikitext-2 datasets. We obtain our results without tuning, as we use the regularization coefficient suggested in Section 4 to match the dropout strength. The Jacobian optimization required for the analytical regularizers results in around 3x runtime slowdown compared to dropout, though we note that the analytical regularizers appear to optimize in fewer iterations (see Figure 5).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Our Derived Regularizers can Replace Dropout", "weight": 1.0} -->

Replacing Dropout Explicit Regularization. In Figure 3, we compare our explicit regularizer (4.4) to mini-batch dropout, $\text{Dropout}_{k}$, with $k = {1,32}$. For $k = 32$, the implicit regularization effect of dropout is heavily reduced, bringing the training procedure closer to training on $\ell_{\text{drop}}$ exactly. Our explicit regularizer outperforms $\text{Dropout}_{32}$, confirming that it matches the explicit regularization effect of dropout. It does not match the performance of $\text{Dropout}_{1}$ because it is missing the implicit regularization effect.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Our Derived Regularizers can Replace Dropout", "weight": 1.0} -->

Replacing Dropout Implicit Regularization. We demonstrate that the our update noise derived in (4.6) can effectively replicate the implicit regularization effect of dropout. We inject appropriately scaled $\xi_{\text{approx}}$ noise into the $\text{Dropout}_{k}$ training procedure. As the covariance of $\nabla_{W}{\hat{\ell}}_{\text{drop},k}$ scales with $\frac{1}{k}$, we scale $\xi_{\text{approx}}$ by a factor $\sqrt{1 - \frac{1}{k}}$. Thus, if $\xi_{\text{approx}}$ and $\xi_{\text{drop}}$ had the same covariance, the covariance of the updates would remain constant across $k$. Algorithm 4 in Section C formally describes this procedure.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Our Derived Regularizers can Replace Dropout", "weight": 1.0} -->

In Figure 4, we demonstrate that this procedure can closely track the performance of $\text{Dropout}_{1}$ for various values of $k$, affirming that $\xi_{\text{approx}}$ captures essential properties of $\xi_{\text{drop}}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Our Derived Regularizers can Replace Dropout", "weight": 1.0} -->

Completely Replacing Dropout. We demonstrate that the combination of our regularizers can completely replace dropout. We apply algorithm 2, setting $R = R_{\text{approx}}$ and $\xi = \xi_{\text{approx}}$. In Figure 5, we plot the validation perplexity vs. time of a model trained with our regularization vs. $\text{Dropout}_{1}$. Figure 5 demonstrates that our regularization is enough to replace dropout, confirming the validity of our derivations. We note that our regularizer appears to require fewer iterations to decrease the validation perplexity. This raises the exciting possibility of designing more efficient regularizers than dropout, which we leave for future work.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Regularizing the Loss Hessian is Necessary", "weight": 1.0} -->

We argue that simply regularizing the stability of the model outputs is not sufficient. As argued in Section 4.1, our derivations show that dropout enforces stronger stability for output coordinates where the model assigns non-trivial probability mass but is not extremely confident. To demonstrate this is helpful, we experiment with replacing $H_{\text{out}}$ in our explicit regularizer (see (4.4)) with two alternative quantities.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Regularizing the Loss Hessian is Necessary", "weight": 1.0} -->

Identity Cannot Replace Loss Hessian. For the first variant, we use an identity matrix instead of the loss Hessian (so the regularizer weights each output coordinate equally). We provide implementation details in Section C. On Penn Treebank, this was ineffective: after thoroughly tuning the regularization strength, the best validation accuracy we obtained was 108.76, which is comparable to the performance of $\ell_{2}$ regularization and much worse than dropout.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Regularizing the Loss Hessian is Necessary", "weight": 1.0} -->

Using the Loss Jacobian Instead of Hessian. For cross entropy loss, in the case where the model predicts the true label very confidently, the loss Hessian $H_{\text{out}}{(x)}$ approaches the outer product of the loss Jacobian with itself: ${H_{\text{out}}{(x)}} \approx {D_{\mathbf{F}}\ell^{\text{ce}}{\lbrack{F{(x)}}\rbrack}^{\top}D_{\mathbf{F}}\ell^{\text{ce}}{\lbrack{F{(x)}}\rbrack}}$ (see Section C.1). Substituting this approximation into our explicit regularizer gives the following alternative regularizer: On Penn Treebank, we find that this regularizer is much more effective than $\ell_{2}$ regularization but cannot match dropout.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Regularizing the Loss Hessian is Necessary", "weight": 1.0} -->

We test whether ${\overset{\sim}{R}}_{\text{approx}}$ performs well as $R_{\text{approx}}$ with or without implicit regularization. In both cases, we tune the explicit regularization strength. Table 1 summarizes the results compared to the Hessian-based regularizer. ${\overset{\sim}{R}}_{\text{approx}}$ on its own significantly outperforms $\ell_{2}$ regularization and can match $R_{\text{approx}}$ after tuning. However, with update noise it does not match dropout or $R_{\text{approx}}$ (even after tuning).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Regularizing the Loss Hessian is Necessary", "weight": 1.0} -->

Best Val. Ppl. ${\overset{\sim}{R}}_{\text{approx}}$ (tuned) ${\overset{\sim}{R}}_{\text{approx}}$ (tuned) and ξapprox Rapprox and ξapprox (4.5) Table 1: Regularization effect of ${\overset{\sim}{R}}_{\text{approx}}$ (see (5.1)) on Penn Treebank with and without implicit regularization. ${\overset{\sim}{R}}_{\text{approx}}$ can significantly outperform ℓ2 regularization but does not match dropout even with implicit regularization, whereas Rapprox can.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Additional Settings", "weight": 1.0} -->

We test how well our findings translate to larger datasets and different architectures. We use the Wikitext-103 dataset, which contains 103,227,021 tokens, and the Transformer-XL and QRNN architectures. First, we explore whether the implicit regularization effect of dropout is as important on larger datasets. We train the Transformer-XL and QRNN architectures on the Wikitext-103 corpus using $\text{Dropout}_{k}$ for $k = {1,2,4}$. Table 2 shows that for Transformer-XL trained on the full dataset, the implicit regularization effect disappears. We observe the same for QRNN (see Section D).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Additional Settings", "weight": 1.0} -->

In Table 2, we also demonstrate that there is an implicit regularization effect when we downsample Wikitext-103 by a factor of 5, though it is not as crucial. Thus, the importance of the implicit regularization depends on the dataset size.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Additional Settings", "weight": 1.0} -->

Finally, we confirm that our explicit regularizer is effective on a larger dataset. For Wikitext-103 and Transformer-XL, Table 2 shows that our explicit regularizer achieves validation perplexity of 24.12, within $0.7$ of dropout.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we show that dropout actually introduces two entangled sources of regularization: an explicit one which modifies the expected objective, and an implicit one due to stochasticity in the updates. We empirically disentangle these regularizers and derive analytic simplifications which faithfully distill each regularization effect. We demonstrate that our simplified regularizers can replace dropout in practice. Our derivations show that dropout regularizes the stability of the model and loss around the training data.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

More broadly, our analytic characterizations of dropout can provide intuition on what works and what doesn't for stability-based regularizers in deep learning. We hope that these intuitions can help inform and motivate the design of more principled regularizers for deep networks.
