<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On a Formal Model of Safe and Scalable Self-driving Cars

Topics include Autonomous driving, Safety, Scalability, Responsibility-sensitive safety, RSS, Self driving.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In recent years, car makers and tech companies have been racing towards self driving cars. It seems that the main parameter in this race is who will have the first car on the road. The goal of this paper is to add to the equation two additional crucial parameters. The first is standardization of safety assurance - what are the minimal requirements that every self-driving car must satisfy, and how can we verify these requirements. The second parameter is scalability - engineering solutions that lead to unleashed costs will not scale to millions of cars, which will push interest in this field into a niche academic corner, and drive the entire field into a "winter of autonomous driving". In the first part of the paper we propose a white-box, interpretable, mathematical model for safety assurance, which we call Responsibility-Sensitive Safety (RSS). In the second part we describe a design of a system that adheres to our safety assurance requirements and is scalable to millions of cars.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The "Winter of AI" is commonly known as the decades long period of inactivity following the collapse of Artificial Intelligence research that over-reached its goals and hyped its promise until the inevitable fall during the early 80s. We believe that the development of Autonomous Vehicles (AV) is dangerously moving along a similar path that might end in great disappointment after which further progress will come to a halt for many years to come.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The challenges posed by most current approaches are centered around lack of safety guarantees, and lack of scalability. Consider the issue of guaranteeing a multi-agent safe driving ("Safety"). Given that society will unlikely tolerate road accident fatalities caused by machines, guarantee of Safety is paramount to the acceptance of autonomous vehicles. Ultimately, our desire is to guarantee zero accidents, but this is impossible since multiple agents are typically involved in an accident and one can easily envision situations where an accident occurs solely due to the blame of other agents (see Fig. 1 for illustration). In light of this, the typical response of practitioners of autonomous vehicle is to resort to a statistical data-driven approach where Safety validation becomes tighter as more mileage is collected.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To appreciate the problematic nature of a data-driven approach to Safety, consider first that the probability of a fatality caused by an accident per one hour of (human) driving is known to be $10^{- 6}$. It is reasonable to assume that for society to accept machines to replace humans in the task of driving, the fatality rate should be reduced by three orders of magnitude, namely a probability of $10^{- 9}$ per hour^11^1This estimate is inspired from the fatality rate of air bags and from aviation standards. In particular, $10^{- 9}$ is the probability that a wing will spontaneously detach from the aircraft in mid air.. In this regard, attempts to guarantee Safety using a data-driven statistical approach, claiming increasing superiority as more mileage is driven, are naive at best. The amount of data required to guarantee a probability of $10^{- 9}$ fatality per hour of driving is proportional to its inverse, $10^{9}$ hours of data (see details in the sequel), which is roughly in the order of thirty billion miles.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, a multi-agent system interacts with its environment and thus cannot be validated offline^22^2unless a realistic simulator emulating real human driving with all its richness and complexities such as reckless driving is available, but the problem of validating the simulator is even harder than creating a Safe autonomous vehicle agent --- see Section 2., thus any change to the software of planning and control will require a new data collection of the same magnitude --- clearly unwieldy. Finally, developing a system through data invariably suffers from lack of transparency, interpretability, and explainability of the actions being taken --- if an autonomous vehicle kills someone, we need to know the reason. Consequently, a model-based approach to Safety is required but the existing "functional safety" and ASIL requirements in the automotive industry are not designed to cope with multi-agent environments. Hence the need for a formal model of Safety which is one of the goals of this paper.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The second area of risk lies with lack of scalability. The difference between autonomous vehicles and other great science and technology achievements of the past is that as a "science project" the effort is not sustainable and will eventually lose steam. The premise underlying autonomous vehicles goes beyond "building a better world" and instead is based on the premise that mobility without a driver can be sustained at a lower cost than with a driver. This premise is invariably coupled with the notion of scalability --- in the sense of supporting mass production of autonomous vehicles (in the millions) and more importantly of supporting a negligible incremental cost to enable driving in a new city. Therefore the cost of computing and sensing does matter, if autonomous vehicles are to be mass manufactured, the cost of validation and the ability to drive "everywhere" rather than in a select few cities is also a necessary requirement to sustain a business.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The combined issues of Safety and Scalability contain the risk of "Winter of autonomous vehicles". The goal of this paper is to provide a formal model of how Safety and Scalability are pieced together into an autonomous vehicles program that society can accept and is scalable in the sense of supporting millions of cars driving anywhere in the developed countries.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contribution of this paper is twofold. On the Safety front we introduce a model called "Responsibility Sensitive Safety" (RSS) which formalizes an interpretation of "Duty of Care" from Tort law. The Duty of Care states that an individual should exercise "reasonable care" while performing acts that could harm others. RSS is a rigorous mathematical model formalizing an interpretation of the law which is applicable to self-driving cars. RSS is designed to achieve three goals: first, the interpretation of the law should be sound in the sense that it complies with how humans interpret the law. While we are at it we would like also to prove "utopia" --- meaning that if all agents follow RSS's interpretation then there will be zero accidents. Second, the interpretation should lead to a useful driving policy, meaning it will lead to an agile driving policy rather than an overly-defensive driving which inevitably would confuse other human drivers and will block traffic and in turn limit the scalability of system deployment; third, the interpretation should be efficiently verifiable in the sense that we can rigorously prove that the self-driving car implements correctly the interpretation of the law.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The last property is not obvious at all because there could be many interpretations which are not analytically verifiable because of "butterfly effects" where a seemingly innocent action could lead to an accident of the agent's fault in the longer future.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

As highlighted in Fig. 1, guaranteeing that an agent will never be involved in an accident is impossible. Hence, our ultimate goal is to guarantee that an agent will be careful enough so as it will never be part of the *cause* of an accident. In other words, the agent should never cause an accident and should be cautious enough so as to be able to compensate for *reasonable* mistakes of other drivers. Also noteworthy, is that the definition of RSS is agnostic to the manner in which it is implemented --- which is a key feature to facilitate our goal of creating a convincing global safety model.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our second contribution evolves around the introduction of a "semantic" language that consists of units, measurements, and action space, and specification as to how they are incorporated into Planning, Sensing and Actuation of the autonomous vehicles. To get a sense of what we mean by Semantics, consider how a human taking driving lessons is instructed to think about "driving policy". These instructions are not geometric --- they do not take the form "drive 13.7 meters at the current speed and then accelerate at a rate of 0.8 $m/s^{2}$". Instead, the instructions are of a semantic nature --- "follow the car in front of you" or "overtake that car on your left". The language of human driving policy is about longitudinal and lateral goals rather than through geometric units of acceleration vectors. We develop a formal Semantic language and show that the Semantic model is crucial on multiple fronts connected to the computational complexity of Planning that do not scale up exponentially with time and number of agents, to the manner in which Safety and Comfort interact, to the way the computation of sensing is defined and the specification of sensor modalities and how they interact in a fusion methodology.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show how the resulting fusion methodology (based on the semantic language) guarantees the RSS model to the required $10^{- 9}$ probability of fatality, per one hour of driving, while performing only offline validation over a dataset of the order of $10^{5}$ hours of driving data.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, we show that in a reinforcement learning setting we can define the Q function^33^3A function evaluating the long term quality of performing an action $a \in A$ when the agent is at state $s \in S$. Given such a Q-function, the natural choice of an action is to pick the one with highest quality, ${\pi{(s)}} = {{\operatorname{argmax}_{a}Q}{(s,a)}}$. over actions defined over a semantic space in which the number of trajectories to be inspected at any given time is bounded by $10^{4}$ regardless of the time horizon used for Planning. Moreover, the signal to noise ratio in this space is high, allowing for effective machine learning approaches to succeed in modeling the Q function. In the case of computation of sensing, Semantics allow to distinguish between mistakes that affect Safety versus those mistakes that affect the Comfort of driving. We define a PAC model^44^4Probably Approximate Correct (PAC), borrowing Valiant's PAC-learning terminology.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

for sensing which is tied to the Q function and show how measurement mistakes are incorporated into Planning in a manner that complies with RSS yet allows to optimize the comfort of driving. The language of semantics is shown to be crucial for the success of this model as other standard measures of error, such as error with respect to a global coordinate system, do not comply with the PAC sensing model. In addition, the semantic language is also a critical enabler for defining HD-maps that can be constructed using low-bandwidth sensing data and thus be constructed through crowd-sourcing and support scalability.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

