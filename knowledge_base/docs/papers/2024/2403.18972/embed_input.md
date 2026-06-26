<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Risk-Aware Robotics: Tail Risk Measures in Planning, Control, and Verification

Topics include Survey, Safety, Risk, Tail risk, Planning, Control, Verification.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Often, control theorists and roboticists expect systems to function as reliably and predictably as the equations we use to represent them. Sadly, reality is often more random than our equations. For example, take a robot navigating in two similar but unstructured environments. Random perturbations in terrain and scenery could cause the robot to take wildly different paths. In another example, take a perfectly orchestrated robotic swarm that finds itself in dissonance moments later due to network connectivity going down and package loss. Such randomness arises because our equations are imperfect models of reality. So, perhaps we should find a way to account for such randomness in our equations themselves. This article delves into how tail risk measures — formal mathematical concepts of risk traditionally used in the financial community — facilitate accounting for this randomness in planning, control, and verification. The exposition to follow both defines these measures and includes multiple examples of their use in prescribing risk-aware control across all levels of the modern control stack. Finally, we end with a brief survey of existing and open problems in the field.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Risk-Aware Robotics: Tail Risk Measures in Planning, Control, and Verification", "weight": 1.0} -->

Prithvi Akella*, Anushri Dixit*, Mohamadreza Ahmadi, Lars Lindemann, Margaret P. Chapman, George J. Pappas, Aaron D. Ames, and Joel W. Burdick P. Akella (prithvi.akella@gmail.com), A. D. Ames (ames@caltech.edu), and J. W. Burdick (jwb@robotics.caltech.edu) are with the Department of Mechanical and Civil Engineering, California Institute of Technology, Pasadena, CA, USA.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Risk-Aware Robotics: Tail Risk Measures in Planning, Control, and Verification", "weight": 1.0} -->

A. Dixit (anushridixit@ucla.edu) is with the Department of Mechanical and Aerospace Engineering, University of California, Los Angeles, USA.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Risk-Aware Robotics: Tail Risk Measures in Planning, Control, and Verification", "weight": 1.0} -->

M. Ahmadi (reza.ahmadi@gatik.ai) is with Gatik AI, 161 E Evelyn Ave, Mountain View, CA 94041.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Risk-Aware Robotics: Tail Risk Measures in Planning, Control, and Verification", "weight": 1.0} -->

