## Introduction

## Motivation

We have two goals in writing this document. One: to satisfy the requirements of a PhD, by writing a thesis describing our original research. Two: to give an accessible survey of the new, rapidly developing, and in our opinion very exciting field of neural differential equations. To the best of our knowledge this is the first survey to have been written on the topic.

We hope this will prove useful to the interested reader! Along the way we shall cover a wide variety of applications, both to classical mathematical modelling, and to typical machine learning problems.

## Getting started

Prerequisites We will assume throughout that the reader is familiar with the basics of ODEs and with the basics of modern deep learning, but we will not assume an in-depth knowledge of either. On the basis that many of our readers may come from a traditional applied mathematics background without much exposure to deep learning, then Appendix A also provides a summary of the relevant deep learning concepts we shall assume. It also provides references for learning more about deep learning.

The material on neural SDEs will assume familiarity with SDEs.

Beyond these (relatively weak) assumptions, we will introduce concepts as we need them. Various parts of the text will touch on topics such as rough path theory, or numerical methods for differential equations. In each case we assume little-tono familiarity on the part of the reader, and where necessary provide references for learning more about them.

The next chapter (on neural ODEs) makes an effort to explicitly spell out even 'elementary' details such as the existence of solutions to ordinary differential equations, or the use of cross entropy as a loss function. Later chapters assume increasing levels of sophistication; it is recommended to read them in sequential order.

Code The reader interested in applying these techniques is strongly encouraged to write some example code.

Each chapter contains a few numerical examples - usually on toy datasets for ease of understanding. The corresponding code is both available and well-documented: they can be found as the examples of the Diffrax software library, which is written for the JAX framework [Bra+18].

Indeed standard software libraries for solving and differentiating differential equations make working with NDEs essentially easy. These are discussed in Section 5.6 (including both Diffrax and other options for other frameworks). These libraries are again well-documented and contain numerous examples.

Experiments The material here focuses on presenting the theory of NDEs; correspondingly our numerical examples will tend to be on toy datasets chosen for ease of understanding. Real world (and possibly very large scale) applications of these techniques may be found in the original papers, which are referenced in the text alongside each individual topic.

## What is a neural differential equation anyway?

A neural differential equation is a differential equation using a neural network to parameterise the vector field. The canonical example is a neural ordinary differential equation [Che+18b]: Here θ represents some vector of learnt parameters, f θ: R × R d 1 ×···× d k → R d 1 ×···× d k is any standard neural architecture, and y: [0, T] → R d 1 ×···× d k is the solution. For many applications f θ will just be a simple feedforward network.

The central idea now is to use a differential equation solver as part of a learnt differentiable computation graph (the sort of computation graph ubiquitous to deep learning).

As a simple example, suppose we observe some picture y 0 ∈ R 3 × 32 × 32 (RGB and 32 × 32 pixels), and wish to classify it as a picture of a cat or as a picture of a dog.

We proceed by taking y = y 0 as the initial condition of the neural ODE, and evolve the ODE until some time T. An affine transformation 1 ℓ θ: R 3 × 32 × 32 → R 2 is then applied, followed by a softmax, so that the output may be interpreted as a length-2 tuple ( P (picture is of a cat), P (picture is of a dog)).

1 Commonly referred to as a 'linear' transformation in deep learning, although this is not technically correct in the mathematical sense of the word. An affine transformation takes the form x ↦→ Wx + b with potentially nonzero bias b; a linear transformation is one for which b = 0. The difference will occasionally be important to us so we endeavour to make the distinction.

Figure 1.1: Computation graph for a simple neural ODE.

This is summarised pictorially in Figure 1.1. In conventional mathematical notation, this computation may be denoted The parameters of the model are θ. The computation graph may be backpropagated through and trained via stochastic gradient descent in the usual way. We will discuss how to backpropagate through an ODE solve in Section 5.1.

In total, then: there is a neural network f θ, embedded in a differential equation for y, embedded in a neural network (the overall computation graph).

## A familiar example

A potentially familiar example of a 'neural' differential equation is the classic SIR model: This is used in mathematical epidemiology to describe the spread of a disease within a population. 2 The quantity s represents the susceptible (uninfected) portion of the population, the quantity i represents the infected portion of the population, and the quantity r represents the removed (recovered or deceased) portion of the population.

The vector field is theoretically derived, with parameters b and k describing the infectivity and the (recovery + mortality) rates respectively.

The right hand side may be regarded as a particular differentiable computation graph: 2 A rather topical choice, with this thesis having being prepared during the global Covid-19 pandemic.

The parameters may be fitted by setting up a loss between the trajectories of the model and the observed trajectories in the data, backpropagating through the model, and applying stochastic gradient descent.

This is precisely the same procedure as the more general neural ODEs we introduced earlier. At first glance, the NDE approach of 'putting a neural network in a differential equation' may seem unusual, but it is actually in line with standard practice. All that has happened is to change the parameterisation of the vector field.

## Continuous-depth neural networks

We have just seen how neural differential equations may be approached via traditional mathematical modelling. They may also be arrived at via modern deep learning.

Recall the formulation of a residual network [He+15]: where f θ (j, ·) is the j -th residual block. (The parameters of all blocks are concatenated together into θ.)

Now recall the neural ODE Discretising this via the explicit Euler method at times t j uniformly separated by ∆ t gives Absorbing the ∆ t into the f θ, we recover the formulation of equation (1.1).

Having made this observation - that neural ODEs are the continuous limit of residual networks - we may be prompted to start making other connections.

It transpires that the key features of a GRU [Cho+14] or an LSTM, over generic recurrent networks, are updates rules that look suspiciously like discretised differential equations (Chapter 3). StyleGAN2 [Kar+19] and (score based) diffusion models [Son+21b] are simply discretised SDEs (Chapter 4). Coupling layers in invertible neural networks [Beh+19] turn out to be related to reversible differential equation solvers (Chapter 5). And so .

By coincidence (or, as the idea becomes more popular, by design) many of the most effective and popular deep learning architectures resemble differential equations. Perhaps we should not be surprised: differential equations have been the dominant modelling paradigm for centuries; they are not so easily toppled.

## An important distinction

There has been a line of work on obtaining numerical approximations to the solution y of an ODE d y d t = f ( t, y ( t )) by representing the solution as some neural network y = y θ.

Perhaps f is known, and the model y θ is fitted by minimising a loss function of the form for some points t i ∈ [0, T]. As such each solution to the differential equation is obtained by solving an optimisation problem. This has strong overtones of collocation methods or finite element methods. This is a popular line of work; see for example [Fan+19; Zub+21] amongst many others.

This is known as a physics-informed neural network (PINN). PINNs are effective when generalised to some PDEs, in particular nonlocal or high-dimensional PDEs, for which traditional solvers are computationally expensive. (Although in most regimes traditional solvers are still the more efficient choice.) [Zub+21] provide an overview.

However, we emphasise that this is a distinct notion to neural differential equations. NDEs use neural networks to specify differential equations. Equation (1.2) uses neural networks to obtain solutions to prespecified differential equations. This distinction is a common point of confusion, especially as the PDE equivalent of (1.2) is sometimes referred to as a 'neural partial differential equation'.

## The case for neural differential equations

## Applications

To this author's knowledge, there are four main applications for neural differential equations: Physical (financial, biological,...) modelling Mechanistic theory-driven differential equation models are already ubiquitous in classical mathematical modelling. However, such theory-driven models will at some point fail to capture the details of reality. By combining existing models with deep learning (with its high-capacity function approximators), we may close the gap between theory and observation.

Time series Messy or irregular data is ubiquitous in time series. Different channels may be observed at different frequencies, data may be missing, time series may be of variable lengths, and so . Treating discrete data in a continuous-time regime offers a way to treat irregular data on the same footing as 'regular' data.

Connections to topics such as system identification and reinforcement learning may also be made here, although they will not feature heavily in the present work.

Generative modelling Generative modelling studies how to model some target distribution ν, from which typically we only have samples. The usual framework is to pick a 'friendly' distribution µ, and then learn a map F such that (the pushforward) F ( µ ) approximates the target distribution ν.

It transpires that effective choices for F are derived from differential equations. For example with continuous normalising flows then µ may be a normal distribution (Section 2.2.3); in the case of a neural SDE then µ may be (the law of) a Brownian motion (Chapter 4).

Inspiration Traditional 'discrete' deep learning is widely applicable, and rightly so. We have already seen the parallels between differential equations and deep learning: a highly successful strategy for the development of deep learning models is simply to take the appropriate differential equation, and then discretise it.

## Advantages

In summary, neural differential equations offers a best-of-both-worlds approach.

The neural network-like structure offers high-capacity function approximation and easy trainability.

The differential equation-like structure offers strong priors on model space, memory efficiency, and theoretical understanding via a well-understood and battle-tested literature.

Relative to the classical differential equation literature, neural differential equations have essentially unprecedented modelling capacity. Relative to the modern deep learning literature, neural differential equations offer a coherent theory of 'what makes a good model'.

## A note on history

Practically speaking, the topic of neural differential equations become a fi eld only a few years ago, starting with the explosion of interest following [Che+18b]; other prominent recent work also includes [E17; ].

However, many of the basic ideas can be found in substantially older literature, often from the 1990s. For example in [Ric+92], a neural ODE is trained to match the dynamics of a chemical reaction, using an MLP for the vector field. Meanwhile the basics of learning a controlled dynamical system are given. consider hybridising neural ODEs with traditional theory-driven mechanistic modelling, and use implicit integrators in conjunction with neural ODEs to learn stiff dynamical systems.

This list of examples is by no means exhaustive. The above references are all short and make for easy reading, so the curious reader is encouraged to look them up.

## Chapter 2

## Neural Ordinary Differential Equations

## Introduction

By far the most common neural differential equation is a neural ODE [Che+18b]: where y 0 ∈ R d 1 ×... × d k is an any-dimensional tensor, θ represents some vector of learnt parameters, and f θ: R × R d 1 ×... × d k → R d 1 ×... × d k is a neural network. Typically f θ will be some standard simple neural architecture, such as a feedforward or convolutional network.

## Existence and uniqueness

The first question typically asked (at least by mathematicians) is about existence and uniqueness of a solution to equation (2.1). This is straightforward. Provided f θ is Lipschitz - something which is typically true of a neural network, which is usually a composition of Lipschitz functions - then Picard's existence theorem [, Theorem 110C] applies: Theorem 2.1 (Picard's Existence Theorem). Let f: [0, T] × R d → R d be continuous in t and uniformly Lipschitz 1 in y. Let y 0 ∈ R d. Then there exists a unique differentiable y: [0, T] → R d satisfying 1 That is, it is Lipschitz in y and the Lipschitz constant is independent of t: there exists C > 0 such that for all t, y 1, y 2 then ‖ f θ (t, y 1) -f θ (t, y 2) ‖ ≤ C ‖ y 1 -y 2 ‖.

## Evaluation and training

As compared to models that are not differential equations, there are two extra concerns that must generally be kept in mind.

First, we must be able to obtain numerical solutions to the differential equation. (An analytic solution will essentially never be available.) Second, we must be able to backpropagate through the differential equation, to obtain gradients for its parameters θ.

Software for performing these tasks is now standardised (Section 5.6), so we are free to focus on the task of constructing the model architecture itself. A more in-depth look at evaluation and backpropagation is given in Chapter 5.

## Applications

## Image classification

Image classification with CNNs is nearly everybody's first introduction to deep learning. It is a natural place to start discussing neural differential equations too.

Dataset Suppose we observe some images, represented as a 3-dimensional tensor R 3 × 32 × 32, corresponding to channels (red, green, blue), height (32 pixels), and width (32 pixels) respectively. Suppose each image has a corresponding class label in R 10, corresponding to a one-hot encoding of what the image is a picture of: perhaps aeroplane, car, bird, cat, deer, dog, frog, horse, ship or lorry.

Model Let f θ: R × R 3 × 32 × 32 → R 3 × 32 × 32 be a convolutional neural network, and let ℓ θ: R 3 × 32 × 32 → R 10 be affine.

Then we may define an image classification model as Loss function By using an appropriate loss function (cross entropy) between this output and the true label, we may train this model so that its output is the probability that the input image is of each of these classes.

Explicitly: given a dataset of images a i ∈ R 3 × 32 × 32 with corresponding labels b i ∈ R 10, for samples i = 1,..., N, we may minimise the cross-entropy by training θ, where · denotes a dot product and log is taken elementwise.

This example is an example only. In practice, for applications such as image classification there is usually little to be gained by using a continuous-time model. Traditional residual networks (that is, explicitly discretised neural ODEs) are simply easier to work .

As such this example is an example only. We do not actually suggest using neural ODEs for this task, for which standard neural networks are likely to be superior.

The manifold hypothesis Neural ODEs interact elegantly with the manifold hypothesis (that the data lies on or near some low-dimensional manifold embedded in the higher-dimensional feature space; Appendix A.5). The ODE describes a flow along which to evolve the data manifold.

## Physical modelling with inductive biases

Endowing a model with any known structure of a problem is known as giving the model an inductive bias. 'Soft' biases through penalty terms are one common example. 'Hard' biases through explicit architectural choices are another.

Physical problems often have known structure, and so a common theme has been to build in inductive biases by hybridising neural networks into this structure. It is this author's prediction that this will shortly become a standard technique in the toolbox of applied mathematical modelling. (If, arguably, it isn't already.)

## Universal differential equations

Consider the Lotka-Volterra model, which is a well known approach for modelling the interaction between a predator species and a prey species: Here, x (t) ∈ R and y (t) ∈ R represent the size of the population of the prey and predator species respectively, at each time t ∈ [0, T]. The right hand side is theoretically constructed, representing interactions between these species.

This theory will not usually be perfectly accurate, however. There will be some gap between the theoretical prediction and what is observed in practice. To remedy this, and letting f θ, g θ: R 2 → R be neural networks, we may instead consider the model in which an existing theoretical model is augmented with a neural network correction term.

We broadly refer to this approach as a universal differential equation, a term due to [Rac+20b]. 2 Loss function and training Suppose we observe data x i (t j) ∈ R, y i (t j) ∈ R, where i = 1,..., N denote independent observations of the target process (from different initial conditions) and j = 1,..., M correspond to different times t j ∈ [0, T], with t 1 = 0. In practice we may only have N = 1, which may be sufficient provided M is large enough.

For either (2.2) or (2.3), let x x 0,y 0 ( t ) denote x ( t ) given initial condition x = x 0 and y = y 0. Similarly for y x 0,y 0 ( t ).

Then we may fit both (2.2) and (2.3) in precisely the same way: stochastic gradient descent with respect to the loss function In switching from (2.2) to (2.3), then no fundamental part of the modelling procedure has changed.

Remark 2.2. The above presentation implicitly assumes that the locations of the observations t j were the same for both x and y, and were the same for all training samples. This is just for simplicity of presentation and is not necessary in general.

High capacity function approximation By switching from (2.2) to (2.3), the high-capacity function approximation provided by the neural networks f θ, g θ offers a way to close the gap between theory and practice. The neural network may be used to model the residual between the theoretical and the observed data.

The use of a neural network is an admission that there is behaviour we do not understand: but through this augmentation, we can at least model.

2 There is little unified terminology here. Other authors have considered essentially the same idea under other names; conversely [Rac+20b] additionally consider variations and extensions to SDEs, PDEs, and so .

These networks will frequently be very small by the standards of deep learning: consider a feedforward network of 10 layers each of width 10. [Rac+20b] consider feedforward networks of width 32 and a single hidden layer.

Use cases This approach becomes natural whenever one is attempting to model complex poorly understood behaviour, and for which there is sufficient data that the theoretical model clearly falls short.

Derivation of closure relations is a neat example. In this case, the differential equation features a term that lacks a precise theoretical description (representing the effects over scales smaller that the numerical solver can resolve), so the strategy becomes to approximate this term with a neural network, and learn this term from data.

Turbulence modelling is a popular example of this. In a Reynolds-averaged Navier Stokes model, approximate the closure relation (the Reynolds stresses) using a neural network carefully designed to satisfy certain physical invariances. See also the substantial follow-up literature: [ Mau+19] and so . Meanwhile as part of a climate model for the ocean, [Ram+20a] model a closure relation (for turbulent vertical heat flux) using a small MLP.

How to train your UDE Training (2.3) directly (via gradient descent) may not produce an interpretable model. The parameters α, β, γ, δ may not necessarily correspond to their usual quantities, if the neural network has modelled some part of the behaviour as well.

One resolution is to fit (2.2) first, use its parameters to initialise α, β, γ, δ in (2.3), and then train only the network parameters θ. This will ensure that the neural network only fits the residual between the theoretical model and the observed data.

Another option is to regularise the norm of the neural network [Yin+21], so that it is used only when necessary.

Another concern when training is that the model may become stuck in a local minimum. (Because the neural networks used with UDEs are often very small.) This may be mitigated by training on the first proportion of a time series (say the first 10%) before training on the whole time series; more generally setting some 'length schedule' that uses an increasing fraction of the time series as training progresses.

## Hamiltonian neural networks

Another approach is to suppose that the observed dynamics evolve according to a Hamiltonian system; a realistic assumption for many physical systems. With respect to some known canonical coordinates q, p ∈ R d and an unknown Hamiltonian function H: R d × R d → R, the system is assumed to evolve according to By parameterising H = H θ as some general neural network (for example just an MLP), this system may be learnt much like a universal differential equation - in this case, the inductive bias is encoded through the use of a Hamiltonian-derived vector field, rather than explicit inclusion of known terms.

Parameterisations of the Hamiltonian The Hamiltonian itself could be parameterised as an unstructured neural network, like an MLP. Alternatively one can go further, by parameterising the Hamiltonian according to kinetic and potential energy where now M θ is a learnt positive-definite mass matrix, and V θ is a learnt potential energy [;].

Control terms Encoding this minimal amount of prior knowledge also makes available tools from classical dynamics. For example, we may suppose that the system responds to a control term β according to where g θ is some neural network. After the system has been learnt from data, then controllers may be synthesised from this description.

## Lagrangian neural networks

One weakness of the Hamiltonian approach is that it assumes knowledge of the canonical coordinates q, p. In general our observed data from a dynamical system may not match up against this canonical structure.

An alternative is to instead parameterise the Lagrangian. Given positions q ∈ R d and velocities ˙ q = d q d t ∈ R d, a Lagrangian is parameterised as some neural network function of them both, L θ (q, ˙ q). The Euler-Lagrange equations state that a system with Lagrangian L θ evolves according to Rearranging, we may obtain where ∂ 2 L θ ∂ 2 ˙ q is a Hessian and so (∂ 2 L θ ∂ 2 ˙ q) -1 denotes a matrix inverse. Once again this defines a dynamical system which may be fitted directly to data as described for universal differential equations. See [Cra+20b].

## Continuous normalising flows

We now switch from supervised learning to unsupervised learning. Suppose we observe some distribution P with a density π over some state space R d 1 ×···× d k. We wish to learn an approximation to P.

For example we may have R d 1 ×···× d k = R 3 × 32 × 32, and P may denote a probability distribution over 'pictures of cats', from which we have empirical samples. By learning a generative model approximating π, we may produce synthetic pictures of cats. (An important task.)

Let d = ∏ k m =1 d m and for simplicity we replace R d 1 ×···× d k with R d.

Consider the random neural ODE defined by We seek to train this model such that the distribution of y (induced by the pushforward of y ∼ N (0, I d × d) by y ↦→ y) is approximately P. This is called a continuous normalising flow (CNF) [Che+18b; Gra+19]. See Figure 2.1.

## Sampling

Sampling from a trained model is straightforward: sample y ∼ N (0, I d × d ) and then solve (2.4).

## Instantaneous change of variables

We still need to train the model. We will proceed via maximum likelihood, which means that we need a tractable expression for the density of the distribution of y.

Theorem 2.3 (Instantaneous change of variables). Recall equation (2.4). Assume f θ = (f θ, 1,..., f θ,d) is Lipschitz continuous. Let where p θ (t, ·) is the density of y (t) for each time t ∈ [0, T]. (In some works written informally as ' p (y (t)) '.) The subscript θ in p θ denotes the dependence on f θ.

Figure 2.1: A continuous normalising flow continuously deforms one distribution into another distribution. The flow lines show how particles from the base distribution are perturbed until they approximate the target distribution.

Then p θ evolves according to the differential equation 3 The right hand side of (2.5) is the divergence of f, or equivalently the trace of the Jacobian of f. The latter description draws the analogy to the change of variables formulas for normalising flows (Appendix A.2).

See [Che+18b, Appendix A] for a straightforward proof.

Remark 2.4. The SDE theorist will find this expression familiar. It is the FokkerPlanck equation for deterministic dynamics, subject to a random initial condition. It has been carefully written so that the right hand side is independent of the unknown p θ.

Training By solving (2.5) we can train a CNF via maximum likelihood. Given any terminal condition x ∈ R d, let y (t, x) denote the solution to the ODE which will be solved backwards in time from t = T to t = 0.

3 Actually, just an integral: log p θ does not appear on the right hand side.

## CHAPTER 2. NEURAL ORDINARY DIFFERENTIAL EQUATIONS

Given a batch of empirical samples y 1,..., y N ∈ R d, maximum likelihood states that with respect to θ, we should minimise This is now possible to evaluate. 1. Starting from some empirical sample y i ∈ R d, we may solve equation (2.6) backwards-in-time from t = T to t = 0. 2. As the solution progresses we obtain y (t, x) for t = T to t = 0. This is an input to the right hand side of (2.7). This integral may be solved as part of this backwards-in-time solve - just concatenate the integral together with (2.6) to form a system of differential equations. 3. Finally, evaluate log p θ (0, y (0, y N)) - recalling that p θ (0, ·) is taken to be a normal distribution - and add it together with the value of the integral in order to obtain a value for (2.7).

Having evaluated (2.7), it is backpropagated and the parameters θ updated via gradient descent. 4 Note that backpropagation is a 'reverse time' procedure. In summary, and as we have already performed one reversal:

- Evaluating (2.7) involves solving from t = T to t = 0; - Backpropagating through (2.7) is an operation progressing from t = 0 to t = T; - Additionally, note that sampling involves solving from t = 0 to t = T, and is only performed at inference time.

## Example

As a fun example, consider a greyscale image, which we may regard as a map f: 2 →. We may fit a continuous normalising flow to f, treating f as the unnormalised density for a probability distribution over R 2 ⊇ 2. A selection of images, and some CNFs that have learnt to approximate them, are shown in Figure 2.2.

4 And as the 'forward pass' involved a derivative, then the backward pass will compute a second derivative; this is fine.

Figure 2.2: Continuous normalising flow example. From top to bottom: target, cat, butterfly. From left to right: the first six pictures show the evolution of the distribution of the CNF as it integrates from t = 0 to t = T, transforming a normal distribution into the desired distribution. The second to last picture shows samples from the learnt CNF. The final picture shows the image used to specify the desired distribution.

We see that CNFs are capable of learning relatively complex two-dimensional distributions, including those with multiple modes (such as the different concentric rings of the target), and those with fine-scale 'filaments' stretching away from the main part of the distribution (such as the whiskers or tail of the cat).

See Appendix D.1 for further details of this experiment. The code is available as an example in Diffrax.

CNFs are a highly flexible approach to modelling probability distributions. [Gra+19; Fin+20a] apply this approach to image generation. That is, the samples from the learnt distribution are images, rather than the whole distribution resembling an image as above. [Yan+19] represent 3D models as distributions (much like the above example representing a picture as a 2D distribution), and use this approach to generate point clouds of the model.

## Efficient estimation of the trace-Jacobian

Note how (2.5), and thus (2.7), involve evaluating the expression ∑ d k =1 ∂f θ,k ∂y k ( t, y ). This is possible simply via autodifferentiation software: evaluate the neural network f θ ( t, y ), and then backpropagate.

There is one foible. Autodifferentiation calculates a product of Jacobians (Appendix A.1), which this expression is not. It may be calculated by performing k = 1,..., d such operations, but this implies a relatively expensive O ( d 2 ) cost. Each evaluation of f θ: R × R d → R d requires at least O ( d ) work. Each subsequent autodifferentiation operation also requires O ( d ) work; so far for a total of still only O ( d ). That we must make k = 1,..., d such calls is what raises this to O ( d 2 ) cost.

Hutchinson's trace estimator Let A ∈ R d × d be any matrix. Let ε be a random variable over R d such that E [ε] = 0 ∈ R d and Cov[ε] = I d × d. (For example, a multivariate normal or Rademacher random variable.) Then The Monte-Carlo approximation derived from this equation is known as Hutchinson's trace estimator.

The trace-Jacobian That the right hand side of (2.5) is a trace-Jacobian now proves useful. We have that Substituting into (2.7) we obtain In practice this expectation will often be approximated by a single Monte-Carlo sample, which as in (2.8) is held constant for the duration of the integration. Training already involves averaging over the batch of data i = 1,..., N and so further MonteCarlo samples are often unnecessary.

And now for punchline: the integrand of (2.8) may be computed in only O ( d ) work. First ε ⊤ ∂f θ ∂y ( t, y ( t, y i )) may be computed as vector-Jacobian product (requiring only O ( d ) work), and then this is combined with the final ε via a simple dot product (also only O ( d ) work). Overall this produces an unbiased estimate of the divergence.

## Comparison to normalising flows

Recall the discussion on normalising flows from Appendix A.2. In both cases, a change in log-probability densities is described in terms of the Jacobian of the transformation.