To summarize, we propose a formal model that covers all the important ingredients of an autonomous vehicle: sense, plan and act. The model guarantees that from a Planning perspective there will be no accidents which are caused by the autonomous vehicle, and also through a PAC sensing model guarantees that, with sensing errors, a fusion methodology we present will require only offline data collection of a very reasonable magnitude to comply with our Safety model. Furthermore, the model ties together Safety and Scalability through the language of semantics, thereby providing a complete methodology for a safe and scalable autonomous vehicles. Finally, it is worth noting that developing an accepted safety model that would be adopted by the industry and regulatory bodies is a necessary condition for the success of autonomous vehicles --- and it is better to do it earlier rather than later. An early adoption of a safety model will enable the industry to focus resources along a path that will lead to acceptance of autonomous vehicles. Our RSS model contains parameters whose values need to be determined through discussion with regulatory bodies and it would serve everyone if this discussion happens early in the process of developing autonomous vehicles solutions.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Safety: Functional versus Nominal", "weight": 1.0} -->

When dealing about safety it is important to bear in mind the distinction between *functional* versus *nominal* safety. Functional Safety (FuSa) refers to the integrity of the operation in an electrical (i.e. HW/SW) subsystem that is operating in a safety critical domain. Functional Safety is concerned with a failure in HW or bugs in the SW that could lead to a safety hazard. For the automotive industry this is well covered by ISO 26262 which defines different Automotive Safety Integrity Levels (ASIL) that provide Failure In Time (FIT) targets for HW and also define systematic processes for how SW should be defined, developed and tested such that it conforms with good systems engineering practices. These include the rigorous maintenance of requirements and traceability from those requirements to different safety goals of the system.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Safety: Functional versus Nominal", "weight": 1.0} -->

However, the most Functionally Safe vehicle in the world can still crash into everyone and everything due to bad logic in the code that results in an unsafe driving decision. Functional Safety cannot help us here; instead this is the domain of Nominal safety. Nominal safety is the concern of whether the AV is making safe logical decisions assuming that the HW and SW systems are operating error free (i.e. are functionally safe). Functional Safety then is a necessary, but not sufficient measure of safety assurance when it comes to evaluating the safety of an AV. In fact, there exists no nominal safety standard for the safe decision making capabilities of an AV. In the remainder of this paper, it is the nominal safety we focus.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Safety: Sense/Plan/Act Methodology", "weight": 1.0} -->

Automated Vehicles are robotic systems and contain three primary stages of functionality: Sense, Plan and Act. Sensing is the ability to accurately perceive the environment around the vehicle. Planning, commonly referred to as driving policy, is where decisions are made about what strategic (i.e. change lanes) and tactical (i.e. overtake the blue car) decisions to take. Acting is the issuance of the decision (translated into mathematical trajectories and velocities) to the various actuators within the vehicle to perform the driving decision. The focus of the paper is on the sensing and planning parts (since the acting part is by and large well understood by control theory).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Safety: Sense/Plan/Act Methodology", "weight": 1.0} -->

Mistakes that might lead to accidents can stem from sensing errors or planning errors. Validation of Sensing systems can be efficiently performed offline^55^5Strictly speaking, the vehicle actions might change the distribution over the way we view the environment. However, this dependency can be circumvented by data augmentation techniques. through the use of large ground truth data sets and sensing errors can be mitigated through redundant sensing modalities that ensure there are at least two independent subsystems to detect any one object, which also serves to simplify validation for each subsystem. A detailed description of the redundant system approach is given in Section 5.2. Planning on the other hand, presents unique validation challenges. Driving a vehicle is a multi-agent process and decisions should dependen on the actions and responses of others. This is why when humans take a driving test, we do not do so on a closed track but rather in the real world because it is only there that our multi-agent decision making capabilities can be sufficiently evaluated.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Safety: Sense/Plan/Act Methodology", "weight": 1.0} -->

In the next section we review existing approaches for evaluating the safety of planning, and in Section 3 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars") we describe our RSS model.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Existing Approaches to Claims on Safe AV Decision Making", "weight": 1.0} -->

Five approaches for evaluating the safety of AV are currently being promoted in the industry: miles driven, disengagements, simulation, scenario based testing and proprietary approaches.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Existing Approaches to Claims on Safe AV Decision Making", "weight": 1.0} -->

The "Miles driven" approach is based on a statistical argument attempting to show that self-driving cars are statistically better than human drivers. This approach is problematic because of the sheer amount of miles that would need to be driven to gain enough statistical evidence that a claimed probability of error (i.e. the chance of making an unsafe driving decision) has been met. In the following technical lemma, we formally show why a statistical approach to validation of an autonomous vehicles system is infeasible, even for validating a simple claim such as "on average, the system makes an accident once in $N$ hours".

<!-- chunk {"id": "body-0024", "role": "body", "section": "The Responsibility-Sensitive Safety (RSS) model for Multi-agent Safety", "weight": 1.0} -->

The discussion above focused on the shortcomings of the existing approaches for validating the nominal safety of an AV agent. Before we proceed, we should rule out what is clearly infeasible which is the naive statement that an AV, sharing the road with human-driven cars, will never be involved in an accident --- a statement we refer to as Utopia.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The Responsibility-Sensitive Safety (RSS) model for Multi-agent Safety", "weight": 1.0} -->

We say an action $a$ taken by a car $c$ is *absolutely safe* if no accident can follow it at some future time. It is easy to see that it is impossible to achieve absolute safety, by observing simple driving scenarios, for example, as depicted in Figure 1: from the central car's perspective, no action can ensure that none of the surrounding cars will crash into it, and no action can help it escape this potentially dangerous situation. We emphasize that solving this problem by forbidding the autonomous car from being in such situations is completely impossible --- every highway with more than 2 lanes will lead to it and forbidding this scenario amounts to staying in the parking lot.

<!-- chunk {"id": "body-0026", "role": "body", "section": "The Responsibility-Sensitive Safety (RSS) model for Multi-agent Safety", "weight": 1.0} -->

Instead we refer to the driving forces underlying human judgement when sharing the road with other road-users. Traffic laws are well defined until one encounters the elusive directive, common in Tort law, called *the Duty of Care*.

<!-- chunk {"id": "body-0027", "role": "body", "section": "The Responsibility-Sensitive Safety (RSS) model for Multi-agent Safety", "weight": 1.0} -->

The Duty of Care states that an individual should exercise "reasonable care" while performing acts that could harm others. What is meant in "being careful" is open for interpretation and must follow societal norms whose definitions are fluid, change over time, and gradually get clarified through legal precedents over past accidents that went through court proceedings for a resolution. A human driver must exercise care due to the uncertainty regarding the actions of other road users. If the driver must take into account the extreme worst case about the actions of other road users then driving becomes impossible. Hence, the human driver makes some "reasonable" assumptions about the worst case scenarios of other road-users. We refer to the assumptions being made as an "interpretation" of the Duty of Care law.

<!-- chunk {"id": "body-0028", "role": "body", "section": "The Responsibility-Sensitive Safety (RSS) model for Multi-agent Safety", "weight": 1.0} -->

Responsibility-Sensitive-Safety (RSS) is a rigorous mathematical model formalizing an interpretation of the Duty of Care law. RSS is designed to achieve three goals: first, the interpretation of the law should be sound in the sense that it complies with how humans interpret the law. While we are at it we would like also to prove "AI-Utopia" --- meaning that if all agents follow RSS interpretation then there will be zero accidents. Second, the interpretation should lead to a useful driving policy, meaning it will lead to an agile driving policy rather than an overly-defensive driving which inevitably would confuse other human drivers and will block traffic and in turn limit the scalability of system deployment; As an example of a valid, but not useful, interpretation is to assume that in order to be "careful" our actions should not affect other road users. Meaning, if we want to change lane we should find a gap large enough such that if other road users continue their own motion uninterrupted we could still squeeze-in without a collision. Clearly, for most societies this interpretation is over-cautious and will lead the AV to block traffic and be non-useful.

<!-- chunk {"id": "body-0029", "role": "body", "section": "The Responsibility-Sensitive Safety (RSS) model for Multi-agent Safety", "weight": 1.0} -->

Third, the interpretation should be efficiently verifiable in the sense that we can rigorously prove that the self-driving car implements correctly the interpretation of the law. The last property is not obvious at all because there could be many interpretations which are not analytically verifiable because of "butterfly effects" where a seemingly innocent action could lead to an accident of the agent's fault in the longer future. One way to ensure efficient verification is to design the interpretation to follow the inductive principle --- a feature we designed into the RSS.

<!-- chunk {"id": "body-0030", "role": "body", "section": "The Responsibility-Sensitive Safety (RSS) model for Multi-agent Safety", "weight": 1.0} -->

By and large, RSS is constructed by formalizing the following 5 "common sense" rules: Do not hit someone from behind.