L. Lindemann (llindema@usc.edu is with the Department of Computer Science, University of Southern California, Los Angeles, CA, USA.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Risk-Aware Robotics: Tail Risk Measures in Planning, Control, and Verification", "weight": 1.0} -->

- M. P. Chapman (mchapman@ece.utoronto.ca) is with the Edward S. Rogers Sr. Department of Electrical and Computer Engineering, University of Toronto, Toronto, ON, Canada.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Risk-Aware Robotics: Tail Risk Measures in Planning, Control, and Verification", "weight": 1.0} -->

G. J. Pappas (pappasg@seas.upenn.edu) is with the Department of Electrical and Systems Engineering, University of Pennsylvania, Philadelphia, PA, USA.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Why is the consideration of risk integral to robotics?", "weight": 1.0} -->

Consider the scenario of a rescue robot designed to navigate through a constrained environment to locate and rescue victims. Despite limited visibility and a ground that is potentially difficult to traverse, the robot is required to assess whether to execute a planned route or to seek an alternative route. Delays in finding an alternative route could negatively impact the victim's well-being while opting for the planned route could lead to the robot getting stuck. How should the robot gauge these competing risks? The issue of risk assessment is not new to roboticists and control engineers, and in practical applications, it is usually tackled using heuristics. For instance, the robot constructs a map of the environment using computer vision. As this map is uncertain, one may attempt to decrease the robot's risk by tightening the area that can safely be traversed. This tightening is often based on past experimental data. However, this experimental data may not accurately represent real-world disaster scenarios. Additionally, an overly conservative tightening might lead the robot to waste time seeking alternate routes, while too little tightening could place the robot at risk of entrapment. Consequently, there is a need for a systematic approach to assessing the risks and rewards associated with different actions amid uncertainty.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Why is the consideration of risk integral to robotics?", "weight": 1.0} -->

The need for a systematic approach to risk assessment has only increased in recent years due to the ubiquity of autonomous systems that alter our day-to-day experiences and their need for safety, e.g., for self-driving vehicles, mobile service robots, and bipedal robots. These systems are expected to function safely in unpredictable environments and interact seamlessly with humans, whose behavior is notably challenging to forecast. To reason about risk in such settings, the fields of systems science and control engineering have a long history and a rich literature on analyzing and designing systems under uncertainty. Existing methodologies can be broadly classified into the three paradigms of worst-case, risk-neutral, and risk-aware approaches as classified. In the worst-case paradigm, a system's ability to remain safe or perform satisfactorily is judged by examining its most severe safety violation or worst performance. This paradigm forms the basis of robust control and robust safety analysis. For instance, if a system is supposed to track a planned trajectory, the largest discrepancy between the system's realized trajectory and the planned trajectory can serve as a measure of the system's performance.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Why is the consideration of risk integral to robotics?", "weight": 1.0} -->

Contrarily, in the riskneutral paradigm, a system's capacity to stay safe or perform satisfactorily is evaluated on average or probabilistically. 1 This paradigm is often used in stochastic control and reinforcement learning as well as in verification. In the case of trajectory tracking, one would consider the average discrepancy between the system's realized trajectory and the planned trajectory to gauge the system's performance when using a risk-neutral approach. If the system aims to reach a designated target while avoiding an unsafe region, the probability of the system accomplishing these goals can be used to assess the system's performance. However, the worst-case paradigm may result in an overly conservative risk assessment and impractical solutions, while the risk-neutral paradigm can not account for harmful but less likely events. We also note that the developments in the worst-case and the risk-neutral paradigms were often mathematically motivated but not necessarily practically driven as one was able to derive closed-form analytical solutions, e.g., as in linear robust control and linear quadratic control.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Why is the consideration of risk integral to robotics?", "weight": 1.0} -->

The risk-aware paradigm, on the other hand, lies conceptually in between and aims to evaluate a system's performance by giving attention to system outcomes that do not correspond to the worst case or the average. Historically, the risk-aware paradigm has focused on the application of mean-variance approximations, e.g., for controller design, which is derived from the Markowitz model for evaluating the risk of financial portfolios.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Why is the consideration of risk integral to robotics?", "weight": 1.0} -->

A contemporary risk-aware approach that is adopted in this survey to mitigate rare and detrimental outcomes employs the use of tail risk measures, a concept borrowed from financial literature. As such, this survey will introduce these measures and explain their relevance in the context of robotic systems. To preface this explanation, however, we will first provide a deeper overview of the aforementioned paradigms, including an emphasis on the limitations of the worst-case and risk-neutral paradigms, which prompted the rise of risk-aware study.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Why is the consideration of risk integral to robotics?", "weight": 1.0} -->

Benefits of the risk-aware paradigm Many systems are affected by uncertainties that can be well-modeled by random noise. For example, uneven terrain can disturb a robot's planned trajectory, wind can destabilize an aerial vehicle, and smoke can interfere with perception during an autonomous rescue mission. However, designing operating rules to optimize a system's performance on average need not yield trustworthy or reliable performance in practice. For example, consider the disaster scenario presented. The robot must be able to assess risks in debris-laden zones while taking into account uncertainties derived from sensor and state estimation inaccuracies. If the robot operates under a worst-case scenario strategy, it may not find a feasible path through the rubble due to its aversion to any risk. On the other hand, a risk-neutral path-planning approach might expose the robot to unsafe, mission-jeopardizing situations. This example is among the many that underline the limitations of the risk-neutral and worst-case paradigms in the context of robotic applications. Another example is how humans may be risk-averse when collaborating with robots, requiring the robot to interpret the risk-averse human model for successful collaborations.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Why is the consideration of risk integral to robotics?", "weight": 1.0} -->

Case studies from our previous works will be presented later on to further illustrate these points, though we will start by introducing the tail risk measures that have helped foster the more recent, risk-aware paradigm.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Why is the consideration of risk integral to robotics?", "weight": 1.0} -->

1 Note that the probability of an undesirable event can be expressed as the expected value over an indicator function, making probabilistic reasoning conceptually similar to average reasoning.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Why is the consideration of risk integral to robotics?", "weight": 1.0} -->

Tail Risk Measures Succinctly, risk measures are functions over scalar-valued random variables designed to identify characteristics of interest of the random variable in question. By tail risk measures, we imply that the risk measures of interest assess the upper right tail of the distribution of the random variable. Typically, the random variable indicates a cost so that tail risk measures capture the risk of incurring a high cost. Figure 1 depicts a few examples of such tail risk measures, namely, Valueat-Risk, Conditional-Value-at-Risk, and Entropic-Value-atRisk. The Value-at-Risk at level β ∈ corresponds to the cutoff value for which a fraction β of the outcomes of the random variable lies to the right of this cutoff value. A more formal description of these risk measures will follow in the Section 'Tail Risk Measures: Definitions and Nota- tion.' We focus on these measures though as they provide a systematic way of assessing the rare and unsafe (costly) outcomes that must be limited during planning, control, and verification. For example, consider a robot traversing through an environment with uncertain information about the obstacles' positions due to sensor noise.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Why is the consideration of risk integral to robotics?", "weight": 1.0} -->

In this case, we could define a cost random variable by negating the minimum distance to all obstacles. As such, more positive, c.f. more costly outcomes, would correspond to more unsafe behavior as the system is not maintaining the required distance to the measured obstacle. Then, as we have uncertain knowledge of the obstacle's location, we aim to minimize the tail risk incurred by this random cost in an effort to realize safe, risk-aware control actions. This intuitive approach to risk-aware decision selection can be applied to several facets of an autonomy stack, i.e. planning, control, and verification, as has recently been done in both the controls and robotics communities.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Why is the consideration of risk integral to robotics?", "weight": 1.0} -->

Organization As such, this survey serves as an introduction to risk-aware planning, control, and verification in robotics, employing tail risk measures - an emerging field in the literature.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Why is the consideration of risk integral to robotics?", "weight": 1.0} -->

- » A summary of risk measure theory with an emphasis on tail risk measures in the section "Tail Risk Measures: Definitions and Notation". We highlight how these measures offer a consistent and intuitive means to adjust the system's risk aversion levels. - » A discussion on the key principles of risk-aware planning and control, an introduction of the algorithms, and multiple presentations of real-world case studies such as planning and control in subterranean environments. These are covered in the sections "Risk-Aware Planning" and "Risk-Aware Control". - » A review of temporal logics as a mathematical formalism for articulating complex robotic system specifications in the "Verification" section. Additionally, we explore why it is important to consider the tail risk of system trajectories evaluated against these specifications. - » An introduction of a tail risk method for safetycritical controller verification in the "Verification" section. We demonstrate this risk-aware verification approach's ability to effectively identify potential mission issues while validating the probabilistic verification statements made within the described framework. - » We end the survey with open problems and future research directions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Why is the consideration of risk integral to robotics?", "weight": 1.0} -->

Related Work Despite the crucial need for systematic risk evaluation in robotics applications, recent surveys do not emphasize risk-aware planning, control, and verification. For instance, Schwarting, Alonso-Mora, and Rus examine planning and decision-making methods for autonomous driving, Karpas and Magazzeni discuss strategies that enable robots to automatically combine smaller tasks to achieve broader goals, and Brunke et al. outline the interplay between control theory and reinforcement learning for safety in robotic applications. However, these works do not focus on risk measures. Moreover, Hobbs et al. provide a comprehensive introduction to non-stochastic run-time assurance systems, such as a system that overrides an existing controller when an extreme hazard is detected, without an emphasis on risk measures. Two closely related works to our survey are Majumdar and Pavone's and Wang and Chapman's. Majumdar and Pavone propose axioms for risk measures suitable for robots and provide intuitive explanations for these axioms. However, their work does not take the form of a survey and present algorithms for risk-aware planning, control, and verification.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Why is the consideration of risk integral to robotics?", "weight": 1.0} -->

On the other hand, Wang and Chapman overview historical and modern research about risk-aware autonomous systems, but they do not focus on robotics applications, temporal logics, or certain tail risk measures such as entropic valueat-risk and total variation distance-based risk measure. Our survey draws inspiration from Majumdar and Pavone and Wang and Chapman and aims to elucidate the concept of tail risk measures for the control systems community and to showcase their utility for planning, control, and verification of robotic systems. We provide the much-needed emphasis on these risk measures in robotics, helping to ensure that the development and application of autonomous systems remain safe, effective, and mindful of potential risks. As we move on in this survey, we will provide more pointers to relevant literature.

<!-- chunk {"id": "body-0023", "role": "body", "section": "TAIL RISK MEASURES: DEFINITIONS AND NOTATION", "weight": 1.0} -->

A Pedagogical Note on the use of Measure Theory A formal definition of tail risk measures such as Definition 1 to follow, requires some concepts from measure theory, namely distributional equivalence, i.e. d =. As such, we begin this section in a more measure-theoretic context, introducing probability spaces first and defining random variables over these spaces. For readers interested in a deeper study into probability and measure theory, please reference. For those unfamiliar, however, it is sufficient to consider the to-be-mentioned scalar random variables X as functions assigning real numbers to the random outcomes of interest, e.g. the canonical example of assigning the numbers 1 -6 to the corresponding rolls of a sixsided die. Likewise, the distribution P of this random variable X denotes the probability of each sampleable event. Continuing with the six-sided die example and assuming a fair die, the probability of realizing any specific roll - the probability of sampling any number 1 -6 under the random variable X - would all be 1 6. With this intuition, we will begin with a formal definition of tail risk measures.

<!-- chunk {"id": "body-0024", "role": "body", "section": "TAIL RISK MEASURES: DEFINITIONS AND NOTATION", "weight": 1.0} -->

Consider a probability space ( Ω, F, P ), where Ω, F, and P are the sample space, the σ -algebra over Ω, and the probability measure over F, respectively. A random variable X: Ω - → R denotes the cost of each outcome, and X is the set of all such random variables defined on Ω. For any random variable X ∈ X, FX ( x ) refers to the cumulative distribution function with inverse F -1 X ( β ) = inf { x ∈ R | FX ( x ) ≥ 1 -β }. For any two random variables X, X ′ ∈ X, the expression X d = X ′ denotes that the random variables X, X ′ have the same distribution under P. Similarly, we use X ≤ X ′ as a shorthand notation to indicate that X ( ω ) ≤ X ′ ( ω ) for almost all ω ∈ Ω. Finally, U denotes the uniform random variable between.

<!-- chunk {"id": "body-0025", "role": "body", "section": "TAIL RISK MEASURES: DEFINITIONS AND NOTATION", "weight": 1.0} -->

A risk measure ρ is a function that maps a cost random variable to a real number, i.e. ρ: X - → R. Informally, tail risk measures refer to the behavior of the cost X in the tail of its distribution. Mathematically, consider the random variable X ∈ X and the risk-level β ∈. As seen, we define X β to be the tail risk of X such that, In other words, the distribution of the random variable X β is the distribution of X in its β -quantile (or tail) normalized to sum to 1. It is also clear that as β - → 0, X β - → ess sup (X). We are now ready to formally define tail risk measures.

<!-- chunk {"id": "body-0026", "role": "body", "section": "TAIL RISK MEASURES: DEFINITIONS AND NOTATION", "weight": 1.0} -->

Definition 1 (Tail Risk Measures ). For β ∈, a risk measure ρ is a β -tail risk measure (or simply tail risk measure) if ρ ( X ) = ρ ( X ′ ) for all X, X ′ ∈ X satisfying X β d = X ′ β.

<!-- chunk {"id": "body-0027", "role": "body", "section": "TAIL RISK MEASURES: DEFINITIONS AND NOTATION", "weight": 1.0} -->

The aforementioned definition is a formal description of tail risk measures, three of which have featured more prominently in recent literature - Value- at-Risk, Conditional-Value-at-Risk, and Entropic-Value-atRisk. Their definitions will follow.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Value-at-Risk", "weight": 1.0} -->

Chance constraints can be reformulated by a commonly used risk measure called the Value-at-Risk (VaR). For a given confidence level β ∈, VaR β denotes the β -quantile value of the cost variable X and is defined as, Therefore, VaR β (X) = F -1 X (β). It follows that VaR β (X) ≤ 0 = ⇒ P (X ≤ 0) ≥ 1 -β.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Conditional Value-at-Risk", "weight": 1.0} -->

The Conditional Value-at-Risk, CVaR β, measures the expected loss in the β -tail of the random variable X. Formally, for some β ∈ (0, 1] CVaR β is defined as follows per: where we use the notation (X -z) + = max (0, X -z). A value of β ≃ 1 corresponds to a risk-neutral case. A value of β → 0 is rather a risk-averse case 2. Importantly, CVaR is a coherent risk measure (see the text below), 2 Another, more intuitive, way to think about the widely used CVaR metric is that it is the expectation of the random variable X conditioned on X ≥ VaR β (X), i.e., CVaR β (X) = E [X | X ≥ VaR β (X)]. For example, the 5% CVaR risk of a portfolio is equivalent to the expected (mean) return on a portfolio in the worst 5% of scenarios over a specified time horizon (in this definition we assume that X is larger for worse returns). prompting its widespread use in the recent literature. Furthermore, CVaR is a loose upper bound on VaR, i.e.,

<!-- chunk {"id": "body-0030", "role": "body", "section": "Entropic Value-at-Risk", "weight": 1.0} -->

The Entropic Value-at-Risk, EVaR β, derived using the Chernoff inequality for the random variable in question, is the tightest upper bound for VaR and CVaR. It was shown in that EVaR β and CVaR β are equal when VaR t (X) = -∞ for all β < t ≤ 1. For some β ∈ (0, 1], Similar to CVaR β, for EVaR β, the limit β → 1 corresponds to a risk-neutral case; whereas, β → 0 corresponds to a risk-averse case. In fact, it was demonstrated in [87, Proposition 3.2] that lim β → 0 EVaR β (X) = ess sup (X), where ess sup (X) is the essential supremum of the random variable X. Finally, EVaR is also a coherent risk measure and is an upper bound for both VaR and CVaR: EVaR gets its name from its dual representation as a risk measure that provides distributional robustness using relative entropy.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Coherent Risk Measures", "weight": 1.0} -->

Coherent risk measures are a prominent class of risk measures that are well-regarded for their robust mathematical properties, their inherent intuitiveness for risk analysis, and their use in robotics. Introduced by Artzner et al. in the context of financial risk management, coherent risk measures satisfy four axiomatic properties: monotonicity, subadditivity, positive homogeneity, and translational invariance. Monotonicity indicates that adding a less risky outcome to a portfolio should not increase its risk. Subadditivity implies that diversifying a risk portfolio should not increase its overall risk. Positive homogeneity signifies that scaling all outcomes in a portfolio should proportionally scale its risk. Translational invariance denotes that adding a risk-free asset to a portfolio should decrease its risk correspondingly. Coherent risk measures offer a rich theoretical foundation to quantify and manage risk systematically. They enable us to capture extreme, but rare, high-consequence events and provide a mechanism to evaluate and compare different risk scenarios, making them particularly valuable for risk-aware planning, control, and verification in robotics. We are now ready to describe coherent risk measures.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Coherent Risk Measures", "weight": 1.0} -->

Definition 2 (Coherent Risk Measure). We call the risk measure ρ: X → R, a coherent risk measure, if it satisfies the following conditions

<!-- chunk {"id": "body-0033", "role": "body", "section": "Coherent Risk Measures", "weight": 1.0} -->

- » Subadditivity: ρ (X + X ′) ≤ ρ (X) + ρ (X ′), for all X, X ′ ∈ X; - » Translational Invariance: ρ (X + c) = ρ (X) + c for all X ∈ X and c ∈ R; - » Monotonicity: If X ≤ X ′ then ρ (X) ≤ ρ (X ′) for all X, X ′ ∈ X; - » Positive Homogeneity: ρ (β X) = βρ (X) for all X ∈ X and β ≥ 0.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Coherent Risk Measures", "weight": 1.0} -->

Note that the properties of subadditivity and positive homogeneity together imply that coherent risk measures are also convex. CVaR and EVaR have been recognized as coherent risk measures. Conversely, VaR does not qualify as a coherent risk measure, as it does not satisfy the subadditivity property. This fact limits its utility in situations where a joint assessment of risks is required, which is often the case in risk-aware robotic planning, control, and verification. While VaR is not a coherent risk measure, each of the measures defined above has its place in risk evaluation, depending on the specific requirements and constraints of the task at hand.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Coherent Risk Measures", "weight": 1.0} -->

Coherent risk measures can also be written as the worstcase expectation over a convex and closed set of probability mass (or density) functions. This distributionally-robust representation of coherent risk measures is defined below.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Coherent Risk Measures", "weight": 1.0} -->

Definition 3 (Representation Theorem). Every coherent risk measure can be represented in its dual form as, where the ambiguity set (or risk envelope), Q, is convex and closed, and probability density function Q (X) is absolutely continuous with respect to the probability density function P (X); i.e., P (X) = 0 = ⇒ Q (X) = 0.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Coherent Risk Measures", "weight": 1.0} -->

Remark 1. In this review, we limit our focus to tail risk measures for robotics but we note that distributionally-robust optimization is another widely used measure of risk. Some tail risk measures, like CVaR and EVaR, may have a distributionally-robust interpretation as well. Some methods that consider distributionally-robust formulations of tail risk measures are also discussed in this review.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Coherent Risk Measures", "weight": 1.0} -->

Coherent risk measures provide a snapshot of potential perils based on current conditions. These measures fall short when applied to dynamic systems, such as those common in robotics, where risks and conditions vary with time. Dynamic coherent risk measures extend beyond the static approach, taking into account the time-varying nature of risk. They are particularly adept at characterizing the evolving risk landscape in dynamic environments. Dynamic risk measures continuously monitor and update risk assessments in response to changes in the system and its environment. This capability to adapt and provide a comprehensive understanding of risk in a fluctuating context aligns well with the realities of robotic operations in unstructured environments.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Coherent Risk Measures", "weight": 1.0} -->

To define these measures, we will first index a sequence of random variables Xt, t = 0,..., N, where N ∈ N ≥ 0 ∪{ ∞ }. Note that prior, each random variable X was defined over a corresponding probability space, and X denoted the set of all random variables defined over that space ( Ω, F, P ). However, in the dynamic context, each sequenced random variable Xt belongs to (perhaps) different spaces of random variables X t. As such, denote X t: N = X t × · · · × X N as the space in which the corresponding sequence Xt: N lives and X = X 0 × X 1 × · · ·. Finally, we assume that the sequence X ∈ X is almost surely bounded (with exceptions having probability zero), i.e., max t ess sup | Xt ( ω ) | < ∞.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Coherent Risk Measures", "weight": 1.0} -->

To describe how one can evaluate the risk of subsequence Xt,..., XN from the perspective of stage t, we require the following definitions.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Coherent Risk Measures", "weight": 1.0} -->

Definition 4 (Conditional Risk Measure). A mapping ρ t: N: X t: N → X t, where 0 ≤ t ≤ N, is called a conditional risk measure, if it has the following monoticity property: Definition 5 (Dynamic Risk Measure). A dynamic risk measure is a sequence of conditional risk measures ρ t: N: X t: N →X t, t = 0,..., N.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Coherent Risk Measures", "weight": 1.0} -->

Akey attribute of dynamic risk measures is their temporal consistency [93, Definition 3]: if two scenarios X and X ′ are identical for a time interval [ τ, θ ], and if X is evaluated to be as favorable as X ′ at some future time point θ, then it stands to reason that X should not be viewed as more risky than X ′ at the earlier time point τ. This principle ensures that the risk assessment remains coherent and consistent across different points in time. The definition of a dynamic coherent risk measure [94, p. 298] then follows from its static counterpart.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Coherent Risk Measures", "weight": 1.0} -->

Definition 6 (Dynamic Coherent Risk Measure). We call the one-step conditional risk measures ρ t: X t + 1 → X t, t = 1,..., N -1 a coherent risk measure if it satisfies the following conditions

<!-- chunk {"id": "body-0044", "role": "body", "section": "Coherent Risk Measures", "weight": 1.0} -->

- » Translational Invariance: ρ t (X + X ′) = X + ρ t (X ′) for all X ∈ X t and X ′ ∈ X t + 1; - » Monotonicity: If X ≤ X ′ then ρ t (X) ≤ ρ t (X ′) for all X, X ′ ∈ X t + 1; - » Positive Homogeneity: ρ t (β X) = βρ t (X) for all X ∈ X t + 1 and β ≥ 0.

<!-- chunk {"id": "body-0045", "role": "body", "section": "AN OVERVIEW OF TAIL RISK MEASURES IN ROBOTICS", "weight": 1.0} -->

The definitions of the prior section now permit us to provide a general overview of how tail risk measures are used to generate risk-aware behavior or validate systems in a risk-aware setting. For such an overview, let us define ρ to be a risk measure that maps a random variable X to a real number that indicates the risk associated with X. For applications in robotics, this random variable X denotes any random cost associated with (perhaps) stochastically evolving system trajectories. To be more specific, consider a (perhaps) nonlinear discrete-time control system at time t with state x (t) ∈ X ⊆ R n, input u (t) ∈ U, and system disturbances d (t) ∼ ξ (x (t), u (t), t) where ξ (x (t), u (t), t) is a (perhaps) state, input, and time-dependent probability distribution over R n: Given a feedback controller U: X → U, which prescribes u (t) = U (x (t)), we can construct a closed-loop, stochastically evolving dynamical system.

<!-- chunk {"id": "body-0046", "role": "body", "section": "AN OVERVIEW OF TAIL RISK MEASURES IN ROBOTICS", "weight": 1.0} -->

To be clear, we first define S X as the set of all signals mapping time to the state space X, e.g. S X = { s: Z → X}. As such, provided an initial condition x 0 ∈ X, this feedback controller U, and a randomly sampled disturbance sequence { d, d,... }, the corresponding state trajectory x = { x = x 0, x,... } following the update in is a signal that lives in S X, i.e. x ∈ S X. Notably, this trajectory x is also a randomly sampled trajectory conditioned on the initial state x 0 due to the randomly sampled disturbance sequence. To be more specific in a tail-risk context then, we define Σ (x 0) as the random variable conditioned on the initial condition x 0 whose samples are these random trajectories x living in S X, i.e., To analyze the tail risk of this trajectory random variable Σ (x 0), we require a mapping from trajectory samples x to the real line: The function C may denote the inverse distance of a robot's trajectory to an obstacle and thereby encode the system's robustness to a collision.

<!-- chunk {"id": "body-0047", "role": "body", "section": "AN OVERVIEW OF TAIL RISK MEASURES IN ROBOTICS", "weight": 1.0} -->

These cost functions can be constructed from principled approaches when the system's desired behavior is expressed as a temporal logic specification. Applying this cost C to the random variable corresponding to system trajectories Σ (x 0) defines the scalar random variable X over which we can apply our tail risk measure ρ, i.e. X = C (Σ (x 0)). For robotic planning, control, and verification, one can then minimize the risk of this cost, ρ (X), or consider using risk as a constraintρ (X) ≤ r for a risk threshold r.

<!-- chunk {"id": "body-0048", "role": "body", "section": "AN OVERVIEW OF TAIL RISK MEASURES IN ROBOTICS", "weight": 1.0} -->

In what follows, we present the two main sections 'Risk-Aware Planning and Control' and 'Risk-Aware Verification and Validation', in this order. We chose this specific organization as planning and control synthesis is usually carried out by making simplifying assumptions on the system and by considering low-fidelity models. The design using low-fidelity models is motivated by the complexity of the problem and computational considerations. The designed planners and controllers are hence not guaranteed to be correct for high-fidelity models or real robotic systems, emphasizing the need for system verification and validation techniques that apply in realistic settings.

<!-- chunk {"id": "body-0049", "role": "body", "section": "RISK-AWARE PLANNING AND CONTROL", "weight": 1.0} -->

The robotic behavior, motion planning, and control problems focus on designing algorithms that allow a robot to interact intelligently and safely with its surroundings. This complex process involves deciding on possible actions, constructing trajectories that a robot can take to achieve specific high-level goals, e.g., safely navigating through unstructured environments, and controlling the instantaneous robot motions to track the trajectory. Behavior planning concerns the higher-level decision-making needed to achieve higher-level robot objectives, while motion planning plans the details of robot movement, determining how a robot should move from one location to another while avoiding obstacles, and factoring in the robot's kinematics and dynamics. The control level manages the details of motion execution by continually computing the system control inputs that minimize tracking error while accounting for uncertainty and unexpected events.

<!-- chunk {"id": "body-0050", "role": "body", "section": "RISK-AWARE PLANNING AND CONTROL", "weight": 1.0} -->

The process of designing robot plans and controls should critically consider potential risks and their overall system implications. These risks include physical risks to humans close to a robot as well as risks to the robot itself due to its unpredictable environment and imperfect robot sensing and perception systems. Notions of risk are particularly important in high-stakes robot tasks, such as search and rescue, or exploration of hazardous sites. To properly manage these risks, this paper advocates for the use of tail risk measures. Importantly, tail risk measures focus on more extreme but rarer events, and thus provide a systematic and principled approach to quantifying and managing risk in robotics. Integrating tail risk measures into robotic planning and control modules can lead to more robust and safer robot operation, effectively balancing performance and safety under uncertainty.

<!-- chunk {"id": "body-0051", "role": "body", "section": "RISK-AWARE PLANNING AND CONTROL", "weight": 1.0} -->

Historical Remark on Exponential Utility: (This remark is adapted.) Risk-aware control has been in development for at least fifty years. The earliest contributions concern the exponential utility measure (i.e., entropic risk measure): where θ = 0 is a risk parameter and X is a nonnegative random variable, which can be interpreted as a meanvariance approximation. When θ < 0, the robotic system is risk averse, while the robot will exhibit more risk tolerant behavior when θ > 0. When θ = 0, the system is risk neutral. Notably, the exponential utility is not a tail risk measure. To our knowledge, the first paper in the area of risk-aware control was a 1972 study about finite-state Markov decision processes by Howard and Matheson, in which performance was assessed by an exponential utility criterion. The authors took inspiration from game theory. One year later, Jacobson investigated the exponential utility criterion in the classical linear-quadratic setting (linear dynamics, quadratic costs, Euclidean spaces, and additive Gaussian noise).

<!-- chunk {"id": "body-0052", "role": "body", "section": "RISK-AWARE PLANNING AND CONTROL", "weight": 1.0} -->

Whittle developed key contributions regarding risk-aware control in the linearquadratic setting using the exponential utility measure, including showing close analogies to optimal control and state estimation results in the risk-neutral case. While exponential utility continues to be investigated (e.g., see), recent attention focuses on different types of risk-aware performance and safety criteria, motivating this survey on tail risk.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Risk-Aware Behavior Planning", "weight": 1.0} -->

Behavior planning for robotics has been studied in many mathematical frameworks, though the most commonly utilized framework has been to reframe planning as a (partially observed) Markov Decision Problem (PO)MDP, which we will discuss in this section. Specifically, an MDP is a triple 3, where X = { x 1,..., x |X |} represents the states of the autonomous agent(s) and the world model, U = { u 1,..., u |U|} represents the actions available to the agent, and T (xj | xi, u) defines the likelihood of transitioning to state xj from state xi when taking action u ∈ U. Furthermore, the transition function must be such that: As such, risk-aware behavior planning aims to construct a policy π that minimizes a risk-measure evaluation over either each state or over some time-horizon of states. Specifically, consider a cost c associated with transitioning from an initial state x 0 via taking an action u to a final state x f, i.e. c: X × U × X → R where c (x 0, u, x f) denotes the cost of the action-specific transition.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Risk-Aware Behavior Planning", "weight": 1.0} -->

As state evolution for an MDP is stochastic, the exact cost of an action is unknown apriori as the final state x f will be a sample from a random variable Xf (x 0, u) conditioned on the initial state and action choice with distribution provided by the and for a finite Markov Decision Process, the state and action spaces must also be finite. Finally, a policy π maps states to actions, i.e. π: X → U.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Risk-Aware Behavior Planning", "weight": 1.0} -->

3 Here, we note that MDPs are typically defined with an associated objective function, and we will define one for risk-aware behavior planning in a section to follow. transition function T. As a result, the corresponding cost of an initial state and action pair is a scalar random variable corresponding to the costs of the random final state samples, i.e. C (x 0, u) = c (x 0, u, Xf (x 0, u)). As such, the one-step optimal policy is to choose actions per state that minimize the tail-risk ρ associated with this cost random variable C (x 0, u), i.e.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Risk-Aware Behavior Planning", "weight": 1.0} -->

We could similarly define policies by considering not just the one-step risk, but the risk over a horizon. To do so, we note that for any horizon length T ∈ { 1, 2,... } ≜ = Z +, an initial state x 0, and a policy π, the state evolution S = { x 0, x 1,..., xT } is random due to probabilistic state transitions. Then provided a similar sequence of risk measures ˆ ρ T = { ρ i } T -1 i = 0, we can define a cost function J corresponding to sequential risk evaluations of each cost random variable over the state horizon, with perhaps some discount factor γ ∈ (0, 1]: Here, we note that while we have defined the interior states x 1, x 2,..., xT -1, they are random based on the probabilistic transitions from the previous state and the provided action. As such, this randomness must be accounted for during risk-measure evaluation, resulting in the nested risk measures in the cost above.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Risk-Aware Behavior Planning", "weight": 1.0} -->

Similarly then, the optimal policy minimizes this cost: Finally, for γ < 1 this is called the discounted MDP problem, for γ = 1 this is called the un-discounted MDP problem, and for either case where T → ∞ this is called the infinitehorizon MDP problem, all of which have been applied to risk-aware behavior planning as will be discussed in the sections to follow.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Risk-Aware Behavior Planning", "weight": 1.0} -->

The last extension on the MDP framework concerns the case where the state is not exactly known, i.e. the system is partially observed at every time step, and as such, we do not know the exact state the system occupies. Rather, we have a belief, a probability distribution, over the states which encodes our understanding of where the system is at any given time. We'll refrain from rigorously defining this Partially Observable Markov Decision Problem (POMDP) as, at a high level, the policy selection pursuit is similar in spirit to what was shown in the prior two optimization problems (for more information on POMDPs though, please reference ). The primary change arises in the consideration of the distribution over states when accounting for risk, whereas the state was known exactly in the prior, MDP case.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Examples", "weight": 1.0} -->

Perhaps the most prevalent use of (PO)MDPs in planning arises in navigation problems wherein the finite (PO)MDP states correspond to a discretization of the robot's state space X into a finite set, e.g. discrete cells on a 2-d grid for planar navigation, combined with the enumeration of a finite list of environmental phenomena, e.g. the occupancy values of those same grid cells. Actions then correspond to a minor navigation task, e.g. moving from one discretized grid cell in the state space to another discretized grid cell. Finally, stochasticity between these transitions arises as either the environmental phenomena is partially observed and might frustrate the immediate application of the minor navigation action, faulty sensors causing some drift in the robot's ability to directly achieve the minor navigation task, etc. Then, the goal is to identify an optimal policy against a risk measure, typically VaR or CVaR. Indeed, this paradigm underlies many works in this vein, a sampling of which is provided here and in the citations within.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Examples", "weight": 1.0} -->

These works are by no means exhaustive, however, and due to the prevalence of MDPs for behavior planning, both control theorists and roboticists alike have also progressed fundamental research in (PO)MDPs in pursuit of advancements in robotic behavioral path planning. A discussion on those advancements will follow.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Examples", "weight": 1.0} -->

Prior Work on Discounted MDPs: In an early work in this vein, the authors of presented techniques for incorporating this measure into dynamic programming. This work resulted in a wave of new work evaluating risk measures in dynamic programming problems. For example, in the authors identified locally optimal solutions via gradient descent, to MDP problems with CVaR constraints and total expected costs. Notably, provides a convergence guarantee whereas does not. The authors of extended these prior notions by developing sample-based saddle point algorithms to identify policies for MDPs whose cost is a coherent risk measure, though not specifically CVaR. Other relevant works include.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Examples", "weight": 1.0} -->

One question posed by the authors in has caused a renewal of work in this vein. Specifically, the authors show that most risk-level dynamic programs cannot guarantee the recovery of a globally optimal value function despite discretized state space. To partially address that concern, in the authors generate optimal risk-aware policies for MDPs with dynamic coherent risk objectives and constraints. By phrasing policy generation as a difference convex program, solutions can also be rapidly identified. Despite these advances, the field of risk-aware discounted MDPs still holds numerous avenues for future exploration. New algorithms and techniques that can handle an expansive range of coherent risk measures and can effectively manage constraints in MDPs are needed.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Examples", "weight": 1.0} -->

Prior Work on POMDPs: While POMDPs can be difficult to design and solve, significant strides have been made in addressing coherent risk measure objectives. For instance, explored POMDPs with coherent risk measure objectives. However, their noteworthy theoretical contributions fell short of providing a computational method for designing policies applicable to general coherent risk measures. Ahmadi et al. aimed to address this gap by proposing a method for finding finite-state controllers for POMDPs with objectives defined in terms of coherent risk measures. Their novel approach took advantage of convex optimization techniques, showcasing the potential of mathematical optimization in policy design. Nevertheless, their method has its limitations: it can only be applied when the risk transition mapping is affine in the policy.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Examples", "weight": 1.0} -->

Recognizing this limitation, Ahmadi et al. extended their prior work to incorporate a broader set of coherent risk measures. They proposed an innovative approach bounded policy iteration method that identifies finite-state risk-averse policies. This methodology breaks the problem down into manageable pieces, tackling convex optimization problems at each policy iteration step. This approach substantially ameliorates the computational tractability of synthesizing risk-averse policies for POMDPs. By iteratively solving these convex optimization problems, the policy synthesis process becomes markedly more feasible.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Examples", "weight": 1.0} -->

However, the methodology outlined in has its limitations. One notable constraint is that the technique can currently only be applied to problems involving hundreds of states due to the computational limitations inherent to convex optimization. Despite existing limitations, the exploration of POMDPs in the context of coherent risk measures presents a promising field of study. As our understanding deepens and computational methods evolve, we can anticipate the development of more pragmatic solutions for planning under uncertainty under a broader range of coherent risk measures.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Risk-Aware Motion Planning and Control", "weight": 1.0} -->

The behavior planning layer as described in the previous section is only the top layer of most controllers. Below this layer, controllers typically comprise of a motion planning layer translating the broken-down behavior into a lowerlevel sequence of commands which are then tracked by the lower-level controller. This section will detail risk-aware work done on the remaining two layers - motion planning and control. Optimization-based motion planning methods are increasingly popular because they provide optimized system behaviors that respect the system's dynamics, while readily incorporating state and control constraints. Critically, one must account for sudden system changes or disturbances to ensure system safety. Risk-awareness methods can be integrated into optimal planning control problems.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Risk-Aware Motion Planning and Control", "weight": 1.0} -->

Our risk-aware motion planning review considers discrete-time controlled stochastic systems, with the form: Here, x (t) ∈ R nx and u (t) ∈ R nu are the system state and controls at time t, respectively. The system is affected by a stochastic process noise d (t) ∈ R nd and f: R nx × R nu × R nd → R nx. An optimization-based planner seeks to minimize a system cost J (x, u) ∈ R for initial condition x = x 0 at time t = 0. The optimal controller U = [u,...,

<!-- chunk {"id": "body-0068", "role": "body", "section": "Risk-Aware MPC", "weight": 1.0} -->

Model Predictive Control (MPC) applies the finite-horizon controller in a receding-horizon fashion. Uncertainty can arise for many reasons. Uncertainty in the robot's dynamics model causes the true system motion to differ from the predicted one. Such effects are typically accounted for via process noise, d ( t ). Sensor noise and imprecise robot localization or estimation of environment states are other common sources of uncertainty. There are many ways to account for these uncertainties in an MPC framework. For example, Robust MPC accounts for worst-case disturbances in a set of bounded uncertainties. Robust approaches are often too conservative because they focus on worst-case events. Conversely, stochastic MPC only accounts for the average realization of the cost while respecting a bound on the probability of violating the state and control constraints, see Sidebar 1. The resulting policy, which is often too optimistic, minimizes the MPC objective in expectation instead of usefully accounting for events in the tail of the uncertainty distribution.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Risk-Aware MPC", "weight": 1.0} -->

Risk-aware MPC optimizes risk-averse behavioral policies: they are not as conservative as in the robust case. But since they account for 'risky' outcomes in the tail of the uncertainty distribution, they perform better in practice. In, the authors provide an MPC scheme for a discrete-time dynamical system with process noise whose objective was a Conditional Value-at-Risk (CVaR) measure. They further provided new Lyapunov conditions for risk-sensitive exponential stability. In, the authors devised an MPC scheme that expressed a distributionallyrobust chance constraint along with a risk-aware cost in terms of a CVaR reformulation. Optimal control using distributionally-robust CVaR constraints with secondorder moment ambiguity sets is posed as a semidefinite program. A tree-based approach for MPC that enumerates all possible extreme disturbance signals and searches for feedback policies that account for a tradeoff between robustness and performance through CVaR metrics was proposed. In, the authors considered multistage risk-averse and risk-constrained optimal control for general coherent risk measures with conic representations.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Risk-Aware MPC", "weight": 1.0} -->

A sampling-based approach, using model predictive path integral, to solve nonlinear, optimal control problems using CVaR risk constraints was considered. Other sampling-based approaches to solving the optimal control problem with state estimation uncertainty involve using a robust version of the RRT ∗ algorithm.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Risk-Aware MPC", "weight": 1.0} -->

Data-driven MPC that uses samples from the uncertainty distribution is becoming increasingly popular. Riskaware MPC approaches provide the required robustness to account for the gap between enforcing the sample-based chance constraints for the empirical distribution and the true chance constraint for the actual uncertainty distribution. In the authors propose a distributionallyrobust data-enabled predictive control (DeePC) algorithm, that uses finite samples of an unknown system to make trajectory predictions. Instead of learning the system dynamics model, the authors propose an equivalent formulation using these data-driven trajectory predictions that enjoys strong out-of-sample guarantees using Wasserstein distributionally-robust CVaR constraints. Reference considers a learning MPC framework whose infinite horizon, CVaR-constrained, optimal control solution is approximated iteratively given a finite number of safe states and uncertainty samples. Through this iterative method, the authors construct a data-driven terminal set for distributionally-robust CVaR-constrained iterative MPC with safety and feasibility guarantees.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Risk-Aware MPC", "weight": 1.0} -->

MPC is also useful for obstacle avoidance in motion planning tasks. Risk-aware MPC accounts for varied obstacle behaviors and sensor and process noise not limited to Gaussian distributions. The MPC scheme in avoids moving obstacles using a CVaR risk metric. Similar results were obtained in on the Entropic Value-at-Risk (EVaR) metric for obstacle avoidance with additional guarantees of recursive feasibility and finite-time task completion while following a set of waypoints. In, these results were extended to general coherent risk measures for systems with process noise to obtain a disturbance feedback policy. The authors propose various constraint-tightening techniques to make the risk-aware obstacle avoidance MPC computationally tractable for motion planning while providing probabilistic guarantees on recursive feasibility and task completion in finite time. A risk-constrained MPC formulation was also studied in wherein the authors computed a risk map for traversing over rough terrain using CVaR. They incorporated this CVaR terrain map into MPC constraints to account for obstacles and terrain hazards. All of the above methods, including the formulation presented in Sidebar 1, consider pointwise-intime constraints for safety.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Risk-Aware MPC", "weight": 1.0} -->

Instead the authors of consider a CVaR-based optimal control formulation for obstacle avoidance such that the risk constraints hold for the entire trajectory by accounting for the time-wise supremum safety cost inside the CVaR risk.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Risk-Aware MPC", "weight": 1.0} -->

Sidebar 1 (Model Predictive Control with Uncertainty). Consider a linear, discrete-time system given by where x (t) ∈ R nx and u (t) ∈ R nu are the system state and controls at time t, respectively. The system is affected by a stochastic, additive, process noise d (t) ∈ R nd. Consider rx state constraints of the form while minimizing the control effort and deviation from the desired trajectory, i.e., we want to minimize the following cost: where Q ∈ R nx × nx and R ∈ R nu × nu are weights on the state and control costs. Model Predictive Control (MPC) provides an optimization-based framework to compute the best N-step control input while satisfying the state and control constraints. The MPC optimization is given, where, x k | t is the state at time k as predicted at the time t while starting from the current state x t | t = x (t) and β is the user chosen risk level.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Risk-Aware MPC", "weight": 1.0} -->

Uncertainty is propagated through the states as, If the uncertainty is i.i.d Gaussian with d (t) ∼ N (0, Σ), the states x (t) are also Gaussian x k + 1 | t ∼ N (ˆ x k | t, Σ k | t) where, ˆ x k | t = A k x t | t + ∑ k i = t A (k -i) B u i | t and Σ k | t = ∑ k i = t D T A (k -i) T Σ A (k -i) D (the family of normal distributions is closed under linear transformations). Hence, we can rewrite the above uncertain MPC optimization as the following deterministic quadratic program, However, if the uncertainty distribution is non-Gaussian, the uncertain MPC is not easily reformulated into a convex optimization program. In this case, one possible solution is to sample the uncertainty distribution and reformulate the MPC optimization as a much more computationally expensive mixed-integer program. Many tail risk measures such as CVaR and EVaR, provide intuitive convex, inner approximations of chance constraints regardless of the uncertainty distribution.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Risk-Aware MPC", "weight": 1.0} -->

Hence, we propose risk-aware MPC formulations not only better account for uncertainty but also provide an efficient convex reformulation without making assumptions about the nature of the uncertainty. The resulting deterministic, risk-aware MPC formulation is given,

<!-- chunk {"id": "body-0077", "role": "body", "section": "Risk-Aware Safety-Critical Control", "weight": 1.0} -->

In the previous subsections, we considered behavior and motion planning algorithms through the lenses of a riskaware approach. Risk-aware feedback control methodologies, like the MPC techniques discussed in the previous subsection, can strike a balance between worst-case and nominal operating conditions and thus account for rare events by enhancing robustness while achieving high performance under nominal operation. Additionally, we must also consider risk with a view to safety-critical autonomous systems, such as those found in aerospace and humanrobot applications. The specific risks here are often associated with the uncertainty of modeling intricate nonlinear dynamics, e.g. bipedal robots, and/or sensing extreme unstructured environments, e.g. subterranean or extraterrestrial exploration. Safety in the feedback control layer is often formulated in terms of set-theoric properties of dynamical systems, e.g., reachability and invariance. Safety verification then involves ensuring that system solutions stay within a predefined safe set or, conversely, steer clear of a predetermined unsafe set. A common technique for this is to calculate the reachable set of a system under disturbances and controls.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Risk-Aware Safety-Critical Control", "weight": 1.0} -->

Yet, for intricate, high-dimensional systems, these methods may be impractical or excessively conservative.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Risk-Aware Safety-Critical Control", "weight": 1.0} -->

Historically, alternative methods for assessing reachability trace back to Nagumo's seminal research on the set invariance of ordinary differential equations (ODEs). This work was later expanded to include ODEs with inputs by Aubin and others, under the framework of viability theory. The rise of interest in hybrid systems in the 2000s led to the development of barrier certificates for safety verification. The creation of these certificates, however, involves solving complex polynomial optimization problems that are challenging for high-dimensional systems, despite some progress made in the last decade. The newer concept of barrier functions offers a solution to the computational difficulties faced by barrier certificates. These functions can be formulated directly from the safe set's definition, simplifying the process. Utilizing this attribute, barrier functions have been effectively applied to design safe controllers (without an existing controller) and safety filters (with an existing controller) for dynamic systems like biped robots and trucks. These applications have demonstrated assured performance and robustness.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Risk-Aware Safety-Critical Control", "weight": 1.0} -->

Conditional Value-at-Risk is a useful measure for assessing how far a realized trajectory may deviate from a safe region of operation. Defining safety in terms of CVaR is well-motivated when constraint violations may be unavoidable: the magnitude of the risk should be minimized during the undesired excursion. Sets of initial conditions whose safety is characterized by motions of CVaR can be estimated using dynamic programming. Pointwise CVaR constraints have also been studied. The problem of optimizing the CVaR of a maximum random cost has been studied in different settings, such as deriving an upper bound approximation, a finite-horizon solution, and an infinite-horizon solution.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Risk-Aware Safety-Critical Control", "weight": 1.0} -->

Safety requirements can also be encoded and enforced via Control Barrier Functions (CBFs), which were proposed. CBFs have been used to design safe controllers for continuous-time dynamical systems, such as bipedal robots and trucks, with guaranteed robustness (see the survey and references therein). For discrete-time systems, discrete-time barrier functions were formulated in and applied to multi-robot coordination. For a class of stochastic (Ito) differential equations, safety in probability and statistical mean was studied in via stochastic barrier functions.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Risk-Aware Safety-Critical Control", "weight": 1.0} -->

The first attempt to formulate risk-aware control barrier functions was carried out, wherein the authors proposed CVaR control barrier functions as a composition of a dynamic CVaR metric with a CBF to study safety, in the CVaR sense, for a discrete-time dynamical system subject to stochastic uncertainty. A computational method based on difference convex programs (DCPs) was also proposed in order to synthesize CVaR-safe controllers. The method was applied to collision avoidance scenarios involving a bipedal robot subject to modeling uncertainty. The CVaR control barrier functions were generalized to risk-aware control barrier functions (RCBFs) with general coherent risk measures, where it was shown that the existence of such barrier functions implies invariance in a coherent risk sense. Furthermore, conditions were proposed based on finite-time RCBFs to guarantee finite-time reachability to a desired set. In recent work, sampling-based under-approximations of the CVaR for belief states were used to define risk CBFs.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Risk-Aware Safety-Critical Control", "weight": 1.0} -->

Sidebar 2 (Risk-Aware Control Barrier Functions). Consider a discrete-time stochastic system given by where at time t ∈ N ≥ 0, x (t) ∈ X ⊂ R n is the state, u (t) ∈ U ⊂ R m is the control input, d (t) ∈ D is the stochastic uncertainty/disturbance, and f: R n ×U × D → R n. We assume that the initial condition x 0 is deterministic and that |D| is finite, i.e., D = { v 1,..., v |D|}. At every time step t, for a state-control pair (x (t), u (t)), the process disturbance d (t) is drawn from set D according to the probabilities p = [p 1,..., p |D|] T, where pi: = P (d (t) = vi), i = 1, 2,..., |D|.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Risk-Aware Safety-Critical Control", "weight": 1.0} -->

Note that the probability mass function for the process disturbance is time-invariant, and that the process disturbance is independent of the process history and of the state-control pair (x (t), u (t)). Note that, in particular, system can capture stochastic hybrid systems, such as Markovian Jump Systems.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Risk-Aware Safety-Critical Control", "weight": 1.0} -->

In risk-aware safety analysis, we are interested in studying the properties of the solutions to with respect to the compact set S described: where h: X → R is a continuous function.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Risk-Aware Safety-Critical Control", "weight": 1.0} -->

In the presence of stochastic uncertainties d, assuring almost sure (with probability one) invariance or safety may not be feasible. Moreover, enforcing safety in expectation is only meaningful if the law of large numbers can be invoked and we are interested in the long-term performance, independent of the actual fluctuations. RCBFs focus on safety in the dynamic coherent risk measure sense with conditional expectation as a special case, allowing for more robust measures of safety.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Risk-Aware Safety-Critical Control", "weight": 1.0} -->

Definition 7 (ρ -Safety). Given a "safe set" S in and a time-consistent, dynamic coherent risk measure ρ 0: t, the solutions to, starting at x 0 ∈ S, are ρ -safe if and only if When x 0 ∈ X \ S, we often want to know if S can be reached in finite time.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Risk-Aware Safety-Critical Control", "weight": 1.0} -->

Definition 8 (ρ -Reachability). Consider system with initial condition x 0 ∈ X \ S. Given a set S as in and a time-consistent, dynamic coherent risk measure ρ 0: t, S is ρ -reachable if and only if there exists a constant t ∗ such that Definition 9 (Risk-Aware Control Barrier Function). For the discrete-time system and a dynamic coherent risk measure ρ, the continuous function h: R n → R is a riskaware control barrier function (RCBF) for the set S as defined, if there exists a convex classK function α 4 satisfying α (r) < r for all r > 0 such that In, the authors demonstrated that the existence of an RCBF implies invariance/safety in the coherent risk measure.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Risk-Aware Safety-Critical Control", "weight": 1.0} -->

Theorem 1. For discrete-time system and the set S as described, let ρ be a coherent risk measure. Then, S is ρ -safe if there exists an RCBF as defined in Definition 9.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Risk-Aware Safety-Critical Control", "weight": 1.0} -->

Note that the most common choice for function α is a constant α = α 0, where α 0 ∈, as α 0 r < r, ∀ r > 0. To study risk-aware reachability, we require the following.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Risk-Aware Safety-Critical Control", "weight": 1.0} -->

Definition 10 (Finite-Time RCBF). For discrete-time system and dynamic coherent risk measure ρ, the continuous function h: X → R is a fi nite-time RCBF for set S, as defined 4 A classK function is a continuous, scalar function α (r) defined for r ∈ [0, a) that is strictly increasing and satisfies α = 0., if there exist constants 0 < γ < 1 and ε > 0 such that ρ (h (x (t + 1))) -γ h (x (t)) ≥ ε (1 -γ), ∀ x (t) ∈ X.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Risk-Aware Safety-Critical Control", "weight": 1.0} -->

It was also shown in that the existence of a finitetime RCBF implies ρ -reachability.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Risk-Aware Safety-Critical Control", "weight": 1.0} -->

Theorem 2. Consider the discrete-time system and a dynamic coherent risk measure ρ. Let S ⊂ X be as described. If there exists a finite-time RCBF h: X → R as in Definition 10, then for all x ∈ X \ S, there exists a t ∗ ∈ N ≥ 0 such that S is ρ -reachable, i.e., inequality holds. Furthermore, where the constants γ and ε are as defined in Definition 10.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Case Study: Risk-Aware Robotic Motion Planning in Subterranean Environments", "weight": 1.0} -->

This case study looks at a hierarchical risk-aware traversability and planning methodology that can be used for autonomous robot (legged or wheeled robot) traversal over extreme terrain, as motivated by the DARPA Subterranean challenge. This is the first framework to integrate a CVaR-based risk-aware planning and control pipeline onto a fully autonomous robotic system. We briefly describe the risk-aware traversability and planning pipeline below.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Case Study: Risk-Aware Robotic Motion Planning in Subterranean Environments", "weight": 1.0} -->

We first need to interpret which parts of the environment the robot can traverse. Evaluation of a natural terrain's traversability is difficult due to uncertainties arising from sensor noise and robot localization errors. Furthermore, there are multiple sources of terrain hazards such as steep slopes, loose surface material, sudden elevation drops, and physical obstacles. To account for these different sources of uncertainty systematically, we evaluate the conditional value-at-risk of the terrain hazards to obtain a risk map that can be used in the planning and control pipeline. The traversability estimate is given by the random variable R that is constructed jointly from the grid map of the terrain, the robot state, and the applied control, see for details on how to construct the map and associated traversability estimate. R provides a cost of traversing over each grid point on the terrain that we use to assess the CVaR value. This CVaR risk evaluation, CVaR β ( R ), enables a robot engineer to define the allowable traversability risk level based on the mission criteria.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Case Study: Risk-Aware Robotic Motion Planning in Subterranean Environments", "weight": 1.0} -->

Furthermore, one can dynamically adjust the risk level, β, online based on 1) the mission-level states, i.e., based on the robot's capabilities and the environment, and 2) whether the robot is stuck in a situation wherein there is no feasible path and decreasing the risk-level (and consequently being less conservative) might allow the robot to find a feasible, but possibly riskier path. The geometric planner and the kinodynamic MPC controller then utilize the risk evaluation, CVaR β ( R ), to obtain a riskaware control policy.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Case Study: Risk-Aware Robotic Motion Planning in Subterranean Environments", "weight": 1.0} -->

After computing the risk-aware traversability cost, the authors utilize this cost for high-level geometric path planning using an A* algorithm to obtain waypoints for navigation. This risk-aware geometric planner uses the dynamic risk measure in the cost of the geometric planner optimization. The waypoints are then passed into an MPC optimization with CVaR constraints for safety for generating obstacle-free trajectories. The statistical performance of the aforementioned risk-aware controllers is evaluated in simulation with randomly generated environment maps and goals. This study illustrates the trade-off between the risk taken by the robot to reach the goal versus the total distance traversed by the robot for different allowable risk levels, β (see Figure 4). When β → 1 (or α → 0), the framework is risk-neutral and mimics the deterministic setting, where we only use the mean value of the traversability estimate. We can see from Figure 4) that the robot takes paths with moderate to high risk more often (i.e. paths with maximum risk > ∼ 0.3).

