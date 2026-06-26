<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Gentle Lecture Note on Filtrations in Reinforcement Learning

Topics include Reinforcement learning, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This note aims to provide a basic intuition on the concept of filtrations as used in the context of reinforcement learning (RL). Filtrations are often used to formally define RL problems, yet their implications might not be eminent for those without a background in measure theory. Essentially, a filtration is a construct that captures partial knowledge up to time t, without revealing any future information that has already been simulated, yet not revealed to the decision-maker. We illustrate this with simple examples from the finance domain on both discrete and continuous outcome spaces. Furthermore, we show that the notion of filtration is not needed, as basing decisions solely on the current problem state (which is possible due to the Markovian property) suffices to eliminate future knowledge from the decision-making process.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

This note aims to provide a basic intuition on the concept of filtrations as used in the context of reinforcement learning (RL). Filtrations are often used to formally define RL problems, yet their implications might not be eminent for those without a background in measure theory. Essentially, a filtration is a construct that captures partial knowledge up to time $t$, without revealing any future information that has already been simulated, yet not revealed to the decision-maker. We illustrate this with simple examples from the finance domain on both discrete and continuous outcome spaces. Furthermore, we show that the notion of filtration is not needed, as basing decisions solely on the current problem state (which is possible due to the Markovian property) suffices to eliminate future knowledge from the decision-making process.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Abstract", "weight": 1.5} -->

When reinforcement learning (RL) problems are introduced, papers typically start with some generic Markov Decision Process (MDP) model that looks something like $(\mathcal{S},{\mathcal{X}{(S_{t + 1})}},{{\mathbb{P}}^{\Omega}{({S_{t + 1} \mid {S_{t},x_{t}}})}},{R{(S_{t},x_{t})}},\rho)$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Abstract", "weight": 1.5} -->

In this tuple, $\mathcal{S}$ defines the set of all problem states, $\mathcal{X}{(S_{t})}$ describes the set of feasible decisions (given some state $S_{t} \in \mathcal{S}$), ${\mathbb{P}}^{\Omega}{({S_{t + 1} \mid {S_{t},x_{t}}})}$ is the probability measure on outcome space (also known as sample space) $\Omega$ that describes state transitions (a probability mass function for discrete outcome spaces and a probability density function for continuous outcome spaces), $R{(S_{t},x_{t})}$ is the reward function that computes rewards for a given state-action pair, and $\rho \in {}$ is the discount factor for future rewards. The outcome space $\Omega$ includes all possible events that may occur, with $\omega \in \Omega$ representing a particular realization of an event path (or sample path) in the outcome space.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Abstract", "weight": 1.5} -->

This paper assumes a finite time horizon $\mathcal{T} = {\{ 0,1,\ldots,T\}}$, in this case we may define $\omega = {\{\omega_{1},\omega_{2},\ldots,\omega_{T}\}}$ as the ordered set of events, which combined with the initial state $S_{0}$ and the sequence of decisions enables to compute all states that are visited. Finally, the Markovian property -- also known as memoryless property -- by definition holds for any MDP, meaning that the probability measure ${\mathbb{P}}^{\Omega}$ is conditional only on the present state, not on states and events in the past.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Abstract", "weight": 1.5} -->

Reinforcement learning aims to approximately solve MDP models and find a decision-making policy $\pi:{S_{t}\mapsto x_{t}}$. Whatever flavor of RL is used, at the framework's core Monte Carlo simulation is performed to repeatedly sample paths in the outcome space and learn good decisions based on these observed paths. In line with ${\mathbb{P}}^{\Omega}$ we sample random variables $W_{t}$ with realizations $W_{t} = \omega_{t}$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Abstract", "weight": 1.5} -->

In addition to the aforementioned model conventions, it is often mentioned that the decision-making policy is $\mathcal{F}_{t}$-measurable, that we deal with a filtered probability space, or that the expected value is conditional on a filtration; this notion of 'filtration' originates from the field of measure theory. Particularly for RL researchers from more applied backgrounds, the implications of a filtered probability space might not be eminent. When looking up the corresponding textbook definition of filtrations (see, e.g.,), you will probably find something like this: > Let $(W_{1},W_{2},\ldots,W_{T})$ be the sequence of information variables defined over $\mathcal{T}$, containing an ordered set of exogenous information $W_{t}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Abstract", "weight": 1.5} -->

