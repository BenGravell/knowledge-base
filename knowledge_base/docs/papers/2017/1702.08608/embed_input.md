<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Towards a Rigorous Science of Interpretable Machine Learning

Topics include Safety, Learning, Machine learning, Position paper.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

As machine learning systems become ubiquitous, there has been a surge of interest in interpretable machine learning: systems that provide explanation for their outputs. These explanations are often used to qualitatively assess other criteria such as safety or non-discrimination. However, despite the interest in interpretability, there is very little consensus on what interpretable machine learning is and how it should be measured. In this position paper, we first define interpretability and describe when interpretability is needed (and when it is not). Next, we suggest a taxonomy for rigorous evaluation and expose open questions towards a more rigorous science of interpretable machine learning.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Interpretability is used to confirm other important desiderata of ML systems", "weight": 1.0} -->

There exist many auxiliary criteria that one may wish to optimize. Notions of *fairness* or *unbiasedness* imply that protected groups (explicit or implicit) are not somehow discriminated against. *Privacy* means the method protects sensitive information in the data. Properties such as *reliability* and *robustness* ascertain whether algorithms reach certain levels of performance in the face of parameter or input variation. *Causality* implies that the predicted change in output due to a perturbation will occur in the real system. *Usable* methods provide information that assist users to accomplish a task---e.g. a knob to tweak image lighting---while *trusted* systems have the confidence of human users---e.g. aircraft collision avoidance systems. Some areas, such as the fairness and privacy the research communities have formalized their criteria, and these formalizations have allowed for a blossoming of rigorous research in these fields (without the need for interpretability). However, in many cases, formal definitions remain elusive.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Interpretability is used to confirm other important desiderata of ML systems", "weight": 1.0} -->

Following the psychology literature, where Keil et al. notes "explanations may highlight an incompleteness," we argue that interpretability can assist in qualitatively ascertaining whether other desiderata---such as fairness, privacy, reliability, robustness, causality, usability and trust---are met. For example, one can provide a feasible explanation that fails to correspond to a causal structure, exposing a potential concern.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Why interpretability? Incompleteness", "weight": 1.0} -->

Not all ML systems require interpretability. Ad servers, postal code sorting, air craft collision avoidance systems---all compute their output without human intervention. Explanation is not necessary either because there are no significant consequences for unacceptable results or the problem is sufficiently well-studied and validated in real applications that we trust the system's decision, even if the system is not perfect.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Why interpretability? Incompleteness", "weight": 1.0} -->

So when is explanation necessary and appropriate? We argue that the need for interpretability stems from an *incompleteness* in the problem formalization, creating a fundamental barrier to optimization and evaluation. Note that incompleteness is distinct from uncertainty: the fused estimate of a missile location may be uncertain, but such uncertainty can be rigorously quantified and formally reasoned about. In machine learning terms, we distinguish between cases where unknowns result in quantified variance---e.g. trying to learn from small data set or with limited sensors---and incompleteness that produces some kind of unquantified bias---e.g. the effect of including domain knowledge in a model selection process.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Why interpretability? Incompleteness", "weight": 1.0} -->

Scientific Understanding: The human's goal is to gain knowledge. We do not have a complete way of stating what knowledge is; thus the best we can do is ask for explanations we can convert into knowledge.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Why interpretability? Incompleteness", "weight": 1.0} -->

Safety: For complex tasks, the end-to-end system is almost never completely testable; one cannot create a complete list of scenarios in which the system may fail. Enumerating all possible outputs given all possible inputs be computationally or logistically infeasible, and we may be unable to flag all undesirable outputs.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Why interpretability? Incompleteness", "weight": 1.0} -->

Ethics: The human may want to guard against certain kinds of discrimination, and their notion of fairness may be too abstract to be completely encoded into the system (e.g., one might desire a 'fair' classifier for loan approval). Even if we can encode protections for specific protected classes into the system, there might be biases that we did not consider a priori (e.g., one may not build gender-biased word embeddings on purpose, but it was a pattern in data that became apparent only after the fact).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Why interpretability? Incompleteness", "weight": 1.0} -->

Mismatched objectives: The agent's algorithm may be optimizing an incomplete objective---that is, a proxy function for the ultimate goal. For example, a clinical system may be optimized for cholesterol control, without considering the likelihood of adherence; an automotive engineer may be interested in engine data not to make predictions about engine failures but to more broadly build a better car.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Why interpretability? Incompleteness", "weight": 1.0} -->