<!-- chunk {"id": "body-0098", "role": "body", "section": "Case Study: Risk-Aware Robotic Motion Planning in Subterranean Environments", "weight": 1.0} -->

Ultimately, the risk level desired is left up to the user, but the main takeaway is that the user can change the risk level to mimic deterministic or robust baselines as desired. The robot uses longer, low-risk paths when the robot is risk-averse (low β ) and shorter, higher-risk paths when the robot is risk-neutral (high β ), see Figure 5.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Case Study: Risk-Aware Robotic Motion Planning in Subterranean Environments", "weight": 1.0} -->

This risk-aware traversability evaluation and planning framework was experimentally tested during the DARPA Subterranean Challenge and in other real-world subterranean environments. The final competition course of the DARPA Subterranean Challenge was comprised of tunnel, urban, and cave environments for which the traversability evaluation and navigation results are provided in Figure 6. The following list describes the difficult terrain hazards found within that environment: Region A An office-like area with narrow corridors and small rooms where it is tough to find a feasible path if the maps are overinflated to avoid obstacles.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Case Study: Risk-Aware Robotic Motion Planning in Subterranean Environments", "weight": 1.0} -->

Region B A mock post-earthquake warehouse whose shelving and clutter are difficult to navigate around.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Case Study: Risk-Aware Robotic Motion Planning in Subterranean Environments", "weight": 1.0} -->