Let $\omega \in \Omega$ be a sample sequence of an event realization ${W_{1} = \omega_{1}},{{W_{2} = {\omega_{2},\ldots}},{W_{T} = \omega_{T}}}$. Furthermore, let $\mathcal{F}$ be the $\sigma$-algebra on $\Omega$, capturing all possible events included in $\Omega$. The set $\mathcal{F}$ is composed of all countable unions and complements of the elements defined in $\Omega$. Let ${\mathbb{P}}^{\Omega}$ be a probability measure on $(\Omega,\mathcal{F})$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Abstract", "weight": 1.5} -->

Let $\mathcal{F}_{t} = {\sigma{(W_{1},\ldots,W_{t})}}$ be the $\sigma$-algebra generated by the process $(W_{1},\ldots,W_{t})$, containing all subsets of $\Omega$ conditional on the information sequence that has been revealed up to time $t$. The sequence $\mathcal{F}_{0},\mathcal{F}_{1},\ldots,\mathcal{F}_{t}$ is a filtration that is subject to ${\mathcal{F}_{t} \subseteq \mathcal{F}_{t + 1}},{{\forall t} \in \mathcal{T}}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Abstract", "weight": 1.5} -->

Although such introductions are needed to rigorously define the concept, they do not necessarily offer an intuitive understanding. We therefore provide a (hopefully) more intuitive background, followed by a toy-sized example. From a mathematical perspective, the outcome space $\Omega$ is simply a set containing elements $\omega$. In an RL context the term 'sample space' is often more appropriate, as we randomly sample outcomes while simulating time transitions. Examples of the outcome space might be: the attainable outcomes of the cast of a die, the possible movements of a stock price, potential arrivals of new jobs, etc. At this point, it is appropriate to define the event $A \in \Omega$, which for convenience we may think of as a set of outcomes with a corresponding 'yes' answer or some common property. The complementary set $A^{C}$ is the set where the answer is 'no' or the property is absent. Each event has a positive probability that we can measure, e.g., the probability that a random number falls within a certain interval.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Abstract", "weight": 1.5} -->

A filtration essentially is a mathematical model that represents partial knowledge about the outcome. Intuitively, if $\mathcal{F}_{t}$ is the filtration and $A \in \Omega$, then if $A \in \mathcal{F}_{t}$ we know whether $\omega \in A$ or not. In plain words: the filtration tells us whether an event happened or not. Furthermore, the filtration expands with the passing of time, as indicated by the property $\mathcal{F}_{t} \subseteq \mathcal{F}_{t + 1}$. One may envision the 'filtration process' as a sequence of filters, each filter providing us a more detailed view of the events in $\Omega$. In the context of MDPs and RL, a filtration $\mathcal{F}_{t}$ provides us with the necessary information to compute the current state $S_{t}$. At the same time, the information embedded in the filtration cannot give any indication of future changes in the process.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Abstract", "weight": 1.5} -->

We know the event path up to $t$, but not the events that will occur after that. Observe that this observation coincides with the Markovian property.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Abstract", "weight": 1.5} -->

As a filtration is a $\sigma$-algebra, a basic understanding of $\sigma$-algebras is essential, although we need not to discuss them in great detail. Loosely defined, a $\sigma$-algebra is a collection of subsets of the outcome space, containing a countable number of events as well as all their complements and unions. Essentially, the $\sigma$-algebra allows to define certain measures (e.g., length, volume), which would not be possible for every subset of the outcome space.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Abstract", "weight": 1.5} -->

We proceed to introduce an example. To illustrate the concept of filtration as simply as possible, we introduce a problem setting in which the state $S_{t} \in {\mathbb{R}}^{+}$ represents the price of a given financial stock at time $t$. No other model information is needed for this exercise, although for practical purposes you might imagine that you aim to buy at a low price and sell at a high price to lock in profits. Suppose the initial stock price is defined by $S_{0}$ and we have a time horizon composed of three discrete time steps ($T = 3$). We define a simplified binomial lattice model to reflect price movements: at each time step the stock price can go either up ($u$) or down ($d$). The realizations $u$ and $d$ are added to (subtracted from) the preceding price ($S_{1} = {S_{0} + u}$ or $S_{1} = {S_{0} - d}$), for details on binomial lattices we refer the interested reader to.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Abstract", "weight": 1.5} -->