<!-- chunk {"id": "body-0031", "role": "body", "section": "The Responsibility-Sensitive Safety (RSS) model for Multi-agent Safety", "weight": 1.0} -->

Be careful of areas with limited visibility If you can avoid an accident without causing another one, you must do it.

<!-- chunk {"id": "body-0032", "role": "body", "section": "The Responsibility-Sensitive Safety (RSS) model for Multi-agent Safety", "weight": 1.0} -->

The subsections below formalize those rules. We begin below with a simple scenario in order to get used to the concept we will be developing in the remainder of the paper.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Gentle Start --- Single Lane Road", "weight": 1.0} -->

We start with the simplest possible scenario: a single lane road, where cars cannot perform lateral manoeuvres. This scenario will allow us to introduce some first, simplistic versions of key concepts such as *safe distance*, *dangerous situation*, *proper response*, and *responsibility*. It also enables us to showcase our technique for formally proving the safety of a driving policy.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Gentle Start --- Single Lane Road", "weight": 1.0} -->

When driving along a single lane road, the common sense rule is "if someone hits you from behind it is not your fault". So, a first try would be to define that if a rear car, $c_{r}$, hits a front car, $c_{f}$, from behind, then $c_{r}$ is responsbile for the accident. But, this definition does not always comply with common sense. For example, suppose that both $c_{r}$ and $c_{f}$ are driving slowly up a hill, and then $c_{f}$ slows down and starts rolling backward until it hits $c_{r}$. Even though $c_{r}$ hit $c_{f}$ from behind, the common sense in this situation is that $c_{f}$ should be responsible.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Gentle Start --- Single Lane Road", "weight": 1.0} -->

We will get back to this issue in later subsections, so for the remainder of this subsection, we assume that cars never drive backward. We turn to discuss the more interesting question of: "how can $c_{r}$ ensure that it will never hit $c_{f}$ from behind". Intuitively, it is the responsibility of $c_{r}$ to keep a "safe distance" from $c_{f}$, and this "safe distance" should be large enough so that no matter what, $c_{r}$ will not hit $c_{f}$. In our simple case, the worst case situation is that $c_{f}$ will suddenly brake hard, it will take $c_{r}$ some time to figure this out and to brake as well, and then both cars will decelerate until reaching a full stop. A formalism of this concept is given below.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 1 (No contradictions and star-shape calculations)", "weight": 1.0} -->

Our definition of proper response enables *star-shape* calculations: we can consider the proper response of our car with respect to each other car individually, each proper response implies a constraint on the maximal acceleration we are allowed to perform, and taking the minimum of these constraints is guaranteed to satisfy all the constraints. Furthermore, the inductive proof technique relies on this pairwise structure. It is important to emphasize that there is an intimate relationship between the specific choice of definitions (of dangerous situation and proper response) and the ability to enable star-shape calculations and to make the inductive argument. To illustrate this point, suppose we would slightly change the definition of proper response, by also requiring the front car to accelerate a little bit when a rear car is approaching towards it fast from behind. In this case, we might reach contradictions: on one hand we should accelerate because someone approaches fast from behind, while on the other hand we need to brake because the car in front of us is braking. To resolve such contradictions we will need to consider all the vehicles together, which is expensive from computational perspective, and requires a different proof technique.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 1 (No contradictions and star-shape calculations)", "weight": 1.0} -->

Maintaining definitions which support efficient star-shape calculations and facilitate formal correctness in the full complexity of driving scenes (including lateral manoeuvres, junctions, pedestrians, and occlusions) is a great challenge that we tackle in this paper.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 2 (The parameters control the soundness/usefulness tradeoff)", "weight": 1.0} -->

The definitions of safe longitudinal distance and proper response depend on parameters: $\rho,a_{\max,{accel}},a_{\min,{brake}},a_{\max,{brake}}$. These parameters induce *assumptions* on the behavior of road agents---for example, the rear car assumes that the front car will not brake stronger than $a_{\max,{brake}}$, even if physically the front car is capable of braking stronger than that. If the front car brakes stronger than $a_{\max,{brake}}$, then the inductive proof breaks and there might be an accident. Since the rear car cannot know the exact braking mechanism of the front car, it has no way of knowing the exact value of $a_{\max,{brake}}$. Setting it to a very large value makes the model more sound (the number of cases in which the assumptions will not hold, and therefore the model will not capture reality, will be much smaller). On the other hand, a very large value of $a_{\max,{brake}}$ induces an extremely defensive driving.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 2 (The parameters control the soundness/usefulness tradeoff)", "weight": 1.0} -->

In the extreme case, when $a_{\max,{brake}} = \infty$, the safe distance formula states that we should refer to every car in front of us as if it stands still, which does not allow a normal flow of traffic.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 2 (The parameters control the soundness/usefulness tradeoff)", "weight": 1.0} -->

We therefore argue that these parameters should be determined to some reasonable values by regulation, as they induce a set of *allowed assumptions* that a driver (robotic or human) can make on the behavior of other road users.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 2 (The parameters control the soundness/usefulness tradeoff)", "weight": 1.0} -->

Of course, the parameters can be set differently for a robotic car and a human driven car. For example, the response time of a robotic car is usually smaller than that of a human driver and a robotic car can brake more effectively than a typical human driver, hence $a_{\min,{brake}}$ can set to be larger for a robotic car. They can also be set differently for different road conditions (wet road, ice, snow).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 3 (Utopia is possible)", "weight": 1.0} -->

Our inductive proof shows that if a car responds properly to dangerous situations then it will not hit another car from behind, as long as the front car will not brake stronger than $a_{\max,{brake}}$ (and will not drive backwards). This immediately implies that if all road users will adhere to the assumptions, and will respond properly to dangerous situations, then utopia is possible, in the sense that there will be no accidents. This strengthens the soundness of our definitions. While this claim is trivial for the simplistic case we are considering now, we will later show that it holds even when considering a much more complicated world (which includes lateral manoeuvres, different geometry, pedestrians, and occlusions).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 3 (Utopia is possible)", "weight": 1.0} -->

Having described the main idea behind our technique, we now turn to the harder part of constructing adequate definitions for all type of roads. We start with formally defining the notions of longitudinal and lateral position/velocity/acceleration.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Longitudinal Safe Distance and Proper Response", "weight": 1.0} -->

The definition of a safe distance from Section 3.1 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars") is sound for the case that both the rear and front cars are driving at the same direction. Indeed, in this case, it is the responsibility of the rear car to keep a safe distance from the front car, and to be ready for unexpected, yet reasonable, braking. However, when the two cars are driving at opposite directions, we need to refine the definition. Consider for example a car $c_{r}$ that is currently at a safe distance from a preceding car, $c_{f}$, that stands still. Suddenly, $c_{f}$ is reversing very fast into a parking spot and $c_{r}$ hits it from behind. Depending on the speed of $c_{f}$'s manoeuvre, the common sense here may be that the responsibility is not on the rear car, even though it hits $c_{f}$ from behind.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Longitudinal Safe Distance and Proper Response", "weight": 1.0} -->

To formalize this common sense, we simply note that the definitions of "rear and front" do not apply to scenarios in which vehicles are moving toward each other (namely, the signs of their longitudinal velocities are opposite). In such cases we expect both cars to decrease the *absolute value* of their velocity in order to avoid a crash.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Longitudinal Safe Distance and Proper Response", "weight": 1.0} -->

We could therefore define the safe distance between cars that drive in opposite directions to be the distance required so as if both cars will brake (after a response time) then there will be no crash. However, it makes sense that the car that drives at the opposite direction to the lane direction should brake harder than the one who drives at the correct direction. This leads to the following definition.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Lateral Safe Distance and Proper Response", "weight": 1.0} -->

Unlike longitudinal velocity, which can be kept to a value of $0$ for a long time (the car is simply not moving), keeping lateral velocity at exactly $0$ is impossible as cars usually perform small lateral fluctuations. It is therefore required to introduce a robust notion of lateral velocity.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 5", "weight": 1.0} -->

The definitions hold for vehicles of arbitrary shapes, by taking the worst-case with respect to all points of each car. In particular, this covers semi-trailers or a car with an open door.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Combining Longitudinal and Lateral Proper Responses", "weight": 1.0} -->

We next combine the longitudinal and lateral proper responses into a single proper response. We start with the case of a multi-lane road (typical highway situations or rural roads), where all lanes share the same geometry. In this case we can refer to all lanes as a single wide lane and the meaning of longitudinal and lateral position is well defined. Cases of multiple geometries (merges, junctions, roundabouts, etc.), and unstructured roads, are discussed in the next subsection, where we introduce the concept of priority.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Combining Longitudinal and Lateral Proper Responses", "weight": 1.0} -->