Region C A door connecting the urban and tunnel part of the course via stairs. The stairs act as a potential sudden drop-off ( i.e., a negative obstacle) for wheeled robots. The drop is hard to detect because of the narrow doorway.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Case Study: Risk-Aware Robotic Motion Planning in Subterranean Environments", "weight": 1.0} -->

Region D A narrow passage littered with debris, vertical pipes along the walls, and ceiling obstacles. The robot must correctly identify the pipes as obstacles.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Case Study: Risk-Aware Robotic Motion Planning in Subterranean Environments", "weight": 1.0} -->

Region E A small cave opening that mimics real caves, wherein humans must crawl through the small openings to reach another cave chamber. The upward-sloping cave floor and downward-sloping ceiling make it difficult to differentiate between the ceiling and the ground. The ceiling height at the opening is very close to the ground height at the end of the opening.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Case Study: Risk-Aware Robotic Motion Planning in Subterranean Environments", "weight": 1.0} -->

Region F A small limestone cave with rubble and loose rock piles. The robot must distinguish between traversable and non-traversable rubble.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Case Study: Risk-Aware Robotic Motion Planning in Subterranean Environments", "weight": 1.0} -->

A statistical analysis of the simulations and the qualitative experimental results from the field show that a risk-aware traversability and planning pipeline provides a framework where the risk of the entire system can be adjusted by changing the risk-level β despite there being multiple risk sources, such as slopes, obstacles, lowceilings, and mud. This framework is agnostic to the kind of ground robot utilized: it has been tested on wheeled robots (Clearpath Husky) and legged robots (Boston Dynamics Spot quadruped).

