<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Role of Optimization in Double Descent: A Least Squares Study

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Empirically it has been observed that the performance of deep neural networks steadily improves as we increase model size, contradicting the classical view on overfitting and generalization. Recently, the double descent phenomena has been proposed to reconcile this observation with theory, suggesting that the test error has a second descent when the model becomes sufficiently overparameterized, as the model size itself acts as an implicit regularizer. In this paper we add to the growing body of work in this space, providing a careful study of learning dynamics as a function of model size for the least squares scenario. We show an excess risk bound for the gradient descent solution of the least squares objective. The bound depends on the smallest non-zero eigenvalue of the covariance matrix of the input features, via a functional form that has the double descent behavior. This gives a new perspective on the double descent curves reported in the literature. Our analysis of the excess risk allows to decouple the effect of optimization and generalization error. In particular, we find that in case of noiseless regression, double descent is explained solely by optimization-related quantities, which was missed in studies focusing on the Moore-Penrose pseudoinverse solution.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We believe that our derivation provides an alternative view compared to existing work, shedding some light on a possible cause of this phenomena, at least in the considered least squares setting. We empirically explore if our predictions hold for neural networks, in particular whether the covariance of intermediary hidden activations has a similar behavior as the one predicted by our derivations.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep Neural Networks have shown amazing versatility across a large range of domains. Among one of their main features is their ability to perform better with scale. Indeed, some of the most impressive results \see e.g. Brock et al., [2021; Brown et al., 2020; Senior et al., 2020; Schrittwieser et al., 2020; Silver et al., 2017; He et al., 2016 and references therein\] have been obtained often by exploiting this fact, leading to models that have at least as many parameters as the number of examples in the dataset they are trained. Empirically, the limitation on the model size seems to be mostly imposed by hardware or compute. From a theoretical point of view, however, this property is quite surprising and counter-intuitive, as one would expect that in such extremely overparametrized regimes the learning would be prone to overfitting.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently Belkin et al. proposed Double Descent (DD) phenomena as an explanation. They argue that the classical view of overfitting does not apply in extremely over-parameterized regimes, which were less studied prior to the emergence of the deep learning era. The classical view in the parametric learning models was based on error curves showing that the training error decreases monotonically when plotted against model size, while the corresponding test errors displayed a U-shape curve, where the model size for the bottom of the U-shape was taken to achieve the ideal trade-off between model size and generalization, and larger model sizes than that were thought to lead to 'overfitting' since the gap between test errors and training errors increased.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The classical U-shape error curve dwells in what is now called the under-parameterized regime, where the model size is smaller than the size of the dataset. Arguably, the restricted model sizes used in the past were tied to the available computing power. By contrast, it is common nowadays for model sizes to be larger than the amount of available data, which we call the over-parameterized regime. The divide between these two regimes is marked by a point where model size matches dataset size, which Belkin et al. called the *interpolation threshold*.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The work of Belkin et al. argues that as model size grows beyond the interpolation threshold, one will observe a second descent of the test error that asymptotes in the limit to smaller values than those in the underparameterized regime, which indicates better generalization rather than overfitting. To some extent this was already known in the *nonparametric* learning where model complexity scales with the amount of data by design (such as in nearest neighbor rules and kernels), yet one can generalize well and even achieve statistical consistency. This has lead to a growing body of works trying to identify the mechanisms behind DD, to which the current manuscript belongs too. We refer the reader to Section 2, where the related literature is discussed. Similar to these works, our goal is also to understand the cause of DD. Our approach is slightly different: we explore the least squares problem that allows us to work with analytic expressions for all the quantities involved. Fig. 1 provides a summary of our findings.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, it shows the behaviour of the excess risk in a setting with random inputs and noise-free labels, for which in Section 3 we prove a bound that has the form ${{{\mathbb{E}}\left\lbrack {({1 - {\alpha{\hat{\lambda}}_{\min}^{+}}})}^{2T} \right\rbrack}{\|{\mathbf{w}}^{\star}\|}^{2}} + \frac{{\|{\mathbf{w}}^{\star}\|}^{2}}{\sqrt{n}}$, for a rapidly decaying spectrum of the sample covariance. In this setting, the linear predictors project $d$-dimensional features by dot product with a weight vector which must be learned from data; then ${\mathbf{w}}^{\star}$ refers to the optimal solution, $\alpha$ is a constant learning rate, and $n$ is the number of examples in the training set.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Note that the feature dimension $d$ coincides with the number of parameters in this particular setting, hence $d > n$ is the overparameterized regime. The quantity ${\hat{\lambda}}_{\min}^{+}$ is of special importance: *It is the smallest positive eigenvalue of the sample covariance matrix of the features.* In particular, we observe that the excess risk is controlled by the smallest non-zero eigenvalue of the covariance of the features, and its functional dependence exhibits a profile similar to the DD curve. This offers a new perspective on the problem.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Fig. 1 we observe *a peaking behavior*, not only in the excess risk, but also in the quantity that we label 'optimization error' which is a special term of the excess risk bound that is purely related to optimization. The peaking behaviour of the excess risk (MSE in case of the square loss) was observed and studied in a number of settings; however, the connection between the peaking behavior and optimization so far received less attention. This pinpoints a less-studied setting and we conjecture that the DD phenomenon occurs due to ${\hat{\lambda}}_{\min}^{+}$. In the absence of label noise, we conclude that DD manifests due to the optimization process. On the other hand, when label noise is present, in addition to the optimization effect, ${\hat{\lambda}}_{\min}^{+}$ also has an effect on the generalization error.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Our main theoretical contribution is provided in Section 3. In particular, Section 3.1 focuses on the noise-free least squares problem, Section 3.2 adds noise to the problem, and Section 3.3 deals with concentration of the sample-dependent ${\hat{\lambda}}_{\min}^{+}$ around its population counterpart. Sections 4 and 5 provide an in-depth discussion on the implications of our findings and an empirical exploration of the question whether simple neural networks have a similar behaviour.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Excess Risk of the Gradient Descent Solution", "weight": 1.0} -->