In order to have a collision between two cars, they must be both at a non-safe longitudinal distance and at a non-safe lateral distance.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Compensating for improper behavior of others", "weight": 1.0} -->

In the previous subsection we have shown that if all cars respond properly, according to the definition of basic proper response, then there will be no collisions. But, it may be the case that some agent does not respond properly, yet the other agent can prevent an accident. In such a case, it is reasonable to require that agents will do their "best effort" in order to avoid dangerous situations. On the other hand, we do not want that an attempt to avoid one accident would lead to another accident and we do not want that a requirement to avoid all accidents will severely harm the usefulness of the model (e.g., if the implication would be to always be at an extremely low speed).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Compensating for improper behavior of others", "weight": 1.0} -->

We tackle the tradeoff by introducing another layer of protection as follows. Suppose we are already at a dangerous situation with respect to some other agent and we figure out that if the other agent will keep its current behavior while we will keep applying proper response, there will be a collision. For example, consider the top row of Figure 3 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars"), where we are the yellow car. Our basic proper response is to not move laterally toward the red car and the red car's proper response is to stop its lateral movement toward us. Suppose the red car does not stop its lateral manoeuvre. To avoid a collision we can either brake longitudinally or move laterally to the left (or both). Any action for which there will be no collision, assuming the red car will keep its current behavior, is a fine evasive manoeuvre. Furthermore, even if a collision is not going to happen, we still don't want to be at a dangerous situation for a long time. Therefore, we should plan an action that will take us back to a non-dangerous situation.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Compensating for improper behavior of others", "weight": 1.0} -->

To make this formal we need some additional definitions.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Multiple Geometry and Right-of-Way Rules", "weight": 1.0} -->

We next turn to deal with scenarios in which there are multiple different road geometries in one scene that overlap in a certain area. Examples include roundabouts, junctions, and merge into highways. See Figure 4 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars") for illustration. In many such cases, one route has priority over others, and vehicles riding on it have the *right of way*.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Multiple Geometry and Right-of-Way Rules", "weight": 1.0} -->

In the previous subsections we could assume that the route is straight, by relying on Section 3.2 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars") that shows how to construct a bijection between a general lane geometry and a straight road, with a coherent meaning for longitudinal and lateral axes. When facing scenarios of multiple route geometries, the definitions should be adjusted. First, two routes with different geometries can yield conflicts in the constraints of the proper response. An example is given in Figure 5 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars").

<!-- chunk {"id": "body-0056", "role": "body", "section": "Multiple Geometry and Right-of-Way Rules", "weight": 1.0} -->

Moreover, consider the T-junction depicted on Figure 4(b) model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars"), and suppose that there is a stop sign for the red route. Suppose that $c_{1}$ is approaching the intersection on the yellow route and at the same time $c_{2}$ is approaching the intersection on the red route. According to the yellow route's coordinate system, $c_{2}$ has a very large lateral velocity, hence $c_{1}$ might deduce that $c_{2}$ is already at a non-safe lateral distance, which implies that $c_{1}$, driving on the prioritized route, must reduce speed in order to maintain a safe longitudinal distance to $c_{2}$. This means that $c_{2}$ should be very conservative w.r.t. traffic that coming from the red route. This is of course an unnatural behavior, as cars on the yellow route have the right-of-way in this case.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Multiple Geometry and Right-of-Way Rules", "weight": 1.0} -->

Furthermore, even $c_{2}$, who doesn't have the priority, should be able to merge into the junction as long as $c_{1}$ can stop in time (this will be crucial in dense traffic). This example shows that when $c_{1}$ drives on $r_{1}$, it doesn't make sense to consider its position and velocity w.r.t the coordinate system of $r_{2}$. As a result, we need to generalize basic notions from previous subsections such as "what does it mean that $c_{1}$ is in front of $c_{2}$", and what does it mean to be at a non safe distance.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 6", "weight": 1.0} -->

The definitions below assume that two cars, $c_{1},c_{2}$ are driving on different routes, $r_{1},r_{2}$. We emphasize that in some situations (for example, the T-junction given in Figure 4(b) model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars")), once there is exactly a single route $r_{1}$ such that both cars are assigned to it, and the time is not dangerous, then from that moment, the definitions are solely w.r.t. $r_{1}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 6", "weight": 1.0} -->

We start with generalizing the definition of safe lateral distance and lateral proper response. It is not hard to verify that applying the definition below to two routes of the same geometry indeed yields the same definition as in Definition 6 ‣ 3.4 Lateral Safe Distance and Proper Response ‣ 3 The Responsibility-Sensitive Safety (RSS) model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars"). Throughout this section, we sometimes refer to a route as a subset of ${\mathbb{R}}^{2}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Remark 7", "weight": 1.0} -->

One may worry that the longitudinal ordering definition is not robust, for example, in item of the definition, suppose that $c_{1},c_{2}$ are at distances of $20,20.1$ meters, respectively, from the intersection. This is not an issue as this definition is effectively being used only when there is a safe longitudinal distance between the two cars, and in that case the ordering between the cars will be obvious. Furthermore, this is exactly analogous to the non-robustness of ordering when two cars are driving side by side on a multi-lane highway road.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Remark 7", "weight": 1.0} -->

An illustration of the ordering definition is given in Figure 6 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars").

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 8 (No contradictions and star-shape calculations Revisited)", "weight": 1.0} -->

The updated definition of proper response is with respect to a pair of cars riding on a pair of routes. As before, we need to consider the proper response of our car with respect to each other car individually. That is, here again we adopt a *star-shape* calculation. Since the proper response with respect to every other car is translated to a lateral and longitudinal braking constraints with respect to *our route*, there can be no conflicts between proper responses with respect to different agents. For example, in the situation depicted on the left of Figure 5 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars"), the proper response with respect to the red car is a longitudinal brake, and hence it does not contradict the proper response of lateral brake with respect to the yellow car. As a result, it is easy to verify that our inductive proof sill holds. Finally, note that there are cases where the route used by another agent is unknown: for example, see Figure 8 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars"). In such case, every agent should comply with the proper response obtained by checking all possibilities.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Traffic Lights", "weight": 1.0} -->

We next discuss intersections with traffic lights. One might think that the simple rule for traffic lights scenarios is "if one car's route has the green light and the other car's route has a red light, then the blame is on the one whose route has the red light". However, this is not the correct rule. Consider for example the scenario depicted in Figure 9 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars"). Even if the yellow car's route has a green light, we do not expect it to ignore the red car that is already in the intersection. The correct rule is that the route that has a green light have a priority over routes that have a red light. Therefore, we obtain a clear reduction from traffic lights to the route priority concept we have described previously. The above discussion is a formalism of the common sense rule of right of way is given, not taken.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Unstructured Road", "weight": 1.0} -->

We next turn to consideration of unstructured roads, for example, see Figure 10 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars"). Consider first the scenario given in Figure 10(a) model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars"). Here, while the partition of the road area to lanes is not well defined, the partition of the road to multiple routes (with a clear geometry for every route) is well defined. Since our definitions of proper response only depend on the route geometry, they apply as is to such scenarios.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Unstructured Road", "weight": 1.0} -->

Next, consider the scenario where there is no route geometry at all (e.g. the parking lot given in Figure 10(b) model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars")). Unlike the structured case, in which we separated the lateral and longitudinal directions, here we need two dimensional trajectories.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Pedestrians", "weight": 1.0} -->

The proper response rules for avoiding collisions involving pedestrians (or other road users) follow the same ideas described in previous subsections, except that we need to adjust the parameters in the definitions of safe distance and proper response, as well as to specify pedestrians' routes (possibly unstructured routes) and their priority w.r.t. vehicles' routes. In some cases, a pedestrian's route is well defined (e.g. a zebra crossing or a sidewalk on a fast road). In other cases, like a typical residential street, we follow the approach we have taken for unstructured roads except that unlike vehicles that typically ride on circles, for pedestrians we constrain the change of heading, $|{h'{(t)}}|$, and assume that at emergency, after the response time, the pedestrian will continue at a straight line. If the pedestrian is standing, we assign it to all possible lines originating from his current position. The priority is set according to the type of the road and possibly based on traffic lights. For example, in a typical residential street, a pedestrian has the priority over the vehicles, and it follows that vehicles must yield and be cautious with respect to pedestrians.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Pedestrians", "weight": 1.0} -->