<!-- chunk {"id": "body-0106", "role": "body", "section": "Case Study: Risk-Aware Bipedal Walking", "weight": 1.0} -->

Control of bipedal walking presents significant challenges, as evidenced by the variety of approaches taken in the literature to handle the nonlinearity and complexity of bipedal robot dynamics. In practice, bipedal walking dynamics are often simplified by approximate models subject to stochastic uncertainty. The horizontal robot state at time t is denoted by x h ( t ) = [ c, p, v ] T, where c represents the horizontal position of the robot's center of mass (COM) relative to an inertial frame, p denotes the horizontal COM position with respect to the stance foot, and v denotes the horizontal COM velocity. The stepto-step (S2S) dynamics of the horizontal COM state is expressed as x h ( t + 1 ) = P h ( x ( t ), τ ( t )), where τ represents the joints' input torques. In practice, deriving the S2S dynamics analytically is challenging due to the robot's nonlinear and hybrid dynamics.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Case Study: Risk-Aware Bipedal Walking", "weight": 1.0} -->

The authors in suggested that a HybridLinear Inverted Pendulum (H-LIP) walking model provides an apt approximation for the actual horizontal S2S dynamics of robot walking. The H-LIP dynamics are represented as where x H-LIP (t + 1) = [c H-LIP, p H-LIP, v H-LIP] T is the H-LIP's discrete pre-impact state, and u H-LIP (t) denotes the step size. The specific expressions for A and B can be found. With this approximation, the S2S dynamics can be rewritten as where d (t): = P h (x (t), τ (t)) -A x h (t) -B u (t) ∈ D can be viewed as a stochastic disturbance to the linear system.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Case Study: Risk-Aware Bipedal Walking", "weight": 1.0} -->

As seen in Figure 7, a CVaR RCBF-based controller can ensure safe, risk-aware 3D bipedal walking. The model discrepancy w is treated as a stochastic uncertainty and risk factor that could elicit undesirable walking behavior. To mitigate this risk, CVaR RCBF-based controllers are synthesized and act as safety filters for the H-LIP-based stepping controller. We will omit how these barrier functions were generated for this specific problem to keep the discussion at a high level. For those more interested in the details, please reference. Abstractly, however, these barrier functions delineate safe regions within which the bipedal robot can navigate by constraining the horizontal position of the robot to lie between the obstacles it is navigating between. To construct this CVaR RCBF, the authors carried out extensive simulations over a wide range of walking behaviors to numerically define an uncertainty set. Then to calculate the CVaR of the RCBF evaluation at the subsequent time steps - as required in the CVaR RCBF condition expressed in - the authors approximated the true distribution via a uniform sampling over the previously calculated uncertainty set, and calculated the CVaR against this distribution.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Case Study: Risk-Aware Bipedal Walking", "weight": 1.0} -->

Even still, the corresponding walking experiments still represented safe behavior, further supporting the use of risk-aware control barrier functions for risk-aware safe controller synthesis.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Case Study: Risk-Aware Bipedal Walking", "weight": 1.0} -->

The simulation results seen in Figure 8 showcase the effectiveness of the CVaR-based CBF, especially when taking into account the inherent uncertainties in 3D bipedal dynamics. Figure 9 presents snapshots from an experiment conducted at the Caltech AMBER Lab using the Agility Robotics' Cassie bipedal Robot.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Open Questions and Future Directions", "weight": 1.0} -->

This section outlined recent advances in risk-aware planning and control. We applied these ideas to bipedal walking and terrain traversability analysis for wheeled and legged robots. Many future research directions are suggested by current work in risk-aware planning and control.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Open Questions and Future Directions", "weight": 1.0} -->

Computation. The best choice of a risk measure for a specific problem remains an open question. The popular CVaR risk measure is computationally attractive as it can be formed into linear programs when the original stochastic optimal control program is also linear, i.e., when the cost, dynamics, and constraints are linear. Other risk measures such as the KL divergence-based EVaR metric or the Wasserstein metric provide rich expressions of the uncertainty but are computationally expensive. Samplingbased methods for risk computation can also require many samples to guarantee the correctness of the resulting risk-aware plan which remains challenging with computationally-limited hardware, i.e., without a GPU.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Open Questions and Future Directions", "weight": 1.0} -->

Risk-Aware Planning with Nonlinear Dynamics. Keeping with the computation theme, forward computations of nonlinear dynamics with complex policies are already difficult. Adding risk-aware planning further complicates the issue making such a procedure currently intractable for non-sample-based approaches. Even still, real-time applications of these methods further limit the number of samples that can be taken to inform planning or control input selection, making efficient estimation of risk measures in these scenarios an open problem. Recent work indicates that parallelizing computation over a samplebased scenario approach might improve efficiency, but such an approach is still computationally intensive.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Open Questions and Future Directions", "weight": 1.0} -->

Multi-agent interactions. Our discussion of risk-aware planning and control only considered a single agent. However, real-world dynamic agents may react to the motion of the controlled agent, and these effects could potentially cause unmodeled uncertainty distribution shifts. An important open problem is how to account for the interactions between dynamic agents in a risk-aware manner.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Open Questions and Future Directions", "weight": 1.0} -->