Multi-objective trade-offs: Two well-defined desiderata in ML systems may compete with each other, such as privacy and prediction quality or privacy and non-discrimination. Even if each objectives are fully-specified, the exact dynamics of the trade-off may not be fully known, and the decision may have to be case-by-case.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Why interpretability? Incompleteness", "weight": 1.0} -->

In the presence of an incompleteness, explanations are one of ways to ensure that effects of gaps in problem formalization are visible to us.

<!-- chunk {"id": "body-0013", "role": "body", "section": "How? A Taxonomy of Interpretability Evaluation", "weight": 1.0} -->

Even in standard ML settings, there exists a taxonomy of evaluation that is considered appropriate. In particular, the evaluation should match the claimed contribution. Evaluation of applied work should demonstrate success in the application: a game-playing agent might best a human player, a classifier may correctly identify star types relevant to astronomers. In contrast, core methods work should demonstrate generalizability via careful evaluation on a variety of synthetic and standard benchmarks.

<!-- chunk {"id": "body-0014", "role": "body", "section": "How? A Taxonomy of Interpretability Evaluation", "weight": 1.0} -->

In this section we lay out an analogous taxonomy of evaluation approaches for interpretability: application-grounded, human-grounded, and functionally-grounded. These range from task-relevant to general, also acknowledge that while human evaluation is essential to assessing interpretability, human-subject evaluation is not an easy task. A human experiment needs to be well-designed to minimize confounding factors, consumed time, and other resources. We discuss the trade-offs between each type of evaluation and when each would be appropriate.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Application-grounded Evaluation: Real humans, real tasks", "weight": 1.0} -->

Application-grounded evaluation involves conducting human experiments within a real application. If the researcher has a concrete application in mind---such as working with doctors on diagnosing patients with a particular disease---the best way to show that the model works is to evaluate it with respect to the task: doctors performing diagnoses. This reasoning aligns with the methods of evaluation common in the human-computer interaction and visualization communities, where there exists a strong ethos around making sure that the system delivers on its intended task. For example, a visualization for correcting segmentations from microscopy data would be evaluated via user studies on segmentation on the target image task; a homework-hint system is evaluated on whether the student achieves better post-test performance.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Application-grounded Evaluation: Real humans, real tasks", "weight": 1.0} -->

Specifically, we evaluate the quality of an explanation in the context of its end-task, such as whether it results in better identification of errors, new facts, or less discrimination.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Application-grounded Evaluation: Real humans, real tasks", "weight": 1.0} -->

Domain expert experiment with the exact application task.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Application-grounded Evaluation: Real humans, real tasks", "weight": 1.0} -->

Domain expert experiment with a simpler or partial task to shorten experiment time and increase the pool of potentially-willing subjects.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Application-grounded Evaluation: Real humans, real tasks", "weight": 1.0} -->

In both cases, an important baseline is how well *human-produced* explanations assist in other humans trying to complete the task. To make high impact in real world applications, it is essential that we as a community respect the time and effort involved to do such evaluations, and also demand high standards of experimental design when such evaluations are performed. As HCI community recognizes, this is not an easy evaluation metric. Nonetheless, it directly tests the objective that the system is built, and thus performance with respect to that objective gives strong evidence of success.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Human-grounded Metrics: Real humans, simplified tasks", "weight": 1.0} -->

Human-grounded evaluation is about conducting simpler human-subject experiments that maintain the essence of the target application. Such an evaluation is appealing when experiments with the target community is challenging. These evaluations can be completed with lay humans, allowing for both a bigger subject pool and less expenses, since we do not have to compensate highly trained domain experts. Human-grounded evaluation is most appropriate when one wishes to test more general notions of the quality of an explanation. For example, to study what kinds of explanations are best understood under severe time constraints, one might create abstract tasks in which other factors---such as the overall task complexity---can be controlled

<!-- chunk {"id": "body-0021", "role": "body", "section": "Human-grounded Metrics: Real humans, simplified tasks", "weight": 1.0} -->

The key question, of course, is how we can evaluate the quality of an explanation without a specific end-goal (such as identifying errors in a safety-oriented task or identifying relevant patterns in a science-oriented task). Ideally, our evaluation approach will depend only on the quality of the explanation, regardless of whether the explanation is the model itself or a post-hoc interpretation of a black-box model, and regardless of the correctness of the associated prediction.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Human-grounded Metrics: Real humans, simplified tasks", "weight": 1.0} -->