Note the difference in computational complexity. In the general normalising flow setting, the log-determinant-Jacobian costs O ( d 3 ) work to evaluate (and backpropagate through). Here it has been reduced to just O ( d 2 ) or O ( d ) work.

Figure 2.3: Overview of latent ODE model.

## Latent ODEs

The previous section considered a generative model for data from some distribution without a time-varying component. For example, a static picture of a cat, rather than samples from a dynamical system evolving in time. We now consider the case that the distribution has an intrinsic time-varying component - for example, it may be a distribution over time series. Once again, we wish to model this distribution.

Consider the space of d -dimensional irregularly-sampled time series For ease of presentation we suppose this is fully-observed (without missing data), but the following construction extends immediately to the partially-observed case too.

We proceed by constructing a VAE. Figure 2.3 provides a summary of the construction we about to present. This is termed a latent ODE [Che+18b; ].

Remark 2.5. The use of a VAE raises the question of whether other generative approaches (GANS,...) may be employed. The answer is yes, and indeed Chapter 4 (Neural Stochastic Differential Equations) will be almost entirely dedicated to the problem of generative time series models.

Decoder Fix d l, d m > 0 as the dimensionality of two latent spaces. (Typically d l, d m ≫ d.) Let be neural networks parametrised by learnt parameters θ. Let p θ,y: R d l → [0, ∞) be some probability density parameterised by y ∈ R d l and learnt parameters θ. (For simplicity of notation we stack all learnt parameters together into a single vector θ.)

Given z ∈ R d m, let y 0 = g θ (z) ∈ R d l and let y (t, y 0) be the solution of the neural ODE For each time t we consider p θ,y (t,y 0). The full collection of t ↦→ p θ,y (t,y 0) is the output of the model.

That is, given some input z ∈ R d m, it is mapped into the latent space R d l, from which the ODE y evolves. At each time the latent value parameterises a probability distribution.

This is the decoder of the VAE.

Example 2.6. Frequently p θ,y may simply be taken to be a Gaussian with fixed variance: let ℓ θ: R d l → R d be affine and let p θ,y be the density of N ( ℓ θ ( y ), I d l × d l ). We will discuss other choices of p θ,y in a moment.

For any x = ((t 0, x 0),..., (t n, x n)) ∈ TS (R d), let which corresponds to the probability density of a full time series x, rather than of just a single observation at a single point in time.

Encoder The encoder of the VAE is some ν θ: TS ( R d ) → R d m × (0, ∞ ) d m; frequently an RNN or a neural CDE (Chapter 3).

The encoder output is the statistics of a multivariate normal distribution with diagonal covariance; we denote this by q θ, x = N ( µ θ, x, diag( σ θ, x ) 2 ) with ( µ θ, x, σ θ, x ) = ν θ ( x ).

If the encoder is an RNN or neural CDE it will sometimes be run backwards-in-time over the input time series, so that the decoder starts where the encoder ends.

Training Given a batch or dataset of time series x 1,..., x N ∈ TS (R d), then the end-to-end optimisation criterion is to minimise θ with respect to This is simply the standard VAE optimisation criterion, and provided p θ,y is 'reasonable' (for example, a Gaussian), then this expression may be evaluated and backpropagated through in the usual way. The first term ensures that the decoder learns to replicate its input samples; the second term ensures that the initial distribution in the latent space matches a known distribution, which may be sampled from at inference time.

Sampling Sampling from the model is straightforward in the usual way for VAEs: sample some z ∼ N (0, I d m × d m ), evaluate y 0 = g θ ( z ), and evaluate (2.9) forward in time. p θ,y ( t,y 0 ) is the model output. If a point statistic is required (for example, just a sample from the model) then the mean of p θ,y ( t,y 0 ) may be returned.

Figure 2.4: Plots of samples y: → R 2 drawn from the latent ODE model. The leftmost picture is a sample from the untrained model. The rightmost picture is a sample from a fully-trained model. In between are samples from partially-trained models. Quality increases as training proceeds.

Choice of distribution The choice of p θ,y is dependent on what behaviour is desired when sampling during inference time. If only a point statistic is required then the choice of p θ,y is essentially just a choice of loss function, and simple choices like Gaussian distributions (Example 2.6) or Laplace distributions (whose log-likelihood is the L 1 distance) are sensible.

If the full model output p θ,y ( t,y 0 ) is of interest - for example to perform uncertainty quantification - then more expressive choices of p θ,y may be of interest. For example, [Den+21] consider taking it to be a normalising flow (and additionally consider replacing the latent ODE with a latent SDE; see Chapter 4).

## Examples

As a simple example, consider a dataset of decaying oscillators. That is, a 2-dimensional time series consisting of (discrete observations of) with y 0, y (t) ∈ R 2, A ∈ R 2 × 2, and such that the eigenvalues of A are complex with negative real component. Samples look like decaying sine and cosine waves.

We take y 0 ∼ N (0, I 2 × 2 ), and generate sample data from (2.10) at irregularly sampled timestamps over. The timestamps are not regularly spaced nor are they consistent between different batch elements.

We fit a latent ODE to this dataset. At test time, we solve the ODE over the larger interval. See Figure 2.4 for some samples generated from this model. We see that by the end of training, excellent samples are produced, even though they are over a time interval four times larger than the model was trained .

See Appendix D.2 for precise details. The code is available as an example in Diffrax.

Irregular sampling The continuous-time approach handles several irregular kinds of sampling without issue: the input data is not regularly spaced, nor are different batch elements sampled at the same times.

Meanwhile, the output is over the (continuous-time) interval, so that we are obtaining samples at all times. This is unlike the analogous RNN, which would be restricted to producing outputs only at prespecified discrete timestamps.

Extrapolation Figure 2.4 shows that the latent ODE has successfully reproduced this dataset. Moreover it exhibits good extrapolation qualities over an interval four times longer than the interval it was trained .

Other examples Many other types of time series problem may be considered. For example apply a latent ODE to model the dynamics of a small (simulated) frog jumping into the air; consider applications to reinforcement learning; combine latent ODEs with changepoint detection algorithms to model switching dynamical systems.

We additionally direct the reader towards Chapter 4, in which neural SDEs will also be used to model (much more general) distributions over time series.

## Sequence-to-sequence models

Essentially the same construction may be used in the construction of sequence-tosequence models, for example to perform time series forecasting. The encoder (an RNN or neural CDE, see Chapter 3) runs over the input time series; the decoder (a neural ODE or neural SDE, see Chapter 4) produces the forecasted sample.

## Residual networks

In Section 1.1.4 we saw that residual networks are the explicit Euler discretisation of a neural ODE.

Correspondingly the theory of dynamical systems offers ways to derive variant residual networks with favourable properties.

## Rotational vector fields

consider replacing the forward pass of a residual network with for some weights and biases K j, b j and some choice of activation function σ. This corresponds to a semi-implicit Euler discretisation of the neural ODE Correspondingly, the Jacobian of the right hand side is Many activation functions are monotonic; if this is the case then the Jacobian is the product of a diagonal matrix with positive entries, and an antisymmetric matrix, and as such the Jacobian has pure-imaginary eigenvalues. 5 This means that the vector field is 'purely rotational': eigenvalues with positive real part drive expansion; eigenvalues with negative real part cause contraction, but zero real part produces neither. Correspondingly, (2.11) is largely immune to vanishing/exploding gradient issues.

Remark 2.7. The trade-off, however, is a potential reduction in expressivity. Purely rotational vector fields are volume preserving (divergence-free). Non-volume-preservation is often important for expressivity. (It is even part of the name of Real Non-Volume Preserving flows.)

This issue of volume preservation may be partially ameliorated by working in a higher dimensional space; see Section 2.3.3.2 later.

## Momentum residual networks

[San+21] consider replacing the forward pass through a residual network with for γ ∈. (γ = 0. 9 would be typical.)

Reversibility The key property of such networks is that they are reversible: whilst (2.12) computes (v j +1, y j +1) from (v j, y j), it also possible to reconstruct (v j, y j) from 5 Proof: let D be positive diagonal with square root A. Let W be antisymmetric. Then DW is similar to AWA, which is antisymmetric and as such has pure-imaginary eigenvalues.

This dramatically improves the memory efficiency of the network, at the cost of some extra computation. When backpropagating through (2.12), the intermediate values y n need not be stored (like they would be for the corresponding residual network). Instead, (2.13) means they can be recomputed on-demand as backpropagation proceeds.

This represents a refinement of similar ideas in [Gom+17; Cha+18], and more generally the topic of invertible neural networks [Beh+19].

As a neural ODE Let ε = 1 / (1 -γ). Then (2.12) is given by the semi-implicit Euler method, with unit step size, applied to Connection to reversible solvers Momentum networks are reversible because the semi-implicit Euler method is reversible. Running the solver forwards in time, then backwards in time, will recover the same numerical solution. This is sometimes described as saying that there are matching truncation errors on the forward and backward solves.

Reversible solvers come strongly recommended for use with neural differential equations for the same reason as here: they allow for backpropagation that is both time and memory efficient (Section 5.3.2). As such they are of substantial interest, and moreover in general do not require the second-order structure that (2.14) exhibits.

## Alternative integration schemes

Other off-the-shelf integration schemes may be substituted for the explicit Euler method.

For example [Lu+17a] consider linear multistep methods and [Hab+19] consider IMEX methods. PolyNet [Zha+17] considers operations of the form which if f θ is a linear contraction, is an approximation to the implicit Euler method Wenote that the advantages of switching to a different integration scheme are strongest when it exhibits particular additional properties, like symplecticity as in Section 2.2.5.1 or reversibility as in Section 2.2.5.2.

## Choice of parameterisation

So far we have touched only lightly on the parameterisation of the vector field f θ. (Although we have discussed some mathematically-inspired parameterisations, such as Hamiltonian-based parameterisations in Section 2.2.2.2.)

Should f θ be a feedforward network, convolutional network, residual network,... ? Should it use batch normalisation? What kinds of activation functions are appropriate? And so .

Good architectural choices and good choices of optimiser are often crucial for success. However (even with the following guidelines) it is not always clear what good choices are. Frequently this is still just a matter of hyperparameter optimisation - or perhaps 'try it and see what works'.

## Neural architectures

Nearly every work uses either a feedforward or convolutional neural network for the vector field f θ. Feedforward networks are straightforward: simply concatenate t and y ( t ) together as inputs. These are what are typically used when the data is anything other than an image.

If the data y 0 has the (channel, height, width) structure of an image, then a suitable vector field may be obtained by using convolutional layers. Recall that the input and output of f θ ( t, · ) must be the same size. This typically means either using padding, or combining convolutional layers with transposed convolutional layers. Time t is often appended to y ( t ) as an additional channel.

Remark 2.8. Other parameterisations are occasionally used. For example [Pol+19; Cra+20a; Den+19; Cha+21] consider graph neural networks, which can for example encode equivariance with respect to permutations of the input points. (Such as may be exhibited in many physical systems; for example the positions of n equally-sized masses evolving under gravity.)

Much of the following discussion carries through to this setting, although we will not discuss graph-structured networks and graph-structured data in detail here.

## Activation functions

The theory of backpropagating through ODEs does technically ask that the vector field (and thus the activation function) be continuously differentiable (Section 5.1), which ReLUs are not.

As such continuously differentiable activation functions like SiLU [], softplus, or tanh are typically used. 6 Despite this theoretical point, ReLU activations are still often used successfully in practice.

## Normalisation

Normalisation schemes, such as batch normalisation and layer normalisation [; ], are typically not used, at least within the vector field f θ. For batch normalisation, this is because the same neural network f θ is evaluated at y ( t ) for different t, and each might have different statistical properties. This is the same problem that occurs when using batch normalisation in recurrent neural networks [; Coo+17].

Meanwhile layer normalisation lacks a satisfying explanation for its lack of efficacy, but at least for CNFs it has been reported that this typically breaks training.

## Initialisation

Initialising the neural vector fields close to zero often improves training, it being easier to perturb a nearly constant t ↦→ y ( t ) than random initial dynamics. For most neural architectures this may be accomplished by choosing the initial parameters θ close to zero.

## Non-autonomy

We have deliberately chosen to include t as an input to the vector field f θ. A residual network has different layers at different depths. Analogously, neural ODE models usually exhibit higher modelling capacity by allowing f θ to depend on the 'continuous depth' parameter t. Such differential equations are referred to as being nonautonomous.

This can be handled simply by concatenating t and y ( t ) together as inputs to f θ. A far more expressive choice is to additionally explicitly encode certain time dependencies.

6 cooked up, and reports being fond of, the 'squareplus' activation x ↦→ 1 2 x + 1 2 √ x 2 +4.

## Depth discretisation: stacking

One straightforward and effective approach is to parameterise f θ in piecewise fashion as several different networks, selected based on the value of t. For example, where θ = (θ 1,..., θ n), and each θ j is itself some vector of parameters.

In principle each f ·, 1,..., f ·,n could represent different architectures. Often f ·,j will all be the same neural architecture, and differ only in which parameter vector θ i they depend upon.

Two options must be considered when using this architecture in practice, with a numerical differential equation solver: whether to use a single call to an ODE solver over [ t 0, t n ], or whether to solve over each [ t i, t i +1 ] region separately, and call an ODE solver n times. Both options are valid but both introduce details that one should be aware of; we defer this numerical discussion to Section 5.3.3.

## Spectral discretisation

Let ψ j: [0, T] → R be some family of (smooth) functions parameterised by j ∈ { 1,..., n }. Take the parameter vector θ to be such that θ = (θ 1,..., θ n) with θ j ∈ R d θ for some d θ ∈ N. Now define Then another choice of non-autonomy is given by where ˜ f is some fixed neural network architecture which at time t uses parameters α θ (t) ∈ R d θ.

The choice of ψ j is up to us. Ideally they should be quite different to each other, for the greatest possible expressivity of the model. For example they could be chosen as Chebyshev polynomials, or as a truncated Fourier basis of sines and cosines (which is what motivates the terminology 'spectral discretisation' [Mas+20]).

## Hypernetworks

Another choice is to let the parameters of the neural ODE be themselves parameterised as the solution of a neural ODE.

That is, let α: [0, T] → R d α be the solution of the neural ODE with learnt parameters θ, vector field g θ: R × R d α → R d α, and learnt initial condition α θ.

We then let the hidden state y of our 'original' neural ODE evolve according to where ˜ f is some fixed neural network architecture which at time t uses parameters α (t) ∈ R d α.

In practice these two differential equations may be concatenated and solved simultaneously as a system. Overall this may be seen as just a neural ODE as originally formulated, with a particular beneficial structure to its vector field. See [Zha+19; Cho+20].

## Variant layers

Other high-performing time-dependent layers may be dreamt up. For example (and inspired by [Gra+19]) the example CNF seen in Section 2.2.3.3 uses an MLP whose affine layers are replaced with layers of the form where x ∈ R d 1, t ∈ R, A ∈ R d 2 × d 1, b, c, d, e ∈ R d 2, σ denotes the sigmoid function, and ∗ denotes elementwise multiplication.

The dependency on the time t is coming in at each layer of the MLP, rather than being concatenated with y ( t ) as just another input.

This is reminiscent of gating procedures in GRUs and LSTMs.

## Enforcing autonomy

One exception to the above procedure sometimes occurs when using neural ODEs equations for time series problems, such as with a latent ODE (Section 2.2.4). In this case, we may sometime suppose that the underlying dynamics are not timedependent, and would instead prefer to remove t as an input. (The same will often also be true of the upcoming neural CDEs and neural SDEs in Chapters 3 and 4.)

## Augmentation

For a moment let us focus on performing image classification with neural ODEs (Section 2.2.1); a problem chosen for its simplicity. In Section 2.2.1, the input to the model was the same size as the hidden state: both the input picture and hidden state were of shape R 3 × 32 × 32. In general however this is neither necessary nor desirable.

'Augmentation' refers to the practice of inserting an affine map between input and initial value, to increase the dimension of the hidden state. That is, given some input x ∈ R d, the initial value of the ODE is taken to be y = g θ (x) for some learnt g θ: R d → R d l with d l > d, rather than simply y = x. We have Standard choices of g θ are either zero augmentation: g θ (x) = [x, 0], learnt augmentation: g θ (x) = [x, ˜ g θ (x)] for some learnt ˜ g θ, or just an affine map: g θ (x) is learnt and affine. The choice is usually unimportant; the increase in dimensionality is the main point. In each case, the output of the model is still obtained by applying some affine map ℓ θ: R d l → R d o to y (T), with d o ∈ N the desired output dimensionality.

This improves model performance dramatically. The reason is that the continuous flow of an ODE is incapable of modifying the topology of its input - so staying in the same space means that topological properties of the input manifold (in the sense of the manifold hypothesis; Appendix A.5) are necessarily preserved. This is a statement we will make precise in Section 2.4, by describing the universal approximation properties of neural ODEs.

Returning now to the general setting (beyond just image classification), we have already seen an example of augmentation: the latent ODE (Section 2.2.4) evolved in some higher-dimensional space R d l, and used an affine map to R d to obtain the output.

(Conversely, note that CNFs cannot use augmentation: as with all normalising flows, it is a requirement of the construction that every operation be bijective.)

Remark 2.9. Lifting into a higher-dimensional space may be regarded as a relaxation of the Markov property. For s < t then the output ℓ θ ( y ( s )) does not completely determine ℓ θ ( y ( t )). In contrast y ( s ) does determine y ( t ). (Whether y is the output of an unaugmented neural ODE or the latent value of an augmented neural ODE.)

The Markov setting can be very beneficial if the problem is known to exhibit this structure, in particular when modelling physical systems. If the data is densely sampled then it can then be possible to avoid the ODE solve entirely: estimate d y d t with finite differences and do direct supervised regression of d y d t against ( t, y ). See [; ] for variations on this idea. The Markov setting is also the one used for symbolic regression (Section 6.1).

In general however the Markov setting is a restrictive assumption usually worth avoiding. The Markov/non-Markov distinction is an important one to watch out for in the NDE literature, as many works have implicitly restricted to the Markov setting without discussion.

## Second-order-augmentation

[Nor+20] introduce an interesting variant on this: they take d l = 2 d and structure the vector field so that the extra dimensions correspond to velocities. For example using a learnt augmentation, This may also be written as a second-order neural ODE d 2 s d t 2 (t) = f θ (t, s (t), d s d t (t)).

This is a choice that makes particular sense if using neural ODEs to model an oscillatory dynamical system.

## Augmenting rotational vector fields

Recall Remark 2.7. Augmentation is one way to ameliorate the lack of expressivity of rotational vector fields.

Example 2.10. Let a = -1, b = 0, c = 1 2 ∈ R, and suppose we wish to classify { a, c } versus { b }, by constructing a neural ODE followed by an affine layer. We will prove in Section 2.4.1 that this is actually impossible with an unaugmented neural ODE; there does not exist a flow whose terminal values linearly separate { a, c } from { b }.

However, projecting these into a = (-1, 0), b =, c = (1 2, 0) ∈ R 2, then the (volume-preserving) flow will linearly separate { a, c } from { b } after any arbitrarily small amount of time.

## Approximation properties

We now examine the universal approximation properties of neural ODEs, as maps from their initial value to their terminal value. See Appendix A.3 for an introduction to the topic of universal approximation.

## 'Unaugmented' neural ODEs are not universal approximators

Consider the map y ↦→ y (T), where y: [0, T] → R d solves some neural ODE Figure 2.5: ODE flows need to cross to linearly separate { a, c } from { b }.

What functions can this approximate?

Unfortunately, the answer is 'not many'. More precisely, the continuous evolution of the ODE ensures that any topological property of its input must be preserved.

Let a = -1, b = 0, c = 1 2 ∈ R, and suppose we wish to classify { a, c } versus { b } by constructing a neural ODE followed by an affine layer. That is, the flow of the ODE should linearly separate { a, c } from { b }.

This is impossible: we are asking that either a < b and c < b, or that a > b and c > b. Correspondingly, either the trajectories for a and b must cross, or the trajectories for b and c must cross. See Figure 2.5.

This is a contradiction, as ODE flows never cross.

Remark 2.11. This is not isolated to d = 1. Higher dimensional counterexamples may be considered by considering analogous 'nested shells', in which { y ∈ R d ∣ ∣ ‖ y ‖ < r 1 } and { y ∈ R d ∣ ∣ r 2 < ‖ y ‖ < r 3 } are classified from each other, with 0 < r 1 < r 2 < r 3.

## 'Augmented' Neural ODEs are universal approximators, even if their vector fields are not universal approximators

Fortunately, this is an issue easily remedied, through augmentation as introduced in Section 2.3.3.

## When the vector field is a universal approximator

We first consider the case that the vector fields are universal approximators.

Theorem 2.12. Fix d, d l, d o ∈ N with d l ≥ d + d o. For f ∈ Lip(R × R d l; R d l), ℓ 1 ∈ L b (R d; R d l), ℓ 2 ∈ L b (R d l; R d o), let φ f,ℓ 1,ℓ 2: R d → R d o denote the map x ↦→ z with is a universal approximator for C (R d; R d o).

(For simplicity this theorem has assumed that the vector field may be drawn from Lip( R × R d l; R d l ), not just some dense subset of it.)

See [Zha+20, Theorem 7] for a short-and-sweet proof of Theorem 2.12.

## When the vector field is not a universal approximator

Perhaps surprisingly, the condition that the vector field must be a universal approximator is not a necessary condition.

Theorem 2.13. Fix d, d o ∈ N. For d l ∈ N, f ∈ C (R × R d l; R d l), ℓ 1 ∈ L b (R d; R d l), ℓ 2 ∈ L b (R d l; R d o), let φ p,f,ℓ 1,ℓ 2: R d → R d o be the map x ↦→ z with for those f for which the solution is unique. 7 For each d l ∈ N there exists an f d l ∈ C (R d l; R d l), for which the above equation has a unique solution, such that is a universal approximator for C (R d; R d o).

See Appendix C.1 for the proof.

## Comparison

If the vector field is a universal approximator, then the width of the latent space d l is fixed, and complexity is obtained through the vector field. In contrast, if the vector field is not a universal approximator, then the latent dimensionality d l is allowed to become arbitrarily large, and complexity is instead obtained through the affine maps.

7 The Peano existence theorem implies existence as f is continuous; but as f is not necessarily Lipschitz then the stronger Picard existence theorem, which gives uniqueness, does not apply.

Remark 2.14. These have direct analogues in the theory of universal approximation for neural networks.

The case for which the vector field is not a universal approximator is directly analogous to the classical universal approximation theorem, which states that sufficiently wide feedforward neural networks may be used to approximate arbitrary continuous functions.

The case for which the vector field is a universal approximator is directly analogous to the 'deep and narrow' universal approximation theorem, which states that sufficiently deep feedforward networks, of bounded width, may be used to approximate arbitrary continuous functions [Lu+17b Par+21].

## Comments