Approximations of risk. Many risk-aware planning and control techniques either assume that the uncertainty is discrete or use approximation techniques like Sample Average Approximation (SAA) for continuous distributions. How can we guarantee the correctness of risk evaluation and control design when using continuous distribution approximations? The next section introduces methods to verify the risk-aware behavior of autonomous systems.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Open Questions and Future Directions", "weight": 1.0} -->

Constructing Control Barrier Functions In the prior risk-aware safety-critical control section, we introduced control barrier functions as a potential method by which a controller can ensure safety even in a risk-aware context. However, it is worth noting that constructing control barrier functions -let alone the risk-aware formulations - remains an open problem for complex systems. There has been recent work aimed at learning control barrier functions and constructing them numerically via methods such as Sum of Squares (see for a tutorial on the sum of squares method). As such, doing so even in a risk-aware context still remains an open problem.

<!-- chunk {"id": "body-0117", "role": "body", "section": "RISK-AWARE VERIFICATION AND VALIDATION", "weight": 1.0} -->

The previous section provided a high-level summary of risk-aware planning and control, with a more in-depth review of existing literature. We highlighted the importance of analyzing the inherent uncertainties and risks in robotic operations, particularly when navigating through unstructured environments. This section briefly summarizes the important companion problem of "risk-aware verification and validation" (V&V) in robotic systems. The verification process determines whether a given system exhibits its desired behavior in the environments in which it is required to operate. This crucial process ensures that the integrated system performs safely, reliably, and as intended under a broad range of operating conditions.

<!-- chunk {"id": "body-0118", "role": "body", "section": "RISK-AWARE VERIFICATION AND VALIDATION", "weight": 1.0} -->

Integration of risk awareness into the V&V process allows for a more comprehensive evaluation of a robotic system and its potential to properly respond to risky situations. Specifically, V&V aims to quantify robotic reliability and safety, explicitly considering interactions with uncertain and unstructured environments. As such, risk-aware V&V requires probabilistic risk assessments, stochastic models, and rigorous testing methods that cover a wide range of potential scenarios. For instance, recent work in Human-Robot Interaction (HRI) has developed procedures to quantify the riskiness of actions taken by systems in a collaborative context. These methods typically formalize the risk assessment against existing International Standards, e.g. ISO 14121 and ISO 12100. Risk assessment of autonomous systems in other fields has also emerged.

<!-- chunk {"id": "body-0119", "role": "body", "section": "RISK-AWARE VERIFICATION AND VALIDATION", "weight": 1.0} -->

As mentioned, prior notions of risk have typically been defined against a corresponding standard and are developed on a case-by-case basis. This observation has prompted recent work in risk-aware verification to adopt the same formal treatment of risk - tail risk measures - as used by the synthesis community. This section delves into the key methodologies and approaches employed for risk-aware verification and validation in robotics, starting with a brief overview of its theoretical foundations and moving toward practical applications and case studies. As works in this area typically exploit the quantifiable semantics of temporal logics to quantify (un)safe system behavior to make risk-aware verification statements, we begin with a brief overview of temporal logics.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Temporal Logic", "weight": 1.0} -->

Temporal logics can be used to express complex system specifications and were originally developed for the analysis and design of reactive systems, i.e., systems with external inputs such as control systems. Temporal logics are extensions of Boolean logic (propositions, negations, conjunctions, disjunctions) by adding temporal operators (until, eventually, always) to reason about the temporal properties of a system. One can make a distinction between temporal logics that reason over qualitative and quantitative temporal properties in their temporal operators. Linear temporal logic, arguably the most common temporal logic, only reasons over qualitative temporal properties, while real-time temporal logics such as metric temporal logic can reason over quantitative temporal properties. This distinction is best exemplified where a qualitative temporal property is 'eventually reach the goal region' while its quantitative counterpart could be 'eventually within the next 5 minutes reach the goal region'.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Temporal Logic", "weight": 1.0} -->

We focus on temporal logic specifications with quantitative temporal reasoning that can encode combinations of timed reachability ('reach region A within 30 sec'), timed surveillance ('visit regions B, C, and C every 10 -60 sec while agents form a triangular formation"), timed safety ('always between 5 -25 sec stay at least 1 m away from region E"), and many others.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Temporal Logic", "weight": 1.0} -->

Temporal logics are formally defined by their syntax and semantics where the syntax defines the rules to construct a temporal logic specification ϕ while the semantics define when a temporal logic specification ϕ is satisfied (or violated). Spatiotemporal logics, as opposed to temporal logics, also permit reasoning about spatial properties, e.g., allowing a system designer to quantify to which extent (with what safety margin) an obstacle is avoided by a robot. It is this property that enables us to quantify how well a specification is satisfied c.f. how severely a specification is violated, which in turn helps define risk for system verification. Signal temporal logic is a commonly used spatiotemporal logic introduced, and we provide a brief introduction to its syntax and semantics in the sidebar 3. For the remainder of the exposition in this section though, assume that ϕ denotes a system specification.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Temporal Logic", "weight": 1.0} -->

Concerning the use of these logics in verification and validation, over the past decades, the formal methods community proposed and studied a broad range of system verification techniques. Existing techniques focus on the verification of 1) deterministic systems, or 2) uncertain systems with the two previously discussed viewpoints of the risk-neutral and the worst-case paradigms. In fact, automated verification tools were developed for deterministic systems, e.g., model checking or theorem proving. Verification of uncertain systems was particularly studied in the risk-neutral paradigm using probabilistic model checking, an extension of deterministic model checking, or statistical model checking, which are sampling-based techniques for probabilistic system verification. System verification techniques, however, should not only be able to reason about the probability of violating a specification but also be able to reason about the severity of a violation in terms of rare harmful outcomes. As briefly discussed previously, spatiotemporal logics enable us to quantify how well (severely) a specification is satisfied (violated), and in turn, allow us to define risk in terms of this quantitative measure for stochastic systems.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Temporal Logic", "weight": 1.0} -->

Sidebar 3 (Signal Temporal Logic: Syntax and Semantics). Signal temporal logic (STL) specifications are interpreted over continuous-time signals x: R ≥ 0 → R n. An STL specification ϕ is recursively constructed from atomic predicates by using Boolean operators and temporal operators. These atomic predicates are Boolean-valued functions µ: R n → { 1, 0 } whose truth value is obtained after evaluation of a real-valued function b: R n → R. At time t, we obtain the truth value of µ as Predicate functions h can encode relationships between state variables, such as relative or absolute distances. The syntax of STL defines a set of rules according to which well-defined STL specifications can be constructed and is given as where the operators ¬, ∧, and UI encode negations, conjunctions, and the until over the time interval I ⊆ R ≥ 0, respectively. The syntax in can be understood as follows: the symbol:: = assigns one of the expressions from the righthand side, which are separated by vertical bars, to the free variable ϕ on the left-hand side.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Temporal Logic", "weight": 1.0} -->

The variables ϕ ′ and ϕ ′′ on the right-hand side are already well-defined STL specifications. While the meaning of negations and conjunctions is clear, the until operator ϕ ′ UI ϕ ′′ encodes that ϕ ′ has to hold until ϕ ′′ holds, which has to happen within the time interval I. We can now use logical equivalences to derive the Boolean disjunction, implication, and equivalence operators and the temporal eventually and always operators. In what follows, ⊤ denotes True in the corresponding logical specification: The semantics of STL define when a signal x satisfies an STL specification ϕ. These semantics are formally defined as a relation | = between x and ϕ, and (x, t) | = ϕ means that the signal x satisfies the specification ϕ at time t. We recursively define the semantics as

<!-- chunk {"id": "body-0126", "role": "body", "section": "Motivations for Tail Risk Measures in Verification", "weight": 1.0} -->

As mentioned previously then, the existence of these spatiotemporal logics makes tail risk measures uniquely suited to serve as the risk measure of choice for verification and validation, and this section will provide an example supporting that claim using the notation offered in Sidebar 4. Consider for the sake of argument that we have two controlled systems Σ 1, Σ 2, a Signal Temporal Logic specification ϕ denoting the desired behavior required of both systems and a robustness measure ρ ϕ for the same specification ϕ. For context, every signal temporal logic specification ϕ comes equipped with a quantitative measure. Let's further assume that every time we query either system Σ 1 or Σ 2, we receive a random trajectory x 1 or x 2 respectively. Let Ri, i = 1, 2, be a random variable whose samples r i are the robustness of the trajectories sampled from system Σ i, i.e. r i = ρ ϕ ( x i ).

<!-- chunk {"id": "body-0127", "role": "body", "section": "Motivations for Tail Risk Measures in Verification", "weight": 1.0} -->

Now, let's assume that an oracle tells us that for both systems, with probability 1 -β for some β ∈ ( 0, 1 ], the random robustness exceeds a cutoff value ϵ > 0. Furthermore, with probability β, Σ 1 exhibits robustness values between ϵ and 0, whereas Σ 2 exhibits robustness values strictly less than 0. In other words, Σ 1 will always realize the desired behavior, while Σ 2 will, in some rare cases, be unable to realize the desired behavior.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Motivations for Tail Risk Measures in Verification", "weight": 1.0} -->

Put into the context of tail risk measures, both systems exhibit a robustness value-at-risk at risk-level β that is positive. This fact arises as the oracle mentioned that with minimum probability 1 -β, both systems exhibit robustnesses exceeding ϵ > 0, i.e. VaR β ( Ri ) = ϵ > 0. Ending the analysis here results in the correct conclusion that both systems exhibit some minimum probability of realizing satisfactory behavior, and this is a traditional, probabilistic V&V statement. However, by considering conditional value-at-risk, we can further discriminate between the two systems, as system 1 is expected to exhibit satisfactory behavior even in the worst 100 β %of cases, whereas system 2 is expected to produce unsatisfactory behavior in the same cases.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Motivations for Tail Risk Measures in Verification", "weight": 1.0} -->

This conclusion arises as even in the worse 100 β %of cases, the oracle mentioned that system 1 exhibits robustness values r 1 ∈ [ 0, ϵ ] whereas system 2 exhibits robustness values r 2 < 0. Taking into account the expected value over those cases -the definition of conditionalvalue-at-risk - we conclude that CVaR β ( R 1 ) ≥ 0 whereas CVaR β ( R 2 ) < 0. Therefore, even if both systems exhibit similar minimum probabilities of specification satisfaction, system 1 is "better" than system 2 as it is still expected to exhibit satisfactory behavior in the worst 100 β % of cases.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Motivations for Tail Risk Measures in Verification", "weight": 1.0} -->

The example described above highlights the utility of tail risk measures in risk-aware V&V. By considering the robustness value-at-risk, we can make statements on the minimum probability with which a system exhibits a desired behavior in its operating environment(s) - this is the traditional notion of probabilistic V&V. Additionally, we can utilize tail risk measures to also make statements on expected worst-case robustness using the conditionalvalue-at-risk, lower bound such expected worst-case robustness using entropic value-at-risk, and calculate these values without exact distribution knowledge as will be described in sections to follow.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Motivations for Tail Risk Measures in Verification", "weight": 1.0} -->

Sidebar 4 (Signal Temporal Logic: Robust Semantics). While the STL semantics tell us if a signal x: R ≥ 0 → R n satisfies an STL specification ϕ, it does not give us any information about the quality of satisfaction. To obtain such information, one can define robust semantics that quantify how robustly the signal x satisfies the specification ϕ. If x satisfies ϕ, we would hence like to quantify how different a signal x ∗: R → R n can be from x while still satisfying ϕ. To quantify this, we first define the closeness of two signals x, x ∗: R → R n as We now want to compute a value ρ ϕ such that all signals x ∗ that are such that d (x, x ∗) < ρ ϕ will also satisfy ϕ, i.e., (x ∗, t) | = ϕ.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Motivations for Tail Risk Measures in Verification", "weight": 1.0} -->

To do so, we first define the signed distance of the signal value x (t) to the set of states that satisfy a predicate µ, denoted by O µ: { x ∈ R n | b (x) ≥ 0 }, as Note that Dist (x (t), O µ) quantifies the extent to which µ is satisfied (if Dist (x (t), O µ) > 0) or violated (if Dist (x (t), O µ) < 0). We can now recursively define the robust semantics of ϕ as a real-valued function ρ ϕ (x, t) as follows Finally, it holds that (x, t) | = ϕ if and only if (x ∗, t) | = ϕ for all signals x ∗: R → R n that are such that d (x, x ∗) <

<!-- chunk {"id": "body-0133", "role": "body", "section": "General Overview of Risk-Aware V&V", "weight": 1.0} -->

For most relevant problems, the system to be verified can be recast as a discrete-time system with known state and input spaces and (perhaps) known dynamics and disturbance spaces. Formally, at some time t ∈ Z + = { 0, 1, 2,... }, let x (t) ∈ X be the system state, u (t) ∈ U be the system control input, d (t) ∈ D be a randomly sampled disturbance. Then for some distribution function ξ: X × U × Z + ×D → over D, Finally, let U: X × Θ × Z + → U be the controller closing the loop for the system to be verified. Note, the controller U is parameterized with a parameter θ ∈ Θ to account for exogenous, user-specific inputs that may influence controller behavior, e.g. parameterized 3-space locations for packages in a warehouse that a warehouse robot receives on-the-fly from a central command station when a package is required to be collected.

