<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Unified Approach to Interpreting Model Predictions

Topics include Explainability, Feature attribution, SHAP, Shapley value, Machine learning interpretability, Model explanations.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces SHAP (SHapley Additive exPlanations), a unified framework for local model explainability grounded in Shapley values from cooperative game theory. Shows that six prior explanation methods are all special cases of SHAP values, and that only SHAP satisfies a desirable set of axioms (local accuracy, missingness, consistency), making it the standard feature-attribution method.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Understanding why a model makes a certain prediction can be as crucial as the prediction's accuracy in many applications. However, the highest accuracy for large modern datasets is often achieved by complex models that even experts struggle to interpret, such as ensemble or deep learning models, creating a tension between accuracy and interpretability. In response, various methods have recently been proposed to help users interpret the predictions of complex models, but it is often unclear how these methods are related and when one method is preferable over another. To address this problem, we present a unified framework for interpreting predictions, SHAP (SHapley Additive exPlanations). SHAP assigns each feature an importance value for a particular prediction. Its novel components include: the identification of a new class of additive feature importance measures, and theoretical results showing there is a unique solution in this class with a set of desirable properties. The new class unifies six existing methods, notable because several recent methods in the class lack the proposed desirable properties. Based on insights from this unification, we present new methods that show improved computational performance and/or better consistency with human intuition than previous approaches.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The ability to correctly interpret a prediction model's output is extremely important. It engenders appropriate user trust, provides insight into how a model may be improved, and supports understanding of the process being modeled. In some applications, simple models (e.g., linear models) are often preferred for their ease of interpretation, even if they may be less accurate than complex ones. However, the growing availability of big data has increased the benefits of using complex models, so bringing to the forefront the trade-off between accuracy and interpretability of a model's output. A wide variety of different methods have been recently proposed to address this issue. But an understanding of how these methods relate and when one method is preferable to another is still lacking.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here, we present a novel unified approach to interpreting model predictions.^11^1 Our approach leads to three potentially surprising results that bring clarity to the growing space of methods: We introduce the perspective of viewing any explanation of a model's prediction as a model itself, which we term the explanation model. This lets us define the class of *additive feature attribution methods* (Section 2), which unifies six current methods.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We then show that game theory results guaranteeing a unique solution apply to the *entire class* of additive feature attribution methods (Section 3) and propose *SHAP values* as a unified measure of feature importance that various methods approximate (Section 4 Values ‣ A Unified Approach to Interpreting Model Predictions")).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose new SHAP value estimation methods and demonstrate that they are better aligned with human intuition as measured by user studies and more effectually discriminate among model output classes than several existing methods (Section 5).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Additive Feature Attribution Methods", "weight": 1.0} -->

The best explanation of a simple model is the model itself; it perfectly represents itself and is easy to understand. For complex models, such as ensemble methods or deep networks, we cannot use the original model as its own best explanation because it is not easy to understand. Instead, we must use a simpler *explanation model*, which we define as any interpretable approximation of the original model. We show below that six current explanation methods from the literature all use the same explanation model. This previously unappreciated unity has interesting implications, which we describe in later sections.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Additive Feature Attribution Methods", "weight": 1.0} -->

Let $f$ be the original prediction model to be explained and $g$ the explanation model. Here, we focus on *local methods* designed to explain a prediction $f{(x)}$ based on a single input $x$, as proposed in LIME. Explanation models often use simplified inputs $x'$ that map to the original inputs through a mapping function $x = {h_{x}{(x')}}$. Local methods try to ensure ${g{(z')}} \approx {f{({h_{x}{(z')}})}}$ whenever $z' \approx x'$. (Note that ${h_{x}{(x')}} = x$ even though $x'$ may contain less information than $x$ because $h_{x}$ is specific to the current input $x$.)

<!-- chunk {"id": "body-0010", "role": "body", "section": "LIME", "weight": 1.0} -->

The LIME method interprets individual model predictions based on locally approximating the model around a given prediction. The local linear explanation model that LIME uses adheres to Equation 1 exactly and is thus an additive feature attribution method. LIME refers to simplified inputs $x'$ as "interpretable inputs," and the mapping $x = {h_{x}{(x')}}$ converts a binary vector of interpretable inputs into the original input space. Different types of $h_{x}$ mappings are used for different input spaces. For bag of words text features, $h_{x}$ converts a vector of $1$'s or $0$'s (present or not) into the original word count if the simplified input is one, or zero if the simplified input is zero. For images, $h_{x}$ treats the image as a set of super pixels; it then maps $1$ to leaving the super pixel as its original value and $0$ to replacing the super pixel with an average of neighboring pixels (this is meant to represent being missing).