In contrast, there are roads with a sidewalk where the common sense behavior is that vehicles should not be worried that a pedestrian on the sidewalk will suddenly start running into the road. There, cars have the priority. Another example is a zebra crossing with a traffic light, where the priority is set dynamically according to the light. Of course, priority is given not taken, hence even if pedestrians do not have priority, if they entered the road at a safe distance, cars must brake and let them pass.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Pedestrians", "weight": 1.0} -->

Let us illustrate the idea by some examples. The first example is a pedestrian that stands on a residential road. The pedestrian is assigned to all routes obtained by rays originating from its current position. Her safe longitudinal distance w.r.t. each of these virtual routes is quite short. For example, setting a delay of $500$ ms, and maximal acceleration^1010^10As mentioned, the estimated acceleration of Usain Bolt is ${3.09m}/s^{2}$. and braking of ${2m}/s^{2}$, yields that her part of the safe longitudinal distance is $50cm$. It follows that a vehicle must be in a kinematic state such that if it will apply a proper response (acceleration for $\rho$ seconds and then braking) it will remain outside of a ball of radius $50cm$ around the pedestrian.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Pedestrians", "weight": 1.0} -->

A second example is a pedestrian standing on the sidewalk right in front of a zebra crossing, the pedestrian has a red light, and a vehicle approaches the zebra crossing at a green light. Here, the vehicle route has the priority, hence the vehicle can assume that the pedestrian will stay on the sidewalk. If the pedestrian enters the road while the vehicle is at a safe longitudinal distance (w.r.t. the vehicle's route), then the vehicle must brake ("right of way is given, not taken"). However, if the pedestrian enters the road while the vehicle is not at a safe longitudinal distance, and as a result the vehicle hits the pedestrian, then the vehicle is not responsible. It follows that in this situation, the vehicle can drive at a normal speed, without worrying about the pedestrian.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Pedestrians", "weight": 1.0} -->

The third example is a pedestrian that runs on a residential road at 10 km per hour (which is $\approx {{2.7m}/s}$). The possible future trajectories of the pedestrian form an isosceles triangle shape. Using the same parmeters as in the first example, the height of this triangle is roughly $15m$. It follows that cars should not enter the pedestrian's route at a distance smaller than $15m$. But, if the car entered the pedestrian's route at a distance larger than $15m$, and the pedestrian didn't stop and crashed into the car, then the responsibility is of the pedestrian.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Cautiousness with respect to Occlusion", "weight": 1.0} -->

A very common human response, when blamed for an accident, falls into the "but I couldn't see him" category. It is, many times, true. Human sensing capabilities are limited, sometimes because of an unaware decision to focus on a different part of the road, sometimes because of carelessness, and sometimes because of physical limitations - it is impossible to see a little kid hidden behind a parked car. While advanced automatic sensing systems are never careless, and have a $360^{\circ}$ view of the road, they might still suffer from limited sensing due to physical occlusions or range of sensor detection.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Example 1", "weight": 1.0} -->

A junction in which a building or a fence occludes traffic approaching the junction from a different route (see illustration in Figure 12 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars")).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Example 2", "weight": 1.0} -->

When changing lanes on a highway, there is a limited view range for detecting cars arriving from behind (see illustration in Figure 13 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars")).

<!-- chunk {"id": "body-0074", "role": "body", "section": "Example 3", "weight": 1.0} -->

A kid that might be occluded behind a parked car.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Example 4", "weight": 1.0} -->

An obstacle ahead which is occluded by the car in front of us (see illustration in Figure 14 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars")).

<!-- chunk {"id": "body-0076", "role": "body", "section": "Example 4", "weight": 1.0} -->

The examples above show that we might be in a dangerous situation without knowing it (due to the occlusion), and as a result we will not respond properly. When a human driver claims "but I couldn't see him", a counter argument is often "well, you should've been more careful". Analogously, we should formalize what does it mean to be careful.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Example 4", "weight": 1.0} -->

The extreme form of "being careful" is to assume the worst possible scenario. That is, we should assume that every occluded position in the world is occupied by a vehicle whose velocity is the worst possible. Unfortunately, without additional assumptions over the occluded object, this results in an over defensive, non natural driving. To see this, consider the simplest case of an occlusion by a static object, as given in Example 1 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars"), and depicted in Figure 12 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars"). In any position the yellow car is, there can be a very far red car which is occluded by the building. When the yellow car enters the corridor of the red car, there exists a high enough speed for the red car, for which this will be considered a non-safe cut-. This results in inability of the yellow car to merge into the main road. Of course, it is unreasonable to limit such manoeuvres.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Example 4", "weight": 1.0} -->

This motivates us to formalize several additional "reasonable assumptions" that a driver may make with regard to the behavior of other road users. Throughout this section, we implicitly defined "unreasonable situations" and allowed vehicles to make the "reasonable assumption" that such cases will not happen. For example, our basic definition of self longitudinal distance assumes that the other car will not brake stronger than $a_{\max,{brake}}$. By making this assumption, we implicitly say that a situation in which a vehicle brakes stronger than $a_{\max,{brake}}$ is an unreasonable situation, and we allow ourselves to not fear from such a case. Of course, we also required vehicles not to cause "unreasonable situations", for example, we should never brake stronger than $a_{\max,{brake}}$. To tackle occlusions, we follow the exact same rational, by defining situations that are unreasonable, and allowing the vehicle to assume they will not happen. So, the vehicle should plan for the worst case, except these unreasonable situations.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Example 4", "weight": 1.0} -->

As we will see, we also require the vehicle to take into account that other vehicles may not fully observe it, hence it should be careful not to cause unreasonable situations.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Example 4", "weight": 1.0} -->

To formalize the above, as a preliminary statement, it is clear that once an object becomes observed, we should act according to the regular proper response rules. We denote this point in time by the *Exposure Time*.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Responsibility", "weight": 1.0} -->

We have defined the notion of proper response to dangerous situations. Before an accident occurs, the situation must be dangerous. We say that an agent is *responsible* for the accident if it did not comply with the proper response contraints.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Responsibility", "weight": 1.0} -->

It is not hard to see that if there are no occlusions, if two agents collide then it must be the case that at least one of them did not comply with the proper response contraints, and this agent is responsible for the accident. However, when there are occlusions, there may be an accident with no clear responsibility. Consider for example Figure 14 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars"). On one hand, the yellow car is allowed to assume that if there is a vehicle $c_{2}$ in front of the red car, then the red car is applying proper response on it. So, the yellow car is not responsible for the accident. It is true that the red car did not respond properly on the blue car, but the red car was not involved in the accident at all so it is not clear if we can blame it for an accident between the yellow car and the blue car. In the next section we prove that if all the agents adhere to proper response rules, then no accidents would happen.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Utopia is Possible", "weight": 1.0} -->

In Lemma 5 model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars") we have shown that if all cars on the road comply with the basic proper response rules, then there will be no collisions. However, in the previous subsection we have shown that agents can make some reasonable assumptions on what happens at occluded areas, and as a result, there may be an accident between two agents where none of them is directly responsible. We now prove that even when considering occlusions, if all agents adhere to the proper response rules as given in Definition 26 ‣ 3.9 Cautiousness with respect to Occlusion ‣ 3 The Responsibility-Sensitive Safety (RSS) model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars"), then no accidents will happen.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Utopia is Possible", "weight": 1.0} -->

The proof technique relies on the lemma below, which shows that if *all* agents adhere to the proper response rules as given in Definition 26 ‣ 3.9 Cautiousness with respect to Occlusion ‣ 3 The Responsibility-Sensitive Safety (RSS) model for Multi-agent Safety ‣ On a Formal Model of Safe and Scalable Self-driving Cars"), they in fact also adhere to the basic proper response rules.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

A driving policy is a mapping from a sensing state (a description of the world around us) into a driving command (e.g., the command is lateral and longitudinal accelerations for the coming second, which determines where and at what speed should the car be in one second from now). The driving command is passed to a controller, that aims at actually moving the car to the desired position/speed.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

In the previous sections we described a formal safety model and proposed constraints on the commands issued by the driving policy that guarantee safety. The constraints on safety are designed for extreme cases. Typically, we do not want to even need these constraints, and would like to construct a driving policy that leads to a comfortable ride. The focus of this section is on how to build an efficient driving policy, in particular, one that requires computational resources that can scale to millions of cars. For now, we ignore the issue of how to obtain the sensing state and assume an utopic sensing state, that faithfully represents the world around us without any limitations. In later sections we will discuss the effect of inaccuracies in the sensing state on the driving policy.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