<!-- chunk {"id": "body-0134", "role": "body", "section": "General Overview of Risk-Aware V&V", "weight": 1.0} -->

Remark. For systems that operate in adversarial environments or in the presence of obstacles, the disturbance distribution ξ can be defined as the singleton distribution over the adversarial choice at the given state x ( t ), input u ( t ), and time t. For more information see dirac distributions and adversarial testing works such as. We can consider both cases - the case with nonadversarial, randomized disturbances and the case with adversarial or otherwise known disturbances - in the same stochastic setting. Furthermore, the state and input spaces have been left arbitrary to allow both the continuous space definitions in the controls community and the finite-state and input definitions in the (PO)MDP computer science literature.

<!-- chunk {"id": "body-0135", "role": "body", "section": "General Overview of Risk-Aware V&V", "weight": 1.0} -->

Closing the loop between and the assumed controller U generates a system Σ that when queried with a specific initial condition x 0 ∈ X 0 ⊆ X and controller parameter θ ∈ Θ produces a (perhaps) different state trajectory x, which is an element of the signal space S = { s: Z + →X}: Finally, let C be a classifier function mapping from the signal and parameter spaces to the real-line, i.e. C: S × Θ → [-a, b] where parameters a, b ∈ R ++ are finite. The classifier C delineates between satisfactory behavior - trajectory and parameter pairs (x, θ) that evaluate to a positive value, i.e. C (x, θ) ≥ 0 - and unsatisfactory behavior - pairs that evaluate to a negative value.

<!-- chunk {"id": "body-0136", "role": "body", "section": "General Overview of Risk-Aware V&V", "weight": 1.0} -->

Examples of such a classifier could be the robustness functions ρ from signal temporal logic, the minimum value of a barrier function h over time, etc. For a description of robustness measures in Signal Temporal Logic, please see Sidebar 4. Generally speaking, we define the outcome of function C to be the robustness of the corresponding trajectory and parameter pair, i.e. for r = C (x, θ), where r is the trajectory and parameter pair's robustness value. More positive values of C (x, θ) indicate better, more robust realization of the desired behavior.

<!-- chunk {"id": "body-0137", "role": "body", "section": "General Overview of Risk-Aware V&V", "weight": 1.0} -->

Remark The rationale to analyze multiple, non-unique trajectories x as defined in arises from the fact that disturbances d in are sampled randomly at each time t from the distribution function ξ. If the distribution function ξ were the singleton distribution corresponding to a specific disturbance d ∈ D for each state, input, and time ( x, u, k ) ∈ X × U × Z +, then Σ ( x 0, θ ) would always produce the same trajectory x upon successive queries at ( x 0, θ ), and this argument holds ∀ ( x 0, θ ) ∈ X 0 × Θ.

<!-- chunk {"id": "body-0138", "role": "body", "section": "General Overview of Risk-Aware V&V", "weight": 1.0} -->

The goal of risk-aware verification then, is to bound the risk-measure evaluation of the classifications of these (perhaps) stochastically evolving trajectories. Stated formally, let χ be a tail risk measure, e.g. Value-at-Risk, ConditionalValue-at-Risk, Entropic-Value-at-Risk, etc. Then, at some risk-level β ∈, determine an upper or lower bound to χ ( C ( Σ ( x 0, θ ))) for some ( x 0, θ ) ∈ X 0 × Θ. Figure 10 depicts this generic risk-aware verification pipeline, and the following section will specify how this pipeline has been implemented in a variety of recent works. To facilitate that discussion, we will define the robustness R ( x 0, θ ) to be the random variable whose samples r = C ( x, θ ), where x is a sample of the random variable Σ ( x 0, θ ). In other words, R ( x 0, θ ) = C ( Σ ( x 0, θ ), θ ) - this term was first defined.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Examples", "weight": 1.0} -->

Perhaps the most prevalent examples of risk-aware verification arise from a re-framing of traditional work in the Stochastic Model Checking (SMC) community. With respect to the aforementioned pipeline, SMC assumes the ability to collect system traces - trajectories x - and evaluate their satisfaction of a desired behavior. These behaviors are typically expressed as a specification ϕ in Probabilistic Computational Tree Logic, which is a form of Temporal Logic (see Sidebar 3). As such, each of these behaviors has satisfiability metrics - classifier functions C in our overarching methodology - with which to determine trace satisfaction of the desired behavior ϕ.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Examples", "weight": 1.0} -->

SMC consists of two different analyses. The first, hypothesis testing, asserts that the system Σ realizes the behavior ϕ with minimum probability p and determines the minimum number of system traces that have to be evaluated to accept or reject this hypothesis. The second, estimation, exploits either the Chernoff bound or Hoeffding's inequality to estimate the probability p with which Σ FIGURE 10: A flowchart for a general risk-aware verification pipeline. In the figure, the parameters θ correspond to obstacle locations and waypoints for the robots highlighted by white and blue circles. Risk-aware verification bounds the risk-measure evaluation of evaluated trajectories - the blue data shown in the right figure. realizes ϕ within some tolerance bounds that are a function of the number of trajectories sampled and evaluated. In both cases, however, the probability of satisfaction p has a one-to-one correspondence with the Value-at-Risk of the random variable R (x 0) (we omit θ in the notation here, as SMC typically does not consider parameterized trajectories). More specifically, p is such that VaR1 -p (R (x 0)) ≥ 0.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Examples", "weight": 1.0} -->

These are not the only works that take a Value-at-Risk approach to system verification. In, the authors use scenario optimization to lower bound the Value-at-Risk of the robustness random variable R (x 0, θ) for a user-defined β ∈. Similarly, the authors of use a sampleaverage-approximation procedure to estimate the Value-atRisk of the same robustness variable for any user-defined β ∈. In, the authors go one step further and express policy or controller synthesis as an optimization problem over a general class of risk measures for verification purposes. They show numerical examples of the success of a convex-concave procedure in identifying such policies for a Markov Decision Process. In this case, the policies optimize for a certain risk sensitivity as expressed by Value-at-Risk among other risk measures expressed in Cumulative Prospect Theory. Finally the authors modify a learned controller online whenever the learned controller outputs an infeasible trajectory. Via a gradient-descent method, they update controller parameters until the resulting trajectory passes an intermediary risk-aware verification step, before implementation of the modified controller.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Examples", "weight": 1.0} -->

In general, however, any of the aforementioned risk-aware works could also be conceived of as Value-at-Risk-based verification, insofar as the classifier functions C were developed against specific standards for their respective applications However, Value-at-Risk verification represents a smaller fraction of risk-aware verification efforts as compared to works using coherent risk measures, such as ConditionalValue-at-Risk. For example, in a similar paradigm as, in the author proves that there exist polynomial time algorithms to determine policies for an MDP that are verifiable by default. Verification arises as the policies are synthesized to achieve a minimum conditional value at risk with respect to objective satisfaction. Similarly, in the authors utilize a CVaR constraint for their optimal controller and verify that the system remains within a risksensitive safe set defined by the same CVaR constraint. In, the authors develop a procedure for learning a controller to tackle simultaneous performance and safety tradeoffs for nonlinear systems and verify the learned controller by estimating the CVaR of a corresponding robustness random variable.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Examples", "weight": 1.0} -->

In, the authors constrain the optimal design of supersonic aircraft bodies against both VaR and CVaR requirements to ensure verifiable, riskaware performance despite uncertainties arising from the transition from laminar to turbulent flow, manufacturing uncertainties, etc. Examples from a larger body of work, including those by the authors, can be found in references.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Case Study: Risk-Aware Verification of Lane Keeping Controllers", "weight": 1.0} -->

In this case study, the goal is to find the least risky controller among two neural network lane-keeping controllers in the autonomous driving simulator CARLA during a left-turn, see Fig. 12 (top and middle). Lanekeeping is realized by tracking a set of predefined waypoints. For verification, we consider the cross-track error ce and the orientation error θ e with respect to the current and next waypoint, see Fig. 12 (bottom). We consider an imitation learning (IL) controller and a control barrier function (CBF) controller. The car model is stochastic, as the control inputs are subject to normally distributed noise, and we uniformly sample the car's initial position from the set ( ce, θ e ) ∈ × [ -0.4, 0.4 ]. We collected N: = 1000 trajectories x i in a validation set D val for each controller.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Case Study: Risk-Aware Verification of Lane Keeping Controllers", "weight": 1.0} -->

We are first concerned with cross-track error and consider the specifications ϕ 1: = G [ 0, ∞ ) ( | ce | ≤ 2.25 ) where 2.25 is an empirically obtained threshold indicating that the car stays within the lane. For the following analysis, recall that a negative value of -ρ ϕ 1 indicates satisfaction of ϕ 1 and positive values indicate a failure to lane-keep. Upper bounds on VaR 0.95 ( -ρ ϕ 1 ( x )), CVaR 0.85 ( -ρ ϕ 1 ( x )), and E ( -ρ ϕ 1 ( x )) are reported in Table 1, along with the empirical satisfaction rate P ϕ 1: = |{ x i ∈ D val | x i satisfies ϕ 1 }| / N. Clearly, the IL controller is the least risky one in terms of VaR 0.95 and CVaR 0.85, and it also has the highest empirical satisfaction rate. Interestingly though, the CBF controller performs better on average. This result can also be seen in the empirical histograms of Fig. 11 (top left).

<!-- chunk {"id": "body-0146", "role": "body", "section": "Case Study: Risk-Aware Verification of Lane Keeping Controllers", "weight": 1.0} -->

We hypothesize that this behavior arises from the long tail of risky behavior for the CBF controller, which corresponds to transient system behavior. We also analyzed the controllers' behavior more closely by looking at the crosstrack error during the steady-state and transient phases for the specifications ϕ 2: = G [ 10, ∞ ) ( | ce | ≤ 2.25 ) and ϕ 3: = F G ( | ce | ≤ 1.25 ), respectively. The upper bounds of the VaR 0.95 ( -ρ ϕ i ( x )) and E ( -ρ ϕ i ( x )) for ϕ 2 and ϕ 2 are shown in Table 1 as well.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Case Study: Risk-Aware Verification of Lane Keeping Controllers", "weight": 1.0} -->

Interestingly, the IL controller is the least risky one only during the transient phase, while the CBF controller is the least risky one in steady state. The corresponding empirical distributions are shown in Figs. 11 (top right and bottom left). Finally, let us verify the controller risk in terms of the orientation error θ e. Consider ϕ 4: = G [ 0, ∞ ) ( ( ce ≥ 1.25 ) = ⇒ F G ( θ e ≤ 0 ) ∧ ( ce ≤ -1.25 ) = ⇒ F G ( θ e ≥ 0 ) ) which expresses the need for the controller to react to large cross-track errors ce using the right orientation adjustment.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Case Study: Risk-Aware Verification of Lane Keeping Controllers", "weight": 1.0} -->

For this specification, the CBF controller is the least risky controller, which aligns with our observation that it is a better controller during steady-state. It can further be observed that both controllers have the same empirical satisfaction probability, while our risk analysis better quantifies a controller's quality. The empirical distribution of both controllers is shown in Fig. 11 (bottom right).

<!-- chunk {"id": "body-0149", "role": "body", "section": "Case Study: Risk-Aware Verification of Quadrupedal Locomotion", "weight": 1.0} -->

This case study aims to verify a quadruped's ability to render positive a collision-avoidance barrier function h for at least T = 150 time-steps with a time-step ∆ t = 0.1. Keeping consistent with our notation for the general overview for risk-aware V&V, our parameters θ include the locations of 4 randomly placed static obstacles in a 5 × 5 meter grid, and the center coordinates of a goal region g in the same grid. Hence, θ ∈ 10 ≜ Θ. To simplify our analysis, we represent the quadruped as a unicycle system, and as such, we assume we can initialize the quadruped at a random planar position and angular orientation in the grid, i.e. x 0 ∈ 2 × [ 0, 2 π ] ≜ X 0. Our classifier function C evaluates the discrete-time fractional difference of a candidate barrier function h that the quadruped is to keep positive.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Case Study: Risk-Aware Verification of Quadrupedal Locomotion", "weight": 1.0} -->