Neural ODEs were originally considered (to the best of this author's knowledge) in early works from the 1990s, such as [; Ric+92 ]. A recent revival of the neural-network-as-dynamical-system was started with works such as [E17; ], and popularised (in particular in continuous time) by [Che+18b].

Indeed [Che+18b] introduced continuous-time neural ODEs for image classification (Section 2.2.1), continuous normalising flows (Section 2.2.3), and latent ODEs (Section 2.2.4). The latter two were expanded on in [Gra+19; ].

Applications of neural ODEs to physical problems span multiple literatures; we can give at most a small selection of examples. Examples from machine learning include [; Rac+20b; ], whilst examples from engineering include [ Por+19; Ji+21]. Other examples include physics, climate science [Ram+20a Hwa+21], epidemiology [Wan+21], neuroscience [Kim+21b], pharmacodynamics [Kim+21a] and so .

Connections between neural ODEs and their discrete-time counterparts include [ San+21; Sch+21] amongst others.

Extensions of neural ODEs to handle discontinuities, such as the velocity of a bouncing ball, include [Pol+21]. [; Lou+20;] generalise CNFs to manifolds, and for example then use CNFs to perform density estimation over distributions on a sphere. [Roz+21] offer a variation suitable for low-dimensional manifolds, that elides the ODE solve. [Fin+20a; Fin+20b; Onk+21; Roz+21] amongst others discuss connections between CNFs and optimal transport, to select good parameterisations and regularisations for the vector field.

Good parameterisations for the vector field are often to be found by examining the code attached to any given neural ODE paper. Works discussing this topic explicitly include [ Zha+19; Cho+20; Mas+20; Nor+20].

## CHAPTER 2. NEURAL ORDINARY DIFFERENTIAL EQUATIONS

note the lack of universal approximation for 'unaugmented' neural ODEs. [Zha+20] demonstrate universal approximation with 'augmented' neural ODEs provided the vector field is a universal approximator. More subtle universal approximation results may also be found in the literature [; Tes+20]. The material on universal approximation when the vector is not a universal approximator (Theorem 2.13) is new here.

A few other review articles combining ordinary dynamical systems and deep learning have recently been published, which the reader may find complements this chapter. For example focus on interpreting deep learning via control theory, focus on applications to fluid mechanics, and [Thu+21] place great emphasis on performing experiments. Most such works place a strong focus on specifically hybrid neural/mechanistic modelling with neural ODEs, which is our Section 2.2.2.

## Chapter 3

## Neural Controlled Differential Equations

## Introduction

Neural ODEs were the continuous-time limit of residual networks. We will now introduce neural controlled differential equations as the continuous-time limit of recurrent neural networks. The following chapter will be of particular interest for those studying RNNs or time series; also to those studying rough path theory, control theory, or reinforcement learning.

Controlled differential equations have until recently been relatively esoteric, so we do not assume familiarity with them on the part of the reader. The forthcoming section will form a 'mini-chapter' offering a self-contained summary of the key ideas, applications, and raison d'ˆ etre for CDEs and neural CDEs.

Recall the equations for a neural ODE: An extra time-like dimension is introduced and then integrated over. The presence of this extra (artificial) dimension motivates us to consider whether this model can be extended to data already exhibiting sequential structure, such as time series.

Given some ordered data ( y 0,..., y n ), the goal is to extend the y = y 0 condition to one resembling ' y = y 0,..., y ( n ) = y n ', to align the introduced time-like dimension with the natural ordering of the data. The key difficulty is that the solution of an ODE is determined by the initial condition at y, so there is no direct mechanism for incorporating data that arrives later.

Fortunately, it turns out that the resolution of this issue - how to incorporate incoming information into a differential equation - is already a well-studied problem in mathematics, via controlled differential equations.

Much of this chapter is due to [Kid+20a].

## Controlled differential equations

Let T > 0 and let d x, d y ∈ N. Let x: [0, T ] → R d x be a continuous function of bounded variation. Let f: R d y → R d y × d x be Lipschitz continuous. Let y 0 ∈ R d y.

A continuous path y: [0, T] → R d y is said to solve a controlled differential equation, controlled or driven by x, if Here 'd x (s)' denotes a Riemann-Stieltjes integral, and ' f (y (s)) d x (s)' refers to a matrix-vector multiplication.

Bounded variation and Riemann-Stieltjes integration Beyond the ODE case of the last chapter, then CDEs depend on two new concepts: bounded variation paths, and Riemann-Stieltjes integration.

Suppose x is differentiable and has bounded derivative - a relatively weak assumption. Then x will be of bounded variation, and the Riemann-Stieltjes integral may be reduced to an ordinary integral As such whilst we will continue to treat the general case, the reader unfamiliar with these concepts should feel free to mentally substitute the above treatment throughout.

Remark 3.1. Equation (3.3) is essentially about reducing a CDE to an ODE. Correspondingly, the term 'vector field' may be used to refer to either f ( y ( s )) or f ( y ( s )) d x d s ( s ).

CDEs are operators A controlled differential equation should be interpreted as a function from path-space to path-space. The input is a path x. The output is a path y. By choosing f carefully, we may use a CDE to compute specific functions of its control.

Example 3.2 (Value and integral of control). Let f: R 2 → R 2 × 2 be defined by (where y ∈ R 2 is decomposed into y = [y 1, y 2]).

Given any control x: [0, T ] → R, let y: [0, T ] → R 2 be the solution of the CDE driven by t ↦→ ( t, x ( t )), with vector field f, with initial condition y = [ x, 0] ∈ R 2. Then y ( t ) will compute the value, and the first integral, of x.

For example, consider the input signal x (t) = sin(t) ∈ R. Then Solving the first component, we see that As advertised: y (t) computes both the value sin(t) of the input signal, and its first integral ∫ t 0 sin(s) d s.

Moreover there was nothing special about the choice of sin( t ), and this CDE will compute the value and first integral of any input signal.

We will make the equivalence more precise later , but the connection to RNNs should be intuitive: much like CDEs, they compute some function of their timevarying input.

Existence and uniqueness The Picard existence theorem (Theorem 2.1) may be adapted to this setting.

Theorem 3.3 (Picard existence theorem, [, Theorem 1.3] or [, Theorem 3.8]). Let f: R d y → R d y × d x be Lipschitz. Let x: [0, T] → R d x be of bounded variation. Let y 0 ∈ R d y. Then there exists a unique continuous y: [0, T] → R d y satisfying Remark 3.4. The differential equation for a CDE is (by convention) autonomous, in the sense that f is independent of the time t. If really desired then t may be included by adding it to the state: replace x with [t, x] and f with [1 0 0 f]. This implies we have replaced y with [t, y].

Remark 3.5. We might wonder about also using right hand sides of the form ' f θ ( y ( s ), x ( s )) '. Whilst there is nothing fundamentally wrong with this alternate approach, it is less theoretically neat. When using ' f θ ( y ( s ), x ( s )) ' it is not possible to have x ↦→ y be the identity function (see Section 3.3.2 later), whilst the ' f θ ( y ( s )) d x ( s ) ' form has connections to integration against Brownian motion, as with stochastic differential equations.

## Neural vector fields

Suppose we observe some data in the form of a (continuous and bounded variation) path x: [0, T ] → R d x. This is often a little unrealistic as usually we observe discrete samples, for example in a time series. We shall fix this in a moment, when we consider applications.

Let f θ: R d y → R d y × d x be any (Lipschitz) neural network depending on parameters θ. The value d y ∈ N is a hyperparameter describing the size of the hidden state. Let ζ θ: R d x → R d y be any neural network depending on the parameters θ. Both f θ and ζ θ will often just be parameterised as MLPs.

We define a neural controlled differential equation [Kid+20a] as the solution of the CDE The quantity y is hidden state, modified in response to observations x. This is directly analogous to an RNN. This hidden state reflects an evolving belief about the system, updated continuously as observations x are made.

Let d o ∈ N be the desired output dimensionality of the model, and let ℓ θ: R d y → R d o be a learnt affine map. Then the output of the model can be ℓ θ ( y ( t )) if a time-evolving output is desired, or ℓ θ ( y ( T )) if it is not, for example when performing whole-timeseries classification. Once again, this parallels the construction of an RNN, for which a learnt affine readout is typically used to map from hidden state to output.

The resemblance between equations (3.1) and (3.4) is clear. The essential difference is that equation (3.4) is driven by the data process x, whilst equation (3.1) is driven only by the identity function R → R. In this way, the neural CDE is naturally adapting to incoming data, as changes in x change the local dynamics of the system.

## Solving CDEs

As with neural ODEs, we expect to numerically discretise the CDE so as to obtain an approximate solution.

A CDE may be discretised in two different ways. One option is to treat the 'd x (s)' analogous to time inside a numerical differential equation solver, so that for example the explicit Euler method becomes Figure 3.1: The hidden state of the neural CDE evolves continuously, driven by observational data.

In practice however most software libraries do not support this (with the notable exception of Diffrax ).

Provided x is differentiable - in practice it often will be - then the CDE may also be reduced to an ODE. Let It is now possible to solve and train the neural CDE using the same techniques as for neural ODEs, and in particular using the same software. See Section 5.6 for more discussion on software for neural differential equations.

## Application to regular time series

Let us now consider a concrete application to 'regular' time series. That is to say, the observations are at regularly-spaced points, these points are the same for each batch element, and there is no missing data. (Extension to irregular time series will be considered in Section 3.2.1.)

Let each time series be some sequence x = ( x 0,..., x n ) with each x j ∈ R d x -1. Let x x: [0, n ] → R d x be some interpolation such that x x ( j ) = ( j, x j ). For example, x x could be a cubic spline. Then x x may be used to drive a neural CDE. See Figure 3.1.

Remark 3.6. x x is sometimes interpreted as an approximation to some underlying process that x has been sampled . This is true, but not really relevant. Rather, x x is just a continuous-time representation of the input data. If we had used -x x instead then this would have represented the information contained in x just as well, despite being neither an interpolation nor an approximation.

We discuss choices of interpolation scheme in more detail in Section 3.5.

## Spiral classification

As a toy example, we construct a two-dimensional dataset consisting of time series of the ( x, y )-position of spirals, and train a neural CDE to perform binary classification of clockwise against anticlockwise. We consider data both with and without corruption by additive Gaussian noise.

The hidden state y of the CDE evolves in R d l with d l = 8, and the prediction of the model at time t is given by σ ( ℓ θ ( y ( t ))) ∈, where ℓ θ: R d l → R is a learnt affine readout and σ is the sigmoid function. The model is trained with binary cross entropy on σ ( ℓ θ ( y ( T ))).

The final output of the model is given by σ ( ℓ θ ( y ( T ))), but we may examine the evolving t ↦→ σ ( ℓ θ ( y ( t ))) for interest. See Figure 3.2. The prediction updates as the input sequence is fed into the model, converging towards a steady state of the correct classification. (On this simple problem the model achieves perfect accuracy.)

Precise experimental details may be found in Appendix D.3. The code is available as an example in Diffrax.

Remark 3.7. The presence of noise does not necessitate any changes to this approach. If really desired the data could for example be smoothed with a filter, but in principle this is not necessary. The interpolation is just a continuous-time representation of the noisy data, which the model consumes as input.

## The inclusion of time

There is only one foible with this construction, which is that x x ( j ) = ( j, x j ) and not simply x x ( j ) = x j. This one detail is important for expressivity of the model.

Example 3.8. Suppose the function computed by the neural CDE should be the length of the input time series. If x x (j) = (j, x j) then this is straightforward. Take d y = 1 so that y (t) ∈ R, and let f θ (y) = [1, 0,..., 0] ∈ R d x be constant. Let the initial value network ζ θ (x) = 0 for all inputs. Then Figure 3.2: Data, and evolving prediction, of the neural CDE. Top: Data without noise. Bottom: Data is corrupted with Gaussian noise prior to training. Left: The (x, y) data, and the prediction of the neural CDE, are shown evolving over time. The prediction converges towards a steady state (of zero; a classification of a clockwise spiral) as sufficient input data becomes available. Right: The (x, y) position is shown at the bottom of the figure. Above it is shown the current prediction of the neural CDE. where the ' ∗ · · · ∗ ' refers to whatever the derivative of the interpolation of x is.

If this extra 'time' variable is missed out, and simply x x ( j ) = x j, then computing the length is impossible. For example suppose x j = 0 for all j, and correspondingly any reasonable interpolation scheme will have x x ( t ) = 0 for all t. Then d x d t ( t ) = 0 as well, and y ( t ) = y regardless of the choice of f θ. And so y ( t ) cannot calculate the length of x for this particular choice of x.

(Note how the Example 3.2, earlier, also included time as an additional channel.)

## Discussion

Neural CDEs offer several advantages, both conceptually and practically.

## Universal approximation

Provided this formulation is followed carefully - and this extra time-like variable is included - then the neural CDE will be a universal approximator.

(Informal) Theorem 3.9. An affine map on the terminal value of a neural CDE is a universal approximator from { sequences in R d x } to R.

We will discuss this further in Section 3.3.1, and provide a formal statement and proof in Appendix C.2.1.

## Continuous-time updates

Neural CDEs update their hidden state in continuous time. In many contexts this is far more natural than the discrete-time updates typical of an RNN.

Irregular data Suppose the data arrives at irregular times. (We'll discuss this use case in much more detail in the next section.) If the times are close together then the hidden state of an RNN or neural CDE will often need only a small update. If the times are far apart then the belief about the system may need a very large update.

An RNN, however, devotes equal processing power to both of these use cases. (A single update step.) This may be inefficient if the times were close together, and insufficient if they were far apart.

In contrast a neural CDE updates continuously. The amount of computational work scales with the gap between observations, and this is likely close to the 'natural timescale' at which we should update our belief about the system. 1 Decoupled data and computation Put precisely, continuous-time updates decouple data and computation; the latter is no longer tied to the former. This is particularly true if solving a neural CDE with an adaptive step size numerical ODE/CDE solver. Such a solver automatically detects the complexity of the dynamics and takes appropriately-sized numerical steps.

Special cases of neural CDEs In light of this, there have now been several proposals in which the hidden state of an RNN is updated in continuous time between observations; popular examples are GRU-D or ODE-RNNs [Che+18a De +19]. These are special cases or discretisations of neural CDEs. (Exercise for the reader!)

## Memory efficient backpropagation

Given an RNN, for which evaluating and backpropagating a single step consumes H memory, then backpropagating an RNN evaluated on a time series of length T will consume O ( HT ) memory.

1 Could we instead repeatedly give the last piece of input data to an RNN, whilst waiting a long time for another observation? Yes, and in doing so have just reinvented a particular discretisation of a neural CDE.

In contrast, neural CDEs can reduce this to only O ( H + T ) memory. This consists of O ( H ) to backpropagate through each step individually, and O ( T ) to hold the underlying data x in memory. That each step can be backpropagated through individually is due to the use of 'optimise-then-discretise' backpropagation. We will discuss this style of backpropagation alongside our other numerical discussions, in Section 5.2.

## Summary

The goal of this section, Section 3.1, has been to summarise the main ideas behind CDEs and neural CDEs. Now that these are in place, we will be ready to move on to some more serious applications of neural CDEs.

We conclude this section with some thoughts on the connections of CDEs to other fields of study.

## Rough path theory

The theory of CDEs may be extended to highly irregular driving paths x, which are not even of bounded variation. This is known as rough path theory, and correspondingly such CDEs become rebranded as rough differential equations (RDEs).

There is broadly speaking a hierarchy from ODEs to CDEs to RDEs to SDEs: CDEs introduce the notion of control; RDEs additionally consider when the control is rough; SDEs additionally consider when the control is stochastic (usually Brownian motion). 2 We will use rough path theory in a few contexts: when applying neural CDEs to long time series (Section 3.2.3), in the proof of universal approximation for neural CDEs (Section 3.3.1), and in a later chapter to construct the 'optimise-then-discretise' equation for neural SDEs (Section 5.2.3).

These all tend towards the theoretical end of things, and we emphasise that a familiarity is neither expected nor required to read this thesis, or to work with the techniques discussed.

Remark 3.10. For those with the right background (graduate-level analysis), then rough path theory gives an excellent framework for understanding neural differential equations. It offers a pathwise theory, and a general framework through which ODEs/CDEs/SDEs may all be unified; for example Diffrax uses its principles to construct a unified system of numerical differential equation solvers. The first few pages of [Hod+20] give a brief introduction to the essential ideas of rough path theory, is a typical introductory text, and is the canonical textbook.

2 For example this hierarchy is demonstrated by numerical SDE solvers, which typically operate by drawing a sample of the Brownian motion and then solving the SDE pathwise.

## Control theory

Despite their similar names, and treatment of similar problems, controlled differential equations and control theory are typically treated as separate fields.

The difference is to some extent philosophical. In control theory, the system f is typically specified 3, and the task is to find a control x producing the desired response y. Meanwhile with (neural) CDEs, this is flipped around: the control x is typically specified, and we shall attempt to find a system f that produces a desired response y.

This is not a distinction we particularly wish to enforce, though - there is still substantial overlap.

## Applications

Neural CDEs have a number of applications, usually to time series. We will see applications to difficult time series (such as irregular or long time series), and will later briefly touch on connections to reinforcement learning. In addition we have previously remarked that RNNs and neural CDEs are linked, and we will also make this connection explicit.

## Irregular time series

Suppose we observe some irregular time series of the form x = ((t 0, x 0),..., (t n, x n)), with each t j ∈ R the timestamp of the observation Here ∗ denotes the possibility of missing data, and t 0 < · · · < t n. The length n is not assumed to be consistent between different time series.

Let T > 0 and 0 = s 0 < s 1 < · · · < s n = T. Let x x: [0, T ] → R d x be some interpolation such that x x ( s j ) = ( t j, x j ) (with the equality being defined up to those elements of x j which are not missing). For example, we could take s j = t j (or s j = j as in the previous section) and x x to be a cubic spline with knots at s 0,..., s n.

Then x x may be used to drive a neural CDE [Kid+20a]; see Figure 3.3.

Remark 3.11. We stress that this interpolation is not imputing missing data. It is simply constructing a continuous-time representation of the input data. We will discuss how to appropriately handle missing data in a moment.

3 Perhaps incompletely via observations, necessitating the additional step of performing system identification.

The choice of interpolation scheme, including the choice of s j, is one we will defer until Section 3.5. A few different choices may be made, depending on the type of problem.

## Missingness as a channel

It has been observed that the frequency of observations may carry information [Che+18a]. For example, doctors may take more frequent measurements of patients they believe to be at greater risk. Some previous work has for example sought to incorporate this information by learning an intensity function [ Che+18b].

A simple (non-learnt) procedure is just to concatenate the index j as an additional channel. That is, construct the path x x: [0, T ] → R d x +1 such that x x ( s j ) = ( t j, x j, j ) instead of just ( t j, x j ). The extra channel of x x then gives the cumulative number of observations over time.

As the derivative of x x is what is then used when evaluating the neural CDE model, as in equation (3.6), then it is the current observational rate that then determines the vector field.

## Partially observed data

When some data is missing, then the frequency of observations in each individual channel may carry information. The previous procedure may now be straightforwardly extended, by having a separate observational channel for each original channel.

Explicitly, take x x ( s j ) = ( t j, x j, c j ( x )), where c j ( x ) = ( c j, 1,..., c j,d x ) ∈ R d x, where c j,k = ∑ j m =0 1 x m,k = ∗ counts the number of observations in the k th channel by time t j. This means that x x: [0, T ] → R 2 d x -1.

Figure 3.3: Some data process is observed at times t 0,..., t n to give observations x 0,..., x n. It is otherwise unobserved. Left: RNNs modify the hidden state at each observation; common variants [Che+18a De +19] continuously evolve the hidden state between observations. Right: In contrast, the hidden state of the neural CDE model has continuous dependence on the observed data.

Adding observational masks is standard practice when working with informatively missing data [Che+18a]; this is the appropriate continuous-time analogy.

## Batching irregular data and choice of s j

In the context of CDEs, the data consists of multiple x x: [ s 0, s n ] → R d x that need to be batched together. In principle each interval [ s 0, s n ] may be different for each batch element, for example if we chose s j = t j and the data is irregularly sampled.

Batchable differential equation solvers Some (very few) differential equation software libraries allow batching over different regions of integration. In this case the problem is straightforward: simply use the capabilities of the library. For example this is the case with Diffrax.

Other differential equation solvers Most differential equation software libraries do not intrinsically support batching over different regions of integration. For example this is the case with torchdiffeq and torchcde [; ].

Fortunately, the structure of neural CDEs mean this is not a serious hurdle, as we may choose specifically s j = j. This ensures that each region of integration begins at the same value, namely zero, and we need merely integrate forwards in time for sufficiently long that every batch element has been integrated. (See also Section 3.5.2 for more discussion on the choice of s j.)

As an additional benefit, the fact that all s j are the same for each batch element can be used to simplify the storage of batches of multiple control paths x x: [0, T ] → R d x. (Instead of juggling different collections of intervals [ s j, sj +1] for each batch element.)

Remark 3.12. This was actually a mistake we made in [Kid+20a] - the above procedure was not done, in favour of an alternate (storage-inefficient) scheme that involved taking the union over the times t j needed to handle each batch of data.

Remark 3.13. One minor quirk in this case arises when using an adaptive step size solver. A subtle dependency between batch elements is introduced, as the step size will be determined by the behaviour across the whole (batched) system. This is usually not a major issue, and this is simply tolerated. (This quirk is not unique to neural CDEs, and is true whenever a batch of neural differential equations are solved with an unbatched adaptive differential equation solver.)

## Example

We now refer back to the regularly-spaced example of Section 3.1.4. Had the observations been irregularly spaced, they could have been handled in the manner just described. Morally speaking neural CDEs make little difference between regular and irregular time series; once a continuous path x x is obtained then both are treated in exactly the same way.

## RNNs are discretised neural CDEs

Wewill now make the connection between RNNs and CDEs explicit; see also [Kid+20a].

## CDEs as RNNs

Consider the CDE Discretising this with Euler's method produces either depending on whether the CDE is converted into an ODE first.

In either case, this is an RNN-like structure: suppose f = f θ is some neural network and x is some input data.

## RNNs as CDEs

Conversely consider an RNN of the form This is an explicit Euler discretisation with unit timestep of Equations of this form, in which the integrand is some function of y (s) and x (s), are special cases of neural CDEs. (We'll discuss this in Section 3.3.2.)

## RNN variants

The ' -y (s)' term in (3.7) feels a little out of place. It would not appear for RNNs of the form RNNs of this form resemble residual networks, and indeed this parameterisation clearly provides a better differential-equation-like structure.

Example 3.14. A GRU is of the above form. Recall that a GRU is defined by for input time series x j evolving hidden state h j, and suitably shaped weight matrices W 1, W 2, W 3, W 4, W 5, W 6 and bias vectors b 1, b 2, b 3, b 4. Here ∗ denotes elementwise multiplication.

This is an explicit Euler discretisation of Remark 3.15. Note the -h (t) that appears on the right hand side of the continuoustime GRU. This corresponds to exponential decay of the hidden state of the GRU, just as with the differential equation d y d t (t) = -y (t) for exponential decay. This explains the classic fact that GRUs/LSTMs struggle to learn long-term time dependencies.

## Long time series and rough differential equations

Neural CDEs, as with RNNs, begin to break down for very long time series. Loss/accuracy worsens, and training time becomes prohibitive due to the sheer number of operations required to evaluate a single pass of the model.

We will now see how this may be remedied. The key idea is to take very large integration steps - much larger than the sampling rate of the data - whilst incorporating sub-step information through additional terms in the numerical solver, through what is known as the log-ODE method.

ACDEtreated in this way is termed a rough differential equation, in the sense of rough path theory. Correspondingly we refer to this approach as neural rough differential equations. (Or less snappily, 'the log-ODE method applied to neural CDEs'.) This was introduced in [Mor+21b].

Remark 3.16. For the reader familiar with numerical SDEs, this inclusion of 'substep information' is directly analogous to the difference between the Euler-Maruyama method and Milstein's method. For the reader familiar with the Magnus expansion [Bla+09], then the log-ODE method is a generalisation to nonlinear differential equations.

More so than the rest of this chapter, this will rely on advanced theoretical tools from rough path theory. As such this material is deferred to Appendix B to avoid breaking the flow.

## Training neural SDEs

We will see in Chapter 4 that SDEs, as generative models, may be trained as GANs. However samples from SDEs are continuous-time paths, which necessitate a discriminator that admits a continuous-time path as an input - such as a neural CDE.

The main ideas for this were introduced in [Kid+21b; Kid+21a], and this will be discussed alongside neural SDEs in Chapter 4.

## Theoretical properties

## Universal approximation

In the CDE literature, it is a well-known theorem that they represent general functions on streams. We think [, Theorem 4.2], see also [Kid+19, Proposition A.6], give the clearest statement of this result. This may be applied to show that neural CDEs are universal approximators, which we summarise in the following informal statement.

(Informal) Theorem 3.9. An affine map on the terminal value of a neural CDE is a universal approximator from { sequences in R d x } to R.

The essential idea is that a suitably large CDE can compute a truncated basis for the space of continuous functions of its input. The final affine map may then take some affine combination of these, and in doing so approximate any continuous function.

Theorem C.25 in Appendix C.2.1 gives a formal statement and a proof, which generalises the original presentation in [Kid+20a, Appendix B].

This property is not necessary for good empirical performance (GRUs frequently achieve good performance without being universal approximators ), but it is reassuring to know that it may be accomplished in principle.

## Comparison to alternative ODE models

If unfamiliar with CDEs, then it may seem natural to replace f θ ( y ( s )) d x d s ( s ) with some h θ ( y ( s ), x ( s )) that is directly applied to, and potentially nonlinear , x ( s ). Indeed, special cases of this have been suggested before, in particular to derive the 'GRU-ODE' analogous to a GRU [Cho+14; De +19; ] (Example 3.14).

However, it turns out that something is lost by doing so, which we summarise in the following statement.

(Informal) Theorem 3.17. Any equation of the form y ( t ) = y + ∫ t 0 h θ ( y ( s ), x ( s )) d s may be represented exactly by a neural CDE of the form y ( t ) = y + ∫ t 0 f θ ( y ( s )) d x ( s ). However the converse statement is not true.

The essential idea is that a neural CDE can easily represent the identity function between paths, whilst the alternative is incapable of doing so. Theorem C.27 in Appendix C.2.2 provides the formal statement and proof, which originally appeared in [Kid+20a, Appendix C].

(This does not preclude using the h θ ( y ( s ), x ( s )) form if this happens to work on any given problem, of course.)

## Invariances

CDEs exhibit two possible invariances. In general these invariances are often undesirable and are removed as follows.

## Translation invariance and initial value networks

The integral defining the evolution of a neural CDE depends upon the control x only through its derivative d x d t. If this were the only way that x was input to the model, then y would be invariant to translations of x.

It is for this reason that the initial hidden state y depends on x through the initial value network ζ θ, so as to ensure sensitivity to translations. Other alternatives may also be admitted: a channel whose first derivative includes translation-sensitive information could be appended, for example by replacing x with ˜ x where ˜ x ( t ) = ( x ( t ), tx ).

## Reparameterisation invariance

CDEs exhibit a reparameterisation invariance property. 4 Proposition 3.18. Let ψ: [0, S] → [0, T] be differentiable, increasing, and such that ψ = 0 and ψ (S) = T. Let y solve a CDE driven by a path x. Then y ◦ ψ solves the same CDE driven by x ◦ ψ, and in particular their terminal values are the same: (y ◦ ψ)(S) = y (T).

This means that a CDE is blind to the speed at which x is traversed. Typically, the speed at which input data arrives is important (for example consider data indicating that a patient's health is declining over years - or over minutes), so this means that the speed at which events occur must be explicitly encoded as a channel in x. Indeed, this is precisely what is done in Section 3.1.4.2 by including time as a channel.

4 In fact they also exhibit a tree-like invariance property, which is a slight generalisation.

See Appendix C.2.3 for a proof, which is straightforward change of variables.

## Choice of parameterisation

So far we have discussed 'the mathematics'. Now we must discuss 'the engineering'. We must still choose optimisers, learning rates, model architectures and so . As is often the case with deep learning, these choices can make or break the efficacy of the model.

## Neural architectures and gating procedures

The initial value network ζ θ is typically parameterised as an MLP.

The vector field f θ is typically parameterised as f θ = tanh ◦ MLP θ, where tanh is applied elementwise, and MLP θ denotes an MLP with weights and biases θ and as in Section 2.3 uses a continuously differentiable activation function.

If the tanh were removed then the MLP could produce arbitrarily large and unconstrained outputs. In contrast the inclusion of a squashing function such as tanh constrains the rate of change of the hidden state. As f θ is iteratively evaluated multiple times over the differential equation, then large outputs from f θ can easily result in the model exploding, with large and untrainable losses.

This is precisely analogous to RNNs, where one of the key features of GRUs and LSTMs are gating procedures which control the rate of change of the hidden state. (Their other key feature is a differential equation like structure.)

Slightly more complex variations on the same theme may be considered. For example let φ θ, ψ θ: R d y → R d y × d x be neural networks; for efficiency often the same MLP just with different final affine layers. Then we may define f θ ( y ) = σ ( φ θ ( y ))) ∗ tanh( ψ θ ( y )), where ∗ denotes an elementwise product and σ is the sigmoid function applied elementwise.

## State-control-vector field interactions

If the vector field f θ: R d y → R d y × d x is a feedforward neural network, with final hidden layer of size d h ∈ N, then the number of scalars for the final affine transformation is of size O ( d h d y d x ), which can easily be very large.

As such this layer is often the greatest computational bottleneck of a neural CDE. But it is possible that not every three-way interaction between the hidden state y (of size d y ), control x (of size d x ), and penultimate layer in the vector field (the layer of size d h ) actually needs to be modelled.

Anecdotally, making the layer sparse (down to a density of about 1%) often still pro- duces good results, whilst rank-one representations of the final matrix f θ ( y ), as an outer product of transformations R d y → R d y and R d y → R d x seem to produce bad results. One can easily imagine many other kinds of reduced-parameter parameterisations, and this is a topic that merits further investigation.

## Multi-layer neural CDEs

Let y 1: [0, T] → R d y 1 solve a neural CDE driven by x: [0, T] → R d x, with system f θ, 1: R d y 1 → R d y 1 × d x: We may now repeat this procedure: let y 2: [0, T] → R d y 2 solve a neural CDE driven by y 1, with system f θ, 2: R d y 2 → R d y 2 × d y 1: This idea of stacking may of course be repeated arbitrarily many times.

The joint system may be solved together as a single CDE driven by x. For example in the two-layer case, we obtain The main disadvantage of this approach is that the output dimension of f θ, 2 is large (d y 1 × d y 2), and therefore computationally expensive.

This offers a sensible way to increase the model capacity of a neural CDE; see for example [Jhi+21]. This is precisely analogous to multi-layer RNNs, in which the hidden state of one RNN is used as the input to another.

## Interpolation schemes

Suppose we observe some (potentially irregular) time series, each of the form x = ((t 0, x 0),..., (t n, x n)), as in Section 3.1.4 or Section 3.2.1. Each t j ∈ R is the timestamp of observation where ∗ denotes the possibility of missing data, t 0 < · · · < t n. The length n is not assumed to be consistent between different time series.

We are interested in picking T > 0, 0 = s 0 < · · · < s n = T, and constructing interpolations x x: [0, T ] → R d x such that x x ( s j ) = ( t j, x j ).

Note that we could also include c j ( x ) channels, which in general are needed when handling missing data; see Sections 3.2.1.1 and 3.2.1.2. These are handled in precisely the same way as the x j channels (just construct interpolations x x: [0, T ] → R 2 d x -1 such that x x ( s j ) = ( t j, x j, c j ( x ))) so for simplicity of notation we leave them out here.

Remark 3.19. That neural CDEs need interpolation schemes sometimes attracts skepticism. Are we imputing missing data? Are we constructing a continuous-time approximation to some underlying data process? Why, morally speaking, should we need to construct an interpolation scheme when the actual data we have observed is discrete?

The answers are: 'no', 'yes (but it's not important)', and 'to process the data at its natural timescale', respectively. Each of these points has been discussed earlier in the text, in Remark 3.11, Remark 3.6, and Section 3.1.5.2 respectively.

We begin with some theoretical conditions that we would like ideal interpolation schemes to satisfy, and then present some sensible choices. The best choice of interpolation scheme will depend on the problem at hand.

Much of the following section is drawn from [Mor+21a].

## Theoretical conditions

There are two main theoretical conditions, namely measurability and smoothness.

## Measurability

Any given time series problem needs outputs at particular times. For example we may wish to only have an output after having observed an entire time series. Alternatively we may wish to produce a continuously-evolving output, updated as more data arrives over time.

We formalise this distinction in terms of measurability, 5 and will require an interpolation scheme that supports the desired behaviour.

We describe problems, and interpolation schemes, as exhibiting one of three different kinds of measurability. Figure 3.4 provides a visual summary.

Continuously measurable We say that an interpolation scheme is continuously measurable if x x ( s ) depends only on those ( t j, x j ) with s j ≤ s. (Recalling that x x ( s j ) = ( t j, x j ).) That is to say, only observations in the past or present may be used to define the interpolation scheme.

5 In [Mor+21a] the terminology of 'online' is used instead.

## CHAPTER 3. NEURAL CONTROLLED DIFFERENTIAL EQUATIONS

Figure 3.4: Summary of measurability definitions. Arrows indicate what data can influence. A green dot indicates that a measurable prediction can be made at that point. Left: a continuously measurable model in which no information is passed backward in time, resulting in a measurable solution at all points in time. Middle: a discretely measurable model in which information can be passed backwards-in-time, but no further than the preceding observation. Right: a non-measurable scheme in which information is passed backward in time further than the preceding observation.

This is probably the most intuitively natural definition of measurability, but it is relatively difficult to construct interpolation schemes satisfying it. (We will present only a single such scheme.) Practically speaking many use cases will find a weaker notion of measurability acceptable.

This kind of measurability is needed if data is arriving over time at inference time (sometimes described as the problem being online ), and either:

- model predictions are needed between observations; - model predictions are needed prior to the final observation in a time series, and there is missing data.

Discretely measurable We say that an interpolation scheme is discretely measurable if x x ( s ) depends only on those ( t j, x j ) with s j -1 ≤ s. That is to say, we may look up to one observation into the future when defining the interpolation scheme.

For example, this is the case with linear interpolation. s ↦→ (1 -s ) a + sb with s ∈ depends on b for all s, even though b will only be attained at s = 1.

This kind of measurability is needed if data is arriving over time at inference time (sometimes described as the problem being online ), and model predictions are only needed at observations, and there is no missing data. Simply integrate up to some s j, wait until ( t j +1, x j +1 ) are observed, and then interpolate and integrate over [ s j, s j +1 ].

Non-measurable Finally we say that a scheme is not measurable if x x ( s ) may depend only on any and all ( t j, x j ). For example, this is the case with natural cubic splines.

Such schemes are appropriate if, at inference time, the whole time series will be available prior to evaluating the model.

## Smoothness

The second desirable theoretical property for an interpolation scheme is smoothness.

We will not define smoothness in a mathematically rigorous way. Rather, we point out that 'smoother' interpolation schemes will result in easier-to-integrate dynamics, which will improve the computational efficiency of the model.

The main dichotomy here is whether the dynamics are globally smooth (for example a cubic spline) or piecewise smooth (for example linear interpolation). The former is preferable but the latter can be tolerated.

Remark 3.20. See Section 5.3.3 for how to correctly integrate piecewise smooth dynamics when using adaptive step size solvers.

See also Section 5.4.1.4, which (mainly in the neural ODE setting) seeks to regularise higher-order derivatives in order to promote easy-to-integrate dynamics.

## Choice of interpolation points

The choice of T > 0 and interpolation points s j (such that x x ( s j ) = ( t j, x j )) is really about determining the desired behaviour of the numerical solver.

In continuous time, this choice is arbitrary, by the reparameterisation property of Section 3.3.3.2. The value of the integral is invariant to the choices of T and s j.

Practically speaking, this does not completely carry through to the numerical discretisation. For example consider using s j = j and a fixed-step numerical solver with unit step size. Then a single numerical step is made between each observation, a fixed number of vector field evaluations would be made, and the neural CDE reduces to an RNN.

Overall, the spacing between s j corresponds roughly to the amount of computational work that should be done between those observations. (Either precisely, when using a fixed solver, or approximately, when using an adaptive solver.) As per Section 3.1.5.2, a desirable choice is for the amount of computational work to scale with the 'natural timescale' at which the data varies. For many datasets this means a reasonable choice is s j = t j.

## Particular interpolation schemes

There are a few main interpolation schemes of interest. In every case, each channel is interpolated separately. If there is missing data then it is interpolated over; for example if x j, 1 and x j +2, 1 are observed but x j +1, 1 is missing then we apply the following procedures over [ s j, s j +2 ] rather than [ s j, s j +1 ].

## Hermite cubic splines with backward differences

The first choice of interest are Hermite cubic splines with backward differences. Each interval [s j, s j +1) is treated independently, and the interpolation over this interval is chosen to satisfy Measurability This scheme is discretely measurable.

Smoothness Such splines are by construction continuously differentiable, so adaptive step size solvers will find the resulting dynamics easy to integrate.

Choice of s j Typically s j = t j is a reasonable choice.

## Linear interpolation

One simple option is just linear interpolation: (Mapping over each entry of the (t, x) tuple.)

Measurability This scheme is discretely measurable.

Smoothness This scheme is only piecewise continuously differentiable. If reducing the neural CDE to an ODE by taking ∫ f θ ( y ( s )) d x ( s ) = ∫ f θ ( y ( s )) d x d s ( s ) d s as in equation (3.6), then the vector field f θ ( y ( s )) d x d s ( s ) will be piecewise constant.

This makes linear interpolation a poor choice if using an adaptive step size numerical solver, which will struggle with these jumps. However if using a fixed step size solver it can be just as good as Hermite cubic splines with backward differences, whilst being slightly cheaper to compute.

Choice of s j Typically s j = t j is a reasonable choice.

## Rectilinear interpolation

Define ¯ x j = (¯ x j, 1,..., ¯ x j,d x -1 ) ∈ R d x -1 as being the fill-forward 6 of x j.

Now additionally select points r j ∈ [0, T], for j ∈ { 1,..., n }, such that Rectilinear interpolation is defined by taking x x (s j) = (t j, ¯ x j), x x (r j) = (t j +1, ¯ x j), and linearly interpolating between s 0, r 1, s 1, r 2,..., r n, s n.

Measurability This now satisfies the measurability condition we require. At inference time we can wait at each s j for the next data point to arrive (regardless of whether it is only partially observed / has missing data), interpolate over [ s j, s j +1 ] in the manner above, and then solve the CDE over [ s j, s j +1 ].

Smoothness Rectilinear interpolation is only piecewise differentiable. As with linear interpolation, when reduced to an ODE then the vector field has jumps. Fixed step size solvers are one resolution to this problem. Alternatively an adaptive step size numerical solver can be made aware of these jumps so as to treat them in the appropriate way, see Section 5.3.3.

Choice of s j and r j Typically s j = t j + j and r j = t j + j -1 is a reasonable choice.

## Natural cubic splines

One simple approach is to use natural cubic splines. (Indeed this was used in the original neural CDE paper [Kid+20a].)

Measurability Unfortunately, natural cubic splines are not measurable. This limits their applicability.

Smoothness However, natural cubic splines are at least very smooth.

Choice of s j Typically s j = t j is a reasonable choice.

6 Explicitly: let ¯ x j,k = x ¯ j ( j,k ),k, where ¯ j ( j, k ) = max { m ≤ j | x m,k = ∗}, recalling that ∗ denotes missing data. If this set is empty then define ¯ x j,k = 0.

Model performance For reasons unknown, neural CDEs that use natural cubic splines produce slightly worse results than those using other interpolation schemes [Mor+21a].

## Overall

Most problems will find either Hermite cubic splines with backward differences or rectilinear interpolation to be of most interest. Use Hermite cubic splines with backward differences if possible, due to their smoothness and relatively good measurability. If their measurability properties are insufficient, then use rectilinear interpolation.

## Comments

CDEs are a classic piece of mathematics, emerging essentially as a meaningful special case of the more general rough differential equations introduced. The first few pages of [Hod+20] give an excellent brief introduction to the essential ideas. is our recommended introductory text. is the canonical reference text.

(As a fascinating historical note, the essential ideas behind CDEs may actually be traced back to Newton [, Prob. 1, Prob. 2]. Newton considers evolving systems in multiple variables, with position (fluent) and derivative (fluxion). Given a relation for either fluent or fluxion, then the other is then solved . Obtaining the relation of fluents from a relation of fluxions is precisely what we would term 'solving a CDE'. We thank Terry Lyons for this observation.)

Various texts use different pieces of terminology to refer to the concept of a CDE. Much of the rough path literature uses the terms CDE and RDE interchangeably. Meanwhile prefer to use CDE and ODE interchangeably. Some texts use the term 'controlled ordinary differential equations'.

Specifically neural CDEs were first introduced in [Kid+20a], where they were applied to both regular and irregular time series, and most of the relevant theoretical properties discussed. The follow-up work [Mor+21a] investigated the choice of interpolation scheme, and promoted the use of the alternative ones just presented ([Kid+20a] used only natural cubic splines). The discussion here is an extension of the one introduced there, and is partly new here. Rectilinear interpolation is due to; the pieces of the interpolation for which the time channel is constant are sometimes referred to as 'virtual time'.

Many of the computational concerns discussed (batching, smoothness and so on) arose from experimentation using both and. The discussion on batching (Section 3.2.1.3) is new here, and is relevant beyond just CDEs - much of the literature has assumed that a differential equation solver must operate over the same time interval for each batch element, and had to work around this limitation (see for example the 'time-varying CNF' of).

We recall the link between CDEs and control theory (Section 3.1.6.2). Meanwhile control theory has well-known links to reinforcement learning (RL). RL applications either explicitly including or of essentially similar character to neural CDEs therefore include [; Kil+20; Lut+21] amongst others.

The neural RDE formulation applying neural CDEs to long time series was introduced in [Mor+21b]. The same rough path theoretic ideas also appear in [Fer+21], to frame RNNs as a kernel method.

Applications to training neural SDEs (really the focus of our next chapter) were introduced in [Kid+21b; Kid+21a].

Much of the discussion on good architectural choices, gating, sparsity and so , is new here.

## Chapter 4

## Neural Stochastic Differential Equations

## Introduction

## 4.1.1

## Stochastic differential equations

Stochastic differential equations have seen widespread use for modelling real-world random phenomena, such as particle systems [ ], financial markets [ ], population dynamics [; ] and genetics. They are a natural extension of ordinary differential equations (ODEs) for modelling systems that evolve in continuous time subject to uncertainty.

The dynamics of an SDE consist of a deterministic term and a stochastic term: are suitably regular functions, w: [0, T] → R d w is a d w -dimensional Brownian motion, and y: [0, T] → R d y is the resulting d y -dimensional continuous stochastic process.

The strong solution y is guaranteed to exist and be unique given mild conditions: that µ, σ are Lipschitz, and that E [ y 2 ] < ∞.

We refer the reader to for a rigorous account of stochastic integration.

Itˆ o versus Stratonovich The notation ' ◦ ' in the noise refers to the SDE being understood in the sense of Stratonovich integration. This is as an alternative to the standard notion of Itˆ o integration. where The reader unfamiliar with Stratonovich integration should generally feel free to ignore this subtlety. Stratonovich SDEs will sometimes be slightly more efficient to backpropagate through (Remark 5.12, later). However, any Itˆ o SDE may be converted to a Stratonovich SDE, and vice versa, so as we will shortly introduce learnt (neural) vector fields then modelling-wise the choice is arbitrary.

Theoretical construction of SDEs SDEs have typically been constructed theoretically, and are usually relatively simple.

One frequent and straightforward technique is to fix a constant matrix σ, and add ' σ ◦ d w (t)' to a pre-existing ODE model. 1 As another example, the Black-Scholes equation, widely used to model asset prices in financial markets, has only two scalar parameters: a fixed drift and a fixed diffusion.

Calibrating SDEs Once an SDE model has been chosen, then model parameters must be calibrated 2 from real-world data.

Since SDEs produce random sample paths, the parameters are typically chosen so that the average behaviour of the SDE matches some statistic(s). A classical approach to calibrating SDEs to observed data y true is to pick some prespecified functions of interest F 1,..., F N, and then ask that E y [F i (y)] ≈ E y true [F i (y true)] for all i. For example this may be done by optimising where the model y depends implicitly on parameters θ.

This ensures that the model and the data behave the same with respect to the functions F i. The functions F i are known as either 'witness functions' or 'payoff functions' depending on the field [Li+17; ]. If the SDE is simple enough - for example the analytically tractable Black-Scholes model - then equation (4.2) can often be computed explicitly.

## Generative and recurrent structure

SDEs feature inherent randomness. In modern machine learning parlance SDEs are generative models.

1 In passing we remark that Itˆ o and Stratonovich are identical in this case as the noise is additive so the corresponding Itˆ o-Stratonovich correction term is zero. We could equally well have written ' σ d w ( t )'.

Comparison to random RNNs As usual, a numerically discretised neural (stochastic) differential equation has a correspondence in the deep learning literature. As with neural CDEs, the appropriate analogy is an RNN. In this case its input is random noise - Brownian motion - and its output is a generated sample.

Consider the autonomous one-dimensional Itˆ o SDE with y (t), µ (y (t)), σ (y (t)), w (t) ∈ R. Then its numerical Euler-Maruyama discretisation is where ∆ t is some fixed time step and ∆ w j ∼ N (0, ∆ t). This numerical discretisation is clearly just an RNN of a particular form.

Generative time series models Each sample y from an SDE is a continuous-time path y: [0, T] → R d y. As such, we may treat neural SDEs as generative time series models.

(Generative) time series models are of classical interest, with forecasting models such as Holt-Winters [; ], ARMA, ARCH, GARCH and so .

It has also attracted much recent interest , besides neural SDEs, the development of ODE-based models like latent ODEs (Section 2.2.4) 3; discrete-time models like Time Series GAN; non-ODE continuous-time models like CTFPs [Den+20; Den+21] and Copula Processes.

See Figure 4.1 for an abstract summary of many of the essential ideas: that SDEs are generative time series models, how SDEs may classically be calibrated, and one of the ways in which we will later generalise this approach to neural networks, via SDE-GANs (Section 4.3.1).

'Static' generative models We may also consider just the terminal value y (T) of an SDE This is a sample drawn from some distribution over R d y. As such we may also treat neural SDEs as 'static' generative models - that is to say, not over a time series.

This immediately draws natural connections to a variety of topics. This is the same basic set-up as a continuous normalising flow (Section 2.2.3), except that the randomness is injected via a Brownian motion w rather than a random initial condition y.

3 And related ideas such as ODE 2 VAE or Neural ODE Processes [Nor+21] Figure 4.1: Brownian motion is continuously injected as noise into an SDE to generate time series. The classical approach fits the SDE to prespecified statistics. One (important) way of handling neural SDEs is to generalise from prespecified statistics to a learnt statistic, namely the discriminator of a (Wasserstein) GANs.

It is also the same starting point used in score-based generative modelling, in which a neural drift and fixed additive diffusion is used, with the initial-to-terminal map calculating a transition between two distributions [Son+21b; Bor+21].

We shall focus mainly on the time-series case discussed in the previous heading. At time of writing, the connections between neural SDEs as presented here, and CNFs and score-based modelling, are largely unexplored.

Comparison to neural CDEs We have now described both neural CDEs and neural SDEs as 'continuous time RNNs'. It is worth being precise about the distinction.

(Neural) CDEs model functions of time series, or equivalently functions of paths. The path is an input and the output is, for example, a classification result determining whether the input path is a clockwise or anticlockwise spiral.

(Neural) SDEs model distributions on time series, or equivalently distributions on paths. Rather than modelling some function of the path, it is is the paths themselves that are being modelled.

In this respect the terminology of differential equations is slightly more precise than the terminology of neural networks, which uses 'RNN' to describe both concepts.

## Construction

The following constructions are primarily from [Kid+21b].

Let T > 0 be a fixed time horizon and consider a path-valued random variable x true: [0, T ] → R d x, with d x ∈ N the dimensionality of the data. x true is what we wish to model, and is the random variable we assume we have observed samples . For example, this may correspond to the evolution of stock prices over time.

(Typically we actually observe x true only at some discretised time stamps; not over a full continuous-time path. For ease of presentation we neglect this detail for now and will return to it later.)

Let w: [0, T] → R d w be a d w -dimensional Brownian motion, and let v ∼ N (0, I d v × d v) be drawn from a d v -dimensional standard multivariate normal. The values d w, d v ∈ N are hyperparameters describing the size of the noise. Let where ζ θ, µ θ and σ θ are neural networks. Collectively ζ θ, µ θ, σ θ, α θ and β θ are parameterised by θ. The dimension d y is a hyperparameter describing the size of the hidden state.

Then a neural stochastic differential equation is a model of the form for t ∈ [0, T], with y: [0, T] → R d y the (strong) solution to the SDE.

The objective will be to train θ so that the distribution of the model x is approximately equal to the distribution of the data x true. (For some notion of 'approximate'.)

Architecture Equation (4.4) has a certain minimum amount of structure. First, the solution y represents hidden state. If it were the output, then future evolution would satisfy a Markov property which need not be true in general. This is the reason for the additional readout operation to x.

Second, there must be an additional source of noise for the initial condition, passed through a nonlinear ζ θ, as x = α θ ζ θ (v)+ β θ does not depend on the Brownian noise w. This will be a learnt approximation to the initial condition of the SDE. ζ θ, µ θ, and σ θ may be taken to be any standard network architectures, such as feedforward networks.

RNNs as discretised SDEs This minimal amount of structure parallels that of RNNs. The solution y corresponds to the hidden state of an RNN.

Sampling Given a trained model, we sample from it by sampling some initial noise v and some Brownian motion w, and then solving equation (4.4) with a numerical SDE solver.

Comparison to the Fokker-Planck equation The distribution of an SDE, as learnt by a neural SDE, contains more information than the distribution obtained by learning a corresponding Fokker-Planck equation. The solution to a FokkerPlanck equation gives (the time evolution of) the probability density of a solution at fixed times. It does not encode information about the time evolution of individual sample paths. This is exemplified by stationary processes, whose sample paths may be nonconstant but whose distribution does not change over time.

## Training criteria

Equation (4.4) produces a random variable x: [0, T ] → R d x implicitly depending on parameters θ. This model must still be fit to data. This may be done by optimising a distance between the probability distributions (laws) for x and x true.

There are two main options: fitting a Wasserstein distance, or fitting a KL divergence. These correspond to SDE-GANs and latent SDEs respectively.

## SDE-GANs

Let P x denote the law of the model x. Likewise let P x true denote the (empirical) law of the data x true. Let W (P x, P x true) denote the 1-Wasserstein distance between them. We may train the model by optimising where P x depends implicitly on the learnt parameters θ.

We will do so in the usual way for Wasserstein GANs, by constructing a discriminator and training adversarially.

Each sample from the generator is a continuous path x: [0, T ] → R d x; these are infinite dimensional and the discriminator must accept such paths as inputs. Fortunately there is a natural choice: parameterise the discriminator as a neural CDE, as in Chapter 3.

This approach is due to [Kid+21b].

Figure 4.2: Summary of equations for an SDE-GAN.

## Architecture Let

where ξ φ, f φ and g φ are (Lipschitz) neural networks. Collectively they are parameterised by φ. The value d h ∈ N is a hyperparameter describing the size of the hidden state.

Recalling that x is the generated sample, we take the discriminator to be a CDE for t ∈ [0, T], with h: [0, T] → R d h the (strong) solution to this CDE, and where · denotes the dot product.

The solution to the CDE exists given mild conditions, namely Lipschitz f φ and g φ; simply concatenate (4.4) and (4.5) together and treat the joint system as an SDE.

The value D ∈ R, which is a function of the terminal hidden state h ( T ), is the discriminator's score for real versus fake; correspondingly we define the overall action of the discriminator via F φ ( x ) = D. This is a deterministic function of the generated sample x.

Summary of equations See Figure 4.2 for a summary of equations, combining together both generator and discriminator.

Training loss The training loss is the usual one for Wasserstein GANs [Goo+14;], namely optimisation with respect to Training is performed via stochastic gradient descent techniques as usual.

This generalises the classical approach to calibration seen in equation (4.2). Instead of optimising over some fixed collection of payoff functions { F i } N i =1, we optimise over some infinite collection of discriminators { F φ } φ.

Remark 4.1. In Chapter 3, we emphasised the need to include time as a channel in the control of a neural CDE. This corresponds to the inclusion of a 'drift' term in equation (4.5). Equivalently we could replace x with t ↦→ ( t, x ( t )) and use the same notation as Chapter 3.

## Lipschitz regularisation

Wasserstein GANs need a Lipschitz discriminator. A variety of methods have been proposed in the GAN literature, such as weight clipping, gradient penalty [Gul+17], or spectral normalisation [Miy+18]. The recurrent nature of the SDE setting means that a little care is needed to employ these successfully - see Section 4.4.3.

## Discretised observations

Observations of x true are typically a discrete time series, rather than a true continuoustime path. This is not a serious hurdle. Simply evaluate (4.5) on an interpolation x true of the observed data. The effect of this is as follows.

Dense data regime Suppose we observe samples from x true 'densely' - that is, with little gap between successive values in time. (Of approximately no more than the step size of the numerical solver.) Then interpolation produces a distribution in path space; the one desired to be modelled. Simple linear interpolation will be sufficient, but due to the dense sampling of the data this is a choice that is largely unimportant.

Technically speaking, as (linear) interpolation will produce a path of bounded variation, then (4.5) will be defined as a Riemann-Stieltjes integral.

Sparse data regime Now suppose data is not observed densely, and may even have substantial time gaps between observations. In this case, we fall back to the neural CDE approach: sample the generated paths at some collection of time points, and interpolate both the generated sample and the true data. (Before passing them to the discriminator defined as a Riemann-Stieltjes integral in both cases.)

This is the familiar setting for applying neural CDE to time series, as set up in Chapter 3. The interpolation scheme has simply become part of the discriminator, and no modelling or discriminatory power is lost.

## Single SDE solve

If working in the dense data regime, then (4.4) and (4.5) may be concatenated together into a single SDE solve. This is of relevance if training using optimise-then-discretise, or with a reversible solver. Both of these are topics we will discuss in Chapter 5; the reader unfamiliar with these concepts should feel free to skip this heading for now.

The state is the combined [y, h], the initial condition is the combined the drift is the combined and the diffusion is the combined Then h (T) is extracted from the final hidden state, and m φ applied, to produce the discriminator's score for that sample.

Training in this way improves memory efficiency, as the SDE solution y: [0, T ] → R d y and the output x: [0, T ] → R d x are not recorded during training. The asymptotics improve from O ( H + T ), as in Section 3.1.5.3, to just O ( H ), where H is the memory cost of evaluating and backpropagating the vector fields once.

## Latent SDEs

We will now consider training not with respect to the Wasserstein distance, but with respect to the KL divergence. This approach is due to [Li+20a]. be Lipschitz neural networks parameterised by φ. The notation { [0, T] → R d x } denotes the space of all functions [0, T] → R d x.

Remark 4.2. We do not discuss the regularity of the functions in { [0, T] → R d x }, as this input to ν θ will actually be a sample of x true, and in practice we will have discrete observations. ν φ is commonly parameterised as ν φ (t, y, x) = ν φ, 1 (t, y, ν φ, 2 (x | [t,T])), where ν φ, 1 is an MLP and ν φ, 2 is either a reverse-time RNN/NCDE or the evaluation function ν φ, 2 (x | [t,T]) = x (t).

Note that w is the same Brownian motion as used in (4.4). Similarly α θ ∈ R d x × d y, β θ ∈ R d x and σ θ are the same objects defined in (4.3).

In doing so, we have constructed another SDE using the same diffusion as the main generative model, but with a different initial condition and drift. There is a standard formula for the KL divergence between two SDEs with the same diffusion, which in this case is given by where (σ θ (t, ̂ y (t))) -1 is the Moore-Penrose pseudoinverse of σ θ (t, ̂ y (t)). Note that although y does not appear explicitly on the right hand side, y defines (and is defined by) the µ θ and σ θ which do appear.

Remark 4.3. Equation (4.7) may be identified as an integral over the KL divergence between two Gaussians.

This opens up a possible training procedure. This 'auxiliary' SDE, which depends on samples of the observed data x true, may be used to autoencode the data. Once the data is represented as an SDE, we may remove the dependence on x true by minimising a KL divergence between our original generative model and the auxiliary model.

Explicitly, this corresponds to training according to Remark 4.4. Note that this training procedure only involves solving the auxiliary SDE, never the original SDE. The main generative model is trained without ever being evaluated.

As a variational autoencoder [Li+20a] interpret this procedure as a variational autoencoder, with a learnt prior, whose latent space is an entire stochastic process. (And indeed the above formula may be derived as an evidence lower-bound.) For this reason [Li+20a] refer to the auxiliary SDE as a posterior SDE.

Interpreted in this way, the first two terms are a VAE for generating x, with latent v. Meanwhile the third term and fourth term are a VAE for generating x, by autoencoding x true to ̂ x, and then fitting y to ̂ y.

Single SDE solve Equation (4.7) is an integral, and so may be estimated by concatenating it alongside the SDE solve.

Alternate probability densities The first and third terms of (4.7) are the L 2 loss, which corresponds to maximising the log-likelihood of x true (t) with respect to a fixed-variance Gaussian whose mean is ̂ x (t): However other probability densities are also admissible. As such the above presentation is chosen for simplicity, and compatibility with the presentation of the generative model in Section 4.2. The affine map corresponding to α θ, β θ is being used to produce the mean of a fixed-variance Gaussian, but it may be replaced by any other procedure for producing the parameters of some probability distribution, and the log-likelihood optimised as normal.

## Comparisons and combinations

The difference between SDE-GANs and latent SDEs is essentially the standard GAN/VAE split. SDE-GANs are more finicky to train, but exhibit substantially higher modelling capacity. Conversely, latent SDEs are easy to train, but often produce worse final models; in particular it is a common feature of latent SDEs that their diffusion will be too small.

It is possible to combine both latent SDEs and SDE-GANs together. (And indeed GAN/VAE hybrids have been proposed in the main deep learning literature too [Lar+15; Bou+17; Ros+17].) This is a way to offset the weakness of each approach with the strengths of the other. An example of this is given in Section 4.5, applied to modelling a Lorenz system.

## Choice of parameterisation

As usual with deep learning, the theoretical construction is only half of the work needed to produce a workable model, and the 'engineering details' - of finding good hyperparameters, optimisers, and so on - still remain.

At time of writing, finding good choices is still largely an open problem for neural SDEs. Much inspiration can likely be drawn from the mainstream generative modelling literature, which has spent the past few years investigating this topic in depth: see for example negative momentum [Gid+19], complex momentum [Lor+21], stochastic weight averaging (Ces` aro means) [Izm+18; Yaz+19], progressive growing [Kar+18], Lipschitz regularisation [Gul+17; Miy+18], architectural choices [Luc+18; Kar+19] and so .

## Choice of optimiser

## SDE-GANs

SDE-GANs can be relatively unstable to train.

Adadelta Empirically, Adadelta, or the similar RMSprop, seems to outperform either SGD or Adam when training SDE-GANs. In part this is because Adadelta lacks momentum; a lack of momentum is beneficial as the optimisation criterion for a GAN is a moving target.

Adam with β 1 = 0, where β 1 is its momentum hyperparameter, also seems to be outperformed by Adadelta.

Learning rate The initial networks ζ θ and ξ φ often work best with a larger learning rate than is used for the rest of the model. (For example a factor of 10 would be typical.) This helps to offset the fact that the initial distribution (of x ) often gets relatively weak supervision compared to the time-varying component (of t ↦→ x ( t )).

Stochastic weight averaging Using the Ces` aro mean of both the generator and discriminator weights, averaged over training, can improve performance in the final model [Izm+18; Yaz+19]. This averages out the oscillatory training behaviour for the min-max objective used in GAN training.

## Latent SDEs

Latent SDEs are relatively easy to train. Given their VAE-like structure, standard optimisers like Adam work without difficulty.

Once again it is still usually worth increasing the learning rate for ζ θ and ξ φ.

## Choice of architecture

## Generator

Recall that µ θ and σ θ were the drift and diffusion of the SDE, defined in (4.3). µ θ and σ θ are typically taken to be MLPs. Numerical SDE solvers will usually demand that the vector fields be sufficiently smooth (for example, bounded with continuous bounded first and second derivatives), so the activation function is often taken to be smooth, like softplus or SiLU.

Final nonlinearities It is common to add a final tanh nonlinearity to µ θ and σ θ. This is for the same reason as neural CDEs: to prevent an unconstrained rate of change in the hidden state and the model potentially exploding (especially at initialisation). If this constrains the rate of change too strongly, then this may be managed by parameterising µ θ and σ θ as where γ ∈ R is a learnt scalar (part of θ).

Initialisation As with ODEs (Section 2.3.1.3), training dynamics may be improved by initialising µ θ and σ θ close to zero.

Choice of driving noise The construction of this chapter has taken the driving noise w to be a Brownian motion. This choice is not necessary; for example fractional Brownian motion or L´ evy processes could also be used, together with or instead of the Brownian motion w.

A choice of particular interest are counting processes t ↦→ N (t) (for example the cumulative sum of a Poisson process) so that the resulting SDE is a jump process where the notation ' t -' is used to emphasise that the vector field depends upon the value immediately prior to the jump.

The optimisation criteria can get slightly more involved in these cases: whilst the SDE-GAN approach translates over without any changes, at time of writing the latent SDE approach has not yet been explored. See also who develop a direct likelihood-based approach to optimise diffusionless drift/jump processes of the form Diffusions for latent SDEs When training a latent SDE, then the KL divergence of equation (4.7), used in the latent SDE, multiplies by the (pseudo)inverse of σ θ. This is expensive to compute for general matrices.

One effective simplification is to take d w = d y and parameterise the diffusion σ θ as a diagonal matrix. This is cheap to compute the inverse of: take the reciprocal of each diagonal element.

For numerical stability it is additionally often desirable to then bound these diagonal elements away from zero: use z ↦→ sigmoid( z ) + 10 -4 as a final nonlinearity for σ θ, or alternatively clamp any values in the range to the edges of that range.

Approximation properties Provided µ θ and σ θ are drawn from suitable (universal approximating) classes of functions, then it is clear that (4.4) is more than capable of approximating any Markov SDE, by the universal approximation theorem for neural networks [; ] and standard approximation results for SDEs.

What is less clear is its ability to model non-Markov SDEs. Certainly this is possible to some extent, due to the explicit use of hidden state. (Indeed this is the reason hidden state is introduced in the first place.) At time of writing a formal result has not been derived.

## Discriminator

When training an SDE-GAN, then additional networks ξ φ, f φ, g φ are introduced. These should be parameterised in accordance with neural CDEs (Section 3.4).

The initial distribution, learnt by ζ θ, can often be improved by providing it additional supervision during training. Redefine D = m φ · h + m φ · h ( T ) or D = κ φ ( x ) + m φ · h ( T ) instead of just D = m φ · h ( T ) in equation (4.5), where κ φ is some neural network.

As with any Wasserstein GAN, the discriminator should be Lipschitz. This is the focus of our next section.

## Lipschitz regularisation

This section is specific to SDE-GANs. SDE-GANs, as with any Wasserstein GAN, need a Lipschitz discriminator.

A variety of methods for enforcing Lipschitzness have been proposed in the general GAN literature, such as weight clipping, gradient penalty [Gul+17], or spectral normalisation [Miy+18]. However a little care must be taken when applying these to the discriminator of an SDE-GAN.

Much of the following discussion originated in [Kid+21a].

## Exponential Lipschitz constant

Given vector fields with Lipschitz constant λ, then the recurrent structure of the discriminator means that the Lipschitz constant of the overall discriminator will be O ( λ T ). This is a key consideration in performing Lipschtiz regularisation, and unfortunately, the aforementioned techniques cannot simply be applied 'off the shelf'.

Lipschitz constant one The first option will be to somehow ensure that the vector fields f φ and g φ of the discriminator are not only Lipschitz, but have Lipschitz constant at most one. Ensuring λ ≈ 1 with λ ≤ 1 will enforce that the overall discriminator is Lipschitz, with a Lipschitz constant of approximately one, as well.

This will be the approach we take in Section 4.4.3.2.

Hard constraint The exponential size of O ( λ T ) means that λ only slightly greater than one is still insufficient for stable training. This is why we specify ' λ ≈ 1 with λ ≤ 1' and not merely ' λ ≈ 1'. Moreover, it rules out enforcing λ ≈ 1 via soft constraints like spectral normalisation.

Whole-discriminator regularisation The second option is to regularise the Lipschitz constant of whole discriminator, without regard for its recurrent structure. This will be the approach we take in Section 4.4.3.3.

## Careful clipping

Let us (within this subsection) now assume that our discriminator vector fields f φ, g φ are MLPs. This is also a common choice made in practice.

Careful clipping Consider each linear operation from R a → R b as a matrix in A ∈ R a × b. After each gradient update, clip its entries to the region [ -1 /b, 1 /b ]. Given z ∈ R a then this enforces ‖ Az ‖ ∞ ≤ ‖ z ‖ ∞.

LipSwish activation function Next we must pick an activation function with Lipschitz constant at most one. It should additionally be at least twice continuously differentiable to ensure convergence of a numerical SDE solver. In particular this rules out the ReLU.

There remain several admissible choices. We tend to use the LipSwish activation function introduced by [Che+19], defined as ρ ( z ) = 0. 909 zσ ( z ), where σ denotes the sigmoid function. This has Lipschitz constant one (due to the carefully-chosen 0. 909 scaling factor), and is smooth. Moreover the SiLU activation function from which it is derived has been reported as an empirically strong choice [ ].

Overall The overall vector fields f φ, g φ of the discriminator consist of linear operations (which are constrained by clipping), adding biases (an operation with Lipschitz constant one), and activation functions (taken to be LipSwish). Thus the Lipschitz constant of the overall vector field is at most one, as desired.

## Gradient penalty

Another option is to directly regularise the Lipschitz constant of the entire discriminator, via gradient penalty. Add as a regularisation term to the training loss, where ̂ x is sampled according to ̂ x = αx +(1 -α) x true with x ∼ P x and x true ∼ P x true and α ∼ Uniform.

This approach works, which is more than can be said for other na¨ ıve approaches. However, compared to the careful clipping of Section 4.4.3.2, this approach mostly comes with disadvantages.

Disadvantages Because (4.8) involves calculating a gradient, then optimising it involves calculating a second derivative - a 'double backward'.

This is of relevance if training using optimise-then-discretise, which is a topic we will discuss in Chapter 5. (The reader unfamiliar with this concept should feel free to skip this heading for now.)

If training proceeds using optimise-then-discretise, then as a single backward constructs an 'adjoint SDE', a double backward constructs an 'adjoint-of-adjoint SDE'. This starts to imply substantial errors in the numerical discretisation, and this can be sufficient to degrade or destroy training.

Another negative is the additional computational cost implied by computing, and autodifferentiating, (4.8). This can easily result in a training procedure that takes about 50% longer than the careful clipping approach.

Remark 4.5. We sidestep questions of how the derivative in (4.8) is defined - given that ̂ x is path valued - by defining it with respect to the numerically discretised solution of ̂ x. In practice gradient penalty is not the preferred option, due to the disadvantages already discussed, so this is not an issue we will seek to tackle formally.

## Examples

Brownian motion As a simplest-possible first example, consider a dataset of samples of (univariate) Brownian motion, with initial condition Uniform. Each element of the dataset is a time series of observations along a single Brownian sample path. We train a small SDE-GAN to match the distribution of the initial condition and the distribution of the time-evolving samples; see Figure 4.3.

This example may seem almost trivially simple, and yet it highlights a class of time series that would be almost impossible to learn with a latent ODE (Section 2.2.4). A Brownian motion represents pure diffusion, whilst a latent ODE is pure drift.

## samples from both real and generated distributions

Figure 4.3: Coarsely-spaced ( t, y ) samples of a Brownian motion, and an SDE-GAN trained to match its distribution.

## samples from both real and generated distributions

Figure 4.4: Finely-spaced ( t, y ) samples of a time-dependent Ornstein-Uhlenbeck process, and an SDE-GAN trained to match its distribution.

Time-dependent Ornstein-Uhlenbeck process Next we consider training an SDE-GAN to recover the distribution of This example introduces explicit time dependency; in particular a time-dependent diffusion.

That this has both nontrivial drift and diffusion makes it an example of a process that is easy to learn via SDEs, but would be difficult to learn with models such as a latent ODE (which is pure drift; Section 2.2.4) or a CTFP (which is almost-pure diffusion; [Den+20]).

Damped harmonic oscillator Next we consider a dataset of samples from a twodimensional damped harmonic oscillator.

This example is multidimensional, pure-drift, and solved over a long time interval.

In this case we train a latent SDE to recover the distribution. See Figure 4.5, which shows a single sample, in the ( y 1, y 2 )-plane, from both the true and generated dataset. (So that time evolves as the trajectory spirals inwards.)

It is by coincidence that the generated sample begins so close to, and partway along, the true sample. (They are not necessarily meant to overlap.) The generated sample

## One sample from both real and generated distributions

Figure 4.5: A single ( y 1, y 2 )-plane sample of a damped harmonic oscillator, and a latent SDE trained to match its distribution.

10 samples from both real and generated distributions.

Figure 4.6: Evolving (y 1, y 2, y 3) samples from a Lorenz attractor, and a 'latent SDE-GAN' trained to match its distribution does an excellent job at matching the drift, even extrapolating past the end of the true sample. The only issue is that the diffusion is still too high - indeed the true diffusion is zero - demonstrating that some additional training may still be required. Nonetheless this demonstrates how neural SDEs subsume neural ODEs as a special case, practically as well as theoretically.

Lorenz attractor We consider a dataset of samples from the Lorenz attractor This example is multidimensional, chaotic, and has state-dependent diffusion. 4 We train a combined latent SDE / SDE-GAN on this dataset. They are combined simply by interchanging separate training steps: one as a latent SDE, followed by one as an SDE-GAN. See Figure 4.6. The model has correctly learnt the distribution of this chaotic multidimensional time series.

Further details See Appendix D.4 for precise details on the experiments considered here. The code is available as an example in Diffrax.

4 In passing, note that this is an Itˆ o SDE. As discussed in Section 4.1.1, it is no issue that we are about to learn it with a Stratonovich neural SDE.

Irregular sampling Both the Brownian motion and the Ornstein-Uhlenbeck example were irregularly sampled with missing data. The process was observed at each integer (in the time domain) with only 70% probability, and unobserved otherwise.

The continuous-time approach discussed in this chapter means that this irregularity requires no special treatment. Moreover the output of each model evolves in continuous time and may be observed at any location.

Other examples Other (real-world) time series problems may be considered. [Li+20a] give an example training latent SDEs to perform short-term forecasting on a 50-dimensional motion capture dataset. [Kid+21b] consider a dataset of 14.6 million observations of Google/Alphabet stock prices, and train an SDE-GAN to replicate the evolution of the midpoint and spread as it evolves over a minute. [Kid+21a] train both latent SDEs and SDE-GANs, and give an example modelling the air quality over Beijing.

## Comments

Several authors have independently introduced notions of neural SDEs. [Li+20a; Kid+21b] were the main works to derive the material presented here, whilst our presentation is derived from the follow-up [Kid+21a].

We have focused on using the Wasserstein distance or KL divergence to match model against data. In principle the classical calibration approach, using fixed statistics, may be employed in conjunction with neural vector fields, and this is now essentially the formulation of an MMD (Appendix A.5). Some care should be taken as to the choice of feature map. For example some authors have used only the mean and variance of the marginal distributions at each time t, and this fails to distinguish t ↦→ w (t) from t ↦→ √ tw. A good choice of feature map is the signature transform; for example this is done in [Kid+21b, Section 4] and [Kid+19, Section 4.1]. (There also exists a corresponding signature kernel [Sal+20;].) [Bri+20; Gie+20] consider variations on the formulation given here, but optimise a distance only between finite-dimensional marginal distributions, rather than optimising the continuous-time model. consider another variation on this formulation, by adding known structure to the discriminator, corresponding to prespecified payoff functions of interest. consider specifically Markov neural SDEs and optimise via maximum likelihood (more-or-less equivalent to optimising the KL criterion considered here) as part of a larger framework for market models; indeed many of the above references target financial applications.

Meanwhile [; ] obtain neural SDEs as a continuous limit of deep latent Gaussian models, and largely focus on the theoretical construction.

The connections between score-based generative modelling and neural SDEs as presented here has not yet been explored in detail. We recommend the first few pages of [Bor+21] for an introduction to score-based generative modelling. [; ] emphasise connections to continuous normalising flows. [Shi+21] give an application to molecular conformation, [Ho+21; ] give large-scale applications to image generation, and [Men+21] give an application to image editing. [; Kin+21; Son+21a] give variational/likelihood-based perspectives.

The mainstream deep learning literature frequently uses stochasticity as a regulariser. A neural SDE may likewise be treated as a regularised neural ODE or CDE [Liu+19 Hod+20]. This will also be discussed as part of our numerical treatment of differential equations in Section 5.4.1.3. give one application of neural SDEs not discussed here, by using the stochasticity as part of procedure to distinguish between epistemic and aleatoric uncertainty.

## Chapter 5

## Numerical Solutions of Neural Differential Equations

## Backpropagation through ODES

Training a neural differential equation usually means backpropagating through the differential equation solve. There are actually several ways to do this.

For clarity of exposition we begin by studying ODEs only, and will return to backpropagation through CDEs and SDEs in the next section.

We shall see three main ways of differentiating through an ODE.

- Discretise-then-optimise - memory inefficient, but accurate and fast; - Optimise-then-discretise - memory efficient, but approximate and a little slow; - Reversible ODE solvers - memory efficient and accurate, but a little slow.

Generally speaking discretise-then-optimise is the preferred approach. If this is not possible, typically due to memory constraints, then reversible ODE solvers are the next best option. Finally, if this is not suitable then optimise-then-discretise methods may be used, but these are typically the least-favoured approach.

All of these choices may typically be found in major differential equation software libraries (Section 5.6), so that the choice of backpropagation is usually an easy thing to change.

## Discretise-then-optimise

The first option is simply to backpropagate through the internal operations of the differential equation solver.

A differential equation solver internally performs the usual arithmetic operations of addition, multiplication, and so , each of which is differentiable. Given that a solve operation is a composition of differentiable operations, it is also differentiable.

This is known as 'discretise-then-optimise'. The derivatives are computed with respect to the discretised version of the differential equation that the solver computed, and not with respect to the idealised continuous-time equation.

## Advantages

Accuracy of gradients The computed gradients will be accurate for the discrete model that is actually being used. This is in contrast to some of the techniques we shall see later, which compute only approximate gradients.

Speed This is often the quickest way to backpropagate. One reason for this is that the full computation graph is known prior to performing the backpropagation, and so the underlying autodifferentiation library may better exploit parallelism.

Ease of implementation The implementation of discretise-then-optimise is generally straightforward: provided the differential equation solver is written in an autodifferentiable framework (such as PyTorch or JAX), then gradients may automatically be computed in the usual way for these frameworks.

## Disadvantages

Memory inefficiency This approach is memory-inefficient, as every internal operation of the solver must be recorded. If the memory cost of recording the operations of a single differential equation step is H, and recalling that T is the time horizon, then this approach consumes O ( HT ) memory.

This is in contrast to the techniques we shall see later, which reduce this to only O ( H ).

Remark 5.1. In some sense it's a little unfair to state that discretise-then-optimise is memory-inefficient. It's simply performing backpropagation as normal, as with any other neural network model, and we do not usually refer to those as memoryinefficient. It is simply that the other options we see later can reduce memory costs to essentially negligible amounts.

Difficulty of implementation In contrast to the 'ease of implementation' just discussed - if the differential equation solver is provided without having been written in an autodifferentiable framework, then this approach is essentially impossible to implement.

## Checkpointing

It is possible to finesse the problem of memory inefficiency through checkpointing. That is, record the value of the forward pass at certain points during the solve, and use these to reconstruct values during the backward pass. This is a general technique in deep learning. discuss this in the specific context of neural ODEs.

## Optimise-then-discretise

We now move on to the optimise-then-discretise approach. This instead works by differentiating the idealised continuous-time model. Doing so produces a backwardsin-time differential equation, which is then solved numerically. (References include [Pon+62 Che+18b] but this technique is widespread.)

Theorem 5.2. Let y 0 ∈ R d and θ ∈ R m. Let f θ: [0, T] × R d → R d be continuous in t, uniformly Lipschitz in y, and continuously differentiable in y. Let y: [0, T] → R d be the unique solution to Let L = L (y (T)) be some (for simplicity scalar) function of the terminal value y (T).

Then d L d y (t) = a y (t) and d L d θ = a θ, where a y: [0, T] → R d and a θ: [0, T] → R m solve the system of differential equations Remark 5.3. The vector-matrix products in equation (5.1) are, more specifically, vector-Jacobian products. These can be computed efficiently via autodifferentiation; see Appendix A.1.

Remark 5.4. Note that the a y ( t ) in the second equation (rather than a θ ( t ) ) is not a typographical error. The vector fields are independent of a θ. This may be exploited to speed up backpropagation through neural ODEs; this is a topic we shall return to in Section 5.4.2.1.

Equations (5.1) are known as the continuous adjoint equations.

These give a way to backpropagate through an ODE solve. Consider for example Figure 1.1. The gradient d L d y (T) is calculated by backpropagating through the softmax and affine layer in the usual way. Then the system of equation (5.1) is solved backwards in time from t = T to t = 0, to compute the parameter gradients d L d θ = a θ. 1 1 And had there also been any preceding operations, then backpropagation could then continue as usual from the computed d L d θ = a θ, d L d y 0 = a y.

Note that equation (5.1) requires knowing the solution y as an input. The usual approach is to find this by augmenting equations (5.1) with the original neural ODE solved backwards-in-time, starting from the numerical approximation to y (T) computed on the forward pass. In integral notation, this is This is known as the 'continuous adjoint method', or as the 'optimise-then-discretise' approach. The derivatives are calculated with respect to the idealised continuous-time model, and then the adjoint equations of (5.1) must themselves then be discretised.

Remark 5.5. The continuous adjoint method is also commonly referred to as simply 'the adjoint method', especially in the modern neural differential equation literature.

This is an unfortunate ambiguity of terminology. Across several prominent works, 'the adjoint method' has been used to refer to both the the discretise-then-optimise approach, and the optimise-then-discretise approach [Che+18b]. Moreover it has sometimes been used to refer to something else entirely: [, Definition 8.2] use it to refer to the inverse map of a numerical integration step, so that for example an implicit Euler step is the 'adjoint' of an explicit Euler step. 2 In this text we strive to be unambiguous by always making clear which adjoint method we are referring to, and would strongly discourage simply writing 'the adjoint method' without further qualification.

## Proof: 'continuous-time backpropagation'

Proving Theorem 5.2 is straightforward, and it is informative to compare this to backpropagation.

Consider two points s, t ∈ [0, T] with s < t, and consider solving the ODE from s to t, and then from t to the terminal time T. Then by the chain rule, For notation's sake let a (t) ⊤ = d L d y (t). Now the left hand side is independent of t, so differentiate with respect to t and set t = s: 2 This relationship between numerical integration steps is something we will actually need later. We refer to it as analytic reversibility, see Section 5.3.2.1.

This is now precisely the first adjoint equation of equation (5.1). The second adjoint equation can be derived by replacing y with the [ y, θ ] and f θ with [ f ·, 0] (that is to say treating the parameters θ as additional state, subject to zero vector field), and applying the same argument as before.

In this way we see that the adjoint equations are essentially 'continuous time backpropagation'. 3

## Advantages

Memory efficiency The continuous adjoint method has one clear advantage: memory efficiency. The forward computations for y need not be stored, as y is recomputed on the backward pass. So whilst differentiating through the internal operations has memory cost O ( HT ), the continuous adjoint method has a memory cost of only O ( H ), independent of the time horizon T.

Ease of implementation Another advantage is a practical one: the differential equation solver need not be written using autodifferentiation software, as required for the discretise-then-optimise approach. The differential equation solver can instead be treated as a black box; for example the solver may have been written for some other purpose as part of some other software package.

## Disadvantages

Computational cost The continuous adjoint method incurs additional computations necessary to recalculate y ( t ) on the backward pass; this implies a slightly slower and more computationally expensive procedure.

3 The mathematically precise reader may still be skeptical: we have not justified the change of limits, nor that the solution to the adjoint differential equation actually exists. See Appendix C.3.1 for these technical points.

Truncation errors The second disadvantage is numerical discretisation error: there will be a difference in the value computed for y ( t ) on the forward pass (computed starting from the initial condition y ), and the value computed for y ( t ) on the backward pass (computed starting from the numerical approximation to the terminal condition y ( T ) obtained on the forward pass).

Furthermore and in addition to the recomputation of y ( t ), the continuous adjoint equations for a y ( t ) and a θ ( t ) must themselves be solved numerically, and in doing so incur some additional numerical error.

The result is that gradients calculated via the continuous adjoint method will not be as accurate as those computed by backpropagating through the solver. (Which are the gold standard, corresponding to the model actually used.) This means that training may be slower, final model performance may be impacted, and in the worst case training may fail altogether. give a description of the possible failure modes of the continuous adjoint method, and perform a thorough empirical investigation comparing optimise-then-discretise against discretise-then-optimise, in favour the of the latter.

Example 5.6. Consider solving the system d y d t ( t ) = λy ( t ) with a numerical ODE solver, where y ( t ) ∈ R, y = y 0, and suppose λ < 0. Most differential equation solvers - those with a nontrivial region of stability [, Definition 2.1] - will handle this without trouble, as errors will decay exponentially. However when this is instead solved backwards-in-time from y ( T ), as in equation (5.2), then small errors are instead magnified exponentially. Moreover if λ > 0 then the same problem arises simply by interchanging the forward and backward passes in the above discussion.

However... Despite these dire warnings, continuous adjoint methods often (but not always) still work in practice, without needing any special care. The continuous adjoint method's suitability for any given problem is typically determined empirically - 'Does training seem to be working?' - and difficulties are frequently not a concern for practitioners.

## Interpolated adjoints

It is possible to finesse the problem of numerical errors in the continuous adjoint method.

Record the values of y ( t ) at specific locations on the forward pass (but not the internal operations of the solver used to obtain these y ( t )). Interpolate these recorded values to form an approximation to y ( t ) for all t. Then solve the continuous adjoint equations on the backward pass without additionally recomputing y ( t ), by instead using the interpolated approximation at whatever values of t are required during the backward solve.

Interpolated adjoints are actually the default backpropagation method used and [Rac+20b], for example. [Kim+21a] report finding that optimise-then-discretise adjoints failed on a stiff differential equation, but that both interpolated adjoints and discretise-then-optimise succeeded.

Stability and stiffness The use of interpolated adjoints implies that the differential equations solved - for y ( t ) forward in time, and a y ( t ) backward in time - now exhibit very similar behaviour, in particular with respect to stability and stiffness.

The local behaviour of a differential equation is understood through the eigenvalues of the Jacobian of the vector field 4 [, Section 112], [, Section I.13, Equation (13.2)].

For y (t), this is ∂f θ ∂y (t, y (t)). Meanwhile for a y (t) and a θ (t), this is The (local) behaviour of a θ (t) is trivial as the vector field has zero Jacobian. Meanwhile recalling that the equation for y (t) is solved forward-in-time and the equation for a y (t) is solved backward in time, we see that their Jacobians are identical.

Remark 5.7. Morally speaking this is expected: differentiation obtains a local linear approximation - that is to say a Jacobian - to a function. In this case the function is the overall act of solving an ODE. Meanwhile, the present analysis on local behaviour of a system is about constructing a local linear approximation - a Jacobian - to the vector field.

Note that this discussion is not true of standard optimise-then-discretise, for which the equation for y is solved in both the forward and backward directions, which exhibit opposite behaviour to each other.

Memory efficiency Recording the values of y ( t ) incurs a small memory cost, but not as much as recording every internal operation of the solver as in the discretisethen-optimise approach.

Choice of interpolation There are several sensible ways to record and interpolate y ( t ). use cubic Hermite interpolation whilst [Dau+20] use barycentric Lagrange interpolation, in both cases recording y ( t 1 ),..., y ( t n ) for some prespecified values t 1,..., t n.

4 An eigenvalue with positive real part describes a mode of a system that is 'locally expansive': points diverge from each other exponentially fast. Likewise negative real part describes a mode of a system that is 'locally contractive': points draw closer together exponentially fast. The imaginary part of an eigenvalue corresponds to the 'local rotation' of a system - see also Section 2.2.5.1.

## Checkpointing

Another way to finesse the problem of numerical errors is to use checkpointing as in Section 5.1.1.3. Each time we hit a checkpoint recorded on the forward pass, then we effectively reset any accumulated truncation error in y acquired on the backward pass. The trade-off being that this increases the memory usage from O ( H ) to O ( H + C ), where C is the number of checkpoints. (Although in practice this is often a relatively modest amount.)

## Reversible ODE solvers

Reversible ODE solvers offer a best-of-both-worlds approach compared to discretisethen-optimise and optimise-then-discretise. Reversible solvers offer both memory efficiency and accuracy of the computed gradients. Like optimise-then-discretise, they do require a small amount of extra computational work, to recompute the forward solution during backpropagation.

This is a topic still in its infancy. At present, two general reversible ODE solvers are known: the reversible Heun method, and the asynchronous leapfrog method (ALF). In addition, if the differential equation has the right structure, then symplectic solvers are typically also reversible.

The main drawback of reversible ODE solvers is that, at time of writing, all such solvers are low-order and exhibit poor stability properties. This is often not a problem if using pure-neural-network vector fields, but if the differential equation has known structure as in Section 2.2.2 then in principle this may result in a poor-quality solution.

We defer a full discussion of reversible solvers to sit alongside our discussion of other numerical solvers, in Section 5.3.2.

## Forward sensitivity

Whilst not technically back propagation, for completeness we mention that it is also possible to compute forward sensitivities of an ODE. (Or indeed a CDE or SDE.)

Once again this can be done either in discretise-then-optimise fashion or in optimisethen-discretise fashion. Discretise-then-optimise is accomplished by computing the forward sensitivity of the solver's computation graph.

Optimise-then-discretise is accomplished by simply differentiating equation (5.3) with respect to y 0 and θ, through which we obtain the following theorem.

Theorem 5.8. Let y 0 ∈ R d, θ ∈ R m, f θ: [0, T] × R d → R d be continuous in t, uniformly Lipschitz in y, and continuously differentiable in y. Let y: [0, T] → R d be the unique solution to Then d y (t) d y 0 = J y (t) and d y (t) d θ = J θ (t), where J y: [0, T] → R d × d and J θ: [0, T] → R d × m solve the system of differential equations The right hand side consists of Jacobian-vector products, which can be computed efficiently via autodifferentiation.

As usual, forward sensitivity is typically less efficient than reverse-mode autodifferentiation when considering machine learning problems with many parameters, so this approach is infrequently used. [Rac+20a] report finding it useful (only) on problems with very few ( < 100) parameters.

## Backpropagation through CDEs and SDEs

We now study backpropagation through differential equations more generally.

## Discretise-then-optimise

This is exactly the same as in the ODE case (Section 5.1.1) - simply differentiate through the internal operations of the controlled/stochastic differential equation solvers, typically by using solvers written in an autodifferentiable framework.

## Optimise-then-discretise for CDEs

There are two approaches to constructing continuous adjoint methods for CDEs. One is to reduce the CDE to an ODE as in Chapter 3, and then applying the continuous adjoint method for ODEs. For example this is what is done in the torchcde library.

Alternatively a backwards-in-time CDE may be constructed, and then numerically solved in whatever manner is desired, by reduction to an ODE or otherwise. The corresponding theorem is as follows.

Theorem 5.9. Let f: R d y → R d y × d x be both Lipschitz and continuously differentiable. Let x: [0, T] → R d x be continuous and of bounded variation. Let L: R d y → R be differentiable (and scalar just for simplicity). Let y 0 ∈ R d y and let y: [0, T] → R d y solve Then the adjoint process a (t) = d L (y (T)) d y (t) satisfies the backwards-in-time linear CDE starting from the terminal condition a (T) = d L (y (T)) d y (T), and where the right hand side denotes a vector-Jacobian product.

For simplicity we have avoided explicitly encoding the dependence on the parameterisation θ. This case may be recovered by replacing y, y 0, f θ with [ y, θ ], [ y 0, θ ], and f ( y, θ ) = [ f θ ( y ), 0].

After having solved equation (5.5) backward-in-time, a = d L ( y ( T )) d y are the desired gradients. As with the ODE case, y need not be recorded on the forward pass and may instead by recomputed on the backward pass, by stacking (5.4) and (5.5) together and solving as a joint system backwards-in-time.

See Appendix C.3.2 for a proof.

## Optimise-then-discretise for SDEs

(Informal) Theorem 5.10. Let µ: R × R d y → R d y and σ: R × R d y → R d y × d w be sufficiently regular. Let L: R d y → R be differentiable (and scalar just for simplicity). Let y 0 ∈ R d y and let y: [0, T] → R d y solve the Stratonovich SDE Then the adjoint process a (t) = d L (y (T)) d y (t) ∈ R d y is a (strong) solution to the backwardsin-time linear Stratonovich SDE using Einstein notation over the indices k 1, k 2, k 3, starting from the terminal condition a (T) = d L (y (T)) d y (T).

In particular w is the same Brownian motion as used in the forward pass.

As in the previous subsection, we have avoided explicitly encoding the dependence on the parameterisation θ, the desired gradients are the computed value a, and (5.6)-(5.7) may be stacked together to recover y ( t ) during the backpropagation. The right hand side of (5.7) consists of vector-Jacobian products, which may be calculated using autodifferentiation.

Note that the nondifferentiability of Brownian sample paths is unrelated to being able to compute derivatives d L ( y ( T )) d y. (It just means that derivatives like d y d t do not exist.)

See Appendix C.3.3 for a precise statement and a proof of Theorem 5.10 via rough path theory.

Rough path theory Theorem 5.10 is stated informally, because putting a precise meaning on the solution of (5.7) is a little outside the usual framework for SDEs. In particular (5.7) fails to exhibit measurability with respect to the natural filtration of w.

Rough path theory provides an elegant (and intuitive) solution, by allowing solutions to (5.6) and (5.7) to be defined pathwise. We simply fix a single sample of w, and evaluate the forward pass via (5.6) and the backward pass via (5.7) - in every respect just like the ODE case.

Remark 5.11. When backpropagating through an SDE solve via discretise-thenoptimise, then a Brownian motion is sampled on the forward pass of the numerical solver, its random samples are fixed as part of the computation graph, and then this computation graph is backpropagated. (Indeed just like any neural generative model; the noise sampled on the forward pass is the same noise on the backward pass.) As such 'discretise-then-optimise' is somehow intrinsically also pathwise.

Remark 5.12. Note the use of Stratonovich integration. This is naturally 'time reversible', unlike Itˆ o integration. If (5.6) was an Itˆ o SDE then the equivalent of (5.7) is substantially more thorny to work : it would be derived by applying the Itˆ o-Stratonovich correction term to convert (5.6) into a Stratonovich integral, applying Theorem 5.10, and then applying the Stratonovich-Itˆ o correction term to (5.7).

In a practical implementation then this double-correction implies substantial computational overhead, so it is preferable to use Stratonovich SDEs instead of Itˆ o SDEs when training via optimise-then-discretise methods.

## Reversible differential equation solvers

CDEs may be reduced to ODEs as discussed in Chapter 3, and correspondingly any reversible ODE solver may be applied. Meanwhile SDEs have a single known reversible solver, namely the reversible Heun method. See Section 5.3.2.

## Numerical solvers

## Off-the-shelf numerical solvers

Neural networks represent unstructured vector fields. This means that many of the more specialised differential equation solvers (developed for any particular equation) do not apply, and we must rely on 'general' solvers.

There is a rich literature of such numerical differential equation solvers. We will largely focus on explicit Runge-Kutta solvers, in particular for ODEs and CDEs, which are a popular family of numerical solvers. Other reasonable choices exist - for example linear multistep methods - but it is not our purpose to restate the numerical differential equation literature.

## General principles

There are some principles, specific to neural differential equations over differential equations in general, that help guide the choice of numerical solver.

Implicit solvers Implicit solvers, for example the implicit Euler method y j +1 = y j +∆ tf ( t j +1, y j +1 ), are rarely used.

They are computationally expensive: implicit solvers solve a linear or nonlinear system at every step, often through a fixed point iteration. Neural differential equations are a regime in which the vector field evaluations are expensive, and many vector field evaluations are already being made (over a batch, and over the course of training). Reducing computational cost is of substantial interest.

A major use-case for implicit solvers is solving stiff differential equations. 5 However stiffness is often not a problem for neural differential equations - if stiffness and an explicit solver produce a poor solution, then the loss between model and data may be large. As this is the criteria we explicitly train to avoid (to achieve a small loss), then the issue is avoided.

Remark 5.13. The above description is typical for 'machine learning neural differential equations' such as CNFs or neural CDEs - Section 2.2.3 and Chapter 3 respectively - but it is not a universal rule. For example if the vector field incorporates known structure (Section 2.2.2), or the data has multiple different timescales, then stiffness may be unavoidable and an implicit solver may become a reasonable choice. See for example [Kim+21a].

Adaptive versus fixed step solvers Both fixed step size and adaptive step size solvers are often reasonable choices for neural differential equations.

Given a time horizon T > 0, then fixed step size solvers choose some step locations 0 = t 0 < t 1 < · · · < t n = T in advance, usually with ∆ t = t j +1 -t j independent of j.

Adaptive step solvers vary the size of the next step t j +1 -t j, so that the (local) error made during the solve is approximately equal to some tolerance. For example embedded Runge-Kutta methods are of this type. This implies a variable computational cost, typically increasing over the course of training as model complexity increases [Che+18b, Figure 3(d)], [Fin+20a, Figure 3(c)]. 6 5 Somewhat tautologically, as stiff differential equations are broadly categorised as 'equations for which explicit solvers fail'.

6 Loosely speaking, neural networks tend to increase in complexity over the course of training [Kal+19], [, Section 5]. This manifests as the training and validation losses following the classic bias-variance curves during training.

Example 5.14. Consider solving a neural CDE with densely-sampled and slowlyvarying time series data as input. The slow variation of the input data means that processing every piece of it - as we may do with an RNN - is likely overkill. The adaptivity of a solver may automatically detect the slow timescale at which the differential equation is driven, and produce integration steps of the appropriate size, larger than the discretisation of the data.

Moreover, RNN training often breaks down as the length of a time series increases. If this length has been achieved by sampling the same signal more and more densely, then it is a bit perverse that this extra information should cause our model to fail to train. Philosophically speaking, it is reassuring to be able to overcome this issue using adaptive solvers.

Baked-in discretisations If only a single solver (in particular a low-order solver or a solver with a fixed step size) is used during model training, then this choice of discretisation may become an intrinsic part of the model. The neural vector fields will have been trained to work best at this discretisation, and may fail with other discretisations [Ott+21; Que+21].

For many applications this need not be a problem. In the introduction to this thesis (Section 1.2), 'inspiration for a discretised model' was described as a good use case for neural differential equations, and baking in the numerical discretisation is simply a subtle instance of this.

Step size and error tolerance Step size (for fixed step size solvers) or error tolerance (for adaptive step size solvers) will often be very large compared to that seen in the usual numerical differential equation literature. For example when using a neural SDE to generate a time series sampled at some points t 0 < · · · < t n, then we may elect to take a single numerical step over each interval [ t j, t j +1 ], even when t j +1 -t j is relatively large.

Once again this may be thought of as treating the continuous model as an ideal, and then deliberately fitting a discretised model. Large step sizes are often motivated by a desire to reduce computational cost, and thus training time.

Example 5.15. In this 'large step size regime', do note that taking smaller steps may produce slightly more expressive models. When looking to increase or decrease the modelling capacity of a neural differential equation, both step sizes and vector field complexity are options that may be adjusted.

As an example, consider fitting a neural SDE as in Chapter 4. If taking a single numerical step using the Euler-Maruyama method, then the conditional distribution of y ( t j +1 ) | y ( t j ) will only be Gaussian, which is relatively inexpressive.

Order of solver Low-order solvers are often reasonable choices, especially when explicitly baking in the discretisation in the large step size regime. For example Euler's method is first-order convergent; midpoint or Heun's method are second-order convergent.

If aiming to fit the idealised continuous model (for example when training via optimisethen-discretise), then higher-order solvers such as Dormand-Prince are often preferred. (At least when they are available, that is to say for ODEs and CDEs but not SDEs.)

## ODEs and CDEs

Bringing the above points together: when solving ODEs, or CDEs reduced to ODEs, then standard low-order solvers are the explicit Euler method (first order), the midpoint method (second order), or Heun's method (second order). Standard higherorder 7 methods are RK4 (fourth order), Dormand-Prince (fifth order), or Tsit5 (fifth order). offer an extensive comparison of explicit Runge-Kutta methods.

## SDEs

Standard choices of numerical solver for neural SDEs include the Euler-Maruyama method or Heun's method, for Itˆ o or Stratonovich SDEs respectively. 8 If the problem has commutative noise 9 then Milstein's method may be applied for both Itˆ o and Stratonovich SDEs.

## Reversible solvers

Weindicated in Sections 5.1 and 5.2 that besides discretise-then-optimise and optimisethen-discretise, there is a third option, namely reversible solvers.

Consider a differential equation solver iteratively computing ( y j, α j ) ↦→ ( y j +1, α j +1 ), where { y j } n j =0 is the numerical approximation to the solution of some differential equation - whether it be an ODE, CDE, or SDE - and α j denotes any extra state that the differential equation solver wishes to keep around.

By definition, ( y j +1, α j +1 ) may be computed from ( y j, α j ). We say that a solver is reversible if ( y j, α j ) may be computed from ( y j +1, α j +1 ). (Note that we have not yet made precise what is meant by 'computed'.)

8 Broadly speaking SDEs solvers are distinguished by whether they converge to the Itˆ o or Stratonovich solution.

9 This is a condition that is satisfied in several common special cases: if the Brownian motion is scalar valued; if the diffusion matrix is independent of the SDE solution; if the diffusion matrix is diagonal.

Algorithm 1: Backward pass through a reversible solver. t denotes time, y denotes the numerical solution, α denotes any additional state the solver keeps around, and ∆ t denotes a step size. x denotes a possible control input, which may be unused if the equation is an ODE and may be a Brownian motion if the equation is an SDE.

## vector-Jacobian product j j

Backpropagation with reversible solvers Backpropagation through a reversible solver is shown in Algorithm 1. The 'local' forward is needed to construct a computational graph, through which the vector-Jacobian product is calculated.

Computational cost Assuming that a forward and reverse step cost the same, the total computational cost of evaluating and backpropagating through a step of a reversible solver is three forward operations and one backward operation: one forward operation on the forward pass, two forward operations on the backward pass, and a single backward operation on the backward pass. As a combined forward/backward operation costs at most four forward operations [, Equation (4.21)], then the overall computational cost is approximately that of six forward operations.

This cost should be contrasted with discretise-then-optimise and optimise-then-discretise. Discretise-then-optimise involves simply a forward operation on the forward pass, and a backward operation on the backward pass, for an overall computational cost of approximately four forward operations. Optimise-then-discretise involves a forward operation on the forward pass, a single forward operation on the backward pass, and a single backward operation on the backward pass, for an overall computational cost of approximately five forward operations.

Remark 5.16. It is sometimes possible to elide the local forward in Algorithm 1. Given suitable structure in the solver, it may be possible to reuse the computational graph of the reverse step, and in doing so save the cost of a single forward operation. See for example the asynchronous leapfrog method coming up in Section 5.3.2.3.

Precise gradients As the same numerical solution { y j } n j =0 is recovered on both the forward and backward passes, the computed gradients are precisely the discretisethen-optimise gradients of the numerical discretisation of the forward pass.

As it is the discretised model that is fit to data, discretise-then-optimise represents the gold standard - the 'true' gradients of the model - so this property is desirable.

## Analytic and algebraic reversibility

We now make precise what it means to 'compute' ( y n, α n ) from ( y n +1, α n +1 ).

Analytic reversibility In some sense, essentially every solver is reversible. For example, the explicit Euler method may be reversed via the (backwards-in-time) implicit Euler method for those ∆ t small enough that the contraction mapping theorem ensures this nonlinear equation has a unique solution.

Unfortunately this requires solving a fixed-point iteration, and computing y j from y j +1 is both approximate and computationally expensive. We refer to reversibility of this type as analytic reversibility.

Example 5.17. For example [Beh+19] consider residual networks as the explicit Euler discretisation of a neural ODE, and exactly as above, use the implicit Euler method to invert the operation of each layer during backpropagation.

Algebraic reversibility Substantially more preferable is what we shall refer to as algebraic reversibility. These are solvers for which the solution of ( y j, α j ) may be written as a closed-form expression with respect to ( y j +1, α j +1 ). As such they are much more computationally reasonable.

We additionally refer to an algebraically reversible solver as symmetric if the reverse computation is of the same form as the forward step, simply performed backward-intime. (If '( y j +1, α j +1 ) = step( y j, α j, ∆ t )' implies '( y j, α j ) = step( y j +1, α j +1, -∆ t )'.)

## Reversible Heun method

The reversible Heun method, introduced in [Kid+21a], is a symmetric algebraically reversible ODE, CDE, or SDE solver. We will consider solving the SDE over [0, T], for which we will obtain the numerical solution { y j } n j =0. If solving an ODE simply set σ = 0. If solving a CDE then either reduce it to an ODE, or mutatis mutandis replace w with some control x.

To the best of this authors' knowledge, and at time of writing, this is the first and only general (non-symplectic) algebraically reversible SDE solver.

Algorithm 2: Forward pass for the reversible Heun method.

Algorithm 3: Reverse pass for the reversible Heun method.

Initialisation The solver tracks several extra pieces of state, ̂ y j, µ j, σ j, which are initialised at ̂ y 0 = y 0, µ 0 = µ (0, y 0 ), σ 0 = σ (0, y 0 ), and which have solution-like, drift-like and diffusion-like interpretations respectively. We additionally take w to be a single sample of Brownian motion, which must be the same on both the forward and backward passes.

Stepping The forward iteration then proceeds by iterating Algorithm 2. Note the similarity to Heun's method.

Convergence Convergence results are as follows.

Theorem 5.18. The reversible Heun method, when applied to ODEs, is a secondorder method.

Theorem 5.19. The reversible Heun method, when applied to SDEs, exhibits strong convergence of order 1 2. If the noise is additive then this increases to order 1.

A proof of the ODE case is given in Appendix C.4. A proof of the SDE case is given in [Kid+21a, Appendix D].

Stability One drawback of the reversible Heun method is its unimpressive stability properties.

Theorem 5.20. The region of stability for the reversible Heun method (for ODEs) is the complex interval [ -i, i ].

A proof is given in Appendix C.4.

Adaptive step sizing The step size ∆ t may either be fixed in advance (to make this a fixed step size solver) or it may be adapted over the course of the integration.

When solving ODEs, then the reversible Heun method may be treated in the same way as embedded Runge-Kutta method by returning the error estimate y error = ( µ j +1 -µ j )∆ t/ 2. This may now be used to adapt step sizing in the usual way (Section 5.4.2).

Reversibility For completeness, the reverse pass through the reversible Heun method is given in Algorithm 3. Note the similarity to the reversible Heun method, as the reversible Heun method is not just algebraically reversible but also symmetric.

Use cases If training via discretise-then-optimise is not an option, then the reversible Heun is an excellent choice of solver for any of neural ODEs, CDEs, or SDEs. If using pure-neural-network vector fields then its low order and lack of stability need not always be a concern, especially if the discretisation is baked-in as in Section 5.3.1.1.

It is only not recommended if solving neural differential equations with built-in structure as in Section 2.2.2.1, for which the low order and lack of stability may be concerns.

Computational efficiency Unlike the traditional Heun method, the reversible Heun method makes only a single evaluation per step. This can mean that it is more computationally efficient.

## Asynchronous leapfrog method

The asynchronous leapfrog method is a symmetric algebraically reversible ODE/CDE (but not SDE) solver, introduced and popularised by [Zhu+21]. We will consider solving the ODE over [0, T], for which we will obtain the numerical solution { y j } n j =0.

Initialisation The solver tracks a single extra piece of extra state v j in addition to the numerical solution y j. This extra state has a velocity-like interpretation and is initialised as v 0 = f ( y 0 ).

Stepping The stepping procedure is then given by iterating Algorithm 4. Note the similarity to the midpoint method.

Algorithm 4: Forward pass through the asynchronous leapfrog method.

Convergence The following convergence result may be shown.

Theorem 5.21. The asynchronous leapfrog method is a second-order method. Specifically, the local truncation error in y is O (∆ t 3 ), whilst the local truncation error in v is O (∆ t 2 ).

See [Zhu+21, Theorem 3.1].

Stability As with the reversible Heun method, one drawback of the asynchronous leapfrog method are its unimpressive stability properties.

Theorem 5.22. The region of stability for the asynchronous leapfrog method is the complex interval [ -i, i ].

A proof is given in [Zhu+21, Appendix A.4].

Adaptive step sizing If adaptively setting the step size, then the error estimate y error = ( v j +1 -v j ) / 2 may be used (in the same way as an embedded Runge-Kutta method).

Efficient reverse pass The general reversibility algorithm given in Algorithm 1 involves both Reverse and Forward operations. For the asynchronous leapfrog method, the extra Forward operation may be elided. This is accomplished by instead differentiating the Reverse pass, and appropriately adjusting the surrounding calculation.

This is because the quantity f ( ̂ t j, ̂ y j ) is computed during both Reverse and Forward. As f is generally both complicated and user-supplied, this is the piece we are most interested in autodifferentiating. We may calculate by hand the appropriate derivatives for the surrounding structure of the algorithm.

Algorithm 5: Efficient backward pass through the asynchronous leapfrog method.

In doing so, we obtain Algorithm 5.

Use cases The asynchronous leapfrog method is useful in essentially the same cases as the reversible Heun method, except that it applies only for ODEs.

Remark 5.23. The asynchronous leapfrog method does not seem to extend to SDEs. There is a clearly analogous procedure, tracking a diffusion-like quantity in addition to a drift-like quantity. However it does not seem obviously possible to demonstrate theoretical convergence of this solver, and neural SDEs trained using it perform relatively poorly empirically.

## Symplectic solvers

Many pre-existing symplectic solvers are already algebraically reversible. There are a great many symplectic solvers; we highlight only a few interesting ones here.

## Semi-implicit Euler method Given a pair of differential equations

the semi-implicit Euler method is defined by A common special case is f (t, v) = v so that v is the velocity of y, and y is understood as the solution of a second-order system.

This is notable for its popularity in deep learning papers; it is the solver used with the rotational vector fields and momentum residual networks of Section 2.2.5.

## Leapfrog/midpoint Consider the integrator

over [0, T ], where { y j } n j =0 is the numerical solution.

We refer to this as the 'leapfrog/midpoint integrator' in accordance with the title of, but other texts will call it simply 'leapfrog' (in ambiguity with the integrator for second order systems of the same name), or the 'explicit midpoint method' (in ambiguity with the Runge-Kutta method of the same name).

This is both algebraically reversible and symmetric, and is applicable to general firstorder systems.

Remark 5.24. As a linear multi-step method it does not admit an immediate way to adapt step sizes during integration, nor does it have very good stability properties. Fixing the first problem produces the asynchronous leapfrog integrator of Section 5.3.2.3.

## Solving vector fields with jumps

One common scenario is that the vector field of a neural ODE has a piecewise structure with respect to time. That is we are solving for solving where For example this occurs when solving a stack of neural ODEs as in Section 2.3.2.1, or when solving a neural CDE, reduced to an ODE, using linear or rectilinear interpolation (Section 3.5).

In this case we have two options: make n separate calls to an ODE solver, over each [ t j, t j +1 ], or to make a single call to an ODE solver, over the whole [ t 0, t n ].

Both options are fine, but in some cases each requires a small amount of caution.

Separate calls If making n separate calls to an ODE solver, and training the neural ODE either via optimise-then-discretise or via reversible ODE solvers (Section 5.3.2), then practically speaking the memory cost will be n times larger than if we had made a single ODE solve: each ODE solve will store y ( t j +1 ) at the end of its solve, for the sake of the later backpropagation through the ODE solve.

This may be desirable - essentially implementing checkpointing as in Section 5.1.2.5. Alternatively it may be undesirable due to the increased memory cost.

Single call If making a single call to the ODE solver, and using an adaptive step size ODE solver, then the solver should be informed about the location of the jumps. Otherwise, the error control in the step size controller will detect a large error every time a threshold is crossed, slow down to resolve it, and then speed back up again.

It is substantially more efficient to simply step directly to the discontinuity; failing to do so can result in an order-of-magnitude slow-down. The software libraries we recommend in Section 5.6 support this as an option.

## Hypersolvers

Known versus unknown structure When motivating the use of standard offthe-shelf solvers like Euler or Dormand-Prince, we wrote: Neural networks represent unstructured vector fields. This means that many of the more specialised differential equation solvers (developed for any particular equation) do not apply, and we must rely on 'general' solvers.

This was, in fact, a white lie.

Neural differential equations do exhibit structure - they exhibit whatever the structure of the problem being modelled is. The problem is simply that this structure is specified by a black-box neural vector field, and is not understood.

A running theme throughout machine learning, and thus also this work, has been that we may substitute theoretical understanding with data - and that given sufficient data, we may close the gap between a theoretical model and the behaviour observed in practice. We may apply the same principle here.

Learnt error corrections For q ∈ N, consider some q -th order ODE solver 10 with update rule ψ. That is to say, for some time points { t j } n j =0 (for simplicity with constant step size ∆ t = t j +1 -t j), the numerical solution y j ≈ y (t j) is obtained by iterating For example ψ (t, y) = f θ (t, y) for Euler's method.

As a q -th order solver, the local truncation error is of order q +1: A hypersolver [Pol+20] is now defined by a learnt correction with g ω: R × R d × R → R d some neural network depending on learnt parameters ω.

Example 5.25. For example, recall Heun's method Then HyperHeun is defined by (This implicitly features a O (∆ t 2) term due to the ̂ y j +1.)

Training Training is performed by assuming access to the true solution of the neural ODE. In practice this may be approximately obtained by using a traditional numerical solver with high order, small step sizes, or tight error tolerances.

Then a hypersolver may then trained by minimising either 10 We will treat only ODEs; the extensions to CDEs and SDEs are natural but so far unexplored. where { y j } n j =1 is the numerical solution obtained by iterating (5.8). (The former is analogous to training an RNN using teacher forcing; the latter to training an RNN without it.)

Applications The primary interest in hypersolvers is to obtain solutions that are both fast and accurate. As speed is of interest, then typically the base update rule ψ is very simple (Euler or Heun), whilst g ω may only be a single-layer MLP. This is often sufficient to obtain excellent results. For example [Pol+20] report striking results in which 80 Dormand-Prince steps may be replaced by only 2 HyperHeun steps, without degrading accuracy (in that example, on a continuous normalising flow).

However, hypersolvers are generally only useful for speeding up inference, not training. The neural ODE changes during training, and so (5.9)-(5.10) become a moving target.

There is related work on training neural networks as differential equation solvers. This is a related but distinct notion to training a neural network as the solution of the differential equation itself [ Fan+19].

## Tips and tricks

## Regularisation

## Weight decay

Adding weight decay to the parameters of a neural vector field may help to improve model performance, just as in traditional deep learning.

For many neural networks, the scale of its output is roughly proportional to the scale of its weights. That is to say, ‖ f θ ‖ / ‖ θ ‖ may be approximately constant over different values of θ. As such an additional implication of weight decay is that the vector field may be closer to zero, and thus numerically easier to integrate.

## Temporal regularisation

For applications of neural differential equations to 'non time series' problems, one form of regularisation is to select the region of integration randomly. For example when training a continuous normalising flow, then instead of taking a fixed a region of integration [τ, T], the endpoints τ, T may be sampled from some distribution; perhaps τ = 0 remains fixed whilst T ∼ Uniform[0. 9, 1. 1]. This is computationally cheap whilst encouraging models which are robust to small perturbations [Gho+20].

## Additive noise

Mainstream deep learning often uses stochasticity as a regulariser, such as dropout. Correspondingly, and for neural ODEs and neural CDEs specifically, then including some small additive noise after each step (so that the model becomes an SDE) is another computationally cheap option that encourages more robust models [; ].

In this case the added noise should be fixed. If it is learnt then the training process will shrink it to zero and no regularisation will be applied.

## Regularising higher-order derivatives

Consider the usual set-up for a neural ODE in which y solves d y d t ( t ) = f θ ( t, y ( t )).

Let q ∈ N and consider some q -th order numerical ODE solver. Over any given numerical step [ t j, t j +1 ], such solvers operate by locally approximating the solution y by some q -th order polynomial. Correspondingly the error made over some step is determined by the q +1-th total derivative d q +1 d t q +1 ( y ( t )) = d q d t q ( f θ ( t, y ( t ))).

We may seek to minimise numerical errors, and promote easy-to-integrate dynamics, by regularising This was investigated in [Kel+21].

(As this is only a regularisation term - this will be made small, not precisely zero then we may also consider regularising lower-order derivatives instead.)

Taylor-mode autodifferentiation In principle evaluating (5.11) may be done via autodifferentiation, although a little care is needed to get the correct derivatives: each derivative on the right hand side involves taking a derivative of y with respect to t, so that d y d t = f θ will start to appear multiple times [, Section 310].

However doing so via na¨ ıve autodifferentiation will be unnecessarily expensive. A Jacobian-vector product typically costs 2. 5 times the cost of the corresponding forward evaluation, so nesting K such evaluations will result in a 2. 5 K = O (exp( K )) cost. That this is a higher-order derivative implies certain structure that may be exploited to reduce the cost to only O ( K 2 ); see [Kel+21, Appendix A] or [, Chapter 13].

Continuous normalising flows A special case arises - see [Fin+20a] - when regularising low-order derivatives of continuous normalising flows (Section 2.2.3). When evaluating (5.11) with q = 1, then and so we may accomplish similar goals by regularising Because this is a CNF, we are already computing derivatives of f. This means that the Jacobian (left) expression may be computed very cheaply, without additional calls to autodifferentiation. (This is also the reason that the ∂f θ ∂t term is neglected, as computing that would require an additional autodifferentiation operation.)

If using exact Jacobian computations then the Jacobian expression may be evaluated directly using the already-computed Jacobian. If using Hutchinson's trace estimator, then letting A = ∂f θ ∂y ( t, y ( t )) the following expression applies:

## Exploiting the structure of adaptive step size controllers

For simplicity we will now focus on explicit embedded Runge-Kutta methods as a class of numerical ODE solvers. As per Section 5.3.1.2 these include many of the typical solvers used for neural differential equations, like Heun's method or Dormand-Prince.

Remark 5.26. The discussions of this section will often actually apply to other solvers and differential equation types too. For example both the reversible Heun method and asynchronous leapfrog method (Section 5.3.2) are very similar to RungeKutta methods.

Such solvers may be decomposed into two main components: an update rule (defined by a Butcher tableau ), and a step size controller for updating the step size. (Which may simply be to use a constant step size.)

The update rule is typically the better-advertised component of a solver. Here we will instead focus on how the step size controller may be used or modified to our advantage.

Webegin with a brief exposition of how step sizes are adjusted; see, [, Section II.4], [, Section 271] for reference.

Set-up We begin with the usual setup. Let y 0 ∈ R d, θ ∈ R m. Let f θ: [0, T] × R d → R d be uniformly Lipschitz and continuously differentiable, and let y: [0, T] → R d solve Let y j ≈ y (t j) be some numerical approximation to the solution of (5.12). Over a step size t j +1 -t j, then a numerical ODE solver may propose some y candidate j +1 ≈ y (t j +1), along with a local error estimate y error j +1 ∈ R d of the numerical error made in each channel during that step.

Scale and error ratios Given some prespecified absolute tolerance ATOL (for example 10 -6) and relative tolerance RTOL (for example 10 -3) and (semi)norm ‖ · ‖: R d → [0, ∞) (for example ‖ y ‖ = √ 1 d ∑ d k =1 y 2 k the RMS norm), then an estimate of the scale of the equation is given by with an elementwise maximum. The error ratio r is then computed as with an elementwise division.

Note the dependence on the choice of norm ‖ · ‖. In particular this determines the relative importance of each channel.

Accepting/rejecting steps If r ≤ 1 then the error is deemed acceptable, the step is accepted and y j +1 = y candidate j +1 is taken. If r > 1 then the error is deemed too large, the step is rejected and the procedure is repeated with a smaller step size.

Step size changes Regardless of whether the step is accepted or rejected, then the next step size ( t j +2 -t j +1 or t j +1 -t j if the step was accepted or rejected respectively) is selected based on the size of SCALE.

For example the step size may be updated by a multiplicative factor where ORDER refers to the order of the solver (2 for Heun, 5 for Dormand-Prince and so on), and SAFETY, IFACTOR, DFACTOR are hyperparameters. Typical values would be SAFETY = 0. 9, IFACTOR = 10, DFACTOR = 0. 2.

This is the 'textbook' step size controller, which is memoryless (each multiplicative factor is dependent only on the previous step). Other step size controllers, often with memory, may also be considered, [, Section 271].

This will be all the necessary background material we need on step size controllers.

## Not-an-ODE and adjoint seminorms

Consider specifically when training neural ODEs via optimise-then-discretise, in which a backward-in-time adjoint ODE is constructed. The particular structure of the continuous adjoint equations actually means that the usual choice of norm for computing the error ratio, such as the RMS norm, is unnecessarily stringent: steps are unnecessarily rejected, and step sizes are too small.

By replacing it with a more appropriate (semi)norm, then on the backward pass: 1. Fewer steps are rejected overall; 2. Fewer steps are accepted overall; 3. Fewer steps are rejected, as a proportion of the overall number of steps.

That fewer steps are both accepted and rejected corresponds to generally larger step sizes being used. Moreover, this occurs without adversely impacting model performance.

Continuous adjoint equations For convenience we begin by recalling the set-up for backpropagating via optimise-then-discretise.

Let L = L (y (T)) be some (for simplicity scalar) function of the terminal value y (T), so that the continuous adjoint equations (Theorem 5.2) correspond to a y: [0, T] → R d and a θ: [0, T] → R m solving which are solved backward-in-time from a terminal condition.

Integral, not an ODE The continuous adjoint equations exhibit certain structure: their vector fields are independent of a θ, and correspondingly the second equation in (5.14) is merely an integral: not an ODE. (See also Remark 5.4.)

As such, whilst it is convenient to evaluate the a θ component of (5.14) as part of the backward-in-time ODE solve, the ODE solver makes the false assumption that small errors in a θ may propagate to create larger errors later.

Adjoint seminorms When numerically solving (5.14) backward-in-time, the easy solution is to pick a choice of ‖ · ‖ that scales down the influence of the a θ channels. A simple such choice is to take ‖ · ‖ as a seminorm, such as ‖ ( y, a y, a θ ) ‖ = √ 1 2 d ∑ d k =1 ( y 2 k + a 2 y,k ) the RMS norm over the y and a y components, and independent of the a θ component. (Recall that the y component is often solved backward-in-time alongside (5.14).)

Does this reduce the accuracy of the parameter gradients? One obvious concern is that we are ultimately interested in the parameter gradients a θ, in order to train a model. In this respect, this approach seems counter-intuitive. Empirically this does not appear to negatively affecting training, however - we explain this by noting that as the y and a y channels truly are ODEs, they are likely to be the dominant source of error overall.

Results This can dramatically reduce the computational cost of training. reduce the cost of the backward pass through neural CDEs and Hamiltonian neural networks (Chapter 3, Section 2.2.2) by 40%-62%, and (less dramatically) through CNFs (Section 2.2.3) by 5%.

Quadrature Other methods for evaluating a θ may also be admitted - for example, whilst it is less convenient than simply using an already-existing ODE solver, a θ could also be evaluated using a quadrature rule [Hin+21, Section 2.5].

## Non-backpropagation through adaptive step size controllers

Consider backpropagation via discretise-then-optimise. Technically speaking, we should expect to backpropagate through the entire computational graph, including through updates to step sizes, and through rejected steps.

Even rejected steps will in principle have a small effect on the backpropagated gradients. Every step (accepted or rejected) is used as an input to SCALE, which is used to compute the multiplicative factor by which a step size is updated (equation (5.13)), which determines the timestep values { t j } n j =1, which in general may be used as an input to the neural vector field f θ.

In practice this is not always desirable. Backpropagating through rejected steps implies additional computational work [Zhu+20b], and anecdotally we have observed that backpropagating through equation (5.13) will sometimes introduce gradient pathologies that hinder training.

For this reason it is very common not to backpropagate through step size selection when differentiating the computational graph we treat the result of equation (5.13) as a constant. 11 Neither the torchdiffeq nor Diffrax software libraries backpropagate through step size selection, for example [; ].

11 In PyTorch this means applying detach to the output of equation (5.13); in JAX or TensorFlow this means applying stop gradient.

## Regularising error estimates

[Pal+21] seek to encourage easy-to-integrate dynamics by adding as a regularisation term when solving a neural ODE. ([Pal+21] also consider a variant of this, by regularising a term used for detecting stiffness of the differential equation.)

This is computationally almost free, as all y error j will already have been computed.

This technique relies on optimising the neural ODE via discretise-then-optimise (or with a bit of work, a reversible solver). If using optimise-then-discretise then the computational graph for computing y error j is not saved for later backpropagation.

## Numerical simulation of Brownian motion

Numerically solving an SDE requires sampling a Brownian motion w: [0, T ] → R d w.

Brownian bridges Mathematically, sampling Brownian motion is straightforward. A fixed-step numerical solver may simply sample independent Gaussian random variables during its time stepping. An adaptive solver (which may reject steps) may use L´ evy's Brownian bridge formula to generate the appropriate correlations: for any s < t < u, and this quantity is (conditionally) independent of w (v) for v < s or v > u.

Brownian reconstruction However, there are computational difficulties. The main one is that during backpropagation, the same Brownian sample as the forward pass must be used, and if using optimise-then-discretise (Section 5.2.3) may potentially be queried at locations other than were sampled on the forward pass.

In addition, we need to efficiently track the value of the Brownian motion at each end of any interval we will later need to condition . (To apply the Brownian bridge formula, for example when rejecting steps.)

Brownian sampling We will now see three approaches to handling this: the Brownian Path, the Virtual Brownian Tree, and the Brownian Interval. 12 The Brownian Path and Virtual Brownian Tree are included as 'warm-ups' for pedagogical purposes; in practice the Brownian Interval will usually be the go-to choice.

12 These choices of terminology are not completely standard; we adopt the names used in the torchsde library.

## Brownian Path

One approach is simply to store every sample, and apply equation (5.15) when appropriate. There are some questions about the optimal data structure to store these values , for efficient querying later - in practice the tree-like structure we will later introduce for the Brownian Interval is often a good choice - but otherwise there is little to discuss here.

This approach is simple and usually gets the job done. During an SDE solve, querying takes O time (assuming a suitable data structure, see the Brownian Interval later). The main downside is the consumption of O ( d w T ) memory.

## Virtual Brownian Tree

The memory cost of the previous approach can sometimes be large enough to be a concern. This is especially true when taking many small steps to solve the SDE, or when using the continuous adjoint method or reversible SDE solvers (Sections 5.2.3 and 5.3.2) for which the Brownian motion samples represent a higher proportion of the overall memory usage.

As such, [Li+20a], motivated, introduce the 'Virtual Brownian Tree'.

Splittable PRNGs The first key ingredient is 'splittable' pseudo-random number generator (PRNG) seeds [Sal+11; ].

Given an m -bit random seed ρ ∈ { 0, 1 } m, splitting is an operation that produces some n new m -bit random seeds ρ 1,..., ρ n ∈ { 0, 1 } m, as a deterministic function of ρ, for which ρ, ρ 1,..., ρ n produce statistically independent streams of random numbers when used as the seed for a PRNG.

Given any rooted tree, we can associate a random seed with every node in the tree in the following way.

Let (V, E, ∗) be a rooted tree, where V denotes some vertex set, denotes some edge set (connected and without cycles), and ∗ ∈ V denotes the root. For any x ∈ V, let Γ(x) = { y ∈ V | { x, y } ∈ E } denote the set of vertices adjacent to x.

Let ρ ∈ { 0, 1 } m be an m -bit seed, which we associate with the root ∗. Split ρ into ρ 1,..., ρ | Γ( ∗ ) | random seeds and pair each one with a corresponding element v i ∈ Γ( ∗ ). Recursively split each ρ i and pair the resulting seeds with the elements of Γ( v i ), and so , recursing this procedure throughout the tree.

By fixing a rooted tree ( V, E, ∗ ) and a root seed ρ, we may deterministically create a PRNG at every node in the tree. Provided we remember only the tree structure and the root seed s, we can later rematerialise every PRNG sequence, for every node of the tree, without holding the samples in memory.

Example 5.27. A function call graph is an example of such a rooted tree. We begin by calling a function. This in turn may call other functions, which in turn may call other functions, and so on - which we consider a tree, rather than a DAG, by treating multiple calls to the same function separately. Splittable PRNGs may be used to deterministically generate pseudorandomness at any point in this call graph, for example when writing pure functions. This is actually the procedure used throughout the JAX software library [Bra+18] whenever generating random samples is required.

Generating Brownian samples Let ε > 0 be some fixed (small) tolerance. Consider the collection of dyadic points V = { Tj 2 -k ∣ ∣ j, k ∈ N, T 2 -k +1 > ε }. These form a tree-like structure: each Tj 2 -k has T ⌈ j/ 2 ⌉ 2 -k +1 as its parent.

By recording only some root-level seed σ ∈ { 0, 1 } m, and associating seeds with the elements of this tree as in the previous heading, then a Brownian sample w ( v ) is completely determined for all v ∈ V: see Algorithm 6.

For x ∈ [0, T ] let [ x ] V denote the member of V closest to x. To approximately sample a Brownian increment w ( t ) -w ( s ) (when an SDE solver steps from s to t ), we first discretise s and t to [ s ] V and [ t ] V, sample w ([ s ] V ) and w ([ t ] V ) as in Algorithm 6, and then return w ([ t ] V ) -w ([ s ] V ). The main downsides are that this takes O (log(1 /ε )) time, and produces only approximate samples. However, it has the advantage that this requires only O memory.

Whilst sampling Brownian motion is easy, the key point of this construction is how it additionally allows for reconstructing the same Brownian motion sample, without holding the individual samples in memory.

## Brownian Interval

We are now ready to present the Brownian Interval, which improves upon the Brownian Tree with exact sampling and O query times.

## Overview

Sampling intervals Let w ( s, t ) denote w ( t ) -w ( s ) ∈ R w.

We begin by shifting from a point-evaluation approach, in which each query to the Brownian object produces some w ( t ), to an interval-evaluation approach, in which each query to the Brownian object generates some w ( s, t ).

Rewriting the Brownian bridge equation (5.15) gives Algorithm 6: Sampling the Virtual Brownian Tree. split seed denotes splitting a seed into two, and bridge denotes the Brownian bridge of equation (5.15).

Input: Time horizon T > 0, sample time τ ∈ [0, T], seed ρ, error tolerance ε > 0 The complement w (t, u) | w (s, u) is calculated as w (t, u) | w (s, u) = w (s, u) -w (s, t) | w (s, u).

Binary tree of (interval, seed) pairs Similar to the binary tree of (point, seed) pairs used in the Brownian Tree, we will now have a binary tree of (interval, seed) pairs. Each parent interval will be the disjoint union of its child intervals.

The tree starts as a stump consisting of the global interval [0, T ] and an m -bit random seed ρ. New leaf nodes are created as queries over intervals are made. For example, making a first query at [ s, t ] ⊆ [0, T ] (an operation that will return w ( s, t )) produces the binary tree shown in Figure 5.1a; making a subsequent query at [ u, v ] with u < s < v < t produces Figure 5.1b. Using a splittable PRNG as in Section 5.5.2, each child node has a random seed deterministically produced from the seed of its parent. Unlike the Virtual Brownian Tree, which has a fixed (dyadic) tree construction, the tree used in the Brownian interval is query-dependent.

Figure 5.1: Binary tree of intervals. Only the intervals, without the corresponding seeds, are shown.

The tree thus completely encodes the conditional statistics of a Brownian motion, conditional on all previous queries: w ( s, t ), w ( t, u ) are completely specified by s, t, u, w ( s, u ), equation (5.16), and the random seed associated with [ s, u ].

Generating Brownian samples In principle we may now calculate w ( s, t ) for any s < t. The query over [ s, t ] adds extra nodes to the tree (if necessary; [ s, t ] may have been queried before), so that the conditional statistics of the query, with respect to all previous queries, are captured. As in Figure 5.1b, this may decompose [ s, t ] into some disjoint union of subintervals. We then calculate w ( s, t ) by applying equation (5.16) to each subinterval.

This calculation does require the Brownian increment w ( s, u ) over the parent interval [ s, u ]. In principle this is calculated recursively in the same way, working our way up the tree. (As with the Virtual Brownian Tree.) However, this may be improved by adding a least recently used (LRU) cache to the computed increments w ( s, t ).

Queries are exact because the tree aligns with the query points. Queries are fast because of the LRU cache: in SDE solvers, subsequent queries are likely to be close to (and thus conditional on) previous queries. The average-case (modal) time complexity is thus O. Even in the event of cache misses all the way up the tree, the worst-case time complexity will only be O (log(1 /h )) in the average step size h of the SDE solver. The (GPU) memory cost is essentially the size of the LRU cache, which is constant and thus O.

The trade-off here is that we must store the tree structure itself, which grows each time a query is made. For an SDE solve on [0, T ] then this will consume O ( T ) CPU memory. In practice however this is unlikely to be a limitation: GPU memory is usually the limiting factor, in comparison to which CPU memory is essentially infinite.

## Algorithmic definitions and further discussion

Precise algorithmic definitions and (substantial) further discussion on the Brownian Interval is deferred to Appendix C.5 to avoid breaking the flow of the presentation.

Remark 5.28. To what extent may either the point-based approach of the Virtual Brownian Tree, or the interval-based approach of the Brownian Interval, be interchanged?

An interval-based approach to the Virtual Brownian Tree is possible, but would likely be inefficient. For small approximation tolerance ε and step sizes possibly much larger than ε, then a query for some interval [ s, t ] would require logarithmically many dyadic intervals (each of length Tj 2 -k for some j, k ), to construct [[ s ] V, [ t ] V ]. This is as opposed to just making two point-based queries. (The Brownian Interval largely avoids this issue with its query-dependent trees.)

A point-based approach to the Brownian Interval is possible (despite the name), but the interval-based approach has several upsides.

- Elegance. We directly query for the sample w (s, t) actually used in the SDE solver. - Efficiency. Making only a single query for w (s, t) as opposed to making two queries for w (s) and w (t). - L´ evy area approximation. Some numerical SDE solvers sample additional randomness beyond just the point evaluations w (t): typically these samples are of higher-order integrals ∫ t s w k 1 (u) d w k 2 (u), computed over intervals [s, t]. For example stochastic Runge-Kutta methods may require space-time L´ evy area samples, and the log-ODE method for SDEs 13 uses full L´ evy area samples. As they are defined over intervals [s, t], these quantities are intrinsically interval-based values, requiring an interval-based Brownian motion construction. The details of this are a topic beyond our scope here; James Foster's doctoral thesis introduce the requisite formulas analogous to (5.16), and the necessary extensions to the Brownian Interval are implemented in torchsde.

## Software

Software packages for the numerical solving and training of neural differential equations are now relatively standardised. They handle most of the details described over the course of this chapter, and correspondingly the user is free to focus on the modelling details that have been the focus on the other chapters in this thesis.

At time of writing, there are a selection of options.

- In the JAX ecosystem [Bra+18] there is Diffrax.

13 This is the same log-ODE method as seen in Appendix B. The additional L´ evy area terms used here correspond to the logsignature terms used there.

- In the PyTorch ecosystem [Pas+19] there is the torchdiffeq, torchcde, and torchsde family of libraries. (And additionally torchdyn as a higher-level wrapper providing some common models.) - In the Julia [Bez+17] ecosystem there is DifferentialEquations.jl.

Every package we recommend is open source, offers a stable API, is relatively featurecomplete, and comes with comprehensive documentation and examples - including code examples for many of the techniques discussed in this thesis.

Whilst exact functionality differs slightly by package, one can expect most of: 1. Explicit and implicit solvers; 2. Fixed and adaptive step size solvers; 3. Differentiation via both optimise-then-discretise and discretise-then-optimise; 4. Reversible differential equation solvers; 7. Handling of jumps in the vector field; 8. For neural CDEs: all interpolation schemes discussed here; 9. For neural RDEs: logsignature pre-processing as in Appendix B; 10. Solving of both Itˆ o and Stratonovich SDEs; 11. Solving SDEs with varying noise types (scalar, additive, diagonal, general); 12. Brownian Interval simulation as in Section 5.5; 13. Levy area approximation;

## GPU support

Any choice amongst these libraries is a reasonable one.

Remark 5.29. If the reader is free to choose, then we would recommend Diffrax. It is the newest of these libraries, and is quite exciting on a technical level, as it solves ODEs, CDEs, and SDEs in a unified way by internally lowering all of them to rough differential equations. In addition if working with irregular time series, then it is the only one amongst these libraries to offer the ability to batch over different regions of integration. We must admit to some bias - Diffrax is the author's own project, created whilst writing this thesis.

## Comments

The choice of discretise-then-optimise versus optimise-then-discretise backpropagation is a classical one in the context of differential equations. is the canonical reference on this topic in the context of neural ODEs. See also [Rac+20a; ] for related comparisons.

Reversible differential equation solvers, as applied to backpropagation, are quite a new topic. [; Zhu+21] introduce a reversible ODE solver, whilst [Kid+21a] introduce the first reversible SDE solver.

The broader comparison of discretise-then-optimise against optimise-then-discretise against reversible differential equation solvers is new here. (And mistakes on this topic are frequent in the literature; we have come across several erroneous statements about favouring optimise-then-discretise over discretise-then-optimise, in contexts where the opposite is true.)

The proof of optimise-then-discretise for ODEs (relegated to Appendix C.3.1), and its sketchproof (Section 5.1.2.1), are new here. To the best of our knowledge the existing literature has relied on only more complicated proofs.

The proofs of optimise-then-discretise for CDEs and SDEs (relegated to Appendices C.3.2 and C.3.3) are new here. Once again to the best of our knowledge, the existing literature has relied on (substantially) more complicated proofs. A proof of optimisethen-discretise for SDEs appeared in [Li+20a]. A proof of optimise-then-discretise for CDEs (along with a rough path theory proof of optimise-then-discretise for SDEs) first appeared in [Kid+20b], although this was never published.

The discussion on the choice of numerical solver is part of the folklore of neural differential equations; our presentation here is based on our own anecdotal experience and our conversations with others.

Baked-in discretisations (both that they occur and that they are acceptable) are again part of the folklore, although they have been explicitly studied in [Ott+21; Que+21].

The terminology of analytic and algebraic reversibility is new here. Some existing texts do refer to just 'reversible solvers', usually in the context of symplectic solvers.

The more efficient backward step for the asynchronous leapfrog method (Algorithm 5) is new here. ([Zhu+21] used the more general, less efficient, Algorithm 1). It is actually also possible to construct a more efficient backward step through the reversible Heun method as well, so as to elide the local forward operation. It is however more finicky to do so - the local backward needs to occur on the reverse pass of the previous step - so for simplicity we omit this here.

On the stability of the asynchronous leapfrog method: [Zhu+21] do additionally introduce a 'damped asynchronous leapfrog method' with nontrivial region of stability. In practice the region of stability remains very small, and one of the main advantages of reversible solvers is the ability to use them with very large step sizes, 14 so the benefit of this is not clear. We note that [Zhu+21] mangle terminology slightly by referring to a 'region of A-stability' when merely 'region of stability' or 'region of absolute stability' would be correct. ('A-stability' is a property of the region of stability itself.)

The 'not-an-ODE'/'adjoint seminorm' trick for improving backpropagation speed through neural ODEs may also be applied to forward sensitivities [Hin+21, Section 5.5].

The comparison of different software libraries is new here. In fact, the Diffrax software library was written by the author for the express purpose of writing this thesis (or perhaps to procrastinate from writing this thesis). Realistically this has been a fast-moving space, and we would not be surprised if the section on software rapidly becomes outdated.

14 Whilst still getting both memory efficiency and accurate gradients; discretise-then-optimise giving only the latter and with large step sizes optimise-then-discretise giving only the former.

## Chapter 6

## Miscellanea

## Symbolic regression

## Introduction to symbolic regression

Deep learning, including neural differential equations, typically produces 'black-box' models. Once the model has been trained, it is a relatively opaque neural network whose mode of operation is essentially mysterious. It may be a good model, but a good model is not always the end goal. Scientific progress may be predicated upon understanding the model as well.

It is often desirable to obtain symbolic expressions - an imprecise term which we use here to refer to some relatively shallow tree of primitive operations, for example x × (( y -4. 2) + z ). These primitive operations typically include addition, multiplication, exponentiation and so .

Symbolic regression is the process of deriving such expressions from data in an automated way. One difficulty is the lack of differentiability of the space of such expressions. Whilst any constant in the expression (such as the 4. 2 above) may be optimised differentiably, the space between expressions is usually traversed via genetic algorithms. Another difficulty is the size of this space: there are (2 n )! ( n +1)! n ! binary trees with n vertices, and so as a rough approximation we may expect there to be a similar number of possible expressions to consider. This is a big number.

For these reasons, symbolic regression is a difficult task that often works best only on simple problems; past a certain point the complexity grows too large and the problem becomes intractable.

## Symbolic regression for dynamical systems

Example 6.1. Suppose we observe paired samples of both y (t) and d y d t (t), assumed to satisfy an equation of the form Then SINDy seeks a symbolic expression for f by selecting some features f i in advance, parameterising f (y) = ∑ N i =1 θ i f i (y), and directly regressing d y d t (t) against { f i (y (t)) } N i =1. A sparsity penalty such as L 1 -regularisation is applied to θ so that only a few terms are selected in the final expression.

This procedure is simply standard LASSO, and the dynamical character of the problem is essentially irrelevant. SINDy is arguably the dominant technique for symbolic regression with dynamical systems; some example extensions and applications include [Rud+17 Kah+19; Kap+21; Cha+19a].

However, SINDy has made two strong assumptions: (a) that paired observations of both y and d y d t ( t ) are available, and (b) that f is a shallow tree of expressions - just a linear combination of preselected features.

We will now see how NDEs offer ways to remove both of the assumptions made in Example 6.1.

Removing assumption (a): no paired observations Suppose we observe samples y (t) assumed to come from some dynamical system which for simplicity we assume is an autonomous ODE. (Although this is not necessary - the same ideas apply equally well to non-autonomous dynamical systems, and to non-ODEs such as CDEs and SDEs.)

Given this data, we learn some f = f θ as a neural network as described in the rest of this thesis. For example, minimising some empirical loss between the data and a numerical solution of the initial value problem, and optimising f θ via backpropagation.

Remark 6.2. Note that unlike SINDy, we have not assumed access to paired observations of both y and d y d t ( t ).

SINDy sometimes works around this by approximating d y d t ( t ) using finite differences. However this requires densely-packed observations, whilst the above procedure applies even when observations of y ( t ) are sparse.

Removing assumption (b): deep symbolic expressions Subsequently, we perform symbolic regression across the learnt f θ. That is, for each observed sample y we evaluate f θ ( y ), and symbolically regress f θ ( y ) against y.

The symbolic regression itself may be performed in any number of ways. A reasonable choice for most tasks is regularised evolution [Rea+19], which is capable of learning complex trees of expressions, and traverses the space between them via genetic algorithms. Open source software libraries exist to perform this task - at time of writing we recommend the PySR and SymbolicRegression.jl libraries for Python and Julia respectively.

More advanced techniques include [; Gui+20 Li+19]. For example deep symbolic regression introduces learnt neural network optimisers to tackle the task of searching through symbolic expressions.

(And if we really wanted, we could just take the simple approach of applying regularised linear regression against preselected features as in Example 6.1 - any symbolic regression technique will do.)

The result of this symbolic regression is our final result.

Remark 6.3. Note the Markov assumption that is being made in equation (6.1): the vector field f depends entirely on the observations y, so that there is no dependence on the past. In contrast observe that our typical set-up for NDEs has been to have the dynamical system operate in some latent space (that is, y is hidden state), and then linearly project this space down to the data space. See for example Remark 2.9, or the use of readout maps with neural CDEs and SDEs (Chapters 3 and 4).

Extending symbolic regression to the non-Markov setting is nontrivial. The essential difficulty is that symbolic regression in a latent space is not obviously meaningful. Supposing that the latent space is some R d y ∋ y ( t ), and letting A ⊆ { R d y → R d y } be some collection of automorphisms of this space, then for any φ ∈ A, both f and φ -1 ◦ f ◦ φ define essentially the same dynamics. That is, we may only identify f up to conjugacy by elements of A.

We note that [Cha+19b] do consider symbolic regression in a latent space. The above problem is dealt with implicitly in an ad-hoc manner, by (a) using only simple symbolic regression techniques (LASSO as with SINDy) to constrain the complexity of the vector field; (b) relying on Lipschitz embeddings/decodings from the latent space, again to constrain complexity; (c) manually selecting the 'best' element of the conjugacy class { φ -1 ◦ f ◦ φ | φ ∈ A} after training has completed. As such 'latent symbolic regression' has seen some success, but is in many respects still an open problem.

## Example

Let T > 0 and consider the nonlinear oscillator with x, y ∼ Uniform[-0. 6, 1]. Samples from this equation resemble warped and deformed sines and cosines.

Figure 6.1: Sample, and trained reconstruction, of the nonlinear oscillator (6.2). Both dimensions ( x, y ) of the oscillator are shown plotted against time t. Model and data align almost perfectly.

We aim to learn the symbolic form of this differential equation from data. Note the form of the vector fields, which would be very difficult to learn using SINDy. 1 Data We fix some points t j ∈ [0, T], with t 0 = 0. For initial conditions x, y ∼ Uniform[-0. 6, 1] we assume access to observations of the corresponding x (t j), y (t j). For simplicity we take the samples to be noiseless.

Neural regression We train a neural ODE via the L 2 loss as described above or as in Chapter 2, to reconstruct x (t j), y (t j) given x, y. That is, we consider the model where f θ: R 2 → R 2 is a neural network, and for each initial condition (x, y) the above equation is solved as an initial value problem using a numerical ODE solver.

The result of training this neural ODE is shown in Figure 6.1. The model has perfectly learnt the structure of the problem.

Symbolic regression We now have access to a function f θ: R 2 → R 2 which we may treat in isolation. The dynamic structure of the problem has been removed.

Symbolically regressing f θ (x (t j), y (t j)) against (x (t j), y (t j)) via regularised evolution produces the expression 1 Requiring for example the additional knowledge that the vector field is in fact a rational function [Man+16].

Neural-symbolic regression Finally, we treat (6.3) as the vector field of a 'neural' differential equation and perform another round of gradient-based optimisation against the original dataset to optimise the constants in the symbolic expressions.

Rounding each constant to the nearest multiple of 0.01 then produces the desired vector field Further details Further details may be found in Appendix D.5. The code is available as an example in Diffrax.

## Limitations of neural differential equations

We have spent most of this thesis discussing the numerous advantages and applications of neural differential equations. It is only fair we dedicate some space to their limitations.

## Data requirements

Neural differential equations have one major difference to classical differential equations. Using a neural network as the vector field (or as a component of the vector field, as with UDEs), results in greatly increased model expressivity, and so correspondingly more data is needed to train the model.

As such data requirements are typically comparable to neural network based approaches. A few hundred samples represents an optimistic lower bound on the amount of data required. The toy example problems considered in this thesis use a few thousand samples. Some examples ([Kid+21b, Section 4.2]) use millions of samples.

This is a limitation compared to classical differential equations - in return for which we receive more expressive models - but compared to neural networks this is of course quite normal.

## Speed

In particular when using higher-order differential equation solvers, which make multiple vector field evaluations, then neural differential equations can be somewhat slow to evaluate or train.

This can be mitigated by using cheaper, lower-order, solvers. 2 For example a low- order reversible solver (Section 5.3.2) can be used to obtain accurate gradients despite its low order.

2 Which need not affect model efficacy. Model efficacy, and accuracy at solving the idealised differential equation, are two different things.

Additionally, neural differential equations have a trick not available to standard neural networks: the choice of solver can be varied. For example a cheap low-order solver can be used for the bulk of training, and a more expensive higher-order solver used for fine-tuning and inference.

## Other discretised architectures

There are successful neural network architectures not so easily explained by being discretised neural differential equations. For example neither U-Net nor Transformers [Vas+17] admit obvious descriptions of this type, although Transformers do have a continuous theory of their own [Ram+20b].

Whilst neural differential equations are one (very successful) paradigm for constructing discrete architectures, it is apparent they are not the only one.

## Beyond neural differential equations: deep implicit layers

Neural differential equations are part of a larger family of models, known as deep implicit models or deep implicit layers.

Most layers (operations) used in machine learning models are 'explicit': given an input x they return an output y, as in where f θ denotes some function depending on trainable parameters θ.

In contrast, implicit layers take the form That is to say, the output is specified implicitly as one satisfying a certain condition.

This immediately opens up a host of questions - such as uniqueness - that we will not attempt to address in detail here. We aim only to give a high-level flavour of some of this broader family of models.

By its very nature, equation (6.5) cannot usually be solved explicitly or in closed form. As such the common thread running through such models is the use of a numerical scheme to find an approximate solution to equation (6.5).

The word 'implicit' thus takes on a dual meaning: not only is the solution y specified implicitly, but the computational steps to locate it need not be explicitly specified either.

Backpropagation through such models is possible - as in Section 5.1, there are both discretise-then-optimise and optimise-then-discretise approaches available. One option is to backpropagate through the operations of some numerical solver for (6.5). Another option is to apply the implicit function theorem, and then implicitly differentiate (6.5) itself. Variations on this are discussed in [, Chapter 15] and [; Blo+21; Fun+21].

A recent line of work has begun to suggest that implicit models may consistently outperform explicit models [Flo+21; Lu+21; Fun+21].

## Neural differential equations as implicit layers

A neural ODE is an implicit model: it is specified as That the computational steps for computing it are left implicit is the very reason Chapter 5 exists.

## Deep equilibrium models

'Deep Equilibrium Models' (DEQs) are essentially another term for implicit modelling in general, although the term is often used to refer to the case in which f θ takes the form of some 'large' neural network architecture, such as a Transformer [Vas+17], in which (6.5) is solved via fixed-point iterations.

As before, given an input x and a neural network f θ, the output y is simply defined as For example if x and y are sequences then taking f θ to be a Transformer is a reasonable choice. consider applications to time series whilst consider applications to computer vision. Monotone Operator Equilibrium Models (monDEQ) impose additional structure to ensure that 6.7 has a unique solution. Stability may be improved via regularisation.

## Multiple shooting: DEQs meet NODEs

Let d ∈ N and let f ∈ Lip(R × R d; R d). For u < v and x ∈ R d, let y denote the solution to and then let φ θ (x, u, v) = y (v) denote the map from initial condition to terminal condition.

Given an input x ∈ R d, a time horizon T > 0, and time points 0 = t 0 < · · · < t n = T, then multiple shooting reframes the solution of an ODE as the solution to the implicit problem: In many ways this is an implicit problem like any other - for example, we may aim to solve it via a fixed-point iteration, perhaps via Newton methods. Each step of this fixed point iteration itself involves solving multiple ODEs, to evaluate each φ θ (b j, t j, t j +1).

The key advantage of this approach is that the solution to the multiple ODEs over each interval [ t i, t i +1 ] may be performed in parallel. Provided that only few steps of the fixed-point solver are required, then this can reduce the overall computation time. (Even though it might not necessarily reduce the overall computational work, due to parallelism.) This is generally the case provided a good initial guess for b can be obtained.

Example 6.4. For example this may be used during training. Fix a single batch of data, and train a neural ODE for several steps (of parameter optimisation, updating θ ) on the same batch of data.

The first such step should obtain a solution via other numerical methods, for example as discussed in Chapter 5. This provides an initial value for each b j. As the learnt parameters θ evolve only slightly over the course of each training step, these b j can be used to provide a good initial guess for subsequent parameter optimisation steps, for which the neural ODE is solved using multiple shooting.

This may be used to train on the same batch of data for a few steps, before sampling a fresh batch.

Example 6.5. Another example arises when using a neural ODE to model a fullyobserved dynamical system. As it is a fully-observed dynamical system we may suppose it is Markov, and attempt to model the observations directly. (So that our neural ODE is 'unaugmented' and does not evolve in a latent space as in Section 2.3.3.)

Suppose further that each training sample consists of multiple observations y ( s j ) for s j ∈ [0, T ]. Then during training we may choose t j = s m j for some choice of m j, and take b j = y ( t j ) = y ( s m j ).

Example 6.6. A final example, this time during inference, is a classical use-case for multiple shooting: when using an ODE to provide forecasts into the future, continuously updated as new information arrives. Each forecast involves solving an ODE from the current time to some future time (for example, the time now plus ten minutes). As new data arrives we update our forecast, and the solution of the old forecast may be used to initialise each b j.

See [Mas+21] for more details.

## Differentiable optimisation

A final kind of implicit model is the solution to optimisation problems.

To be clear, whilst 'optimisation' often refers to the training of parameters, we are here referring to a model or layer whose operation is defined as the solution to an optimisation problem. We might express this as an implicit layer as where θ denotes trainable parameters, x denotes an input to the model, and C θ (x) is some constraint set.

Equivalently, and once again setting aside concerns such as uniqueness, Brandon Amos' doctoral thesis gives more details on differentiable optimisation, building on [Agr+19].

Example 6.7. For example, we might consider the optimisation problem where each θ i ∈ R d and each φ i ∈ R. This projects x onto some convex polytope, defined as the intersection of n half-spaces. In this case, θ i and φ i are trainable parameters. Given some paired observations x, y, denoting points x and their projections y onto some unknown polytope, then by optimising (6.8) we may learn an approximation to this unknown polytope.

## Comments

The material on symbolic regression is joint work with Miles Cranmer, and is new here.

The discussion on limitations of neural differential equations is a standard part of the folklore.

The notion of deep implicit layers is a recent one in deep learning, largely popularised.

## Chapter 7

## Conclusion

## Future directions

Having discussed the story so far - what future directions do we anticipate?

Boutique versus 'off the shelf' Most applications of neural differential equations are still 'boutique', rather than 'off the shelf'. The model is tailored - with largely unstructured vector fields retrained from scratch - for each individual use case.

This is unlike traditional differential equations, for which we have numerous wellstudied models, and in each case may expect to find a wealth of literature discussing their long-term behaviour, bifurcation properties and so . There already exists an analogous literature in modern deep learning, studying the behaviour of models such as GPT-3 [Bro+20], CLIP [Rad+21] and so .

In time the same development may take place for neural differential equations.

Neural ODEs Thousands of papers are written every year applying non-neural ODEs to topics across science, finance, economics,..., and so . Correspondingly, one significant opportunity is to apply neural ODEs to many of the tasks to which only non-neural ODEs have so far been applied.

Neural CDEs and SDEs Neural CDEs and neural SDEs are much newer. Work remains to be done on the practical machine learning details: finding expressive choices of vector field, and determining how to train these models efficiently. As with neural ODEs, another future direction is their application to practical topics, or how to hybridise them with their non-neural equivalents.

In addition, CDEs and neural CDEs have natural connections to control theory, and from that to reinforcement learning; these connections are largely unexplored.

Connections between neural SDEs, score matching diffusions, continuous normalising flows, optimal transport and Schr¨ odinger bridges are still in their infancy.

Numerical methods Numerical methods for neural differential equations are the single largest chapter in this thesis, and with good reason. Numerical differential equation solvers are an old topic, but recent developments such as reversible solvers and hypersolvers offer opportunities yet to be exploited. For example it would be desirable to have higher order reversible ODE solvers, or to be able to apply hypersolvers during training.

Symbolic regression Symbolic regression - both the underlying techniques and their application to dynamical systems - is still more alchemy than science. That is, it is more a matter of 'seeing what sticks' than of applying guiding principles.

For dynamical systems, only SINDy and its variants are well-established. The development and application of more advanced techniques such as regularised evolution and deep symbolic regression remains almost entirely wide open.

Neural PDEs One topic, made conspicuous by its absence from this thesis, is the possibility of neural partial differential equations.

There have been a selection of ideas in this space. For example a convolutional network is roughly equivalent to the discretisation of a parabolic PDE. [Li+20b; Li+20c; Li+21] consider the 'Fourier Neural Operator', which is probably the most welldeveloped current theory for something approaching neural PDEs. present some initial thoughts on neural stochastic partial differential equations. This list of references is far from exhaustive.

In practice many of the ideas in this space have yet to converge. (Perhaps unsurprisingly: there are a great many types of PDE to consider, after all.) This represents a major open direction for the field of neural differential equations.

## Thank you

Finally, it remains to thank the reader for their attention. We hope we have adequately conveyed some amount of insight (and our own enthusiasm) for this new, rapidly developing, and in our opinion highly exciting field of neural differential equations.

Neural differential equations sit at the intersection of arguably the two most successful modelling paradigms ever invented. In doing so, they demonstrate that these 'two' paradigms are perhaps much closer to one paradigm than at first glance we might imagine.