In terms of samples, we have ${\omega_{t} \in {\{ u,d\}}},{{\forall t} \in \mathcal{T}}$ and $\omega = {\{\omega_{1},\omega_{2},\omega_{3}\}}$ describes a realization of a price path, e.g., $\omega = {\{ u,d,u\}}$. The binomial lattice corresponding to the example is depicted in Figure 1.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Abstract", "weight": 1.5} -->

We now introduce the events corresponding to the price movements. We will see that the information embedded in the filtrations becomes increasingly detailed and specific over time. At $t = 0$, all paths are possible. Thus, the event set $A = {\{{uuu},{uud},{udu},{udd},{ddd},{ddu},{dud},{duu}\}}$ -- with the sequences describing the movement per time step -- contains all possible paths $\omega \in \Omega$, such that $A \equiv \Omega$. At $t = 1$, we know that the stock price went either up or down. The corresponding events can be defined by $A_{u} = {\{{uuu},{uud},{udu},{udd}\}}$ and $A_{d} = {\{{ddd},{ddu},{dud},{duu}\}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Abstract", "weight": 1.5} -->

Note that if the price went up, we know our sample path $\omega$ will be in $A_{u}$ and not in $A_{d}$. At $t = 2$, we have four event sets: $A_{uu} = {\{{uuu},{uud}\}}$, $A_{ud} = {\{{udu},{udd}\}}$, $A_{du} = {\{{duu},{dud}\}}$, and $A_{dd} = {\{{ddu},{ddd}\}}$. Observe that the information is getting increasingly fine-grained; the sets to which $\omega$ might belong are becoming smaller and more numerous. At $t = 3$, we obviously know the exact price path that has been followed.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Abstract", "weight": 1.5} -->

Having defined the events, we can define the corresponding filtrations for $t = {0,1,2,3}$: For $\mathcal{F}_{0}$, it is eminent that any $\omega$ must belong to $\Omega$ and not to $\varnothing$. We have not observed any information that allows for a more accurate classification. For $\mathcal{F}_{1}$, we can define two more sets to which $\omega$ may belong. Due to observing the first price change, we are now able to assign $\omega$ to $A_{u}$ or $A_{d}$; we may state that these sets are 'resolved'. When moving to $\mathcal{F}_{2}$, things get slightly more involved. Whenever we have resolved a set, we have also resolved its complement.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Abstract", "weight": 1.5} -->

In $\mathcal{F}_{1}$ we had $A_{u}^{C} = A_{d}$ and vice versa, but for $\mathcal{F}_{2}$ we must explicitly define the complements (e.g., a path either is in $A_{uu}$ or in $A_{uu}^{C}$). Finally, whenever multiple sets are resolved, so is their union. Again, in $\mathcal{F}_{1}$ we had ${A_{u} \cup A_{d}} = \Omega$, so an explicit union definition was not necessary. For $\mathcal{F}_{2}$ however, we must explicitly include the unions, e.g., $A_{ud} \cup A_{dd}$. Note that the triple unions are equivalent to complements and that the quadruple union equals the outcome space.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Abstract", "weight": 1.5} -->

From this example it can be seen that $\mathcal{F}_{t} \subseteq \mathcal{F}_{t + 1}$ indeed holds. The filtration at time $t$ embeds all event sets that can be distinguished up until that point, based on the possible realizations of the random variables $W_{1},\ldots,W_{t}$. We further illustrate this result with some figures. Figure 2 visualizes the event sets $A_{u}$ and $A_{d}$: Figure 2: Intuitive visualization of ℱ1. The colors red and blue indicate the event sets Au and Ad after observing one stock price movement.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Abstract", "weight": 1.5} -->

The filtration $\mathcal{F}_{2}$ encapsulates $\mathcal{F}_{1}$ and also takes into account the return information revealed at $t = 2$. Thus, we now has event sets $A_{uu}$, $A_{ud}$, $A_{du}$ and $A_{dd}$, illustrated by the distinct colors in Figure 3: Figure 3: Intuitive visualization of ℱ2. The colors red, green, orange and blue indicate event sets Au u, Au d, Ad u, Ad d respectively. Note that this filtration is more fine-grained than ℱ1.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Abstract", "weight": 1.5} -->

This tiny lattice example extends to all problems with discrete outcome spaces $\Omega$ and time horizons $T$ of any size. However, an augmentation to continuous outcome spaces is not necessarily trivial. Suppose that rather than a lattice model, we use a continuous stochastic process to generate returns at each discrete time step. For the purpose of illustration, let us assume that the return may be any number in ${\lbrack{- d},u\rbrack} \cup {\mathbb{R}}$, i.e., any real number between $- d$ and $u$. The outcome space $\Omega$ is now continuous. The core concept of the filtration remains unchanged for continuous outcome spaces, but requires some more attention. Again, the filtration embeds all events based on every possible price path, the unions of these events, and the complements of these events. However, it is no longer eminent what an 'event' is; individual outcomes have probability 0 in continuous space. Simply stated, the 'event' is something we want to measure.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Abstract", "weight": 1.5} -->

On the real line, we often use the Borel $\sigma$-algebra, which contains all open intervals, their unions and their complements. For instance, on a domain ${{\lbrack{S - d},{S + u}\rbrack} \cup {\mathbb{R}}} = {\lbrack 329,335\rbrack}$ we could define a Borel $\sigma$-algebra $\mathcal{B}{\lbrack 329,335\rbrack}$. Such algebras may contain intervals^11^1As individual points have a probability of 0 occurring, open and closed sets have the same probability. such as as well as all their unions and complements. The complement of $\lbrack 330.3,331.9)$ would be Furthermore, we can construct a plethora of unions such as Although we can think of infinitely many events, we may assign a positive probability to each of them and verify whether or not the price path is in the interval.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Abstract", "weight": 1.5} -->