We can cast the problem of defining a driving policy in the language of Reinforcement Learning (RL). At each iteration of RL, an agent observes a state describing the world, denoted $s_{t}$, and should pick an action, denoted $a_{t}$, based on a policy function, $\pi$, that maps states into actions. As a result of its action and other factors out of its control (such as the actions of other agents), the state of the world is changed to $s_{t + 1}$. We denote a (state,action) sequence by $\overline{s} = {({(s_{1},a_{1})},{(s_{2},a_{2})},\ldots,{(s_{\text{len}{(\overline{s})}},a_{\text{len}{(\overline{s})}})})}$. Every policy induces a probability function over (state,action) sequences.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

This probability function is affected by the actions taken by the agent, but also depends on the environment (and in particular, on how other agents behave). We denote by $P_{\pi}$ the probability over (state,action) sequences induced by $\pi$. The quality of a policy is defined to be $\mathbb{E}_{\overline{s} \sim P_{\pi}}{\lbrack{\rho{(\overline{s})}}\rbrack}$, where $\rho{(\overline{s})}$ is a reward function that measures how good the sequence $\overline{s}$ is.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

In most case, $\rho{(\overline{s})}$ takes the form ${\rho{(\overline{s})}} = {\sum_{t = 1}^{\text{len}{(\overline{s})}}{\rho{(s_{t},a_{t})}}}$, where $\rho{(s,a)}$ is an instantaneous reward function, that measures the immediate quality of being at state $s$ and performing action $a$. For simplicity, we stick to this simpler case.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

To cast the driving policy problem in the above RL language, let $s_{t}$ be some representation of the road, and the positions, velocities, and accelerations, of the ego vehicle as well as other road users. Let $a_{t}$ be a lateral and longitudinal acceleration command. The next state, $s_{t + 1}$, depends on $a_{t}$ as well as on how the other agents will behave. The instantaneous reward, $\rho{(s_{t},a_{t})}$, may depend on the relative position/velocities/acceleration to other cars, the difference between our speed and the desired speed, whether we follow the desired route, whether our acceleration is comfortable etc.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

The main difficulty of deciding what action should the policy take at time $t$ stems from the fact that one needs to estimate the long term effect of this action on the reward. For example, in the context of driving policy, an action that is taken at time $t$ may seem a good action for the present (that is, the reward value $\rho{(s_{t},a_{t})}$ is good), but might lead to an accident after $5$ seconds (that is, the reward value in $5$ seconds would be catastrophic). We therefore need to estimate the long term quality of performing an action $a$ when the agent is at state $s$. This is often called the $Q$ function, namely, $Q{(s,a)}$ should reflect the long term quality of performing action $a$ at state $s$. Given such a $Q$ function, the natural choice of an action is to pick the one with highest quality, ${\pi{(s)}} = {{\operatorname{argmax}_{a}Q}{(s,a)}}$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

The immediate questions are how to define $Q$ and how to evaluate $Q$ efficiently. Let us first make the (completely non-realistic) simplifying assumption that $s_{t + 1}$ is some deterministic function of $(s_{t},a_{t})$, namely, $s_{t + 1} = {f{(s_{t},a_{t})}}$. The reader familiar with Markov Decision Processes (MDPs), will quickly notice that this assumption is even stronger than the Markovian assumption of MDPs (i.e., that $s_{t + 1}$ is conditionally independent of the past given $(s_{t},a_{t})$). As noted, even the Markovian assumption is not adequate for multi-agent scenarios, such as driving, and we will therefore later relax the assumption.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

Under this simplifying assumption, given $s_{t}$, for every sequence of decisions for $T$ steps, $(a_{t},\ldots,a_{t + T})$, we can calculate exactly the future states $(s_{t + 1},\ldots,s_{t + T + 1})$ as well as the reward values for times $t,\ldots,T$. Summarizing all these reward values into a single number, e.g. by taking their sum $\sum_{\tau = t}^{T}{\rho{(s_{\tau},a_{\tau})}}$, we can define $Q{(s,a)}$ as follows: That is, $Q{(s,a)}$ is the best future we can hope, if we are currently at state $s$ and immediately perform action $a$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

Let us discuss how to calculate $Q$. The first idea is to discretize the set of possible actions, $A$, into a finite set $\hat{A}$, and simply traverse all action sequences in the discretized set. Then, the runtime is dominated by the number of discrete action sequences, ${|\hat{A}|}^{T}$. If $\hat{A}$ represents $10$ lateral accelerations and $10$ longitudinal accelerations, we obtain $100^{T}$ possibilities, which becomes infeasible even for small values of $T$. While there are heuristics for speeding up the search (e.g. coarse-to-fine search), this brute-force approach requires tremendous computational power.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

The parameter $T$ is often called the "time horizon of planning", and it controls a natural tradeoff between computation time and quality of evaluation --- the larger $T$ is, the better our evaluation of the current action (since we explicitly examine its effect deeper into the future), but on the other hand, a larger $T$ increases the computation time exponentially. To understand why we may need a large value of $T$, consider a scenario in which we are 200 meters before a highway exit and we should take it. When the time horizon is long enough, the cumulative reward will indicate if at some time $\tau$ between $t$ and $t + T$ we have arrived to the exit lane. On the other hand, for a short time horizon, even if we perform the right immediate action we will not know if it will lead us eventually to the exit lane.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

A different approach attempts to perform offline calculations in order to construct an approximation of $Q$, denoted $\hat{Q}$, and then during the online run of the policy, use $\hat{Q}$ as an approximation to $Q$, without explicitly rolling out the future. One way to construct such an approximation is to discretize both the action domain and the state domain. Denote by $\hat{A},\hat{S}$ these discretized sets. We can perform an offline calculation for evaluating the value of $Q{(s,a)}$ for every ${(s,a)} \in {\hat{S} \times \hat{A}}$. Then, for every $a \in \hat{A}$ we define $\hat{Q}{(s_{t},a)}$ to be $Q{(s,a)}$ for $s = {\operatorname{argmin}_{s \in \hat{S}}{\|{s - s_{t}}\|}}$.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

Furthermore, based on the pioneering work of Bellman, we can calculate $Q{(s,a)}$ for every ${(s,a)} \in {\hat{S} \times \hat{A}}$, based on dynamic programming procedures (such as the Value Iteration algorithm), and under our assumptions, the total runtime is order of $T{|\hat{A}|}{|\hat{S}|}$. The main problem with this approach is that in any reasonable approximation, $\hat{S}$ is extremely large (due to the curse of dimensionality). Indeed, the sensing state should represent $6$ parameters for every other relevant vehicle in the sense --- the longitudinal and lateral position, velocity, and acceleration. Even if we discretize each dimension to only $10$ values (a very crude discretization), since we have $6$ dimensions, to describe a single car we need $10^{6}$ states, and to describe $k$ cars we need $10^{6k}$ states.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

This leads to unrealistic memory requirements for storing the values of $Q$ for every $(s,a)$ in $\hat{S} \times \hat{A}$.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

A popular approach to deal with this curse of dimensionality is to restrict $Q$ to come from a restricted class of functions (often called a hypothesis class), such as linear functions over manually determined features or deep neural networks. For example, learned a deep neural network that approximates $Q$ in the context of playing Atari games. This leads to a resource-efficient solution, provided that the class of functions that approximate $Q$ can be evaluated efficiently. However, there are several disadvantages of this approach. First, it is not known if the chosen class of functions contain a good approximation to the desired $Q$ function. Second, even if such function exists, it is not known if existing algorithms will manage to learn it efficiently. So far, there are not many success stories for learning a $Q$ function for complicated multi-agent problems, such as the ones we are facing in driving. There are several theoretical reasons why this task is difficult. We have already mentioned that the Markovian assumption, underlying existing methods, is problematic. But, a more severe problem is that we are facing a very small signal-to-noise ratio due to the time resolution of decision making, as we explain below.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

Consider a simple scenario in which we need to change lane in order to take a highway exit in $200$ meters and the road is currently empty. The best decision is to start making the lane change. We are making decisions every $0.1$ second, so at the current time $t$, the best value of $Q{(s_{t},a)}$ should be for the action $a$ corresponding to a small lateral acceleration to the right. Consider the action $a'$ that corresponds to zero lateral acceleration. Since there is a very little difference between starting the change lane now, or in $0.1$ seconds, the values of $Q{(s_{t},a)}$ and $Q{(s_{t},a')}$ are almost the same. In other words, there is very little *advantage* for picking $a$ over $a'$. On the other hand, since we are using a function approximation for $Q$, and since there is noise in measuring the state $s_{t}$, it is likely that our approximation to the $Q$ value is noisy.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

This yields a very small signal-to-noise ratio, which leads to an extremely slow learning, especially for stochastic learning algorithms which are heavily used for the neural networks approximation class. However, as noted, this problem is not a property of any particular function approximation class, but rather, it is inherent in the definition of the $Q$ function.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