<!-- chunk {"id": "body-0011", "role": "body", "section": "LIME", "weight": 1.0} -->

To find $\phi$, LIME minimizes the following objective function: Faithfulness of the explanation model $g{(z')}$ to the original model $f{({h_{x}{(z')}})}$ is enforced through the loss $L$ over a set of samples in the simplified input space weighted by the local kernel $\pi_{x'}$. $\Omega$ penalizes the complexity of $g$. Since in LIME $g$ follows Equation 1 and $L$ is a squared loss, Equation 2 can be solved using penalized linear regression.

<!-- chunk {"id": "body-0012", "role": "body", "section": "DeepLIFT", "weight": 1.0} -->

DeepLIFT was recently proposed as a recursive prediction explanation method for deep learning. It attributes to each input $x_{i}$ a value $C_{\Deltax_{i}\Deltay}$ that represents the effect of that input being set to a reference value as opposed to its original value. This means that for DeepLIFT, the mapping $x = {h_{x}{(x')}}$ converts binary values into the original inputs, where $1$ indicates that an input takes its original value, and $0$ indicates that it takes the reference value. The reference value, though chosen by the user, represents a typical uninformative background value for the feature.

<!-- chunk {"id": "body-0013", "role": "body", "section": "DeepLIFT", "weight": 1.0} -->

DeepLIFT uses a \"summation-to-delta\" property that states: where $o = {f{(x)}}$ is the model output, ${\Deltao} = {{f{(x)}} - {f{(r)}}}$, ${\Deltax_{i}} = {x_{i} - r_{i}}$, and $r$ is the reference input. If we let $\phi_{i} = C_{\Deltax_{i}\Deltao}$ and $\phi_{0} = {f{(r)}}$, then DeepLIFT's explanation model matches Equation 1 and is thus another additive feature attribution method.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Layer-Wise Relevance Propagation", "weight": 1.0} -->

The layer-wise relevance propagation method interprets the predictions of deep networks. As noted, this menthod is equivalent to DeepLIFT with the reference activations of all neurons fixed to zero. Thus, $x = {h_{x}{(x')}}$ converts binary values into the original input space, where $1$ means that an input takes its original value, and $0$ means an input takes the $0$ value. Layer-wise relevance propagation's explanation model, like DeepLIFT's, matches Equation 1.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Classic Shapley Value Estimation", "weight": 1.0} -->

Three previous methods use classic equations from cooperative game theory to compute explanations of model predictions: Shapley regression values, Shapley sampling values, and Quantitative Input Influence.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Classic Shapley Value Estimation", "weight": 1.0} -->

Shapley regression values are feature importances for linear models in the presence of multicollinearity. This method requires retraining the model on all feature subsets $S \subseteq F$, where $F$ is the set of all features. It assigns an importance value to each feature that represents the effect on the model prediction of including that feature. To compute this effect, a model $f_{S \cup {\{ i\}}}$ is trained with that feature present, and another model $f_{S}$ is trained with the feature withheld. Then, predictions from the two models are compared on the current input ${f_{S \cup {\{ i\}}}{(x_{S \cup {\{ i\}}})}} - {f_{S}{(x_{S})}}$, where $x_{S}$ represents the values of the input features in the set $S$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Classic Shapley Value Estimation", "weight": 1.0} -->

Since the effect of withholding a feature depends on other features in the model, the preceding differences are computed for all possible subsets $S \subseteq {F \smallsetminus {\{ i\}}}$. The Shapley values are then computed and used as feature attributions. They are a weighted average of all possible differences: For Shapley regression values, $h_{x}$ maps $1$ or $0$ to the original input space, where $1$ indicates the input is included in the model, and $0$ indicates exclusion from the model. If we let $\phi_{0} = {f_{\varnothing}{(\varnothing)}}$, then the Shapley regression values match Equation 1 and are hence an additive feature attribution method.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Classic Shapley Value Estimation", "weight": 1.0} -->

Shapley sampling values are meant to explain any model: applying sampling approximations to Equation 4, and approximating the effect of removing a variable from the model by integrating over samples from the training dataset. This eliminates the need to retrain the model and allows fewer than $2^{|F|}$ differences to be computed. Since the explanation model form of Shapley sampling values is the same as that for Shapley regression values, it is also an additive feature attribution method.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Classic Shapley Value Estimation", "weight": 1.0} -->

Quantitative input influence is a broader framework that addresses more than feature attributions. However, as part of its method it independently proposes a sampling approximation to Shapley values that is nearly identical to Shapley sampling values. It is thus another additive feature attribution method.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Simple Properties Uniquely Determine Additive Feature Attributions", "weight": 1.0} -->

A surprising attribute of the class of additive feature attribution methods is the presence of a single unique solution in this class with three desirable properties (described below). While these properties are familiar to the classical Shapley value estimation methods, they were previously unknown for other additive feature attribution methods.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Simple Properties Uniquely Determine Additive Feature Attributions", "weight": 1.0} -->

The first desirable property is local accuracy. When approximating the original model $f$ for a specific input $x$, local accuracy requires the explanation model to at least match the output of $f$ for the simplified input $x'$ (which corresponds to the original input $x$).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Property 1 (Local accuracy)", "weight": 1.0} -->

The explanation model $g{(x')}$ matches the original model $f{(x)}$ when $x = {h_{x}{(x')}}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Property 1 (Local accuracy)", "weight": 1.0} -->

The second property is missingness. If the simplified inputs represent feature presence, then missingness requires features missing in the original input to have no impact. All of the methods described in Section 2 obey the missingness property.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Property 2 (Missingness)", "weight": 1.0} -->

Missingness constrains features where $x_{i}' = 0$ to have no attributed impact.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Property 2 (Missingness)", "weight": 1.0} -->

The third property is consistency. Consistency states that if a model changes so that some simplified input's contribution increases or stays the same regardless of the other inputs, that input's attribution should not decrease.

<!-- chunk {"id": "body-0026", "role": "body", "section": "SHAP (SHapley Additive exPlanation) Values", "weight": 1.0} -->

We propose SHAP values as a unified measure of feature importance. These are the Shapley values of a conditional expectation function of the original model; thus, they are the solution to Equation 8, where ${f_{x}{(z')}} = {f{({h_{x}{(z')}})}} = {E{\lbrack{{f{(z)}} \mid z_{S}}\rbrack}}$, and $S$ is the set of non-zero indexes in $z'$ (Figure 1 Values ‣ A Unified Approach to Interpreting Model Predictions")). Based on Sections 2 and 3, SHAP values provide the unique additive feature importance measure that adheres to Properties 1-3 and uses conditional expectations to define simplified inputs. Implicit in this definition of SHAP values is a simplified input mapping, ${h_{x}{(z')}} = z_{S}$, where $z_{S}$ has missing values for features not in the set $S$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "SHAP (SHapley Additive exPlanation) Values", "weight": 1.0} -->