If we start with price $S_{0}$, the price at $t = 1$ falls within $\lbrack{S_{0} - d},{S_{0} + u}\rbrack$, at $t = 2$ it falls within $\lbrack{S_{0} - {2d}},{S_{0} + {2u}}\rbrack$, etc. Thus, the outcome space may be visualized as a cone shape that contains all possible price paths. As time passes, we can define increasingly narrow boundaries, although within these boundaries we can define an infinite number of open intervals (and their complements and unions). Figure 4 illustrates two possible event sets corresponding to a simulated price path $\omega$ in continuous space.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Abstract", "weight": 1.5} -->

To wrap up, we revisit the use of filtrations in a reinforcement learning context. In each learning episode, we construct a sample path $\omega$ that is typically randomly drawn from the outcome space. If we define a decision $x_{t}{(\omega)}$ based on the outcome space, we would already know all information, including events revealed at ${t + 1},\ldots,T$. In our stock price example, we would know exactly when to buy or sell, having perfect insight into the price movements up to $T$. However, if we impose that $x_{t}{(\omega)}$ is $\mathcal{F}_{t}$-measurable, decisions can only be made based on the information up till time $t$, such that realizations of $W_{t + 1},\ldots,W_{T}$ are not taken into account when making a decision at $t$. This way, the notion of filtrations elegantly resolves the issue of prematurely revealing future information to the decision maker.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Abstract", "weight": 1.5} -->

Recall that in RL, we aim to find a decision-making policy $\pi:{S_{t}\mapsto x_{t}}$. The state $S_{t}$ can be computed based on the initial state $S_{0}$, the decisions made, and the information sequence ${W_{1} = {\omega_{1},\ldots}},{W_{t} = \omega_{t}}$. However, as the Markovian property holds (remind that decisions only depend on the current state of the system, not on information from the past), we need solely our current state $S_{t}$ to make a decision, not the entire information sequence leading to that state. In case of our stock price example, decisions whether to sell or buy only depend on the current stock price, which implicitly embeds all price fluctuations of the past. Hence, when stripping our MDP model to the minimum information that is strictly necessary to make a decision, the notion of filtrations is redundant.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Abstract", "weight": 1.5} -->

Nevertheless, filtrations are generic and broadly applicable, which is why many authors opt to use filtration concept in the formal definition of their MDPs. Ultimately, it boils down to convention and background. Whether utilizing the concept or not, for anyone active in the RL domain it is useful to have at least an intuitive understanding of the concept of filtrations.