We focus on learners that optimize parameters via the Gradient Descent algorithm. We treat GD as a measurable map $\mathcal{A}:{{\mathcal{S} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}^{d}}$, where $\mathcal{S} = \mathcal{Z}^{n}$ is the space of size-$n$ training sets.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Excess Risk of the Gradient Descent Solution", "weight": 1.0} -->

We look at the behavior of GD in the *overparameterized* regime ($d > n$) when the initialization parameters are sampled from an isotropic Gaussian density, that is ${\mathbf{W}}_{0} \sim {\mathcal{N}{(\mathbf{0},{\nu_{init}^{2}{\mathbf{I}}_{d \times d}})}}$ with some initialization variance $\nu_{init}^{2}$. It is well-known that in the overparameterized regime, GD is able to achieve zero empirical loss.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Least-Squares with Random Design and No Label Noise", "weight": 1.0} -->

where instances $\mathbf{X}$ are distributed according to some unknown distribution $P_{X}$ supported on a $d$-dimensional unit Euclidean ball. After observing a training sample $S = \left( {({\mathbf{X}}_{i},Y_{i})} \right)_{i = 1}^{n}$, we run GD on the given empirical square loss

<!-- chunk {"id": "body-0015", "role": "body", "section": "Concentration of the Smallest Non-zero Eigenvalue", "weight": 1.0} -->

In this section we take a look at the behaviour of ${\hat{\lambda}}_{\min}^{+}$ assuming that input instances ${\mathbf{X}}_{1},\ldots,{\mathbf{X}}_{n}$ are i.i.d. *random* vectors, sampled from some underlying marginal density that meets some regularity requirements (Definitions 2. ‣ 3.3 Concentration of the Smallest Non-zero Eigenvalue ‣ 3 Excess Risk of the Gradient Descent Solution ‣ On the Role of Optimization in Double Descent: A Least Squares Study") and 3. ‣ 3.3 Concentration of the Smallest Non-zero Eigenvalue ‣ 3 Excess Risk of the Gradient Descent Solution ‣ On the Role of Optimization in Double Descent: A Least Squares Study") below) so that we may use the results from random matrix theory.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Concentration of the Smallest Non-zero Eigenvalue", "weight": 1.0} -->

In particular, the Bai-Yin limit characterization of the extreme eigenvalues of sample covariance matrices implies that ${\hat{\lambda}}_{\min}^{+}$ has almost surely an asymptotic behavior ${({1 - \sqrt{d/n}})}^{2}$ as the dimensions grow to infinity, assuming that the matrix ${\mathbf{X}}:={\lbrack{\mathbf{X}}_{1},\ldots,{\mathbf{X}}_{n}\rbrack} \in {\mathbb{R}}^{d \times n}$ has independent entries. We are interested in the non-asymptotic version of this result. However, unlike Bai and Yin, we do not assume independence of all entries, but rather independence of observation vectors (columns of $\mathbf{X}$). This will be done by introducing a distributional assumption: we assume that observations are *sub-Gaussian* and *isotropic* random vectors.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Excess risk as a function of over-parameterization", "weight": 1.0} -->