Binary forced choice: humans are presented with pairs of explanations, and must choose the one that they find of higher quality (basic face-validity test made quantitative).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Human-grounded Metrics: Real humans, simplified tasks", "weight": 1.0} -->

Forward simulation/prediction: humans are presented with an explanation and an input, and must correctly simulate the model's output (regardless of the true output).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Human-grounded Metrics: Real humans, simplified tasks", "weight": 1.0} -->

Counterfactual simulation: humans are presented with an explanation, an input, and an output, and are asked what must be changed to change the method's prediction to a desired output (and related variants).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Human-grounded Metrics: Real humans, simplified tasks", "weight": 1.0} -->

Here is a concrete example. The common intrusion-detection test in topic models is a form of the forward simulation/prediction task: we ask the human to find the difference between the model's true output and some corrupted output as a way to determine whether the human has correctly understood what the model's true output is.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Functionally-grounded Evaluation: No humans, proxy tasks", "weight": 1.0} -->

Functionally-grounded evaluation requires no human experiments; instead, it uses some formal definition of interpretability as a proxy for explanation quality. Such experiments are appealing because even general human-subject experiments require time and costs both to perform and to get necessary approvals (e.g., IRBs), which may be beyond the resources of a machine learning researcher. Functionally-grounded evaluations are most appropriate once we have a class of models or regularizers that have already been validated, e.g. via human-grounded experiments. They may also be appropriate when a method is not yet mature or when human subject experiments are unethical.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Functionally-grounded Evaluation: No humans, proxy tasks", "weight": 1.0} -->

The challenge, of course, is to determine what proxies to use. For example, decision trees have been considered interpretable in many situations. In section 4, we describe open problems in determining what proxies are reasonable. Once a proxy has been formalized, the challenge is squarely an optimization problem, as the model class or regularizer is likely to be discrete, non-convex and often non-differentiable. Examples of experiments include

<!-- chunk {"id": "body-0028", "role": "body", "section": "Functionally-grounded Evaluation: No humans, proxy tasks", "weight": 1.0} -->

Show the improvement of prediction performance of a model that is already proven to be interpretable (assumes that someone has run human experiments to show that the model class is interpretable).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Functionally-grounded Evaluation: No humans, proxy tasks", "weight": 1.0} -->

Show that one's method performs better with respect to certain regularizers---for example, is more sparse---compared to other baselines (assumes someone has run human experiments to show that the regularizer is appropriate).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Open Problems in the Science of Interpretability, Theory and Practice", "weight": 1.0} -->

It is essential that the three types of evaluation in the previous section inform each other: the factors that capture the essential needs of real world tasks should inform what kinds of simplified tasks we perform, and the performance of our methods with respect to functional proxies should reflect their performance in real-world settings.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Open Problems in the Science of Interpretability, Theory and Practice", "weight": 1.0} -->

What proxies are best for what real-world applications? (functionally to application-grounded)

<!-- chunk {"id": "body-0032", "role": "body", "section": "Open Problems in the Science of Interpretability, Theory and Practice", "weight": 1.0} -->

What are the important factors to consider when designing simpler tasks that maintain the essence of the real end-task? (human to application-grounded)

<!-- chunk {"id": "body-0033", "role": "body", "section": "Open Problems in the Science of Interpretability, Theory and Practice", "weight": 1.0} -->

What are the important factors to consider when characterizing proxies for explanation quality? (human to functionally-grounded)

<!-- chunk {"id": "body-0034", "role": "body", "section": "Open Problems in the Science of Interpretability, Theory and Practice", "weight": 1.0} -->

Below, we describe a path to answering each of these questions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Data-driven approach to discover factors of interpretability", "weight": 1.0} -->

Imagine a matrix where rows are specific real-world tasks, columns are specific methods, and the entries are the performance of the method on the end-task. For example, one could represent how well a decision tree of depth less than 4 worked in assisting doctors in identifying pneumonia patients under age 30 in US. Once constructed, methods in machine learning could be used to identify latent dimensions that represent factors that are important to interpretability. This approach is similar to efforts to characterize classification and clustering problems. For example, one might perform matrix factorization to embed both tasks and methods respectively in low-dimensional spaces (which we can then seek to interpret), as shown in Figure 2. These embeddings could help predict what methods would be most promising for a new problem, similarly to collaborative filtering.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Data-driven approach to discover factors of interpretability", "weight": 1.0} -->