As such, the classifier outputs the minimum value over all time-steps k of h ( x ( t + 1 ) / h ( x ( t )), as realized by the quadruped over one trajectory x = { x, x,..., x }. Therefore, C ( x ) < 0 is equivalent to stating that there existed an interior timestep xj ∈ x such that h ( xj ) < 0 and the quadruped failed to remain safe.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Case Study: Risk-Aware Verification of Quadrupedal Locomotion", "weight": 1.0} -->

Slightly different from the general overview, however, instead of aiming to determine a lower bound on the Value-at-Risk level β = 0.9 of the robustness random variable R ( x 0, θ ), we also randomize over initial conditions and parameters ( x 0, θ ) from their combined space. As such, the evaluation r of a sampled trajectory x generated by first sampling ( x 0, θ ) ∼ U [ X 0 × Θ ] is a sample of the holistic robustness random variable R - this term was first defined. That being said, we still aim to lower bound VaR β = 0.9 ( R ), which, according to the samplebased methods detailed in Sidebar 5, has a known sample complexity (number N of trajectories to be evaluated) to determine such a lower bound. To be specific, riskaware verification in this context amounts to identifying a high-probability lower bound on the Value-at-Risk of the holistic robustness random variable R through a samplebased approach predicated on scenario optimization.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Case Study: Risk-Aware Verification of Quadrupedal Locomotion", "weight": 1.0} -->

Therefore, after taking N = 50 trajectories, we can state with ≈ 99.5% confidence, that the quadruped will realize positive value trajectories with 90% probability, as the identified lower bound on VaR β = 0.9 ( R ) was positive. The associated safety information is depicted in Figure 14.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Case Study: Risk-Aware Verification of Quadrupedal Locomotion", "weight": 1.0} -->

We can also show that the reported probabilistic bounds are accurate. In we employed the same, risk-aware verification procedure as described above, to validate the controllers for a Quadruped and a multi-agent robotic system. The expressions for the classifier function were the same in both cases, though we will refrain from reproducing them here for the sake of brevity. Suffice it to say that any trajectory that evaluates to a positive value under C would have made non-trivial progress toward a goal while avoiding static/moving obstacles within 10 seconds. To that end then, we only implemented controllers on hardware systems once they exhibited a positive lower bound for VaR0.99 ( R ). To determine such a lower bound we sampled 300 trajectories for both controllers and calculated their robustness under the aforementioned classifier C. Doing so for our chosen controllers indicated positive lower bounds, and we can verify the accuracy of these lower bounds by taking 20000 trajectories, evaluating them, numerically approximating the distribution of the holistic robustness random variable R, and reporting the numeric VaR0.99 ( R ) as our approximation.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Case Study: Risk-Aware Verification of Quadrupedal Locomotion", "weight": 1.0} -->

Figure 13 showcases the validity of the reported lower bounds, overlaid on the numeric approximation of the distribution for R, and Figure 15 shows tiles of the controllers implemented on their respective hardware systems. Note that in all of the randomized cases, the controllers steered the systems successfully to their goals while avoiding all obstacles. This controller reliability is the primary reason we take a tail risk approach to verification, as the purpose of the procedure is to identify rare, unsafe phenomena and ensure that even in those rare cases, the system still performs admirably.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Case Study: Risk-Aware Verification of Quadrupedal Locomotion", "weight": 1.0} -->

Sidebar 5 (Concentration Inequalities: Risk Measure Estimation). This sidebar will briefly describe two methods to estimate the tail risk measures expounded upon in this article. We will describe these methods as they are applied to arbitrary scalar random variables X.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Case Study: Risk-Aware Verification of Quadrupedal Locomotion", "weight": 1.0} -->

Sample-Average Approximation This first method estimates VaR β (X), CVaR β (X) for any β ∈ and any scalar random variable X. Let { xi } N i = 1 be a set of N independently drawn samples of X. The empirical distribution function ˆ FN (x) for X based on this set of samples is with 1 being the indicator function. The Sample-Average Approximation (SAA) exploits the Dvoretsky-Kiefer-Wolfowitz Inequality built upon by Paul Massart, which proves that the empirical distribution has bounded deviation with respect to the true cumulative distribution function F for X to within some probability δ ∈: The tail risk VaR β (X) can be lower and upper bounded for any β ∈ using. Define upper bound VaR β (X) as: Then, using, the following result holds ∀ β, δ ∈ Note that as the number of samples, N, of the random variable X increases, the gap between the upper and lower bounds shrinks, as the bounds converge to the true value VaR β (X). Similar methods exist to estimate CVaR β (X) as well. Scenario Bounds.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Case Study: Risk-Aware Verification of Quadrupedal Locomotion", "weight": 1.0} -->

The second method upper bounds VaR β (X), CVaR β (X), EVaR β (X) for any β ∈. As before, let { xi } N i = 1 be a set of N independently drawn samples of the scalar random variable X. Consider the following optimization problem, termed a scenario program: The theory of scenario optimization states that the solution to this optimization problem is an upper bound on VaR β (X) with minimum probability 1 -(1 -β) N, i.e. if X has probability density function π, then The above result was proven. Note that does not need the density function π for X to be known. It just requires an ability to take N independent samples of X. Therefore, if we have a constant c ∈ R such that P π [x ≤ c] = 1, then we can exploit this inequality to similarly upper bound CVaR β (X) and EVaR β (X). Details on this approach can be found in Section 3 of.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Case Study: Risk-Aware Verification of Quadrupedal Locomotion", "weight": 1.0} -->

Remark on Utility in Controller Synthesis and Verification: As will be mentioned in various sections in this article, utilizing these concentration inequalities to estimate risk measures assumes that any taken samples are identically distributed. This may pose a problem for controller synthesis, as oftentimes the randomness prompting the need for a risk-aware analysis stems from a random disturbance whose distribution is conditioned on the control input to be chosen. Similarly for verification, one must take care to ensure that the method used to randomly sample trajectories to be verified consistently samples these random trajectories from the same distribution. As ensuring that these samples are identically distributed oftentimes requires considerable effort or may be impossible, recent work aims to estimate these risk measures over non-stationary distributions, though this remains an open problem (for more here, please reference the Open Problems and Future Directions section towards the end of the article).

<!-- chunk {"id": "body-0159", "role": "body", "section": "Case Study: Risk-Aware Verification of Quadrupedal Locomotion", "weight": 1.0} -->

Hardware Demonstrations of Verified Controllers All Successes FIGURE 15: Hardware demonstration of controllers verified from a tail risk perspective. As the implemented controllers were 'verified" since the reported lower bound on their Robustness Value-at-Risk was positive, we expect decent behavior in practice. Indeed, the verified controllers performed admirably despite randomized test cases generated for each system. Figure adapted.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Open Questions and Future Directions in V&V Sample Complexity", "weight": 1.0} -->

There exist several open questions in risk-aware verification, though the most notable one concerns the small tail probability requirements for industrial applications. More specifically, for most product-level robotic systems requiring a verification statement, i.e. autonomous cars, factory robots, flight software, etc, current standards require these systems to be verified to arbitrarily high probabilities, i.e. 1 -10 -4, 1 -10 -6, 1 -10 -9 or even higher. If we assume that the underlying distributions are known, i.e. Gaussian as is typically done, then this analysis can be carried out in a tractable, even analytic, fashion. However, if we follow the philosophy underlying the sample-based works that have recently become more popular, as they do not assume underlying distributional knowledge for verification, then verifying systems to these probabilities could require hundreds of thousands of samples or even more. If each of those samples constitutes even one experimental run of the system, then this makes the direct application of these theoretical concepts exceedingly costly or time-intensive.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Open Questions and Future Directions in V&V Sample Complexity", "weight": 1.0} -->

As such, reducing this sample complexity, whether via intelligent test design or by leveraging partial system knowledge, would go a long way to facilitate the widespread industrial adoption of these currently theoretical pipelines.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Compositional Verification", "weight": 1.0} -->

In a similar vein as prior, this second open question stems from a primarily industrial concern as well. Namely, typical large-scale systems are composed of a variety of moving parts, each of which has to satisfy its own component specifications such that the larger, architectured system satisfies a grander objective. Per the prior pipeline, each component could be verified separately in a probabilistic fashion, but in systems with potentially hundreds of separately engineered parts, separate verification procedures could be potentially prohibitive. On the other hand, the system could be verified as a largescale black-box system, though this could similarly fall under the sample-complexity questions as risen in the prior subsection. As such, determining an optimal way of breaking down these larger-scale, system-level specifications, into easily verifiable subcomponents for their respective systems remains an open problem. Indeed, the satisfiability of a given signal temporal logic specification itself remains a challenging problem. Determining the min- imum number of such subcomponents would also mitigate any further sample-complexity issues arising from separate verification procedures as well. On the other hand, perhaps via smart instrumentation, all verification procedures for all subcomponents could be performed simultaneously.

<!-- chunk {"id": "body-0163", "role": "body", "section": "OPEN PROBLEMS AND FUTURE DIRECTIONS", "weight": 1.0} -->

Our discourse up to this point has predominantly centered on the utilization of tail risk measures in the domains of planning, control, and verification within robotic systems. Nonetheless, it is crucial to emphasize the broader applicability and potential impact of these notions. In this section, we detail several emerging areas that have gained substantial attention.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Risk-Aware Learning", "weight": 1.0} -->

There exists a rich body of literature exploring the integration of tail risk measures within learning paradigms such as reinforcement learning, supervised learning, and unsupervised learning. These studies delve into diverse topics ranging from risk-sensitive reward functions and policy optimization to risk-aware feature learning and model training. Such research underscores the versatile role of tail risk measures in not only guiding robotic behavior in uncertain environments but also enabling robots to learn and adapt in a risk-aware manner over time. Thus, to provide a comprehensive overview of the role of tail risk measures in robotics, it is crucial to shed light on their applications in learning-based contexts as well.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Risk-Aware Learning", "weight": 1.0} -->

The recent exploration into risk-averse reinforcement learning is well encapsulated by the work of Greenberg et al.. They emphasized the challenges of optimizing risk measures, as conventional methods often overlook high-return strategies. To address this, they proposed a soft risk mechanism coupled with a Cross-Entropy module for efficient risk sampling. This innovative method, while maintaining risk aversion, demonstrated improved risk aversion across diverse benchmarks, setting a precedent for future exploration in this realm. In another interesting direction, Lacotte et al. delved into a risk-sensitive Generative Adversarial Imitation Learning (GAIL) approach aimed to perform as well as or better than the expert regarding a risk profile.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Risk-Aware Learning", "weight": 1.0} -->

Focusing on risk-constrained reinforcement learning, Chow et al. developed algorithms for risk-constrained MDPs, using chance constraints or CVaR as the risk representation. Their work represents an important step towards understanding and implementing risk constraints in RL and how these can be used for practical applications. Finally, Kose and Ruszczynski's work proposed a novel reinforcement learning methodology employing a Markov coherent dynamic risk measure. This work provided new risk-averse counterparts for basic and multistep methods of temporal differences, paving the way for future exploration in risk-averse learning methodologies.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Risk-Aware Learning", "weight": 1.0} -->

Despite the notable strides made in these studies, there are still many open problems in risk-aware reinforcement learning. One that specifically ties into the next section includes risk-aware reinforcement learning when the underlying distribution changes over time. Such nonstationarity would frustrate, for example, immediate applications of distributional reinforcement learning for policy development, as such approaches aim to learn the underlying distribution to inform future risk-aware action choices. However, we do expect such nonstationarity in real-world contexts, e.g. changing wind patterns over time for a drone. Keeping with the realistic theme, most risk-aware reinforcement learning approaches are sample complex. While this is fine in a simulation or lab-based setting, how do we efficiently learn such policies in real-world contexts where experiments are not cheap? Alternatively, how might we transition the learned simulation or labbased policies to real-world contexts where disturbance distributions are almost certainly different?

<!-- chunk {"id": "body-0168", "role": "body", "section": "Risk-Awareness with Nonstationary and Dependent Data", "weight": 1.0} -->

This second area has garnered substantial interest insofar as it breaks the assumptions in the works discussed in this survey. Namely, the vast majority of the work discussed has all centered around risk-aware methodologies where either 1) the underlying distribution was known either exactly or in a distributionally-robust sense, or 2) the distribution is queryable in a sample-based fashion, where the algorithm receives independent samples. What happens when either of these assumptions fails to hold? This is the central question in a new area of work that is just beginning in the risk-aware space, and for important reasons as well. Consider a robot ambulating over uneven terrain. As the robot traverses the space, any recording of the unevenness of the terrain would correspond to samples from a nonstationary distribution, and if the robot's controller builds a map of the terrain with this information and chooses actions predicated on this map, then successive data is necessarily not independent.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Risk-Awareness with Nonstationary and Dependent Data", "weight": 1.0} -->

When the underlying distribution of the uncertainty changes during a motion planning task, we would ideally like to understand the level of this shift, so that we can account for it in our risk-aware planners. There has been a push towards identifying out-of-distribution data for learning-based tasks. In, the authors study task-driven OOD detection using Probably Approximately Correct (PAC)-Bayes theory for training the robot. The PAC-Bayes procedure provides a performance bound such that violating this bound signals that the robot is operating in an OOD environment.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Risk-Awareness with Nonstationary and Dependent Data", "weight": 1.0} -->

In addition to detection of OOD scenarios, we would also like to respond to such scenarios online. Here, distribution- free prediction schemes like those offered by conformal prediction are gaining more traction. As these tools offer ways of generating probabilistically accurate predictors provided streams of, potentially non-independent data, these predictors have been used for motion planning, confidence regions for learned classifiers, and even for risk-aware decision making, though not in a tail risk sense. If we can identify and adapt to distribution shifts in a risk-aware manner, we can enable robotic systems to react to data drift, unseen data, or spurious correlations. By dynamically adjusting the risk level to adapt to the changing uncertainty distribution and guaranteeing the desired level of safety for the motion planning task, robots can operate in a wider array of unstructured environments while guaranteeing safety, task completion, and efficiency.