First we note that, in the noise-free case, the middle term in the upper bound of Theorem 1. ‣ 3 Excess Risk of the Gradient Descent Solution ‣ On the Role of Optimization in Double Descent: A Least Squares Study") vanishes: ${{\mathbb{E}}{\lbrack{\|{{\mathcal{A}_{S}{({\mathbf{w}}^{\star})}} - {\mathbf{w}}^{\star}}\|}_{\hat{\mathbf{M}}}^{2}\rbrack}} = 0$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Excess risk as a function of over-parameterization", "weight": 1.0} -->

Thus, as in Theorem 2, the upper bound consists only of the term involving the smallest positive eigenvalue ${\hat{\lambda}}_{\min}^{+}$ and the term involving ${\mathbb{E}}{\lbrack{\|{\mathbf{w}}^{\star}\|}_{{\mathbf{I}} - \hat{\mathbf{M}}}^{2}\rbrack}$. The behaviour of the former was clarified in Section 3.3, and the latter is controlled as explained in Appendix E ‣ On the Role of Optimization in Double Descent: A Least Squares Study"). Thus, in the *overparametrized* regime ($d > n$) we have: ^22^2We use $f \lesssim g$ when there exists a universal constant $C > 0$ such that $f \leq {Cg}$ uniformly over all arguments.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Excess risk as a function of over-parameterization", "weight": 1.0} -->