Since most models cannot handle arbitrary patterns of missing input values, we approximate $f{(z_{S})}$ with $E{\lbrack{{f{(z)}} \mid z_{S}}\rbrack}$. This definition of SHAP values is designed to closely align with the Shapley regression, Shapley sampling, and quantitative input influence feature attributions, while also allowing for connections with LIME, DeepLIFT, and layer-wise relevance propagation.

<!-- chunk {"id": "body-0028", "role": "body", "section": "SHAP (SHapley Additive exPlanation) Values", "weight": 1.0} -->

The exact computation of SHAP values is challenging. However, by combining insights from current additive feature attribution methods, we can approximate them. We describe two model-agnostic approximation methods, one that is already known (Shapley sampling values) and another that is novel (Kernel SHAP). We also describe four model-type-specific approximation methods, two of which are novel (Max SHAP, Deep SHAP). When using these methods, feature independence and model linearity are two optional assumptions simplifying the computation of the expected values (note that $\overline{S}$ is the set of features not in $S$): Figure 1: SHAP (SHapley Additive exPlanation) values attribute to each feature the change in the expected model prediction when conditioning on that feature. They explain how to get from the base value E [f (z)] that would be predicted if we did not know any features to the current output f (x). This diagram shows a single ordering.

<!-- chunk {"id": "body-0029", "role": "body", "section": "SHAP (SHapley Additive exPlanation) Values", "weight": 1.0} -->

When the model is non-linear or the input features are not independent, however, the order in which features are added to the expectation matters, and the SHAP values arise from averaging the ϕi values across all possible orderings.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Model-Agnostic Approximations", "weight": 1.0} -->

If we assume feature independence when approximating conditional expectations (Equation 11 Values ‣ A Unified Approach to Interpreting Model Predictions")), as, then SHAP values can be estimated directly using the Shapley sampling values method or equivalently the Quantitative Input Influence method. These methods use a sampling approximation of a permutation version of the classic Shapley value equations (Equation 8). Separate sampling estimates are performed for each feature attribution. While reasonable to compute for a small number of inputs, the Kernel SHAP method described next requires fewer evaluations of the original model to obtain similar approximation accuracy (Section 5).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Kernel SHAP (Linear LIME + Shapley values)", "weight": 1.0} -->