The challenge, of course, is in creating this matrix. For example, one could imagine creating a repository of clinical cases in which the ML system has access to the patient's record but not certain current features that are only accessible to the clinician, or a repository of discrimination-in-loan cases where the ML system must provide outputs that assist a lawyer in their decision. Ideally these would be linked to domain experts who have agreed to be employed to evaluate methods when applied to their domain of expertise. *Just as there are now large open repositories for problems in classification, regression, and reinforcement learning, we advocate for the creation of repositories that contain problems corresponding to real-world tasks in which human-input is required.* Creating such repositories will be more challenging than creating collections of standard machine learning datasets because they must include a system for human assessment, but with the availablity of crowdsourcing tools these technical challenges can be surmounted.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Data-driven approach to discover factors of interpretability", "weight": 1.0} -->

In practice, constructing such a matrix will be expensive since each cell must be evaluated in the context of a real application, and interpreting the latent dimensions will be an iterative effort of hypothesizing why certain tasks or methods share dimensions and then checking whether our hypotheses are true. In the next two open problems, we lay out some hypotheses about what latent dimensions may correspond to; these hypotheses can be tested via much less expensive human-grounded evaluations on simulated tasks.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Hypothesis: task-related latent dimensions of interpretability", "weight": 1.0} -->

Disparate-seeming applications may share common categories: an application involving preventing medical error at the bedside and an application involving support for identifying inappropriate language on social media might be similar in that they involve making a decision about a specific case---a patient, a post---in a relatively short period of time. However, when it comes to time constraints, the needs in those scenarios might be different from an application involving the understanding of the main characteristics of a large omics data set, where the goal---science---is much more abstract and the scientist may have hours or days to inspect the model outputs.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Hypothesis: task-related latent dimensions of interpretability", "weight": 1.0} -->

*Global vs. Local.* Global interpretability implies knowing what patterns are present in general (such as key features governing galaxy formation), while local interpretability implies knowing the reasons for a specific decision (such as why a particular loan application was rejected). The former may be important for when scientific understanding or bias detection is the goal; the latter when one needs a justification for a specific decision.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Hypothesis: task-related latent dimensions of interpretability", "weight": 1.0} -->

*Area, Severity of Incompleteness.* What part of the problem formulation is incomplete, and how incomplete is it? We hypothesize that the types of explanations needed may vary depending on whether the source of concern is due to incompletely specified inputs, constraints, domains, internal model structure, costs, or even in the need to understand the training algorithm. The severity of the incompleteness may also affect explanation needs. For example, one can imagine a spectrum of questions about the safety of self-driving cars. On one end, one may have general curiosity about how autonomous cars make decisions. At the other, one may wish to check a specific list of scenarios (e.g., sets of sensor inputs that causes the car to drive off of the road by 10cm). In between, one might want to check a general property---safe urban driving---without an exhaustive list of scenarios and safety criteria.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Hypothesis: task-related latent dimensions of interpretability", "weight": 1.0} -->

*Time Constraints.* How long can the user afford to spend to understand the explanation? A decision that needs to be made at the bedside or during the operation of a plant must be understood quickly, while in scientific or anti-discrimination applications, the end-user may be willing to spend hours trying to fully understand an explanation.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Hypothesis: task-related latent dimensions of interpretability", "weight": 1.0} -->

*Nature of User Expertise.* How experienced is the user in the task? The user's experience will affect what kind of *cognitive chunks* they have, that is, how they organize individual elements of information into collections. For example, a clinician may have a notion that autism and ADHD are both developmental diseases. The nature of the user's expertise will also influence what level of sophistication they expect in their explanations. For example, domain experts may expect or prefer a somewhat larger and sophisticated model---which confirms facts they know---over a smaller, more opaque one. These preferences may be quite different from hospital ethicist who may be more narrowly concerned about whether decisions are being made in an ethical manner. More broadly, decison-makers, scientists, compliance and safety engineers, data scientists, and machine learning researchers all come with different background knowledge and communication styles.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Hypothesis: task-related latent dimensions of interpretability", "weight": 1.0} -->

Each of these factors can be isolated in human-grounded experiments in simulated tasks to determine which methods work best when they are present.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Hypothesis: method-related latent dimensions of interpretability", "weight": 1.0} -->