In summary, existing approaches can be roughly divided into two camps. The first one is the brute-force approach which includes searching over many sequences of actions or discretizing the sensing state domain and maintaining a huge table in memory. This approach can lead to a very accurate approximation of $Q$ but requires unleashed resources, either in terms of computation time or in terms of memory. The second one is a resource efficient approach in which we either search for short sequences of actions or we apply a function approximation to $Q$. In both cases, we pay by having a less accurate approximation of $Q$, that might lead to poor decisions.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Driving Policy", "weight": 1.0} -->

Our approach to constructing a $Q$ function that is both resource-efficient and accurate is to depart from geometrical actions and to adapt a semantic action space, as described in the next subsection.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Semantics to the rescue", "weight": 1.0} -->

To motivate our semantic approach, consider a teenager that just got his driving license. His father seats next to him and gives him "driving policy" instructions. These instructions are not geometric --- they do not take the form "drive 13.7 meters at the current speed and then accelerate at a rate of 0.8 $m/s^{2}$". Instead, the instructions are of semantic nature --- "follow the car in front of you" or "quickly overtake that car on your left". We formalize a semantic language for such instructions, and use them as a semantic action space. We then define the $Q$ function over the semantic action space. We show that a semantic action can have a very long time horizon, which allows us to estimate $Q{(s,a)}$ without planning for many future semantic actions. Yet, the total number of semantic actions is still small. This allows us to obtain an accurate estimation of the $Q$ function while still being resource efficient. Furthermore, as we show later, we combine learning techniques for further improving the quality function, while not suffering from a small signal-to-noise ratio due to a significant difference between different semantic actions.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Semantics to the rescue", "weight": 1.0} -->

We now define our semantic action space. The main idea is to define lateral and longitudinal goals, as well as the aggressiveness level of achieving them. Lateral goals are desired positions in lane coordinate system (e.g., "my goal is to be in the center of lane number 2"). Longitudinal goals are of three types. The first is relative position and speed w.r.t. other vehicles (e.g., "my goal is to be behind car number 3, at its same speed, and at a distance of $2$ seconds from it"). The second is a speed target (e.g., "drive at the allowed speed for this road times 110%"). The third is a speed constraint at a certain position (e.g., when approaching a junction, "speed of 0 at the stop line", or when passing a sharp curve, "speed of at most 60kmh at a certain position on the curve"). For the third option we can instead apply a "speed profile" (few discrete points on the route and the desired speed at each of them).

<!-- chunk {"id": "body-0106", "role": "body", "section": "Semantics to the rescue", "weight": 1.0} -->

A reasonable number of lateral goals is bounded by $16 = {4 \times 4}$ ($4$ positions in at most $4$ relevant lanes). A reasonable number of longitudinal goals of the first type is bounded by ${8 \times 2 \times 3} = 48$ ($8$ relevant cars, whether to be in front or behind them, and $3$ relevant distances). A reasonable number of absolute speed targets are $10$, and a reasonable upper bound on the number of speed constraints is $2$. To implement a given lateral or longitudinal goal, we need to apply acceleration and then deceleration (or the other way around). The aggressiveness of achieving the goal is a maximal (in absolute value) acceleration/deceleration to achieve the goal. With the goal and aggressivness defined, we have a closed form formula to implement the goal, using kinematic calculations. The only remaining part is to determine the combination between the lateral and longitudinal goals (e.g., "start with the lateral goal, and exactly at the middle of it, start to apply also the longitudinal goal").

<!-- chunk {"id": "body-0107", "role": "body", "section": "Semantics to the rescue", "weight": 1.0} -->

A set of $5$ mixing times and $3$ aggressiveness levels seems more than enough. All in all, we have obtained a semantic action space whose size is $\approx 10^{4}$.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Semantics to the rescue", "weight": 1.0} -->

It is worth mentioning that the variable time required for fulfilling these semantic actions is not the same as the frequency of the decision making process. To be reactive to the dynamic world, we should make decisions at a high frequency --- in our implementation, every 100ms. In contrast, each such decision is based on constructing a trajectory that fulfills some semantic action, which will have a much longer time horizon (say, 10 seconds). We use the longer time horizon since it helps us to better evaluate the short term prefix of the trajectory. In the next subsection we discuss the evaluation of semantic actions, but before that, we argue that semantic actions induce a sufficient search space.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Is this sufficient", "weight": 1.0} -->

We have seen that a semantic action space induces a subset of all possible geometrical curves, whose size is exponentially smaller (in $T$) than enumerating all possible geometrical curves. The first immediate question is whether the set of short term prefixes of this smaller search space contains all geometric commands that we will ever want to use. We argue that this is indeed sufficient in the following sense. If the road is free of other agents, then there is no reason to make changes except setting a lateral goal and/or absolute acceleration commands and/or speed constraints on certain positions. If the road contains other agents, we may want to negotiate the right of way with the other agents. In this case, it suffices to set longitudinal goals relatively to the other agents. The exact implementation of these goals in the long run may vary, but the short term prefixes will not change by much. Hence, we obtain a very good cover of the relevant short term geometrical commands.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Constructing an evaluation function for semantic actions", "weight": 1.0} -->

We have defined a semantic set of actions, denoted by $A^{s}$. Given that we are currently in state $s$, we need a way to choose the best $a^{s} \in A^{s}$. To tackle this problem, we follow a similar approach to the *options mechanism* of. The basic idea is to think of $a^{s}$ as a meta-action (or an option). For each choice of a meta-action, we construct a geometrical trajectory ${(s_{1},a_{1})},\ldots,{(s_{T},a_{T})}$ that represents an implementation of the meta-action, $a^{s}$. To do so we of course need to know how other agents will react to our actions, but for now we are still relying on (the non-realistic) assumption that $s_{t + 1} = {f{(s_{t},a_{t})}}$ for some known deterministic function $f$.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Constructing an evaluation function for semantic actions", "weight": 1.0} -->

Most of the time, this simple approach yields a powerful driving policy. However, in some situations a more sophisticated quality function is required. For example, suppose that we are following a slow truck before an exit lane, where we need to take the exit lane. One semantic option is to keep driving slowly behind the truck. Another one is to overtake the truck, hoping that later we can get back to the exit lane and make the exit on time. The quality measure described previously does not consider what will happen after we will overtake the truck, and hence we will not choose the second semantic action even if there is enough time to make the overtake and return to the exit lane. Machine learning can help us to construct a better evaluation of semantic actions, that will take into account more than the immediate semantic actions. Previously, we have argued that learning a $Q$ function over immediate geometric actions is problematic due to the low signal-to-noise ratio (the lack of advantage). This is not problematic when considering semantic actions, both because there is a large difference between performing the different semantic actions and because the semantic time horizon (how many semantic actions we take into account) is very small (probably less than three in most cases).

<!-- chunk {"id": "body-0112", "role": "body", "section": "Constructing an evaluation function for semantic actions", "weight": 1.0} -->

Another advantage of applying machine learning is for the sake of *generalization*: we can probably set an adequate evaluation function for *every* road, by a manual inspection of the properties of the road, and maybe some trial and error. But, can we automatically generalize to *any* road? Here, a machine learning approach can be trained on a large variety of road types so as to generalize to unseen roads as well.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Constructing an evaluation function for semantic actions", "weight": 1.0} -->

To summarize, our semantic action space allows to enjoy the benefits of both worlds: semantic actions contain information on a long time horizon, hence we can obtain a very accurate evaluation of their quality while being resource efficient.

<!-- chunk {"id": "body-0114", "role": "body", "section": "The dynamics of the other agents", "weight": 1.0} -->

So far, we have relied on the assumption that $s_{t + 1}$ is a deterministic function of $s_{t}$ and $a_{t}$. As we have emphasized previously, this assumption is completely not realistic as our actions affect the behavior of other road users. While we do take into account some reactions of other agents to our actions (for example, we assume that if we will perform a safe cut-, then the car behind us will adjust its speed so as not to hit us from behind), it is not realistic to assume that we model all of the dynamics of other agents.

<!-- chunk {"id": "body-0115", "role": "body", "section": "The dynamics of the other agents", "weight": 1.0} -->

The solution to this problem is to re-apply our decision making at a high frequency, and by doing this, we constantly adapt our policy to the parts of the environment that are beyond our modeling. In a sense, one can think of this as a Markovization of the world at every step. This is a common technique that tends to work very good in practice as long as the balance between modeling error and frequency of planning is adequate.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Sensing", "weight": 1.0} -->