Linear LIME uses a linear explanation model to locally approximate $f$, where local is measured in the simplified binary input space. At first glance, the regression formulation of LIME in Equation 2 seems very different from the classical Shapley value formulation of Equation 8. However, since linear LIME is an additive feature attribution method, we know the Shapley values are the only possible solution to Equation 2 that satisfies Properties 1-3 -- local accuracy, missingness and consistency. A natural question to pose is whether the solution to Equation 2 recovers these values. The answer depends on the choice of loss function $L$, weighting kernel $\pi_{x'}$ and regularization term $\Omega$. The LIME choices for these parameters are made heuristically; using these choices, Equation 2 does not recover the Shapley values. One consequence is that local accuracy and/or consistency are violated, which in turn leads to unintuitive behavior in certain circumstances (see Section 5).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Kernel SHAP (Linear LIME + Shapley values)", "weight": 1.0} -->

Below we show how to avoid heuristically choosing the parameters in Equation 2 and how to find the loss function $L$, weighting kernel $\pi_{x'}$, and regularization term $\Omega$ that recover the Shapley values.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Model-Specific Approximations", "weight": 1.0} -->

While Kernel SHAP improves the sample efficiency of model-agnostic estimations of SHAP values, by restricting our attention to specific model types, we can develop faster model-specific approximation methods.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Linear SHAP", "weight": 1.0} -->

For linear models, if we assume input feature independence (Equation 11 Values ‣ A Unified Approach to Interpreting Model Predictions")), SHAP values can be approximated directly from the model's weight coefficients.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Low-Order SHAP", "weight": 1.0} -->

Since linear regression using Theorem 2 ‣ Kernel SHAP (Linear LIME + Shapley values) ‣ 4.1 Model-Agnostic Approximations ‣ 4 SHAP (SHapley Additive exPlanation) Values ‣ A Unified Approach to Interpreting Model Predictions") has complexity $O{({2^{M} + M^{3}})}$, it is efficient for small values of $M$ if we choose an approximation of the conditional expectations (Equation 11 Values ‣ A Unified Approach to Interpreting Model Predictions") or 12 Values ‣ A Unified Approach to Interpreting Model Predictions")).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Max SHAP", "weight": 1.0} -->

Using a permutation formulation of Shapley values, we can calculate the probability that each input will increase the maximum value over every other input. Doing this on a sorted order of input values lets us compute the Shapley values of a max function with $M$ inputs in $O{(M^{2})}$ time instead of $O{({M2^{M}})}$. See Supplementary Material for the full algorithm.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Deep SHAP (DeepLIFT + Shapley values)", "weight": 1.0} -->

While Kernel SHAP can be used on any model, including deep models, it is natural to ask whether there is a way to leverage extra knowledge about the compositional nature of deep networks to improve computational performance. We find an answer to this question through a previously unappreciated connection between Shapley values and DeepLIFT. If we interpret the reference value in Equation 3 as representing $E{\lbrack x\rbrack}$ in Equation 12 Values ‣ A Unified Approach to Interpreting Model Predictions"), then DeepLIFT approximates SHAP values assuming that the input features are independent of one another and the deep model is linear. DeepLIFT uses a linear composition rule, which is equivalent to linearizing the non-linear components of a neural network. Its back-propagation rules defining how each component is linearized are intuitive but were heuristically chosen. Since DeepLIFT is an additive feature attribution method that satisfies local accuracy and missingness, we know that Shapley values represent the only attribution values that satisfy consistency. This motivates our adapting DeepLIFT to become a compositional approximation of SHAP values, leading to Deep SHAP.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Deep SHAP (DeepLIFT + Shapley values)", "weight": 1.0} -->

Deep SHAP combines SHAP values computed for smaller components of the network into SHAP values for the whole network. It does so by recursively passing DeepLIFT's multipliers, now defined in terms of SHAP values, backwards through the network as in Figure 2 Values ‣ A Unified Approach to Interpreting Model Predictions")B: | | $\phi_{i}{(f_{3},y)}$ | $\approx {m_{y_{i}f_{3}}{({y_{i} - {E{\lbrack y_{i}\rbrack}}})}}$ | linear approximation | | \(16\) | Since the SHAP values for the simple network components can be efficiently solved analytically if they are linear, max pooling, or an activation function with just one input, this composition rule enables a fast approximation of values for the whole model. Deep SHAP avoids the need to heuristically choose ways to linearize components. Instead, it derives an effective linearization from the SHAP values computed for each component.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Deep SHAP (DeepLIFT + Shapley values)", "weight": 1.0} -->