Just as disparate applications may share common categories, disparate methods may share common qualities that correlate to their utility as explanation. As before, we provide a (non-exhaustive!) set of factors that may correspond to different explanation needs: Here, we define *cognitive chunks* to be the basic units of explanation.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Hypothesis: method-related latent dimensions of interpretability", "weight": 1.0} -->

*Form of cognitive chunks.* What are the basic units of the explanation? Are they raw features? Derived features that have some semantic meaning to the expert (e.g. "neurological disorder" for a collection of diseases or "chair" for a collection of pixels)? Prototypes?

<!-- chunk {"id": "body-0046", "role": "body", "section": "Hypothesis: method-related latent dimensions of interpretability", "weight": 1.0} -->

*Number of cognitive chunks.* How many cognitive chunks does the explanation contain? How does the quantity interact with the type: for example, a prototype can contain a lot more information than a feature; can we handle them in similar quantities?

<!-- chunk {"id": "body-0047", "role": "body", "section": "Hypothesis: method-related latent dimensions of interpretability", "weight": 1.0} -->

*Level of compositionality.* Are the cognitive chunks organized in a structured way? Rules, hierarchies, and other abstractions can limit what a human needs to process at one time. For example, part of an explanation may involve *defining* a new unit (a chunk) that is a function of raw units, and then providing an explanation in terms of that new unit.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Hypothesis: method-related latent dimensions of interpretability", "weight": 1.0} -->

*Monotonicity and other interactions between cognitive chunks.* Does it matter if the cognitive chunks are combined in linear or nonlinear ways? In monotone ways ? Are some functions more natural to humans than others ?

<!-- chunk {"id": "body-0049", "role": "body", "section": "Hypothesis: method-related latent dimensions of interpretability", "weight": 1.0} -->

*Uncertainty and stochasticity.* How well do people understand uncertainty measures? To what extent is stochasticity understood by humans?

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion: Recommendations for Researchers", "weight": 1.5} -->

In this work, we have laid the groundwork for a process to rigorously define and evaluate interpretability. There are many open questions in creating the formal links between applications, the science of human understanding, and more traditional machine learning regularizers. In the mean time, we encourage the community to consider some general principles.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion: Recommendations for Researchers", "weight": 1.5} -->

*The claim of the research should match the type of the evaluation.* Just as one would be critical of a reliability-oriented paper that only cites accuracy statistics, the choice of evaluation should match the specificity of the claim being made. A contribution that is focused on a particular application should be expected to be evaluated in the context of that application (application-grounded evaluation), or on a human experiment with a closely-related task (human-grounded evaluation). A contribution that is focused on better optimizing a model class for some definition of interpretability should be expected to be evaluated with functionally-grounded metrics. As a community, we must be careful in the work on interpretability, both recognizing the need for and the costs of human-subject experiments.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion: Recommendations for Researchers", "weight": 1.5} -->

*We should categorize our applications and methods with a common taxonomy.* In section 4, we hypothesized factors that may be the latent dimensions of interpretability. Creating a shared language around such factors is essential not only to evaluation, but also for the citation and comparison of related work. For example, work on creating a safe healthcare agent might be framed as focused on the need for explanation due to unknown inputs at the local scale, evaluated at the level of an application. In contrast, work on learning sparse linear models might also be framed as focused on the need for explanation due to unknown inputs, but this time evaluated at global scale. As we share each of our work with the community, we can do each other a service by describing factors such as

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion: Recommendations for Researchers", "weight": 1.5} -->

How is the problem formulation incomplete? (Section 2)

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion: Recommendations for Researchers", "weight": 1.5} -->

At what level is the evaluation being performed? (application, general user study, proxy; Section 3)

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion: Recommendations for Researchers", "weight": 1.5} -->

What are task-related relevant factors? (e.g. global vs. local, severity of incompleteness, level of user expertise, time constraints; Section 4.2)

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion: Recommendations for Researchers", "weight": 1.5} -->

What are method-related relevant factors being explored? (e.g. form of cognitive chunks, number of cognitive chunks, compositionality, monotonicity, uncertainty; Section 4.3)

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion: Recommendations for Researchers", "weight": 1.5} -->

and of course, adding and refining these factors as our taxonomies evolve. These considerations should move us away from vague claims about the interpretability of a particular model and toward classifying applications by a common set of terms.