In this section we describe the sensing state, which is a description of the relevant information of the scene, and forms the input to the driving policy module. By and large, the sensing state contains static and dynamic objects. The static objects are lanes, physical road delimiters, constraints on speed, constraints on the right of way, and information on occluders (e.g. a fence that occludes relevant part of a merging road). Dynamic objects are vehicles (bounding box, speed, acceleration), pedestrians (bounding box, speed, acceleration), traffic lights, dynamic road delimiters (e.g. cones at a construction area), temporary traffic signs and police activity, and other obstacles on the road (e.g. an animal, a mattress that fell from a truck, etc.).

<!-- chunk {"id": "body-0117", "role": "body", "section": "Sensing", "weight": 1.0} -->

In any reasonable sensor setting, we cannot expect to obtain the exact sensing state, $s$. Instead, we view raw sensor and mapping data, which we denote by $x \in X$, and there is a sensing system that takes $x$ and produces an approximate sensing state. Formally,

<!-- chunk {"id": "body-0118", "role": "body", "section": "Comfort", "weight": 1.0} -->

But, it is also not bad at all to pick $\pi{({\hat{s}{(x)}})}$ as long as the quality of $\pi{({\hat{s}{(x)}})}$ w.r.t. the true state, $s$, is almost optimal, namely, ${Q{(s,{\pi{({\hat{s}{(x)}})}})}} \geq {{Q{(s,{\pi{(s)}})}} - \epsilon}$, for some parameter $\epsilon$. We say that $\hat{s}$ is $\epsilon$-accurate w.r.t. $Q$ in such case. Naturally, we cannot expect the sensing system to be $\epsilon$-accurate all the time. We therefore also allow the sensing system to fail with some small probability $\delta$. In such a case we say that $\hat{s}$ is Probably (w.p.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Comfort", "weight": 1.0} -->

of at least $1 - \delta$), Approximately (up to $\epsilon$), Correct, or PAC for short (borrowing Valiant's PAC learning terminology ).

<!-- chunk {"id": "body-0120", "role": "body", "section": "Comfort", "weight": 1.0} -->

We may use several $(\epsilon,\delta)$ pairs for evaluating different aspects of the system. For example, we can choose three thresholds, $\epsilon_{1} < \epsilon_{2} < \epsilon_{3}$ to represent mild, medium, and gross mistakes, and for each one of them set a different value of $\delta$. This leads to the following definition.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Safety", "weight": 1.0} -->

We now discuss sensing mistakes that lead to non-safe behavior. As mentioned before, our policy is provably safe, in the sense that it won't lead to accidents of the autonomous vehicle's blame. Such accidents might still occur due to hardware failure (e.g., a break down of all the sensors or exploding tire on the highway), software failure (a significant bug in some of the modules), or a sensing mistake. Our ultimate goal is that the probability of such events will be extremely small --- a probability of $10^{- 9}$ for such an accident per hour. To appreciate this number, the average number of hours an american driver spends on the road is less than $300$. So, in expectation, one needs to live 3.3 million years to be in an accident.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Safety", "weight": 1.0} -->

Roughly speaking, there are two types of safety-critic sensing mistake. The first type is a *safety-critic miss*, meaning that a dangerous situation is considered non-dangerous according to our sensing system. The second type is a *safety-critic ghost*, meaning that a non-dangerous situation is considered dangerous according to our sensing system. Safety-critic misses are obviously dangerous as we will not know that we should respond properly to the danger. Safety-critic ghosts might be dangerous when our speed is high, we brake hard for no reason, and there is a car behind us.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Safety", "weight": 1.0} -->

Usually, a safety-critic miss is caused by a false negative while a safety-critic ghost is caused by a false positive. Such mistakes can also be caused from significantly incorrect measurements, but in most cases, our comfort objective ensures we are far away from the boundaries of non-safe distances, and therefore reasonable measurement errors are unlikely to lead to safety-critic mistakes.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Safety", "weight": 1.0} -->

How can we ensure that the probability of safety-critic mistakes will be very small, say, smaller than $10^{- 9}$ per hour? As followed from Lemma 1, without making further assumptions we need to check our system on more than $10^{9}$ hours of driving. This is unrealistic (or at least extremely challenging) --- it amounts to recording the driving of $3.3$ million cars over a year. Furthermore, building a system that achieves such a high accuracy is a great challenge. Our solution for both the system design and validation challenges is to rely on several sub-systems, each of which is engineered independently and depends on a different technology, and the systems are fused together in a way that ensures boosting of their individual accuracy.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Safety", "weight": 1.0} -->

Suppose we build $3$ sub-systems, denoted, $s_{1},s_{2},s_{3}$ (the extension to more than $3$ is straightforward). Each sub-system should decide if the current situation is dangerous or not. Situations which are non-dangerous according to the majority of the sub-systems ($2$ in our case) are considered safe.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Safety", "weight": 1.0} -->

Let us now analyze the performance of this fusion scheme.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Remark 9", "weight": 1.0} -->

Our definition of safety-critic ghost requires that the situation is dangerous by at least two sensors. We argue that even in difficult conditions (e.g. heavy fog), this is unlikely to happen. The reason is that in such situations, systems that are affected by the difficult conditions (e.g. the lidar), will dictate a very defensive driving to the policy, as they can declare that high velocity and lateral maneuvers would lead to a dangerous situation. As a result, we will drive slowly, and then even if we require an emergency stop, it is not dangerous due to the low speed of driving. Therefore, an adaptation of the driving style to the conditions of the road will follow from the definitions.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Building a scalable sensing system", "weight": 1.0} -->

We have described the requirements from a sensing system, both in terms of comfort and safety. We now briefly suggest our approach for building a sensing system that meets these requirements while being scalable.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Building a scalable sensing system", "weight": 1.0} -->

There are three main components of our sensing system. The first is long range, $360$ degrees coverage, of the scene based on cameras. The three main advantages of cameras are: high resolution, texture, price. The low price enables a scalable system. The texture enables to understand the semantics of the scene, including lane marks, traffic light, intentions of pedestrians, and more. The high resolution enables a long range of detection. Furthermore, detecting lane marks and objects in the same domain enables excellent semantic lateral accuracy. The two main disadvantages of cameras are: the information is 2D and estimating longitudinal distance is difficult, sensitivity to lighting conditions (low sun, bad weather). We overcome these difficulties using the next two components of our system.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Building a scalable sensing system", "weight": 1.0} -->

The second component of our system is a semantic high-definition mapping technology, called Road Experience Management (REM). A common geometrical approach to map creation is to record a cloud of 3D points (obtained by a lidar) in the map creation process, and then, localization on the map is obtained by matching the existing lidar points to the ones in the map. There are several disadvantages of this approach. First, it requires a large memory per kilometer of mapping data, as we need to save many points. This necessitates an expensive communication infrastructure. Second, only few cars are equipped with lidar sensors, and therefore, the map is updated very infrequently. This is problematic as changes in the road can occur (construction zones, hazards), and the "time-to-reflect-reality" of lidar-based mapping solutions is large. In contrast, REM follows a semantic-based approach. The idea is to leverage the large number of vehicles that are equipped with cameras and with software that detects semantically meaningful objects in the scene (lane marks, curbs, poles, traffic lights, etc.).

<!-- chunk {"id": "body-0131", "role": "body", "section": "Building a scalable sensing system", "weight": 1.0} -->

Nowadays, many new cars are equipped with ADAS systems which can be leveraged for crowd source based creation of the map. Since the processing is done on the vehicle side, only a small amount of semantic data should be communicated to the cloud. This allows a very frequent update of the map in a scalable way. In addition, the autonomous vehicles can receive the small sized mapping data over existing communication platforms (the cellular network). Finally, highly accurate localization on the map can be obtained based on cameras, without the need for expensive lidars.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Building a scalable sensing system", "weight": 1.0} -->

REM is used for three purposes. First, it gives us a foresight on the static structure of the road (we can plan for a highway exit way in advance). Second, it gives us another source of accurate information of all of the static information, which together with the camera detections yields a robust view of the static part of the world. Third, it solves the problem of lifting the 2D information from the image plane into the 3D world as follows. The map describes all of the lanes as curves in the 3D world. Localization of the ego vehicle on the map enables to trivially lift every object on the road from the image plane to its 3D position. This yields a positioning system that adheres to the accuracy in semantic units described in Section 5.1.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Building a scalable sensing system", "weight": 1.0} -->

The third component of our system is a complementary radar and lidar system. This system serves two purposes. First, they enable to yield an extremely high accuracy for the sake of safety (as described in Section 5.2). Second, they give direct measurements on speed and distances, which further improves the comfort of the ride.