It is interesting to see how $\left( {1 - {\alpha{({\sqrt{d/n} - 1})}_{+}^{2}}} \right)^{2T}$ varies with model size $d$ for a given fixed dataset size $n$ and fixed number of gradient updates $T$. Setting $y = {d/n}$ and considering the cases $y\rightarrow 0$ (underparameterized regime), $y \sim 1$ (the peak), and $y > 1$ (overparameterized regime) it becomes evident that this term has a double descent behaviour. Thus, the double descent is captured in the part of the excess risk bound that corresponds to learning dynamics on the space spanned by $\hat{\mathbf{M}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Excess risk as a function of over-parameterization", "weight": 1.0} -->

Similarly, we can now consider the scenario with label noise: we can similarly bound the excess risk, following the same logic as for noise-free case; however we have an additional dependence on $\sigma^{2}$ via the term $\frac{4\sigma^{2}}{n}{{\mathbb{E}}\left\lbrack \left( {\hat{\lambda}}_{\min}^{+} \right)^{- 2} \right\rbrack}$. While this does not interfere with the DD shape as we change model size, it does imply that the peak is dependent on the amount of noise. In particular, the more noise we have in the learning problem the larger we expect the peak at the interpolation boundary to be.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Excess risk as a function of over-parameterization", "weight": 1.0} -->

While the presence of the double descent has been studied by several works, our derivation provides two potentially new interesting insights. The first one is that there is a dependency between the noise in the learning problem and the shape of the curve, the larger the noise is, the larger the peak in DD curve. This agrees with the typical intuition in the underparmetrized regime that the model fits the noise when it has enough capacity, leading towards a spike in test error. However, due to the dependence on ${\hat{\lambda}}_{\min}^{+}$, it is subdued as the model size grows. Secondly, and maybe considerably more interesting, there seems to be a connection between the double descent curve of the excess risk and the optimization process. In particular, our derivation is specific to gradient descent. In this case the excess risk seems to depend on the conditioning of the features in the least squares problem on the subspace spanned by the data through ${\hat{\lambda}}_{\min}^{+}$, which also affects convergence of the optimization process.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Excess risk as a function of over-parameterization", "weight": 1.0} -->

For the least squares problem this can easily be seen, as the sample covariance of the features corresponds to the Gauss-Newton approximation of the Hessian, hence it impacts the convergence. In a more precise way, conditioning of any matrix is measured by the ratio $s_{\max}/s_{\min}$ (the 'condition number') which is determined solely by the smallest singular value $s_{\min}$ in cases when $s_{\max}$ is of constant order, such as the case that we studied here: Note that by our boundedness assumption, $s_{\max}$ is constant, but in general one needs to consider both $s_{\max}$ and $s_{\min}$ in order to characterize the condition numbers, which interestingly have been observed to display a double descent as well Poggio et al..

<!-- chunk {"id": "body-0023", "role": "body", "section": "Excess risk as a function of over-parameterization", "weight": 1.0} -->

More generally, normalization, standardization, whitening and various other preprocessing of the input data have been a default step in many computer vision systems where it has been shown empirically that they greatly affect learning. Such preprocessing techniques are usually aimed to improve conditioning of the data. Furthermore, various normalization layers like batch-norm or layer-norm are typical components of recent architectures, ensuring that features of intermediary layers are well conditioned. Furthermore, it has been suggested that model size improves conditioning of the learning problem, which is in line with our expectation given the behaviour of ${\hat{\lambda}}_{\min}^{+}$. Taking inspiration from the optimization literature, it is natural for us to ask whether for neural networks, we can also connect the conditioning or ${\hat{\lambda}}_{\min}^{+}$ of intermediary features and double descent. This particular might be significant if we think of the last layer of the architecture as a least squares problem (assuming we are working with mean square error), and all previous layers as some random projection, ignoring that learning is affecting this projection as well.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Excess risk as a function of over-parameterization", "weight": 1.0} -->

This relationship between generalization and double descent on one hand, and the conditioning of the features and optimization process raises some additional interesting questions, particularly since, compared to the typical least squares setting, the conditioning of the problem for deep architectures does not solely depend on size. In the next section we empirically look at some of these questions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Empirical exploration in neural networks", "weight": 1.0} -->

The first natural question to ask is whether the observed behaviour for the least squares problem is reflected when working with neural networks. To explore this hypothesis, and to allow tractability of computing various quantities of interest (like ${\hat{\lambda}}_{\min}^{+}$), we focus on one hidden layer MLPs on the MNIST and FashionMNIST datasets. We follow the protocol used by Belkin et al., relying on a squared error loss. In order to increase the model size we simply increase the dimensionality of the latent space, and rely on gradient descent with a fixed learning rate and a training set to $1000$ randomly chosen examples for both datasets. More details can be found in Appendix G.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Empirical exploration in neural networks", "weight": 1.0} -->

Following this, if we think of the output layer as solving a least squares problem, while the rest of the network provides a projection of the data, we can consider what can affect the conditioning of the last latent space of the network. We put forward the hypothesis that ${\hat{\lambda}}_{\min}^{+}$ is not simply affected by the number of parameters, but actually the distribution of these parameters in the architecture matters.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Empirical exploration in neural networks", "weight": 1.0} -->

To test this hypothesis, we conduct an experiment where we compare the behavior of a network with a single hidden layer and a network with three hidden layers. For both networks, we increase the size of the hidden layers. For the deeper network, we consider either increasing the size of all the hidden layers or grow only the last hidden layer while keeping the others to a fixed small size, creating a strong bottleneck in the network. Figure 3 shows the results obtained with the former, while the effect of the bottleneck can be seen in Appendix F. We first observe that for the three tested networks, the drop in the minimum eigenvalues happens when the size of the last hidden layer reaches the number of training samples, as predicted by the theory. The magnitude of this drop and behavior across the different tested sizes depends however on the previous layers. In particular, we observe that the bottleneck yields features that are more ill-conditioned than the network with wide hidden layers, where the width of the last layer on its own can not compensate for the existence of the bottleneck.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Empirical exploration in neural networks", "weight": 1.0} -->

Moreover, from Figure 3, we can clearly see that the features obtained by the deeper network have a bigger drop in the minimum eigenvalue, which results, as expected in a higher increase in the test error around the interpolation threshold.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Empirical exploration in neural networks", "weight": 1.0} -->

It is well known that depth can harm optimization making the problem ill-conditioned, hence the reliance on skip-connections and batch normalization De and Smith to train very deep architecture. Our construction provides a way of reasoning about double descent that allows us to factor in the ill-conditioning of the learning problem. Rather than focusing simply on the model size, it suggests that for neural networks the quantity of interest might also be ${\hat{\lambda}}_{\min}^{+}$ for intermediary features, which is affected by size of the model but also by the distribution of the weights and architectural choices. For now we present more empirical explorations and ablations in Appendix G, and put forward this perspective as a conjecture for further exploration.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this work we analyse the double descent phenomenon in the context of the least squares problem. We make the observation that the excess risk of gradient descent is controlled by the smallest *positive* eigenvalue, ${\hat{\lambda}}_{\min}^{+}$, of the feature covariance matrix. Furthermore, this quantity follows the Bai-Yin law with high probability under mild distributional assumptions on features, that is, it manifests a U-shaped behaviour as the number of features increases, which we argue induces a double descent shape of the excess risk. Through this we provide a connection between the widely known phenomena and optimization process and conditioning of the problem. We believe this insight provides a different perspective compared to existing results focusing on the Moore-Penrose pseudo-inverse solution. In particular our work conjectures that the connection between the known double descent shape and model size is through ${\hat{\lambda}}_{\min}^{+}$ of the features at intermediary layers. For the least squares problem ${\hat{\lambda}}_{\min}^{+}$ correlates strongly with model size (and hence feature size).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

However this might not necessarily be always true for neural networks. For example we show empirically that while both depth and width increase the model size, they might affect ${\hat{\lambda}}_{\min}^{+}$ differently. We believe that our work could enable much needed effort, either empirical or theoretical, to disentangle further the role of various factors, like depth and width or other architectural choices like skip connections on double descent.