The $max$ function offers one example where this leads to improved attributions (see Section 5).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Computational and User Study Experiments", "weight": 1.0} -->

We evaluated the benefits of SHAP values using the Kernel SHAP and Deep SHAP approximation methods. First, we compared the computational efficiency and accuracy of Kernel SHAP vs. LIME and Shapley sampling values. Second, we designed user studies to compare SHAP values with alternative feature importance allocations represented by DeepLIFT and LIME. As might be expected, SHAP values prove more consistent with human intuition than other methods that fail to meet Properties 1-3 (Section 2). Finally, we use MNIST digit image classification to compare SHAP with DeepLIFT and LIME.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Computational Efficiency", "weight": 1.0} -->

Theorem 2 ‣ Kernel SHAP (Linear LIME + Shapley values) ‣ 4.1 Model-Agnostic Approximations ‣ 4 SHAP (SHapley Additive exPlanation) Values ‣ A Unified Approach to Interpreting Model Predictions") connects Shapley values from game theory with weighted linear regression. Kernal SHAP uses this connection to compute feature importance. This leads to more accurate estimates with fewer evaluations of the original model than previous sampling-based estimates of Equation 8, particularly when regularization is added to the linear model (Figure 3). Comparing Shapley sampling, SHAP, and LIME on both dense and sparse decision tree models illustrates both the improved sample efficiency of Kernel SHAP and that values from LIME can differ significantly from SHAP values that satisfy local accuracy and consistency.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Consistency with Human Intuition", "weight": 1.0} -->

Theorem 1 provides a strong incentive for all additive feature attribution methods to use SHAP values. Both LIME and DeepLIFT, as originally demonstrated, compute different feature importance values. To validate the importance of Theorem 1, we compared explanations from LIME, DeepLIFT, and SHAP with user explanations of simple models (using Amazon Mechanical Turk). Our testing assumes that good model explanations should be consistent with explanations from humans who understand that model.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Consistency with Human Intuition", "weight": 1.0} -->

We compared LIME, DeepLIFT, and SHAP with human explanations for two settings. The first setting used a sickness score that was higher when only one of two symptoms was present (Figure 4A). The second used a max allocation problem to which DeepLIFT can be applied. Participants were told a short story about how three men made money based on the maximum score any of them achieved (Figure 4B). In both cases, participants were asked to assign credit for the output (the sickness score or money won) among the inputs (i.e., symptoms or players). We found a much stronger agreement between human explanations and SHAP than with other methods. SHAP's improved performance for max functions addresses the open problem of max pooling functions in DeepLIFT.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Explaining Class Differences", "weight": 1.0} -->

As discussed in Section 4.2 Values ‣ A Unified Approach to Interpreting Model Predictions"), DeepLIFT's compositional approach suggests a compositional approximation of SHAP values (Deep SHAP). These insights, in turn, improve DeepLIFT, and a new version includes updates to better match Shapley values. Figure 5 extends DeepLIFT's convolutional network example to highlight the increased performance of estimates that are closer to SHAP values. The pre-trained model and Figure 5 example are the same as those used, with inputs normalized between 0 and 1. Two convolution layers and 2 dense layers are followed by a 10-way softmax output layer. Both DeepLIFT versions explain a normalized version of the linear layer, while SHAP (computed using Kernel SHAP) and LIME explain the model's output. SHAP and LIME were both run with 50k samples (Supplementary Figure 1); to improve performance, LIME was modified to use single pixel segmentation over the digit pixels. To match, we masked 20% of the pixels chosen to switch the predicted class from 8 to 3 according to the feature attribution given by each method.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The growing tension between the accuracy and interpretability of model predictions has motivated the development of methods that help users interpret predictions. The SHAP framework identifies the class of additive feature importance methods (which includes six previous methods) and shows there is a unique solution in this class that adheres to desirable properties. The thread of unity that SHAP weaves through the literature is an encouraging sign that common principles about model interpretation can inform the development of future methods.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented several different estimation methods for SHAP values, along with proofs and experiments showing that these values are desirable. Promising next steps involve developing faster model-type-specific estimation methods that make fewer assumptions, integrating work on estimating interaction effects from game theory, and defining new explanation model classes.
