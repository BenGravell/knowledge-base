<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Elements of Differentiable Programming

Topics include Uncertainty, Graphs, Datasets, Optimization, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Artificial intelligence has recently experienced remarkable advances, fueled by large models, vast datasets, accelerated hardware, and, last but not least, the transformative power of differentiable programming. This new programming paradigm enables end-to-end differentiation of complex computer programs (including those with control flows and data structures), making gradient-based optimization of program parameters possible. As an emerging paradigm, differentiable programming builds upon several areas of computer science and applied mathematics, including automatic differentiation, graphical models, optimization and statistics. This book presents a comprehensive review of the fundamental concepts useful for differentiable programming. We adopt two main perspectives, that of optimization and that of probability, with clear analogies between the two. Differentiable programming is not merely the differentiation of programs, but also the thoughtful design of programs intended for differentiation. By making programs differentiable, we inherently introduce probability distributions over their execution, providing a means to quantify the uncertainty associated with program outputs.

<!-- chunk {"id": "body-0003", "role": "body", "section": "What is differentiable programming?", "weight": 1.0} -->

A computer program is a sequence of elementary instructions for performing a task. In traditional computer programming, the program is typically manually written by a programmer. However, for certain tasks, particularly those involving intricate patterns and complex decisionmaking, such as image recognition or text generation, manually writing a program is extremely challenging, if not impossible.

<!-- chunk {"id": "body-0004", "role": "body", "section": "What is differentiable programming?", "weight": 1.0} -->

In contrast, modern neural networks offer a different approach. They are constructed by combining parameterized functional blocks and are trained directly from data using gradient-based optimization. This end-to-end training process, where the network learns both feature extraction and task execution simultaneously, allows neural networks to tackle complex tasks that were previously considered insurmountable for traditional, hand-coded programs. This new programming paradigm has been referred to as 'differentiable programming' or 'software 2.0'. We give an informal definition below.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Unparameterized program", "weight": 1.0} -->

Definition 1.1 (Differentiable programming). Differentiable programming is a programming paradigm in which complex computer programs (including those with control flows and data structures) can be differentiated end-to-end automatically, enabling gradient-based optimization of parameters in the program.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Neural networks as parameterized programs", "weight": 1.0} -->

In differentiable programming, as in regular computer programming, a program is defined as the composition of elementary operations, forming a computation graph. The key difference is that, as illustrated in Fig. 1.1, the program (such as a neural network) contains parameters that can be adjusted from data and can be differentiated end-to-end, using automatic differentiation (autodiff). Typically, it is assumed that the program defines a mathematically valid function (a.k.a. pure function): the function should return identical values for identical arguments and should not have any side effects. Moreover, the function should have well-defined derivatives, ensuring that it can be used in a gradient-based optimization algorithm. Therefore, differentiable programming is not only the art of differentiating through programs but also of designing meaningful differentiable programs.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Why do we need derivatives?", "weight": 1.0} -->

Machine learning typically boils down to optimizing a certain objective function, which is the composition of a loss function and a model (network) function. Derivative-free optimization is called zero-order optimization. It only assumes that we can evaluate the objective function that we wish to optimize. Unfortunately, it is known to suffer from the curse of dimensionality, i.e., it only scales to small dimensional problems, such as less than 10 dimensions. Derivative-based optimization, on the other hand, is much more efficient and can scale to millions or billions of parameters. Algorithms that use first and second derivatives are known as first-order and second-order algorithms, respectively.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Why is autodiff so useful?", "weight": 1.0} -->

Before the autodiff revolution, researchers and practitioners needed to manually implement the gradient of the functions they wished to optimize. Manually deriving gradients can become very tedious for complicated functions. Moreover, every time the function is changed (for example, for trying out a new idea), the gradient needs to be rederived. Autodiff is a game changer because it allows users to focus on quickly and creatively experimenting with functions for their tasks. An example of JAX code is given in Fig. 1.2.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Differentiable programming is not just deep learning", "weight": 1.0} -->

While there is clearly overlap between deep learning and differentiable programming, their focus is different. Deep learning studies artificial neural networks composed of multiple layers, able to learn intermediate representations of the data. Neural network architectures have been proposed with various inductive biases. For example, convolutional neural networks are designed for images and transformers are designed for sequences. On the other hand, differentiable programming studies the techniques for designing complex programs and differentiating through them. It is useful beyond deep learning: for instance in reinforcement learning, probabilistic programming and scientific computing in general.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Differentiable programming is not just deep learning", "weight": 1.0} -->

import jax.numpy as jnp from jax import grad, jit def predict (params, inputs): for W, b in params: outputs = jnp.dot(inputs, W) + b inputs = jnp.tanh(outputs) return outputs def loss_fn (params, inputs, targets): outputs = predict(params, inputs) return jnp.sum((outputs - targets) ** 2) grad_fun = jit(grad(loss_fn)) Figure 1.2: Thanks to automatic differentiation (autodiff), the user can focus on expressing the forward computation (model), enabling fast experimentation and alleviating the need for error-prone manual gradient derivation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Differentiable programming is not just autodiff", "weight": 1.0} -->

While autodiff is a key ingredient of differentiable programming, this is not the only one. Differentiable programming is also concerned with the design of principled differentiable operations. In fact, much research on differentiable programming has been devoted to make classical computer programming operations compatible with autodiff. As we shall see, many differentiable relaxations can be interpreted in a probabilistic framework. A core theme of this book is the interplay between optimization, probability and differentiation. Differentiation is useful for optimization and conversely, optimization can be used to design differentiable operators.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Our vision for differentiable programming", "weight": 1.0} -->

Computer programming offers powerful tools like control flows, data structures, and standard libraries, enabling users to construct complex programs for solving intricate problems. Our long-term vision is to achieve parity between traditional and differentiable programming, empowering programmers to seamlessly express differentiable programs (such as neural networks) using the full suite of tools they are accus- tomed to. However, as discussed earlier, differentiable programming is not simply a matter of applying automatic differentiation to existing code. Programs must be designed with differentiability in mind. This usually comes to inducing a probability distribution over the program or its components. While significant work remains to fully realize this ambitious goal, we hope this book offers a solid foundation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Where does 'differentiable programming' come from?", "weight": 1.0} -->

While neural networks and autodiff have existed for several decades, the term 'differentiable programming' is more recent. Olah discussed anologies between neural network architectures and higher-order functions in functional programming, and referred to it as a 'new kind of programming'. Dalrymple wrote an essay titled 'differentiable programming', recognizing a paradigm where programs learn details through differentiation, with the expressiveness of functional programming. Plotkin gave a keynote talk titled 'Some principles of differential programming languages' at POPL 2018. The 'differentiable programming' and 'software 2.0' terms were popularized among others by LeCun and Karpathy. From this perspective, autodiff frameworks can be seen, not merely as libraries, but as domain-specific languages (DSLs) embedded into an existing programming language, such as Python. See also Imai for a review.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Book goals and scope", "weight": 1.0} -->

The present book aims to provide an comprehensive introduction to differentiable programming with an emphasis on core mathematical tools.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Book goals and scope", "weight": 1.0} -->

- In Part I, we review fundamentals: differentiation and probabilistic learning. - In Part II, we review differentiable programs. This includes neural networks, sequence networks and control flows. - In Part III, we review how to differentiate through programs. This includes automatic differentiation, but also differentiating through optimization and integration (in particular, expectations).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Book goals and scope", "weight": 1.0} -->

- In Part IV, we review smoothing programs. We focus on two main techniques: infimal convolution, which comes from the world of optimization and convolution, which comes from the world of integration. We also strive to spell out the connections between them. - In Part V, we review optimizing programs: basic optimization concepts, first-order algorithms, second-order algorithms and duality.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Book goals and scope", "weight": 1.0} -->

Our goal is to present the fundamental techniques useful for differentiable programming, not to survey how these techniques have been used in various applications.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Intended audience", "weight": 1.0} -->

This book is intended to be a graduate-level introduction to differentiable programming. Our pedagogical choices are made with the machine learning community in mind. Some familiarity with calculus, linear algebra, probability theory and machine learning is beneficial.

<!-- chunk {"id": "body-0019", "role": "body", "section": "How to read this book?", "weight": 1.0} -->

This book does not need to be read linearly chapter by chapter. When needed, we indicate at the beginning of a chapter what chapters are recommended to be read as a prerequisite.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Differentiation", "weight": 1.0} -->

In this chapter, we review key differentiation concepts. In particular, we emphasize on the fundamental role played by linear maps.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Derivatives", "weight": 1.0} -->

To study functions, we need to capture their infinitesimal variations around points as defined by the notion of limit.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Derivatives", "weight": 1.0} -->

Definition 2.1 (Limit). We say that c ∈ R is the limit of f: R → R as v ∈ R approaches w ∈ R, denoted if, for any ε > 0, there exists R > 0 such that for any v ∈ R satisfying 0 < | v -w | ≤ R, we have | f (v) -c | ≤ ε.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Derivatives", "weight": 1.0} -->

We can also write f ( v ) → c as v → w. Limits are preserved under additions and multiplications. Namely, if lim v → w f ( v ) = c and lim v → w g ( v ) = d, then denoting ( af + bg )( w ):= af ( w ) + bg ( w ) for any a, b ∈ R and ( fg )( w ):= f ( w ) g ( w ), we have by definition of the limit, lim v → w ( af + bg )( v ) = ac + bd and lim v → w ( fg )( v ) = cd. The preservation of the limit under addition and multiplication by a scalar is generally referred to as the linearity of the limit, a property that many definitions in the sequel inherit.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Derivatives", "weight": 1.0} -->

With the notion of limit, we can already delineate a class of 'wellbehaved' functions: functions whose limits at any point equals the value of the function at that point. Functions satisfying this property are called continuous.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Derivatives", "weight": 1.0} -->

Definition 2.2 (Continuous function). A function f: R → R is continuous at a point w ∈ R if A function f is said to be continuous if it is continuous at all points in its domain.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Derivatives", "weight": 1.0} -->

Although the notion of continuity appears to be a benign assumption, several functions commonly-used in machine learning, such as the Heaviside step function (displayed in the left panel of Fig. 2.2), are not continuous and require special treatment.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Derivatives", "weight": 1.0} -->

Remark 2.1 (Little o notation). In the following, we will make use of Landau's little o notation. We write That is, the function f dominates g in the limit v → w. For example, f is continuous at w if and only if We now explain derivatives. Consider a function f: R → R. As illustrated in Fig. 2.1, its value on an interval [w 0, w 0 + δ] can be approximated by the secant between its values f (w 0) and f (w 0 + δ), a linear function with slope (f (w 0 + δ) -f (w 0)) /δ. In the limit of an infinitesimal variation δ around w 0, the secant converges to the tangent of f at w 0 and the resulting slope defines the derivative of f at w 0. The definition below formalizes this intuition.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Derivatives", "weight": 1.0} -->

Definition 2.3 (Derivative). The derivative of f: R → R at w ∈ R is defined as provided that the limit exists. If f ′ (w) is well-defined at a particular w, we say that the function f is differentiable at w. If f is differentiable at any w ∈ R, we say that it is differentiable everywhere or differentiable for short.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Derivatives", "weight": 1.0} -->

If f is differentiable at a given w, then it is necessarily continuous at w as shown in the following proposition. Non-differentiability of a continuous function at a given point w is generally illustrated by a kink, as shown in Fig. 2.2.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Calculus rules", "weight": 1.0} -->

For a given w ∈ R and two functions f: R → R and g: R → R, the derivative of elementary operations on f and g such as their sums, products or compositions can easily be derived from the definition of the derivative, under appropriate conditions on the differentiability of f and g at w. For example, if the derivatives of f and g exist at w, then the derivatives of their weighted sum or product exist, and satisfy the rules where (fg)(w):= f (w) g (w). The linearity can be verified directly from the linearity of the limits. For the product rule, in little o notation, we have, as δ → 0, hence the result.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Calculus rules", "weight": 1.0} -->

If the derivatives of g at w and of f at g (w) exist, then the derivative of the composition (f ◦ g)(w):= f (g (w)) at w exists and is given by We prove this result more generally in Proposition 2.2. As seen in the sequel, the linearity and the product rule can be seen as byproducts of the chain rule, making the chain rule the cornerstone of differentiation.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Calculus rules", "weight": 1.0} -->

Consider a function that can be expressed using sums, products or compositions of elementary functions, such as f ( w ):= e w ln w +cos w 2. Its derivative can be computed by applying the aforementioned rules on the decomposition of f into elementary operations and functions.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Calculus rules", "weight": 1.0} -->

Example 2.2 (Applying rules of differentiation). Consider f (w):= e w ln w +cos w 2. The derivative of f at w > 0 can be computed step by step as follows, denoting sq(w):= w 2, We therefore obtain that f ′ (w) = e w ln w + e w /w -2 w sin w 2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Calculus rules", "weight": 1.0} -->

Such a process is purely mechanical and lends itself to an automated procedure, which is the main idea of automatic differentiation presented in Chapter 8.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Leibniz's notation", "weight": 1.0} -->

The notion of derivative was first introduced independently by Newton and Leibniz in the 18 th century. The latter considered derivatives as the quotient of infinitesimal variations. Namely, denoting u = f (w) a variable depending on w through f, Leibniz considered the derivative of f as the quotient where du and dw denote infinitesimal variations of u and w respectively and the symbol | w denotes the evaluation of the derivative at a given point w. This notation simplifies the statement of the chain rule first discovered by Leibniz as we have for v = g (w) and u = f (v) This hints that derivatives are multiplied when considering compositions. At evaluation, the chain rule in Leibniz notation recovers the formula presented above as The ability of Leibniz's notation to capture the chain rule as a mere product of quotients made it popular throughout the centuries, especially in mechanics. The rationale behind Leibniz's notation, the concept of 'infinitesimal variations', was questioned by later mathematicians for its potential logical issues. The notation f ′ (w) first introduced by Euler and further popularized by Lagrange has then taken over in numerous mathematical textbooks.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Leibniz's notation", "weight": 1.0} -->

The concept of infinitesimal variations has been rigorously defined by using the set of hyperreal numbers. They extend the set of real numbers by considering each number as a sum of a non-infinitesimal part and an infinitesimal part. The formalism of infinitesimal variations further underlies the development of automatic differentiation algorithms through the concept of dual numbers.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Directional derivatives", "weight": 1.0} -->

Let us now consider a function f: R P → R with multi-dimensional input w:= ( w 1,..., w P ) ∈ R P. The most important example in machine learning is a function which, to the parameters w ∈ R P of a neural network, associates a loss value in R. Variations of f need to be defined along specific directions, such as the variation f ( w + δ v ) -f ( w ) of f around w ∈ R P in the direction v ∈ R P by an amount δ > 0. This consideration naturally leads to the definition of the directional derivative.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Directional derivatives", "weight": 1.0} -->

Definition 2.4 (Directional derivative). The directional derivative of f at w in the direction v is given by provided that the limit exists.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Directional derivatives", "weight": 1.0} -->

We use the notation [ v ] to emphasize that, for a given input w, we can see v ↦→ ∂f ( w )[ v ] as a function. This is essential to define the differentiability of f (Definition 2.6) at w and to later define linear maps (Section 2.3).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Directional derivatives", "weight": 1.0} -->

One example of directional derivative consists in computing the derivative of a function f at w in any of the canonical directions This allows us to define the notion of partial derivatives, denoted for i ∈ [P] This is also denoted in Leibniz's notation as ∂ i f (w) = ∂f (w) ∂w i or ∂ i f (w) = ∂ w i f (w). By moving along only the i th coordinate of the function, the partial derivative is akin to differentiating the function ω i ↦→ f (w 1,..., ω i,..., w P) around ω i, letting all other coordinates fixed at their values w i.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Gradients", "weight": 1.0} -->

We now introduce the gradient vector, which gathers the partial derivatives. We first recall the definitions of linear map and linear form.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Gradients", "weight": 1.0} -->

Definition 2.5 (Linear map, linear form). A function l: R P → R M is a linear map if for any a 1, a 2 ∈ R, v 1, v 2 ∈ R D, A linear map with values in R, l: R P → R, is called a linear form.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Gradients", "weight": 1.0} -->

Linearity plays a crucial role in the differentiability of a function.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Gradients", "weight": 1.0} -->

Definition 2.6 (Differentiability, single-output case). A function f: R P → R is differentiable at w ∈ R P if its directional derivative is defined along any direction, is linear in any direction v, and if We can now introduce the gradient.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Gradients", "weight": 1.0} -->

Definition 2.7 (Gradient). The gradient of a differentiable function f: R P → R at a point w ∈ R P is defined as the vector of partial derivatives By linearity, the directional derivative of f at w in the direction v = ∑ P i =1 v i e i is then given by Here, 〈·, ·〉 denotes the inner product. We provide its definition in Euclidean spaces in Section 2.3.2.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Gradients", "weight": 1.0} -->

As a simple example, any linear function of the form f ( w ) = 〈 a, w 〉 = ∑ P i =1 a i w i is differentiable as we have ( 〈 a, w + v 〉 - 〈 a, w 〉 -〈 a, v 〉 ) / ‖ v ‖ 2 = 0 for any v and in particular for ‖ v ‖ → 0. Moreover, its gradient is naturally given by ∇ f ( w ) = a.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Gradients", "weight": 1.0} -->

In the definition above, the fact that the gradient can be used to compute the directional derivative is a mere consequence of the linearity of ∂f ( w )[ v ] w.r.t. v. However, in more abstract cases presented in later sections, the gradient is defined directly through this property.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Gradients", "weight": 1.0} -->

More generally, to show that a function is differentiable and find its gradient, one approach is to approximate f (w + v) around v = 0. If we can find a vector g such that then f is differentiable at w, since 〈 g, ·〉 is linear. Moreover, g is then the gradient of f at w.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Gradients", "weight": 1.0} -->

Remark 2.3 (Gateaux and Fréchet differentiability). Multiple definitions of differentiability exist. The one presented in Definition 2.6 is that of Fréchet differentiable functions. Alternatively, if f: R P → R has well-defined directional derivatives along any directions then the function is Gateaux differentiable. Note that the existence of directional derivatives in any directions is not a sufficient condition for the function to be differentiable. In other words, any Fréchet differentiable function is Gateaux differentiable, but the converse is not true. As a counter-example, one can verify that the function f ( x 1, x 2 ):= x 3 1 / ( x 2 1 + x 2 2 ) is Gateaux differentiable at 0 but not (Fréchet) differentiable at 0 (because the directional derivative at 0 is not linear).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Gradients", "weight": 1.0} -->

Some authors also require Gateaux differentiable functions to have linear directional derivatives along any direction. These are still not Fréchet differentiable functions. Indeed, the limit in Definition 2.6 is over any vectors tending to 0 (potentially in a pathological way), while directional derivatives look at such limits uniquely in terms of a single direction.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Gradients", "weight": 1.0} -->

In the remainder of this chapter, all definitions of differentiability are in terms of Fréchet differentiability.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Gradients", "weight": 1.0} -->

The next example illustrates how to compute the gradient of the logistic loss and validates its differentiability.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Gradients", "weight": 1.0} -->

Example 2.3 (Gradient of logistic loss). Consider the logistic loss ℓ (θ, y):= -〈 y, θ 〉 +log ∑ i M =1 e θ i, that measures the prediction error of the logits θ ∈ R M w.r.t. the correct label y ∈ { e 1,..., e M }. Let us compute the gradient of this loss w.r.t. θ for fixed y, i.e., we want to compute the gradient of f (θ):= ℓ (θ, y). Let us decompose f as f = l +logsumexp with l (θ):= 〈-y, θ 〉 and the log-sum-exp function. The function l is linear so differentiable with gradient ∇ l (θ) = -y. We therefore focus on logsumexp.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Gradients", "weight": 1.0} -->

Denoting exp(θ) = (exp(θ 1),..., exp(θ M)), using that exp(x) = 1+ x + o (x), log(1 + x) = x + o (x), and denoting ⊙ the elementwise product, we get The above decomposition of logsumexp(θ + v) shows that it is differentiable, and that ∇ logsumexp(θ) = softargmax(θ), where Overall, we get that ∇ f (θ) = -y +softargmax(θ).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Linearity of gradients", "weight": 1.0} -->

The notion of differentiability for multi-input functions naturally inherits from the linearity of derivatives for single-input functions. For any u 1,..., u M ∈ R and any multi-input functions f 1,..., f M differentiable at w, the function u 1 f 1 +... + u M f M is differentiable at w and its gradient is

<!-- chunk {"id": "body-0056", "role": "body", "section": "Why is the gradient useful?", "weight": 1.0} -->

When f is differentiable, we say that v is an ascent direction of f from w if Conversely, we say that v is a descent direction of f from w if Using this definition, the gradient leads to the steepest ascent direction of f from w. To see why, we note that where we assumed ∇ f (w) = 0. The gradient ∇ f (w) is orthogonal to the level set of the function (the set of points w sharing the same value f (w)) and points towards higher values of f, as illustrated in Fig. 2.3. Conversely, the negative gradient -∇ f (w) points towards lower values of f. This observation motivates the development of optimization algorithms such as gradient descent. It is based on iteratively performing the update w t +1:= w t -γ ∇ f (w t), for γ > 0. It therefore seeks for a minimizer of f by moving along the steepest descent direction around w t given, up to a multiplicative factor, by -∇ f (w t). See also Definition 17.1 for more details.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Jacobians", "weight": 1.0} -->

Let us now consider a multi-output function f: R P → R M defined by f (w):= (f 1 (w),..., f M (w)), where f j: R P → R. A typical example in machine learning is a neural network. The notion of directional derivative can be extended to such function by defining it as the vector composed of the coordinate-wise directional derivatives: where the limits (provided that they exist) are applied coordinate-wise. The directional derivative of f in the direction v ∈ R P is therefore the vector that gathers the directional derivative of each f j, i.e., ∂f (w)[v] = (∂f j (w)[v]) j M =1. In particular, we can define the partial derivatives of f at w as the vectors As for the usual definition of the derivative, the directional derivative can provide a linear approximation of a function around a current input, as illustrated in Fig. 2.4 for a parametric curve f: R → R 2.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Jacobians", "weight": 1.0} -->

Just as in the single-output case, differentiability is defined not only as the existence of directional derivatives in any direction but also by the linearity in the chosen direction.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Jacobians", "weight": 1.0} -->

Definition 2.8 (Differentiability, multi-output case). A function f: R P → R M is (Fréchet) differentiable at a point w ∈ R P if its directional derivative is defined along any direction, is linear in any direction, and, The partial derivatives of each coordinate's function are gathered in the Jacobian matrix.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Jacobians", "weight": 1.0} -->

Definition 2.9 (Jacobian). The Jacobian of a differentiable function f: R P → R M at w is defined as the matrix gathering partial derivatives of each coordinate's function provided they exist, The Jacobian can be represented by stacking columns of partial derivatives or rows of gradients, By linearity, the directional derivative of f at w along any input direction v = ∑ P i =1 v i e i ∈ R P is then given by Notice that we use bold ∂ to indicate the Jacobian, seen as a matrix. The Jacobian matrix naturally generalizes the concepts of derivatives and gradients presented earlier. As for the single input case, to show that a function is differentiable, one approach is to approximate f (w + v) around v = 0. If we find a linear map l such that then f is differentiable at w. Moreover, if l is represented by matrix J such that l [v] = Jv then J = ∂ f (w).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Jacobians", "weight": 1.0} -->

As a simple example, any linear function f ( w ) = Aw for A ∈ R M × P is differentiable, since all its coordinate-wise components are singleoutput linear functions, and the Jacobian of f at any w is given by ∂ f ( w ) = A.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Jacobians", "weight": 1.0} -->

Remark 2.4 (Special cases of the Jacobian). For single-output functions f: R P → R, i.e., M = 1, the Jacobian matrix reduces to a row vector identified as the transpose of the gradient, For a single-input function f: R → R M, the Jacobian reduces to a single column vector of directional derivatives, denoted For a single-input single-output function f: R → R, the Jacobian reduces to the derivative of f, i.e., The next example illustrates the form of the Jacobian matrix for the element-wise application of a differentiable function σ, such as the softplus activation. In this case, the Jacobian takes a simple diagonal matrix form. As a consequence, the directional derivative associated with this function is simply given by an element-wise product: a full matrix-vector product is not needed, as would suggest Definition 2.9. We will revisit this point in Section 2.3.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Jacobians", "weight": 1.0} -->

Example 2.4 (Jacobian matrix of the softplus activation). Consider the element-wise application of the softplus defined for w ∈ R P by Since σ is differentiable, each coordinate of this function is differentiable and the overall function is differentiable. The j th coordinate of f is independent of the i th coordinate of w for i = j, so ∂ i f j (w) = 0 for i = j. For i = j, the result boils down to the derivative of σ at w j. That is, ∂ j f j (w) = σ ′ (w j), where σ ′ (w) = e w / (1 + e w). The Jacobian of f is therefore a diagonal matrix

<!-- chunk {"id": "body-0064", "role": "body", "section": "Chain rule", "weight": 1.0} -->

Equipped with a generic definition of differentiability and the associated objects, gradients and Jacobians, we can now generalize the chain rule, previously introduced for single-input single-output functions.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Chain rule", "weight": 1.0} -->

Proposition 2.2 (Chain rule). Consider f: R P → R M and g: R M → R R. If f is differentiable at w ∈ R P and g is differentiable at f (w) ∈ R M, then the composition g ◦ f is differentiable at w ∈ R P and its Jacobian is given by Proof. We progressively approximate g ◦ f (w + v) using the differentiability of f at w and g at f (w), Hence, g ◦ f is differentiable at w with Jacobian ∂ g (f (w)) ∂ f (w).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Chain rule", "weight": 1.0} -->

Proposition 2.2 can be seen as the cornerstone of any derivative computations. For example, it can be used to rederive the linearity and product rules associated to the derivatives of single-input single-outptut functions.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Chain rule", "weight": 1.0} -->

When g is scalar-valued, combined with Remark 2.4, we obtain a simple expression for ∇ ( g ◦ f ).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Chain rule", "weight": 1.0} -->

Proposition 2.3 (Chain rule, scalar-valued case). Consider f: R P → R M and g: R M → R. The gradient of the composition is given by This is a very useful identity in machine learning, as we often need to compose a vector-valued model function and a scalar-valued loss function. We illustrate this with linear regression below.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Chain rule", "weight": 1.0} -->

Example 2.5 (Linear regression). Consider a linear regression of N inputs x 1,..., x N ∈ R D onto N targets y 1,..., y N ∈ R, using a parameter vector w ∈ R D. The loss is defined as the sum of squared residuals, L ( w ):= ‖ Xw -y ‖ 2 2 = ∑ N i =1 ( 〈 x i, w 〉 -y i ) 2 where X:= ( x 1,..., x N ) ⊤ ∈ R N × D and y:= ( y 1,..., y N ) ⊤ ∈ R N.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Chain rule", "weight": 1.0} -->

The function L can be decomposed into a linear mapping f (w):= Xw and a squared error ℓ (p):= ‖ p -y ‖ 2 2, so that L = ℓ ◦ f. We can then apply the chain rule in Proposition 2.3 to get provided that f and ℓ are differentiable at w and f (w), respectively.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Chain rule", "weight": 1.0} -->

The function f is linear so differentiable with Jacobian ∂ f ( w ) = X. On the other hand the partial derivatives of ℓ are given by ∂ j ℓ ( p ) = 2( p j -y j ) for j ∈ { 1,..., N }. Therefore, ℓ is differentiable at any p and its gradient is ∇ ℓ ( p ) = 2( p -y ). By combining the two, we then get the gradient of L as

<!-- chunk {"id": "body-0072", "role": "body", "section": "Linear maps", "weight": 1.0} -->

The Jacobian matrix is useful as a representation of the partial derivatives. However, the core idea underlying the definition of differentiable functions, as well as their implementation in an autodiff framework, lies in the access to two key linear maps. These two maps encode infinitesimal variations along input or output directions and are referred to, respectively, as Jacobian-vector product (JVP) and Vectorjacobian product (VJP). This section formalizes these notions, in the context of Euclidean spaces.

<!-- chunk {"id": "body-0073", "role": "body", "section": "The need for linear maps", "weight": 1.0} -->

So far, we have focused on functions f: R P → R M, that take a vector as input and produce a vector as output. However, functions that use matrix or even tensor inputs/outputs are common place in neural networks. For example, consider the function of matrices of the form f ( W ):= Wx, where x ∈ R D and W ∈ R M × D. This function takes a matrix as input, not a vector. Of course, a matrix W ∈ R M × D can always be 'flattened' into a vector w ∈ R MD, by stacking the columns of W. We denote this operation by w = vec( W ) and its inverse by W = vec -1 ( w ). We can then equivalently write f ( W ) as ˜ f ( w ) = f (vec -1 ( w )) = vec -1 ( w ) x, so that the previous framework applies. However, we will now see that this would be inefficient.

<!-- chunk {"id": "body-0074", "role": "body", "section": "The need for linear maps", "weight": 1.0} -->

Indeed, the resulting Jacobian of ˜ f at any w consists in a matrix of size R M × MD, which, after some computations, can be observed to be mostly filled with zeros. Getting the directional derivative of f at W ∈ R M × D in a direction V ∈ R M × D would consist in (i) vectorizing V into v = vec( V ), (ii) computing the matrix-vector product ∂ ˜ f ( w ) v at a cost of M 3 D 2 computations (ignoring the fact that the Jacobian has many zero entries), (iii) re-shaping the result into a matrix.

<!-- chunk {"id": "body-0075", "role": "body", "section": "The need for linear maps", "weight": 1.0} -->

On the other hand, since f is linear in its matrix input, we can infer that the directional derivative of f at any W ∈ R M × D in any direction V ∈ R M × D is simply given by the function itself applied on V. Namely, we have ∂f ( W )[ V ] = f ( V ) = V x, which is simple to implement and clearly only requires MD operations. Note that the cost would have been the same, had we ignored the non-zero entries of ∂ ˜ f ( w ). The point here is that by considering the operations associated to the differentiation of a function as linear maps rather than using the associated representation as a Jacobian matrix, we can efficiently exploit the underlying input or output space structure. To that end, we now recall the main abstractions necessary to extend the previous definitions in the context of Euclidean spaces.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Euclidean spaces", "weight": 1.0} -->

Linear spaces, a.k.a. vector spaces, are spaces equipped with and closed under an addition rule compatible with multiplication by a scalar (we limit ourselves to the field of reals). Namely, in a linear space E, there exist operations + and ·, such that for any u, v ∈ E, and a ∈ R, we have u + v ∈ E and a · u ∈ E.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Euclidean spaces", "weight": 1.0} -->

Euclidean spaces are linear spaces equipped with a basis e 1,..., e P ∈ E. Any element v ∈ E can be decomposed as v = ∑ P i =1 v i e i for some unique scalars v 1,..., v P ∈ R. A canonical example of Euclidean space is the set R P of all vectors of size P that we already covered. The set of matrices R P 1 × P 2 of size P 1 × P 2 is also naturally a Euclidean space generated by the set of canonical matrices E ij ∈ { 0, 1 } P 1 × P 2 for i ∈ [ P 1 ], j ∈ [ P 2 ] filled with zero except at the ( i, j ) th entry filled with one. For example, W ∈ R P 1 × P 2 can be written W = ∑ P 1,P 2 i,j =1 W ij E ij. Euclidean spaces are naturally equipped with a notion of inner product.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Euclidean spaces", "weight": 1.0} -->

Definition 2.10 (Inner product). An inner product on a linear space E is a function 〈·, ·〉: E × E → R that is

<!-- chunk {"id": "body-0079", "role": "body", "section": "Euclidean spaces", "weight": 1.0} -->

- bilinear: x ↦→〈 x, w 〉 and y ↦→〈 v, y 〉 are linear for any w, v ∈ E, - symmetric: 〈 w, v 〉 = 〈 v, w 〉 for any w, v ∈ E, - positive definite: 〈 w, w 〉 ≥ 0 for any w ∈ E, and 〈 w, w 〉 = 0 if and only if w = 0.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Euclidean spaces", "weight": 1.0} -->

The norm induced by an inner product defines a distance ‖ w -v ‖ between w, v ∈ E, and therefore a notion of convergence.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Euclidean spaces", "weight": 1.0} -->

For vectors, where E = R P, the inner product is the usual one 〈 w, v 〉 = ∑ P i =1 w i v i. For matrices, where E = R P 1 × P 2, the inner product is the so-called Frobenius inner product. It is defined for any W, V ∈ R P 1 × P 2 by where tr(Z):= ∑ P i =1 Z ii is the trace operator defined for square matrices Z ∈ R P × P. For tensors of order R, which generalize matrices to E = R P 1 ×... × P R, the inner product is defined similarly for W, V ∈ R P 1 ×... × P R by where W i 1...i R is the (i 1,..., i R) th entry of W.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Linear maps and their adjoints", "weight": 1.0} -->

The notion of linear map in Definition 2.5 naturally extends to Euclidean spaces. Namely, a function l: E → F from a Euclidean space E onto a Euclidean space F is a linear map if for any w, v ∈ E and a, b ∈ R, we have l [ a w + b v ] = a · l [ w ] + b · l [ v ]. When E = R P and F = R M, there always exists a matrix A ∈ R M × P such that l [ v ] = Av. Therefore, we can think of A as the 'materialization' as a matrix of l.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Linear maps and their adjoints", "weight": 1.0} -->

Example 2.6 (Linear map). Consider the linear map l [ v ]:= ( ab ⊤ ) v, where a ∈ R M, b ∈ R P and v ∈ R P. This is a function from R P to R M. We can always materialize the linear map as a matrix A:= ab ⊤ ∈ R M × P and write l [ v ] = Av. However, applying a linear map on a vector v often does not require materializing the corresponding matrix. Following the previous example, we can simply write l [ v ] = ( b ⊤ v ) a, which only requires an inner product and an element-wise multiplication. This is more efficient than materializing A then computing Av, which requires an outer product and a matrix-vector multiplication.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Linear maps and their adjoints", "weight": 1.0} -->

We can define the adjoint operator of a linear map.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Linear maps and their adjoints", "weight": 1.0} -->

Definition 2.11 (Adjoint operator). Given two Euclidean spaces E and F equipped with inner products 〈·, ·〉 E and 〈·, ·〉 F, the adjoint of a linear map l: E → F is the unique linear map l ∗: F → E such that for any v ∈ E and u ∈ F, The adjoint can be thought as the counterpart of the matrix transpose for linear maps. When l [v] = Av, we have l ∗ [u] = A ⊤ u since Example 2.7 (Adjoint linear map). Using the linear map l [v] from the previous example, we have for all u ∈ R M and v ∈ R P, Therefore, the adjoint linear map is l ∗ [u] = (ba ⊤) u. This is a function from R M to R P. It can be materialized as the matrix A ⊤ = ba ⊤ ∈ R P × M. Applying l ∗ [u] can be done efficiently as l ∗ [u] = (a ⊤ u) b.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Jacobian-vector products", "weight": 1.0} -->

We now define the directional derivative using linear maps, leading to the notion of Jacobian-vector product (JVP). This can be used to facilitate the treatment of functions on tensors or for further extensions to infinite-dimensional spaces. In the following, E and F denote two Euclidean spaces equipped with inner products 〈·, ·〉 E and 〈·, ·〉 F. We start by defining differentiability in general Euclidean spaces.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Jacobian-vector products", "weight": 1.0} -->

Definition 2.12 (Differentiability in Euclidean spaces). Afunction f: E → F is differentiable at a point w ∈ E if the directional derivative along v ∈ E is well-defined for any v ∈ E, linear in v and if We can now formally define the Jacobian-vector product.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Jacobian-vector products", "weight": 1.0} -->

Definition 2.13 (Jacobian-vector product). For a differentiable function f: E → F, the linear map ∂f (w): E → F, mapping v to ∂f (w)[v], is called the Jacobian-vector product (JVP). From this perspective, the function ∂f is a function from E to a linear map from E to F. That is, we have We emphasize again that the directional derivative ∂f (w)[v] ∈ R is a value, while the JVP v ↦→ f (w)[v] is a function. Strictly speaking, v can belong to any Euclidean space E and does not need to be limited to a vector, as the JVP acronym would suggest. We adopt the name JVP, as it is now standard.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Recovering the gradient", "weight": 1.0} -->

Previously, we saw that for differentiable functions with vector input and scalar output, the directional derivative is equal to the inner product between the direction and the gradient. The same applies when considering differentiable functions from a Euclidean space with single outputs, except that the gradient is now an element of the input space and the inner product is the one associated with the input space.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Recovering the gradient", "weight": 1.0} -->

Proposition 2.4 (Gradient). If a function f: E → R is differentiable at w ∈ E, then there exists ∇ f (w) ∈ E, called the gradient of f at w such that the directional derivative of f at w along any input direction v ∈ E is given by In Euclidean spaces, the existence of the gradient can simply be shown by decomposing the partial derivative along a basis of E. Such a definition generalizes to infinite-dimensional (e.g., Hilbert spaces) spaces as discussed in Section 2.3.9.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Vector-Jacobian products", "weight": 1.0} -->

Consider a function f: R P → R M. Instead of variations of f along an input direction v ∈ R P, we may also consider the variations of f along an output direction u ∈ R M, namely, computing the gradient ∇〈 u, f 〉 (w) of the scalar-valued function Equivalently, we may compute the gradients ∇ f j (w) of each coordinate function f j:= 〈 e j, f 〉 at w, where e j is the j th canonical vector in R M. The infinitesimal variations of f at w along any output direction u = ∑ j M =1 u j e j ∈ R M are given by where ∂ f (w) ⊤ ∈ R P × M is the Jacobian's transpose. Using the definition of derivative as a limit, we may also write for i ∈ [P] where e i is the i th canonical vector in R P.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Vector-Jacobian products", "weight": 1.0} -->

For generic Euclidean spaces E and F, the counterpart of the transpose is the adjoint operator, leading to the notion of vector-Jacobian product.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Vector-Jacobian products", "weight": 1.0} -->

Proposition 2.5 (Vector-Jacobian product). If a function f: E → F is differentiable at w ∈ E, then its infinitesimal variation along an output direction u ∈ F is given by the adjoint map ∂f (w) ∗: F → E of the JVP, called the vector-Jacobian product (VJP). It satisfies where we denoted 〈 u, f 〉 F (w):= 〈 u, f (w) 〉 F. The function ∂f (·) ∗ is a function from E to a linear map from F to E. That is, we have Proof. The chain rule presented in Proposition 2.2 naturally generalizes to Euclidean spaces (see Proposition 2.6). Since 〈 u, ·〉 F is linear, its directional derivative is itself. Therefore, the directional derivative of 〈 u, f 〉 F is As this is true for any v ∈ E, ∂f (w) ∗ [u] is the gradient of 〈 u, f 〉 F per Proposition 2.4.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Vector-Jacobian products", "weight": 1.0} -->

We illustrate the JVP and VJP linear maps in Fig. 2.5.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Chain rule using linear maps", "weight": 1.0} -->

The chain rule presented before in terms of Jacobian matrices can readily be formulated to take advantage of the implementations of the JVP and VJP as linear maps.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Chain rule using linear maps", "weight": 1.0} -->

Proposition 2.6 (Chain rule, general case). Consider f: E → F and g: F → G, where E, F and G are Euclidean spaces. If f is differentiable at w ∈ E and g is differentiable at f (w) ∈ F, then the composition g ◦ f is differentiable at w ∈ E. Its JVP is given for all v ∈ E by Figure 2.5: Jacobian-vector product (JVP) v ↦→ ∂f (w)[v] and vector-Jacobian product (VJP) u ↦→ ∂f (w) ∗ [u], seen as linear maps. and its VJP is given for all u ∈ G by The proof follows the one of Proposition 2.2. This is illustrated in Fig. 2.6. When the last function is scalar-valued, which is often the case in machine learning, we obtain the following simplified result.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Chain rule using linear maps", "weight": 1.0} -->

Proposition 2.7 (Chain rule, scalar case). Consider f: E → F and g: F → R, the gradient of the composition is given by

<!-- chunk {"id": "body-0098", "role": "body", "section": "Functions of multiple inputs (fan-in)", "weight": 1.0} -->

Oftentimes, the inputs of a function do not belong to only one Euclidean space but to a product of them. An example is f ( x, W ):= Wx, which is defined on E:= R D × R M × D. In such a case, it is convenient to generalize the notion of partial derivatives to handle blocks of inputs.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Functions of multiple inputs (fan-in)", "weight": 1.0} -->

Consider a function f ( w 1,..., w S ) defined on E:= E 1 ×... ×E S, where w i ∈ E i. We denote the partial derivative with respect to the i th input w i along v i ∈ E i as ∂ i f ( w 1,..., w S )[ v i ]. Equipped with this notation, we can analyze how JVPs or VJPs are decomposed along several inputs.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Functions of multiple inputs (fan-in)", "weight": 1.0} -->

Proposition 2.8 (Multiple inputs). Consider a differentiable function of the form f (w) = f (w 1,..., w S) with signature f: E → F, where w:= (w 1,..., w S) ∈ E and E:= E 1 × · · · × E S. Then the JVP with the input direction v = (v 1,..., v S) ∈ E is given by The VJP with the output direction u ∈ F is given by Example 2.8 (Matrix-vector product). Consider f (x, W):= Wx, where W ∈ R M × D and x ∈ R D. This corresponds to setting E:= E 1 ×E 2:= R D × R M × D and F:= R M. For the JVP, letting v ∈ E 1 and V ∈ E 2, we obtain We can also access the individual JVPs as For the VJP, letting u ∈ F, we obtain We can access the individual VJPs by Remark 2.5 (Nested inputs). It is sometimes convenient to group inputs into meaningful parts.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Functions of multiple inputs (fan-in)", "weight": 1.0} -->

For instance, if the input is naturally broken down into two parts x = (x 1, x 2), where x 1 is a text part and x 2 is an image part, and the network parameters are naturally grouped into three layers w = (w 1, w 2, w 3), we can write f (x, w) = f ((x 1, x 2), (w 1, w 2, w 3)). This is mostly a convenience and we can again reduce it to a function of a single input, thanks to the linear map perspective in Euclidean spaces.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Functions of multiple inputs (fan-in)", "weight": 1.0} -->

Remark 2.6 (Hiding away inputs). It will often be convenient to ignore inputs when differentiating. We use the semicolon for this purpose. For instance, a function of the form L ( w; x, y ) (notice the semicolon) has signature L: W → R because we treat x and y as constants. Therefore, the gradient is ∇ L ( w; x, y ) ∈ W. On the other hand, the function L ( w, x, y ) (notice the comma) has signature L: W × X × Y → R so its gradient is ∇ L ( w, x, y ) ∈ W×X ×Y. If we need to access partial gradients, we use indexing, e.g., ∇ 1 L ( w, x, y ) ∈ W or ∇ w L ( w, x, y ) ∈ W when there is no ambiguity.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Functions with multiple outputs (fan-out)", "weight": 1.0} -->

Similarly, it is often convenient to deal with functions that have multiple outputs.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Functions with multiple outputs (fan-out)", "weight": 1.0} -->

Proposition 2.9 (Multiple outputs). Consider a differentiable function of the form f (w):= (f 1 (w),..., f T (w)), with signatures f: E → F and f i: E → F i, where F:= F 1 × · · · × F T. Then the JVP with the input direction v ∈ E is given by The VJP with the output direction u = (u 1,..., u T) ∈ F is Combined with the chain rule, we obtain that the Jacobian of is ∂h (w) = ∑ T i =1 ∂ i g (f (w)) ◦ ∂f i (w) and therefore the JVP is

<!-- chunk {"id": "body-0105", "role": "body", "section": "Extensions to non-Euclidean linear spaces", "weight": 1.0} -->

So far, we focused on Euclidean spaces, i.e., linear spaces with a finite basis. However, the notions studied earlier can be generalized to more generic spaces.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Extensions to non-Euclidean linear spaces", "weight": 1.0} -->

For example, directional derivatives (see Definition 2.12) can be defined in any linear space equipped with a norm and complete with respect to this norm. Such spaces are called Banach spaces. Completeness is a technical assumption that requires that any Cauchy sequence converges (a Cauchy sequence is a sequence whose elements become arbitrarily close to each other as the sequence progresses). A function f: E → F defined from a Banach space E onto a Banach space F is then called Gateaux differentiable if its directional derivative is defined along any direction (where limits are defined w.r.t. the norm in F ). Some authors also require the directional derivative to be linear to define a Gateaux differentiable function.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Extensions to non-Euclidean linear spaces", "weight": 1.0} -->

Fréchet differentiability can also naturally be generalized to Banach spaces. The only difference is that, in generic Banach spaces, the linear map l satisfying Definition 2.12 must be continuous, i.e., there must exist C > 0, such that l [ v ] ≤ C ‖ v ‖, where ‖ · ‖ is the norm in the Banach space E.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Extensions to non-Euclidean linear spaces", "weight": 1.0} -->

The definitions of gradient and VJPs require in addition a notion of inner product. They can be defined in Hilbert spaces, that is, linear spaces equipped with an inner product and complete with respect to the norm induced by the inner product (they could also be defined in a Banach space by considering operations in the dual space, see, e.g. ). The existence of the gradient is ensured by Riesz's representation theorem which states that any continuous linear form in a Hilbert space can be represented by the inner product with a vector. Since for a differentiable function f: E → R, the JVP ∂f ( w ): E → R is a linear form, Riesz's representation theorem ensures the existence of the gradient as the element g ∈ E such that ∂f ( w ) v = 〈 g, v 〉 for any v ∈ E. The VJP is also well-defined as the adjoint of the JVP w.r.t. the inner product of the Hilbert space.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Extensions to non-Euclidean linear spaces", "weight": 1.0} -->

As an example, the space of squared integrable functions on R is a Hilbert space equipped with the inner product 〈 a, b 〉:= ∫ a ( x ) b ( x ) dx. Here, we cannot find a finite number of functions that can express all possible functions on R. Therefore, this space is not a mere Euclidean space. Nevertheless, we can consider functions on this Hilbert space (called functionals to distinguish them from the elements of the space). The associated directional derivatives and gradients, can be defined and are called respectively, functional derivative and functional gradient, see, e.g., Frigyik et al. and references therein.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Second derivatives", "weight": 1.0} -->

For a single-input, single-output differentiable function f: R → R, its derivative at any point is itself a function f ′: R → R. We may then consider the derivative of the derivative at any point: the second derivative.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Second derivatives", "weight": 1.0} -->

Definition 2.14 (Second derivative). The second derivative f (w) of a differentiable function f: R → R at w ∈ R is defined as the derivative of f ′ at w, that is, provided that the limit is well-defined. If the second derivative of a function f is well-defined at w, the function is said to be twice differentiable at w. The second derivative is also denoted f ′′.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Second derivatives", "weight": 1.0} -->

If f has a small second derivative at a given w, the derivative around w is almost constant. That is, the function behaves like a line around w, as illustrated in Fig. 2.7. Hence, the second derivative is usually interpreted as the curvature of the function at a given point.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Second directional derivatives", "weight": 1.0} -->

For a multi-input function f: R P → R, we saw that the directional derivative encodes infinitesimal variations of f along a given direction. To analyze the second derivative, the curvature of the function at a given point w, we can consider the variations along a pair of directions, as defined below.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Second directional derivatives", "weight": 1.0} -->

Definition 2.15 (Second directional derivative). The second directional derivative of f: R P → R at w ∈ R P along v, v ′ ∈ R P is defined as the directional derivative of w ↦→ ∂f (w)[v] along v ′, that is, provided that ∂f (w)[v] is well-defined around w and that the limit exists.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Second directional derivatives", "weight": 1.0} -->

Of particular interest are the variations of a function around the canonical directions: the second partial derivatives, defined as for e i, e j the i th and j th canonical directions in R P, respectively. In Leibniz notation, the second partial derivatives are denoted

<!-- chunk {"id": "body-0116", "role": "body", "section": "Hessians", "weight": 1.0} -->

For a multi-input function, twice differentiability is simply defined as the differentiability of any directional derivative ∂f ( w )[ v ] w.r.t. w.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Hessians", "weight": 1.0} -->

Definition 2.16 (Twice differentiability). A function f: R P → R is twice differentiable at w ∈ R P if it is differentiable and ∂f: R P → ( R P → R ) is also differentiable at w.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Hessians", "weight": 1.0} -->

As a result, the second directional derivative is a bilinear form.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Hessians", "weight": 1.0} -->

Definition 2.17 (Bilinear map, bilinear form). A function b: R P × R P → R M is a bilinear map if b [v, ·]: R P → R is linear for any v and b [·, v ′] is linear for any v ′. That is, for v = ∑ P i =1 v i e i and v ′ = ∑ P i =1 v ′ i e i. A bilinear map with values in R, b: R P × R P → R, is called a bilinear form.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Hessians", "weight": 1.0} -->

The second partial derivatives are gathered in the Hessian and the second directional derivatives can be computed from it.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Hessians", "weight": 1.0} -->

Definition 2.18 (Hessian). The Hessian of a twice differentiable function f: R P → R at w is the P × P matrix gathering all second partial derivatives, provided that all second partial derivatives are well-defined.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Hessians", "weight": 1.0} -->

The second directional derivative at w is bilinear in any directions v = ∑ P i =1 v i e i and v ′ = ∑ P i =1 v ′ i e i. Therefore, Given the gradient of f, the Hessian is equivalent to the transpose of the Jacobian of the gradient. By slightly generalizing the notation ∇ to denote the transpose of the Jacobian of a function (which matches its definition for single-output functions), we have that the Hessian can be expressed as ∇ 2 f (w) = ∇ (∇ f)(w), which justifies its notation.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Hessians", "weight": 1.0} -->

Similarly as for the differentiability of a function f, twice differentiability of f at w is equivalent to having the second partial derivatives not only defined but also continuous in a neighborhood of w. Remarkably, by requiring twice differentiability, i.e., continuous second partial derivatives, the Hessian is guaranteed to be symmetric (Schwarz, 1873).

<!-- chunk {"id": "body-0124", "role": "body", "section": "Hessians", "weight": 1.0} -->

Proposition 2.10 (Symmetry of the Hessian). If a function f: R P → R is twice differentiable at w, then its Hessian ∇ 2 f ( w ) is symmetric, that is, ∂ 2 ij f ( w ) = ∂ 2 ji f ( w ) for any i, j ∈ { 1,... P }.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Hessians", "weight": 1.0} -->

The symmetry of the Hessian means that it can alternatively be written as ∇ 2 f ( w ) = ( ∂ 2 ji f ( w )) P i,j =1 = ∂ ( ∇ f )( w ), i.e., the Jacobian of the gradient of f.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Hessian-vector products", "weight": 1.0} -->

Similarly to the Jacobian, we can exploit the formal definition of the Hessian as a bilinear form to extend its definition to Euclidean spaces. In particular, we can define the notion of Hessian-vector product.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Hessian-vector products", "weight": 1.0} -->

Definition 2.19 (Hessian-vector product). If a function f: E → R defined on a Euclidean space E with inner product 〈·, ·〉, is twice differentiable at w ∈ E, then for any v ∈ E, there exists v ↦→ ∇ 2 f (w)[v], called the Hessian-vector product (HVP) of f at w along v, such that for any v ′ ∈ E, In particular for E = R P, the HVP is ∇ 2 f (w)[v] = (∂ 2 f (w)[v, e i]) P i =1.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Hessian-vector products", "weight": 1.0} -->

From an autodiff point of view, the HVP can be implemented in four different ways, as explained in Section 9.1.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Second-order Jacobians", "weight": 1.0} -->

The previous definitions naturally extend to multi-output functions f: E → F, where f:= (f 1,..., f M), f j: E → F j and F:= F 1 ×···×F M. The second directional derivative is defined by gathering the second derivatives of each coordinate's function. That is, for w, v, v ′ ∈ E, The function f is twice differentiable if and only if all its coordinates are twice differentiable. The second directional derivative is then a bilinear map. We can then compute second directional derivatives as When E = R P and F j = R, so that F = R M, the bilinear map can be materialized as a tensor the 'second-order Jacobian' of f. However, similarly to the Hessian, it is usually more convenient to apply the bilinear map to prescribed vectors v and v ′ than to materialize the second partial derivatives as a tensor.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Higher-order derivatives", "weight": 1.0} -->

Derivatives can be extended to any order. Formally, the n th derivative can be defined inductively as follows for a single-input, single-output function.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Higher-order derivatives", "weight": 1.0} -->

Definition 2.20 (n th order derivative). The n th derivative f (n) of a function f: R → R at w ∈ R is defined as provided that f n -1 is differentiable around w and that the limit exists. In such a case, the function is said to be n times differentiable at w.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Higher-order directional derivatives", "weight": 1.0} -->

For a multi-input function f, we can naturally extend the notion of directional derivative as follows.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Higher-order directional derivatives", "weight": 1.0} -->

Definition 2.21 (n th order directional derivative). The n th directional derivative of f: R P → R at w ∈ R P along v 1,..., v n is defined as A multi-input function f is n -times differentiable if it is n -1 differentiable and its n -1 directional derivative along any direction is differentiable. As a consequence the n th directional derivative is a multilinear form.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Higher-order directional derivatives", "weight": 1.0} -->

Definition 2.22 (Multilinear map, multilinear form). A function c: ⊗ n i =1 R P → R M is a multilinear map if it is linear in each coordinate given all others fixed, that is, if v j ↦→ c [ v 1,..., v j,..., v n ] is linear in v j for any j ∈ [ n ]. It is a multilinear form if it has values in R.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Higher-order directional derivatives", "weight": 1.0} -->

The n th order directional derivative is then given by The n th order partial derivatives can be materialized as an n th order tensor

<!-- chunk {"id": "body-0136", "role": "body", "section": "Higher-order Jacobians", "weight": 1.0} -->

All above definitions extend directly to the case of multi-output functions f: E → F, where F:= F 1 ×··· × F M. The n th directional derivatives are then The function f is then n times differentiable if it is n -1 differentiable and its n -1 directional derivative along any direction is differentiable.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Higher-order Jacobians", "weight": 1.0} -->

As a consequence, the n th directional derivative is a multilinear map. The n th directional derivative can be decomposed into partial derivatives as When E = R P and F = R M, the n th order partial derivatives can be materialized by an n +1 th order tensor

<!-- chunk {"id": "body-0138", "role": "body", "section": "Taylor expansions", "weight": 1.0} -->

With Landau's little o notation, we have seen that if a function is differentiable, it is approximated by a linear function in v, Such an expansion of the function up to its first derivative is called the first-order Taylor expansion of f around w.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Taylor expansions", "weight": 1.0} -->

If the function f is twice differentiable, we can approximate it by a quadratic in v, leading to the second-order Taylor expansion of f around w, Compared to the first-order Taylor approximation, it is naturally more accurate around w, as reflected by the fact that ‖ v ‖ 3 2 ≤ ‖ v ‖ 2 2 for ‖ v ‖ 2 ≤ 1.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Taylor expansions", "weight": 1.0} -->

More generally, we can build the n th order Taylor expansion of a n times differentiable function f: R P → R M around w ∈ R P by Note that, using the change of variable w ′ = w + v ⇐⇒ v = w ′ -w, it is often convenient to write the n th Taylor expansion of f (w ′) around w as Taylor expansions will prove useful in Chapter 7 for computing derivatives by finite differences.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Differential geometry", "weight": 1.0} -->

In this chapter, we progressively generalized the notion of derivative from real numbers to vectors and variables living in a linear space (a.k.a. vector space), either finite dimensional or infinite dimensional. We can further generalize these notions by considering a local notion of linearity. This is formalized by smooth manifolds in differential geometry, whose terminology is commonly adopted in the automatic differentiation literature and software. In this section, we give a brief overview of derivatives on smooth manifolds (simply referred to as manifolds), and refer to Boumal for a complete introduction.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Differentiability on manifolds", "weight": 1.0} -->

Essentially, a manifold is a set that can be locally approximated by a Euclidean space. The most common example is a sphere like the Earth. Seen from the Moon, the Earth is not a plane, but locally, at a human level, it can be seen as a flat surface. Euclidean spaces are also trivial examples of manifolds. A formal characterization of the sphere as a manifold is presented in Example 2.9. For now, we may think of a 'manifold' as some set (e.g., the sphere) contained in some ambient Euclidean space; note however that manifolds can be defined generally without being contained in a Euclidean space. Differentiability in manifolds is simply inherited from the notion of differentiability in the ambient Euclidean space.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Differentiability on manifolds", "weight": 1.0} -->

Definition 2.23 (Differentiability of restricted functions). Let M and N be manifolds. A function f: M→N defined from M⊆E to N ⊆ F, with E and F Euclidean spaces, is differentiable if f is the restriction of a differentiable function ¯ f: E → F, so that f coincides with ¯ f on M.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Differentiability on manifolds", "weight": 1.0} -->

Our objective is to formalize the directional derivatives and gradients for functions defined on manifolds. This formalization leads to the definitions of tangent spaces and cotangent spaces, and the associated generalizations of JVP and VJP operators as pushforward and pullback operators, respectively.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Tangent spaces and pushforward operators", "weight": 1.0} -->

To generalize the notion of directional derivatives of a function f, the one property we want to preserve is the chain rule. Rather than starting from the variations of f at a given point along a direction, we start with the variations of f along curves. Namely, on a manifold like the sphere S P in R P, we can look at curves α: R →S P passing through w ∈ S P at time 0, that is, α = w. For single-input functions like α, we denote for simplicity α ′:= ( α ′ 1,..., α ′ P ). The directional derivative of a function f must typically serve to define the derivative of f ◦ α at 0, such that ( f ◦ α ) ′ = ∂f ( w )[ α ′ ]. In the case of the sphere, as illustrated in Fig. 2.8, the derivative α ′ of a curve α passing through a point w is always tangent to the sphere at w. The tangent plane to the sphere at w then captures all possible relevant vectors to pass to the JVP we are building.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Tangent spaces and pushforward operators", "weight": 1.0} -->

To define the directional derivative of a function f on a manifold, we therefore restrict ourselves to an operator defined on the tangent space T w M, whose definition below is simplified for our purposes.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Tangent spaces and pushforward operators", "weight": 1.0} -->

Definition 2.24 (Tangent space). The tangent space of a manifold M at w ∈ M is defined as In the case of the sphere in Fig. 2.8, the tangent space is a plane, that is, a Euclidean space. This property is generally true: tangent spaces are Euclidean spaces, enabling us to define directional derivatives as linear maps. Now, if f is differentiable and goes from a manifold M to a manifold N, then f ◦ α is a differentiable curve in N. Therefore, Figure 2.8: A differentiable function f defined from a sphere M to a sphere N defines a push-forward operator that maps tangent vectors (derivatives of functions on the sphere passing through w) in the tangent space T w M to tangent vectors of N at f (w) in the tangent space T f (w) N.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Tangent spaces and pushforward operators", "weight": 1.0} -->

( f ◦ α ) ′ is the derivative of a curve passing through f ( w ) at 0 and is tangent to N at f ( w ). Hence, the directional derivative of f: M→N at w can be defined as a function from the tangent space T w M of M at w onto the tangent space T f ( w ) N of N at f ( w ). Overall, we built the directional derivative (JVP) by considering how a composition of f with any curve α pushes forward the derivative of α into the derivative of f ◦ α. The resulting JVP is called a pushforward operator in differentiable geometry.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Tangent spaces and pushforward operators", "weight": 1.0} -->

Definition 2.25 (Pushforward operator). Given two manifolds M and N, the pushforward operator of a differentiable function f: M→N at w ∈ M is the linear map ∂f (w): T w M→T f (w) N defined by for any v ∈ T w M such that v = α ′, where α: R → M is a differerentiable curve passing through w at 0, i.e., α = w.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Cotangent spaces and pullback operators", "weight": 1.0} -->

To generalize the JVP, we composed f: M→N with any single-input function α: R →M giving values on the manifold. The derivative of any such α is then pushed forward from T w M to T f ( w ) N by the action of f. To define the VJP, we take a symmetric approach. We consider all single-output differentiable functions β: N → R defined on y ∈ N with y = f ( w ) for some w ∈ M. We then want to pull back the derivatives of β when precomposing it by f. Therefore, the space on which the VJP acts is the space of directional derivatives of any β: N → R at y, defining the cotangent space.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Cotangent spaces and pullback operators", "weight": 1.0} -->

Definition 2.26 (Cotangent space). The cotangent space of a manifold N at y ∈ N is defined as Note that elements of the cotangent space are linear mappings, not vectors. This distinction is important to define the pullback operator as an operator on functions as done in measure theory. From a linear algebra viewpoint, the cotangent space is exactly the dual space of T y N, that is, the set of linear maps from T y N to R, called linear forms. As T y N is a Euclidean space, its dual space T ∗ y N is also a Euclidean space. The pullback operator is then defined as the operator that gives access to directional derivatives of β ◦ f given the directional derivative of β at f (w).

<!-- chunk {"id": "body-0152", "role": "body", "section": "Cotangent spaces and pullback operators", "weight": 1.0} -->

Definition 2.27 (Pullback operator). Given two manifolds M and N, the pullback operator of a differentiable function f: M→N at w ∈ M is the linear map ∂f (w) ⋆: T ∗ f (w) N → T ∗ w M defined by for any u ∈ T f (w) N ∗ such that ∂β (f (w)) = u, for a differentiable function β: N → R.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Cotangent spaces and pullback operators", "weight": 1.0} -->

Contrary to the pushforward operator that acts on vectors, the pullback operator acts on linear forms. Hence, the slight difference in notation between ∂f ( w ) ⋆ and ∂f ( w ) ∗, the adjoint operator of ∂f ( w ). To properly define the adjoint operator ∂f ( w ) ∗, we need a notion of inner product. Since tangent spaces are Euclidean spaces, we can define an inner product 〈·, ·〉 w for each T w M and w ∈ M, making M a Riemannian manifold. Equipped with these inner products, the cotangent space can be identified with the tangent space, and we can define gradients.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Cotangent spaces and pullback operators", "weight": 1.0} -->

Table 2.1: For a differentiable function f defined from a manifold M onto a manifold N, the JVP is generalized with the notion of pushforward ∂f ( w ). The counterpart of the pushforward is the pullback operation ∂f ( w ) ⋆ that acts on linear forms in the tangent spaces. For Riemannian manifolds, the pullback operation can be identified with the adjoint operator ∂f ( w ) ∗ of the pushforward operator as any linear form is represented by a vector.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Cotangent spaces and pullback operators", "weight": 1.0} -->

Definition 2.28 (Gradients in Riemannian manifolds). Let M be a Riemannian manifold equipped with inner products 〈·, ·〉 w. For any cotangent vector u ∈ T ∗ w M, with w ∈ M, there exists a unique tangent vector u ∈ T w M such that In particular for any differentiable function f: M→ R, we can define the gradient of f as the unique tangent vector ∇ f (w) ∈ T w M such that Therefore, rather than pulling back directional derivatives, we can pull back gradients. The corresponding operator is then naturally the adjoint ∂f (w) ∗ of the pushforward operator. Namely, given two Riemannian manifolds M and N, and a differentiable function f: M→N, we have Example 2.9 (The sphere as a manifold). The sphere S P in R P is defined as the set of points w ∈ R P, satisfying c (w):= 〈 w, w 〉-1 = 0, with JVP ∂c (w)[v] = 2 〈 w, v 〉.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Cotangent spaces and pullback operators", "weight": 1.0} -->

For any v = ( v 1,..., v P -1 ) ∈ R P -1 close enough to a point w on the sphere, we can define ψ 1 ( v ):= √ 1 -〈 v, v 〉 such that ψ ( v ):= ( v 1,..., v P -1, ψ 1 ( v )) satisfies 〈 ψ ( v ), ψ ( v ) 〉 = 1, that is c ( ψ ( w )) = 1. With the help of the mapping ψ -1 from a neighborhood of w in the sphere to R P -1, we can locally see the sphere as a space of dimension P -1.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Cotangent spaces and pullback operators", "weight": 1.0} -->

The tangent space can be naturally characterized in terms of the constraining function c. Namely, the curve α: R →S such that α = w satisfies for any δ ∈ R, c (α (δ)) = 0. Hence, differentiating the implicit equation, we have That is, α ′ is in the null space of ∂c (w), denoted The tangent space of S at w is then We naturally recover that the tangent space is a Euclidean space of dimension P -1, defined as the set of points orthogonal to w.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Generalized derivatives", "weight": 1.0} -->

While we largely focus on differentiable functions in this book, it is important to characterize non-differentiable functions. We distinguish here two cases: continuous functions and non-continuous functions. For the former case, there exist generalizations of the notion of directional derivative, gradient and Jacobian, presented below. For non-continuous functions, even if derivatives exist almost everywhere, they may be uninformative. For example, piecewise-constant functions, encountered in e.g. control flows (Chapter 5), are almost everywhere differentiable but with zero derivatives. In such cases, surrogate functions can be defined to ensure the differentiability of a program (Part IV).

<!-- chunk {"id": "body-0159", "role": "body", "section": "Rademacher's theorem", "weight": 1.0} -->

We first recall the definition of (locally) Lipschitz continuous function.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Rademacher's theorem", "weight": 1.0} -->

Definition 2.29 ((Locally) Lipschitz continuous function). Afunction f: E → F, is Lipschitz continuous if there exists C ≥ 0 such that for any x, y ∈ E, A function f: E → F is locally Lipschitz continuous if for any x ∈ E, there exists a neighborhood U of x such that f restricted to U is Lipschitz continuous.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Rademacher's theorem", "weight": 1.0} -->

Rademacher's theorem then ensures that f is differentiable almost everywhere.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Rademacher's theorem", "weight": 1.0} -->

Proposition 2.11 (Rademacher's theorem). Let E and F denote Euclidean spaces. If f: E → F is locally Lipschitz-continuous, then f is almost everywhere differentiable, that is, the set of points in E at which f is not differentiable is of (Lebesgue) measure zero.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Rademacher's theorem", "weight": 1.0} -->

See also Morrey Jr for a standard proof.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Clarke derivatives", "weight": 1.0} -->

Rademacher's theorem hints that the definitions of directional derivatives, gradients and Jacobians may be generalized to locally Lipschitz continuous functions. This is what Clarke did in his seminal work, which laid the foundation of nonsmooth analysis. The first building block is a notion of generalized directional derivative.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Clarke derivatives", "weight": 1.0} -->

Definition 2.30 (Clarke generalized directional derivative). The Clarke generalized directional derivative of a locally Lipschitz continuous function f: E → R at w ∈ E in the direction v ∈ E is provided that the limit exists, where δ ↘ 0 means that δ approaches 0 by non-negative values, and where the limit superior is defined as for B (a, ε):= { x ∈ E: ‖ x -a ‖ ≤ ε } the ball centered at a of radius ε.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Clarke derivatives", "weight": 1.0} -->

There are two differences with the usual definition of a directional derivative: (i) we consider slopes of the function in a neighborhood of the point rather than at the given point, (ii) we take a limit superior rather than a usual limit. The first point is rather natural in the light of Rademacher's theorem: we can properly characterize variations on points where the function is differentiable, therefore we may take the limits of these slopes as a candidate slope for the point of interest. The second point is more technical but essential: it allows us to characterize the directional derivative as the supremum of some linear forms. These linear forms in turn define a set of generalized gradients.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Clarke derivatives", "weight": 1.0} -->

Definition 2.31 (Clarke generalized gradient). A Clarke generalized gradient of a locally Lipschitz function f: E → R at w ∈ E is a point g ∈ E such that ∀ v ∈ E The set of Clarke generalized gradients is called the Clarke subdifferential of f at w.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Clarke derivatives", "weight": 1.0} -->

Definition 2.30 and Definition 2.31 can be used in non-Euclidean spaces, such as Banach or Hilbert spaces. In Euclidean spaces, the Clarke generalized gradients can be characterized more simply thanks to Rademacher's theorem. Namely, as shown below, they can be defined as a convex combination of limits of gradients of f evaluated at a sequence in E \ Ω that converges to w.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Clarke derivatives", "weight": 1.0} -->

Proposition 2.12 (Characterization of Clarke generalized gradients). Let f: E → R be a locally Lipschitz continuous and denote Ω the set of points at which f is not differentiable (Proposition 2.11). An element g ∈ E is a Clarke generalized gradient of f at w ∈ E if and only if In the above, the convex hull of a set S ⊆ E, the set of convex combinations of elements of S, is denoted The Jacobian of a function f: E → F between two Euclidean spaces can be generalized similarly.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Clarke derivatives", "weight": 1.0} -->

Definition 2.32 (Clarke generalized Jacobian). Let f: E → F be a locally Lipschitz continuous and denote Ω the set of points at which f is not differentiable (Proposition 2.11). A Clarke generalized Jacobian of f at w ∈ E is an element J of For a continuously differentiable function f: E → F or f: E → R, there is a unique generalized gradient, recovering the usual gradient. The chain rule can be generalized to these objects. Recently, Bolte and Pauwels and Bolte et al. further generalized Clarke gradients through the definition of conservative gradients to define automatic differentiation schemes for nonsmooth functions.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Summary", "weight": 1.0} -->

- The usual definition of derivatives of real-valued univariate functions extends to multivariate functions f: R P → R through the notion of directional derivative ∂f ( w )[ v ] at w ∈ R P in the direction v ∈ R P.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Summary", "weight": 1.0} -->

- To take advantage of the representation of w = ∑ P j =1 w j e j using the canonical bases { e 1,..., e P }, the definition of differentiable functions requires the linearity of the directional derivative w.r.t. the direction v. - This requirement gives rise to the notion of gradient ∇ f (w) ∈ R P, the vector that gathers the partial derivatives and further defines the steepest ascent direction at w. - For vector-input vector-output functions f: R P → R M, the directional derivative leads to the definition of Jacobian matrix ∂ f (w) ∈ R M × P, the matrix which gathers all partial derivatives (notice that we use bold ∂). The chain rule is then the product of Jacobian matrices. - These notions can be extended to general Euclidean spaces, such as the spaces of matrices or tensors. For functions of the form f: E → R, the gradient is ∇ f (w) ∈ E. More generally, for functions of the form f: E → F, the Jacobian ∂f (w) can be seen as a linear map (notice the non-bold ∂).

<!-- chunk {"id": "body-0173", "role": "body", "section": "Summary", "weight": 1.0} -->

The directional derivative at w ∈ E naturally defines a linear map l [v] = ∂f (w)[v], where ∂f (w): E → F is called the Jacobian vector product (JVP) and captures the infinitesimal variation at w ∈ E along the input direction v ∈ E. - Its adjoint ∂f (w) ∗: F → E defines another linear map l [u] = ∂f (w) ∗ [u] called the vector Jacobian product (VJP) and captures the infinitesimal variation at w ∈ E along the output direction u ∈ F. The chain rule is then the composition of these linear maps. - For the particular case when we compose a scalar-valued function ℓ (such as a loss function) with a vector-valued function f (such as a network function), the gradient is given by ∇ (ℓ ◦ f)(w) = ∂f (w) ∗ ∇ ℓ (f (w)). This is why being able to apply the adjoint to a gradient, which as we shall see can be done with reverse-mode autodiff, is so pervasive in machine learning.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Summary", "weight": 1.0} -->

- The definitions of JVP and VJP operators can further be generalized in the context of differentiable geometry. In that framework, the JVP amounts to the pushforward operator that acts on tangent vectors. The VJP amounts to the pullback operator that acts on cotangent vectors. - We also saw that the Hessian matrix of a function f (w) from R P to R is denoted ∇ 2 f (w) ∈ R P × P. It is symmetric if the second partial derivatives are continuous. Seen as linear map, the Hessian leads to the notion of Hessian-vector product (HVP), which we saw can be reduced to the JVP or the VJP of ∇ f (w). - The main take-away message of this chapter is that computing the directional derivative or the gradient of compositions of functions does not require computing intermediate Jacobians but only to evaluate linear maps (JVPs or VJPs) associated with these intermediate functions. The goal of automatic differentiation, presented in Chapter 8, is precisely to provide an efficient implementation of these maps for computation chains or more generally for computation graphs.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Probabilistic learning", "weight": 1.0} -->

In this chapter, we review how to perform probabilistic learning. We also introduce exponential family distributions, as they play a key role in this book.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Discrete probability distributions", "weight": 1.0} -->

A discrete probability distribution over a set Y is specified by its probability mass function (PMF) p: Y →. The probability of y ∈ Y is then defined by where Y denotes a random variable. When Y follows a distribution p, we write Y ∼ p (with some abuse of notation, we use the same letter p to denote the distribution and the PMF). The expectation of φ (Y), where Y ∼ p and φ: Y → R M, is then its variance (for one-dimensional variables) is and its mode is The Kullback-Leibler (KL) divergence (also known as relative entropy) between two discrete distributions over Y, with associated PMFs p and q, is the statistical 'distance' defined by

<!-- chunk {"id": "body-0177", "role": "body", "section": "Continuous probability distributions", "weight": 1.0} -->

A continuous probability distribution over Y is specified by its probability density function (PDF) p: Y → R +. The probability of A ⊆ Y is then The definitions of expectation, variance and KL divergence are defined analogously to the discrete setting, simply replacing ∑ y ∈Y with ∫ Y. Specifically, the expectation of φ (Y) is and the KL divergence is The mode is defined as the arg maximum of the PDF.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Continuous probability distributions", "weight": 1.0} -->

When Y = R, we can also define the cumulative distribution function (CDF) The probability of Y lying in the semi-closed interval (a, b] is then

<!-- chunk {"id": "body-0179", "role": "body", "section": "Negative log-likelihood", "weight": 1.0} -->

We saw that a probability distribution over Y is specified by p (y), which is called the probability mass function (PMF) for discrete variables or the probability density function (PDF) for continuous variables. In practice, the true distribution p generating the data is unknown and we wish to approximate it with a distribution p λ, with parameters λ ∈ Λ. Given a finite set of i.i.d. observations y 1,..., y N, how do we fit λ ∈ Λ to the data? This can be done by maximizing the likelihood of the data, i.e., we seek to solve This is known as maximum likelihood estimation (MLE). Because the log function is monotonically increasing, this is equivalent to minimizing the negative log-likelihood, i.e., we have Example 3.1 (MLE for the normal distribution). Suppose we set p λ to the normal distribution with parameters λ = (µ, σ), i.e., Then, given observations y 1,..., y N, the MLE estimators for µ and σ 2 are the sample mean and the sample variance, respectively.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Consistency w.r.t. the Kullback-Leibler divergence", "weight": 1.0} -->

It is well-known that the MLE estimator is consistent, in the sense of the Kullback-Leibler divergence. That is, denoting the true distribution p and then ̂ λ N → λ ∞ in expectation over the observations, as N →∞. This can be seen by using and the law of large numbers.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Conditional probability distributions", "weight": 1.0} -->

Many times in machine learning, instead of a probability P (Y = y) for some y ∈ Y, we wish to define a conditional probability P (Y = y | X = x), for some input x ∈ X. This can be achieved by reduction to an unconditional probability distribution, and f is a model function with model parameters w ∈ W. That is, rather than being a deterministic function from X to Y, f is a function from X to Λ, the set of permissible distribution parameters of the output distribution associated with the input.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Conditional probability distributions", "weight": 1.0} -->

In Section 3.4 and throughout this book, we will also use the notation p θ instead of p λ when θ are the canonical parameters of an exponential family distribution.

<!-- chunk {"id": "body-0183", "role": "body", "section": "Conditional probability distributions", "weight": 1.0} -->

We emphasize that λ could be a single parameter or a collection of parameters. For instance, in the Bernoulli distribution, λ = π, while in the univariate normal distribution, λ = ( µ, σ ).

<!-- chunk {"id": "body-0184", "role": "body", "section": "Inference", "weight": 1.0} -->

The main advantage of this probabilistic approach is that our prediction model is much richer than if we just learned a function from X to Y.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Inference", "weight": 1.0} -->

We now review probability distributions useful for binary classification, multiclass classification, regression, multivariate regression, and integer regression. In the following, to make the notation more lightweight, we omit the dependence on x.

<!-- chunk {"id": "body-0186", "role": "body", "section": "Binary classification", "weight": 1.0} -->

For binary outcomes, where Y = { 0, 1 }, we can use a Bernoulli distribution with parameter When a random variable Y is distributed according to a Bernoulli distribution with parameter π, we write The PMF of this distribution is The Bernoulli distribution is a binomial distribution with a single trial. Since y ∈ { 0, 1 }, the PMF can be rewritten as and the variance is Figure 3.1: The Bernoulli distribution, whose PMF and CDF are here illustrated with parameter π = 0. 8. Its mean function is π = A ′ (θ) = logistic(θ) = 1 1+exp(-θ), where θ is for instance the output of a neural network. The negative log-likelihood leads to the logistic loss, L (θ, y) = softplus(θ) -θy = log(1 + exp(θ)) -θy. The loss curve is shown for y ∈ { 0, 1 }.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Parameterization using a sigmoid", "weight": 1.0} -->

Since the parameter π of a Bernoulli distribution needs to belong to, we typically use a sigmoid function (Section 4.4.3), such as a logistic function as the output layer: where g: X × W → R is for example a neural network and When g is linear in w, this is known as binary logistic regression.

<!-- chunk {"id": "body-0188", "role": "body", "section": "Parameterization using a sigmoid", "weight": 1.0} -->

Remark 3.1 (Link with the logistic distribution). The logistic distribution with mean and scale parameters µ and σ is a continuous probability distribution with PDF If a random variable U follows a logistic distribution with parameters µ and σ, we write U ∼ Logistic(µ, σ). The CDF of U ∼ Logistic(µ, σ) is Here, U can be interpreted as a latent continuous variable and u as a threshold.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Multiclass classification", "weight": 1.0} -->

For categorical outcomes with M possible choices, where Y = [M], we can use a categorical distribution with parameters where we define the probability simplex i.e., the set of valid discrete probability distributions. When Y follows a categorical distribution with parameter π, we write The PMF of the categorical distribution is is the standard basis vector for the coordinate y ∈ [M].

<!-- chunk {"id": "body-0190", "role": "body", "section": "Multiclass classification", "weight": 1.0} -->

Since Y is a categorical variable, it does not make sense to compute the expectation of Y but we can compute that of φ (Y) = e Y, Figure 3.2: The categorical distribution, whose PMF and CDF are here illustrated with parameter π = (0. 3, 0. 6, 0. 1). Its mean function is π = ∇ A (θ) = softargmax(θ), where θ ∈ R M is for instance the output of a neural network. Here, for illustration purpose, we choose to set θ = (s, 1, 0) and vary only s. Since the mean function ∇ A (θ) belongs to R 3, we choose to display 〈∇ A (θ), e i 〉 = ∇ A (θ) i, for i ∈ { 1, 2, 3 }. The negative log-likelihood leads to the logistic loss, L (θ, y) = logsumexp(θ) - 〈 θ, y 〉. The loss curve is shown for y ∈ { e 1, e 2, e 3 }, again with θ = (s, 1, 0) and varying s.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Multiclass classification", "weight": 1.0} -->

Therefore, as was also the case for the Bernoulli distribution, the mean and the probability distribution (represented by the vector π ) are the same in this case.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Parameterization using a softargmax", "weight": 1.0} -->

Since the parameter vector π of a categorical distribution needs to belong to △ M, we typically use a softargmax as the output layer: where g: X × W → R M is for example a neural network and The output of the softargmax is in the relative interior of △ M, relint(△ M) = △ M ∩ R M > 0. That is, the produced probabilities are always strictly positive. The categorical distribution is a multinomial distribution with a single trial. When g is linear in w, this is therefore known as multiclass or multinomial logistic regression, though strictly speaking a multinomial distribution could use more than one trial.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Regression", "weight": 1.0} -->

For real outcomes, where Y = R, we can use, among other choices, a normal distribution with parameters where µ ∈ R is the mean parameter and σ ∈ R + is the standard deviation parameter. When Y follows a normal distribution with parameters (µ, σ), we write One advantage of the probabilistic perspective is that we are not limited to predicting the mean. We can also compute the CDF where we used the error function This function is available in most scientific computing libraries, such as SciPy. We can also write is the CDF of the standard Gaussian distribution (with zero mean and unit variance). From the CDF, we also easily obtain Figure 3.3: The Gaussian distribution, with mean parameter µ and variance σ 2 = 1. Its mean function is µ = A ′ (θ) = θ, where θ is for instance the output of a neural network. The negative log-likelihood leads to the squared loss, L (θ, y) = (y -θ) 2. The loss curve is shown for y ∈ {-2, 0, 2 }.

<!-- chunk {"id": "body-0194", "role": "body", "section": "Parameterization", "weight": 1.0} -->

Typically, in regression, the mean is output by a model, while the standard deviation σ is kept fixed (typically set to 1). Since µ is unconstrained, we can simply set where f: X × W → R is for example a neural network. That is, the output of f is the mean of the distribution, We can also use µ to predict P (Y ≤ y) or P (a < Y ≤ b), as shown above.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Multivariate regression", "weight": 1.0} -->

More generally, for multivariate outcomes, where Y = R M, we can use a multivariate normal distribution with parameters where µ ∈ R M is the mean and Σ ∈ R M × M is the covariance matrix. When Y follows a multivariate normal distribution with parameters (µ, Σ), we write Using a diagonal covariance matrix is equivalent to using M independent normal distributions for each Y j, for j ∈ [M]. The expectation is

<!-- chunk {"id": "body-0196", "role": "body", "section": "Parameterization", "weight": 1.0} -->

Typically, in multivariate regression, the mean is output by a model, while the covariance matrix is kept fixed (typically set to the identity matrix). Since µ is again unconstrained, we can simply set More generally, we can parametrize the function f so as to output both the mean µ and the covariance matrix Σ, i.e., The function f must be designed such that Σ is symmetric and positive semi-definite. This is easy to achieve for instance by parametrizing Σ = SS ⊤ for some matrix S.

<!-- chunk {"id": "body-0197", "role": "body", "section": "Integer regression", "weight": 1.0} -->

For integer outcomes, where Y = N, we can use, among other choices, a Poisson distribution with mean parameter λ > 0. When Y follows a Poisson distribution with parameter λ, we write It is the probability of y events occuring in an interval of time. The Poisson distribution is frequently used when there is a large number of possible events, each of which is rare.

<!-- chunk {"id": "body-0198", "role": "body", "section": "Integer regression", "weight": 1.0} -->

The Poisson distribution implies that the index of dispersion (the ratio between variance and mean) is 1, since When this assumption is inappropriate, one can use generalized Poisson distributions.

<!-- chunk {"id": "body-0199", "role": "body", "section": "Loss functions", "weight": 1.0} -->

We now discuss how to learn the model parameters w ∈ W from input-output pairs ( x 1, y 1 ),..., ( x N, y N ).

<!-- chunk {"id": "body-0200", "role": "body", "section": "Deterministic vs. probabilistic approaches", "weight": 1.0} -->

In a deterministic approach, if we used a mapping f: X × W → Y, we could formulate an objective function of the form where ℓ: Y × Y → R is a loss function. Unfortunately, L (w) would be typically discontinuous if Y is a discrete output space (as is the case in classification), making optimization difficult.

<!-- chunk {"id": "body-0201", "role": "body", "section": "Deterministic vs. probabilistic approaches", "weight": 1.0} -->

In contrast, in the probabilistic approach, we use a mapping f: X × W → Λ to distribution parameters, and we can formulate an objective of the form where ℓ: Λ ×Y → R. This is typically a continuous objective, since Λ is typically a continuous set and p λ varies continuously w.r.t. λ even if p λ is a distribution over a discrete set Y. In other words, the probabilistic approach is not only powerful for the inference it allows us to do (probability, expectation, variance, mode), but also because it allows to formulate a continuous and typically differentiable objective function!

<!-- chunk {"id": "body-0202", "role": "body", "section": "Negative log-likelihood", "weight": 1.0} -->

In the conditional setting briefly reviewed in Section 3.3.1, we can use maximum likelihood estimation (MLE) to estimate the model parameters w ∈ W of f. Given a set of input-output pairs (x 1, y 1),..., (x N, y N), we choose the model parameters that maximize the likelihood of the data, where Again, this is equivalent to minimizing the negative log-likelihood, In the notation above, this corresponds to defining the loss function

<!-- chunk {"id": "body-0203", "role": "body", "section": "Recovering well-known loss functions", "weight": 1.0} -->

Interestingly, MLE allows us to recover several popular loss functions.

<!-- chunk {"id": "body-0204", "role": "body", "section": "Recovering well-known loss functions", "weight": 1.0} -->

- For the Bernoulli distribution with parameter λ i = π i = logistic(g (x i, w)), we have which is the binary logistic loss function.

<!-- chunk {"id": "body-0205", "role": "body", "section": "Recovering well-known loss functions", "weight": 1.0} -->

- For the categorical distribution with parameters λ i = π i = softargmax(g (x i, w)), we have which is the multiclass logistic loss function, also known as cross-entropy loss.

<!-- chunk {"id": "body-0206", "role": "body", "section": "Recovering well-known loss functions", "weight": 1.0} -->

- For the normal distribution with mean λ i = µ i = f (x i, w) and fixed variance σ 2 i, we have which is, up to constant and with unit variance, the squared loss function.

<!-- chunk {"id": "body-0207", "role": "body", "section": "Recovering well-known loss functions", "weight": 1.0} -->

- For the Poisson distribution with mean λ i = exp(θ i), where θ i:= g (x i, w), we have which is the Poisson loss function. The loss function is convex w.r.t. λ i and θ i for y i ≥ 0.

<!-- chunk {"id": "body-0208", "role": "body", "section": "The log-partition function", "weight": 1.0} -->

The log-partition function A is the logarithm of the distribution's normalization factor. That is, for discrete random variables and for continuous random variables. We denote the set of valid parameters We can conveniently rewrite A (θ) for discrete random variables as and similarly for continuous variables. Here, we defined the affine map Since A (θ) is the composition of logsumexp, a convex function, and of B, an affine map, we immediately obtain the following proposition.

<!-- chunk {"id": "body-0209", "role": "body", "section": "The log-partition function", "weight": 1.0} -->

Proposition 3.1 (Convexity of the log-partition). A ( θ ) is a convex function.

<!-- chunk {"id": "body-0210", "role": "body", "section": "The log-partition function", "weight": 1.0} -->

A major property of the log-partition function is that its gradient coincides with the expectation of φ ( Y ) according to p θ.

<!-- chunk {"id": "body-0211", "role": "body", "section": "The log-partition function", "weight": 1.0} -->

Table 3.1: Examples of distributions in the exponential family.

<!-- chunk {"id": "body-0212", "role": "body", "section": "The log-partition function", "weight": 1.0} -->

Proof. The result follows directly from The gradient ∇ A (θ) is therefore often called the mean function. The set of achievable means µ (θ) is defined by where conv(S) is the convex hull of S and P (Y) is the set of valid probability distributions over Y.

<!-- chunk {"id": "body-0213", "role": "body", "section": "The log-partition function", "weight": 1.0} -->

When the exponential family is minimal, which means that the parameters θ uniquely identify the distribution, it is known that ∇ A is a one-to-one mapping from Θ to M. That is, µ ( θ ) = ∇ A ( θ ) and θ = ( ∇ A ) -1 ( µ ( θ )).

<!-- chunk {"id": "body-0214", "role": "body", "section": "The log-partition function", "weight": 1.0} -->

Similarly, the Hessian ∇ 2 A ( θ ) coincides with the covariance matrix of φ ( Y ) according to p θ.

<!-- chunk {"id": "body-0215", "role": "body", "section": "Maximum entropy principle", "weight": 1.0} -->

Suppose we observe the empirical mean ̂ µ = 1 N ∑ n i =1 φ (y i) ∈ M of some observations y 1,..., y N. How do we find a probability distribution achieving this mean? Clearly, such a distribution may not be unique. One way to choose among all possible distributions is by using the maximum entropy principle. Let us define the Shannon entropy by for discrete variables and by for continuous variables. This captures the level of 'uncertainty' in p, i.e., it is maximized when the distribution is uniform. Then, the maximum entropy distribution satisfying the first-order moment condition (i.e., whose expectation matches the empirical mean) is It can be shown that the maximum entropy distribution is necessarily in the exponential family with sufficient statistics defined by φ and its canonical parameters θ coincide with the Lagrange multipliers of the above constraint.

<!-- chunk {"id": "body-0216", "role": "body", "section": "Maximum likelihood estimation", "weight": 1.0} -->

Similarly as in Section 3.2, to fit the parameters θ ∈ Θ of an exponential family distribution to some i.i.d. observations y 1,..., y N, we can use the MLE principle, i.e., Fortunately, for exponential family distributions, the log probability/density enjoys a particularly simple form.

<!-- chunk {"id": "body-0217", "role": "body", "section": "Maximum likelihood estimation", "weight": 1.0} -->

Proposition 3.3 (Negative log-likelihood). The negative log-likelihood of an exponential family distribution is and its Hessian is It follows from Proposition 3.1 that θ ↦→ -log p θ (y) is convex. Interestingly, we see that the gradient is the residual between the expectation of φ (Y) according to the model and the observed φ (y). Therefore, the negative log-likelihood of an exponential family distribution can be seen as performing first moment matching.

<!-- chunk {"id": "body-0218", "role": "body", "section": "Probabilistic learning with exponential families", "weight": 1.0} -->

In the supervised probabilistic learning setting, we wish to estimate a conditional distribution of the form p w (y | x). Given a model function f, such as a neural network, a common approach for defining such a conditional distribution is by reduction to the unconditional setting, In other words, the role of f is to produce the parameters of p θ given some input x. It is a function from X × W to Θ. Note that f must be designed such that it produces an output in Many times, Θ will be the entire R M but this is not always the case. For instance, as we previously discussed, for a multivariate normal distribution, where θ = (µ, Σ) = f (x, w), we need to ensure that Σ is a positive semidefinite matrix.

<!-- chunk {"id": "body-0219", "role": "body", "section": "Training", "weight": 1.0} -->

Given input-output pairs { (x i, y i) } N i =1, we then seek to find the parameters w of f (x, w) by minimizing the negative log-likelihood where θ i:= f (x i, w). While -log p θ (y) is a convex function of θ for exponential family distributions, we emphasize that -log p f (x, w) (y) is typically a nonconvex function of w, when f is a nonlinear function, such as a neural network.

<!-- chunk {"id": "body-0220", "role": "body", "section": "Inference", "weight": 1.0} -->

Once we found w by minimizing the objective function above, there are several possible strategies to perform inference for a new input x.

<!-- chunk {"id": "body-0221", "role": "body", "section": "Inference", "weight": 1.0} -->

- Expectation. When the goal is to compute the expectation of φ (Y), we can use ∇ A (f (x, w)). That is, we compute the distribution parameters associated with x by θ = f (x, w) and then we compute the mean by µ = ∇ A (θ). When f is linear in w, the composition ∇ A ◦ f is called a generalized linear model. - Probability. When the goal is to compute the probability of a certain y, we can compute the distribution parameters associated with x by θ = f (x, w) and then we can compute P (Y = y | X = x) = p θ (y).

<!-- chunk {"id": "body-0222", "role": "body", "section": "Inference", "weight": 1.0} -->

- Other statistics. When the goal is to compute other quantities, such as the variance or the CDF, we can convert the natural parameters θ to the original distribution parameters λ (see Table 3.1 for examples). Then, we can use established formulas for the distribution in original form, to compute the desired quantities.

<!-- chunk {"id": "body-0223", "role": "body", "section": "Summary", "weight": 1.0} -->

- We reviewed discrete and continuous probability distributions. - We saw how to fit distribution parameters to data using the maximum likelihood estimation (MLE) principle and saw its connection with the Kullback-Leibler divergence. - Instead of designing a model function from the input space X to the output space Y, we saw that we can perform probabilistic supervised learning by designing a model function from X to distribution parameters Λ. - Leveraging the so-obtained parametric conditional distribution then allowed us to compute, not only output probabilities, but also various statistics such as the mean and the variance of the outputs.

<!-- chunk {"id": "body-0224", "role": "body", "section": "Summary", "weight": 1.0} -->

- We reviewed the exponential family, a principled generalization of numerous distributions, which we saw is tightly connected with the maximum entropy principle. - Importantly, the approaches described in this chapter produce perfectly valid computation graphs, meaning that we can combine them with neural networks and we can use automatic differentiation, to compute their derivatives.

<!-- chunk {"id": "body-0225", "role": "body", "section": "Parameterized programs", "weight": 1.0} -->

Neural networks can be thought of as parameterized programs: programs with learnable parameters. In this chapter, we begin by reviewing how to represent programs mathematically. We then review several key neural network architectures and components.

<!-- chunk {"id": "body-0226", "role": "body", "section": "Computation chains", "weight": 1.0} -->

To begin, we consider simple programs that apply a sequence of functions f 1,..., f K to an input s 0 ∈ S 0. We call such programs computation chains. For example, an image may go through a sequence of transformations such as cropping, rotation, normalization, and so. In neural networks, the transformations are typically parameterized, and the parameters are learned, leading to feedforward networks, presented in Section 4.2. Another example of sequence of functions is a for loop, presented in Section 5.8.

<!-- chunk {"id": "body-0227", "role": "body", "section": "Computation chains", "weight": 1.0} -->

Formally, a computation chain can be written as Here, s 0 is the input, s k ∈ S k is an intermediate state of the program, and s K ∈ S K is the final output. Of course, the domain (input space) of f k must be compatible with the image (output space) of f k -1. That is, we should have f k: S k -1 →S k. We can write a computation chain equivalently as A computation chain can be represented by a directed graph, shown in Fig. 4.1. The edges in the chain define a total order. The order is total, since two nodes are necessarily linked to each other by a path.

<!-- chunk {"id": "body-0228", "role": "body", "section": "Directed acylic graphs", "weight": 1.0} -->

In generic programs, intermediate functions may depend, not only on the previous function output, but on the outputs of several different functions. Such dependencies are best expressed using graphs.

<!-- chunk {"id": "body-0229", "role": "body", "section": "Directed acylic graphs", "weight": 1.0} -->

A directed graph G = ( V, E ) is defined by a set of vertices or nodes V and a set of edges E defining directed dependencies between vertices. An edge ( i, j ) ∈ E is an ordered pair of vertices i ∈ V and j ∈ V. It is also denoted i → j, to indicate that j depends on i. For representing inputs and outputs, it will be convenient to use incoming half-edges → j and outgoing half-edges i →.

<!-- chunk {"id": "body-0230", "role": "body", "section": "Directed acylic graphs", "weight": 1.0} -->

In a graph G = ( V, E ), the parents of a vertex j is the set of nodes pointing to j, denoted pa( j ):= { i: i → j }. The children of a vertex i is the set of nodes i is pointing to, that is, ch( i ):= { j: i → j }. Vertices without parents are called roots and vertices without children are called leaves.

<!-- chunk {"id": "body-0231", "role": "body", "section": "Directed acylic graphs", "weight": 1.0} -->

A path from i to j is defined by a sequence of vertices j 1,..., j m, potentially empty, such that i → j 1 →... → j m → j. An acyclic graph is a graph such that there exists no vertex i with a path from i to i. A directed acyclic graph (DAG) is a graph that is both directed and acyclic.

<!-- chunk {"id": "body-0232", "role": "body", "section": "Directed acylic graphs", "weight": 1.0} -->

The edges of a DAG define a partial order of the vertices, denoted i ⪯ j if there exists a path from i to j. The order is partial, since two vertices may not necessarily be linked to each other by a path. Nevertheless, we can define a total order called a topological order: any order such that i ≤ j if and only if there is no path from j to i.

<!-- chunk {"id": "body-0233", "role": "body", "section": "Computer programs as DAGs", "weight": 1.0} -->

We assume that a program defines a mathematically valid function (a.k.a. pure function): the program should return identical values for identical arguments and should not have any side effects. We also assume that the program halts, i.e., that it terminates in a finite number of steps. As such a program is made of a finite number of intermediate functions and intermediate variables, the dependencies between functions and variables can be expressed using a directed acyclic graph (DAG). Without loss of generality, we make the following simplifying assumptions: 1. There is a single input s 0 ∈ S 0. 2. There is a single output s K ∈ S K. 3. Each intermediate function f k in the program outputs a single variable s k ∈ S k.

<!-- chunk {"id": "body-0234", "role": "body", "section": "Computer programs as DAGs", "weight": 1.0} -->

We number the nodes as V:= { 0, 1,..., K }. Node 0 is the root, corresponding to the input s 0 ∈ S 0. Node K is the leaf, corresponding to the final output s K ∈ S K. Because of the third assumption above, apart from s 0, each variable s k is in bijection with a function f k. Therefore, node 0 represents the input s 0, and nodes 1,..., K represent both a function f k and an output variable s k.

<!-- chunk {"id": "body-0235", "role": "body", "section": "Computer programs as DAGs", "weight": 1.0} -->

Edges in the DAG represent dependencies. The parents i 1,..., i p k:= pa( k ) of node k, where p k:= | pa( k ) |, indicate the variables s pa ( k ):= s i 1,..., s i p k that the function f k needs to perform its computation. Put

<!-- chunk {"id": "body-0236", "role": "body", "section": "Algorithm 4.1 Executing a program", "weight": 1.0} -->

Functions: f 1,..., f K in topological order Input: input s 0 ∈ S 0 1: for k:= 1,..., K do 2: Retrieve parent nodes (i 1,..., i p k):= pa(k) 3: Compute s k:= f k (s pa(k)):= f k (s i 1,..., s i p k) 4: Output: f (s 0):= s K differently, the parents i 1,..., i p k indicate the functions f i 1,..., f i p k that need to be evaluated, prior to evaluating f k. An example of computation graph in our formalism is presented in Fig. 4.3.

<!-- chunk {"id": "body-0237", "role": "body", "section": "Executing a program", "weight": 1.0} -->

To execute a program, we need to ensure that we evaluate the intermediate functions in the correct order. Therefore, we assume that the nodes 0, 1,..., K are in a topological order (if this is not the case, we need to perform a topological sort first). We can then execute a program by evaluating for k ∈ [K] Note that we can either view f k as a single-input function of s pa(k), which is a tuple of elements, or as a multi-input function of s i 1,..., s i p k. The two views are essentially equivalent.

<!-- chunk {"id": "body-0238", "role": "body", "section": "Executing a program", "weight": 1.0} -->

The procedure for executing a program is summarized in Algorithm 4.1.

<!-- chunk {"id": "body-0239", "role": "body", "section": "Dealing with multiple program inputs or outputs", "weight": 1.0} -->

When a program has multiple inputs, we can always group them into s 0 ∈ S 0 as s 0 = ( s 0, 1,..., s 0,N 0 ) with S 0 = ( S 0, 1 ×··· × S 0,N 0 ), since later functions can always filter out what elements of s 0 they need. Likewise, if an intermediate function f k has multiple outputs, we can always group them as a single output s k = ( s k, 1,..., s k,N k ) with S k = ( S k, 1 ×··· × S k,N k ), since later functions can filter out the elements of s k that they need.

<!-- chunk {"id": "body-0240", "role": "body", "section": "Alternative representation: bipartite graphs", "weight": 1.0} -->

In our formalism, because a function f k always has a single output s k, a node k can be seen as representing both the variable s k and the function f k. Alternatively, as shown in Fig. 4.4, we can represent variables and functions as separate nodes, that is, using a bipartite graph. This formalism is akin to factor graphs used in probabilistic modeling, but with directed edges. One advantage of this formalism is that it allows functions to explicitly have multiple outputs. We focus on our formalism for simplicity.

<!-- chunk {"id": "body-0241", "role": "body", "section": "Arithmetic circuits", "weight": 1.0} -->

Arithmetic circuits are one of the simplest examples of computation graph, originating from computational complexity theory. Formally, an arithmetic circuit over a field F, such as the reals R, is a directed acyclic graph (DAG) whose root nodes are elements of F and whose functions f k are either + or ×. The latter are often called gates. Contrary to the general computation graph case, because each f k is either + or ×, it is important to allow the graph to have several root nodes. Root nodes can be either variables or constants, and should belong to F.

<!-- chunk {"id": "body-0242", "role": "body", "section": "Arithmetic circuits", "weight": 1.0} -->

Arithmetic circuits can be used to compute polynomials. There are potentially multiple arithmetic circuits for representing a given polynomial. One important question is then to find the most efficient arithmetic circuit for computing a given polynomial. To compare arithmetic circuits representing the same polynomial, an intuitive notion of complexity is the circuit size, as defined below.

<!-- chunk {"id": "body-0243", "role": "body", "section": "Arithmetic circuits", "weight": 1.0} -->

Definition 4.1 (Circuit and polynomial sizes). The size S ( C ) of a circuit C is the number of edges in the directed acyclic graph representing C. The size S ( f ) of a polynomial f is the smallest S ( C ) among all C representing f.

<!-- chunk {"id": "body-0244", "role": "body", "section": "Arithmetic circuits", "weight": 1.0} -->

For more information on arithmetic circuits, we refer the reader to the monograph of Chen et al..

<!-- chunk {"id": "body-0245", "role": "body", "section": "Feedforward networks", "weight": 1.0} -->

A feedforward network can be seen as a computation chain with for a given input and Given such a parameterized program, we can learn the parameters by adjusting w to fit some data. For instance, given a dataset of (x i, y i) pairs, we may minimize the squared loss ‖ y i -f (x i, w) ‖ 2 2 on average over the data, w.r.t. w. The minimization of such a loss requires accessing its gradients with respect to w. x ∈ X learnable parameters w 1,..., w K ∈ W 1 ×··· × W K. Each function f k is called a layer and each s k ∈ S k can be seen as an intermediate representation of the input x. The dimensionality of S k is known as the width (or number of hidden units) of layer k. A feedforward network defines a function s K =: f (x, w) from X × W to S K, where w:= (w 1,..., w K) ∈ W:= W 1 ×... ×W K.

<!-- chunk {"id": "body-0246", "role": "body", "section": "Combining affine layers and activations", "weight": 1.0} -->

In the previous section, we did not specify how to parametrize the feedforward network. A typical parametrization, called the multilayer perceptron (MLP), uses fully-connected (also called dense) layers of the form where we defined the tuple w k:= (W k, b k) and where we assumed that W k and b k are a matrix and vector of appropriate size. We can further decompose the layer into two functions. The function s ↦→ W k s + b k is called an affine layer. The function v ↦→ a k (v) is a parameter-free nonlinearity, often called an activation function (see Section 4.4). The value α k:= W k s k -1 + b k is often called the pre-activation value and the value a k (α k) is the activation value.

<!-- chunk {"id": "body-0247", "role": "body", "section": "Combining affine layers and activations", "weight": 1.0} -->

More generally, we may replace the matrix-vector product W k s k -1 by any parametrized linear function of s k -1. For example, convolutional layers use the convolution of an input s k -1 with some filters W k, seen as a linear map.

<!-- chunk {"id": "body-0248", "role": "body", "section": "Combining affine layers and activations", "weight": 1.0} -->

Remark 4.1 (Dealing with multiple inputs). Sometimes, it is necessary to deal with networks of multiple inputs. For example, suppose we want to design a function g ( x 1, x 2, w g ), where x 1 ∈ X 1 and x 2 ∈ X 2. A simple way to do so is to use the concatenation x:= x 1 ⊕ x 2 ∈ X 2 ⊕X 2 as input to a network f ( x, w f ). Alternatively, instead of concatenating x 1 and x 2 at the input layer, they can be concatenated after having been through one or more hidden layers.

<!-- chunk {"id": "body-0249", "role": "body", "section": "Link with generalized linear models", "weight": 1.0} -->

When the depth is K = 1 (only one layer), the output of an MLP is This is called a generalized linear model (GLM); see Section 3.4. Therefore, MLPs include GLMs as a special case. In particular, when a 1 is the softargmax (see Section 4.4), we obtain (multiclass) logistic regression. For general depth K, the output of an MLP is This can be seen as a GLM on top of learned representation s K -1 of the input x. This is the main appeal of MLPs: they learn the feature representation and the output model at the same time! We will see that MLPs can also be used as subcomponents in other architectures.

<!-- chunk {"id": "body-0250", "role": "body", "section": "Activation functions", "weight": 1.0} -->

As we saw in Section 4.3, feedforward networks typically use an activation function a k at each layer. In this section, we present various nonlinearities from scalar to scalar or from vector to scalar. We also present probability mappings that can be used as such activations.

<!-- chunk {"id": "body-0251", "role": "body", "section": "ReLU and softplus", "weight": 1.0} -->

Many activations are scalar-to-scalar functions, but they can also be applied to vectors in an element-wise fashion. The ReLU (rectified linear unit) is a popular nonlinearity defined as the non-negative part of its input It is a piecewise linear function and includes a kink at u = 0. A multilayer perceptron with ReLU activations is called a rectifier neural network. The layers take the form where the ReLU is applied element-wise. The ReLU can be replaced with a smooth approximation (i.e., without kinks), called the softplus Unlike the ReLU, it is always strictly positive. Other smoothed variants of the ReLU are possible, see Section 13.4.

<!-- chunk {"id": "body-0252", "role": "body", "section": "Max pooling and log-sum-exp", "weight": 1.0} -->

Many activations are vector-to-scalar functions: they reduce vectors to a scalar value. This scalar value can be seen as a statistic, 'summarizing' the vector.

<!-- chunk {"id": "body-0253", "role": "body", "section": "Max pooling", "weight": 1.0} -->

An example of vector-to-scalar reduction is the maximum value, also known as max pooling. Given a vector u ∈ R M, it is defined as

<!-- chunk {"id": "body-0254", "role": "body", "section": "Log-sum-exp as a soft maximum", "weight": 1.0} -->

Another example of vector-to-scalar reduction is the log-sum-exp, As illustrated in Fig. 4.5, it is known to behave like a soft maximum. The log-sum-exp can be seen as a generalization of the softplus, as we have for all u ∈ R A numerically stable implementation of the log-sum-exp is given by More generally, we can introduce a temperature parameter γ > 0 It can be shown that for all u ∈ R M, Therefore, logsumexp γ (u) → max(u) as γ → 0. Other definitions of soft maximum are possible; see Section 13.5.

<!-- chunk {"id": "body-0255", "role": "body", "section": "Log-sum-exp as a log-domain sum", "weight": 1.0} -->

Besides its use as a soft maximum, the log-sum-exp often arises for computing sums in the log domain. Indeed, suppose we want to compute s:= ∑ j M =1 u i, where u i > 0. If we define ˜ u i:= log u i and ˜ s:= log s, we then have Written differently, we have the identity We can therefore see the log-sum-exp as the sum counterpart of the identity for products As an example, we use the log-sum-exp to perform the forward-backward algorithm in the log-domain in Section 10.7.1.

<!-- chunk {"id": "body-0256", "role": "body", "section": "Sigmoids: binary step and logistic functions", "weight": 1.0} -->

Oftentimes, we want to map a real value to a number, that can represent the probability of an event. For that purpose, we generally use sigmoids. A sigmoid is a function with a characteristic 'S'-shaped curve. These functions are scalar-to-scalar probability mappings: they are used to squash real values to.

<!-- chunk {"id": "body-0257", "role": "body", "section": "Binary step function", "weight": 1.0} -->

An example is the binary step function, also known as Heaviside step function, It is a mapping from R to { 0, 1 }. Unfortunately, it has a discontinuity: a jump in its graph at u = 0. Moreover, because the function is constant at all other points, it has zero derivative at these points, which makes it difficult to use as part of a neural network trained with backpropagation.

<!-- chunk {"id": "body-0258", "role": "body", "section": "Logistic function", "weight": 1.0} -->

A better sigmoid is the logistic function, which is a mapping from R to and is defined as It maps (-∞, 0) to (0, 0. 5),[0, + ∞) to [0. 5, 1) and it satisfies logistic = 0. 5. It can therefore be seen as mapping from real values to probability values. The logistic can be seen as a differentiable approximation to the discontinuous binary step function step(u). The logistic function can be shown to be the derivative of softplus, i.e., for all u ∈ R Two important properties of the logistic function are that for all u ∈ R Other sigmoids are possible; see Section 13.6.

<!-- chunk {"id": "body-0259", "role": "body", "section": "Probability mappings: argmax and softargmax", "weight": 1.0} -->

It is often useful to transform a real vector into a vector of probabilities. This is a mapping from R M to the probability simplex, defined by Two examples of such vector-to-vector probability mappings are the argmax and the softargmax.

<!-- chunk {"id": "body-0260", "role": "body", "section": "Argmax", "weight": 1.0} -->

The argmax operator is defined by where φ (j) denotes the one-hot encoding of an integer j ∈ [M], that is, This mapping puts all the probability mass onto a single coordinate (in case of ties, we pick a single coordinate arbitrarily). Unfortunately, this mapping is a discontinuous function.

<!-- chunk {"id": "body-0261", "role": "body", "section": "Softargmax", "weight": 1.0} -->

As a differentiable everywhere relaxation, we can use the softargmax defined by This operator is commonly known in the literature as softmax but this is a misnomer: this operator really defines a differentiable relaxation of the argmax. The output of the softargmax belongs to the relative interior of the probability simplex relint(△ M) = { π ∈ △ M: π > 0 }, meaning that it can never reach the borders of the simplex. If we denote π = softargmax(u), this means that π j ∈, that is, π j can never be exactly 0 or 1. The softargmax is the gradient of log-sum-exp, The softargmax can be seen as a generalization of the logistic function, as we have for all u ∈ R Remark 4.2 (Degrees of freedom and invertibility of softargmax). The softargmax operator satisfies the property for all u ∈ R M and c ∈ R This means that the softargmax operator has M -1 degrees of freedom and is a non-invertible function.

<!-- chunk {"id": "body-0262", "role": "body", "section": "Softargmax", "weight": 1.0} -->

However, due to the above property, without loss of generality, we can impose u ⊤ 1 = ∑ i M =1 u i = 0 (if this is not the case, we simply do u i ← u i -¯ u, where ¯ u:= 1 M ∑ j M =1 u j). Using this constraint together with

<!-- chunk {"id": "body-0263", "role": "body", "section": "Normalization layers", "weight": 1.0} -->

Intermediate states in neural networks, such as activations, can often attain a wide range of different values, potentially making it difficult for gradient descent to converge. To remedy this issue, we can introduce normalization layers at suitable locations in the network. In this section, we present the two most popular ones: batch normalization and layer normalization.

<!-- chunk {"id": "body-0264", "role": "body", "section": "Batch normalization", "weight": 1.0} -->

Suppose we are given a batch of intermediate variables (such as activations or states) s 1,..., s B ∈ R D, where s i:= (s i, 1,..., s i,D), obtained by applying some function to B samples drawn from the training set (we omit the dependency on the layer index k for clarity). In batch normalization, we normalize the values by calculating the standard score (a.k.a. z-score) across batch samples, Here, the means µ j and the standard deviations σ j are computed for each feature j ∈ [D] across samples i ∈ [B] in the batch. In practice, we often add a small value ε > 0 to σ j to avoid division by zero or numerical instabilities. Moreover, we often rescale the values as where the means β:= (β 1,..., β D) and standard deviations γ:= (γ 1,..., γ D) are learnable parameters.

<!-- chunk {"id": "body-0265", "role": "body", "section": "Batch normalization", "weight": 1.0} -->

One issue with batch normalization is that the means µ j and standard deviations σ j cannot be computed at inference time, as there is no notion of training batch (a single sample would lead to a variance of 0). To address this issue, we can estimate means ̂ µ j and standard deviations ̂ σ j across the whole training set during the course of training, usually using a running average. A pratical batch normalization implementation therefore needs to maintain D mean and standard deviation statistics, so as to be able to use them at inference time.

<!-- chunk {"id": "body-0266", "role": "body", "section": "Layer normalization", "weight": 1.0} -->

As an alternative, in layer normalization, we instead standardize the values by summing across features, This time, the means and the standard deviations are computed] (as before, we often add). Similarly to batch normalization, we often rescale µ i σ i for each sample i ∈ [B] across features j ∈ [D a small value ε to σ i the values as where the means β:= (β 1,..., β D) and standard deviations γ:= (γ 1,..., γ D) are learnable parameters. A key advantage of layer normalization compared to batch normalization is that it is well defined at inference time, since it is applied on a per-sample basis and does not rely on the notion of training batch. As a result, we can view layer normalization as a function that to any s i ∈ R D (regardless of whether it is part of a batch or not) associates

<!-- chunk {"id": "body-0267", "role": "body", "section": "Residual neural networks", "weight": 1.0} -->

We now discuss another feedforward network parametrization: residual neural networks. Consider a feedforward network with K + 1 layers f 1,..., f K, f K +1. Surely, as long as f K +1 can exactly represent the identity function, the set of functions that this feedforward network can express should be a superset of the functions that f 1,..., f K can express. In other words, depth should in theory not hurt the expressive power of feedforward networks. Unfortunately, the assumption that each f k can exactly represent the identity function may not hold in practice. This means that deeper networks can sometimes be more difficult to train than shallower ones, making the accuracy saturate or degrade as a function of depth.

<!-- chunk {"id": "body-0268", "role": "body", "section": "Residual neural networks", "weight": 1.0} -->

The key idea of residual neural networks is to design layers f k, called residual blocks, that make it easier to represent the identity function. Formally, a residual block takes the form The function h k is called residual, since it models the difference s k -s k -1. The addition with s k -1 is often called a skip connection. As long as it is easy to adjust w k so that h k (s k -1, w k) = 0, f k can freely become the identity function. For instance, if we use where w k:= (W k, b k, C k, d k), it suffices to set C k and d k to a zero matrix and vector. Residual blocks are known to remedy the so-called vanishing gradient problem.

<!-- chunk {"id": "body-0269", "role": "body", "section": "Residual neural networks", "weight": 1.0} -->

Many papers and software packages include an additional activation and instead define the residual block as where a k is typically chosen to be the ReLU activation. Whether to include this additional activation or not is essentially a modelling choice. In practice, residual blocks may also include additional operations such as batch norm and convolutional layers.

<!-- chunk {"id": "body-0270", "role": "body", "section": "Recurrent neural networks", "weight": 1.0} -->

Recurrent neural networks (RNNs) are a class of neural networks that operate on sequences of vectors, either as input, output or both. Their actual parametrization depends on the setup but the core idea is to maintain a state vector that is updated from step to step by a recursive function that uses shared parameters across steps. Unrolling this recursion defines a valid computational graph, as we will see in Chapter 8. We distinguish between the following setups illustrated in Fig. 4.7:

<!-- chunk {"id": "body-0271", "role": "body", "section": "Recurrent neural networks", "weight": 1.0} -->

- Vector to sequence (one to many): f d: R D × R P → R L × M - Sequence to vector (many to one): f e: R L × D × R P → R M - Sequence to sequence (many to many, aligned): f a: R L × D × R P → R L × M - Sequence to sequence (many to many, unaligned): f u: R L × D × R P → R L ′ × M where L stands for length. Note that we use the same number of parameters P for each setup for notational convenience, but this of course does not need to be the case. Throughout this section, we use the notation p 1: L:= (p 1,..., p L) for a sequence of L vectors.

<!-- chunk {"id": "body-0272", "role": "body", "section": "Vector to sequence", "weight": 1.0} -->

In this setting, we define a decoder function p 1: L = f d (x, w) from an input vector x ∈ R D and parameters w ∈ R P to an output sequence p 1: L ∈ R L × M. This is for instance useful for image caption generation, where a sentence (a sequence of word embeddings) is generated from an image (a vector of pixels). Formally, we may define p 1: L:= f d (x, w) through the recursion Figure 4.7: Recurrent neural network architectures where w:= (w g, w h, z 0). The goal of g is to update the current decoder state z l given the input x, and the previous decoder state z l -1. The goal of h is to generate the output p l given the current decoder state z l. Importantly, the parameters of g and h are shared across steps. Typically, g and h are parametrized using one-hidden-layer MLPs. Note that g has multiple inputs; we discuss how to deal with such cases in Section 4.3.

<!-- chunk {"id": "body-0273", "role": "body", "section": "Sequence to vector", "weight": 1.0} -->

In this setting, we define an encoder function p = f e (x 1: L, w) from an input sequence x 1: L ∈ R L × D and parameters w ∈ R P to an output vector p ∈ R M. This is for instance useful for sequence classification, such as sentiment analysis. Formally, we may define p:= f e (x 1: L, w) using the recursion where w:= (w g, s 0). The goal of γ is similar as g, except that it updates encoder states and does not take previous predictions as input. The pooling function is typically parameter-less. Its goal is to reduce a sequence to a vector. Examples include using the last state, the average of states and the coordinate-wise maximum of states.

<!-- chunk {"id": "body-0274", "role": "body", "section": "Sequence to sequence (aligned)", "weight": 1.0} -->

In this setting, we define a function p 1: L = f a ( x 1: L, w ) from an input sequence x 1: L ∈ R L × D and parameters w ∈ R P to an output sequence p 1: L ∈ R L × M, which we assume to be of the same length. An example of application is part-of-speech tagging, where the goal is to assign each word x l to a part-of-speech (noun, verb, adjective, etc).

<!-- chunk {"id": "body-0275", "role": "body", "section": "Sequence to sequence (aligned)", "weight": 1.0} -->

Formally, we may define p 1: L = f a (x 1: L, w) as where w:= (w γ, w h, s 0). The function γ and h are similar as before.

<!-- chunk {"id": "body-0276", "role": "body", "section": "Sequence to sequence (unaligned)", "weight": 1.0} -->

In this setting, we define a function p 1: L ′ = f u (x 1: L, w) from an input sequence x 1: L ∈ R L × D and parameters w ∈ R P to an output sequence p 1: L ′ ∈ R L ′ × M, which potentially has a different length. An example of application is machine translation, where the sentences in the source and target languages do not necessarily have the same length. Typically, p 1: L ′ = f u (x 1: L, w) is defined as the following two steps where w:= (w e, w d), and where we reused the previously-defined encoder f e and decoder f d. Putting the two steps together, we obtain This architecture is aptly named the encoder-decoder architecture. Note that we denoted the length of the target sequence as L ′. However, in practice, the target length can be input dependent and is often not known ahead of time. To deal with this issue, the vocabulary (of size D is our notation) is typically augmented with an 'end of sequence' (EOS) token so that, at inference time, we know when to stop generating the output sequence.

<!-- chunk {"id": "body-0277", "role": "body", "section": "Sequence to sequence (unaligned)", "weight": 1.0} -->

One disadvantage of this encoder-decoder architecture, however, is that all the information about the input sequence is contained in the context vector c, which can therefore become a bottleneck.

<!-- chunk {"id": "body-0278", "role": "body", "section": "Transformers", "weight": 1.0} -->

Transformers are one of the most successful recent developments in deep learning. In this section, we review Transformers, component by component.

<!-- chunk {"id": "body-0279", "role": "body", "section": "Attention", "weight": 1.0} -->

The goal of an attention layer is to map a sequence of inputs v 1,..., v L ∈ R D v to a sequence of outputs u 1,..., u L ∈ R D v, of same dimension. A natural idea is to define each output element u i using a linear combination of the input elements, We typically use a convex combination: we assume that the combination weights are such that a i:= (a i, 1,..., a i,L) ∈ △ L. This ensures that increasing a coefficient a i,j is made at the expense of decreasing another coefficient a i,j ′, for j = j ′. Let us form the matrices V ∈ R L × D v and U ∈ R L × D v by stacking v 1,..., v L and u 1,..., u L, seen as row vectors. Let us also form the attention matrix A ∈ △ L × L gathering the entries a i,j, where △ L × L denotes the set of row-wise stochastic L × L matrices.

<!-- chunk {"id": "body-0280", "role": "body", "section": "Attention", "weight": 1.0} -->

Then, we can rewrite attention succinctly as Following Section 6.2, we can view attention as a soft dictionary lookup. From this perspective, the matrix V ∈ R L × D v plays the role of dictionary values, and the attention matrix can be defined as where Q ∈ R L × D k and K ∈ R L × D k play the roles of queries and dictionary keys, respectively. Intuitively, QK ⊤ ∈ R L × L can be seen as a similarity matrix containing the similarities between queries and dictionary keys. Putting everything together, we can define attention as In masked attention, we additionally incorporate a mask M ∈ R L × L, where ◦ denotes the Hadamard product (element-wise multiplication). The mask can be used to force some attention weights a i,j to be zero, by setting the corresponding mask entry m i,j to -∞. For instance, in decoder-only architectures (Section 4.8.8), the mask will prove useful to define causal attention for autoregressive models.

<!-- chunk {"id": "body-0281", "role": "body", "section": "Attention", "weight": 1.0} -->

Remark 4.3 (Scaled attention). Practical implementations often use scaled attention, where a factor of 1 √ D k is used within the softargmax, in order to reduce the variance. We omit this detail for clarity.

<!-- chunk {"id": "body-0282", "role": "body", "section": "Self-attention", "weight": 1.0} -->

Suppose we are given a sequence of feature vectors x 1,..., x L ∈ R D, that we gather as a matrix X ∈ R L × D. To define the attention weights a i,j, a natural idea is to consider the similarity between x i and x j, as measured by the inner product 〈 x i, x j 〉. To ensure that a i:= (a i, 1,..., a i,L) ∈ △ L, we can then define In matrix notation, this can be written where softargmax is applied in a row-wise fashion. The matrix XX ⊤ ∈ R L × L is the Gram matrix associated with the row vectors x 1,..., x L. In the notation of the previous section, this corresponds to using Attention(Q, K, V) with Q = K = V = X. In other words, the elements of the sequence 'pay attention' to each other. This is called self-attention.

<!-- chunk {"id": "body-0283", "role": "body", "section": "Self-attention", "weight": 1.0} -->

So far, the formulation we described is parameter-free. To give more expressive power to the self-attention layer, Vaswani et al. proposed instead to define Q, K and V by projecting X as using the learned weight matrices Importantly, the size of the weight matrices is independent of the length L of the sequences. This allows self-attention to work with sequence of arbitrary length.

<!-- chunk {"id": "body-0284", "role": "body", "section": "Multi-head attention", "weight": 1.0} -->

In order to be able capture multiple patterns of attention, Vaswani et al. found it beneficial to define H attention heads using the learned weight matrices Let us denote the concatenation of the H attention heads by

<!-- chunk {"id": "body-0285", "role": "body", "section": "Algorithm 4.2 Multi-head attention with H attention heads", "weight": 1.0} -->

Input: X ∈ R L × D, optional mask M ∈ R L × L Vaswani et al. then define multi-head attention as where W O ∈ R HD v × D is a learned matrix. We summarize the procedure in Algorithm 4.2. We use a for loop for the sake of clarity; a GPUfriendly implementation would instead be based on a single matrix multiplication.

<!-- chunk {"id": "body-0286", "role": "body", "section": "Transformer layer", "weight": 1.0} -->

To improve training efficiency, we can introduce residual connections and a first layer normalization (Section 4.5.2), to define To improve expressiveness, a Transformer layer furthers uses an MLP and a second layer normalization, The subscripts in LayerNorm are used to emphasize that the two layers use their own parameters. In addition, normalization is applied in an

<!-- chunk {"id": "body-0287", "role": "body", "section": "Algorithm 4.3 Transformer's MLP block", "weight": 1.0} -->

Input: Z ∈ R L × D Parameters: W 1 ∈ R D × D 1, W 2 ∈ R D 1 × D 1: Z ← ZW 1 ∈ R L × D 1 2: Z ← σ (Z) ∈ R L × D 1 3: Z ← ZW 2 ∈ R L × D Output: Z ∈ R L × D element-wise (token-wise) fashion. The MLP block typically uses a single hidden layer with an activation function σ, such as a GELU (Gaussian error linear unit); see Algorithm 4.3. Because of the use of residual connections, the input and output dimensions of the MLP block must be the same.

<!-- chunk {"id": "body-0288", "role": "body", "section": "Algorithm 4.3 Transformer's MLP block", "weight": 1.0} -->

Remark 4.4 (Post-normalization vs. pre-normalization). Our description of the Transformer layer follows the original formulation, which uses post-normalization. Some implementations instead rely on pre-normalization, that is, Z:= MultiheadAttention(LayerNorm 1 (X); M) + X ∈ R L × D X ← MLP(LayerNorm 2 (Z)) + Z ∈ R L × D.

<!-- chunk {"id": "body-0289", "role": "body", "section": "Transformer block", "weight": 1.0} -->

A Transformer layer can be iterated K times (each time with different parameters) to define a Transformer block of depth K. Keeping the dependency on parameters implicit, we can see a Transformer, with an optional mask M ∈ R L × L, as a function from R L × D to R L × D. The Transformer takes a sequence X ∈ R L × D and uses the inter-dependencies between sequence elements to produce a representation of that sequence. We summarize the procedure in Algorithm 4.4. The MultiheadAttention, LayerNorm and MLP blocks are indexed by k to emphasize that their parameters are different for each iteration.

<!-- chunk {"id": "body-0290", "role": "body", "section": "Algorithm 4.4 Transformer block of depth K", "weight": 1.0} -->

Input: X ∈ R L × D optional mask M ∈ R L × L Parameters: Multi-head attention parameters, MLP parameters and layer norm parameters (each depth k uses different parameters) 3: Z:= LayerNorm k, 1 (Y + X) ∈ R L × D ▷ Residual connection 4: X ← LayerNorm k, 2 (MLP k (Z) + Z) ∈ R L × D ▷ MLP layer

<!-- chunk {"id": "body-0291", "role": "body", "section": "Number of parameters and computational complexity", "weight": 1.0} -->

The Transformer layer can be seen as a function from R L × D to R L × D. To offer the same function signature, a standard multi-layer perceptron would have needed O ( N 2 D 2 ) parameters and a forward pass through the network would have had a time complexity of O ( N 2 D 2 ) as well. In contrast, a Transformer layer has O ( D 2 ) parameters. Self-attention has a complexity of O ( N 2 D ) and the final MLP layer has a complexity of O ( ND 2 ).

<!-- chunk {"id": "body-0292", "role": "body", "section": "Token encoding", "weight": 1.0} -->

Text can be represented as a sequence x 1,..., x L of discrete symbols, often called tokens. Here, each token x i ∈ [M], where M is the vocabulary size, can correspond to words, subwords, or even individual characters, depending on the tokenization procedure. To obtain a sequence of continuous vectors x 1,..., x L, where x i ∈ R D, it is common to use an embedding layer. This layer transforms x i ∈ [M] into x i ∈ R D using the linear projection where e j ∈ R M is the one-hot encoding of j ∈ [M] and W E ∈ R D × M is a learnable embedding matrix. The column W E:,j ∈ R D can be interpreted as the continuous representation of token j ∈ [V]. Usually, the vocabulary includes special tokens such as 'BOS' (beginning of sequence), 'EOS' (end of sequence) and 'PAD' (padding token, to ensure that the sequence is of length L).

<!-- chunk {"id": "body-0293", "role": "body", "section": "Positional encoding", "weight": 1.0} -->

Due to their parameterization, Transformers are equivariant with respect to permutations: permuting the input sequence and applying the Transformer is equivalent to applying the Transformer and permuting the output sequence. Formally, for any permutation matrix P of size L × L and input sequence x 1,..., x L seen as a matrix X, we have This means that Transformers treat an ordered sequence as a multi-set (a modification of the concept of a set that allows for multiple instances of its elements). To leverage order information in a Transformer, several approaches are possible: adding positional encoding (either absolute or relative), modifying the attention matrix and preprocessing the input sequence with an RNN. To add positional encoding, one typically adds a vector p i ∈ R D representing the position i ∈ [L] to the corresponding element x i ∈ R D, An ideal positional encoding should work with any sequence length.

<!-- chunk {"id": "body-0294", "role": "body", "section": "Learned positional encoding", "weight": 1.0} -->

Similarly to the token encoding, a simple way to define a positional encoding is to use an embedding layer. Each position i ∈ [L] is transformed into a position vector p i ∈ R D by where e i ∈ R L is the one-hot encoding of i ∈ [L] and W P ∈ R D × L is a learnable embedding matrix. The column W P:,i ∈ R D can be interpreted as the continuous representation of position i ∈ [L].

<!-- chunk {"id": "body-0295", "role": "body", "section": "Sinusoidal positional encoding", "weight": 1.0} -->

Instead of learning the positional encoding, we can define it in a heuristic manner. For instance, Vaswani et al. proposed the sinusoidal positional encoding p i:= (p i, 1,..., p i,D), defined by and where N is a constant, set to N:= 10000 by the authors. We can gather the values in a position encoding matrix P ∈ R L × D, as depicted in Fig. 4.8.

<!-- chunk {"id": "body-0296", "role": "body", "section": "Sinusoidal positional encoding", "weight": 1.0} -->

On first sight, sinusoidal positional encoding may seem a bit mysterious. To gain some intuition, it is useful to compare it to a discrete binary encoding of integers, We see that the bits alternate more frequently between 0 and 1 as we go from right to left. The sinusoidal positional encoding achieves a similar behavior, but is continuous. Indeed, each coordinate j ∈ [D] is associated with a sine wave (when j is even) or a cosine wave (when j is odd). The wavelength or period of the wave associated with j is 2 π ω j and its frequency is ω j 2 π. Since ω j is a decreasing function of j, we see that the waves oscillate more frequently when j is small. This behavior is illustrated in Fig. 4.9.

<!-- chunk {"id": "body-0297", "role": "body", "section": "Sinusoidal positional encoding", "weight": 1.0} -->

Stacking sine and cosine waves has been used for creating random Fourier features. These use waves of random frequencies, while sinusoidal positional encoding uses waves of increasing frequency. These approaches therefore mainly differ in the way we choose wave frequencies.

<!-- chunk {"id": "body-0298", "role": "body", "section": "Recovering relative positional information", "weight": 1.0} -->

An important property of the sinusoidal positional encoding is that p i + δ can be represented as a linear function of p i, for any offset δ. The model should therefore be able to easily learn to attend by relative positions. Indeed, using the trigonometric identities for angle sums Figure 4.9: Using a sinusoidal positional encoding, each coordinate j ∈ [D] is associated with a sine or cosine wave. In analogy with a binary encoding, in which lower bits alternate between 0 and 1 more frequently than higher bits, the wave associated with j oscillates more frequently when j is small. we have for j even Therefore, (p i,j +1, p i,j) can be linearly projected to (p i + δ,j +1, p i + δ,j), by applying a rotation matrix. This allows a Transformer to easily learn to attend by relative positions.

<!-- chunk {"id": "body-0299", "role": "body", "section": "Rotary positional encoding (RoPE)", "weight": 1.0} -->

Another popular approach for taking into account absolute positional information in self-attention is RoPE, which stands for rotary positional encoding. For simplicity, we briefly explain the idea with a single attention head and D v = D k = D. Suppose we have a sequence x 1,..., x L ∈ R D already encoded with token encoding. We then define the query and key vectors as where R D (θ, m) ∈ R D × D is a rotation matrix. The main intuition is that we are rotating the 2-dimensional vector by an angle which is a multiple of the position m. In contrast to the learned and sinusoidal positional encodings, the weight matrices W Q and W K are applied before applying RoPE, not after.

<!-- chunk {"id": "body-0300", "role": "body", "section": "Rotary positional encoding (RoPE)", "weight": 1.0} -->

When D = 2, R D (θ, m) = R 2 (θ, m) is defined as the rotation matrix for some angle θ ∈ R and position m ∈ [L]. Using Euler's formula we note that v ′:= R 2 (θ, m) v for v = (v 1, v 2) ∈ R 2 and v ′ = (v ′ 1, v ′ 2) ∈ R 2 is equivalent to z ′:= ze imθ for z:= v 1 + iv 2 ∈ C and z ′ = v ′ 1 + iv ′ 2 ∈ C. See Su et al. for a detailed derivation of RoPE's formula.

<!-- chunk {"id": "body-0301", "role": "body", "section": "Rotary positional encoding (RoPE)", "weight": 1.0} -->

When D > 2, assuming D is even, R D (θ, m) is defined as where θ j:= 10000 -2(j -1) /D. In practice, we never materialize R D (θ, m) as a matrix, since it would be very sparse, but rather view it as a linear map applied to an arbitrary vector v ∈ R D, Once we computed Q and K, we can use Attention(Q, K, V; M) as usual. For multi-head attention, we simply apply the same approach for each attention head.

<!-- chunk {"id": "body-0302", "role": "body", "section": "Rotary positional encoding (RoPE)", "weight": 1.0} -->

As analyzed by Su et al., RoPE satisfies several valuable properties. In particular, it is flexible w.r.t. the sequence length L and despite being an absolute encoding, it manages to also capture relative distance between tokens. It therefore has the merits of both absolute and relative positional encodings.

<!-- chunk {"id": "body-0303", "role": "body", "section": "Defining a language model", "weight": 1.0} -->

Transformers were originally developed to create encoder-decoder architectures for machine translation. However, in the context of language modelling, Transformers are now routinely used for decoder-only autoregressive architectures. Suppose we are given a sequence of discrete symbols x 1,..., x L ∈ [M] (if a sequence has less than L elements, we can use padding symbols). The goal of (unconditional) language models is to create a function producing the joint probability, Using the chain rule of probability (Section 10.1), without loss of generality, we can write If the maximum length L is very large, it is more pratical to only consider a context window of size N, This amounts to defining a higher-order Markov chain (Section 10.4.3).

<!-- chunk {"id": "body-0304", "role": "body", "section": "Defining a language model", "weight": 1.0} -->

Using this approach, creating a language model then boils down to defining a function Let us assume that the sequence of discrete symbols x 1,..., x L ∈ [M] has been mapped to a sequence of continuous vectors x 1,..., x L ∈ R D using token encoding (Section 4.8.6) and positional encoding (Section 4.8.7). Using a causal Transformer block, we can obtain a representation of the current context, To ensure that the Transformer only relies on past tokens to predict the current token, the mask matrix M N is set to a triangular matrix of size N × N, with the elements of the lower part set to 1, and the elements of the upper part set to -∞. To reduce this to logits in R M, we usually use the last element of the context x k -1 ∈ R D and apply a linear model, to obtain where W D ∈ R M × D is a learned 'disembedding' matrix. To obtain a valid probability distribution, we apply a soft-argmax on the logits θ k, Finally, we can now define Remark 4.5 (Weight tying).

<!-- chunk {"id": "body-0305", "role": "body", "section": "Defining a language model", "weight": 1.0} -->

Instead of learning a separate disembedding matrix W D ∈ R M × D, a frequently used technique is to set W D:= (W E) ⊤, where W E ∈ R D × M is the embedding matrix from Section 4.8.6. This weight tying reduces the number of parameters to learn and is shown to work well in practice.

<!-- chunk {"id": "body-0306", "role": "body", "section": "Training", "weight": 1.0} -->

Let us gather the Transformer parameters (multi-head attention, MLP, layer norm) as w ∈ R P. The decoder-only Transformer with a context window of size N then defines a parametric probability distribution Given a corpus of sequences D, we usually seek the parameters w ∈ R P by maximizing the log-likelihood, This amounts to using a logistic (cross-entropy) loss in a token-wise fashion. Importantly, the context x k -N,..., x k -1 used to predict the next token x k always comes from the data, not from the tokens generated by the model. This is called teacher forcing and makes Transformer training highly parallelizable. The objective is usually solved approximately using stochastic gradient algorithms. To maximize GPU utilization, sequences of variable lengths are usually packed together in order to form batches.

<!-- chunk {"id": "body-0307", "role": "body", "section": "Sampling", "weight": 1.0} -->

A decoder-only Transformer with a context window of size N can be seen as forming a higher-order Markov chain, which is a special case of Bayesian network. To generate a sequence from the model, we can therefore use ancestral sampling (Section 10.5.3), where x 0 denotes the beginning-of-sequence (BOS) token. The sampling stops when the end-of-sequence (EOS) token is generated or when a maximum length is reached. The generated sequences are i.i.d.

<!-- chunk {"id": "body-0308", "role": "body", "section": "Sampling", "weight": 1.0} -->

Because sampling happens one token at a time, it is highly sequential.

<!-- chunk {"id": "body-0309", "role": "body", "section": "Sampling", "weight": 1.0} -->

The Transformer block is called sequentially as To avoid repeating the same computations again and again, assuming that a causal mask is used, the past key and value matrices used in multi-head attention (Section 4.8.3) are usually stored in the so-called KV cache.

<!-- chunk {"id": "body-0310", "role": "body", "section": "Encoder-only architectures", "weight": 1.0} -->

Encoder-only Transformers can be used for learning to represent sequences. The most prominent example is BERT, which stands for bidirectional encoder representations from transformers. BERT uses Algorithm 4.4 without causal mask (hence 'bidirectional' in the acronym). Discrete sequence elements are transformed to vectors using token encoding, positional encoding and potentially segment encoding. For reasons that will become clear below, the first token of every sequence is always a special classification token [CLS]. Training is broken down into two phases: pretraining and finetuning.

<!-- chunk {"id": "body-0311", "role": "body", "section": "Pretraining", "weight": 1.0} -->

Since pre-training is performed on an unlabeled corpus, it is necessary to synthetically generate prediction tasks.

<!-- chunk {"id": "body-0312", "role": "body", "section": "Pretraining", "weight": 1.0} -->

In masked prediction, a percentage (typically 15%) of the input tokens are randomly masked. The model is then trained to predict the original vocabulary ID of the masked tokens, given the context provided by the unmasked tokens. This forces the model to learn a rich, bidirectional representation of the language.

<!-- chunk {"id": "body-0313", "role": "body", "section": "Pretraining", "weight": 1.0} -->

- 80% of the time, replacing the chosen token with [MASK], - 10% of the time, replacing the chosen token with a random token from the vocabulary,

<!-- chunk {"id": "body-0314", "role": "body", "section": "Pretraining", "weight": 1.0} -->

- 10% of the time, keeping the chosen token unchanged.

<!-- chunk {"id": "body-0315", "role": "body", "section": "Pretraining", "weight": 1.0} -->

In next sentence prediction, the model is trained to understand the relationship between two sentences. For each training example, BERT is given two sentences, A and B. 50% of the time, B is the actual next sentence that follows A in the original document (labeled IsNext). The other 50% of the time, B is a random sentence from the corpus (labeled NotNext). A special [CLS] token is prepended to the input sequence, and its final hidden state is used to predict whether sentence B follows sentence A. The [SEP] token separates the two sentences.

<!-- chunk {"id": "body-0316", "role": "body", "section": "Finetuning", "weight": 1.0} -->

After pre-training on a massive corpus, the pretrained BERT model can be finetuned for various downstream NLP tasks (e.g., text classification, question answering, named entity recognition) by adding a small, taskspecific output layer on top of the pre-trained Transformer encoder. The entire model, including the pretrained weights, is then finetuned on the labeled data for the specific task. For classification tasks, the final hidden state corresponding to the class token [CLS] is used. For tagging tasks (token-level classification) such as named entity recognition (NER) or part-of-speech (POS) tagging, the final hidden state of each token is used. For question answering tasks, which usually involve finding a span (start and end token) within a given text, this is treated as two token-level classification problems: one for the start token and one for the end token.

<!-- chunk {"id": "body-0317", "role": "body", "section": "Encoder-decoder architectures", "weight": 1.0} -->

The encoder-decoder architecture was the original architecture proposed in the seminal Transformer paper. It can be used for sequence-to-sequence tasks, such as machine translation, summarization and question answering. We denote the input sequence by X and the output sequence by Y.

<!-- chunk {"id": "body-0318", "role": "body", "section": "Encoder", "weight": 1.0} -->

The role of the encoder is to produce a rich representation H enc of the input sequence X, which serves as a context for the subsequent decoding phase. As in encoder-only architectures, this is achieved by using Algorithm 4.4 without causal mask. The multi-head self-attention layer allows the encoder to weigh the importance of different tokens in the input sequence relative to each other. For each token in the input, it computes a representation that incorporates information from all other tokens in the same sequence. The encoder block uses its own parameters for each sub-component (multi-head attention, layer norm, MLP). In particular, multi-head attention uses parameters { W Q i } H i =1, { W i K } H i =1, { W V i } H i =1 and W O.

<!-- chunk {"id": "body-0319", "role": "body", "section": "Decoder", "weight": 1.0} -->

The role of the decoder is to generate the output sequence Y one token at a time, based on the encoded representation H enc from the encoder and the previously generated tokens Y 1: t -1. The decoder differs in the way attention is applied. First, we apply causal multi-head self-attention to obtain a representation H dec corresponding to the previously generated tokens Y 1: t -1. Second, we apply multi-head cross-attention. The key difference with multi-head self-attention is that the key, query and value matrices are defined as where { W ′ Q i } H i =1, { W ′ K i } H i =1 and { W ′ V i } H i =1 are the weight matrices used for the decoder. Subsequently, MLP and layer norm layers are applied, similarly as before.

<!-- chunk {"id": "body-0320", "role": "body", "section": "Differences with decoder-only architectures", "weight": 1.0} -->

An encoder-decoder architecture provides a dedicated component for understanding the input and another for generating the output. It allows for a bidirectional understanding of the input. It is therefore best suited for sequence-to-sequence (seq2seq) tasks where the input and output sequences may have different domains or modalities.

<!-- chunk {"id": "body-0321", "role": "body", "section": "Differences with decoder-only architectures", "weight": 1.0} -->

Decoder-only models, on the other hand, are streamlined for generating text by continuously predicting the next token, leveraging a single, powerful autoregressive mechanism. That being said, due to their simplicity, decoder-only architectures are now increasinglh being used even for seq2seq tasks, by prepending the input (prompt) to the context. This means that the input is subject to the causal mask, but the performance remains remarkably strong.

<!-- chunk {"id": "body-0322", "role": "body", "section": "Summary", "weight": 1.0} -->

- Programs can be mathematically represented as a directed acyclic graph. - Neural networks are parameterized programs. - Feedfoward networks are parameterized computation chains. - Multilayer perceptrons (MLPs), residual neural networks (ResNets) and convolutional neural network (CNNs) are all particular parametrizations of feedforward networks. - Transformer blocks are designed to process sequences of variablelength, but they are equivariant to permutations and therefore require positional encoding, in order to leverage positional information.

<!-- chunk {"id": "body-0323", "role": "body", "section": "Control flows", "weight": 1.0} -->

Control flows, such as conditionals or loops, are an essential part of computer programming, as they allow us to express complex programs. It is therefore natural to ask whether these constructs can be included in a differentiable program. This is what we study in this chapter.

<!-- chunk {"id": "body-0324", "role": "body", "section": "Comparison operators", "weight": 1.0} -->

Control flows rely on comparison operators, a.k.a. relational operators. Formally, we can define a comparison operator π = op( u 1, u 2 ) as a function from u 1 ∈ R and u 2 ∈ R to π ∈ { 0, 1 }. The binary (Boolean) output π can then be used within a conditional statement (see Section 5.6, Section 5.7) to decide whether to execute one branch or another. We define the following operators, illustrated in Fig. 5.1:

<!-- chunk {"id": "body-0325", "role": "body", "section": "· greater than", "weight": 1.0} -->

R →{, } Heaviside step function where step: 0 1 is the The Heaviside step function is piecewise constant. At = 0, the function u is discontinuous. At u = 0, it is continuous and has null derivative. Since the comparison operators we presented are all expressed in terms of the step function, they are all continuous and differentiable almost everywhere, with null derivative. Therefore, while their derivatives are well-defined almost everywhere, they are uninformative and prevent gradient backpropagation.

<!-- chunk {"id": "body-0326", "role": "body", "section": "Heuristic definition", "weight": 1.0} -->

To obtain a continuous relaxation of inequality operators, we can heuristically replace the step function in the expression of 'greater than' and 'less than' by a sigmoid function sigmoid σ, where σ > 0 is a scaling parameter. Such a sigmoid function should satisfy the following properties: Two examples of sigmoids satisfying the aforementioned properties are the logistic function (the CDF of the standard logistic distribution) and the standard Gaussian's CDF, defined in Eq. (3.1), We may then define the soft 'greater than' and the soft 'less than' In the limit, we have that sigmoid σ (µ 1 -µ 2) → 1 when µ 1 -µ 2 →∞. In the limit, sigmoid σ therefore outputs a value of 1 if µ 1 and µ 2 are infinitely apart. Besides the logistic function and the standard Gaussian's CDF, other sigmoid functions are possible, as discussed in Section 13.6. In particular, with sparse sigmoids, there exists a finite value τ such that µ 1 -µ 2 ≥ τ = ⇒ sigmoid σ (µ 1 -µ 2) = 1.

<!-- chunk {"id": "body-0327", "role": "body", "section": "Stochastic process perspective", "weight": 1.0} -->

When the sigmoid used to replace the step function is the logistic function or the standard Gaussian's CDF, we can revisit the previous heuristic definition of gt σ (µ 1, µ 2) and lt σ (µ 1, µ 2) from a more formal perspective. Indeed, to real values µ 1 ∈ R and µ 2 ∈ R, we can associate random variables thereby forming a stochastic process (we assume that σ 1 and σ 2 are fixed). Alternatively, we can also write where for two distributions p 1 and p 2, we denote p 1 ⊗ p 2 their outer product (p 1 ⊗ p 2)(u 1, u 2):= p 1 (u 1) p 2 (u 2). We can then define where is the (CDF) of the F X cumulative distribution function random variable X, and σ is a function of σ 1 and σ 2. Similarly, we obtain We see that the soft inequality operators are based on the CDF of the difference between U 1 and U 2.

<!-- chunk {"id": "body-0328", "role": "body", "section": "Stochastic process perspective", "weight": 1.0} -->

For location-scale family distributions (Section 12.4.1), from a perturbation perspective, we can also define noise variables Z 1 ∼ p 0, 1 and Z 2 ∼ p 0, 1 such that U 1 = µ 1 + σ 1 Z 1 and U 2 = µ 2 + σ 2 Z 2 (Section 12.4.1). We then have

<!-- chunk {"id": "body-0329", "role": "body", "section": "Gaussian case", "weight": 1.0} -->

When U 1 ∼ Normal(µ 1, σ 2 1) and U 2 ∼ Normal(µ 2, σ 2 2), we have Denoting Φ the standard Gaussian's CDF, we then obtain where σ:= √ σ 2 1 + σ 2 2. The corresponding distribution for Z 1 and Z 2 is Gaussian noise.

<!-- chunk {"id": "body-0330", "role": "body", "section": "Logistic case", "weight": 1.0} -->

When U 1 ∼ Gumbel(µ 1, σ) and U 2 ∼ Gumbel(µ 2, σ), we have We then obtain (see also Proposition 14.3) The corresponding distribution for Z 1 and Z 2 is Gumbel noise.

<!-- chunk {"id": "body-0331", "role": "body", "section": "Recovering hard inequality operators", "weight": 1.0} -->

We easily recover the 'hard' inequality operator by where U i ∼ δ µ i and where δ µ i is the delta distribution that assigns a probability of 1 to µ i.

<!-- chunk {"id": "body-0332", "role": "body", "section": "Heuristic definition", "weight": 1.0} -->

The equality operator eq(µ 1, µ 2) can be seen as an extreme kind of similarity function between numbers, that can only output the values 0 or 1. To define soft equality operators, a natural idea is therefore to replace the equality operator by a more general similarity function. A similarity function should achieve its maximum at µ 1 = µ 2 and it should decrease as µ 1 and µ 2 move apart. A common family of similarity functions are kernels. Briefly, a kernel k (µ 1, µ 2) can be seen as the inner product between the embbedings φ (µ 1) and φ (µ 2) of µ 1 and µ 2 in some (potentially infinite-dimensional) space H, a reproducing kernel Hilbert space to be precise; see Schölkopf and Smola and Shawe-Taylor and Cristianini for an in-depth review of kernels. To obtain a similarity measure between 0 and 1 approximating the equality operator, we can normalize to obtain where ‖ φ (µ) ‖:= √ 〈 φ (µ), φ (µ) 〉 = √ κ (µ, µ).

<!-- chunk {"id": "body-0333", "role": "body", "section": "Heuristic definition", "weight": 1.0} -->

This is the cosine similarity between φ (µ 1) and φ (µ 2).

<!-- chunk {"id": "body-0334", "role": "body", "section": "Heuristic definition", "weight": 1.0} -->

A particular kind of kernel are isotropic kernels of the form that depend only on the difference between inputs. When the kernel has a scale parameter σ > 0, we use the notation κ σ. We can then define a soft equality operator as Several isotropic kernels can be chosen such as the Gaussian kernel Figure 5.2: Soft equality and soft greater than operators can be defined as normalized kernels (PDF) and as CDF functions, respectively. or the logistic kernel where we defined the hyperbolic secant As their names suggest, these kernels arise naturally from a probabilistic perspective, that we present below.

<!-- chunk {"id": "body-0335", "role": "body", "section": "Heuristic definition", "weight": 1.0} -->

The soft equality operators obtained with these kernels are illustrated in Fig. 5.2. Intuitively, we replaced a bar located at µ 1 = µ 2 with a bump function. The soft equality operator obtained with the logistic kernel coincides with the expression Petersen et al. arrive at (see their Eq. 9), in a different manner.

<!-- chunk {"id": "body-0336", "role": "body", "section": "Stochastic process perspective", "weight": 1.0} -->

We again adopt the stochastic process perspective, in which we associate random variables to real values µ 1 ∈ R and µ 2 ∈ R. However, to handle the equality operator, we cannot simply use the expectation of eq(U 1, U 2) since U 1 and U 2 being independent continuous variables. While we cannot use the probability of U 1 = U 2, or equivalently of U 1 -U 2 = 0, we can consider using the probability density function (PDF) f U 1 -U 2 of U 1 -U 2 evaluated at 0. To ensure that the maximum is achieved at 0 with value 1, we can normalize the PDF to define It is well-known that the PDF of the sum of two random variables is the convolution of their respectives PDFs. We therefore have In particular, with t = 0, if f X is the PDF of a location-scale family distributed random variable, we obtain We indeed recover an inner product and therefore a kernel.

<!-- chunk {"id": "body-0337", "role": "body", "section": "CDF and PDF of absolute difference", "weight": 1.0} -->

While P (U 1 = U 2) = 0, we can also consider using P (| U 1 -U 2 | ≤ ε) = F | U 1 -U 2 | (ε) as an alternative notion of soft equality. For any random variable X, we have Therefore, We can also derive the PDF of | X | as further justifying using the PDF of U 1 -U 2 evaluated at 0. When X follows a normal distribution, | X | follows the so-called folded normal distribution.

<!-- chunk {"id": "body-0338", "role": "body", "section": "Gaussian case", "weight": 1.0} -->

When U 1 ∼ Normal(µ 1, σ 2 1) and U 2 ∼ Normal(µ 2, σ 2 2), we obtain from Eq. (5.1) We indeed recover κ σ (µ 1 -µ 2) /κ σ, where κ σ is the Gaussian kernel with σ = √ σ 2 1 + σ 2 2. For the CDF of the absolute difference, we obtain

<!-- chunk {"id": "body-0339", "role": "body", "section": "Logistic case", "weight": 1.0} -->

When U 1 ∼ Gumbel(µ 1, σ) and U 2 ∼ Gumbel(µ 2, σ), recalling that We indeed recover κ σ (µ 1 -µ 2) /κ σ, where κ σ is the logistic kernel with σ = σ 1 = σ 2.

<!-- chunk {"id": "body-0340", "role": "body", "section": "Gaussian process perspective", "weight": 1.0} -->

The previous approach relied on mapping µ 1 and µ 2 to two independent random variables U 1 ∼ p µ 1,σ 1 and U 2 ∼ p µ 2,σ 2 (we assume that σ 1 and σ 2 are fixed). Instead, we can consider mapping µ 1 and µ 2 to two dependent random variables U 1 and U 2, whose covariance depends on the similarity between µ 1 and µ 2. We can do so by using a Gaussian process.

<!-- chunk {"id": "body-0341", "role": "body", "section": "Gaussian process perspective", "weight": 1.0} -->

AGaussian process on R is a stochastic process { U µ: µ ∈ R } indexed by µ ∈ R such that any subset of K random variables (U µ 1,..., U µ K) associated with (µ 1,..., µ K) ∈ R is a multivariate Gaussian random variable. The Gaussian process is characterized by the mean function µ ↦→ E [U µ], and its covariance function (µ i, µ j) ↦→ Cov(U µ i, U µ j). For the mean function, we may simply choose E [U µ] = µ. For the covariance function, we need to ensure that the variance of any combination of random variables in the Gaussian process is non-negative. This property is satisfied by kernel functions. We can therefore define for some kernel k. Equipped with such a mapping from real numbers to random variables, we need a measure of similarity between random variables. A natural choice is their correlation which coincides with the cosine similarity measure we saw before.

<!-- chunk {"id": "body-0342", "role": "body", "section": "Gaussian process perspective", "weight": 1.0} -->

In the particular case K = 2 and when k σ (µ 1, µ 2) = κ (µ 1 -µ 2), we then recover the previous heuristically-defined soft equality operator

<!-- chunk {"id": "body-0343", "role": "body", "section": "Logical operators", "weight": 1.0} -->

Logical operators can be used to perform Boolean algebra. Formally, we can define them as functions from { 0, 1 } × { 0, 1 } to { 0, 1 }. The and (logical conjunction a.k.a. logical product), or (logical disjunction a.k.a. logical addition) and not (logical negation a.k.a. logical complement) operators, for example, are defined by Classical properties of these operators include

<!-- chunk {"id": "body-0344", "role": "body", "section": "Logical operators", "weight": 1.0} -->

- Distributivity of and over or: More generally, for a binary vector π = (π 1,..., π K) ∈ { 0, 1 } K, we can define all (universal quantification, ∀) and any (existential quantification, ∃) operators, which are functions from { 0, 1 } K to { 0, 1 }, as

<!-- chunk {"id": "body-0345", "role": "body", "section": "Probabilistic continuous extension", "weight": 1.0} -->

We can equivalently write the and, or and not operators as These are extensions of the previous definitions: we can use them as functions from × →, as illustrated in Fig. 5.3. This means that we can use the soft comparison operators defined in Section 5.2 to obtain π, π ′ ∈. Likewise, we can define continuous extensions of Figure 5.3: The Boolean and and or operators are functions from { 0, 1 } × { 0, 1 } to { 0, 1 } (corners in the figure) but their continuous extensions and(π, π ′):= π · π ′ as well as or(π, π ′):= π + π ′ -π · π ′ define a function from × to. all and any, which are functions from K to, as From a probabilistic perspective, if we let Y and Y ′ to be two independent random variables distributed according to Bernoulli distributions with parameter π and π ′, then In probability theory, these correspond to the product rule of two independent variables, the addition rule, and the complement rule.

<!-- chunk {"id": "body-0346", "role": "body", "section": "Probabilistic continuous extension", "weight": 1.0} -->

Likewise, if we let Y = (Y 1,..., Y K) ∈ { 0, 1 } K be a random variable distributed according to a multivariate Bernoulli distribution with parameters π = (π 1,..., π K), then These are the chain rule of probability and the addition rule of probability for K independent variables.

<!-- chunk {"id": "body-0347", "role": "body", "section": "Triangular norms and co-norms", "weight": 1.0} -->

More generally, in the fuzzy logic literature, the concepts of triangular norms and co-norms have been introduced to provide continuous relaxations of the and and or operators, respectively.

<!-- chunk {"id": "body-0348", "role": "body", "section": "Triangular norms and co-norms", "weight": 1.0} -->

Definition 5.1 (Triangular norms and conorms). A triangular norm, a.k.a. t-norm, is a function from × to which is commutative, associative, neutral w.r.t. 1 and is monotone, meaning that t ( π, π ′ ) ≤ t ( τ, τ ′ ) for all π ≤ τ and π ′ ≤ τ ′. A triangular conorm, a.k.a. t-conorm, is defined similarly but is neutral w.r.t. 0.

<!-- chunk {"id": "body-0349", "role": "body", "section": "Triangular norms and co-norms", "weight": 1.0} -->

The previously-defined probabilistic extensions of and and or are examples of triangle norm and conorm. More examples are given in Table 5.1. Thanks to the associative property of these operators, we can generalize them to vectors π ∈ K to define continuous extensions of the all and any operators, as shown in Table 5.2. For more examples and analysis, see for instance van Krieken.

<!-- chunk {"id": "body-0350", "role": "body", "section": "Triangular norms and co-norms", "weight": 1.0} -->

Table 5.1: Examples of triangular norms and conorms, which are continuous relaxations of the and and or operators, respectively. More instances can be obtained by smoothing out the min and max operators.

<!-- chunk {"id": "body-0351", "role": "body", "section": "Triangular norms and co-norms", "weight": 1.0} -->

| | t-norm (relaxed and) | t-conorm (relaxed or) |

<!-- chunk {"id": "body-0352", "role": "body", "section": "If-else statements", "weight": 1.0} -->

An if-else statement executes different code depending on a condition. Formally, we can define the ifelse: { 0, 1 } × V × V → V function by The π variable is called the predicate. It is a binary (Boolean) variable, making the function ifelse undefined if π ̸∈ { 0, 1 }. The function is therefore discontinuous and nondifferentiable w.r.t. π ∈ { 0, 1 }. On the other hand, v 0 ∈ V and v 1 ∈ V, which correspond to the false and true branches, can be continuous variables. If π = 1, the function is linear w.r.t. v 1 and constant w.r.t. v 0. Conversely, if π = 0, the function is linear w.r.t. v 0 and constant w.r.t. v 1. We now discuss how to differentiate through ifelse.

<!-- chunk {"id": "body-0353", "role": "body", "section": "If-else statements", "weight": 1.0} -->

Table 5.2: Continuous extensions of the all and any operators.

<!-- chunk {"id": "body-0354", "role": "body", "section": "Differentiating through branch variables", "weight": 1.0} -->

For π ∈ { 0, 1 } fi xed, ifelse(π, v 1, v 0) is a valid function w.r.t. v 1 ∈ V and v 0 ∈ V, and can therefore be used as a node in a computational graph (Section 8.3). Due to the linearity w.r.t. v 1 and v 0, we obtain that the Jacobians w.r.t. v 1 and v 0 are where I is the identity matrix of appropriate size. Most of the time, if-else statements are composed with other functions. Let g 1: U 1 →V and g 0: U 0 →V be differentiable functions. We then define v 1:= g 1 (u 1) and v 0:= g 0 (u 0), where u 1 ∈ U 1 and u 0 ∈ U 0. The composition of ifelse, g 1 and g 0 is then the function f: { 0, 1 }×U 1 ×U 0 →V defined by We obtain that the Jacobians are As long as g 1 and g 0 are differentiable functions, we can therefore differentiate through the branch variables u 1 and u 0 without any issue.

<!-- chunk {"id": "body-0355", "role": "body", "section": "Differentiating through branch variables", "weight": 1.0} -->

More problematic is the predicate variable π, as we now discuss.

<!-- chunk {"id": "body-0356", "role": "body", "section": "Differentiating through predicate variables", "weight": 1.0} -->

The predicate variable π is binary and therefore cannot be differentiated directly. However, π can be the output of a comparison operator. For example, suppose we want to express the function f h: R ×U 1 ×U 0 →V defined by Using our notation, this can be rewritten as The Heaviside step function has a discontinuity at p = 0, but it is continuous and differentiable with derivative step ′ (p) = 0 for all p = 0. The function f h therefore has null derivative w.r.t. p = 0, In other words, while f h has well-defined derivatives w.r.t. p for p = 0, the derivatives are uninformative. As another example, let us now consider the function for some differentiable function t. This time, u 1 influences both the predicate and the true branch. Then, using Proposition 2.8, we obtain In other words, the derivatives of the predicate t (u 1) do not influence the derivatives of g h.

<!-- chunk {"id": "body-0357", "role": "body", "section": "Continuous relaxations", "weight": 1.0} -->

Fortunately, we recall that This function is perfectly well-defined, even if π ∈, instead of π ∈ { 0, 1 }. That is, this definition is an extension of Eq. (5.3) from the discrete set { 0, 1 } to the continuous unit segment. We saw that where we use sigmoid σ to denote a differentiable S-shaped function mapping R to. For instance, we can use the logistic function or the standard Gaussian's CDF. If we now define the Jacobian becomes If sigmoid σ = logistic(· /σ) or sigmoid σ = Φ(· /σ), the Jacobian is nonnull everywhere, allowing gradients to backpropagate through the computational graph. This is an example of smoothing as studied in Part IV.

<!-- chunk {"id": "body-0358", "role": "body", "section": "Probabilistic perspective", "weight": 1.0} -->

From a probabilistic perspective, we can view Eq. (5.4) as the expectation of g i (u i), where i ∈ { 0, 1 } is a binary random variable distributed according to a Bernoulli distribution with parameter π = sigmoid σ (p): Taking the expectation over the two possibles branches makes the function differentiable with respect to p, since sigmoid σ (p) is differentiable. Of course, this comes at the cost of evaluating both branches, instead of a single one. The probabilistic perspective suggests that we can also compute the variance if needed as Figure 5.5: Computation graphs of programs using if-else statements with either hard or soft comparison operators. By using a hard comparison operator (step function, left panel) the predicate π is a discrete variable (represented by a dashed line). Depending on the value (0 or 1) of the predicate π, only one branch (red or blue) contributes to the output. Derivatives along a path of continuous variables (dense lines) can be computed. However, discrete variables such as the predicate prevent the propagation of meaningful derivatives.

<!-- chunk {"id": "body-0359", "role": "body", "section": "Probabilistic perspective", "weight": 1.0} -->

By using a soft comparison operator (sigmoid, right panel), the predicate is a continuous variable and derivatives with respect to the input p can be taken. In this case both branches (corresponding to g 0 and g 1) contribute to the output and therefore need to be evaluated.

<!-- chunk {"id": "body-0360", "role": "body", "section": "Probabilistic perspective", "weight": 1.0} -->

The probabilistic viewpoint also suggests different scales at which a smoothing can be defined as illustrated in Fig. 5.6.

<!-- chunk {"id": "body-0361", "role": "body", "section": "Probabilistic perspective", "weight": 1.0} -->

Another perspective is based on the logistic distribution. Indeed, if P is a random variable following a logistic distribution with mean p and scale 1, we saw in Remark 3.1 that the CDF is P (P ≤ 0) = logistic(-p) = 1 -logistic(p) and therefore Remark 5.1 (Global versus local smoothing). Consider the function The derivatives w.r.t. y and z are well-defined. The derivative w.r.t. x on the other hand is not well-defined since it involves comparison operators and the logical operator and. Using our notation, we can rewrite the function as A local smoothing approach consists in replacing gt and lt by gt σ and lt σ locally in the program: for any sigmoid function sigmoid σ. A global smoothing approach instead uses the expectation of the entire program Figure 5.6: Global versus local smoothing approaches on a gate function f (x):= 1 if x ∈, and f (x):= 0 otherwise. In our notation, we can write f (x) = ifelse(and(gt(x, -1), lt(x, 1)), 1, 0).

<!-- chunk {"id": "body-0362", "role": "body", "section": "Probabilistic perspective", "weight": 1.0} -->

A local approach smoothes out gt and lt separately. A global approach uses the expectation of the whole program, see Remark 5.1. We observe that, though the approaches differ for large σ, they quickly coincide for smaller σ. for sigmoid σ the CDF of σZ. We therefore obtain The difference stems from the fact that the local approach smoothes out a ≤ x and x ≤ b independently (treating 1 X ≥ a and 1 X ≤ b as independent random variables), while the global approah smoothes out a ≤ x ≤ b simultaenously. In practice, both approaches approximate the original function well as σ → 0 and coincide for σ sufficiently small as illustrated in Fig. 5.6.

<!-- chunk {"id": "body-0363", "role": "body", "section": "Else-if statements", "weight": 1.0} -->

In the previous section, we focused on if-else statements: conditionals with only two branches. We now generalize our study to conditionals including else-if statements, that have K branches.

<!-- chunk {"id": "body-0364", "role": "body", "section": "Encoding K branches", "weight": 1.0} -->

For conditionals with only 2 branches, we encoded the branch that the conditional needs to take using the binary variable π ∈ { 0, 1 }. For conditionals with K branches, we need a way to encode which of the K branches the conditional needs to take. To do so, we can use a vector π ∈ { e 1,..., e K }, where e i denotes the standard basis vector (a.k.a. one-hot vector) a vector with a single one in the coordinate i and K -1 zeros. The vector e i is the encoding of a categorical variable i ∈ [K].

<!-- chunk {"id": "body-0365", "role": "body", "section": "Combining booleans", "weight": 1.0} -->

To form, such a vector π ∈ { e 1,..., e K }, we can combine the previouslydefined comparison and logical operators to define π = ( π 1,..., π K ). However, we need to ensure that only one π i is non-zero. We give an example in Example 5.1.

<!-- chunk {"id": "body-0366", "role": "body", "section": "Argmax and argmin operators", "weight": 1.0} -->

Another way to form π is to use the argmax and argmin operators They can be seen as a natural generalization of the greater than and less than operators. In case of ties, we break them arbitrarily.

<!-- chunk {"id": "body-0367", "role": "body", "section": "Conditionals", "weight": 1.0} -->

We can now express a conditional statement as the function cond: { e 1,..., e K } × V K →V defined by Similarly as for the ifelse function, the cond function is discontinuous and nondifferentiable w.r.t. π ∈ { e 1,..., e K }. However, given π = e i fixed for some i, the function is linear in v i and constant in v j for j = i. We illustrate how to express a simple example, using this formalism.

<!-- chunk {"id": "body-0368", "role": "body", "section": "Conditionals", "weight": 1.0} -->

Example 5.1 (Soft-thresholding operator). The soft-thresholding operator (see also Section 16.4) is a commonly-used operator to promote sparsity. It is defined by To express it in our formalism, we can define π ∈ { e 1, e 2, e 3 } using comparison operators as Equivalently, we can also define π using an argmax operator as In case of ties, which happens at | u | = λ, we keep only one non-zero coordinate in π. We can then rewrite the operator as As we will see, replacing argmax with softargmax induces a categorical distribution over the three possible branches. The mean value can be seen as a smoothed out version of the operator, and we can also compute the standard deviation, as illustrated in Fig. 5.7.

<!-- chunk {"id": "body-0369", "role": "body", "section": "Differentiating through branch variables", "weight": 1.0} -->

For π fi xed, cond(π, v 1,..., v K) is a valid function w.r.t. v i, and can therefore again be used as a node in a computational graph. Due to the linearity w.r.t. v i, we obtain that the Jacobian w.r.t. v i is Figure 5.7: A conditional with three branches: the soft-thresholding operator (see Example 5.1). It is a piecewise linear function (dotted black line). Using a softargmax, we can induce a categorical probability distribution over the three branches. The expected value (blue line) can be seen as a smoothed out version of the operator. The induced distribution allows us to also compute the standard deviation.

<!-- chunk {"id": "body-0370", "role": "body", "section": "Differentiating through branch variables", "weight": 1.0} -->

Let g i: U i → V be a differentiable function and u i ∈ U i. If we define the composition we then obtain that the Jacobian w.r.t. u i is As long as the g i functions are differentiable, we can therefore differentiate through the branch variables u i for π fi xed.

<!-- chunk {"id": "body-0371", "role": "body", "section": "Differentiating through predicate variables", "weight": 1.0} -->

As we saw, π can be obtained by combining comparison and logical operators, or it can be obtained by argmax and argmin operators.

<!-- chunk {"id": "body-0372", "role": "body", "section": "Differentiating through predicate variables", "weight": 1.0} -->

We illustrate here why these operators are problematic. For example, suppose we want to express the function In our notation, this can be expressed as As for the ifelse case, the Jacobian w.r.t. p is null almost everywhere,

<!-- chunk {"id": "body-0373", "role": "body", "section": "Continuous relaxations", "weight": 1.0} -->

Similarly to the Heaviside step function, the argmax and argmin functions are piecewise constant, with discontinuities in case of ties. Their Jacobian are zero almost everywhere, and undefined in case of ties. Therefore, while their Jacobian is well-defined almost everywhere, they are uninformative and prevent gradient backpropagation. We can replace the argmax with a softargmax Other relaxations of the argmax are possible, as discussed in Section 13.7. See also Section 14.5.3 for the perturbation perspective.

<!-- chunk {"id": "body-0374", "role": "body", "section": "Continuous relaxations", "weight": 1.0} -->

Fortunately, the definition is perfectly valid if we use π ∈ △ K instead of π ∈ { e 1,..., e K }, and and similarly can therefore be seen as an extension of Eq. (5.5). If we now define the Jacobian becomes which is non-null everywhere, allowing gradients to backpropagate through the computational graph.

<!-- chunk {"id": "body-0375", "role": "body", "section": "Probabilistic perspective", "weight": 1.0} -->

From a probabilistic perspective, we can view Eq. (5.6) as the expectation of g i (u i), where i ∈ [K] is a categorical random variable distributed according to a categorical distribution with parameter π = softargmax(p): Taking the expectation over the K possible branches makes the function differentiable with respect to p, at the cost of evaluating all branches, instead of a single one. Similarly as for the if-else case, we can compute the variance if needed as This is illustrated in Fig. 5.7.

<!-- chunk {"id": "body-0376", "role": "body", "section": "For loops", "weight": 1.0} -->

For loops are a control flow for sequentially calling a fixed number K of functions, reusing the output from the previous iteration. In full generality, a for loop can be written as follows.

<!-- chunk {"id": "body-0377", "role": "body", "section": "Algorithm 5.1 r = forloop( s 0 )", "weight": 1.0} -->

As illustrated in Fig. 5.8, this defines a computation chain. Assuming the functions f k are all differentiable, this defines a valid computation graph, we can therefore use automatic differentiation to differentiate forloop w.r.t. its input s 0. Feedforward networks, reviewed in Section 4.2, can be seen as parameterized for loops, i.e., for some differentiable function g k.

<!-- chunk {"id": "body-0378", "role": "body", "section": "Algorithm 5.1 r = forloop( s 0 )", "weight": 1.0} -->

Example 5.2 (Unrolled gradient descent). Suppose we want to minimize w.r.t. w the function Given an initialization w 0, gradient descent (Section 16.1) performs iterations of the form Gradient descent can therefore be expressed as a for loop with This means that we can differentiate through the iterations of gradient descent, as long as f is differentiable, meaning that L is twice differentiable. This is useful for instance to perform gradientbased optimization of the hyperparameters γ k or λ. This a special case of bilevel optimization; see also Chapter 11.

<!-- chunk {"id": "body-0379", "role": "body", "section": "Algorithm 5.1 r = forloop( s 0 )", "weight": 1.0} -->

Example 5.3 (Bubble sort). Bubble sort is a simple sorting algorithm that works by repeatedly swapping elements if necessary.

<!-- chunk {"id": "body-0380", "role": "body", "section": "Algorithm 5.1 r = forloop( s 0 )", "weight": 1.0} -->

Mathematically, swapping two elements i and j can be written as a function from R N × [N] × [N] to R N defined by We can then write bubble sort as Replacing the Heaviside step function with the logistic function gives a smoothed version of the algorithm.

<!-- chunk {"id": "body-0381", "role": "body", "section": "Scan functions", "weight": 1.0} -->

Scan is a higher-order function (meaning a function of a function) originating from functional programming. It is useful to perform an operation f on individual elements u k while carrying the result s k of that operation to the next iteration.

<!-- chunk {"id": "body-0382", "role": "body", "section": "Scan functions", "weight": 1.0} -->

As illustrated in Fig. 5.9, this again defines a valid computational graph and can be differentiated through using autodiff, assuming the function f is differentiable. Sequence-to-sequence RNNs, reviewed in Section 4.7, can be seen as a parameterized scan. An advantage of this abstraction is that parallel scan algorithms have been studied extensively in computer science.

<!-- chunk {"id": "body-0383", "role": "body", "section": "Scan functions", "weight": 1.0} -->

Example 5.4 (Prefix sum). Scan can be seen as a generalization of the prefix sum (a.k.a. cumulated sum) from the addition to any binary operation. Indeed, a prefix sum amounts to perform which can be expressed as a scan by defining starting from s 0 = 0 (s K and v K are redundant in this case).

<!-- chunk {"id": "body-0384", "role": "body", "section": "While loops as cyclic graphs", "weight": 1.0} -->

A while loop is a control flow used to repeatedly perform an operation, reusing the output of the previous iteration, until a certain condition is met. Suppose f: S → { 0, 1 } is a function to determine whether to stop ( π = 1) or continue ( π = 0) and g: S → S is a function for performing an operation. Then, without loss of generality, a while loop can be written as follows.

<!-- chunk {"id": "body-0385", "role": "body", "section": "Algorithm 5.3 r = whileloop( s )", "weight": 1.0} -->

This definition is somewhat cyclic, as we used the while keyword. However, we can equivalently rewrite the algorithm recursively.

<!-- chunk {"id": "body-0386", "role": "body", "section": "Algorithm 5.4 r = whileloop( s )", "weight": 1.0} -->

π:= f (s) if π = 0 then r:= s else r:= whileloop(g (s)) Unlike for loops and scan, the number of iterations of while loops is not known ahead of time, and may even be infinite. In this respect, a while loop can be seen as a cyclic graph, as illustrated in Fig. 5.10.

<!-- chunk {"id": "body-0387", "role": "body", "section": "Importance of lazy evaluation", "weight": 1.0} -->

We can also implement Algorithm 5.4 in terms of the ifelse function defined in Section 5.6 as However, to avoid an infinite recursion, it is crucial that ifelse supports lazy evaluation. That is, whileloop(g (s)) in the definition above should be evaluated if and only if π = f (s) = 0. In other words, the fact that f (s) ∈ { 0, 1 } is crucial to ensure that the recursion is well-defined.

<!-- chunk {"id": "body-0388", "role": "body", "section": "Unrolled while loops", "weight": 1.0} -->

To avoid the issues with unbounded while loops, we can enforce that a while loop stops after T iterations, i.e., we can truncate the while loop. Unrolling Algorithm 5.4 gives (here with T = 3) Using the ifelse function, we can rewrite it as which is itself equivalent to More generally, for T ∈ N, the formula is See also. If we further define the shorthand notation so that ˜ π:= (˜ π 0, ˜ π 1,..., ˜ π T) ∈ △ T +1 is a discrete probability distribution containing the probabilities to stop at each of the T iterations, we can rewrite the output of a truncated while using a conditional, Figure 5.11: Computation graph of an unrolled truncated while loop. As in Fig. 5.5, we depict continuous variables in dense lines and discrete variables in dashed lines. The output of a while loop with at most T iterations can be written as a conditional with T +1 branches, cond(˜ π, s 0,..., s T) = ∑ T t =0 ˜ π t s t.

<!-- chunk {"id": "body-0389", "role": "body", "section": "Unrolled while loops", "weight": 1.0} -->

Example 5.5 (Computing the square root using Newton's method). Computing the square root √ x of a real number x > 0 can be cast as a root finding problem, which we can solve using Newton's method. Starting from an initialization s 0, the iterations read To measure the error on iteration i, we can define As a stopping criterion, we can then use where 0 < τ ≪ 1 is an error tolerance and step is the Heaviside step function.

<!-- chunk {"id": "body-0390", "role": "body", "section": "Markov chain perspective", "weight": 1.0} -->

Given the function g: S → S and the initialization s 0 ∈ S, a while loop can only go through a discrete set of values s 0, s 1, s 2,... defined by s i = g (s i -1). This set is potentially countably infinite if the while loop is unbounded, and finite if the while loop is guaranteed to stop. Whether the loop moves from the state s i to the state s i +1, or stays at s i, is determined by the stopping criterion π i ∈ { 0, 1 }. To model the state of the while loop, we can then consider a Markov chain with a discrete space { s 0, s 1, s 2,... }, which we can always identify with { 0, 1, 2,... }, with transition probabilities and initial state S 0 = s 0. Here, S t is the value at iteration t of the loop. Note that since π i ∈ { 0, 1 }, the p i,j values are 'degenerate' probabilities. However, this framework lets us generalize to a smooth version of the while loop naturally.

<!-- chunk {"id": "body-0391", "role": "body", "section": "Markov chain perspective", "weight": 1.0} -->

To illustrate the framework, if the while loop stops at T = 3, the transition probabilities can be cast as a matrix The output r of the while-loop is determined by the time at which the state stays at the same value Note that I itself is a random variable, as it is defined by the S i variables. It is called a stopping time. The output of the chain is then Because the stopping time is not known ahead of time, the sum over i goes from 0 to ∞. However, if we enforce in the stopping criterion that the while loop runs no longer than T iterations, by setting we then naturally recover the expression found by unrolling the while loop before, For example, with T = 3, the transition probability matrix is

<!-- chunk {"id": "body-0392", "role": "body", "section": "Smoothed while loops", "weight": 1.0} -->

With the help of this framework, we can backpropagate even through the while loop's stopping criterion, provided that we smooth out the predicate. For example, we saw that the stopping criterion in Example 5.5 is f (s i) = step(τ -ε (s i)) and therefore Due to the step function, the derivative of the while loop with respect to τ will always be 0, just like it was the case for if-else statements. If we change the stopping criterion to f (s i) = sigmoid(τ -ε (s i)), we then have (recall that or is well defined on ×) With sigmoid, we obtain more informative derivatives. In particular, with sigmoid = logistic, the derivatives w.r.t. τ are always non-zero. The smoothed output is expressed as before as the expectation Instead of enforcing a number T of iterations, it is also possible to stop when the probability of stopping becomes high enough, assuming that the probability of stopping converges to 1.

<!-- chunk {"id": "body-0393", "role": "body", "section": "Summary", "weight": 1.0} -->

- For conditionals, we saw that differentiating through the branch variables is not problematic given a fixed predicate. - However, for the predicate variable, we saw that a differentiable relaxation is required to avoid null derivatives. - We introduced soft comparison operators in a principled manner, using a stochastic process perspective, as well as the continuous extension of logical operators.

<!-- chunk {"id": "body-0394", "role": "body", "section": "Summary", "weight": 1.0} -->

- For loops and scan define valid computational graphs, as their number of iterations is fixed ahead of time. Feedforward networks and RNNs can be seen as parameterized for loops and scan, respectively. - Unlike for loops and scan, the number of iterations of while loops is not known ahead of time and may even be infinite. However, unrolled while loops define valid directed acyclic graphs. We defined a principled way to differentiate through the stopping criterion of a while loop, thanks to a Markov chain perspective.

<!-- chunk {"id": "body-0395", "role": "body", "section": "Data structures", "weight": 1.0} -->

In computer science, a data structure is a specialized format for organizing, storing and accessing data. Mathematically, a data structure forms a so-called algebraic structure: it consists of a set and the functions to operate on that set. In this chapter, we review how to incorporate data structures into differentiable programs, with a focus on lists and dictionaries.

<!-- chunk {"id": "body-0396", "role": "body", "section": "Lists", "weight": 1.0} -->

A list is an ordered sequence of elements. We restrict ourselves to lists whose elements all belong to the same value space V. Formally, we denote a list of fixed length K with values in V by a K -tuple where each l i ∈ V and where

<!-- chunk {"id": "body-0397", "role": "body", "section": "Getting values", "weight": 1.0} -->

We first present how to retrieve values from a list l ∈ L K (V). We define the function list. get: L K (V) × [K] →V as The function is continuous and differentiable in l ∈ L K (V) but not in i ∈ [K], as it is a discrete variable. In the particular case V = R, L K (V) is equivalent to R K and we can therefore write where { e 1,..., e K } is the standard basis of R K.

<!-- chunk {"id": "body-0398", "role": "body", "section": "Setting values", "weight": 1.0} -->

We now present how to replace values from a list l ∈ L K (V). We define the function list. set: L K (V) × [K] ×V → L K (V) as for j ∈ [K]. In the functional programming spirit, the function returns the whole new list, even though a single element has been modified. Again, the function is continuous and differentiable in l ∈ L K (V) and v ∈ V but not in i ∈ [K]. In the particular case V = R, given a list l = (l 1,..., l K), we can write That is, we subtract the old value l i and add the new value v at the location i ∈ [K].

<!-- chunk {"id": "body-0399", "role": "body", "section": "Implementation", "weight": 1.0} -->

A fixed-length list can be implemented as an array, which enables O random access to individual elements. The hardware counterpart of an array is random access memory (RAM), in which memory can be retrieved by address (location).

<!-- chunk {"id": "body-0400", "role": "body", "section": "Operations on variable-length lists", "weight": 1.0} -->

So far, we focused on lists of fixed length K. We now turn our attention to variable-length lists, whose size can decrease or increase over time. In addition to the list. get and list. set functions, they support functions that can change the size of a list.

<!-- chunk {"id": "body-0401", "role": "body", "section": "Initializing lists", "weight": 1.0} -->

In order to initialize a list, we define list. init: V → L 1 (V) as where used (v) to denote a 1-tuple.

<!-- chunk {"id": "body-0402", "role": "body", "section": "Pushing values", "weight": 1.0} -->

In order to add new values either to the left or to the right, we define list. pushLeft: L K (V) ×V → L K +1 (V) as and list. pushRight: L K (V) ×V → L K +1 (V) as

<!-- chunk {"id": "body-0403", "role": "body", "section": "Popping values", "weight": 1.0} -->

In order to remove values either from the left or from the right, we define list. popLeft: L K (V) →L K -1 (V) ×V as and list. popRight: L K (V) →L K -1 (V) ×V as The set L 0 (V) is a singleton which contains the empty list.

<!-- chunk {"id": "body-0404", "role": "body", "section": "Inserting values", "weight": 1.0} -->

The pushLeft and pushRight functions can only insert values at the beginning and at the end of a list, respectively. We now study the insert function, whose goal is to be able to add a new value at an arbitrary location, shifting all values to the right and increasing the list size by 1. We define the function list. insert: L K (V) × [K +1] ×V → L K +1 (V) as for j ∈ [K +1]. As for the list. set function, list. insert is readily continuous and differentiable in l and v, but not in i, as it is a discrete variable. As special cases, we naturally recover

<!-- chunk {"id": "body-0405", "role": "body", "section": "Differentiability", "weight": 1.0} -->

The list. init, list. push and list. pop functions are readily continuous and differentiable with respect to their arguments (a continuous relaxation is not needed). As for the list. set function, the list. insert function is continuous and differentiable in l and v, but not in i.

<!-- chunk {"id": "body-0406", "role": "body", "section": "Implementation", "weight": 1.0} -->

Under the hood, a variable-length list can be implemented as a linked list or as a dynamic array. A linked list gives O ( K ) random access while a dynamic array allows O random access, at the cost of memory reallocations.

<!-- chunk {"id": "body-0407", "role": "body", "section": "Stacks and queues", "weight": 1.0} -->

The list. pushRight and list. popRight functions can be used to implement a stack (last in first out a.k.a. LIFO behavior). The list. pushLeft and list. popRight functions can be used to implement a queue (first in first out a.k.a. FIFO behavior).

<!-- chunk {"id": "body-0408", "role": "body", "section": "Getting values", "weight": 1.0} -->

In order to be able to differentiate list. get w.r.t. indexing, a natural idea is to replace the integer index i ∈ [K] by a distribution π i ∈ △ K, which we can interpret as a soft index. An integer index i ∈ [K] is then equivalent to a delta distribution π i ∈ { e 1,..., e K }. We define the continuous relaxation list. softGet: L K (V) ×△ K → conv(V) as where cond is studied in Section 5.7. In the particular case V = R, we obtain This is illustrated in Fig. 6.1.

<!-- chunk {"id": "body-0409", "role": "body", "section": "Getting values", "weight": 1.0} -->

The choice of the distribution π i = (π i, 1,..., π i,K) encodes the importance of the elements (l 1,..., l K) w.r.t. l i. If we consider that the smaller | i -j | is, the more related l i and l j are, then it makes sense to define a distribution centered around i (i.e., such that the mode of the distribution is achieved at i). For example, limiting ourselves to the neighbors l i -1 and l i +1 (i.e., a window of size 1), we can define the sparse distribution In this particular case, the continuous relaxation of the list. get function can then be expressed as a discrete convolution, where κ (-1):= 1 4, κ:= 1 4, κ:= 1 2, and κ (j):= 0 for j ̸∈ {-1, 0, 1 }. Assuming V = R M, the computational complexity of list. softGet is O (M · | supp(π i) |).

<!-- chunk {"id": "body-0410", "role": "body", "section": "Setting values", "weight": 1.0} -->

To differentiate w.r.t. indexing, we can define the continuous relaxation list. softSet: L K (V) ×△ K ×V → L K (conv(V)) as where j ∈ [K] and I ∼ Categorical(π i). Equivalently, we can write where ifelse is studied in Section 5.6. Since this relaxation amounts to using an element-wise expectation. As a result, the list output by list. softSet takes values in conv(V) instead of V. Note however that when V = R M, then conv(V) = R M as well.

<!-- chunk {"id": "body-0411", "role": "body", "section": "Inserting values", "weight": 1.0} -->

To differentiate value insertion w.r.t. indexing, we can define the continuous relaxation list. softInsert: L K (V) ×△ K +1 ×V → L K +1 (conv(V)) where I ∼ Categorical(π i). The three necessary probabilities can easily be calculated for j ∈ [K +1] by

<!-- chunk {"id": "body-0412", "role": "body", "section": "Multi-dimensional indexing", "weight": 1.0} -->

In multi-dimensional lists (arrays or tensors), each element li ∈ V of a list l ∈ L K 1,...,K T ( V ) can now be indexed by a multivariate integer i = ( i 1,..., i T ) ∈ [ K 1 ] ×···× [ K T ], where T ∈ N is the number of axes of l. We can always flatten a multi-dimensional list into an uni-dimensional list by replacing the multi-dimensional index i ∈ [ K 1 ] ×··· × [ K T ] by a flat index i ∈ [ K 1... K T ]. The converse operation, converting a flat uni-dimensional array into a multi-dimensional array, is also possible. Therefore, there is a bijection between [ K ] and [ K 1 ] ×··· × [ K T ] for K:= K 1... K T.

<!-- chunk {"id": "body-0413", "role": "body", "section": "Multi-dimensional indexing", "weight": 1.0} -->

This means that the previous discussion on soft indexing in the uni-dimensional setting readily applies to the multi-dimensional setting. All it takes is the ability to define a probability distribution πi ∈ △ K 1 ×···× K T. For example, when working with images, we can define a probability distribution putting probability mass only on the neighboring pixels of pixel i, a standard approach in image processing. Another simple approach is to use a product of axis-wise probability distributions.

<!-- chunk {"id": "body-0414", "role": "body", "section": "Dictionaries", "weight": 1.0} -->

A dictionary (a.k.a. associative array or map) is an unordered list of key-value pairs, such that each possible key appears at most once in the list. We denote the set of keys by K and the set of values by V (both being potentially infinite). We can then define the set of dictionaries of size L from K to V by and one such dictionary by

<!-- chunk {"id": "body-0415", "role": "body", "section": "Getting values", "weight": 1.0} -->

The goal of the dict. get function is to retrieve the value associated with a key, assuming that the dictionary contains this key. Formally, we define the dict. get: D L (K, V) ×K → V ∪ {∞} function as The function is continuous and differentiable in the dictionary d, but not in the key k. Equivalently, we can write the function as The denominator encodes the fact that the function is undefined if no key in the dictionary d matches the key k. Assuming k ∈ { k 1,..., k L } and V = R M, we can also write which shows that we can see dict. get as a nearest neighbor search.

<!-- chunk {"id": "body-0416", "role": "body", "section": "Setting values", "weight": 1.0} -->

The goal of the dict. set function is to replace the value associated with an existing key. Formally, we define the dict. set: D L (K, V) ×K×V → D L (K, V) function as The function leaves the dictionary unchanged if no key in the dictionary matches the input key k. The function is continuous and differentiable in d and v, but not in k.

<!-- chunk {"id": "body-0417", "role": "body", "section": "Implementation", "weight": 1.0} -->

While we view dictionaries as lists of key-value pairs, in practice, a dictionary (a.k.a. associative array) is often implemented using a hash table or search trees. The hardware counterpart of a dictionary is called content-addressable memory (CAM), a.k.a. associative memory.

<!-- chunk {"id": "body-0418", "role": "body", "section": "Continuous relaxation using kernel regression", "weight": 1.0} -->

A dictionary can been seen as a (potentially non-injective) function that associates a value v to each key k. To obtain a continuous relaxation of the operations associated to a dictionary, we can adopt a probabilistic perspective of the mapping from keys to values. We can view keys and values as two continuous random variables K and V. We can express the conditional PDF f (v | k) of V | K in terms of the joint PDF f (k, v) of (K,V) and the marginal PDF f (k) of K as Integrating, we obtain the conditional expectation This is the Bayes predictor, in the sense that E [V | K] is the minimizer of E [(h (K) -V) 2] over the space of measurable functions h: K → V. Using a sample of L input-output pairs (k i, v i), corresponding to key-value pairs in our case, Nadaraya-Watson kernel regression estimates the joint PDF and the marginal PDF using kernel density estimation (KDE).

<!-- chunk {"id": "body-0419", "role": "body", "section": "Continuous relaxation using kernel regression", "weight": 1.0} -->

Using a product of isotropic kernels κ σ and ρ σ for key-value pairs, we can define The corresponding marginal distribution on the keys is then given as Replacing f with ̂ f σ, we obtain the following estimator of the conditional expectation In the above, we assumed that ρ σ (v -v i) = p v i,σ (v), where p v i,σ (v) is the PDF of a distribution whose mean is v i, so that Given a dictionary d = ((k 1, v 1),..., (k L, v L)), we can therefore define the dict. softGet: D L (K, V) ×K → conv(V) function as This kernel regression perspective on dictionaries was previously pointed out by Zhang et al.. It is illustrated in Fig. 6.2 with K = V = R.

<!-- chunk {"id": "body-0420", "role": "body", "section": "Discrete probability distribution perspective", "weight": 1.0} -->

While the set of possible keys K is potentially infinite, the set of keys { k 1,..., k L } ⊂ K associated with a particular dictionary d = ((k 1, v 1),..., (k L, v L)) is finite. To a particular key k, we can therefore associate a discrete probability distribution πk = (π k, 1,..., π k,L) ∈ △ L over the keys (k 1,..., k L) of d, defined by Figure 6.3: Computation graph of the dict. softGet function. We can use a kernel κ σ to produce a discrete probability distribution π k = (π k, 1,..., π k,L) ∈ △ L, that captures the affinity between the dictionary keys (k 1,..., k L) and the input key k. The dict. softGet function can then merely be seen as a convex combination (weighted average) of values (v 1,..., v L) using the probability values (π k, 1,..., π k,L) as weights.

<!-- chunk {"id": "body-0421", "role": "body", "section": "Discrete probability distribution perspective", "weight": 1.0} -->

This distribution captures the affinity between the input key k and the keys (k 1,..., k L) of dictionary d. As illustrated in Fig. 6.3, we obtain In the limit σ → 0, we recover While the dict. get function is using a mapping from keys k ∈ { k 1,..., k L } to integer indices [L], the dict. softGet function is using a mapping from keys k ∈ { k 1,..., k L } to distributions πk ∈ △ L. This perspective allows us to reuse the soft functions we developed for lists in Section 6.1. For example, we can softly replace the value associated with key k by performing Unlike dict. set, the function is differentiable w.r.t. the distribution πk.

<!-- chunk {"id": "body-0422", "role": "body", "section": "Link with attention in Transformers", "weight": 1.0} -->

In the case when κ σ is the Gaussian kernel, assuming that the keys are normalized to have unit norm (which is often the case in practical implementations), we obtain We recognize the softargmax operator. Given, a dictionary d = ((k 1, v 1),..., (k L, v L)), we thus recover attention from Transformers as Transformers can therefore be interpreted as relying on a differentiable dictionary mechanism. Besides Transformers, content-based memory addressing is also used in neural Turing machines.

<!-- chunk {"id": "body-0423", "role": "body", "section": "Summary", "weight": 1.0} -->

- Operations on lists are continuous and differentiable w.r.t. the list, but not w.r.t. the integer index. Similarly, operations on dictionaries are continuous and differentiable w.r.t. the dictionary, but not w.r.t. the input key. - Similarly to the way we handled the predicate in conditionals, we can replace the integer index (respectively the key) with a probability distribution over the indices (respectively the keys). - This allows us to obtain a probabilistic relaxation of operations on lists. In particular, the relaxation for list. get amounts to performing a convolution. The relaxation for dict. get amounts to computing a conditional expectation using kernel regression.

<!-- chunk {"id": "body-0424", "role": "body", "section": "Summary", "weight": 1.0} -->

- When using a Gaussian kernel with keys normalized to unit norm, we recover softargmax attention from Transformers.

<!-- chunk {"id": "body-0425", "role": "body", "section": "Finite differences", "weight": 1.0} -->

One of the simplest way to numerically compute derivatives is to use finite differences, which approximate the infinitesimal definition of derivatives. Finite differences only require function evaluations, and can therefore work with blackbox functions (i.e., they ignore the compositional structure of functions). Without loss of generality, our exposition focuses on computing directional derivatives ∂f ( w )[ v ], for a function f: E → F, evaluated at w ∈ E, in the direction v ∈ E.

<!-- chunk {"id": "body-0426", "role": "body", "section": "Forward differences", "weight": 1.0} -->

From Definition 2.4 and Definition 2.13, the directional derivative and more generally the JVP are defined as a limit, This suggests that we can approximate the directional derivative and the JVP using for some 0 < δ ≪ 1. This formula is called a forward difference. From the Taylor expansion in Section 2.5.4, we indeed have The error incurred by choosing a finite rather than infinitesimal δ in the forward difference formula is called the truncation error. The Taylor approximation above shows that this error is of the order of o (δ).

<!-- chunk {"id": "body-0427", "role": "body", "section": "Forward differences", "weight": 1.0} -->

However, we cannot choose a too small value of δ, because the evaluation of the function f on a computer rounds the value of f to machine precision. Mathematically, a scalar-valued function f evaluated on a computer becomes a function ˜ f such that ˜ f ( w ) ≈ [ f ( w ) /ε ] ε, where [ f ( w ) /ε ] denotes the closest integer of f ( w ) /ε ∈ R and ε is the machine precision, i.e., the smallest non-zero real number encoded by the machine. This means that the difference f ( w + δ v ) -f ( w ) evaluated on a computer is prone to round-off error of the order of o ( ε ). We illustrate the trade-off between truncation and round-off errors in Fig. 7.1.

<!-- chunk {"id": "body-0428", "role": "body", "section": "Backward differences", "weight": 1.0} -->

As an alternative, we can approximate the directional derivative and the JVP by for some 0 < δ ≪ 1. This formula is called a backward difference. From the Taylor expansion in Section 2.5.4, we easily verify that (f (w) -f (w -δ v)) /δ = ∂f (w)[v] + o (δ), so that the truncation error is the same as for the forward difference.

<!-- chunk {"id": "body-0429", "role": "body", "section": "Central differences", "weight": 1.0} -->

Rather than using an asymmetric formula to approximate the derivative, as in forward and backward differences, we can use a symmetric formula for some 0 < δ ≪ 1. This formula is called a central difference. From the Taylor expansion in Section 2.5.4, we have We see that the terms corresponding to derivatives of even order canceled out, allowing the formula to achieve o (δ 2) truncation error.

<!-- chunk {"id": "body-0430", "role": "body", "section": "Central differences", "weight": 1.0} -->

For any δ < 1, the truncation error of the central difference is much smaller than the one of the forward or backward differences as confirmed empirically in Fig. 7.1.

<!-- chunk {"id": "body-0431", "role": "body", "section": "Higher-accuracy finite differences", "weight": 1.0} -->

The truncation error can be further reduced by making use of additional function evaluations. One can generalize the forward difference scheme by a formula of the form requiring p +1 evaluations. To select the a i and reach a truncation error of order o (δ p), we can use a Taylor expansion on each term of the sum to get By grouping the terms in the sum for each order of derivative, we obtain a set of p +1 equations to be satisfied by the p +1 coefficients a 0,..., a p, that is, This system of equations can be solved analytically to derive the coefficients. Backward differences can be generalized similarly by using ∂f (w)[v] ≈ ∑ p i =0 a i δ f (w -iδ v). Similarly, the central difference scheme can be generalized by using to reach a truncation error of order o (δ 2 p). Solving for the coefficients a -p,..., a p as above reveals that a 0 = 0. Therefore, only 2 p evaluations are necessary.

<!-- chunk {"id": "body-0432", "role": "body", "section": "Higher-order finite differences", "weight": 1.0} -->

To approximate higher order derivatives, we can follow a similar reasoning. Namely, we can generalize the forward difference scheme to approximate the derivative of order k by As before, we can expand the terms in the sum. For the approximation to capture only the k th derivative, we now require the coefficients a i to satisfy With the resulting coefficients, we obtain a truncation error of order o (δ p -k +1), while making p +1 evaluations. For example, for p = k = 2, we can approximate the second-order derivative as with a truncation error of order o (δ).

<!-- chunk {"id": "body-0433", "role": "body", "section": "Higher-order finite differences", "weight": 1.0} -->

The central difference scheme can be generalized similarly by to reach truncation errors of order o (δ 2 p +2 -2 ⌈ (k +1) / 2 ⌉). For example, for k = 2, p = 1, we obtain the second-order central difference By using a Taylor expansion we see that, this time, the terms corresponding to derivatives of odd order cancel out and the truncation error is o (δ 2) while requiring 3 evaluations.

<!-- chunk {"id": "body-0434", "role": "body", "section": "Complex-step derivatives", "weight": 1.0} -->

Suppose f is well defined on C P, the space of P -dimensional complex numbers. Let us denote the imaginary unit by i = √ -1. Then, the Taylor expansion of f reads We see that the real part corresponds to even-degree terms and the imaginary part corresponds to odd-degree terms. We therefore obtain This suggests that we can compute directional derivatives using the approximation for 0 < δ ≪ 1. This is called the complex-step derivative approximation.

<!-- chunk {"id": "body-0435", "role": "body", "section": "Complex-step derivatives", "weight": 1.0} -->

Contrary to forward, backward and central differences, we see that only a single function call is necessary. A function call on complex numbers may take roughly twice the cost of a function call on real numbers. However, thanks to the fact that a difference of functions is no longer needed, the complex-step derivative approximation usually enjoys smaller round-off error as illustrated in Fig. 7.1. That said, one drawback of the method is that all elementary operations within the program implementing the function f must be well-defined on complex numbers, e.g., using overloading.

<!-- chunk {"id": "body-0436", "role": "body", "section": "Complex-step derivatives", "weight": 1.0} -->

Table 7.1: Computational complexity in number of function evaluations for computing the directional derivative and the gradient of a function f: R P → R by finite differences and complex step derivatives.

<!-- chunk {"id": "body-0437", "role": "body", "section": "Complexity", "weight": 1.0} -->

We now discuss the computational complexity in terms of function evaluations of finite differences and complex-step derivatives. For concreteness, as this is the most common use case in machine learning, we discuss the case of a single M = 1 output, i.e., we want to differentiate a function f: R P → R. Whether we use forward, backward or central differences, the computational complexity of computing the directional derivative ∂f (w)[v] in any direction v amounts to two calls to f. For computing the gradient ∇ f (w), we can use (see Definition 2.7) that for j ∈ [P]. For forward and backward differences, we therefore need P +1 function calls to compute the gradient, while we need 2 P function calls for central differences. For the complex step approximation, we need P complex function calls. We summarize the complexities in Table 7.1.

<!-- chunk {"id": "body-0438", "role": "body", "section": "Summary", "weight": 1.0} -->

- Finite differences are a simple way to numerically compute derivatives using only function evaluations. - Central differences achieve smaller truncation error than forward and backward differences. It is possible to achieve smaller truncation error, at the cost of more function evaluations.

<!-- chunk {"id": "body-0439", "role": "body", "section": "Summary", "weight": 1.0} -->

- Complex-step derivatives achieve smaller round-off error than central differences but require the function and the program implementing it to be well-defined on complex numbers. - However, whatever the method used, finite differences require a number of function calls that is proportional to the number of dimensions. They are therefore seldom used in machine learning, where there can be millions or billions of dimensions. The main use cases of finite differences are therefore i) for blackbox functions of low dimension and ii) for test purposes (e.g., checking that a gradient function is correctly implemented). - For modern machine learning, the main workhorse is automatic differentiation, as it leverages the compositional structure of functions. This is what we study in the next chapter.

<!-- chunk {"id": "body-0440", "role": "body", "section": "Automatic differentiation", "weight": 1.0} -->

In Chapter 2, we reviewed the fundamentals of differentiation and stressed the importance of two linear maps: the Jacobian-vector product (JVP) and its adjoint, the vector-Jacobian product (VJP). In this chapter, we review forward-mode and reverse-mode autodiff using these two linear maps. We start with computation chains and then generalize to feedforward networks and general computation graphs. We also review checkpointing, reversible layers and randomized estimators.

<!-- chunk {"id": "body-0441", "role": "body", "section": "Computation chains", "weight": 1.0} -->

To begin, consider a computation chain (Section 4.1.1) representing a function f: S 0 →S K expressed as a sequence of compositions f:= f K ◦ · · · ◦ f 1, where f k: S k -1 →S k. The computation of f can be unrolled into a sequence of operations Our goal is to compute the variations of f around a given input s 0. In a feedforward network, this amounts to estimating the influence of a given input s 0 for fixed parameters (we will see how to estimate the variations w.r.t. parameters w in the sequel).

<!-- chunk {"id": "body-0442", "role": "body", "section": "Computation chains", "weight": 1.0} -->

Jacobian matrix. We first consider the computation of the full Jacobian ∂ f (s 0), seen as a matrix, as the notation ∂ indicates. Following Proposition 2.2, we have where ∂ f k (s k -1) are the Jacobians of the intermediate functions computed at s 0,..., s K, as defined in Eq. (8.1). We may also want to compute the tranpose of the Jacobian In both cases, the main drawback of this approach is computational: computing the full ∂ f (s 0) requires to materialize the intermediate Jacobians in memory and to perform matrix-matrix multiplications. However, in practice, computing the full Jacobian is rarely needed. Indeed, oftentimes, we only need to right-multiply or left-multiply with ∂ f (s 0). This gives rise to forward-mode and reverse-mode autodiff, respectively.

<!-- chunk {"id": "body-0443", "role": "body", "section": "Forward-mode", "weight": 1.0} -->

We now interpret the Jacobian ∂f (s 0) as a linear map, as the non-bold ∂ indicates. Following Proposition 2.6, ∂f (s 0) is the composition of the intermediate linear maps, Figure 8.1: Forward-mode autodiff for a computation chain. For readability, we denoted the intermediate JVP as a function of two variables ∂f k: s k -1, t k -1 ↦→ ∂f k (s k -1)[t k -1] with ∂f k (s k -1)[t k -1] = t k.

<!-- chunk {"id": "body-0444", "role": "body", "section": "Forward-mode", "weight": 1.0} -->

Evaluating ∂f (s 0) on an input direction v ∈ S 0 can be decomposed, like the function Eq. (8.1) itself, into intermediate computations Each intermediate ∂f k (s k -1)[t k -1] amounts to a Jacobian-vector product (JVP) and can be performed in a forward manner, along the computation of the intermediate states s k. This can also be seen as multiplying the matrix defined in Eq. (8.2) with a vector, from right to left. This is illustrated in Fig. 8.1 and the procedure is summarized in Algorithm 8.1.

<!-- chunk {"id": "body-0445", "role": "body", "section": "Forward-mode", "weight": 1.0} -->

Computational complexity. The JVP follows exactly the computations of f, with an additional variable t k being propagated. If we consider that computing ∂f k is roughly as costly as computing f k, then computing a

<!-- chunk {"id": "body-0446", "role": "body", "section": "Algorithm 8.1", "weight": 1.0} -->

Functions: f f K ◦... ◦ f 1 Inputs: input s 0 ∈ S 0, input direction v ∈ S 0 1: Initialize t 0:= v 2: for k:= 1,..., K do 3: Compute s k:= f k (s k -1) ∈ S k 4: Compute t k:= ∂f k (s k -1)[t k -1] ∈ S k Outputs: f (s 0):= s K, ∂f (s 0)[v] = t K Forward-mode autodiff for computation chains:= JVP has roughly twice the computational cost of f. See Section 8.3.3 for a more general and more formal statement.

<!-- chunk {"id": "body-0447", "role": "body", "section": "Algorithm 8.1", "weight": 1.0} -->

Memory usage. The memory usage of a program at a given evaluation step is the number of variables that need to be stored in memory to ensure the execution of all remaining steps. The memory cost of a program is then the maximal memory usage over all evaluation steps. For our purposes, we analyze the memory usage and memory cost by examining the given program. Formal definitions of operations on memory such as read, write, delete and associated memory costs are presented by Griewank and Walther.

<!-- chunk {"id": "body-0448", "role": "body", "section": "Algorithm 8.1", "weight": 1.0} -->

For example, to execute the chain f = f K ◦ · · · ◦ f 1, at each step k, we only need to have access to s k -1 to execute the rest of the program. As we compute s k, we can delete s k -1 from memory and replace it by s k. Therefore, the memory cost associated to the evaluation of f is just the maximal dimension of the s k variables.

<!-- chunk {"id": "body-0449", "role": "body", "section": "Algorithm 8.1", "weight": 1.0} -->

For forward mode autodiff, as we follow the computations of f, at each step k, we only need to have access to s k -1 and t k -1 to execute the rest of the program. The memory used by s k -1 and t k -1 can directly be used for s k, t k once they are computed. The memory usage associated to the JVP is summarized in Fig. 8.2. Overall the memory cost of the JVP is then exactly twice the memory cost of the function itself.

<!-- chunk {"id": "body-0450", "role": "body", "section": "Reverse-mode", "weight": 1.0} -->

In machine learning, most functions whose gradient we need to compute take the form ℓ ◦ f, where ℓ is a scalar-valued loss function and f is a network. As seen in Proposition 2.3, the gradient takes the form This motivates the need for applying the adjoint ∂f (s 0) ∗ to ∇ ℓ (f (s 0)) ∈ S K and more generally to any output direction u ∈ S K. From Proposition 2.7, we have Evaluating ∂f (s 0) ∗ on an output direction u ∈ S K is decomposed as Each intermediate adjoint ∂f k (s k -1) ∗ amounts to a vector-Jacobian product (VJP). The key difference with the forward mode is that the procedure runs backward through the chain, hence the name reverse mode autodiff. This can also be seen as multiplying Eq. (8.2) from left to right. The procedure is illustrated in Fig. 8.3 and summarized in Algorithm 8.2.

<!-- chunk {"id": "body-0451", "role": "body", "section": "Algorithm 8.2 Reverse-mode autodiff for computation chains", "weight": 1.0} -->

- 1: for k:= 1,..., K do ▷ Forward pass - for k:= K,..., 1 do ▷ Backward pass Inputs: input s 0 ∈ S 0, output direction u ∈ S K Figure 8.4: Memory usage of reverse mode autodiff for a computation chain.

<!-- chunk {"id": "body-0452", "role": "body", "section": "Algorithm 8.2 Reverse-mode autodiff for computation chains", "weight": 1.0} -->

Computational complexity. In terms of number of operations, the VJP simply passes two times through the chain, once forward, then backward. If we consider the intermediate VJPs to be roughly as costly as the intermediate functions themselves, the VJP amounts just to twice the cost of the original function, just as the JVP. See Section 8.3.3 for a more generic and formal statement.

<!-- chunk {"id": "body-0453", "role": "body", "section": "Algorithm 8.2 Reverse-mode autodiff for computation chains", "weight": 1.0} -->

Memory usage. Recall that the memory usage of a program at a given evaluation step is the number of variables that need to be stored in memory to ensure the execution of the remaining steps. If we inspect Algorithm 8.3, to execute all backward steps, that is the loop in line 4, we need to have access to all the intermediate inputs s 0,..., s K -1. Therefore, the memory cost of reverse-mode autodiff is proportional to the length of the chain K. Fig. 8.4 illustrates the memory usage during reverse mode autodiff. It grows linearly until the end of the forward pass and then progressively decreases until it outputs the value of the function and the VJP. The memory cost can be mitigated by means of checkpointing techniques presented in Section 8.5.

<!-- chunk {"id": "body-0454", "role": "body", "section": "Algorithm 8.2 Reverse-mode autodiff for computation chains", "weight": 1.0} -->

Decoupled function and VJP evaluations. The additional memory cost of reverse mode autodiff comes with some advantages. If we need to compute ∂f (s 0) ∗ [u i] for n different output directions u i, we only need to compute and store once the intermediate computations s k and then make n calls to the backward pass. In other words, by storing in memory the intermediate computations s k, we may instantiate a VJP operator, which we may apply to any u through the backward pass. Formally, the forward and backward passes can be decoupled as In functional programming terminology, the VJP ∂f (s 0) ∗ is a closure, as it contains the intermediate computations s 0,... s K. The same can be done for the JVP ∂f (s 0) if we want to apply to multiple directions v i.

<!-- chunk {"id": "body-0455", "role": "body", "section": "Algorithm 8.2 Reverse-mode autodiff for computation chains", "weight": 1.0} -->

Example 8.1 (Multilayer perceptron with fixed parameters). As a running example, consider a multilayer perceptron (MLP) with one hidden layer and (for now) given fixed weights. As presented in Chapter 4, an MLP can be decomposed as for A 1, A 2, b 1, b 2 some fixed parameters and σ an activation function such as the softplus activation function σ (x) = log(1+ e x) with derivative σ ′ (x) = e x / (1 + e x).

<!-- chunk {"id": "body-0456", "role": "body", "section": "Algorithm 8.2 Reverse-mode autodiff for computation chains", "weight": 1.0} -->

Evaluating the JVP of f on an input x along a direction v can then be decomposed as where we used in the second line the JVP of element-wise function as in Example 8.4.

<!-- chunk {"id": "body-0457", "role": "body", "section": "Algorithm 8.2 Reverse-mode autodiff for computation chains", "weight": 1.0} -->

Evaluating the VJP of f at x requires to evaluate the intermediate VJPs at the stored activations

<!-- chunk {"id": "body-0458", "role": "body", "section": "Complexity of computing entire Jacobians", "weight": 1.0} -->

In this section, we analyze the time and space complexities of forwardmode and reverse-mode autodiff for computing the entire Jacobian matrix ∂ f ( s 0 ) of a computation chain f = f K ◦· · ·◦ f 1, where f k: S k -1 → S k. We assume S k ⊆ R D k, D K = M and D 0 = D. Therefore, we have f: R D → R M and ∂ f ( s 0 ) ∈ R M × D.

<!-- chunk {"id": "body-0459", "role": "body", "section": "Complexity of forward-mode autodiff", "weight": 1.0} -->

Using Definition 2.9, we find that we can extract each column [∂ f (s 0)]:,j ∈ R M of the Jacobian matrix, for j ∈ [D], by multiplying with the standard basis vector e j ∈ R D: Computing the full Jacobian matrix therefore requires D JVPs with vectors in R D. Assuming each f k in the chain composition has the form f k: R D k -1 → R D k, seen as a matrix, ∂ f k (s k -1) has size D k × D k -1. Therefore, the computational cost of D JVPs is O (D ∑ K k =1 D k D k -1). The memory cost is O (max k ∈ [K] D k), since we can release intermediate computations after each layer is processed. Setting D 1 = · · · = D K -1 = D for simplicity and using D K = M, we obtain that the computational cost of computing D JVPs and therefore of computing the full Jacobian matrix by forward-mode autodiff is O (MD 2 + KD 3). The memory cost is O (max { D,M }).

<!-- chunk {"id": "body-0460", "role": "body", "section": "Complexity of forward-mode autodiff", "weight": 1.0} -->

If a function has a single-input (D = 1), then the forward mode computes the entire Jacobian at once, which reduces to a single directional derivative.

<!-- chunk {"id": "body-0461", "role": "body", "section": "Complexity of reverse-mode autodiff", "weight": 1.0} -->

Using Definition 2.9, we find that we can extract each row of the Jacobian matrix [∂ f (s 0)] i ∈ R D, for i ∈ [M], by multiplying with the standard basis vector e i ∈ R M: Computing the full Jacobian matrix therefore requires M VJPs with vectors in R M. Assuming as before that each f k in the chain composition has the form f k: R D k -1 → R D k, the computational cost of M VJPs is O (M ∑ K k =1 D k D k -1). However, the memory cost is O (∑ K k =1 D k), as we need to store the intermediate computations for each of the K layers. Setting D 0 = · · · = D K -1 = D for simplicity and using D K = M, we obtain that the computational cost of computing M VJPs and therefore of computing the full Jacobian matrix by reverse-mode autodiff is O (M 2 D + KMD 2). The memory cost is O (KD + M).

<!-- chunk {"id": "body-0462", "role": "body", "section": "Complexity of reverse-mode autodiff", "weight": 1.0} -->

If the function has a single output (M = 1), reverse-mode autodiff computes the entire Jacobian at once, which reduces to the gradient.

<!-- chunk {"id": "body-0463", "role": "body", "section": "When to use forward-mode vs. reverse-mode autodiff?", "weight": 1.0} -->

We summarize the time and space complexities in Table 8.1. Generally, if M < D, reverse-mode is more advantageous at the price of some memory cost. If M ≥ D, forward mode is more advantageous.

<!-- chunk {"id": "body-0464", "role": "body", "section": "When to use forward-mode vs. reverse-mode autodiff?", "weight": 1.0} -->

Table 8.1: Time and space complexities of forward-mode and reverse-mode autodiff for computing the full Jacobian of a chain of functions f = f K ◦ · · · ◦ f 1, where f k: R D → R D if k = 1,..., K -1 and f K: R D → R M. We assume ∂f k is a dense linear operator. Forward mode requires D JVPs. Reverse mode requires M VJPs.

<!-- chunk {"id": "body-0465", "role": "body", "section": "Feedforward networks", "weight": 1.0} -->

In the previous section, we derived forward-mode autodiff and reversemode autodiff for computation chains with an input s 0 ∈ S 0. In this section, we now derive reverse-mode autodiff for feedforward networks, in which each layer f k is now allowed to depend explicitly on some additional parameters w k ∈ W k. The recursion is where S 0 = X and w = (w 1,..., w K) ∈ W 1 × · · · × W K. Each f k is now a function of two arguments. The first argument depends on the previous layer, but the second argument does not. This is illustrated in Fig. 8.5. We now explain how to differentiate a feedforward network.

<!-- chunk {"id": "body-0466", "role": "body", "section": "Computing the adjoint", "weight": 1.0} -->

The function has the form f: E → F, where E:= X × ( W 1 × · · · × W K ) and F:= S K. From Section 2.3, we know that the VJP has the form ∂f ( x, w ) ∗: F → E. Therefore, we want to be able to compute ∂f ( x, w ) ∗ [ u ] ∈ E for any u ∈ F.

<!-- chunk {"id": "body-0467", "role": "body", "section": "Computing the adjoint", "weight": 1.0} -->

Fortunately, the backward recursion is only a slight modification of the computation chain case. Indeed, since f k: E k → F k, where E k:= S k -1 ×W k and F k:= S k, the intermediate VJPs have the form ∂f k (s k -1, w k) ∗: F k →E k. We therefore arrive at the recursion The final output is

<!-- chunk {"id": "body-0468", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

We often compose a network with a loss function From Proposition 2.7, the gradient is given by with u = ∇ ℓ (f (x, w); y) ∈ S K. The output r 0 ∈ S 0, where S 0 = X, corresponds to the gradient w.r.t. x ∈ X and is typically not needed, except in generative modeling settings. The full procedure is summarized in Algorithm 8.3.

<!-- chunk {"id": "body-0469", "role": "body", "section": "Computing the gradient", "weight": 1.0} -->

Functions: f 1,..., f K in sequential order Inputs: data point (x, y) ∈ X × Y parameters w = (w 1,... w K) ∈ W 1 ×··· × W K 1: Initialize s 0:= x ▷ Forward pass 2: for k:= 1,..., K do 3: Compute and store s k:= f k (s k -1, w k) ∈ S k 4: Compute ℓ (s K; y) and u:= ∇ ℓ (s K; y) ∈ S K 5: Initialize r K:= u ∈ S K ▷ Backward pass 6: for k:= K,..., 1 do 7: Compute (r k -1, g k):= ∂f k (s k -1, w k) ∗ [r k] ∈ S k -1 ×W k 8: Outputs: L (w; x, y):= ℓ (s K; y), ∇ L (w; x, y) = (g 1,..., g K) Algorithm 8.3 Gradient back-propagation for feedforward networks

<!-- chunk {"id": "body-0470", "role": "body", "section": "Computation graphs", "weight": 1.0} -->

In the previous sections, we reviewed autodiff for computation chains and its extension to feedforward networks. In this section, we review its generalization to computation graphs, introduced in Section 4.1.3. Our formalism assumes, without loss of generality, that functions can take multiple inputs but only produce a single output, as we can always group multiple outputs as a tuple. This enables a one-to-one correspondence between output variables s k and functions f k.

<!-- chunk {"id": "body-0471", "role": "body", "section": "Forward mode", "weight": 1.0} -->

The forward mode corresponds to computing the JVP of the program in an input direction v ∈ S 0. In the case of a computation chain f:= f K ◦ · · · ◦ f 1, each f k takes a single input s k -1 ∈ S k -1 and each ∂f k (s k -1) takes a single input direction t k -1 ∈ S k -1. The forward pass on iteration k ∈ [K] is then, starting from t 0:= v, In the case of a computation graph, specified by functions f 1,..., f K in topological order, each f k may now take multiple inputs (s i 1,..., s i p k) ∈ S i 1 ×··· × S i p k, and each ∂f k (s i 1,..., s i p k) takes as many input directions (t i 1,..., t i p k) ∈ S i 1 ×··· × S i p k, where (i 1,..., i p k):= pa(k) are the parents of f k.

<!-- chunk {"id": "body-0472", "role": "body", "section": "Forward mode", "weight": 1.0} -->

The forward pass on step k ∈ [K] then computes both intermediate inputs and directions as Let us recall that ∂ i f k means that we differentiate f k w.r.t. to its i th argument. Using the fan-in rule in Proposition 2.8, we obtain that the derivatives are propagated as The final output is ∂f (s 0)[v] = t K. The resulting generic forward-mode procedure is summarized in Fig. 8.7 and in Algorithm 8.4. Intuitively, the algorithm consists in computing and summing intermediate JVPs along the forward pass. Although not explicitly mentioned, we can release s k and t k from memory when no child node depends on node k.

<!-- chunk {"id": "body-0473", "role": "body", "section": "Algorithm 8.4 Forward-mode autodiff for computation graphs", "weight": 1.0} -->

- 2: for k:= 1,..., K do ▷ Forward pass input s 0 ∈ S 0, input direction v ∈ S 0

<!-- chunk {"id": "body-0474", "role": "body", "section": "Reverse mode", "weight": 1.0} -->

The reverse mode corresponds to computing the VJP of the program in an output direction u ∈ S K. In the case of a computation chain f:= f K ◦ · · · ◦ f 1, each intermediate variable s k is used only once to compute the next variable s k +1:= f k +1 (s k). To compute the VJP of the chain, it then suffices to reverse the order of the operations and to use the corresponding VJPs. Since each function takes a single input, each VJP ∂f k (s k) ∗ [r k] produces a single output direction r k -1 ∈ S k. A backward pass therefore computes from k:= K to k:= 1, starting from r K:= u, The final output is r 0:= ∂f (s 0) ∗ [u].

<!-- chunk {"id": "body-0475", "role": "body", "section": "Reverse mode", "weight": 1.0} -->

In computation graphs, intermediate variables may be used more than once, since a node k may have several children nodes. This complicates reversing the computation graph. To circumvent this issue, following the formalism of Roy Frostig, we may formally distinguish between the output s k of f k and the inputs s k → j of f j for j ∈ ch(k), the children of f k. We do so by introducing an operation that simply duplicates s k, The tuple output by dup is of length | ch(k) |. The forward pass can then be formally rewritten as, for k ∈ [K], where (j 1,..., j c k):= ch(k). The benefit of this approach is that each duplicated output is input only once to the subsequent child functions. Thanks to this, we can now associate to each variable, s i → j or s k, a single corresponding intermediate variable, r i → j or r k, in the backward pass. The reverse mode can then simply be written by going through the VJPs of the functions f k and the VJP of dup in reverse order.

<!-- chunk {"id": "body-0476", "role": "body", "section": "Reverse mode", "weight": 1.0} -->

For the VJP of the dup operation, let us denote the intermediate variables in the backward pass associated to s k → j 1,..., s k → j c k by r k → j 1,..., r k → j c k. Following the fan-out rule in Proposition 2.9, the VJP of the dup operation on iteration k is In the last line, we used that dup i (s) = s by definition of the duplication operation so ∂ dup i (s) = I and ∂ dup i (s) ∗ = I. The VJP of dup justifies why, if an intermediate value s k is used by later functions f j 1,..., f j c k, for (j 1,..., j c k):= ch(k), the derivatives with respect to s k need to sum all the variations through the f j functions into the variable r k.

<!-- chunk {"id": "body-0477", "role": "body", "section": "Reverse mode", "weight": 1.0} -->

For the VJP of the f k functions, following the fan-in rule in Proposition 2.8, the VJP returns multiple output variations, The overall formalism is summarized in Fig. 8.8.

<!-- chunk {"id": "body-0478", "role": "body", "section": "Implementation", "weight": 1.0} -->

The duplication operation dup is just a formalism to mathematically derive the reverse mode. In practice, the variables s k are not duplicated but accessed several times during the backward pass. The variables r k are computed by accumulating r k → j into r k each time a variable r k → j is computed. Therefore, for each k ∈ [K], we can compute the VJP and perform the in-place updates, Figure 8.8: Reverse mode automatic differentiation in a computation graph.

<!-- chunk {"id": "body-0479", "role": "body", "section": "Algorithm 8.5 Reverse-mode autodiff for computation graphs", "weight": 1.0} -->

- Functions: f 1,..., f K in topological order Inputs: input s 0 ∈ S 0, output direction u ∈ S K 1: for k:= 1,..., K do ▷ Forward pass 2: Retrieve parent nodes (i 1,..., i p k):= pa(k) 3: Compute s k:= f k (s i 1,..., s i p k) ∈ S k 4: Instantiate VJP l k:= ∂f k (s i 1,..., s i p k) ∗ 5: Initialize r K:= u, r k ← 0 ∀ k ∈ { 0,..., K -1 } ▷ Backward pass 6: for k:= K,..., 1 do 7: Retrieve parent nodes (i 1,..., i p k) = pa(k) 8: Compute r i 1 → k,..., r i p k → k:= l k [r k] 9: Compute r i j ← r i j + r i j → k ∈ S i j ∀ j ∈ { 1,...,

<!-- chunk {"id": "body-0480", "role": "body", "section": "Algorithm 8.5 Reverse-mode autodiff for computation graphs", "weight": 1.0} -->

Outputs: f (s 0):= s K ∈ S K, ∂f (s 0) ∗ [u] = r 0 ∈ S 0 The topological ordering ensures that r k has been fully computed when we reach f k. The resulting generic reverse-mode procedure is presented in Algorithm 8.5.

<!-- chunk {"id": "body-0481", "role": "body", "section": "Algorithm 8.5 Reverse-mode autodiff for computation graphs", "weight": 1.0} -->

Example 8.2 (Example of forward and reverse modes). Weuse Fig. 8.9 to illustrate the forward and reverse modes in a computation graph. Let us assume that the intermediate variables s 1,..., s 7 have readily been computed. The forward mode corresponds to Figure 8.9: Same computation graph as Fig. 4.3 but without the actual definition of each f k, for simplicity.

<!-- chunk {"id": "body-0482", "role": "body", "section": "Complexity, the Baur-Strassen theorem", "weight": 1.0} -->

For computing the gradient of a function f: E → R represented by a computation graph, we saw that the reverse mode is more efficient than the forward mode. As we previously stated, assuming that the elementary functions f k in the DAG and their VJP have roughly the same computational complexity, then f and ∇ f have roughly the same computational complexity. This fact is crucial and is the pillar on which modern machine learning relies: it allows us to optimize high-dimensional functions by gradient descent.

<!-- chunk {"id": "body-0483", "role": "body", "section": "Complexity, the Baur-Strassen theorem", "weight": 1.0} -->

For arithmetic circuits, reviewed in Section 4.1.4, this crucial fact is made more precise in the celebrated Baur-Strassen theorem. If f is a polynomial, then so is its gradient ∇ f. The theorem gives an upper bound on the size of the best circuit for computing ∇ f from the size of the best circuit for computing f.

<!-- chunk {"id": "body-0484", "role": "body", "section": "Complexity, the Baur-Strassen theorem", "weight": 1.0} -->

Proposition 8.1 (Baur-Strassen's theorem). f: E → R, we have where the size S (f) of a polynomial f is defined in Definition 4.1.

<!-- chunk {"id": "body-0485", "role": "body", "section": "Complexity, the Baur-Strassen theorem", "weight": 1.0} -->

A simpler proof by backward induction was given by Morgenstern. See also the proof of Theorem 9.10 in Chen et al.. For general computation graphs, that have more primitive functions than just + and ×, a similar result can be obtained; see, e.g.,.

<!-- chunk {"id": "body-0486", "role": "body", "section": "Primitive functions", "weight": 1.0} -->

An autodiff system implements a set A of primitive or elementary functions, which serve as building blocks for creating other functions, by function composition. For instance, we saw that in arithmetic circuits (Section 4.1.4), A = { +, ×}. More generally, A may contain all the necessary functions for expressing programs. We emphasize, however, that A is not necessarily restricted to low-level functions such as log For any polynomial and exp, but may also contain higher-level functions. For instance, even though the log-sum-exp can be expressed as the composition of elementary operations (log, sum, exp), it is usually included as a primitive on its own, both because it is a very commonly-used building block, but also for numerical stability reasons.

<!-- chunk {"id": "body-0487", "role": "body", "section": "Closure under function composition", "weight": 1.0} -->

Each function f k in a computation graph belongs to a set F, the class of functions supported by the system. A desirable property of an autodiff implementation is that the set F is closed under function composition, meaning that if f ∈ F and g ∈ F, then f ◦ g ∈ F. This means that composed functions can themselves be used for composing new functions. This property is also crucial for supporting higher-order differentiation (Chapter 9) and automatic linear transposition (Section 8.4.4). When f k is a composition of elementary functions in A, then f k itself is a nested DAG. However, we can always inline each composite function, such that all functions in the DAG belong to A.

<!-- chunk {"id": "body-0488", "role": "body", "section": "Examples of JVPs and VJPs", "weight": 1.0} -->

An autodiff system must implement for each f ∈ A its JVP for supporting the forward mode, and its VJP for supporting the reverse mode. We give a couple of examples. We start with the JVP and VJP of linear functions.

<!-- chunk {"id": "body-0489", "role": "body", "section": "Examples of JVPs and VJPs", "weight": 1.0} -->

Example 8.3 (JVP and VJP of linear functions). Consider the matrixvector product f (W) = Wx ∈ R M, where x ∈ R D is fixed and W ∈ R M × D. As already mentioned in Section 2.3.1, the JVP of f at W ∈ R M × D along an input direction V ∈ R M × D is simply To find the associated VJP, we note that for any u ∈ R M and V ∈ R M × D, we must have 〈 ∂f (W)[V], u 〉 = 〈 V, ∂f (W) ∗ [u] 〉. Using the properties of the trace, we have Therefore, we find that the VJP is given by Similarly, consider now a matrix-matrix product f (W) = WX, where W ∈ R M × D and where X ∈ R D × N is fixed. The JVP at W ∈ R M × D along an input direction V ∈ R M × D is simply The VJP along the output direction U ∈ R M × N is Another simple example are element-wise separable functions.

<!-- chunk {"id": "body-0490", "role": "body", "section": "Examples of JVPs and VJPs", "weight": 1.0} -->

Example 8.4 (JVP and VJP of separable function). Consider the function f (w):= (g 1 (w 1),..., g P (w P)), where each g i: R → R has a derivative g ′ i. The Jacobian matrix is then a diagonal matrix In this case, the JVP and VJP are actually the same where ⊙ indicates element-wise multiplication.

<!-- chunk {"id": "body-0491", "role": "body", "section": "Automatic linear transposition", "weight": 1.0} -->

On first sight, if we want to support both forward ans reverse modes, it appears like we need to implement both the JVP and the VJP for each primitive operation f ∈ A. Fortunately, there exists a way to recover VJPs from JVPs, and vice-versa.

<!-- chunk {"id": "body-0492", "role": "body", "section": "Automatic linear transposition", "weight": 1.0} -->

Let us define l (u; w):= ∂f (w) ∗ [u], i.e., the VJP of f in the output direction u. Since l (u; w) is linear in u, we can apply the reasoning We saw in Section 2.3 that if l (w) is a linear map, then its JVP is ∂l (w)[v] = l (v) (independent of w). Conversely, the VJP is ∂l (w) ∗ [u] = l ∗ (u), where l ∗ is the adjoint operator of l (again, independent of w). above to compute its VJP which is independent of u. In words, the VJP of a VJP is the corresponding JVP! This means that we can implement forward-mode autodiff even if we only have access to VJPs. As an illustration and sanity check, we give the following example.

<!-- chunk {"id": "body-0493", "role": "body", "section": "Automatic linear transposition", "weight": 1.0} -->

Example 8.5 (Automatic transpose of 'dot'). If we define f (x, W):= Wx, from Example 8.3, we know that Using Proposition 2.9, we obtain The other direction, automatically creating a VJP from a JVP, is also possible but is more technical and relies on the notion of partial evaluation.

<!-- chunk {"id": "body-0494", "role": "body", "section": "Checkpointing", "weight": 1.0} -->

We saw that forward-mode autodiff can release intermediate computations from memory along the way, while reverse-mode autodiff needs to cache all of them. This means that the memory complexity of reversemode autodiff, in its standard form, grows linearly with the number of nodes in the computation graph. A commonly-used technique to circumvent this issue is checkpointing, which trades-off computation time for better memory usage. Checkpointing works by selectively storing only a subset of the intermediate values, called checkpoints, and by recomputing others on the fly. The specific choice of the checkpoint locations in the computation graph determines the memory-computation trade-off. While it is possible to heuristically set checkpoints at userspecified locations, it is also possible to perform a checkpointing strategy algorithmically, as studied in depth by Griewank and Griewank and Walther. In this section, we review two divide-an-conquer algorithms: recursive halving and dynamic programming. Our exposition focuses on computation chains f = f K ◦... ◦ f 1, with f k: R D → R D for simplicity.

<!-- chunk {"id": "body-0495", "role": "body", "section": "Computational and memory complexities at two extremes. Let C ( K )", "weight": 1.0} -->

be the number of calls to the individual functions f k (we ignore the cost of computing the intermediate VJPs) and M (K) be the number of function inputs cached, when performing reverse-mode autodiff on a chain f = f K ◦... ◦ f 1. On one extreme, if we store all intermediate computations, as done in Algorithm 8.1, to compute only the VJP ∂f (s 0) ∗ [u], we have This is optimal w.r.t. computational complexity, but suboptimal w.r.t. memory. On the other extreme, if we only store the initial input, as Algorithm 8.6 Reverse-mode autodiff with constant memory vjp_full_recompute (f K ◦... ◦ f 1, s 0, u):= ∂ (f K ◦... ◦ f 1)(s 0) ∗ [u] Inputs: Chain f K ◦.

<!-- chunk {"id": "body-0496", "role": "body", "section": "Computational and memory complexities at two extremes. Let C ( K )", "weight": 1.0} -->

◦ f 1, input s 0 ∈ S 0, output direction u ∈ S K 1: if K = 1 then 2: return ∂f 1 (s 0) ∗ [u] 3: else 4: Set r K = u 5: for k:= K,..., 1 do 6: Compute s k -1 = (f k -1 ◦... ◦ f 1)(s 0) 7: Compute r k -1 = ∂f k (s k -1) ∗ [r k] 8: return: r 0 done in Algorithm 8.6, then we have This is optimal w.r.t. memory but leads to a computational complexity that is quadratic in K.

<!-- chunk {"id": "body-0497", "role": "body", "section": "Recursive halving", "weight": 1.0} -->

As a first step towards obtaining a better computation-memory trade-off, we may split the chain s K = f K ◦ · · · ◦ f 1 (s 0) as for K even. Then, rather than recomputing all intermediate computations s k from the input s 0 as in Algorithm 8.6, we can store s K/ 2 and recompute s k for k > K/ 2 starting from s K/ 2. Formally, this strategy amounts to the following steps. 2. Compute r K/ 2 = vjp\_full\_recompute (f K ◦... ◦ f K/ 2+1, s K/ 2, u) 3. Compute r 0 = vjp\_full\_recompute (f K/ 2 ◦... ◦ f 1, s 0, r K/ 2) Algorithm 8.7 Reverse-mode autodiff with recursive halving vjp_halving (f K ◦... ◦ f 1, s 0, u):= ∂ (f K ◦... ◦ f 1)(s 0) ∗ [u] Functions: Chain f K ◦.

<!-- chunk {"id": "body-0498", "role": "body", "section": "Recursive halving", "weight": 1.0} -->

◦ f 1 Inputs: input s 0 ∈ S 0, output direction u ∈ S K 1: if K = 1 then 2: return ∂f 1 (s 0) ∗ [u] 3: else 4: Compute s K/ 2 = f K/ 2 ◦... ◦ f 1 (s 0) 5: Compute r K/ 2 = vjp_halving (f K ◦... ◦ f K/ 2+1, s K/ 2, u) 6: Compute r 0 = vjp_halving (f K/ 2 ◦... ◦ f 1, s 0, r K/ 2) 7: return: r 0 At the expense of having to store the additional checkpoint s K/ 2, this already roughly halves the computational complexity compared to Algorithm 8.6.

<!-- chunk {"id": "body-0499", "role": "body", "section": "Recursive halving", "weight": 1.0} -->

We can then apply this reasoning recursively, as formalized in Algorithm 8.7. The algorithm is known as recursive binary schedule and illustrated in Fig. 8.11. In terms of number of function evaluations C (K), for K even, we make K/ 2 function calls, and we call the procedure recursively twice, that is, If the chain is of length 1, we directly use the VJP, so C = 0. Hence, the numbers of function calls, if K is a power of 2, is In terms of memory usage, Algorithm 8.7 uses s 0 not only at line 4 but also at line 6. So when the algorithm is called recursively on the second half of the chain at line 5, one memory slot is taken by s 0. This line is called recursively until the chain is reduced to a single function.

<!-- chunk {"id": "body-0500", "role": "body", "section": "Recursive halving", "weight": 1.0} -->

At that point, the total number of memory slots used is equal to the number of times we split the function in half, that is, log 2 K for K a power of 2. On the other hand, the input s 0 is no longer used after line 6 of Algorithm 8.7. At that line, the memory slot taken by s 0 can be consumed by the recursive call on the first-half. In other words, calling the algorithm recursively on the first half does not incur extra memory cost. So if K is a power of 2, the memory cost of Algorithm 8.7 is Figure 8.11: Illustration of checkpointing with recursive halving, for a chain of 8 functions. The chain is first fully evaluated while storing some computations as checkpoints in memory. Then, during the backward pass, we recompute some intermediate values from the latest checkpoint available. In contrast, vanilla reversemode autodiff (with full caching of the intermediate computations) would lead to a simple triangle shape.

<!-- chunk {"id": "body-0501", "role": "body", "section": "Dynamic programming", "weight": 1.0} -->

Recursive halving requires log 2 K memory slots for a chain of length K. However, as illustrated in Fig. 8.11, at a given time step, all memory slots may not be exploited.

<!-- chunk {"id": "body-0502", "role": "body", "section": "Dynamic programming", "weight": 1.0} -->

To optimize the approach, we observe that recursive halving is just one instance of a program that splits the chain and calls itself recursively on each part. In other words, it is a form of divide-andconquer algorithm. Rather than splitting the chain in half, we may consider splitting the chain at some index l. One split is used to reverse the computations from l +1 to K by a recursive call that consumes one memory slot. The other split is used on a recursive call that reverses the computations from 0 to l. That second call does not require an additional memory slot, as it can use directly the memory slot used by the original input s 0. To split the chain in such two parts, we need l intermediate computations to go from s 0 to s l. The computational complexity C (k, s), counted as the number of function evaluations, for a chain of length k with s memory slots then satisfies the recurrence for all l ∈ { 1,..., k -1 }. By simply taking l = k/ 2, we recover exactly the computational complexity of recursive halving.

<!-- chunk {"id": "body-0503", "role": "body", "section": "Dynamic programming", "weight": 1.0} -->

To refine the latter, we may split the chain by selecting l to minimize the complexity. An optimal scheme must satisfy the recursive equation, Note that C ∗ (K,S) can be computed from C ∗ (k, s) for k = 1,..., K -1, s = 1,..., S -1. This suggests a dynamic programming approach to find an optimal scheme algorithmically. For a chain of length k = 1, the cost is null as we directly reverse the computation, so C ∗ (1, s):= 0. On the other hand for a memory s = 1, there is only one possible scheme that saves only the initial input as in Algorithm 8.6, so C ∗ (k, 1):= (k (k -1)) / 2. The values C ∗ (k, s) can then be computed incrementally from k = 1 to K and s = 1 to S using Eq. (8.3).

<!-- chunk {"id": "body-0504", "role": "body", "section": "Dynamic programming", "weight": 1.0} -->

The optimal splits can be recorded along the way as The optimal split for K,S can then be found by backtracking the optimal splits along both branches corresponding to C ∗ (k -l, s -1) and C ∗ (l, s). As the final output consists in traversing a binary tree, it was called treeverse. Note that the dynamic programming procedure is generic and could a priori incorporate varying computational costs for the intermediate functions f k.

<!-- chunk {"id": "body-0505", "role": "body", "section": "Analytical formula", "weight": 1.0} -->

It turns out that we can also find an optimal scheme analytically. This scheme was found by Griewank, following the analysis of optimal inversions of sequential programs by divide-and-conquer algorithms done by Grimm et al.; see also Griewank for a simple proof. The main idea consists in considering the number of times an evaluation step f k is repeated. As we split the chain at l, all steps from 1 to l will be repeated at least once. In other words, treating the second half of the chain incurs one memory cost, while treating the first half of the chain incurs one repetition cost. Griewank shows that for fixed K, S, we can find the minimal number of repetitions analytically and build the corresponding scheme with simple formulas for the optimal splits.

<!-- chunk {"id": "body-0506", "role": "body", "section": "Analytical formula", "weight": 1.0} -->

Compared to the dynamic programming approach, it means that we do not need to compute the pointers l ∗ ( k, s ), and we can use a simple formula to set l ∗ ( k, s ). We still need to traverse the corresponding binary tree given K,S and l ∗ ( k, s ) to obtain the schedules. Note that such optimal scheme does not take into account varying computational costs for the functions f k.

<!-- chunk {"id": "body-0507", "role": "body", "section": "Online checkpointing", "weight": 1.0} -->

The optimal scheme presented above requires knowing the total number of nodes in the computation graph ahead of time. However, when differentiating through for example a while loop (Section 5.10), this is not the case. To circumvent this issue, online checkpointing schemes have been developed and proven to be nearly optimal. These schemes start by defining a set of S checkpoints with the first S computations, then these checkpoints are rewritten dynamically as the computations keep going. Once the computations terminate, the optimal approach presented above for a fixed length is applied on the set of checkpoints recorded.

<!-- chunk {"id": "body-0508", "role": "body", "section": "General case", "weight": 1.0} -->

The memory requirements of reverse-mode autodiff can be completely alleviated when the functions f k are invertible (meaning that f -1 k exists) and when f -1 k is easily accessible. In that case, rather than storing the intermediate computations s k -1, necessary to compute the VJP r k ↦→ Algorithm 8.8 Reverse-mode autodiff for reversible chains.

<!-- chunk {"id": "body-0509", "role": "body", "section": "General case", "weight": 1.0} -->

Functions: f:= f K ◦... ◦ f 1, with each f k invertible Inputs: input s 0 ∈ S 0, output direction u ∈ S K 1: Compute s K = f K ◦... ◦ f 1 (s 0) 2: for k:= K,..., 1 do 3: Compute s k -1 = f -1 k (s k) 4: Compute r k -1 = ∂f k (s k -1) ∗ [r k] Outputs: f (s 0):= s K, ∂f (s 0) ∗ [u] = r 0 ∂f k (s k -1) ∗ [r k], one can compute them on the fly during the backward pass from s k using s k -1 = f -1 k (s k). We summarize the procedure for the case of computation chains in Algorithm 8.8. Compared to vanilla reverse-mode autodiff in Algorithm 8.2, the algorithm has optimal memory complexity, as we can release s k and r k as we go.

<!-- chunk {"id": "body-0510", "role": "body", "section": "General case", "weight": 1.0} -->

In practice, f -1 k often does not exist or may not be easily accessible. However, network architectures can be constructed to be easily invertible by design. Examples include reversible residual networks, orthonormal RNNs, neural ODEs (Section 12.6), and momentum residual neural networks; see also references therein.

<!-- chunk {"id": "body-0511", "role": "body", "section": "Case of orthonormal JVPs", "weight": 1.0} -->

When the JVP of each f k is an orthonormal linear mapping, i.e., it is easy to check that the VJP of f = f K ◦... ◦ f 1 is equal to the JVP of f -1 = f -1 1 ◦... ◦ f -1 K, that is In other words, in the case of orthormal JVPs, reverse-mode autodiff of f coincides with forward-mode autodiff of f -1.

<!-- chunk {"id": "body-0512", "role": "body", "section": "Randomized forward-mode gradient estimator", "weight": 1.0} -->

Forward-mode autodiff does not require to store intermediate activations. However, for a function f: R P → R, computing the gradient ∇ f using forward-mode autodiff requires P JVPs, which is intractable if P is large. Can we approximate ∇ f with fewer JVPs? The following proposition gives an unbiased estimator of ∇ f that only involves JVPs.

<!-- chunk {"id": "body-0513", "role": "body", "section": "Randomized forward-mode gradient estimator", "weight": 1.0} -->

Proposition 8.2 (Unbiased forward-mode estimator of the gradient). Let f: R P → R be a differentiable function. Then, where p:= Normal P is the isotropic Gaussian distribution.

<!-- chunk {"id": "body-0514", "role": "body", "section": "Randomized forward-mode gradient estimator", "weight": 1.0} -->

This estimator is for instance used by Baydin et al.. It can be seen as the zero-temperature limit of the gradient of a perturbed function, estimated by the score-function estimator (SFE); see Section 14.4.6.

<!-- chunk {"id": "body-0515", "role": "body", "section": "Randomized forward-mode gradient estimator", "weight": 1.0} -->

A word of caution: while this estimator can be useful for example when we do not want to store the intermediate activations for memory reasons, this of course comes at the cost of increasing the variance, which influences the convergence rate of SGD, as seen in Section 16.2.

<!-- chunk {"id": "body-0516", "role": "body", "section": "Randomized forward-mode gradient estimator", "weight": 1.0} -->

In practice, the expectation above can be approximated by drawing M noise vectors z 1,..., z M, and averaging 〈∇ f ( µ ), z i 〉 over i ∈ [ M ].

<!-- chunk {"id": "body-0517", "role": "body", "section": "Summary", "weight": 1.0} -->

- Computer programs can be seen as directed acyclic graphs, where nodes correspond to the output of intermediate operations in the program, and edges represent the dependencies of current operations on past operations. - Automatic differentiation (autodiff) for a function f: R P → R M has two main modes: forward mode and reverse mode. - The forward mode: i) uses JVPs, ii) builds the Jacobian one column at a time, iii) is efficient for tall Jacobians (M ≥ P), iv) need not store intermediate computations. - The reverse mode: i) uses VJPs, builds the Jacobian one row at a time, iii) is efficient for wide Jacobians (P ≥ M), iv) needs to store intermediate computations, in order to be computationally optimal. - To trade computational efficiency for better memory efficiency, we can use checkpointing techniques. - The complexity of computing the gradient of a function f: R P → R using the reverse mode is at most a constant time bigger than that of evaluating the function itself. This is the Baur-Strassen theorem, in arithmetic circuits. This astonishing result is one of the pillars of modern machine learning.

<!-- chunk {"id": "body-0518", "role": "body", "section": "Second-order automatic differentiation", "weight": 1.0} -->

We review in this chapter how to perform automatic differentiation for second-order derivatives.

<!-- chunk {"id": "body-0519", "role": "body", "section": "Hessian-vector products", "weight": 1.0} -->

We consider in this section a function f: E → R. Similarly to the Jacobian, for most purposes, we do not need access to the full Hessian but rather to the Hessian-vector product (HVP) ∇ 2 f ( w )[ v ] at w ∈ E, in a direction v ∈ E, as defined in Definition 2.19. The latter can be computed in four different ways, depending on how we combine the two main modes of autodiff.

<!-- chunk {"id": "body-0520", "role": "body", "section": "Four possible methods", "weight": 1.0} -->

An HVP can be computed in four different ways. 1. Reverse on reverse: The Hessian can be seen as the transposed Jacobian of the gradient, hence the HVP can be computed as the VJP of the gradient, 2. Forward on reverse: Owing to its symmetry (see Proposition 2.10), the Hessian can also be seen as the Jacobian of the gradient, hence the HVP can be computed as the JVP of the gradient, 3. Reverse on forward: Recall that for any function g: E → E, the VJP can equivalently be defined as the gradient along an output direction v ∈ E, that is, where we recall the shorthand 〈 g, v 〉 (w):= 〈 v, g (w) 〉, so that 〈 g, v 〉 is a function of w. In our case, we can therefore rewrite the reverse-on-reverse approach as We know that 〈∇ f, v 〉 (w) = 〈∇ f (w), v 〉 = ∂f (w)[v] is the JVP of f at w along v.

<!-- chunk {"id": "body-0521", "role": "body", "section": "Four possible methods", "weight": 1.0} -->

Therefore, we can also compute the HVP as the gradient of the JVP of f at w along v, where we use the notation (∂f (·)[v])(w):= ∂f (w)[v] to insist on the fact that it is a function of w. 4. Forward on forward: Finally, we can use the definition of the HVP in Definition 2.19 as a vector of second partial derivatives along v and each canonical direction. That is, assuming E = R P, we can compute the JVP of the JVP P times, The four different ways of computing the HVP are summarized in Table 9.1.

<!-- chunk {"id": "body-0522", "role": "body", "section": "Complexity", "weight": 1.0} -->

To get a sense of the computational and memory complexity of the four approaches, we consider a chain of functions f:= f K ◦ · · · ◦ f 1 as done in Section 8.1. To simplify our analysis, we assume f k: R P → R P for k ∈ { 1,..., K -1 } and f K: R P → R.

<!-- chunk {"id": "body-0523", "role": "body", "section": "Complexity", "weight": 1.0} -->

Table 9.1: Four different ways of computing the HVP ∇ 2 f ( w )[ v ].

<!-- chunk {"id": "body-0524", "role": "body", "section": "Complexity", "weight": 1.0} -->

We illustrate the computation graphs of reverse-on-reverse and forward-on-reverse in Fig. 9.2 and Fig. 9.3 respectively. By applying reverse mode on reverse mode, at each fan-in operation s k -1, r k ↦→ ∂f k ( s k -1 )[ r k ], the reverse mode on ∇ f branches out in two paths that are later merged by a sum. By applying forward mode on top of reverse mode, the flow of computations simply follows the one of ∇ f.

<!-- chunk {"id": "body-0525", "role": "body", "section": "Complexity", "weight": 1.0} -->

The computation graph of the reverse mode is illustrated in Fig. 9.1. While f = f K ◦ · · · ◦ f 1 would be represented by a simple chain, the computational graph of ∇ f is no longer a chain: it is a DAG. This is due to the computations of ∂f k ( s k -1 )[ r k ], where both s k -1 and r k depend on s 0.

<!-- chunk {"id": "body-0526", "role": "body", "section": "Complexity", "weight": 1.0} -->

With this in mind, following a similar calculation as for Table 8.1, we obtain the following results. We assume that each ∂f k ( s k -1 ) is a dense linear operator, so that its application has the same cost as a matrix-vector multiplication. For the memory complexity, we consider that the inputs of each operation is saved to compute the required derivatives in the backward passes.

<!-- chunk {"id": "body-0527", "role": "body", "section": "Complexity", "weight": 1.0} -->

We see that, for chains of functions, 'reverse on reverse', 'forward on reverse' and 'reverse on forward' all have similar time complexities up to some constant factors. Using reverse mode on top of reverse mode requires storing the information backpropagated, i.e., the r k (resp. the information forwarded, i.e., the t k in Fig. 8.1), to perform the final reverse pass. By using forward mode on top of reverse mode, this additional cost is not incurred, making it slightly less memory expensive. In addition, reverse mode on top of reverse mode induces a few additional summations due to the branching and merge operations depicted in Fig. 9.2. The same holds when using reverse on top of forward as we cannot avoid fan-in operations (this time of the form s k -1, t k -1 ↦→ ∂f k ( s k -1 )[ t k -1 ]). Unfortunately, 'forward on forward' is prohibitively expensive.

<!-- chunk {"id": "body-0528", "role": "body", "section": "Complexity", "weight": 1.0} -->

To summarize, among the four approaches presented to compute HVPs, the forward-over-reverse mode is a priori the most preferable in terms of computational and memory complexities. Note, however, that computations of higher derivatives can benefit from dedicated autodiff implementations such as Taylor mode autodiff, that do not merely compose forward and reverse modes. For general functions f, it is reasonable to benchmark the first three methods to determine which method is the best for the function at hand.

<!-- chunk {"id": "body-0529", "role": "body", "section": "An approximation of the Hessian", "weight": 1.0} -->

The Hessian matrix ∇ 2 L (w) of a function L: W → R is often used to construct a quadratic approximation of L (w), Unfortunately, when L is nonconvex, ∇ 2 L (w) is typically an indefinite matrix, which means that the above approximation is a nonconvex quadratic w.r.t. v. For instance, if L = ℓ ◦ f with ℓ convex, then L is convex if f is linear, but it is typically nonconvex if f is nonlinear. The (generalized) Gauss-Newton matrix is a principled alternative to the Hessian, which is defined for L:= ℓ ◦ f.

<!-- chunk {"id": "body-0530", "role": "body", "section": "An approximation of the Hessian", "weight": 1.0} -->

Definition 9.1 (Gauss-Newton matrix). Given a differentiable function f: W → M and a twice differentiable function ℓ: M→ R, the (generalized) Gauss-Newton matrix of the composition L = ℓ ◦ f evaluated at a point w ∈ W is defined as As studied in Section 17.2, the Gauss-Newton matrix is a key ingredient of the Gauss-Newton method. An advantage of the Gauss-Newton matrix is its positive semi-definiteness provided that ℓ is convex.

<!-- chunk {"id": "body-0531", "role": "body", "section": "An approximation of the Hessian", "weight": 1.0} -->

Proposition 9.1 (Positive semi-definiteness of the GN matrix). If ℓ is convex, then ∇ 2 GN ( ℓ ◦ f )( w ) is positive semi-definite for all f.

<!-- chunk {"id": "body-0532", "role": "body", "section": "An approximation of the Hessian", "weight": 1.0} -->

This means that the approximation Using the chain rule, we find that the Hessian of L = ℓ ◦ f decomposes into the sum of two terms (see also Proposition 9.7).

<!-- chunk {"id": "body-0533", "role": "body", "section": "An approximation of the Hessian", "weight": 1.0} -->

Proposition 9.2 (Approximation of the Hessian). For f differentiable and ℓ twice differentiable, we have If f is linear, then the Hessian and Gauss-Newton matrices coincide, The Gauss-Newton operator ∇ 2 GN (ℓ ◦ f) can therefore be seen as an approximation of the Hessian ∇ 2 (ℓ ◦ f), with equality if f is linear.

<!-- chunk {"id": "body-0534", "role": "body", "section": "Gauss-Newton chain rule", "weight": 1.0} -->

A chain rule for computing the Hessian of a composition of two functions is presented in Proposition 9.7, but the formula is relatively complicated, due to the cross-terms. In contrast, a Gauss-Newton chain rule is straightforward.

<!-- chunk {"id": "body-0535", "role": "body", "section": "Gauss-Newton vector product", "weight": 1.0} -->

As for the Hessian, we rarely need to materialize the full Gauss-Newton matrix in memory. Indeed, we can define the Gauss-Newton vector product (GNVP), a linear map for a direction v ∈ W, as where ∇ 2 ℓ (θ) u is the HVP of ℓ, a linear map from M to M. The GNVP can be computed using the JVP of f, the HVP of ℓ and the VJP of f. Instantiating the VJP requires 1 forward pass through f, from which we get both the value f (w) and the adjoint linear map u ↦→ (∂f (w) ∗ u). Evaluating the VJP requires 1 backward pass through f. Evaluating the JVP requires 1 forward pass through f. In total, evaluating v ↦→∇ 2 GN (ℓ ◦ f)(w) v therefore requires 2 forward passes and 1 backward pass through f.

<!-- chunk {"id": "body-0536", "role": "body", "section": "Gauss-Newton matrix factorization", "weight": 1.0} -->

In this section, we assume W ⊆ R P and M⊆ R M. When ℓ is convex, we know that the Gauss-Newton matrix is positive semi-definite and therefore it can be factorized into ∇ 2 GN (ℓ ◦ f)(w) = V V ⊤ for some V ∈ R P × R, where R ≤ min { P, M } is the rank of the matrix. Such a decomposition can actually be computed easily from a factorization of the Hessian of ℓ. For instance, suppose we know the eigendecomposition of the Hessian of ℓ, ∇ 2 ℓ (f (w)) = ∑ j M =1 λ i u i u ⊤ i, where the u i are the eigenvectors and the λ i ≥ 0 are the eigenvalues (which we know are non-negative due to positive semidefiniteness). Then, the Gauss-Newton matrix can be decomposed as Stacking the vectors v i into a matrix V = (v 1,..., v M), we recover the factorization ∇ 2 GN (ℓ ◦ f)(w) = V V ⊤.

<!-- chunk {"id": "body-0537", "role": "body", "section": "Gauss-Newton matrix factorization", "weight": 1.0} -->

To form this decomposition, we need to perform the eigendecomposition of ∇ 2 ℓ (f (w)) ∈ R M × M, which takes O (M 3) time. We also need M calls to the VJP of f at w. Compared to the direct implementation in Eq. (9.1), the factorization, once computed, allows us to compute the Gauss-Newton vector product (GNVP) as ∇ 2 GN (ℓ ◦ f)(w)[v] = V V ⊤ v. The factorization only requires P × M memory, while the direct implementation in Eq. (9.1) requires us to maintain the intermediate computations of f. The computationmemory trade-offs therefore depend on the function considered.

<!-- chunk {"id": "body-0538", "role": "body", "section": "Stochastic setting", "weight": 1.0} -->

Suppose the objective function is of the form With some slight abuse of notation, we then have that the Gauss-Newton matrix associated with a pair (x, y) is Given a distribution ρ over (x, y) pairs, the Gauss-Newton matrix associated with the averaged loss

<!-- chunk {"id": "body-0539", "role": "body", "section": "Link with the Hessian", "weight": 1.0} -->

Provided that the probability distribution is twice differentiable w.r.t. w with integrable second derivatives, the Fisher information matrix can also be expressed as the Hessian of the negative log-likelihood.

<!-- chunk {"id": "body-0540", "role": "body", "section": "Link with the Hessian", "weight": 1.0} -->

Proposition 9.4 (Connection with the Hessian). The Fisher information matrix of the negative log-likelihood L (w; S) = -log q w (S) satisfies Remark 9.1 (Empirical Fisher). We emphasize that in the above definitions, S is sampled from the model distribution q w, not from the data distribution ρ. That is, we have The latter is sometimes called ambiguously the 'empirical' Fisher, though this name has generated confusion.

<!-- chunk {"id": "body-0541", "role": "body", "section": "Equivalence with the Gauss-Newton matrix", "weight": 1.0} -->

So far, we discussed the Fisher information for a generic random variable S ∼ q w. We now discuss the supervised probabilistic learning setting where S = ( X,Y ) and where, using the product rule of probability, we define the PDF q w ( X,Y ):= ρ X ( X ) p θ ( Y ), with the shorthand θ:= f ( w; X ).

<!-- chunk {"id": "body-0542", "role": "body", "section": "Equivalence with the Gauss-Newton matrix", "weight": 1.0} -->

Proposition 9.5 (Fisher matrix in supervised setting). Suppose (X,Y) ∼ q w where the PDF of q w is q w (X,Y):= ρ X (X) p θ (Y). In that case, the Fisher information matrix of the negative log- likelihood L (w; x, y) = -log q w (x, y) decomposes as, where we defined the shorthand θ:= f (w; X) and where we defined the negative log-likelihood loss ℓ (θ; Y):= -log p θ (Y).

<!-- chunk {"id": "body-0543", "role": "body", "section": "Equivalence with the Gauss-Newton matrix", "weight": 1.0} -->

When p θ is an exponential family distribution, we can show that the Fisher information matrix and the Gauss-Newton matrix are equivalent.

<!-- chunk {"id": "body-0544", "role": "body", "section": "Equivalence with the Gauss-Newton matrix", "weight": 1.0} -->

Proposition 9.6 (Equivalence between Fisher and Gauss-Newton). If p θ is an exponential family distribution, then Proof. From Proposition 3.3, if p θ is an exponential family distribution, ∇ 2 ℓ (θ, y) is actually independent of y. Using Bartlett's second identity Eq. (12.3), we then obtain where we used · to indicate that the results holds for all y. Plugging the result back in the Fisher information matrix concludes the proof.

<!-- chunk {"id": "body-0545", "role": "body", "section": "Implementation with matrix-free linear solvers", "weight": 1.0} -->

Numerous direct methods exist to compute the inverse of a matrix, such as the Cholesky decomposition, QR decomposition and Gaussian elimination. However, these algorithms require accessing elementary entries of the matrix, while an autodiff framework gives access to the Hessian through HVPs. Fortunately, there exists so-called matrix-free algorithms, that can solve a linear system of equations by only accessing the linear map v ↦→ H [v] for any v. Among such algorithms, we have the conjugate gradient (CG) method, that applies for H positive-definite, i.e., such that 〈 v, H [v] 〉 > 0 for all v = 0, or the generalized minimal residual (GMRES) method, that applies for any invertible H. A longer list of solvers can be found in public software such as SciPy.

<!-- chunk {"id": "body-0546", "role": "body", "section": "Implementation with matrix-free linear solvers", "weight": 1.0} -->

The IHVP of a strictly convex function (ensuring that the Hessian is positive definite) can therefore be computed by instantiating CG on the HVP, Positive-definiteness of the Hessian is indeed guaranteed for strictly convex functions for example, while for generic non-convex functions, such property may be verified around a minimizer but not in general. The conjugate gradient method is recalled in Algorithm 9.1 in its simplest form. In theory, the exact solution of the linear system is found after at most T = P iterations of CG, though in practice numerical errors may prevent from getting an exact solution.

<!-- chunk {"id": "body-0547", "role": "body", "section": "Complexity", "weight": 1.0} -->

For a given matrix H ∈ R P × P, solving H v = u can be done with decomposition methods (LU, QR, Cholesky) in O ( P 3 ) time. For matrixfree methods such as CG or GMRES, the cost per iteration is O ( P 2 ). Since they theoretically solve the linear system in O ( P ) iterations, the cost to obtain an exact solution is theoretically the same, O ( P 3 ).

<!-- chunk {"id": "body-0548", "role": "body", "section": "Complexity", "weight": 1.0} -->

However, CG or GMRES differ from decomposition methods in that they are iterative methods, meaning that, at each iteration, they get closer to a solution. Unlike decomposition methods, this means that we can stop them before an exact solution is found. In practice, the number of iterations required to find a good approximate solution depends on the matrix. Well conditioned matrices require only few iterations. Badly conditioned matrices lead to some numerical instabilities for CG, so that more than P iterations may be needed to get a good solution. In contrast, decomposition methods proceed in two steps: first they build a decomposition of H at a cost of O ( P 3 ), and second they solve a linear system at a cost of O ( P 2 ), by leveraging the structure. LU and QR decompositions are known to be generally more stable and are therefore often preferred in practice, when we can access entries of H at no cost.

<!-- chunk {"id": "body-0549", "role": "body", "section": "Complexity", "weight": 1.0} -->

If we do not have access to the Hessian H, but only to its HVP, accessing entries of H comes at a prohibitive cost. Indeed, entries of H can still be recovered from HVPs, since e ⊤ i H e j = H i,j, but accessing each row or column of H costs one HVP (matrix-vector product). To access the information necessary to use a decomposition method, we therefore need P calls to HVPs before being able to actually compute the solution. For the same number of calls, CG or GMRES will already have found an approximate solution. In addition, a CG method does not require to store any memory.

<!-- chunk {"id": "body-0550", "role": "body", "section": "Second-order Jacobian chain rule", "weight": 1.0} -->

The essential ingredient to develop forward-mode and reverse-mode autodiff hinged upon the chain rule for composed functions, h = g ◦ f. For second derivatives, a similar rule can be obtained. To do so, we slightly abuse notations and denote where h: R P → R Q, w ∈ R P, u ∈ R Q, and where we recall the shorthand notation 〈 u, h 〉 (w):= 〈 u, h (w) 〉. Moreover, we view the above quantity as a linear map. Strictly speaking, the superscript ∗ is not a linear adjoint anymore, since v 1, v 2 ↦→ ∂ 2 h (w)[v 1, v 2] is no longer linear but bilinear. However, this superscript plays the same role as the VJP, since it takes an output vector and returns the input derivatives that correspond to infinitesimal variations along that output vector.

<!-- chunk {"id": "body-0551", "role": "body", "section": "Second-order Jacobian chain rule", "weight": 1.0} -->

Proposition 9.7 (Hessian chain-rule). For two twice differentiable functions f: R P → R M and g: R M → R Q, the second directional derivative of the composition g ◦ f is a bilinear map from R P × R P to R Q along input directions v 1, v 2 ∈ R P of the form The Hessian of the composition g ◦ f along an output direction u ∈ R Q is, seen as a linear map, For the composition of f: R P → R M with a scalar-valued function function ℓ: R M → R, we have in matrix form Note that, while the Hessian is usually defined for scalar-valued functions h: R P → R, the above definition is for a generalized notion of Hessian that works for any function h: R P → R Q.

<!-- chunk {"id": "body-0552", "role": "body", "section": "Second-order Jacobian chain rule", "weight": 1.0} -->

The Hessian back-propagation rule in Eq. (9.2) reveals two terms. The first one ∂ 2 f ( w ) ∗ [ ∂g ( f ( w )) ∗ u ] simply computes the Hessian of the intermediate function along the output direction normally backpropagated by a VJP. The second term ∂f ( w ) ∗ ∂ 2 g ( f ( w )) ∗ [ u ] ∂f ( w ) shows how intermediate first-order variations influence second order derivatives of the output.

<!-- chunk {"id": "body-0553", "role": "body", "section": "Second-order Jacobian chain rule", "weight": 1.0} -->

Example 9.1 (Composition with an elementwise nonlinear function). Consider the element-wise application of a twice differentiable scalar-valued function f (x) = (f (x i)) i M =1 followed by some twice differentiable function ℓ. Note that ∇ 2 f i (x) = f ′′ (x i) e i e ⊤ i. Hence, the Hessian of the composition reads Example 9.2 (Hessian of the composition with a linear function). Consider a linear function f (W) = Wx, for W ∈ R M × D, composed with some twice differentiable function ℓ: R M → R. From Proposition 9.7, we get, in terms of linear maps, As already noted in Section 2.3, we have that ∂f (W)[V] = V x and ∂f (W) ∗ [u] = ux ⊤. Hence, the Hessian seen as a linear map reads

<!-- chunk {"id": "body-0554", "role": "body", "section": "Computation chains", "weight": 1.0} -->

For a simple computation chain f = f K ◦... ◦ f 1 as in Section 8.1, the formula derived in Proposition 9.7 suffices to develop an algorithm that backpropagates the Hessian, as shown in Algorithm 9.2. Compared to Algorithm 8.2, we simply backpropagate both the vectors r k and the matrices R k using intermediate first and second derivatives.

<!-- chunk {"id": "body-0555", "role": "body", "section": "Fan-in and fan-out", "weight": 1.0} -->

For generic computation graphs (see Section 8.3), we saw that multiinput functions (fan-in) were crucial. For Hessian backpropagation in computation graphs, we therefore need to develop a similar formula.

<!-- chunk {"id": "body-0556", "role": "body", "section": "Fan-in and fan-out", "weight": 1.0} -->

Proposition 9.8 (Hessian chain-rule for fan-in). Consider n +1 twice differentiable functions f 1,..., f n and g with f i: R P → R M i and g: R M 1 ×... × R M n → R Q. The Hessian of g ◦ f for f (w) = (f 1 (w),..., f n (w)) along an output direction u ∈ R Q is given by The gradient backpropagation expression for fan-in is simple because the functions f i are not linked by any path. In contrast, the Hessian backpropagation involves cross-product terms On the other hand, developing a backpropagation rule for fan-out does not pose any issue, since each output function can be treated ∂f i (w) ∗ ∂ 2 i,j g (f (w)) ∗ [u] ∂f j (w) for i = j. The nodes associated to the f i computations cannot be treated independently anymore.

<!-- chunk {"id": "body-0557", "role": "body", "section": "Fan-in and fan-out", "weight": 1.0} -->

Proposition 9.9 (Hessian chain-rule for fan-out). Consider n +1 twice differentiable functions g 1,..., g n and f with g i: R M → R Q i and f: R P → R M. The Hessian of g ◦ f for g ( w ) = ( g 1 ( w ),..., g n ( w )) along a direction u = ( u 1,..., u n ) ∈ R Q 1 ×... × R Q n is given by

<!-- chunk {"id": "body-0558", "role": "body", "section": "Block diagonal approximations", "weight": 1.0} -->

Rather than computing the whole Hessian or Gauss-Newton matrices, we can consider computing block-diagonal or diagonal approximations, which are easier to invert. The approximation rules we present in this section build upon the Hessian chain rule studied in Section 9.5.

<!-- chunk {"id": "body-0559", "role": "body", "section": "Feedforward networks", "weight": 1.0} -->

Recall the definition of a feedforward network: where w:= (w 1,..., w K). Rather than computing the entire Hessian of ℓ ◦ f w.r.t. w, we can compute the Hessians w.r.t. each set of parameters w k. For the case of computation chains, the Hessian backpropagation recursion we used in Algorithm 9.2 was Extending this recursion to the feedforward network case, we obtain, starting from r K:= ∇ ℓ (s K) and R K:= ∇ 2 ℓ (s K), where we used ∼ to indicate that these blocks are not used. The Hessians w.r.t each set of parameters are then The validity of this result stems from the fact that we can view the Hessian w.r.t. w k as computing the Hessian w.r.t. w k of where ˜ f i:= f i (·, w k), for i ∈ { k +1,..., K }.

<!-- chunk {"id": "body-0560", "role": "body", "section": "Feedforward networks", "weight": 1.0} -->

As the computations of the block-wise Hessians share most of the computations, they can be evaluated in a single backward pass just as the gradients.

<!-- chunk {"id": "body-0561", "role": "body", "section": "Feedforward networks", "weight": 1.0} -->

Example 9.3 (Block-wise computation of the Gauss-Newton matrix). Our blockwise backpropagation scheme can readily be adapted for the Gauss-Newton matrix as starting from R K:= ∇ 2 ℓ (s K). The outputs R 0, G 0,..., G K give a block-wise approximation of the Gauss-Newton matrix.

<!-- chunk {"id": "body-0562", "role": "body", "section": "Feedforward networks", "weight": 1.0} -->

Now, consider a simple multilayer perceptron such that Using Example 9.2 and Example 9.1 adapted to the Gauss-Newton matrix, we can compute the block-wise decomposition of the GaussNewton matrix as, for k = K,..., 1, starting from R K:= ∇ 2 ℓ (s K). The outputs G 1,..., G K correspond to the block-wise elements of the Gauss-Newton matrix of f for the vectorized weights w 1,..., w K. Similar computations were done in KFRA and BackPack.

<!-- chunk {"id": "body-0563", "role": "body", "section": "Computation graphs", "weight": 1.0} -->

For generic computation graphs, consider a function f (x, w) defined, denoting i 1,..., i p k:= pa(k), such that f (x, w) = s K, and k is following a topological ordering of the graph (see Section 8.3). We can consider the following backpropagation scheme, for k = K,..., 1 and j ∈ pa(k) starting from R K:= ∇ 2 ℓ (s K) and r K:= ∇ ℓ (s K). Recall that for multiple inputs, the chain-rule presented in Proposition 9.8 involves the cross-derivatives. For this reason the back-propagation scheme in Eq. (9.3) only computes an approximation. For example, one can verify that using Eq. (9.3) to compute the Hessian of ℓ (f 1 (w), f 2 (w)) does not provide an exact expression for the Hessian of f. This scheme is easy to implement and may provide a relevant proxy for the Hessian.

<!-- chunk {"id": "body-0564", "role": "body", "section": "Diagonal approximations", "weight": 1.0} -->

Similarly to the idea of designing a backpropagation scheme that approximates blocks of the Hessian, we can design a backpropagation scheme that approximates the diagonal of the Hessian. The approach was originally proposed by Becker and Le Cun for feedforward networks, but our exposition, new to our knowledge, has the benefit that it naturally extends to computational graphs, as we shall see.

<!-- chunk {"id": "body-0565", "role": "body", "section": "Computation chains", "weight": 1.0} -->

The idea stems from modifying the Hessian backpropagation rule in Proposition 9.7 to only keep the diagonal of the Hessian. Formally, given a matrix M ∈ R D × D, we denote by diag (M) = (M ii) D i =1 ∈ R D the vector of diagonal entries of M, and for a vector m ∈ R D, we denote Diag (m) = ∑ D i =1 m i e i e ⊤ i the diagonal matrix with entries m i. For the backpropagation of the Hessian of ℓ ◦ f K ◦... ◦ f 1, we see from Algorithm 9.2 that diag (H k -1) can be expressed in terms of H k as Unfortunately, that recursion needs access to the whole Hessian H k, and would therefore be too expensive. A natural idea is to modify the recursion to approximate diag (H k) by backpropagating vectors: The diagonal matrix Diag (d k) serves as a surrogate for H k.

<!-- chunk {"id": "body-0566", "role": "body", "section": "Computation chains", "weight": 1.0} -->

Each iteration of this recursion can be computed in linear time in the output dimension D k since To initialize the recursion, we can set d K:= diag (∇ 2 ℓ (s K)). As an alternative, as proposed by Elsayed and Mahmood, if H K has a simple form, we can use ∇ 2 ℓ (s K) instead of Diag (d K) at the first iteration. This is the case for instance if f K is a cross-entropy loss. The recursion is repeated until we obtain the approximate diagonal Hessian d 0 ≈ diag (∇ 2 (ℓ ◦ f)(x)). The gradients r k, needed to compute d k, are computed along the way and the algorithm can therefore also return r 0 = ∇ (ℓ ◦ f)(x).

<!-- chunk {"id": "body-0567", "role": "body", "section": "Computation graphs", "weight": 1.0} -->

Although this diagonal approximation was originally derived for feedforward networks Becker and Le Cun, it is straightforward to generalize it to computation graphs. Namely, for a function f (x, w) decomposed along a computation graph, we can backpropagate a diagonal approximation in reverse topological order as for j ∈ pa(k), starting from r K = ∇ ℓ (s K) and d K = diag (∇ 2 ℓ (s K)) or Diag (d K) = ∇ 2 ℓ (s K). To implement such an algorithm, each elementary function in the computational graph needs to be augmented with an oracle that computes the Hessian diagonal approximation of the current function, given the previous ones. An example with MLPs is presented in Example 9.4.

<!-- chunk {"id": "body-0568", "role": "body", "section": "Computation graphs", "weight": 1.0} -->

Example 9.4 (Hessian diagonal approximation for MLPs). Consider a multilayer perceptron starting from s 0 = x. Here a k is the element-wise activation function (potentially the identity) and w encapsulates the weight matrices W 1,..., W K. We consider the derivatives w.r.t. the flattened matrices, so that gradients and diagonal approximations w.r.t. these flattened quantities are vectors. The backpropagation scheme (9.5) then reduces to, denoting t k = W k s k -1, starting from r K = ∇ ℓ (s K) and, e.g., d K = diag (∇ 2 ℓ (s K)). The algorithm returns g 1,..., g K as the gradients of f w.r.t. w 1,..., w K, with w i = vec(W i), and h 1,..., h K as the diagonal approximations of the Hessian w.r.t. w 1,..., w K.

<!-- chunk {"id": "body-0569", "role": "body", "section": "Randomized estimators", "weight": 1.0} -->

In this section, we describe randomized estimators of the diagonal of the Hessian or Gauss-Newton matrices.

<!-- chunk {"id": "body-0570", "role": "body", "section": "Girard-Hutchinson estimator", "weight": 1.0} -->

We begin with a generic estimator, originally proposed for trace estimation by Girard and extended by Hutchinson. Let A ∈ R P × P be an arbitrary square matrix, whose matrix-vector product (matvec) is available. Suppose ω ∈ R P is an isotropic random vector, i.e., such that E ω ∼ p [ωω ⊤] = I. For example, two common choices are the Rademacher distribution p = Uniform({-1, 1 }) and the standard normal distribution p = Normal(0, I). Then, we have Applications include generalized cross-validation, computing the KullbackLeibler divergence between two Gaussians, and computing the derivatives of the log-determinant.

<!-- chunk {"id": "body-0571", "role": "body", "section": "Girard-Hutchinson estimator", "weight": 1.0} -->

The approach can be extended to obtain an estimator of the diagonal of A, where ⊙ denotes the Hadamard product (element-wise multiplication). This suggests that we can use the Monte-Carlo method to estimate the diagonal of A, with equality as S → ∞, since the estimator is unbiased. Since, as reviewed in Section 9.1 and Section 9.2, we know how to multiply efficiently with the Hessian and the Gauss-Newton matrices, we can apply the technique with these matrices. The variance is determined by the number S of samples drawn and therefore by the number of matvecs performed. More elaborated approaches have been proposed to further reduce the variance.

<!-- chunk {"id": "body-0572", "role": "body", "section": "Bartlett estimator for the factorization", "weight": 1.0} -->

Suppose the objective function is of the form L (w; x, y):= ℓ (f (w; x); y) where ℓ is the negative log-likelihood ℓ (θ; y):= -log p θ (y) of an exponential family distribution, and θ:= f (w; x), for some network f. We saw from the equivalence between the Fisher and Gauss-Newton matrices in Proposition 9.6 (which follows from the Bartlett identity) that where · indicates that the result holds for any value of the second argument. This suggests a Monte-Carlo scheme where y i 1,..., y i S ∼ p θ and θ = f (w, x). In words, we can approximate the Gauss-Newton matrix with S gradient computations. This factorization can also be used to approximate the GNVP in Eq. (9.1).

<!-- chunk {"id": "body-0573", "role": "body", "section": "Bartlett estimator for the diagonal", "weight": 1.0} -->

Following a similar approach, we obtain where ⊙ indicates the element-wise (Hadamard) product. Using a MonteCarlo scheme, sampling y i 1,..., y i S from p θ, we therefore obtain with equality when all labels in the support of p θ have been sampled. That estimator, used for instance, requires access to individual gradients evaluated at the sampled labels. Another possible estimator of the diagonal is given by Letting γ i:= ∇ L (w; x, Y i), this follows from where we used that E [γ i ⊙ γ j] = E [γ i] ⊙ E [γ j] = 0 since γ i and γ j are independent variables for i = j and have zero mean, from Bartlett's first identity Eq. (12.2). We can then use the Monte-Carlo method to obtain with equality when all labels in the support of p θ have been sampled. This estimator can be more convenient to implement, since it only needs access to the gradient of the averaged losses. However, it may suffer from higher variance.

<!-- chunk {"id": "body-0574", "role": "body", "section": "Bartlett estimator for the diagonal", "weight": 1.0} -->

A special case of this estimator is used by Liu et al., where they draw only one y for each x.

<!-- chunk {"id": "body-0575", "role": "body", "section": "Summary", "weight": 1.0} -->

- By using a Hessian chain rule, we can develop a 'Hessian backpropagation'. While it is reasonably simple for computation chains, it becomes computationally prohibitive for computation graphs, due to the cross-product terms occurring with fan-. - A better approach is to use Hessian-vector products (HVPs). We saw that there are four possible methods to compute HVPs, but the forward-over-reverse method is a priori the most efficient. Similarly as for computing gradients, computing HVPs is only a constant times more expensive than evaluating the function itself. - The Gauss-Newton matrix associated with the composition ℓ ◦ f can be seen as an approximation of the Hessian. It is a positive semidefinite matrix if ℓ is convex, and can be used to build a principled quadratic approximation of a function. It is equivalent to the Fisher information matrix in the case of exponential families. Gauss-Newton-vector products can be computed efficiently, like HVPs. - We also described other approximations, such as (block) diagonal approximations, and randomized estimators.

<!-- chunk {"id": "body-0576", "role": "body", "section": "Inference in graphical models as differentiation", "weight": 1.0} -->

A graphical model specifies how random variables depend on each other and therefore determines how their joint probability distribution factorizes. In this chapter, we review key concepts in graphical models and how they relate to differentiation, drawing in the process analogies with computation chains and computation graphs.

<!-- chunk {"id": "body-0577", "role": "body", "section": "Chain rule of probability", "weight": 1.0} -->

The chain rule of probability is a fundamental law in probability theory for computing the joint probability of events. In the case of only two events A 1 and A 2, it reduces to the product rule For two discrete random variables S 1 and S 2, using the events A 1:= { S 1 = s 1 } and A 2:= { S 2 = s 2 }, the product rule becomes More generally, using the product rule, we have for K events Applying the product rule one more time, we have Repeating the process recursively, we arrive at the chain rule of probability For K discrete random variables S j, using the events A j:= { S j = s j }, the chain rule of probability becomes Importantly, this factorization holds without any independence assumption on the variables S 1,..., S K. In other words, the space of probability distributions specified by the joint probability on the lefthand side, and the space of probability distributions specified by the product of conditional probabilities on the right-hand side, are the same. We can further simplify the factorization if we make additional conditional independence assumptions.

<!-- chunk {"id": "body-0578", "role": "body", "section": "Conditional independence", "weight": 1.0} -->

We know that if two events A and B are independent, then Similarly, if two random variables S 1 and S 2 are independent, then More generally, if we work with K variables S 1,..., S K, some variables may depend on each other, while others may not. To simplify the notation, given a set C, we define the shorthands We say that a variable S j is independent of S D conditioned on S C, with C ∩ D = ∅, if for any s j, s C, s D

<!-- chunk {"id": "body-0579", "role": "body", "section": "Joint probability distributions", "weight": 1.0} -->

We consider a collection of K variables s:= (s 1,..., s K), potentially ordered or unordered. Each s belongs to the Cartesian product S:= S 1 ×··· × S K. Throughout this chapter, we assume that the sets S k are discrete for concreteness, with S k:= { v 1,..., v M k }. Note that because S k is discrete, we can always identify it with { 1,..., M k }. A graphical model specifies a joint probability distribution where p is the probability mass function of the joint probability distribution. Summing over the Cartesian product of all possible configurations, we obtain As we shall see, the graph of a graphical model encodes the dependencies between the variables (S 1,..., S K) and therefore how their joint distribution factorizes. Given access to a joint probability distribution, there are several inference problems one typically needs to solve.

<!-- chunk {"id": "body-0580", "role": "body", "section": "Likelihood", "weight": 1.0} -->

A simple task is to compute the likelihood of some observations s = (s 1,..., s K), It is also common to compute the log-likelihood,

<!-- chunk {"id": "body-0581", "role": "body", "section": "Maximum a-posteriori inference", "weight": 1.0} -->

Another common task is to compute the most likely configuration, This is the mode of the joint probability distribution. This is also known as maximum a-posteriori (MAP) inference in the literature.

<!-- chunk {"id": "body-0582", "role": "body", "section": "Marginal inference", "weight": 1.0} -->

The operation of marginalization consists in summing (or integrating) over all possible values of a given variable in a joint probability distribution. This allows us to compute the marginal probability of the remaining variables. For instance, we may want to marginalize all variables but S k = s k. To do so, we define the Cartesian product Summing over all variables but S k, we obtain the marginal probability of S k = s k as In particular, we may want to compute the marginal probability of two consecutive variables, P (S k -1 = s k -1, S k = s k).

<!-- chunk {"id": "body-0583", "role": "body", "section": "Expectation, convex hull, marginal polytope", "weight": 1.0} -->

Another common operation is to compute the expectation of φ (S) under a distribution p. It is defined by For the expectation under p θ, we write In exponential family distributions (Section 3.4), the function φ is called a statistic. It decomposes as where C ⊆ [K]. Intuitively, φ (s) can be thought as an encoding or embedding of s (a potentially discrete object such as a sequence of integers) in a vector space. Under this decomposition, we can also compute

<!-- chunk {"id": "body-0584", "role": "body", "section": "Convex hull", "weight": 1.0} -->

The mean µ belongs to the convex hull of φ (S):= { φ (s): s ∈ S}, where P (S) is the set of all possible probability distributions over S. In other words, M is the set of all possible convex combinations of φ (s) for s ∈ S. The vertices of M are all the s ∈ S.

<!-- chunk {"id": "body-0585", "role": "body", "section": "Case of binary encodings: the marginal polytope", "weight": 1.0} -->

In the special case of a discrete set S k = { v 1,..., v M } and of a binary encoding (indicator function) φ (s), the set M is called the marginal polytope, because each point µ ∈ M contains marginal probabilities. To see why, consider the unary potential where I (p):= 1 if p is true, 0 otherwise. We then obtain the marginal probability of S k = v i, Likewise, consider the pairwise potential We then obtain the marginal probability of S k = v i and S l = v j, We can do the same with higher-order potential functions.

<!-- chunk {"id": "body-0586", "role": "body", "section": "Complexity of brute force", "weight": 1.0} -->

Apart from computing the likelihood, which is trivial, computing the marginal, mode and expectation by brute force takes O ( ∏ K k =1 |S k | ) time. In particular, if |S k | = M ∀ k ∈ [ K ], brute force takes O ( M K ) time.

<!-- chunk {"id": "body-0587", "role": "body", "section": "Markov chains", "weight": 1.0} -->

In this section, we briefly review Markov chains. Our notation is chosen to emphasize the analogies with computation chains.

<!-- chunk {"id": "body-0588", "role": "body", "section": "The Markov property", "weight": 1.0} -->

When random variables are organized sequentially as S 1,..., S K, a simple example of conditional independence is when each variable S k ∈ S k only depends on the previous variable S k -1 ∈ S k -1, that is, A probability distribution satisfying the above is said to satisfy the Markov property, and is called a Markov chain. A computation chain is specified by the functions f k, that take s k -1 as input and output s k. In analogy, a Markov chain is specified by the conditional probability distributions p k of S k given S k -1. We can then define the generative process Strictly speaking, we should write S k | S k -1 ∼ p k (· | S k -1). We choose our notation both for conciseness and for analogy with computation chains. Furthermore, to simplify the notation, we assume without loss of generality that S 0 is deterministic (if this is not the case, we can always move S 0 to S 1 and add a dummy variable as S 0). That is, P (S 0 = s 0) = p 0 (s 0):= 1 and S 0:= { s 0 }.

<!-- chunk {"id": "body-0589", "role": "body", "section": "The Markov property", "weight": 1.0} -->

This amounts to setting the initial distribution of S 1 as Figure 10.1: Left: Markov chain. Right: Computation graph of the forwardbackward and the Viterbi algorithms: a lattice.

<!-- chunk {"id": "body-0590", "role": "body", "section": "The Markov property", "weight": 1.0} -->

We can then compute the joint probability of the Markov chain by where we left the dependence on s 0 implicit, since p 0 (s 0) = 1. A Markov chain with S k = { 1, 2, 3 } is illustrated in Fig. 10.1. A chain defines a totally ordered set { 1,..., K }, since two nodes in the graph are necessarily linked to each other by a path.

<!-- chunk {"id": "body-0591", "role": "body", "section": "The Markov property", "weight": 1.0} -->

Example 10.1 (Chain of categorical distributions). Suppose our goal is predict, from x ∈ X, a sequence of length K, where each S k belongs to S k = { 1,..., M }. In natural language processing, this task is called sequence tagging. We can define We emphasize that because k -1 and k are always consecutive, the representation θ k -1,k,i,j is inefficient; we could use θ k,i,j instead. Our notation is designed for consistency with Markov random fields.

<!-- chunk {"id": "body-0592", "role": "body", "section": "Time-homogeneous Markov chains", "weight": 1.0} -->

A time-homogeneous discrete-time Markov chain corresponds to the case when the distribution of S k given S k -1 is the same regardless of k: The fi nite-space case corresponds to when each S k ∈ S can take a finite set of values S = { v 1,..., v M } and where π i,j ∈ is the transition probability from v i to v j. Because the set S = { v 1,..., v M } is discrete, we can always identify it with { 1,..., M }. That is, we can instead write

<!-- chunk {"id": "body-0593", "role": "body", "section": "Higher-order Markov chains", "weight": 1.0} -->

More generally, a n th -order Markov chain may depend, not only on the last variable, but on the last n variables, Autoregressive models such as Transformers (Section 4.8) can be seen as specifying a higher-order Markov chain, with a context window of size n. The larger context makes exact inference using dynamic programming computationally intractable. This is why practitioners use beam search or ancestral sampling (Section 10.5.3) instead.

<!-- chunk {"id": "body-0594", "role": "body", "section": "Bayesian networks", "weight": 1.0} -->

In this section, we briefly review Bayesian networks. Our notation is chosen to emphasize the analogies with computation graphs.

<!-- chunk {"id": "body-0595", "role": "body", "section": "Expressing variable dependencies using DAGs", "weight": 1.0} -->

Markov chains and more generally higher-order Markov chains are a special case of Bayesian network. Similarly to computation graphs reviewed in Section 8.3, variable dependencies can be expressed using a directed acyclic graph (DAG) G = (V, E), where the vertices V = { 1,..., K } represent variables and edges E represent variable dependencies. The set { i 1,..., i n k } = pa(k) ⊆ V, where n k:= | pa(k) |, indicates the variables S i 1,..., S i n k that S k depends. This defines a partially ordered set (poset). For notational simplicity, we again assume without loss of generality that S 0 is deterministic. A computation graph is specified by functions f 1,..., f K in topological order. In analogy, a Bayesian network is specified by conditional probability distributions p k of S k given S pa(k).

<!-- chunk {"id": "body-0596", "role": "body", "section": "Expressing variable dependencies using DAGs", "weight": 1.0} -->

We can then define the generative process Using the chain rule of probability and variable independencies expressed by the DAG, the joint probability distribution is then (assuming a topological order for S 0, S 1,..., S K) This representation is well suited to express causal relationships between random variables.

<!-- chunk {"id": "body-0597", "role": "body", "section": "Parameterizing Bayesian networks", "weight": 1.0} -->

In a Bayesian framework, observed data, latent variables, parameters and noise variables are all treated as random variables. If the conditional distribution p k associated to node k depends on some parameters, they can be provided to p k as conditioning, using parent nodes.

<!-- chunk {"id": "body-0598", "role": "body", "section": "Parameterizing Bayesian networks", "weight": 1.0} -->

A Bayesian network is specified by the conditional distributions p k. Therefore, unlike computation graphs, there is no notion of function f k in a Bayesian network. However, the root nodes of the Bayesian network can be the output of a neural network. For instance, autoregressive models, such as RNNs or Transformers, specify the conditional probability distribution of a token given past tokens, and the chain rule of probability is used to obtain a probability distribution over entire sequences.

<!-- chunk {"id": "body-0599", "role": "body", "section": "Ancestral sampling", "weight": 1.0} -->

A major advantage of Bayesian networks is that, provided that each conditional distribution p k is normalized, the joint distribution of S = ( S 1,..., S K ) is automatically normalized. This means that we can very easily draw i.i.d. samples from the joint distribution, by following the generative process: we follow the topological order k = 1,..., K and on iteration k we draw a value s k ∼ p k ( ·| s pa( k ) ) conditioned on the previous values s pa( k ). This is known as ancestral sampling.

<!-- chunk {"id": "body-0600", "role": "body", "section": "Expressing factors using undirected graphs", "weight": 1.0} -->

A Markov random field (MRF), a.k.a. undirected graphical model, specifies a distribution that factorizes as where C is the set of maximal cliques of G, that is, subsets of V that are fully connected, Z is a normalization constant defined by and ψ C: S C → R + is a potential function (a.k.a. compatibility function), with S C:= (S j) j ∈C. According to the Hammersley-Clifford theorem, an MRF can be equivalently defined in terms of Markov properties; we refer the interested reader to Wainwright and Jordan. For the sake of this chapter, the definition above is sufficient for our purposes.

<!-- chunk {"id": "body-0601", "role": "body", "section": "Expressing factors using undirected graphs", "weight": 1.0} -->

Example 10.2 (Markov chains as Markov random fields). For a chain, letting S = (S 1,..., S K) and s = (s 1,..., s K), recall that This is equivalent to an MRF with Z = 1 (since a chain is auto- matically normalized), and with potential function More generally, a Bayesian network can be similarly written as an MRF by creating appropriate potential functions corresponding to the parents of each node.

<!-- chunk {"id": "body-0602", "role": "body", "section": "MRFs as exponential family distributions", "weight": 1.0} -->

Let us define the potential functions for some sufficient statistic function φ C: S C → Θ C and parameters θ C ∈ Θ C. Then, Therefore, for this choice of potential functions, we can view an MRF as an exponential family distribution (Section 3.4) with natural parameters θ, sufficient statistic φ and log-partition function A (θ).

<!-- chunk {"id": "body-0603", "role": "body", "section": "MRFs as exponential family distributions", "weight": 1.0} -->

Example 10.3 (Ising model). The Ising model is a classical example of MRF. Let Y = (Y 1,..., Y M) ∈ { 0, 1 } M be an unordered collection of binary variables Y i ∈ { 0, 1 }. This forms a graph G = (V, E), where V = [M] and E ⊆ V 2, such that (i, j) ∈ E means that Y i interacts with Y j. In statistical physics, Y i may indicate the presence or absence of particles, or the orientation of magnets. In image processing, Y i may represent a black and white pixel. In multi-label classification, Y i may indicate the presence or absence of a label. The probability of y = (y 1,..., y M) ∈ { 0, 1 } M is then where C:= V ∪ E and θ ∈ R |V| + |E| is the concatenation of (θ i) i ∈V and (θ i,j) (i,j) ∈E. These models are also known as Boltzmann machines in a neural network context.

<!-- chunk {"id": "body-0604", "role": "body", "section": "MRFs as exponential family distributions", "weight": 1.0} -->

MAP inference in general Ising models is known to be NP-hard, but when the interaction weights θ i,j are non-negative, MAP inference can be reduced to graph cut algorithms. There are two ways the above equation can be extended. First, we can use higher-order interactions, such as y i y j y k for (i, j, k) ∈ V 3. Second, we may want to use categorical variables, which leads to the Potts model.

<!-- chunk {"id": "body-0605", "role": "body", "section": "Conditional random fields", "weight": 1.0} -->

Conditional random fields are a special case of Markov random field, in which a conditioning variable is explicitly incorporated. For example, when the goal is to predict a variable y conditioned on a variable x, CRFs are defined as Note that the potential functions Ψ C are allowed to depend on the whole x, as x is just a conditioning variable.

<!-- chunk {"id": "body-0606", "role": "body", "section": "Sampling", "weight": 1.0} -->

Contrary to Bayesian networks, MRFs require an explicit normalization constant Z. As a result, sampling from a distribution represented by a general MRF is usually more involved than for Bayesian networks. A commonly-used technique is Gibbs sampling.

<!-- chunk {"id": "body-0607", "role": "body", "section": "Inference on chains", "weight": 1.0} -->

In this section, we review how to perform marginal inference and maximum a-posteriori inference on joint distributions of the form and where we used ψ k as a shorthand for ψ k -1,k, since k -1 and k are consecutive. As explained in Example 10.2, this also includes Markov chains by setting

<!-- chunk {"id": "body-0608", "role": "body", "section": "The forward-backward algorithm", "weight": 1.0} -->

The key idea of the forward-backward algorithm is to use the distributivity of multiplication over addition to write We can compute these sums recursively, either forward or backward. Recalling the definitions of A k -1 and B k +1 in Eq. (10.1), we define the summations up to and down to k, We can compute the two quantities by recursing forward and backward where we defined the initializations The normalization term can then be computed by and the marginal probabilities by We can also compute the conditional probabilities by In practice, the two recursions are often implemented in the log-domain for numerical stability, We recognize the log-sum-exp operator, which can be implemented in a numerically stable way (Section 4.4.2). The overall dynamic programming procedure, a.k.a. forward-backward algorithm, is summarized in Algorithm 10.1. We notice that the forward and backward passes are actually independent of each other, and can therefore be performed in parallel.

<!-- chunk {"id": "body-0609", "role": "body", "section": "The Viterbi algorithm", "weight": 1.0} -->

Similarly, using the distributivity of multiplication over maximization,

<!-- chunk {"id": "body-0610", "role": "body", "section": "Algorithm 10.1 Marginal inference on a chain", "weight": 1.0} -->

Let us define for k ∈ [K] We can compute these quantities recursively, since for k ∈ [K] with δ 1 (s k):= ψ (s 0, s k). We finally have In practice, for numerical stability, we often implement the forward recursion in the log-domain. Using the fact that the logarithm is monotonic, we indeed have for all k ∈ [K] To enable efficient backtracking, during the forward pass, we compute which can be thought as backpointers from s ⋆ k to s ⋆ k -1.

<!-- chunk {"id": "body-0611", "role": "body", "section": "Algorithm 10.1 Marginal inference on a chain", "weight": 1.0} -->

The resulting dynamic programming procedure, a.k.a. Viterbi algorithm, is summarized in Algorithm 10.2.

<!-- chunk {"id": "body-0612", "role": "body", "section": "Inference on trees", "weight": 1.0} -->

More generally, efficient inference based on dynamic programming can be performed when dependencies between variables are expressed using a tree or polytree. The resulting marginal inference and MAP inference algorithms are often referred to as the sum-product and max-sum algorithms. The sum-product algorithm is also known as belief propagation or message passing, since it can be interpreted as propagating 'local messages' through the graph. See for instance for more details.

<!-- chunk {"id": "body-0613", "role": "body", "section": "Inference as differentiation", "weight": 1.0} -->

In this section, we review the profound connections between differentiating the log-partition function of an exponential family distribution on one hand, and performing marginal inference (as well as maximum a-posteriori inference in the zero-temperature limit) on the other hand.

<!-- chunk {"id": "body-0614", "role": "body", "section": "Inference as gradient of the log-partition", "weight": 1.0} -->

We first discuss a well-known fact in the graphical model literature: when using a binary encoding as the sufficient statistic φ in an exponential family distribution, the gradient ∇ A ( θ ) of the log-partition A ( θ ) gathers all the marginals.

<!-- chunk {"id": "body-0615", "role": "body", "section": "Inference as gradient of the log-partition", "weight": 1.0} -->

To see why, recall from Section 3.4 the definition of an exponential family distribution and of its log-partition Therefore, with the binary encodings in Eq. (10.2) and Eq. (10.3), Put differently, if we have an efficient algorithm for computing A (θ), we can perform reverse-mode autodiff on A (θ) to obtain ∇ A (θ), and therefore obtain the marginal probabilities. Following Section 8.3.3, the complexity of computing all marginal probabilities is therefore roughly the same as that of computing A (θ).

<!-- chunk {"id": "body-0616", "role": "body", "section": "Inference as gradient of the log-partition", "weight": 1.0} -->

In the special case of chains, we obtain where we left the dependence of Z, α and β on θ implicit.

<!-- chunk {"id": "body-0617", "role": "body", "section": "Inference as gradient of the log-partition", "weight": 1.0} -->

We now show i) how to unify the forward pass of the forwardbackward and Viterbi algorithms using semirings and softmax operators ii) how to compute the gradient of the log-partition using backpropagation.

<!-- chunk {"id": "body-0618", "role": "body", "section": "Inference as gradient of the log-partition", "weight": 1.0} -->

If we define A ε ( θ ):= εA ( θ /ε ), in the zero-temperature limit ε → 0, we obtain that µ ( θ ) is a binary encoding of the mode, i.e., of the maximum a-posteriori inference solution.

<!-- chunk {"id": "body-0619", "role": "body", "section": "Semirings and softmax operators", "weight": 1.0} -->

The forward passes in the forward-backward and Viterbi algorithms are clearly similar. In fact, they can be formally linked to each other using semirings.

<!-- chunk {"id": "body-0620", "role": "body", "section": "Semirings and softmax operators", "weight": 1.0} -->

Definition 10.1 (Semiring). A semiring is a set K equipped with two binary operations ( ⊕, ⊗ ) such that

<!-- chunk {"id": "body-0621", "role": "body", "section": "Semirings and softmax operators", "weight": 1.0} -->

- ⊗ is commutative and associative, - ⊕ is associative and distributive over ⊕, - ⊗ and ⊕ have identity element ¯ 0 and ¯ 1, respectively.

<!-- chunk {"id": "body-0622", "role": "body", "section": "Semirings and softmax operators", "weight": 1.0} -->

We use the notations ⊕, ⊗, ¯ 0 and ¯ 1 to clearly distinguish them from the classical addition, multiplication, 0 and 1.

<!-- chunk {"id": "body-0623", "role": "body", "section": "Semirings and softmax operators", "weight": 1.0} -->

We recall the following laws for binary operations: A set equipped with a binary operation supporting associativity and an identity element is called a monoid. A monoid such that every element has an inverse element is called a group. The difference between a ring and a semiring is that the latter only requires (K, ⊕) and (K, ⊗) to be monoids, not groups.

<!-- chunk {"id": "body-0624", "role": "body", "section": "Semirings and softmax operators", "weight": 1.0} -->

- the forward-backward algorithm in the exponential domain uses the semiring R + equipped with (+, ×) and identity elements; - the Viterbi algorithm in the log domain uses the semiring R equipped with (max, +) and identity elements (-∞, 0); - the forward-backward algorithm in the log domain uses the semiring R equipped with (max ε, +) and identity elements (-∞, 0), where we defined the soft max operator (log-add-exp) It can be checked that indeed max ε is commutative, associative, and addition is distributive over max ε. Its identity element is -∞. By associativity, In contrast, note that the sparsemax in Section 13.5 is not associative.

<!-- chunk {"id": "body-0625", "role": "body", "section": "Semirings and softmax operators", "weight": 1.0} -->

Thanks to associativity, we can introduce the shorthand notations Many algorithms can be generalized thanks to the use of semirings; see among others Aji and McEliece and Mohri et al.. The distributive and associative properties play a key role in breaking down large problems into smaller ones.

<!-- chunk {"id": "body-0626", "role": "body", "section": "Inference as backpropagation", "weight": 1.0} -->

In this section, we show that, algorithmically, backtracking is recovered as a special case of backpropagation. See also.

<!-- chunk {"id": "body-0627", "role": "body", "section": "Inference as backpropagation", "weight": 1.0} -->

For notation simplicity, we assume S 0 = { 1 } and S k = { 1,..., M } for all k ∈ [K]. We focus on the case We also introduce the shorthands Our goal is to compute the gradient w.r.t. θ ∈ R K × M × M of The soft argmax counterpart of this quantity is Computing the gradient of A is similar to computing the gradient of a feedforward network, in the sense that θ k influences not only a k but also a k +1,..., a K. Let us introduce the adjoint variable which we initialize as Since θ k,i,j directly influences a k,j, we have for k ∈ [K], i ∈ [M] and j ∈ [M] Since a k,i directly influences a k +1,j for j ∈ [M], we have for k ∈ { 1,..., K -1 } and i ∈ [M] We summarize the procedure in Algorithm 10.3. The forward pass uses the softmax operator max ε and the softargmax operator argmax ε.

<!-- chunk {"id": "body-0628", "role": "body", "section": "Inference as backpropagation", "weight": 1.0} -->

In the hard max case, in Algorithm 10.2, we used q to store backpointers from integer to integer. In the soft max case, in Algorithm 10.3, we used q to store soft backpointers, that is, discrete probability distributions. In the zero-temperature limit, backpropagation outputs a binary encoding of the solution of backtracking.

<!-- chunk {"id": "body-0629", "role": "body", "section": "Summary", "weight": 1.0} -->

- Graphical models represent the conditional dependencies between variables and therefore specify how their joint distribution factorizes. - There are clear analogies between the worlds of functions and of distributions: the counterparts of computation chains and computation graphs are Markov chains and Bayesian networks. - Inference on chains and more generally on trees, for exponential family distributions, is equivalent, both statistically and algorithmically, to differentiating the log-partition function. - The forward-backward algorithm can be seen as using a sumproduct algebra, while the Viterbi algorithm can be seen as using a max-plus algebra. Equivalently, in the log domain, we can see the former as using a soft max, and the latter as using a hard max.

<!-- chunk {"id": "body-0630", "role": "body", "section": "Differentiating through optimization", "weight": 1.0} -->

In this chapter, we study how to differentiate through optimization problems, and more generally through nonlinear systems of equations.

<!-- chunk {"id": "body-0631", "role": "body", "section": "Implicit functions", "weight": 1.0} -->

Implicit functions are functions that do not enjoy an explicit decomposition into elementary functions, for which automatic differentiation, as studied in Chapter 8, can therefore not be directly applied. We describe in this chapter techniques to differentiate through such functions and how to integrate them into an autodiff framework.

<!-- chunk {"id": "body-0632", "role": "body", "section": "Implicit functions", "weight": 1.0} -->

Formally, we will denote an implicit function by w ⋆ ( λ ), where w ⋆: Λ → W. One question is then how to compute the Jacobian ∂ w ⋆ ( λ ). As a first application one can consider sensitivity analysis of a system. For example, w ⋆ ( λ ) could correspond to the equilibrium state of a physical system and in this case, ∂ w ⋆ ( λ ) would tell us about the sensitivity of the system to some parameters λ ∈ Λ.

<!-- chunk {"id": "body-0633", "role": "body", "section": "Optimization problems", "weight": 1.0} -->

Another example is a function implicitly defined as the solution (assumed unique) of an optimization problem where f: W× Λ → R and W denotes a constraint set. Note that we use an arg max for convenience, but the same applies when using an arg min.

<!-- chunk {"id": "body-0634", "role": "body", "section": "Nonlinear equations", "weight": 1.0} -->

More generally, w ⋆ ( λ ) can be defined as the root of some function F: W × Λ → W, i.e., w ⋆ ( λ ) is implicitly defined as the function satisfying the (potentially nonlinear) system of equations

<!-- chunk {"id": "body-0635", "role": "body", "section": "Application to bilevel optimization", "weight": 1.0} -->

Besides sensitivity analysis, another example of application is bilevel optimization. Many times, we want to minimize a function defined as the composition of a fixed function and the solution of an optimization problem. Formally, let f, g: W× Λ → R. We consider the composition h (λ) defined as This includes for instance hyperparameter optimization, where f is an inner log-likelihood objective, g is an outer validation loss, w ∈ W are model parameters and λ ∈ Λ are model hyperparameters, such as regularization strength, as illustrated in Fig. 11.1. To minimize h (λ) one generally resorts to a gradient descent scheme w.r.t. λ, which requires computing ∇ h (λ). Assuming that w ⋆ (λ) is differentiable at λ, by the chain rule, we obtain the Jacobian Figure 11.1: Hyperparameter optimization in nonlinear regression can be cast as a bilevel optimization problem. Each line corresponds to the estimator obtained by fitting some training data (in blue circles) using a different hyperparameter λ. Formally, denoting f the training objective, the estimators are w ⋆ (λ):= arg min w f (w; λ).

<!-- chunk {"id": "body-0636", "role": "body", "section": "Application to bilevel optimization", "weight": 1.0} -->

The goal is to find the best hyperparameter that fits some validation data (here in cyan diamonds), that is, minimizing h (λ):= g (w ⋆ (λ), λ), where g is the validation objective. A too small λ 1 leads to overfitting the training objective and performs badly on validation objective. Conversely, a larger λ 2 underfits both training and validation objectives. The optimal parameter λ ⋆ minimizes the validation objective and may be obtained by iterating gradient descent w.r.t. λ. This requires gradients of h (λ) = g (w ⋆ (λ), λ) w.r.t. λ.

<!-- chunk {"id": "body-0637", "role": "body", "section": "Application to bilevel optimization", "weight": 1.0} -->

Using ∂h (λ) ⊤ = ∇ h (λ) (see Remark 2.4), we obtain the gradient The only problematic term is ∂ w ⋆ (λ), as it requires argmax differentiation. Indeed, most of the time, there is no explicit formula for w ⋆ (λ) and it does not decompose into elementary functions.

<!-- chunk {"id": "body-0638", "role": "body", "section": "Envelope theorems", "weight": 1.0} -->

In the special case g = f, the composition h defined in Eq. (11.1) is simply given by That is, we no longer need argmax differentiation, but only max differentiation, which, as we shall now see is much easier. The function h is often called a value function. The and reason for the name 'envelope' is illustrated in Fig. 11.2. We emphasize that there is not one, but several envelope theorems, depending on the assumptions on f.

<!-- chunk {"id": "body-0639", "role": "body", "section": "Danskin's theorem", "weight": 1.0} -->

When f is concave-convex, we can use Danskin's theorem.

<!-- chunk {"id": "body-0640", "role": "body", "section": "Danskin's theorem", "weight": 1.0} -->

Theorem 11.1 (Danskin's theorem). Let f: W× Λ → R and W be a compact convex set. Let If f is concave in w, convex in λ, and the maximum w ⋆ (λ) is unique, then the function h is differentiable with gradient If the maximum is not unique, we get a subgradient.

<!-- chunk {"id": "body-0641", "role": "body", "section": "Danskin's theorem", "weight": 1.0} -->

Informally, Danskin's theorem means that we can treat w ⋆ ( λ ) as if it were a constant of λ, i.e., we do not need to differentiate through it, even though it depends on λ. Danskin's theorem can also be used to differentiate through a minimum, h ( λ ) = min w ∈W f ( w, λ ), if f ( w, λ ) is convex in w and concave in λ, as we now illustrate.

<!-- chunk {"id": "body-0642", "role": "body", "section": "Danskin's theorem", "weight": 1.0} -->

Example 11.1 (Ilustration of Danskin's theorem). Let us define h ( λ ):= min w ∈ R f ( w,λ ), where f ( w,λ ):= λ 2 w 2 + bw + c and λ > 0. Let w ⋆ ( λ ) be the minimum. The derivative of f w.r.t. λ is 1 2 w 2. From Danskin's theorem, we have h ′ ( λ ) = 1 2 w ⋆ ( λ ). Let us check that this result is correct. The derivative of f w.r.t. w is λw + b. Setting it to zero, we get w ⋆ ( λ ) = -b λ. We thus obtain h ′ ( λ ) = 1 2 b 2 λ 2. Plugging w ⋆ ( λ ) back into f ( w,λ ), we get h ( λ ) = -1 2 b 2 λ + c. Using ( 1 λ ) ′ = -1 λ 2, we indeed obtain the same result for h ′ ( λ ).

<!-- chunk {"id": "body-0643", "role": "body", "section": "Danskin's theorem", "weight": 1.0} -->

Danskin's theorem has a simple interpretation for functions that are linear in λ as shown below.

<!-- chunk {"id": "body-0644", "role": "body", "section": "Danskin's theorem", "weight": 1.0} -->

Example 11.2 (Convex conjugate). Let f ( w, λ ):= 〈 w, λ 〉 -Ω( w ) with Ω convex. We then have h ( λ ) = max w ∈W 〈 w, λ 〉 -Ω( w ) =: Ω ∗ ( λ ), where Ω ∗ denotes the convex conjugate of Ω. Since f satisfies the conditions of Danskin's theorem and since we have ∇ 2 f ( w, λ ) = w, we obtain ∇ h ( λ ) = ∇ Ω ∗ ( λ ) = w ⋆ ( λ ). In other words, in this special case, the gradient of the max is equal to the argmax. This is due to the fact that f ( w, λ ) is linear in λ.

<!-- chunk {"id": "body-0645", "role": "body", "section": "Danskin's theorem", "weight": 1.0} -->

Another application is saddle point optimization.

<!-- chunk {"id": "body-0646", "role": "body", "section": "Danskin's theorem", "weight": 1.0} -->

Example 11.3 (Saddle point problem). Consider the saddle point problem min λ ∈ Λ max w ∈W f ( w, λ ). If it is difficult to minimize w.r.t. λ but easy to maximize w.r.t. w, we can rewrite the problem as min λ ∈ Λ h ( λ ), where h ( λ ):= max w ∈W f ( w, λ ), and use ∇ h ( λ ) to perform (projected) gradient descent w.r.t. λ.

<!-- chunk {"id": "body-0647", "role": "body", "section": "Rockafellar's theorem", "weight": 1.0} -->

A related theorem can be proved under different assumptions on f, in particular without concavity w.r.t. w.

<!-- chunk {"id": "body-0648", "role": "body", "section": "Rockafellar's theorem", "weight": 1.0} -->

Theorem 11.2 (Rockafellar's envelope theorem). Let f: W× Λ → R and W be a compact convex set. Let If f is continuously differentiable in λ for all w ∈ W, ∇ 1 f is continuous and the maximum w ⋆ (λ) is unique, then the function h is differentiable with gradient See Rockafellar and Wets. Compared to Danskin's theorem, Rockafellar's theorem does not require f to be concave-convex, but requires stronger assumptions on the differentiability of f.

<!-- chunk {"id": "body-0649", "role": "body", "section": "Univariate functions", "weight": 1.0} -->

The implicit function theorem (IFT) provides conditions under which an implicit relationship of the form F ( w,λ ) = 0 can be rewritten as a function w = w ⋆ ( λ ) locally, and provides a way to compute its derivative w.r.t. λ.

<!-- chunk {"id": "body-0650", "role": "body", "section": "Univariate functions", "weight": 1.0} -->

Theorem 11.3 (Implicit function theorem, univariate case). Let F: R × R → R. Assume F ( w,λ ) is a continuously differentiable function in a neighborhood U of ( w 0, λ 0 ) such that F ( w 0, λ 0 ) = 0 and ∂ 1 F ( w 0, λ 0 ) = 0. Then there exists a neighborhood V ⊆ U of ( w 0, λ 0 ) in which there is a function w ⋆ ( λ ) such that

<!-- chunk {"id": "body-0651", "role": "body", "section": "Univariate functions", "weight": 1.0} -->

- F (w ⋆ (λ), λ) = 0 for all λ in the neighborhood V, Figure 11.3: The circle equation F (x, y):= x 2 + y 2 -1 = 0 is not a function from y ∈ to x ∈, as there are always two possible x values, x = √ 1 -y 2 or x = -√ 1 -y 2. However, locally around some point (x 0, y 0), e.g., such that x 0 > 0 and y 0 > 0 (upper-right quadrant), the function x = x ⋆ (y) = √ 1 -y 2 is well-defined. The implicit function theorem gives conditions for such a function to exist locally and provides a way to compute its derivative.

<!-- chunk {"id": "body-0652", "role": "body", "section": "Univariate functions", "weight": 1.0} -->

We postpone the proof to the multivariate case and begin with a classical example of application of the theorem.

<!-- chunk {"id": "body-0653", "role": "body", "section": "Univariate functions", "weight": 1.0} -->

Example 11.4 (Equation of the unit circle). We use w ≡ x and λ ≡ y for clarity. Let F ( x, y ):= x 2 + y 2 -1. In general, we cannot rewrite the unit circle equation F ( x, y ) = 0 as a function from y to x, because for every y ∈, there are always two possible x values, namely, x = √ 1 -y 2 or x = -√ 1 -y 2. However, locally around some point ( x 0, y 0 ), e.g., such that x 0 > 0 and y 0 > 0 (upper-right quadrant), the function x = x ⋆ ( y ) = √ 1 -y 2 is welldefined. Using ∂ 1 F ( x, y ) = 2 x and ∂ 2 F ( x, y ) = 2 y, we get ∂x ⋆ ( y ) = -∂ 2 F ( x ⋆ ( y ),y ) ∂ 1 F ( x ⋆ ( y ),y ) = -2 y 2 x ⋆ ( y ) = -y √ 1 -y 2 in that neighborhood (the upper right quadrant in this case).

<!-- chunk {"id": "body-0654", "role": "body", "section": "Univariate functions", "weight": 1.0} -->

This is indeed the same derivative expression as if we used the chain rule on √ 1 -y 2 and is welldefined on y ∈ [0, 1).

<!-- chunk {"id": "body-0655", "role": "body", "section": "Univariate functions", "weight": 1.0} -->

In the above simple example, we can easily derive an explicit function relating y to x in a given neighborhood, but this is not always the case. The IFT gives us conditions guaranteeing that such function exists and a way to differentiate it, but not a way to construct such a function. In fact, finding w ⋆ ( λ ) such that F ( w ⋆ ( λ ), λ ) = 0 typically involves a root finding algorithm, an optimization algorithm, a nonlinear system solver, etc.

<!-- chunk {"id": "body-0656", "role": "body", "section": "Univariate functions", "weight": 1.0} -->

Example 11.5 (Polynomial). Let F ( w,λ ) = w 5 + w 3 + w -λ. According to the Abel-Ruffini theorem, quintics (polynomials of degree 5) do no enjoy roots in terms of radicals and one must resort to numerical root finding. In addition, odd-degree polynomials have real roots. Moreover, ∂ 1 F ( w,λ ) = 5 w 4 +3 w 2 +1 is strictly positive. Therefore, by the intermediate value theorem, there must be only one root w ⋆ ( λ ) such that F ( w ⋆ ( λ ), λ ) = 0. This unique root can for example be found by bisection. Using the IFT, its derivative is found to be ∂w ⋆ ( λ ) = (5 w ⋆ ( λ ) 4 +3 w ⋆ ( λ ) 2 +1) -1.

<!-- chunk {"id": "body-0657", "role": "body", "section": "Univariate functions", "weight": 1.0} -->

While an implicit function is differentiable at a point if the assumptions of the IFT hold in a neighborhood of that point, the reciprocal is not true: failure of the IFT assumptions does not necessarily mean that the implicit function is not differentiable, as we now illustrate.

<!-- chunk {"id": "body-0658", "role": "body", "section": "Univariate functions", "weight": 1.0} -->

Example 11.6 (IFT conditions are not necessary for differentiability). Consider F ( w,λ ) = ( w -λ ) 2. We clearly have that F ( w ⋆ ( λ ), λ ) = 0 if we define w ⋆ ( λ ) = λ, the identity function. It is clearly differentiable for all λ, yet the assumptions of the IFT fail, since we have ∂ 1 F ( w,λ ) = 2( w -λ ) and therefore ∂ 1 F = 0.

<!-- chunk {"id": "body-0659", "role": "body", "section": "Multivariate functions", "weight": 1.0} -->

We now present the IFT in the general multivariate setting. Informally, if F (w ⋆ (λ), λ) = 0, then by the chain rule, we have meaning that the Jacobian ∂ w ⋆ (λ), assuming that it exists, satisfies The IFT gives us conditions for the existence of ∂ w ⋆ (λ).

<!-- chunk {"id": "body-0660", "role": "body", "section": "Multivariate functions", "weight": 1.0} -->

Theorem 11.4 (Implicit function theorem, multivariate case). Let us define F: W× Λ →W. Assume F ( w, λ ) is a continuously differentiable function in a neighborhood of ( w 0, λ 0 ) such that F ( w 0, λ 0 ) = 0 and ∂ 1 F ( w 0, λ 0 ) is invertible, i.e., its determinant is nonzero. Then there exists a neighborhood of λ 0 in which there is a function w ⋆ ( λ ) such that

<!-- chunk {"id": "body-0661", "role": "body", "section": "Multivariate functions", "weight": 1.0} -->

- F (w ⋆ (λ), λ) = 0 for all λ in the neighborhood, We begin with a simple unconstrained optimization algorithm.

<!-- chunk {"id": "body-0662", "role": "body", "section": "Multivariate functions", "weight": 1.0} -->

Example 11.7 (Unconstrained optimization). Assume we want to differentiate through w ⋆ ( λ ) = arg min w ∈ R P f ( w, λ ), where f is strictly convex in w, which ensures that the solution is unique. From the stationary conditions, if we define F ( w, λ ):= ∇ 1 f ( w, λ ), then w ⋆ ( λ ) is uniquely characterized as the root of F in the first argument, i.e., F ( w ⋆ ( λ ), λ ) = 0. We have ∂ 1 F ( w, λ ) = ∇ 2 1 f ( w, λ ), the Hessian of f in w, and ∂ 2 F ( w, λ ) = ∂ 2 ∇ 1 f ( w, λ ), the cross derivatives of f in w and λ.

<!-- chunk {"id": "body-0663", "role": "body", "section": "Multivariate functions", "weight": 1.0} -->

Therefore, assuming that the Hessian is well-defined and invertible at ( w ⋆ ( λ ), λ ), we can use the IFT to differentiate through w ⋆ ( λ ) and obtain ∂ w ⋆ ( λ ) = -( ∇ 2 1 f ( w ⋆ ( λ ), λ )) -1 ∂ 2 ∇ 1 f ( w ⋆ ( λ ), λ ).

<!-- chunk {"id": "body-0664", "role": "body", "section": "Multivariate functions", "weight": 1.0} -->

Next, we generalize the previous example, by allowing constraints in the optimization problem.

<!-- chunk {"id": "body-0665", "role": "body", "section": "Multivariate functions", "weight": 1.0} -->

Example 11.8 (Constrained optimization). Now, assume we want to differentiate through w ⋆ (λ) = arg min w ∈C f (w, λ), where f is strictly convex in w and C ⊆ W is a convex set. A solution is characterized by the fixed point equation w ⋆ (λ) = P C (w ⋆ (λ) η ∇ 1 f (w ⋆ (λ), λ)), for any η > 0, where P (y):= arg min x ∈C ‖ x -y ‖ 2 2 is the Euclidean projection of y onto C. Therefore, w ⋆ (λ) is the root of F (w, λ) = w -P C (w -η ∇ 1 f (w, λ)) (see Chapter 16). We can differentiate through w ⋆ (λ) using the IFT, assuming that the conditions of the theorem apply. Note that ∂ 1 F (w, λ) requires the expression of the Jacobian ∂P C (y). Fortunately, P C (y) and its Jacobian are easy to compute for many sets C.

<!-- chunk {"id": "body-0666", "role": "body", "section": "JVP and VJP of implicit functions", "weight": 1.0} -->

To integrate an implicit function w ⋆ ( λ ) in an autodiff framework, we need to be able to compute its JVP or VJP. This is the purpose of the next proposition.

<!-- chunk {"id": "body-0667", "role": "body", "section": "JVP and VJP of implicit functions", "weight": 1.0} -->

Proposition 11.1 (JVP and VJP of implicit functions). Let w ⋆: Λ → W be a function implicitly defined as the solution of F (w ⋆ (λ), λ) = 0, for some function F: W× Λ →W. Define Assume the assumptions of the IFT hold. The JVP t:= ∂ w ⋆ (λ) v in the input direction v ∈ Λ is obtained by solving the linear system The VJP ∂ w ⋆ (λ) ∗ u in the output direction u ∈ W is obtained by solving the linear system Using the solution r, we get Note that in the above linear systems, we can access to A and B as linear maps, the JVPs of F. Their adjoints, A ∗ and B ∗, correspond to the VJPs of F. To solve these systems, we can therefore use matrix-free solvers as detailed in Section 9.4. For example, when A is symmetric pos- itive semi-definite, we can use the conjugate gradient method. When A is not symmetric positive definite, we can use GMRES or BiCGSTAB.

<!-- chunk {"id": "body-0668", "role": "body", "section": "Differentiating nonlinear equations", "weight": 1.0} -->

We describe in this section the adjoint state method (a.k.a. adjoint method, method of adjoints, adjoint sensitivity method). The method can be used to compute the gradient of the composition of an explicit function and an implicit function, defined through an equality constraint (e.g., a nonlinear equation ). The method dates back to Céa.

<!-- chunk {"id": "body-0669", "role": "body", "section": "Differentiating nonlinear equations", "weight": 1.0} -->

Suppose a variable s ∈ S (which corresponds to a state in optimal control) is implicitly defined given some parameters w ∈ W through the (potentially nonlinear) equation c (s, w) = 0, where c: S × W → S. Assuming s is uniquely determined for all w ∈ W, this defines an implicit function s ⋆ (w) from W to S such that c (s ⋆ (w), w) = 0. Given an objective function L: S × W → R, the goal of the adjoint state method is then to compute the gradient of However, this is not trivial as s ⋆ (w) is an implicit function. For instance, this can be used to convert the equality-constrained problem into the unconstrained problem Access to ∇ L (w) allows us to solve this problem by gradient descent.

<!-- chunk {"id": "body-0670", "role": "body", "section": "Differentiating nonlinear equations", "weight": 1.0} -->

Proposition 11.2 (Adjoint state method). Let c: S × W → S be a mapping defining constraints of the form c (s, w). Assume that for each w ∈ W, there exists a unique s ⋆ (w) satisfying c (s ⋆ (w), w) = 0 and that s ⋆ (w) is differentiable. The gradient of for some differentiable function L: S × W → R, is given by where r ⋆ (w) is the solution of the linear system As shown in the proof below, r ⋆ (w) corresponds to a Lagrange multiplier. The linear system can be solved using matrix-free solvers.

<!-- chunk {"id": "body-0671", "role": "body", "section": "Relation with envelope theorems", "weight": 1.0} -->

Because s is uniquely determined for any w ∈ W by c (s, w) = 0, we can alternatively rewrite L (w) as the trivial minimization or maximization, Therefore, the adjoint state method can be seen as an envelope theorem for computing ∇ L (w), for the case when w is involved in both the objective function and in the equality constraint.

<!-- chunk {"id": "body-0672", "role": "body", "section": "Reverse mode as adjoint method with backsubstitution", "weight": 1.0} -->

In this section, we revisit reverse-mode autodiff from the perspective of the adjoint state method. For clarity, we focus our exposition on feedforward networks with input x ∈ X and network weights w = (w 1,..., w k) ∈ W 1 ×... ×W K, Here we focus on gradients with respect to the parameters w, hence the notation f (w). We can use the adjoint state method to recover reverse-mode autodiff, and prove its correctness in the process. While we focus for simplicity on feedforward networks, our exposition can be generalized to computation graphs.

<!-- chunk {"id": "body-0673", "role": "body", "section": "Feedforward networks as the solution of a nonlinear equation", "weight": 1.0} -->

While we defined the set of intermediate computations s = (s 1,..., s K) ∈ S 1 ×... ×S K as a sequence of operations, they can also be defined as the unique solution of the nonlinear equation c (s, w) = 0, where This defines an implicit function s ⋆ (w) = (s ⋆ 1 (w),..., s ⋆ K (w)), the solution of this nonlinear system, which is given by the variables s 1,..., s K defined in Eq. (11.2). The output of the feedforward network is then f (w) = s ⋆ K (w).

<!-- chunk {"id": "body-0674", "role": "body", "section": "Feedforward networks as the solution of a nonlinear equation", "weight": 1.0} -->

In machine learning, the final layer s ⋆ K (w) is typically fed into a loss ℓ, to define Note that an alternative is to write L (w) as More generally, if we just want to compute the VJP of s ⋆ K (w) in some direction u K ∈ S K, we can define the scalar-valued function Let us define u ∈ S 1 ×···×S K -1 ×S K as u:= (0,..., 0, ∇ 1 ℓ (f (w); y)) (gradient of the loss ℓ case) or u:= (0,..., 0, u K) (VJP of f in the direction u K case). Using the adjoint state method, we know that the gradient of this objective is obtained as for r ⋆ (w) the solution of the linear system

<!-- chunk {"id": "body-0675", "role": "body", "section": "Solving the linear system using backsubtitution", "weight": 1.0} -->

The JVP of the constraint function c at s ⋆ (w), materialized as a matrix, takes the form of a block lower-triangular matrix where A k:= ∂ 1 f k (s k -1, w k). Crucially the triangular structure of the JVP stems from the fact that each intermediate activation only depends from the past intermediate activations. Therefore, the constraints, corresponding to the lines of the Jacobian, cannot introduce non-zero values beyond its diagonal. The VJP takes the form of a block uppertriangular matrix Solving an upper triangular system like ∂ 1 c (s (w), w) ∗ r = u can then be done efficiently by backsubstitution. Starting from the last adjoint state r K = u, we can compute each adjoint state r k from that computed at k +1. Namely, for k ∈ (K -1,..., 1), we have The VJPs with respect to the parameters are then obtained by recovering reverse-mode autodiff.

<!-- chunk {"id": "body-0676", "role": "body", "section": "Solving the linear system using backsubtitution", "weight": 1.0} -->

The Lagrangian perspective of backpropagation for networks with separate parameters w = ( w 1,..., w K ) is well-known; see for instance LeCun or Recht. The Lagrangian perspective of backpropagation through time for networks with shared parameter w is discussed for instance by Franceschi et al.. Our exposition uses the adjoint state method, which can itself be proved either using the method of Lagrange multipliers (Section 11.4.3) or by the implicit function theorem (Section 11.4.4), combined with backsubtitution for solving the upper-triangular linear system. Past works often minimize over w but we do not require this, as gradients are not necessarily used for optimization. Our exposition also supports computing the VJP of any vector-valued function f, while existing works derive the gradient of a scalar-valued loss function.

<!-- chunk {"id": "body-0677", "role": "body", "section": "Differentiating inverse functions", "weight": 1.0} -->

In some cases (see for instance Section 12.4.4), it is useful to compute the Jacobian of an inverse function f -1. The inverse function theorem below allows us to relate the Jacobian of f -1 with the Jacobian of f.

<!-- chunk {"id": "body-0678", "role": "body", "section": "Differentiating inverse functions", "weight": 1.0} -->

Theorem 11.5 (Inverse function theorem). Assume f: W → W is continuously differentiable with invertible Jacobian ∂f ( w 0 ) at w 0. Then f is bijective from a neighborhood of w 0 to a neighborhood of f ( w 0 ). Moreover, the inverse f -1 is continuously differentiable near ω 0 = f ( w 0 ) and the Jacobian of the inverse ∂f -1 ( ω ) is

<!-- chunk {"id": "body-0679", "role": "body", "section": "Link with the implicit function theorem", "weight": 1.0} -->

The inverse function theorem can be used to prove the implicit function theorem; see proof of Theorem 11.4. Conversely, recall that, in order to use the implicit function theorem, we need to choose a root objective F: W × Λ → W. If we set W = Λ = R Q and F ( w, ω ) = f ( w ) -ω, with f: R Q → R Q, then we have that the root w ⋆ ( ω ) satisfying F ( w ⋆ ( ω ), ω ) = 0 is exactly w ⋆ ( ω ) = f -1 ( ω ). Moreover, ∂ 1 F ( w, ω ) = ∂f ( w ) and ∂ 2 F ( w, ω ) = -I. By applying the implicit function theorem with this F, we indeed recover the inverse function theorem.

<!-- chunk {"id": "body-0680", "role": "body", "section": "Summary", "weight": 1.0} -->

- Implicit functions are functions that cannot be decomposed into elementary operations and for which autodiff can therefore not be directly applied. Examples are optimization problems and nonlinear equations.

<!-- chunk {"id": "body-0681", "role": "body", "section": "Summary", "weight": 1.0} -->

- Envelope theorems can be used for differentiating through the min or max value (not solution) of a function. - More generally, the implicit function theorem allows us to differentiate through implicit functions. It gives conditions for the existence of derivatives and how to obtain them. - The adjoint state method can be used to obtain the gradient of the composition of an explicit function and of an implicit function, specified by equality constraints. It can be used to prove the correctness of reverse-mode autodiff. - The inverse function theorem can be used to differentiate function inverses. - In a sense, the implicit function theorem can be thought as the mother theorem, as it can be used to prove envelope theorems, the adjoint state method and the inverse function theorem.

<!-- chunk {"id": "body-0682", "role": "body", "section": "Differentiating through integration", "weight": 1.0} -->

In this chapter, we study how to differentiate through integrals, with a focus on expectations and solutions of ordinary differential equations.

<!-- chunk {"id": "body-0683", "role": "body", "section": "Differentiation under the integral sign", "weight": 1.0} -->

Given two Euclidean spaces Θ and Y, and a function f: Θ ×Y → R, we often want to differentiate an integral of the form Provided that we can swap integration and differentiation, we have The conditions enabling us to do so are best examined in the context of measure theory. We refer the reader to e.g. for a course on measure theory and Flanders for an in-depth study of the differentiation under the integral sign. Briefly, if Θ = Y = R, the following conditions are sufficient. 1. f is measurable in both its arguments, and f (θ, ·) is integrable for almost all θ ∈ Θ fixed, 2. f (·, y) is absolutely continuous for almost all y ∈ Y, that is, there exists an integrable function g (·, y) such that f (θ, y) = f (θ 0, y) + ∫ θ θ 0 g (τ, y) dτ, 3.

<!-- chunk {"id": "body-0684", "role": "body", "section": "Differentiation under the integral sign", "weight": 1.0} -->

∂ 1 f (θ, y) (which exists almost everywhere if f (·, y) is absolutely continuous), is locally integrable, that is, for any closed interval [θ 0, θ 1], the integral ∫ θ 1 θ 0 ∫ | ∂ 1 f (θ, y) | dydθ is finite.

<!-- chunk {"id": "body-0685", "role": "body", "section": "Differentiation under the integral sign", "weight": 1.0} -->

Any differentiable function f: Θ × Y → R is absolutely continuous. However, the conditions also hold if f is just absolutely continuous, that is, if f ( ·, y ) is differentiable for almost all y. This weaker assumption can be used to smooth out differentiable almost-everywhere functions, such as the ReLu, as we study in Section 14.4.

<!-- chunk {"id": "body-0686", "role": "body", "section": "Differentiating through expectations", "weight": 1.0} -->

A special case of differentiating through integrals is differentiating through expectations. We can distinguish between two cases, depending on whether the parameters θ we wish to differentiate are involved in the distribution or in the function, whose expectation we compute.

<!-- chunk {"id": "body-0687", "role": "body", "section": "Parameter-independent distributions", "weight": 1.0} -->

We first consider expectations of the form for a random variable Y ∈ Y ⊆ R M, distributed according to a distribution p, and a function g: Y × Θ → R. Importantly, the distribution is independent of the parameters θ. Under mild conditions recalled in Section 12.1, we can swap differentiation and integration to obtain Generally, the expectation cannot be computed in closed form. However, provided that we can sample from p, we can define a Monte-Carlo estimator of the value for N i.i.d. samples Y 1,..., Y N from p. These estimators are unbiased, meaning that E [̂ F N (θ)] = F (θ) and E [∇ ̂ F N (θ)] = ∇ F (θ), and converge to the true quantity as N → + ∞. This suggests a simple implementation in an autodiff framework of the approximation of ∇ F (θ): 3. Compute the gradient ∇ ̂ F N (θ) by automatic differentiation.

<!-- chunk {"id": "body-0688", "role": "body", "section": "Parameter-independent distributions", "weight": 1.0} -->

Computing higher order derivatives follow the same principle: to get an approximation of ∇ 2 F ( θ ), we can simply compute ∇ 2 ̂ F N ( θ ) by autodiff. As such, the implementation delineated above is akin to the 'discretize-then-optimize' approach used to differentiate through the solution of an ODE (Section 12.6): we implement an approximation of the objective and simply call autodiff on it.

<!-- chunk {"id": "body-0689", "role": "body", "section": "Parameter-dependent distributions", "weight": 1.0} -->

A more challenging case arises when the distribution depends on the parameters θ: where Y ∈ Y ⊆ R M is a random variable, distributed according to a distribution p θ parameterized by θ ∈ Θ and where g: Y → R is, depending on the setting, potentially a blackbox function (i.e., we do not and of the gradient have access to its gradients). Typically, θ ∈ Θ could be parameters we wish to estimate, or it could indirectly be generated by θ = f (x, w) ∈ Θ, where f is a neural network with parameters w ∈ W we wish to estimate. The main difficulty in computing ∇ E (θ) stems from the fact that θ are the parameters of the distribution p θ. Estimating an expectation E (θ) = E Y ∼ p θ [g (Y)] using Monte-Carlo estimation requires us to sample from p θ. However, it is not clear how to differentiate E w.r.t. θ if θ is involved in the sampling process.

<!-- chunk {"id": "body-0690", "role": "body", "section": "Continuous case", "weight": 1.0} -->

When Y is a continuous set (that is, p θ (y) is a probability density function), we can rewrite E (θ) as Provided that we can swap integration and differentiation (see Section 12.1), we then have Unfortunately, this integral is not an expectation and it could be intractable in general.

<!-- chunk {"id": "body-0691", "role": "body", "section": "Discrete case", "weight": 1.0} -->

When Y is a discrete set (that is, p θ (y) is a probability mass function), we can rewrite E (θ) as Again ∇ E (θ) is not an expectation. We therefore cannot use MonteCarlo estimation to estimate the gradient. Instead, we can compute it In Sections 12.3 and 12.4, we review the score function and pathwise gradient estimators, to (approximately) compute ∇ E (θ), allowing us to optimize θ (or w using the chain rule) by gradient-based algorithms. by brute force, i.e., by summing over all possible y ∈ Y. However, this is clearly only computationally tractable if |Y| is small or if p θ is designed to have sparse support, i.e., so that the set { y ∈ Y: p θ (y) = 0 } is small. Moreover, even if these conditions hold, summing over y could be problematic if g (y) is expensive to compute. Therefore, exact gradients are seldom used in practice.

<!-- chunk {"id": "body-0692", "role": "body", "section": "Application to expected loss functions", "weight": 1.0} -->

Differentiating through expectations is particularly useful when working with expected loss functions of the form where y is some ground truth. Equivalently, we can set ℓ = -r, where r is a reward function. As we shall see, the score function estimator will support a discrete loss function ℓ: Y × Y → R, while the pathwise gradient estimator will require a differentiable loss function ℓ: R M ×Y → R. Intuitively, L (θ; y) will be low if p θ assigns high probability to predictions ̂ y with low loss value ℓ (̂ y, y).

<!-- chunk {"id": "body-0693", "role": "body", "section": "Application to expected loss functions", "weight": 1.0} -->

In the classification setting, where Y = [M], p θ is often chosen to be the Gibbs distribution, which is a categorical distribution induced by a softargmax where θ y:= f (x, y, w) ∈ R are logits produced by a neural network f. More generally, in the structured prediction setting, where Y ⊆ R M but |Y| ≫ M, we often use the distribution Given a distribution ρ over X × Y, we then want to minimize the expected loss function, also known as risk, Typically, minimizing R (w) is done through some form of gradient descent, which requires us to be able to compute Computing ∇ R (w) therefore boils down to computing the gradient of L (θ; y), which is the gradient of an expectation.

<!-- chunk {"id": "body-0694", "role": "body", "section": "Application to experimental design", "weight": 1.0} -->

In experimental design, we wish to minimize a function g ( λ ), which we assume costly to evaluate. As an example, evaluating g ( λ ) could require us to run a scientific experiment with parameters λ ∈ R Q. As another example, in hyperparameter optimization, evaluating g ( λ ) would require us to run a learning algorithm with hyperparameters λ ∈ R Q. Instead of solving the problem arg min λ ∈ R Q g ( λ ), we can lift the problem to probability distributions and solve arg min θ ∈ R M E ( θ ), where E ( θ ) = E λ ∼ p θ [ g ( λ )]. This requires the probability distribution p θ to assign high probability to λ values that achieve small g ( λ ) value. Solving this problem by stochastic gradient descent requires us to be able to compute estimates of ∇ E ( θ ). This can be done for instance with SFE explained in Section 12.3, which does not require gradients of g, unlike implicit differentiation explained in Chapter 11. This approach also requires us to choose a distribution p θ over λ.

<!-- chunk {"id": "body-0695", "role": "body", "section": "Application to experimental design", "weight": 1.0} -->

For continuous hyperparameters, a natural choice would be the normal distribution λ ∼ Normal( µ, Σ ), setting θ = ( µ, Σ ). Once we obtained θ by minimizing E ( θ ), we need a way to recover λ. This can be done for example by choosing the mode of the distribution, i.e., arg max λ ∈ R Q p θ ( λ ), or the mean of the distribution E λ ∼ p θ ( λ ) [ λ ]. Of course, in the case of the normal distribution, they coincide.

<!-- chunk {"id": "body-0696", "role": "body", "section": "Scalar-valued functions", "weight": 1.0} -->

The key idea of the score function estimator (SFE), also known as REINFORCE, is to rewrite ∇ E (θ) as an expectation. The estimator is based on the logarithmic derivative identity Using this identity, we obtain the following gradient estimator.

<!-- chunk {"id": "body-0697", "role": "body", "section": "Scalar-valued functions", "weight": 1.0} -->

Proposition 12.1 (SFE for scalar-valued functions). Given a family of distributions p θ on Y, for θ ∈ Θ, define where Y ∈ Y ⊆ R M and g: Y → R. Then, The gradient of the log-PDF w.r.t. θ, ∇ θ log p θ (y), is known as the score function, hence the estimator name. SFE is suitable when two requirements are met: it is easy to sample from p θ and the score function is available in closed form. Since the SFE gradient is an expectation, we can use Monte-Carlo estimation to compute an unbiased estimator of ∇ E (θ): where Y 1,..., Y N are sampled from p θ.

<!-- chunk {"id": "body-0698", "role": "body", "section": "Scalar-valued functions", "weight": 1.0} -->

Interestingly, the gradient of g is not needed in this estimator. Therefore, there is no differentiability assumption about g. This is why SFE is useful when g is a discrete loss function or more generally a blackbox function.

<!-- chunk {"id": "body-0699", "role": "body", "section": "Scalar-valued functions", "weight": 1.0} -->

Example 12.1 (SFE with a language model). In a language model, the probability of a sentence y = (y 1,..., y L) is typically factored using the chain rule of probability (see Section 10.1) where p θ is modeled using a transformer or RNN. Note that the probabilities are normalized by construction, so there is no need for an explicit normalization constant. Thanks to this factorization, it is easy to sample from p θ using ancestral sampling (see Section 10.5.3) and the log-probability enjoys the simple expression This gradient is easy to compute, since the token-wise distributions p θ (y j | y 1,..., y j -1) are typically defined using a softargmax. We can therefore easily compute ∇ E (θ) under p θ using SFE. This is for instance useful to optimize an expected reward, in order to finetune or align a language model.

<!-- chunk {"id": "body-0700", "role": "body", "section": "Scalar-valued functions", "weight": 1.0} -->

Another example when ∇ θ p θ ( y ) is available in closed form is in the context of reinforcement learning, where p θ ( y ) is a Markov Decision Process (MDP) and is called the policy. Applying the SFE leads to the (vanilla) policy gradient method and can then be used to compute the gradient of an expected cumulative reward. However, SFE is more problematic when used with the Gibbs distribution, due to the explicit normalization constant.

<!-- chunk {"id": "body-0701", "role": "body", "section": "Scalar-valued functions", "weight": 1.0} -->

Example 12.2 (SFE with a Gibbs distribution). The Gibbs distribu- tion is parameterized, for θ ∈ R Y, where we defined the log-partition function A typical parametrization is θ y = f (x, y, w) with f the output of network on a sample x with parameters w. We then have We therefore see that ∇ θ log p θ (y) crucially depends on ∇ A (θ), the gradient of the log-partition. This gradient is available for some structured sets Y, see e.g., but not in general.

<!-- chunk {"id": "body-0702", "role": "body", "section": "Scalar-valued functions", "weight": 1.0} -->

As another example, we apply SFE in Section 14.4 to derive the gradient of perturbed functions.

<!-- chunk {"id": "body-0703", "role": "body", "section": "Differentiating through both the distribution and the function", "weight": 1.0} -->

Suppose both the distribution and the function now depend on θ. When g is scalar-valued and differentiable w.r.t. θ, we want to differentiate Using the product rule, we obtain

<!-- chunk {"id": "body-0704", "role": "body", "section": "Differentiating through joint distributions", "weight": 1.0} -->

Suppose we now want to differentiate through The gradient is then given by which is easily seen by applying Proposition 12.1 on the joint distribution ρ θ:= p θ · q θ. The extension to more than two variables is straightforward.

<!-- chunk {"id": "body-0705", "role": "body", "section": "Bias and variance", "weight": 1.0} -->

Recall the definition of ̂ γ N in Eq. (12.1). SFE is an unbiased estimator, meaning that where the expectation is taken with respect to the N samples drawn. Since the gradient is vector-valued, we need to define a scalar-valued notion of variance. We do so by using the squared Euclidean distance in the usual variance definition to define The variance naturally goes to zero as N →∞.

<!-- chunk {"id": "body-0706", "role": "body", "section": "Baseline", "weight": 1.0} -->

SFE is known to suffer from high variance. This means that this estimator may require us to draw many samples from the distribution p θ to work well in practice. One of the simplest variance reduction technique consists in shifting the function g with a constant β, called a baseline, to obtain The reason this is still a valid estimator of ∇ E (θ) stems from for any valid distribution p θ. The baseline β is often set to the running average of past values of the function g, though it is neither optimal nor does it guarantee to lower the variance.

<!-- chunk {"id": "body-0707", "role": "body", "section": "Control variates", "weight": 1.0} -->

Another general technique are control variates. Let us denote the expectation of a function h: R M → R under the distribution p θ as Suppose that H (θ) and its gradient ∇ H (θ) are known in closed form. Then, for any γ ≥ 0, we clearly have Applying SFE, we then obtain Examples of h include a bound on f or a second-order Taylor expansion of f, assuming that these approximations are easier to integrate than f.

<!-- chunk {"id": "body-0708", "role": "body", "section": "Vector-valued functions", "weight": 1.0} -->

It is straightforward to extend the SFE to vector-valued functions.

<!-- chunk {"id": "body-0709", "role": "body", "section": "Vector-valued functions", "weight": 1.0} -->

Proposition 12.2 (SFE for vector-valued functions). Given a family of distributions p θ on Y, for θ ∈ Θ, define where Y ∈ Y, g: Y → G. The JVP of E at θ ∈ Θ along v ∈ Θ is and the VJP of E at θ ∈ Θ along u ∈ G is The Jacobian of E at θ ∈ Θ can then be written as where ⊗ denote the outer product.

<!-- chunk {"id": "body-0710", "role": "body", "section": "Vector-valued functions", "weight": 1.0} -->

Proof. The VJP of E at θ ∈ Θ along u ∈ Θ amounts to compute the gradient of the scalar function The expression of the VJP follows by using the SFE on the scalar valued integrand 〈 g (Y), u 〉. The JVP is obtained as the adjoint operator of the VJP and the Jacobian follows.

<!-- chunk {"id": "body-0711", "role": "body", "section": "Differentiating through both the distribution and the function", "weight": 1.0} -->

If θ now influences both the distribution and the function,

<!-- chunk {"id": "body-0712", "role": "body", "section": "Second derivatives", "weight": 1.0} -->

Using the previous subsection with g ( y, θ ) = g ( y ) ∇ θ log p θ ( θ ), we easily obtain an estimator of the Hessian.

<!-- chunk {"id": "body-0713", "role": "body", "section": "Second derivatives", "weight": 1.0} -->

Proposition 12.3 (SFE for the Hessian). Let us define the scalarvalued function E (θ):= E Y ∼ p θ [g (Y)]. Then, This can also be derived using the second-order log-derivative

<!-- chunk {"id": "body-0714", "role": "body", "section": "Link with the Bartlett identities", "weight": 1.0} -->

The Bartlett identities are expressions relating the moments of the score function (gradient of the log-likelihood function). Using Proposition 12.1 with g (y) = 1 and ∫ Y p θ (y) d y = 1, we obtain which is known as Bartlett's first identity. Similarly, using Proposition 12.3, we obtain which is known as Bartlett's second identity.

<!-- chunk {"id": "body-0715", "role": "body", "section": "Path gradient estimators, reparametrization trick", "weight": 1.0} -->

As we saw previously, the main difficulty in computing gradients of expectations arises when the parameters θ play a role in the distribution p θ being sampled. The key idea of path gradient estimators (PGE), also known as reparametrization trick, is to rewrite the expectation in such a way that the parameters are moved from the distribution to the function, using a change of variable.

<!-- chunk {"id": "body-0716", "role": "body", "section": "Location-scale transforms", "weight": 1.0} -->

The canonical example of path gradient estimator is differentiating through the expectation where g: R → R is a differentiable function. If we let Z ∼ Normal, it is easy to check that U = µ + σZ. We can therefore write The key advantage is that we can now easily compute the derivatives by mere application of the chain rule, since the parameters µ and σ are moved from the distribution to the function: The change of variable is called a location-scale transform. Such a transformation exists, not only for the normal distribution, but for location-scale family distributions, i.e., distributions parametrized by a location parameter µ and a scale parameter σ > 0, such that U is distributed according to a distribution in the same family as Z is distributed. Besides the normal distribution, examples of location-scale family distributions include the Cauchy distribution, the uniform distribution, the logistic distribution, the Laplace distribution, and Student's t -distribution.

<!-- chunk {"id": "body-0717", "role": "body", "section": "Location-scale transforms", "weight": 1.0} -->

We can easily relate the cumulative distribution function (CDF) and the probability density function (PDF) of Z to that of U, and vice-versa.

<!-- chunk {"id": "body-0718", "role": "body", "section": "Location-scale transforms", "weight": 1.0} -->

Proposition 12.4 (CDF and PDF of location-scale family distributions) Let F Z (z):= P (Z ≤ z) and f Z (z):= F ′ (z). If U:= µ + σZ, then and we obtain f Z (z) by differentiating F Z (z).

<!-- chunk {"id": "body-0719", "role": "body", "section": "Differentiable transforms", "weight": 1.0} -->

We can generalize the idea of path gradient estimator (PGE) to any change of variable where T: R M × R Q → R M is a differentiable transformation. For example, if we gather µ and σ as θ:= (µ, σ), we can write the location-scale transform as We can derive the path gradient estimator for any such differentiable transformation T.

<!-- chunk {"id": "body-0720", "role": "body", "section": "Differentiable transforms", "weight": 1.0} -->

Proposition 12.5 (Path gradient estimator). Let us define where U ∈ U ⊆ R M and g: R M → R is differentiable. Suppose there is a differentiable transformation T: R M × R Q → R M such that if Z ∼ p (where p does not depend on θ) and U:= T (Z, θ), then U ∼ p θ. Then, we have where h (z, θ):= g (T (z, θ)). This implies The path gradient estimator (a.k.a. reparametrization trick) gives an unbiased estimator of ∇ E (θ). It has however two key disadvantages. First, it assumes that g is differentiable (almost everywhere), which may not always be the case. Second, it assumes that g is well-defined on R M, not on U, which could be problematic for some discrete loss functions, such as the zero-one loss function or ranking loss functions.

<!-- chunk {"id": "body-0721", "role": "body", "section": "Differentiable transforms", "weight": 1.0} -->

As an example of differentiable transform, in machine learning, we can sample Gaussian noise Z and make it go through a neural network with parameters w to generate an image X:= T ( Z, w ). In statistics, many distributions are related to each other through differentiable transforms, as we recall below.

<!-- chunk {"id": "body-0722", "role": "body", "section": "Differentiable transforms", "weight": 1.0} -->

Example 12.3 (Some differentiable transforms in statistics). Wegive below a non-exhaustive list of differentiable transform examples.

<!-- chunk {"id": "body-0723", "role": "body", "section": "Differentiable transforms", "weight": 1.0} -->

- If X ∼ Normal(µ, σ 2), then exp(X) ∼ Lognormal(µ, σ 2). - If U ∼ Uniform, then -log(U) /λ ∼ Exponential(λ). - If X 1,..., X N ∼ Exponential(λ) (i.i.d.), then ∑ N i =1 X i ∼ Gamma(N,λ). - If X i ∼ Gamma(α i, θ) for i ∈ [K], then (X 1 ∑ K i =1 X i,..., X K ∑ K i =1 X i) ∼ Dirichlet(α 1,..., α K).

<!-- chunk {"id": "body-0724", "role": "body", "section": "Inverse transforms", "weight": 1.0} -->

The inverse transform method can be used for sampling from a probability distribution, given access to its associated quantile function. Recall that the cumulative distribution function (CDF) associated with a random variable Y is the function F Y: R → defined by The quantile function is then a function Q Y: → R such that Q Y (π) = y for π = F Y (y). Assuming F Y is continuous and strictly increasing, we have that Q Y is the inverse CDF, In the general case of CDF functions that are not strictly increasing, the quantile function is usually defined as Given access to the quantile function Q Y (π) associated with a distribution p, inverse transform sampling allows us to sample from p by first drawing a sample from the uniform distribution and then making this sample go through the quantile function.

<!-- chunk {"id": "body-0725", "role": "body", "section": "Inverse transforms", "weight": 1.0} -->

Proposition 12.6 (Inverse transform sampling). Suppose Y ∼ p, where p is a distribution with quantile function Q Y. If U ∼ Uniform, then Q Y ( U ) ∼ p.

<!-- chunk {"id": "body-0726", "role": "body", "section": "Inverse transforms", "weight": 1.0} -->

Proof. If π ≤ F Y (t), then by definition of Q Y, Q Y (π) ≤ t. If π ≥ F Y (t), then by definition of Q Y, F Y (Q Y (π)) ≥ π, so F Y (Q Y (π)) ≥ F Y (t) and since a CDF is always non-decreasing, Q Y (π) ≥ t. Hence, we have, Q Y (π) ≤ t ⇐⇒ π ≤ F Y (t), so The CDFs of Q Y (U) and Y coincide, hence they have the same distribution.

<!-- chunk {"id": "body-0727", "role": "body", "section": "Inverse transforms", "weight": 1.0} -->

If the quantile function is differentiable, we can therefore use it as a transformation within the reparametrization trick. Indeed, if Y ∼ p θ, where p θ is a distribution with parameter θ and quantile function Q Y (π, θ), then we have and therefore, by the reparametrization trick (Proposition 12.5), Example 12.4 (Examples of quantile functions). If Y ∼ Exponential(λ), the CDF of Y is π = F Y (y) = 1 -exp(-λy) for y ≥ 0 and therefore the quantile function is Q Y (π, λ) = -log(1 -π) λ. If Y ∼ Normal(µ, σ 2), the CDF is F Y (y) = 1 2 [1 + erf (y -µ σ √ 2)] and the quantile function is Q Y (π, θ) = µ + σ √ 2 · erf -1 (2 π -1), where θ = (µ, σ). This therefore defines an alternative transformation to the location-scale transformation in Eq. (12.4).

<!-- chunk {"id": "body-0728", "role": "body", "section": "Inverse transforms", "weight": 1.0} -->

Note that, in the above example, the error function erf and its inverse do not enjoy analytical expressions but autodiff packages usually provide numerical routines to compute them and differentiate through them. Nonetheless, one caveat of the inverse transform is that it indeed requires access to (approximations of) the quantile function and its derivatives, which may be difficult for complicated distributions.

<!-- chunk {"id": "body-0729", "role": "body", "section": "Pushforward distributions", "weight": 1.0} -->

We saw so far that the reparametrization trick is based on using a change of variables in order to differentiate an expectation w.r.t. the parameters of the distribution. In this section, we further formalize that approach using pushforward distributions.

<!-- chunk {"id": "body-0730", "role": "body", "section": "Pushforward distributions", "weight": 1.0} -->

Definition 12.1 (Pushforward distribution). Suppose Z ∼ p, where p is a distribution over Z. Given a continuous map T: Z → U, the pushforward distribution of p through T is the distribution q according to which U:= T ( Z ) ∈ U is distributed, i.e., U ∼ q.

<!-- chunk {"id": "body-0731", "role": "body", "section": "Pushforward distributions", "weight": 1.0} -->

Although not explicit in the above, the transformation T can depend on some learnable parameters, for example if T is a neural network. Intuitively, the pushforward distribution is obtained by moving the position of all the points in the support of p. We give a few examples below.

<!-- chunk {"id": "body-0732", "role": "body", "section": "Pushforward distributions", "weight": 1.0} -->

- Inverse transform sampling studied in Section 12.4.3 can be seen as performing the pushforward of the uniform distribution through T = Q, where Q is the quantile function.

<!-- chunk {"id": "body-0733", "role": "body", "section": "Pushforward distributions", "weight": 1.0} -->

- The Gumbel trick studied in Section 14.5 can be seen as a the pushforward of Gumbel noise through T = argmax (a discontinuous function). - Gumbel noise can itself be obtained by pushing forward the uniform distribution through T = -log(-log(·)) (Remark 14.3). - In a generative modeling setting, as we mentioned previously, we use the pushforward of Gaussian noise through a parametrized transformation X = T (Z, w) called a generator, typically a neural network. - It is possible to define distributions over (sparse) probability vectors by sampling then projecting.

<!-- chunk {"id": "body-0734", "role": "body", "section": "Pushforward distributions", "weight": 1.0} -->

A crucial aspect of the pushforward distribution q is that it can be implicitly defined, meaning that we do not necessarily need to know the explicit form of the associated PDF. In fact, it is easy to to sample from q, provided that it is easy to sample from p: Hence the usefulness of the pushforward distribution in generative modeling. Furthermore, if p has associated PDF p Z, we can compute the expectation of a function f according to q as even though we do not know the explicit form of the PDF of q.

<!-- chunk {"id": "body-0735", "role": "body", "section": "Pushforward measures", "weight": 1.0} -->

More generally, we can define the notion of pushforward, in the language of measures. Denote M (Z) the set of measures on a set Z. A measure α ∈ M (Z), that has a density dα (z):= p Z (z) d z, can be integrated against a funtcion f as A measure α is called a probability measure if it is positive and satisfies α (Z) = ∫ Z dα (z) = ∫ Z p Z (z) d z = 1. See Peyré and Cuturi for a concise introduction.

<!-- chunk {"id": "body-0736", "role": "body", "section": "Pushforward measures", "weight": 1.0} -->

Definition 12.2 (Pushforward operator and measure). Given a continuous map T: Z → U and some measure α ∈ M (Z), the pushforward measure β = T ♯ α ∈ M (U) is such that for all continuous functions f ∈ C (U) Equivalently, for any measurable set A ⊂ U, we have Importantly, the pushforward operator preserves positivity and mass, therefore if α is a probability measure, then so is T ♯ α. The pushforward of a probability measure therefore defines a pushforward distribution (since a distribution can be parametrized by a probability measure).

<!-- chunk {"id": "body-0737", "role": "body", "section": "Change-of-variables theorem", "weight": 1.0} -->

We saw that a pushforward distribution associated with a variable U is implicitly defined through a transform U:= T (Z) and can be easily sampled from as long as it is easy to sample Z. However, in some applications (e.g., density estimation), we may want to know the PDF associated with U. Assuming the transform T is invertible, we have Z = T -1 (U) and therefore for A ⊆ U, we have Using the change-of-variables theorem from multivariate calculus, assuming T -1 is available, we can give an explicit formula for the PDF of the pushforward distribution, see e.g..

<!-- chunk {"id": "body-0738", "role": "body", "section": "Change-of-variables theorem", "weight": 1.0} -->

Proposition 12.7 (PDF of the pushforward distribution). Suppose Z ∼ p, where p is a distribution over Z, with PDF p Z. Given a diffeomorphism T: Z → U (i.e., an invertible and differentiable map), the pushforward distribution of p through T is the distribution q such that U:= T (Z) ∼ q and its PDF is where ∂T -1 (u) is the Jacobian of T -1: U → Z.

<!-- chunk {"id": "body-0739", "role": "body", "section": "Change-of-variables theorem", "weight": 1.0} -->

Using this formula, we obtain Using the inverse function theorem (Theorem 11.5), we then have under the assumption that T (z) is continuously differentiable and has invertible Jacobian ∂T (z). Normalizing flows are parametrized transformations T designed such that T -1 and its Jacobian ∂T -1 are easy to compute; see e.g. Kobyzev et al. and Papamakarios et al. for a review.

<!-- chunk {"id": "body-0740", "role": "body", "section": "Stochastic programs", "weight": 1.0} -->

A stochastic program is a program that involves some form of randomness. In a stochastic program, the final output, as well as intermediate variables, may therefore be random variables. In other words, a stochastic program induces a probability distribution over program outputs, as well as over execution trajectories.

<!-- chunk {"id": "body-0741", "role": "body", "section": "Stochastic computation graphs", "weight": 1.0} -->

A stochastic program can be represented by a stochastic computation graph as originally introduced by Schulman et al.. Departing from that work, our exposition explicitly supports two types of intermediate operations: sampling from a conditional distribution or evaluating a function. These operations can produce either deterministic variables or random variables.

<!-- chunk {"id": "body-0742", "role": "body", "section": "Function and distribution nodes", "weight": 1.0} -->

Formally, we define a stochastic computation graph as a directed acyclic graph G = ( V, E ), where V = V f ∪ V p, V f is the set of function nodes and V p is the set of distribution nodes. Similarly to computation graphs reviewed in Section 4.1.3, we number the nodes as V = { 0, 1,..., K }. Node 0 corresponds to the input s 0 ∈ S 0, which we assume to be deterministic. It is the variable with respect to which we wish to differentiate. Node K corresponds to the program output S K ∈ S K, which we assume to be a random variable. A node k ∈ { 1,..., K } can either be a function node k ∈ V f with an associated function f k or a distribution node k ∈ V p, with associated conditional distribution p k. A stochastic program has at least one distribution node, the source of randomness. Otherwise, it is a deterministic program. As for computation graphs, the set of edges E is used to represent dependencies between nodes. We denotes the parents of node k by pa( k ).

<!-- chunk {"id": "body-0743", "role": "body", "section": "Deterministic and random variables", "weight": 1.0} -->

We distinguish between two types of intermediate variables: deterministic variables s k and random variables S k. Therefore, a distribution p k or a function f k may receive both types of variables as conditioning or input. It is then convenient to split pa( k ) as pa( k ) = determ( k ) ∪ random( k ), where we defined the deterministic parents determ( k ):= { i 1,..., i p k } and the random parents random( k ):= { j 1,..., j q k }. Therefore, s i 1,..., s i p k are the deterministic parent variables and S j 1,..., S j q k are the random parent variables, of node k.

<!-- chunk {"id": "body-0744", "role": "body", "section": "Executing a stochastic program", "weight": 1.0} -->

We assume that nodes 0, 1,..., K are in topological order (if this is not the case, we need to perform a topological sort). Given parent variables s i 1,..., s i p k and S j 1,..., S j q k, a node k ∈ { 1,..., K } produces an output as follows.

<!-- chunk {"id": "body-0745", "role": "body", "section": "Executing a stochastic program", "weight": 1.0} -->

- If k ∈ V p (distribution node), the output is Note that technically p k is the distribution of S k conditioned on its parents, not the distribution of S k. Therefore, we should in principle write S k | s determ(k), S random(k) ∼ p k (· | s determ(k), S random(k)). We avoid this notation for conciseness and for symmetry with function nodes.

<!-- chunk {"id": "body-0746", "role": "body", "section": "Executing a stochastic program", "weight": 1.0} -->

Contrary to a function node, a distribution node can have no parents. That is, if k ∈ V p, it is possible that pa( k ) = ∅. A good example would be a parameter-free noise distribution.

<!-- chunk {"id": "body-0747", "role": "body", "section": "Executing a stochastic program", "weight": 1.0} -->

- If k ∈ V f (function node), the output is in general and in the special case q k = | random(k) | = 0, the output is Unless the associated conditional distribution p k is a delta distribution, that puts all the probability mass on a single point, the output of a distribution node k ∈ V p is necessarily a random variable S k ∈ S k. For function nodes k ∈ V f, the output of the function f k is a random variable S k ∈ S k if at least one of the parents of k produces a random variable. Otherwise, if all parents of k produce deterministic variables, the output of f k is a deterministic variable s k ∈ S k.

<!-- chunk {"id": "body-0748", "role": "body", "section": "Executing a stochastic program", "weight": 1.0} -->

The entire procedure is summarized in Algorithm 12.1. We emphasize that S K = f ( s 0 ) ∈ S K is a random variable. Therefore, a stochastic program (implicitly) induces a distribution over S K, and also over intermediate random variables S k. Executing the stochastic program allows us to draw samples from that distribution.

<!-- chunk {"id": "body-0749", "role": "body", "section": "Algorithm 12.1 Executing a stochastic program", "weight": 1.0} -->

Nodes: 1,..., K in topological order, where node k is either a function f k or a conditional distribution p k Input: input s 0 ∈ S 0 1: for k:= 1,..., K do 2: Retrieve pa( k ) = determ( k ) ∪ random( k ) 3: if k ∈ V p then ▷ Distribution node 4: S k ∼ p k ( ·| s determ( k ), S random( k ) ) 5: else if k ∈ V f then ▷ Function node 6: if | random( k ) | = 0 then 7: S k:= f k ( s determ( k ), S random( k ) ) ▷ Output is a R.V. 8: else if | random( k ) | = 0 then 9: s k:= f k ( s determ( k ) ) ▷ Output is deterministic 10: Output: f ( s 0 ):= S K ∈ S K

<!-- chunk {"id": "body-0750", "role": "body", "section": "Special cases", "weight": 1.0} -->

If all nodes are function nodes, we recover computation graphs, reviewed in Section 4.1.3. If all nodes are distribution nodes, we recover Bayesian networks, reviewed in Section 10.5.

<!-- chunk {"id": "body-0751", "role": "body", "section": "Examples", "weight": 1.0} -->

We now present several examples that illustrate our formalism. We use the legend below in the following illustrations.

<!-- chunk {"id": "body-0752", "role": "body", "section": "Examples", "weight": 1.0} -->

- Example 3 (SFE estimator + chain rule): As can be seen, the gradient expressions can quickly become quite complicated, demonstrating the merits of automatic differentiation in stochastic computation graphs.

<!-- chunk {"id": "body-0753", "role": "body", "section": "Unbiased gradient estimators", "weight": 1.0} -->

The output of a stochastic program is a random variable It implicitly defines a probability distribution p (·| s 0) such that S K ∼ p (·| s 0). Executing the stochastic program once gives us an i.i.d. sample from p (·| s 0).

<!-- chunk {"id": "body-0754", "role": "body", "section": "Unbiased gradient estimators", "weight": 1.0} -->

Since derivatives are defined for deterministic variables, we need a way to convert a random variable to a deterministic variable. One way to do so is to consider the expected value (another way would be the mode) where the expectation is over S K ∼ p (·| s 0) or equivalently over the intermediate random variables S k for k ∈ V p (the distribution nodes). We then wish to compute the gradient or more generally the Jacobian of E (s 0).

<!-- chunk {"id": "body-0755", "role": "body", "section": "Unbiased gradient estimators", "weight": 1.0} -->

If all nodes in the stochastic computation graph are function nodes, we can estimate the gradient of E ( s 0 ) using the pathwise estimator a.k.a. reparametrization trick (Section 12.4). This is the approach taken by Kingma and Welling and Rezende et al..

<!-- chunk {"id": "body-0756", "role": "body", "section": "Unbiased gradient estimators", "weight": 1.0} -->

If all nodes in the stochastic computation graph are distribution nodes, we can use the SFE estimator (Section 12.3). Schulman et al. propose a surrogate loss so that using autodiff on that loss produces an unbiased gradient of the expectation, using the SFE estimator. Foerster et al. extend the approach to support high-order differentiation. Krieken et al. further extend the approach by supporting different estimators per node, as well as control variates.

<!-- chunk {"id": "body-0757", "role": "body", "section": "Converting distribution nodes into function nodes and vice-versa", "weight": 1.0} -->

Our formalism uses two types of nodes: distribution nodes with associated conditional distribution p k and function nodes with associated function f k. It is often possible to convert between node types.

<!-- chunk {"id": "body-0758", "role": "body", "section": "Converting distribution nodes into function nodes and vice-versa", "weight": 1.0} -->

Converting a distribution node into a function node is exactly the reparametrization trick studied in Section 12.4. We can use transformations such as the location-scale transform or the inverse transform.

<!-- chunk {"id": "body-0759", "role": "body", "section": "Converting distribution nodes into function nodes and vice-versa", "weight": 1.0} -->

Converting a function node into a distribution node can be done using the change-of-variables theorem, studied in Section 12.4.5, on a pushforward distribution.

<!-- chunk {"id": "body-0760", "role": "body", "section": "Converting distribution nodes into function nodes and vice-versa", "weight": 1.0} -->

Because the pathwise estimator has lower variance than SFE, this is the method of choice when the f k functions are available. The conversion from distribution node to function node and vice-versa is illustrated in Fig. 12.1.

<!-- chunk {"id": "body-0761", "role": "body", "section": "Local vs. global expectations", "weight": 1.0} -->

A stochastic computation graph can be seen as a stochastic process, a collection of random variables S k, indexed by k, the position in the topological order. However, random variables are incompatible with autodiff. Replacing random variables by their expectation can be seen as a way to make them compatible with autodiff. Two strategies are then possible.

<!-- chunk {"id": "body-0762", "role": "body", "section": "Local vs. global expectations", "weight": 1.0} -->

A second strategy is to replace an intermediate random variable S k ∈ S k, for k ∈ { 1,..., K }, by its expectation E [ S k ] ∈ conv( S k ). This strategy corresponds to a local smoothing. A potential drawback of this approach is that E [ S k ] belongs to conv( S k ), the convex hull of S k.

<!-- chunk {"id": "body-0763", "role": "body", "section": "Local vs. global expectations", "weight": 1.0} -->

As we saw in the previous section, a strategy is to consider the expectation of the last output S K. This strategy corresponds to a global smoothing. The two major advantages are that i) we do not need to assume that f k +1 is well-defined on conv( S k ) and ii) this induces a probability distribution over program executions. This is for instance useful to compute the variance of the program. The gradient of the program's expected value can be estimated by the reparametrization trick or by the SFE, depending on the type of nodes used.

<!-- chunk {"id": "body-0764", "role": "body", "section": "Local vs. global expectations", "weight": 1.0} -->

Therefore, the function f k +1 in which E [ S k ] is fed must be well-defined on conv( S k ), which may not always be the case. In the case of control flows, another disadvantage is computational. We saw in Section 5.6 and Section 5.7 that using a soft comparison operator within a conditional statement induces a distribution on a binary or categorical random variable, corresponding to the branch to be selected. A conditional statement can then be locally smoothed out by replacing the random variable by its expectation i.e., a convex combination of all the branches. This means that, unless the distribution has sparse support, all branches must be evaluated.

<!-- chunk {"id": "body-0765", "role": "body", "section": "From residual networks to neural ODEs", "weight": 1.0} -->

Starting from s 0:= x, residual networks, reviewed in Section 4.6, iterate for k ∈ { 1,..., K } A residual network can be seen as parameterizing incremental discretetime input changes (hence the name 'residual') Chen et al. proposed to parameterize continuous-time (instantaneous) changes instead. They considered the evolution s (t) of the inputs in continuous time driven by a function h (t, s, w) parameterized by w, starting from x. Formally, the evolution s (t) is the solution of the ordinary differential equation (ODE) Here, s ′ (t) is the vector of derivatives of s as defined in Remark 2.4, and T denotes a final time for the trajectory. The output of such a neural ODE is then f (x, w):= s (T). Alternatively, the output can be seen as the solution of an integration problem Differential equations like Eq. (12.5) arise in many contexts beyond neural ODEs, ranging from modeling physical systems to pandemics.

<!-- chunk {"id": "body-0766", "role": "body", "section": "From residual networks to neural ODEs", "weight": 1.0} -->

Moreover, the differential equation presented in Eq. (12.5) is just an example of an ordinary differential equation, while controlled differential equations or stochastic differential equations can also be considered.

<!-- chunk {"id": "body-0767", "role": "body", "section": "Existence of a solution", "weight": 1.0} -->

First and foremost, the question is whether s ( t ) is well-defined. Fortunately, the answer is positive under mild conditions, as shown by Picard-Lindelöf's theorem recalled below.

<!-- chunk {"id": "body-0768", "role": "body", "section": "Existence of a solution", "weight": 1.0} -->

Theorem 12.1 (Exsistence and uniqueness of ODE solutions). If h: [0, T] × S → S is continuous in its first variable and Lipschitzcontinuous in its second variable, then there exists a unique differentiable map s: [0, T] →S satisfying for some given s 0 ∈ S.

<!-- chunk {"id": "body-0769", "role": "body", "section": "Existence of a solution", "weight": 1.0} -->

For time-independent linear functions h (t, s) = As, the integral in Eq. (12.6) can be computed in closed form as where exp(A) is the matrix exponential. Hence, the output s (T) can be expressed as a simple function of the parameters (A in this case). However, generally, we do not have access to such analytical solutions, and, just as for solving optimization problems in Chapter 11, we need to resort to some iterative algorithms.

<!-- chunk {"id": "body-0770", "role": "body", "section": "Integration methods", "weight": 1.0} -->

To numerically solve an ODE, we can use integration methods, whose goal is to build a sequence s k that approximates the solution s (t) at times t k. The simplest integration method is the explicit Euler method, that approximates the solutions between times t k -1 and t k as The resulting integration scheme consists in computing starting from s 0 = x, for k ∈ { 1,..., K }, Assimilating δ k h (t k -1, s k -1, w) with h k (s k -1, w k), we find that residual networks are essentially the discretization of a neural ODE by an explicit Euler method; more precisely, a non-autonomous neural ODEs, see e.g..

<!-- chunk {"id": "body-0771", "role": "body", "section": "Integration methods", "weight": 1.0} -->

Given a fixed time interval δ k = δ and K = ⌈ T/δ ⌉ points, an integration method is consistent of order k if ‖ s k -s ( kδ ) ‖ = O ( δ k ) as δ → 0 and therefore k → + ∞. The higher the order k, the fewer points we need to reach an approximation error ε on the points considered. The term ‖ s k -s ( kδ ) ‖ = O ( δ k ) is reminiscent of the error encountered in finite differences (Chapter 7) and is called the truncation error.

<!-- chunk {"id": "body-0772", "role": "body", "section": "Integration methods", "weight": 1.0} -->

Euler's forward method is only one integration method among many. To cite a few, there are implicit Euler methods, semi-implicit methods, Runge-Kutta methods, linear multistep methods, etc. See, e.g., Gautschi for a detailed review. The quality of an integration method is measured by its consistency and its stability. These concepts naturally influence the development of evaluation and differentiation techniques for ODEs. We briefly summarize them below.

<!-- chunk {"id": "body-0773", "role": "body", "section": "Integration methods", "weight": 1.0} -->

The (absolute) stability of a method is defined by the set of timesteps such that the integration method can integrate s ′ ( t ) = λs ( t ) for some λ ∈ C without blowing up as t → + ∞.

<!-- chunk {"id": "body-0774", "role": "body", "section": "Continuous adjoint method", "weight": 1.0} -->

Since different parameters w induce different trajectories associated to h (t, s, w) in Eq. (12.5), we may want to select one of these trajectories by minimizing some criterion. For example, we may consider selecting w ∈ W by minimizing a loss L on the final point of the trajectory, To solve such problems, we need to access gradients of ℓ composed with f through VJPs of the solution of the ODE. The VJPs can actually be characterized as solutions of an ODE themselves thanks to the continuous time adjoint method, presented below, and whose proof is postponed to Section 12.6.6.

<!-- chunk {"id": "body-0775", "role": "body", "section": "Continuous adjoint method", "weight": 1.0} -->

Proposition 12.8 (Continuous-time adjoint method). Consider a function h: [0, T] ×S×W → S, continuous in its first variable, Lipschitzcontinuous and continuously differentiable in its second variable. Assume that ∂ 3 h (t, s, w) exists for any t, s, w, and is also continuous in its first variable, Lipschitz-continuous in its second variable. Denote s: S → S the solution of the ODE and f (x, w) = s (T) the final state of the ODE at time T.

<!-- chunk {"id": "body-0776", "role": "body", "section": "Continuous adjoint method", "weight": 1.0} -->

Then, the function f is differentiable, and for an output direction u ∈ S, its VJP along u is given by for and for r solving the adjoint (backward) ODE In particular, the gradient ∇ (L ◦ f)(x, w) for L: S → R a differentiable loss is obtained by solving the adjoint ODE with r (T) = ∇ L (s (T)).

<!-- chunk {"id": "body-0777", "role": "body", "section": "Continuous adjoint method", "weight": 1.0} -->

Example 12.5 (Fitting data through the solution of an ODE). As an illustrative example, we can consider optimizing the parameters of an ODE to fit some data points. Namely, we may seek a continuous time solution z (t; w) of a modified Lotka Volterra ODE for w = (α, β, γ, δ, c), that fits some observations z 1,..., z T. The optimization problem consists then of and requires backpropagating through the solution z (·; w) of the ODE w.r.t. to its candidate parameters w. Fig. 12.2 illustrates such a problem with varying candidate parameters

<!-- chunk {"id": "body-0778", "role": "body", "section": "Gradients via the continuous adjoint method", "weight": 1.0} -->

Proposition 12.8 gives a formal definition of the gradient. However, just as computing the mapping f ( x, w ) itself, computing its VJP or the gradient of L ◦ f requires solving an integration problem. Note that the integration of r ( t ) in Proposition 12.8 requires also values of s ( t ). Therefore, we need to integrate both r ( t ) and s ( t ). Such an approach is generally referred as optimize-then-discretize because we first formulate the gradient in continuous time (the 'optimize part') and then discretize the resulting ODE.

<!-- chunk {"id": "body-0779", "role": "body", "section": "Simple discretization scheme", "weight": 1.0} -->

A first approach consists in defining a backward discretization scheme that can approximate s (t) backward in time. Namely, by defining σ (t) = s (T -t), ρ (t) = r (T -t), and γ (t) = ∫ T t ∂ 3 h (τ, s (τ), w) ∗ r (τ) dτ, the derivative of L ◦ f is given by (ρ (T), γ (T)). The functions σ, ρ, γ are solutions of a standard ODE The above ODE can then be solved by any integration method. Note, however, that it requires first computing s (T) and ∇ L (s (T)) by an integration method. The overall computation of the gradient using an explicit Euler method to solve forward and backward ODEs is summarized in Algorithm 12.2.

<!-- chunk {"id": "body-0780", "role": "body", "section": "Simple discretization scheme", "weight": 1.0} -->

Algorithm 12.2 naturally looks like the reverse mode of autodiff for a residual neural networks with shared weights. A striking difference Algorithm 12.2 Gradient computation via continuous adjoint method with Euler explicit discretization 1: Functions: h: [0, T] ×S × W → R, L: S → R 2: Inputs: input x, parameters w, number of discretization steps K. 3: Set discretization step δ = T/K, denote h k (s, w) = h (kδ, s, w). 4: Set s 0:= x 5: for k:= 1,..., K do ▷ Forward discretization 6: Compute s k:= s k -1 + δh k -1 (s k -1, w). 7: Compute u:= ∇ L (s K).

<!-- chunk {"id": "body-0781", "role": "body", "section": "Simple discretization scheme", "weight": 1.0} -->

8: Initialize r K:= u, ˆ s K = s K, g K = 0 9: for k:= K,..., 1 do ▷ Backward discretization 10: Compute ˆ s k -1:= ˆ s k -δh k (ˆ s k, w) 11: Compute r k -1:= r k + δ∂ 2 h k (ˆ s k, w) ∗ r k 12: Compute g k -1:= g k + δ∂ 3 h k (ˆ s k, w) ∗ r k 13: Output: (r 0, g 0) ≈ ∇ (L ◦ f)(x, w) is that the intermediate computations s k are not kept in memory and, instead, new variables ˆ s k are computed along the backward ODE. One may believe that by switching to continuous time, we solved the memory issues encountered in reverse-mode autodiff. Unfortunately, this comes at the cost of numerical stability. As we use a discretization scheme to recompute the intermediate states backward in time through ˆ s k in Algorithm 12.2, we accumulate some truncation errors.

<!-- chunk {"id": "body-0782", "role": "body", "section": "Simple discretization scheme", "weight": 1.0} -->

To understand the issue here, consider applying Algorithm 12.2 repeatedly on the same parameters but using ˆ s 0 instead of s 0 = x each time. In the continuous realm, σ ( T ) = s. But after discretization, ˆ s 0 ≈ σ ( T ) does not match s 0. Therefore, by applying Algorithm 12.2 with s 0 = ˆ s 0, we would not get the same output even if in continuous time we naturally should have. This phenomenon is illustrated in Fig. 12.3. It intuitively shows why Algorithm 12.2 induces some noise in the estimation of the gradient.

<!-- chunk {"id": "body-0783", "role": "body", "section": "Multiple shooting scheme", "weight": 1.0} -->

An alternative approach consists in integrating both the forward and backward ODEs jointly. Namely, we may solve an ODE with boundary values by means of a multiple shooting method or a collocation method. This approach still requires ∇ L (s (T)) to be approximated first.

<!-- chunk {"id": "body-0784", "role": "body", "section": "Gradients via reverse-mode on discretization", "weight": 1.0} -->

A simpler approach consists in replacing the objective in Eq. (12.7) by its version discretized using some numerical method, such as an Euler forward discretization scheme. That is, we seek to solve with s 0 = 0 and δ some discretization step. Gradients of the objective can be computed by automatic differentiation. That approach is often referred to as discretize-then-optimize. At first glance, this approach may suffer from very high memory requirements. Indeed, to get an accurate solution of the ODE, a numerical integration method may require K to be very large. Since a naive implementation of reverse-mode automatic differentiation has a memory that scales linearly with K, computing the gradient by a discretize-then-optimize method could be prohibitive. However, the memory requirements may easily be amortized using checkpointing, as explained in Section 8.5; see also.

<!-- chunk {"id": "body-0785", "role": "body", "section": "Gradients via reverse-mode on discretization", "weight": 1.0} -->

As for the optimize-then-discretize method, we still accumulate some truncation errors in the forward discretization process. This discretization error occurs when computing the gradient in reverse-mode too. The discretize-then-optimize method can be seen as computing gradients of a surrogate objective. For that objective, the gradients are correct and well-defined. However, they may not match the gradients of the true ODE formulation.

<!-- chunk {"id": "body-0786", "role": "body", "section": "Gradients via reverse-mode on discretization", "weight": 1.0} -->

To compare the discretize-then-optimize and optimize-then-discretize approaches, Gholaminejad et al. compared their performance on an ODE whose solution can be computed analytically by selecting h to be linear in s. The authors observed that discretize-then-optimize generally outperformed optimize-then-discretize. A middle ground can actually be found by using reversible differentiation schemes.

<!-- chunk {"id": "body-0787", "role": "body", "section": "Reversible discretization schemes", "weight": 1.0} -->

Our exposition of the optimize-then-discretize or discretize-then-optimize approaches used a simple Euler explicit discretization scheme. However, for both approaches, we could have used other discretization schemes instead, such as reversible discretization schemes.

<!-- chunk {"id": "body-0788", "role": "body", "section": "Reversible discretization schemes", "weight": 1.0} -->

A reversible discretization scheme is a discretization scheme such that we have access to a closed-form formula for the inverse of its discretization step. Formally, a discretization method M builds an approximation (s k) K k =1 of the solution of an ODE s ′ (t) = h (t, s (t)) on an interval [0, T] by computing for k ∈ (1,..., K) where δ > 0 is some fixed discretization step, t k is the time step (typically t k = t k -1 + δ), s k is the approximation of s (t k), and c k is some additional context variables used by the discretization method to build the iterates. An explicit Euler method does not have a context, but just as an optimization method may update some internal states, a discretization method can update some context variable. The discretization scheme in Eq. (12.8) is a forward discretization scheme as we took a positive discretization step.

<!-- chunk {"id": "body-0789", "role": "body", "section": "Reversible discretization schemes", "weight": 1.0} -->

By taking a negative discretization step, we obtain the corresponding backward discretization scheme, for k ∈ (K,..., 1), A discretization method is reversible if we have access to M -1 to recompute the inputs of the discretization step from its outputs, A reversible discretization method is symmetric if the backward discretization scheme is exactly the inverse of the forward discretization scheme, i.e., The explicit Euler method is clearly not symmetric and a priori not reversible, unless we can solve for y k -1, the equation y k = y k -1 -δf (y k -1).

<!-- chunk {"id": "body-0790", "role": "body", "section": "Leapfrog method", "weight": 1.0} -->

The (asynchronous) leapfrog method on the other hand is an example of symmetric reversible discretization method. For a constant discretization step δ, given t k -1, s k -1, c k -1 and a function h, it computes One can verify that we indeed have M (t k, s k, c k; h, -δ) = (t k -1, s k, c k).

<!-- chunk {"id": "body-0791", "role": "body", "section": "Leapfrog method", "weight": 1.0} -->

By using a reversible symmetric discretization scheme in the optimizethen-discretize approach, we ensure that, at the end of the backward discretization pass, we recover exactly the original input. Therefore, by repeating forward and backward discretization schemes we always get the same gradient, which was not the case for an Euler explicit scheme.

<!-- chunk {"id": "body-0792", "role": "body", "section": "Leapfrog method", "weight": 1.0} -->

By using a reversible discretization scheme in the discretize-thenoptimize method, we address the memory issues of reverse mode autodiff. As explained in Section 8.6, we can recompute intermediate values during the backward pass rather than storing them.

<!-- chunk {"id": "body-0793", "role": "body", "section": "Momentum residual networks", "weight": 1.0} -->

In the leapfrog method, the additional variables c k may actually be interpreted as velocities of a system whose acceleration is driven by the given function, that is, s ′′ ( t ) = h ( t, s ( t ), w ). Such an interpretation suggests alternatives to the usual neural ODE paradigm. For instance, momentum neural networks, can be interpreted as the discretization of a second-order ordinary differential equations, which are naturally amenable to reversible differentiation schemes with a low memory footprint.

<!-- chunk {"id": "body-0794", "role": "body", "section": "Summary", "weight": 1.0} -->

- We studied how to differentiate integrals, with a focus on expec- - tations and solutions of a differential equation.

<!-- chunk {"id": "body-0795", "role": "body", "section": "Summary", "weight": 1.0} -->

- For differentiating through expectations, we studied two main methods: the score function estimator (SFE, a.k.a. REINFORCE) and the path gradient estimator (PGE, a.k.a. reparametrization trick). - The SFE is suitable when it is easy to sample from the distribution and its log-PDF is explicitly available. It is an unbiased estimator, but is known to suffer from high variance. - The PGE is suitable for pushforward distributions, distributions that are implicitly defined through a transformation, or a sequence of them. These distributions can be easily sampled, by injecting a source of randomness (such as noise) through the transformations. An unbiased, low-variance estimator of the gradient of their expectation is easily obtained, provided that we can interchange integration and differentiation. - If we have an explicit distribution, we can sometimes convert it to an implicit distribution, thanks to the location-scale transformation or the inverse transformation. - Conversely, if we have an implicit distribution, we can convert it to an explicit distribution using the change-of-variables theorem.

<!-- chunk {"id": "body-0796", "role": "body", "section": "Summary", "weight": 1.0} -->

However, this formula requires to compute the determinant of an inverse Jacobian, and is computationally expensive in general. Normalizing flows use invertible transformations so that the inverse Jacobian is cheap to compute, by design. - Stochastic computation graphs can use a mix of explicit and implicit distributions at each node. - For differentiating through the solution of a differential equation, two approaches can be considered. - We can express the gradient as the solution of a differential equation thanks to the continuous adjoint method. We may then discretize backwards in time the differential equation that the gradient satisfies. This is the optimize-then-discretize approach.

<!-- chunk {"id": "body-0797", "role": "body", "section": "Summary", "weight": 1.0} -->

- We can also first discretize the problem in such a way that the gradient can simply be computed by reverse mode auto-diff, applied on the discretization steps. This is the discretize-thenoptimize approach. The optimize-then-discretize approach has no memory cost, but discrepancies between the forward and backward discretization passes often lead to numerical errors. The discretize-then-optimize introduces no such discrepancies but may come at a large memory cost. - Reversible discretization schemes can circumvent the memory cost, as they enable the recomputation of intermediate discretization steps backwards in time.

<!-- chunk {"id": "body-0798", "role": "body", "section": "Smoothing by optimization", "weight": 1.0} -->

When a function is non-differentiable (or worse, discontinuous), a reasonable approach is to replace it by a differentiable approximation (or at least, by a continuous relaxation). We refer to the process of transforming a non-differentiable function into a differentiable one as 'smoothing' the original function. In this chapter, we begin by reviewing a smoothing technique based on infimal convolution. We then review an equivalent dual approach, based on the Legendre-Fenchel transform. We illustrate how to apply these techniques to compute smoothed ReLUs and smoothed max operators, as well as continuous relaxations of step functions and argmax operators.

<!-- chunk {"id": "body-0799", "role": "body", "section": "Primal approach", "weight": 1.0} -->

We first review how to smooth functions in the original, primal space of the function, using the infimal convolution and more particularly the Moreau envelope, a.k.a. Moreau-Yoshida regularization. In this chapter, we consider functions taking potentially infinite positive values, that is, functions taking values in the half-extended real line R ∪ {∞}. For a function f: R M → R ∪ ∞, we define its domain as

<!-- chunk {"id": "body-0800", "role": "body", "section": "Infimal convolution", "weight": 1.0} -->

Sometimes abbreviated inf-conv, the infimal convolution between two functions f and g creates a new function f □ g. It is defined as follows.

<!-- chunk {"id": "body-0801", "role": "body", "section": "Infimal convolution", "weight": 1.0} -->

Definition 13.1 (Infimal convolution). The infimal convolution between two functions f: R M → R ∪ {∞} and g: R M → R ∪ {∞} is defined by It is easy to check that the three definitions are indeed equivalent, by using the change of variable u:= µ + z, which is a location-scale transform; see Section 12.4.1.

<!-- chunk {"id": "body-0802", "role": "body", "section": "Infimal convolution", "weight": 1.0} -->

The infimal convolution can be seen as a counterpart of the usual convolution, in which integration has been replaced by minimization (hence its name). Similarly to the classical convolution, it is commutative, meaning that for all µ ∈ R M, we have Computing the infimal convolution involves the resolution of a minimization problem, that may or may not enjoy an analytical solution. Some examples are given in Table 13.1.

<!-- chunk {"id": "body-0803", "role": "body", "section": "Existence", "weight": 1.0} -->

The infimal convolution ( f □ g )( µ ) exists if the infimum inf u ∈ R M f ( u ) + g ( µ -u ) is finite. A sufficient condition to achieve this is that u ↦→ f ( u ) + g ( µ -u ) is convex for all µ ∈ R M. However, this is not a necessary condition. For example, the infimum can be finite even if f or g are nonconvex, for example if their domain is a compact set.

<!-- chunk {"id": "body-0804", "role": "body", "section": "Existence", "weight": 1.0} -->

Table 13.1: Examples of infimal convolutions. We use ι C to denote the indicator function of the set C.

<!-- chunk {"id": "body-0805", "role": "body", "section": "Infimal convolution with a regularization function", "weight": 1.0} -->

When a function f is non-differentiable, a commonly-used technique is to replace it by its infimal convolution f □ R, with some regularization R. The most used regularization is the squared 2-norm, leading to the Moreau envelope, as we now review.

<!-- chunk {"id": "body-0806", "role": "body", "section": "Moreau envelope", "weight": 1.0} -->

When R ( z ):= 1 2 ‖ z ‖ 2 2, the infimal convolution f □ R gives the so-called Moreau envelope of f, which is also known as Moreau-Yoshida regularization of f.

<!-- chunk {"id": "body-0807", "role": "body", "section": "Moreau envelope", "weight": 1.0} -->

Definition 13.2 (Moreau envelope). Given a function f: R M → R ∪ {∞}, its Moreau envelope is defined as Intuitively, the Moreau envelope is the minimal value over u ∈ R M of a trade-off between staying close to the input µ according to the proximity term 1 2 ‖ µ -u ‖ 2 2 and minimizing f (u). Provided that the minimizer exists and is unique, we can define the associated proximal operator of f as In other words, we have for prox f (µ) well defined,

<!-- chunk {"id": "body-0808", "role": "body", "section": "Properties", "weight": 1.0} -->

A crucial property of the Moreau envelope env f is that for any convex function f, it is always a smooth function, even when f itself is not smooth. By smooth, we formally mean that the resulting function env f is differentiable everywhere with Lipschitz-continuous gradients. We say L -smooth, if the gradients are L -Lipshcitz continuous. Such a property can determine the efficiency of optimization algorithms as reviewed in Section 15.4. We recap below useful properties of the Moreau envelope.

<!-- chunk {"id": "body-0809", "role": "body", "section": "Properties", "weight": 1.0} -->

Proposition 13.1 (Properties of Moreau envelope). Let f: R M → R ∪ {∞}. 1. Smoothness: If f is convex, the function env f is 1-smooth. 2. Gradient: Provided that prox f (µ) is well-defined on µ ∈ R M, the gradient of the Moreau envelope can be expressed in terms of the proximal operator as 3. Moreau decomposition: If f is convex, then for any µ ∈ R M, we have the following identity

<!-- chunk {"id": "body-0810", "role": "body", "section": "Examples", "weight": 1.0} -->

To illustrate smoothing from the Moreau envelope perspective, we show how to smooth the 1-norm. In this case, we obtain an analytical expression for the Moreau envelope. where f ∗ is the convex conjugate of f, detailed in Section 13.2. In particular, we get 4. Convexity: env f is convex if f is convex. 5. Infimums coincide env f has the same infimum as the original function f: Figure 13.1: The Huber loss is the Moreau envelope of the absolute loss.

<!-- chunk {"id": "body-0811", "role": "body", "section": "Examples", "weight": 1.0} -->

Example 13.1 (Smoothing the 1 -norm via infimal convolution). We wish to smooth f (u):= ‖ u ‖ 1 = ∑ j M =1 | u j |. The corresponding proximal operator is the soft-thresholding operator (see Section 16.4), Using Eq. (13.1) and after some algebraic manipulations, we obtain where we defined the Huber loss This is illustrated in Fig. 13.1 with M = 1.

<!-- chunk {"id": "body-0812", "role": "body", "section": "Examples", "weight": 1.0} -->

We also illustrate in Fig. 13.2 that the Moreau envelope of nonconvex functions can be approximately computed numerically.

<!-- chunk {"id": "body-0813", "role": "body", "section": "Vector-valued functions", "weight": 1.0} -->

The Moreau envelope is defined by env f (µ):= inf u ∈ R M f (u)+ 1 2 ‖ µ -u ‖ 2 2. As such, it is limited to scalar-valued functions f: R M → R. To extend the Moreau envelope to vector-valued functions f: R M → R T, where f (u) = (f 1 (u),..., f T (u)) and f i: R M → R for i ∈ [T], we may choose to smooth each f j separately to define This approach requires to solve T separate minimization problems and performs the smoothing of each output coordinate i ∈ [T] independently. From Proposition 2.9, we then have that the VJP of env f (u) with any direction d ∈ R T is In the particular case f (u) = (f 1 (u 1),..., f T (u T)), we obtain An alternative was proposed by Roulet and Harchaoui.

<!-- chunk {"id": "body-0814", "role": "body", "section": "Vector-valued functions", "weight": 1.0} -->

For a differentiable function f: R M → R T, we recall that the VJP of f with a direction d ∈ R T reads where we defined the scalar-valued function 〈 f, d 〉 (u):= 〈 f (u), d 〉. As a result, if f is non differentiable, a natural idea is to approximate its VJP ∂f (u) ∗ [d] (had it existed) by the gradient ∇ env 〈 f, d 〉 (µ) of the Moreau envelope This requires a single optimization problem to solve, independently of the number of outputs T. Moreover, for d = e i, this recovers env f i (µ) as a special case.

<!-- chunk {"id": "body-0815", "role": "body", "section": "Vector-valued functions", "weight": 1.0} -->

This approach allows in principle to perform reverse-mode autodiff (gradient backpropagation) on a neural network whose layers use the Moreau envelope. Indeed, following Proposition 13.1, the approximate VJP of f with a direction d is given by where u ⋆ is the solution of the minimization problem in Eq. (13.2). However, we emphasize that this minimization problem could be difficult to solve in general. Indeed, when performing gradient backpropagation, the direction d is not necessarily non-negative, therefore the function being minimized in Eq. (13.2) could be nonconvex, even if each f i is convex. Another potential caveat is that the direction d influences the smoothing strength, while in principle we should be able to smooth a function independently of whether we compute its VJP or not.

<!-- chunk {"id": "body-0816", "role": "body", "section": "Vector-valued functions", "weight": 1.0} -->

To see that, for example in the particular case f (u) = (f 1 (u 1),..., f T (u T)), one easily checks that for d = (d 1,..., d T), we get Smoothing vector-valued functions by Moreau envelope (or more generally, by infimal convolution) remains an open area of research. We will see in Chapter 14 that smoothing by convolution more naturally supports vector-valued functions.

<!-- chunk {"id": "body-0817", "role": "body", "section": "Legendre-Fenchel transforms, convex conjugates", "weight": 1.0} -->

The Legendre-Fenchel transform, a.k.a. convex conjugate, is a way to turn a function f into a new function, denoted f ∗. We now review it in detail, as it plays a major role for the dual approach to smoothing.

<!-- chunk {"id": "body-0818", "role": "body", "section": "Closed-form examples", "weight": 1.0} -->

Computing f ∗ ( v ) involves the resolution of a maximization problem, which could be difficult in general without assumption on f. In some cases, however, we can compute an analytical expression, as we now illustrate.

<!-- chunk {"id": "body-0819", "role": "body", "section": "Closed-form examples", "weight": 1.0} -->

Example 13.2 (Analytical conjugate examples). When f (u) = 1 2 ‖ u ‖ 2 2, with dom(f) = R M, the conjugate is Figure 13.4: Left: instead of representing a convex function f by its graph (u, f (u)) for u ∈ dom(f), we can represent it by the set of tangents with slope v and intercept -f ∗ (v) for v ∈ dom(f ∗). Right: by varying the slope v of all possible tangents, we obtain a function of the slope v rather than of the original input u. The colors of the tangents on the left are chosen to match the colors of the vertical lines on the right.

<!-- chunk {"id": "body-0820", "role": "body", "section": "Closed-form examples", "weight": 1.0} -->

Setting the gradient u ↦→〈 u, v 〉 -1 2 ‖ u ‖ 2 2 to zero, we obtain u ⋆ = v. Plugging u ⋆ back, we therefore obtain Therefore, f = f ∗ in this case.

<!-- chunk {"id": "body-0821", "role": "body", "section": "Closed-form examples", "weight": 1.0} -->

When f (u) = 〈 u, log u 〉, with dom(f) = R M +, the minimizer of u ↦→〈 u, v 〉 - 〈 u, log u 〉 is u ⋆ = exp(v -1) and the conjugate is See for instance Boyd and Vandenberghe or Beck for many more examples.

<!-- chunk {"id": "body-0822", "role": "body", "section": "Constraining the domain", "weight": 1.0} -->

We can incorporate constraints using an indicator function with values in the extended real line R ∪ {∞}, Example 13.3 (Incorporating constraints). If f (u) = ι C (u), where C is a convex set, then which is known as the support function of C. The corresponding argmax (assuming that it exists), is known as the linear maximization oracle (LMO) of C. As another example, if f (u) = 〈 u, log u 〉 + ι △ M (u) then We postpone a proof to Proposition 13.9.

<!-- chunk {"id": "body-0823", "role": "body", "section": "Properties", "weight": 1.0} -->

The conjugate enjoys several useful properties, that we now summarize.

<!-- chunk {"id": "body-0824", "role": "body", "section": "Properties", "weight": 1.0} -->

Proposition 13.2 (Convex conjugate properties). 1. Convexity: f ∗ (v) is a convex function for all f: R M → R ∪ {∞} (even if f is nonconvex). 2. Fenchel-Young inequality: for all u, v ∈ R M 3. Gradient: if the supremum in Definition 13.3 is uniquely achieved, then f ∗ (v) is differentiable at v and its gradient is Otherwise, f ∗ (v) is sub-differentiable at v and we get a subgradient instead. 4. Maps: If f and f ∗ are differentiable, then 5. Biconjugate: f = f ∗∗ if and only if f is convex and closed (i.e., its sublevel sets form a closed set), otherwise f ∗∗ ≤ f.

<!-- chunk {"id": "body-0825", "role": "body", "section": "Conjugate calculus", "weight": 1.0} -->

While deriving a convex conjugate expression can be difficult in general, in some cases, it is possible to use simple rules to derive conjugates in terms of other conjugates.

<!-- chunk {"id": "body-0826", "role": "body", "section": "Fast Legendre transform", "weight": 1.0} -->

When an analytical expression is not available, we can resort to numerical schemes to approximately compute the transform / conjugate. When f is convex, because -f is concave, the maximization in Definition 13.3 is that of a concave function. Therefore, the conjugate can be computed to arbitrary precision in polynomial time using classical iterative algo- rithms for constrained optimization such as projected gradient descent (Section 16.3) or conditional gradient a.k.a. Frank-Wolfe. Without convexity assumption on f, f ∗ (v) can be approximated by where U ⊆ dom(f) is a discrete grid of values. We can then compute f ∗ (v) for several inputs v ∈ V using the linear-time Legendre transform algorithm, where V ⊆ dom(f ∗) is another discrete grid. The complexity is O (|U| · |V|), which is linear in the grid sizes. However, the grid sizes are typically |U| = |V| = O (N M), for N equally-distributed points in each of the M dimensions.

<!-- chunk {"id": "body-0827", "role": "body", "section": "Fast Legendre transform", "weight": 1.0} -->

Therefore, this approach is limited to small-dimensional settings, e.g., M ∈ { 1, 2, 3 }.

<!-- chunk {"id": "body-0828", "role": "body", "section": "Dual approach", "weight": 1.0} -->

Previously, we presented how to smooth a function by performing its infimal convolution with a primal-space regularization R. We now present how to smooth a function by regularizing its Legendre-Fenchel transform (convex conjugate) instead. This dual, equivalent approach, is often mathematically more convenient.

<!-- chunk {"id": "body-0829", "role": "body", "section": "Duality between strong convexity and smoothness", "weight": 1.0} -->

We begin by stating a well-known result that will underpin this whole section: smoothness and strong convexity are dual to each other.

<!-- chunk {"id": "body-0830", "role": "body", "section": "Duality between strong convexity and smoothness", "weight": 1.0} -->

Proposition 13.4 (Duality between strong convexity and smoothness). f is 1 µ -strongly convex w.r.t. the norm ‖ · ‖ over dom( f ) if and only if f ∗ is µ -smooth w.r.t. the dual norm ‖ · ‖ ∗ over dom( f ∗ ).

<!-- chunk {"id": "body-0831", "role": "body", "section": "Duality between strong convexity and smoothness", "weight": 1.0} -->

For a review of the notions of smoothness and strong convexity, see Section 15.4. We give two examples of strongly-convex and smooth conjugate pairs in Table 13.2.

<!-- chunk {"id": "body-0832", "role": "body", "section": "Duality between strong convexity and smoothness", "weight": 1.0} -->

Table 13.2: Examples of strongly-convex and smooth conjugate pairs.

<!-- chunk {"id": "body-0833", "role": "body", "section": "Duality between strong convexity and smoothness", "weight": 1.0} -->

| Function | Norm | Domain | Conjugate | Dual norm | Dual domain |

<!-- chunk {"id": "body-0834", "role": "body", "section": "Smoothing by dual regularization", "weight": 1.0} -->

The duality between smoothness and strong convexity suggests a generic approach in order to smooth a function f: R M → R, by going through the dual space. 1. Compute the conjugate f ∗: 2. Add strongly-convex regularization Ω to the conjugate: 3. Go back to the primal space, by computing the conjugate of f ∗ Ω: Note that u and v belong to different spaces, i.e., u ∈ dom(f) and v ∈ dom(f ∗). Following Proposition 13.4, if Ω is µ -strongly convex, then f Ω (u) is 1 µ -smooth. Furthermore, following Proposition 13.2, f Ω (u) is convex, even if f is nonconvex. Therefore, f Ω (u) is a smooth and convex relaxation of f (u).

<!-- chunk {"id": "body-0835", "role": "body", "section": "Smoothing by dual regularization", "weight": 1.0} -->

Steps 1 and 3 are the most challenging, as they both require the derivation of a conjugate. While an analytical solution may not exist in general, in some simple cases, there is, as we now illustrate.

<!-- chunk {"id": "body-0836", "role": "body", "section": "Smoothing by dual regularization", "weight": 1.0} -->

Example 13.4 (Smoothing the 1 -norm via dual regularization). Werevisit Example 13.1, this time from the dual perspective. We wish to smooth out the 1-norm f (u):= ‖ u ‖ 1 = ∑ j M =1 | u j |. 1. Compute the conjugate. The conjugate of any norm ‖ · ‖ is the indicator function of the dual norm's unit ball { v ∈ R M: ‖ v ‖ ∗ ≤ 1 } (see e.g. Boyd and Vandenberghe). The dual norm of ‖ u ‖ 1 is ‖ v ‖ ∞. Moreover, Recalling that ι C is the indicator function of C, we obtain 2. Adding strongly-convex regularization. Weadd quadratic regularization Ω(v):= 1 2 ‖ v ‖ 2 2 to define 3. Going back to the primal.

<!-- chunk {"id": "body-0837", "role": "body", "section": "Smoothing by dual regularization", "weight": 1.0} -->

We therefore indeed recover the Huber loss from Example 13.1.

<!-- chunk {"id": "body-0838", "role": "body", "section": "Smoothing by dual regularization", "weight": 1.0} -->

ReLU functions can be smoothed out in a similar way, as we see in more details in Section 13.4.

<!-- chunk {"id": "body-0839", "role": "body", "section": "Smoothing by dual regularization", "weight": 1.0} -->

The dual approach allows us to easily bound the smoothed function in terms of the original function.

<!-- chunk {"id": "body-0840", "role": "body", "section": "Smoothing by dual regularization", "weight": 1.0} -->

Proposition 13.5 (Bounds). If L Ω ≤ Ω(v) ≤ U Ω for all v ∈ dom(Ω), then for all u ∈ R M, Proof. Let us define where we recall that f ∗ Ω:= f ∗ +Ω. We then have for all u ∈ R M Combining the two with L Ω ≤ Ω(v) ≤ U Ω for all v ∈ dom(Ω), we obtain Remark 13.1 (The gradient is differentiable almost everywhere). From Proposition 13.2, the gradient of f Ω (u) equals If Ω is strongly convex, then f Ω is smooth, meaning that ∇ f Ω is Lipschitz continuous. From Rademacher's theorem reviewed in Section 2.7.1, ∇ f Ω is then differentiable almost everywhere (that is, f Ω is twice differentiable almost everywhere). We use this property in the sequel to define continuous differentiable almost everywhere relaxations of step functions and argmax operators.

<!-- chunk {"id": "body-0841", "role": "body", "section": "Equivalence between primal and dual regularizations", "weight": 1.0} -->

So far, we saw two approches to obtain a smooth approximation of a function f. The first approach is based on the infimal convolution f □ R, where R: dom( f ) → R denotes primal regularization. The second approach is based on regularizing the Legendre-Fenchel transform (convex conjugate) f ∗ of f with some dual regularization Ω, to define f Ω = ( f ∗ +Ω) ∗. It turns out that both approaches are equivalent.

<!-- chunk {"id": "body-0842", "role": "body", "section": "Equivalence between primal and dual regularizations", "weight": 1.0} -->

Proposition 13.6 (Equivalence between primal and dual regularizations). Let f: R M → R ∪ {∞} and R: R M → R ∪ {∞}, both convex and closed. Then, f Ω = ( f ∗ +Ω) ∗ = f □ R with Ω = R ∗.

<!-- chunk {"id": "body-0843", "role": "body", "section": "Equivalence between primal and dual regularizations", "weight": 1.0} -->

If h 1 and h 2 are convex, we have ( h 1 + h 2 ) ∗ = h ∗ 1 □ h ∗ 2. Using h 1 = f ∗ and h 2 = Ω = R ∗ gives the desired result using that f ∗∗ = f and R ∗∗ = R since both are convex and closed (see Proposition 13.2).

<!-- chunk {"id": "body-0844", "role": "body", "section": "Equivalence between primal and dual regularizations", "weight": 1.0} -->

In particular, with Ω = 1 2 ‖ · ‖ 2 2 = Ω ∗, this shows that the Moreau envelope can equivalently be written as Given the equivalence between the primal and dual approaches, using one approach or the other is mainly a matter of mathematical or algorithmic convenience, depending on the case.

<!-- chunk {"id": "body-0845", "role": "body", "section": "Equivalence between primal and dual regularizations", "weight": 1.0} -->

In this book, we focus on applications of smoothing techniques to differentiable programming. For applications to non-smooth optimization, see Nesterov and Beck and Teboulle.

<!-- chunk {"id": "body-0846", "role": "body", "section": "Dual approach", "weight": 1.0} -->

If Ω is 1-strongly convex, then f Ω is a 1-smooth approximation of the original function f. To control the smoothness of the approximation, it suffices to regularize with ε Ω for ε > 0, leading to a 1 /ε -smooth approximation f ε Ω of f. Moreover, one can check that Therefore, if we know how to compute f Ω, we can also compute f ε Ω and its gradient easily. Furthermore, the approximation error induced by the smoothing can be quantified using Proposition 13.5 as we then have provided that L Ω ≤ Ω(v) ≤ U Ω for all v ∈ dom(Ω).

<!-- chunk {"id": "body-0847", "role": "body", "section": "Primal approach", "weight": 1.0} -->

Following Definition 13.2, if we use dual regularization ε Ω, where ε > 0 controls the regularization strength, the corresponding primal regularization is R = ε Ω ∗ (· /ε). That is, we have In the particular case Ω(v) = 1 2 ‖ v ‖ 2 2, we have

<!-- chunk {"id": "body-0848", "role": "body", "section": "Generalized entropies", "weight": 1.0} -->

A natural choice of dual regularization Ω( π ), when π ∈ △ M is a discrete probability distribution, is a negative entropy function, also known as negentropy. Since negentropies play a major role in smoothed max operators, we discuss them in detail here.

<!-- chunk {"id": "body-0849", "role": "body", "section": "Information content and entropy", "weight": 1.0} -->

An entropy function measures the amount of 'suprise' of a random variable or equivalently of a distribution. To define an entropy, we must first define the information content I (E) of an event E. The value returned by such a function should be 0 if the probability of the event is 1, as there is no surprise. Conversely, information content should attain its maximal value if the probability of the event is 0, as it is maximally surprising. Furthermore, the more probable an event E is, the less surprising it is. Therefore, when p (E) increases, I (E) should decrease. Overloading the notation, we also write the information content of the outcome y of a random variable Y as the information content of the event { Y = y }, Given an information content function, we can then define the entropy H (Y) of a random variable Y ∈ Y as the expected information content, Different definitions of information content lead to different definitions of entropy.

<!-- chunk {"id": "body-0850", "role": "body", "section": "Shannon's entropy", "weight": 1.0} -->

A definition of information content satisfying the criteria above is Indeed, -log 1 = 0, -log 0 = ∞ and -log is a decreasing function over (0, 1]. Using this information content definition leads to Shannon's entropy We can therefore define the Shannon entropy of a discrete probability distribution π ∈ △ M as and use the corresponding negentropy as regularization The function is strongly convex w.r.t. ‖ · ‖ 1 over △ M. However, it is not strongly convex over R M +, since this is not a bounded set; see for instance. Since Ω is added to f ∗ in Eq. (13.3), we can therefore use this choice of Ω to smooth out a function f if dom(f ∗) ⊆ △ M.

<!-- chunk {"id": "body-0851", "role": "body", "section": "Gini's entropy", "weight": 1.0} -->

As an alternative, we can define information content as Figure 13.5: Tsallis entropies of the distribution π = (π, 1 -π) ∈ △ 2, for π ∈. An entropy is a non-negative concave function that attains its maximum at the uniform distribution, here (0. 5, 0. 5). A negative entropy, a.k.a. negentropy, can be used as a dual regularization function Ω to smooth out a function f when dom(f ∗) ⊆ △ M.

<!-- chunk {"id": "body-0852", "role": "body", "section": "Gini's entropy", "weight": 1.0} -->

The 1 2 factor is for later mathematical convenience. This again satisfies the criteria of an information content function. Indeed, i) when p (E) = 1, I (E) = 0 ii) when p (E) = 0, I (E) attains its maximum of 1 2 iii) the function is decreasing w.r.t. p (E). Using this information content definition leads to Gini's entropy a.k.a. Gini index We can use Gini's negative entropy to define for all π ∈ △ M The function is strongly convex w.r.t. ‖ · ‖ 2 over R M. We can therefore use this choice of Ω to smooth out a function f if dom(f ∗) ⊆ R M. This means that the set of functions that we can smooth out with Gini entropy is larger than the set of functions we can smooth out with Shannon entropy.

<!-- chunk {"id": "body-0853", "role": "body", "section": "Tsallis entropies", "weight": 1.0} -->

Given α ≥ 1, a more general information content definition is Figure 13.6: Contours of Tsallis entropies on the probability simplex.

<!-- chunk {"id": "body-0854", "role": "body", "section": "Tsallis entropies", "weight": 1.0} -->

Using this definition leads to the Tsallis entropy The Tsallis entropy recovers the Shannon entropy in the limit α → 1 and the Gini entropy when α = 2. We can use the Tsallis negative entropy to define for all π ∈ △ M where ‖ v ‖ p is the p -norm for (p ≥ 1) Tsallis entropies for α → 1 (Shannon entropy), α = 1. 5 and α = 2 (Gini entropy) are illustrated in Fig. 13.5 and Fig. 13.6.

<!-- chunk {"id": "body-0855", "role": "body", "section": "Smoothed ReLU functions", "weight": 1.0} -->

To demonstrate the application of the smoothing techniques discussed in this chapter, we begin by explaining how to smooth the ReLU function. The ReLU function is defined by We recall that in order to smooth a function f by the dual approach, we calculate its conjugate f ∗, add regularization Ω to it to obtain f ∗ Ω:= f ∗ +Ω and then obtain f Ω by computing f ∗∗ Ω.

<!-- chunk {"id": "body-0856", "role": "body", "section": "Smoothed ReLU functions", "weight": 1.0} -->

Here, we wish to smooth out f = relu. Its convex conjugate is To notice why, we observe that Indeed, since the objective is linear in π, the maximum is attained at one of the extreme points of, so that we can replace the constraint π ∈ with π ∈ { 0, 1 }. This shows that the ReLU is exactly the support function of. Since the conjugate of the support function is the indicator function, we indeed obtain relu ∗ = ι. We therefore have and for some choice of Ω, we need to be able to compute

<!-- chunk {"id": "body-0857", "role": "body", "section": "The softplus", "weight": 1.0} -->

If we use the regularizer Ω(π) = π log π + (1 -π) log(1 -π), which comes from using Shannon's negentropy 〈 π, log π 〉 with π = (π, 1 -π), we obtain This result is a special case of Proposition 13.9.

<!-- chunk {"id": "body-0858", "role": "body", "section": "The sparseplus", "weight": 1.0} -->

If we use the regularizer Ω(π) = π (π -1), which comes from using Gini's negentropy with 1 2 〈 π, π -1 〉 with π = (π, 1 -π), we obtain See Fig. 13.8 (left figure) for a comparison of softplus and sparseplus.

<!-- chunk {"id": "body-0859", "role": "body", "section": "Smoothed max operators", "weight": 1.0} -->

As a more elaborate application of the smoothing techniques discussed in this chapter, we explain how to smooth max operators. Smoothed max operators include smoothed ReLU functions as a special case.

<!-- chunk {"id": "body-0860", "role": "body", "section": "Smoothed min operators", "weight": 1.0} -->

The minimum operator can be expressed in terms of the maximum operator, since for all u ∈ R M, Given a smoothed max operator max Ω, we can therefore easily define a smoothed min operator as

<!-- chunk {"id": "body-0861", "role": "body", "section": "Reduction to root finding", "weight": 1.0} -->

Computing max Ω (u) for a general strongly-convex regularization Ω involves the resolution of a maximum over probability simplex constraints. For convenience, let us define the notation The following proposition shows that we can reduce computing max Ω to solving a root equation involving δ Ω.

<!-- chunk {"id": "body-0862", "role": "body", "section": "Reduction to root finding", "weight": 1.0} -->

Proposition 13.8 (Computing max Ω as root finding). Suppose Ω is strongly convex. For all u ∈ R M, where τ ⋆ is the solution w.r.t. τ of the above min, which satisfies the root equation Proof. The idea is to keep the non-negativity constraint explicit, but to use a Lagrange multiplier for the equality constraint of the probability simplex. We then have where we used that we can swap the min and the max, since (u, v) ↦→ 〈 u, v 〉-Ω(v) is convex-concave and v ∈ △ M is an affine constraint. The gradient ∇ δ Ω (u) follows from Danskin's theorem. The root equation follows from computing the derivative of τ ↦→ τ + δ Ω (u -τ 1) and setting it to zero.

<!-- chunk {"id": "body-0863", "role": "body", "section": "The softmax", "weight": 1.0} -->

When Ω is Shannon's negentropy, we obtain that max Ω is the softmax, already briefly discussed in Section 4.4.2.

<!-- chunk {"id": "body-0864", "role": "body", "section": "The softmax", "weight": 1.0} -->

Proposition 13.9 (Analytical expression of the softmax). When Ω(π) = 〈 π, log π 〉, we get Proof. Since dom(Ω) = R M +, we have δ Ω = Ω ∗ (i.e., the non-negativity constraint is redundant). From Example 13.2, we therefore have δ Ω (u) = ∑ j M =1 exp(u j -1). From Proposition 13.8, max Ω (u) = τ ⋆ + δ Ω (u -τ ⋆ 1) where τ ⋆ satisfies 〈∇ δ Ω (u -τ ⋆ 1), 1 〉 = 1. Since ∇ δ Ω (u) = exp(u -1), we need to solve ∑ j M =1 exp(u j -1 -τ) = 1. We therefore get τ ⋆ + 1 = logsumexp(u) and therefore max Ω (u) = logsumexp(u) -1 + ∑ j M =1 exp(u j -logsumexp(u)) = logsumexp(u).

<!-- chunk {"id": "body-0865", "role": "body", "section": "The softmax", "weight": 1.0} -->

Since -log M ≤ Ω(π) ≤ 0 for all π ∈ △ M, following Proposition 13.7, we get for all u ∈ R M A unique property of the softmax, which is not the case of all max Ω operators, is that it supports associativity.

<!-- chunk {"id": "body-0866", "role": "body", "section": "The softmax", "weight": 1.0} -->

Proposition 13.10 (Associativity of the softmax). For all a, b, c ∈ R, softmax(softmax(a, b), c) = softmax(a, softmax(b, c)).

<!-- chunk {"id": "body-0867", "role": "body", "section": "The sparsemax", "weight": 1.0} -->

Alternatively, choosing Ω to be Gini's negentropy leads to the sparsemax.

<!-- chunk {"id": "body-0868", "role": "body", "section": "The sparsemax", "weight": 1.0} -->

Proposition 13.11 (Variational formulation of sparsemax). When Ω(π) = 1 2 〈 π, π -1 〉, we have Proof. This follows from the fact that Ω(π) is up to a constant equal to 1 2 ‖ π ‖ 2 2 and completing the square.

<!-- chunk {"id": "body-0869", "role": "body", "section": "The sparsemax", "weight": 1.0} -->

Therefore, computing the sparsemax can use the sparseargmax (the Euclidean projection onto the probability simplex) as a building block. We discuss how to compute it in more detail in Section 13.7. Applying Proposition 13.8 gives an alternative formulation.

<!-- chunk {"id": "body-0870", "role": "body", "section": "The sparsemax", "weight": 1.0} -->

Proposition 13.12 (Sparsemax as root finding). When Ω(π) = 1 2 〈 π, π -1 〉, we have Proof. First, we compute the expression of δ Ω (u) = max v ∈ R M + 〈 u, v 〉 -Ω(v). Setting the gradient of v ↦→ 〈 u, v 〉 -Ω(v) and clipping, we obtain v ⋆ = [u] +. Plugging v ⋆ back, we obtain δ Ω (u) = 1 2 ∑ i M =1 [u i] 2 +. Using Proposition 13.8 proves the proposition's first part. Setting the derivative w.r.t. τ to zero gives the second part.

<!-- chunk {"id": "body-0871", "role": "body", "section": "The sparsemax", "weight": 1.0} -->

It can be shown that the exact solution τ ⋆ is obtained by where j ⋆ is the largest j ∈ [M] such that and where we used the notation u ≥ u ≥ ··· ≥ u [M]. As an alternative, we can also compute τ ⋆ approximately using a bisection or by gradient descent w.r.t. τ.

<!-- chunk {"id": "body-0872", "role": "body", "section": "The sparsemax", "weight": 1.0} -->

Since 1 2 M ≤ ‖ π ‖ 2 2 ≤ 1 2, we get -M -1 2 M ≤ ‖ π ‖ 2 2 ≤ 0 for all π ∈ △ M. Following Proposition 13.7, we therefore get for all u ∈ R M

<!-- chunk {"id": "body-0873", "role": "body", "section": "Recovering smoothed ReLU functions", "weight": 1.0} -->

Using the vector u = (u, 0) ∈ R 2 as input, the smoothed max operator recovers the smoothed ReLU: where we defined Ψ(π):= Ω((π, 1 -π)). With Ω being Shannon's negentropy, we recover Ψ(π) = π log π +(1 -π) log(1 -π); with Ω being Gini's negentropy, we recover Ψ(π) = π (π -1), that we used to smooth the ReLU.

<!-- chunk {"id": "body-0874", "role": "body", "section": "Relaxed step functions (sigmoids)", "weight": 1.0} -->

We now turn to creating continuous relaxations of step functions. The binary step function, a.k.a. Heaviside step function, is defined by From Eq. (13.4), its variational form is We can therefore define the relaxation Notice that, unlike the case of the smoothed ReLU, it is a regularized argmax, not a regularized max. Following Remark 13.1, strongly convex regularization Ω ensures that step Ω (u) is a Lipschitz continuous function of u and is therefore, at least, differentiable almost everywhere, unlike step(u).

<!-- chunk {"id": "body-0875", "role": "body", "section": "The logistic function", "weight": 1.0} -->

If we use the regularizer Ω(π) = π log π +(1 -π) log(1 -π), we obtain the closed form This function is differentiable everywhere.

<!-- chunk {"id": "body-0876", "role": "body", "section": "The sparse sigmoid", "weight": 1.0} -->

As an alternative, if we use Ω(π) = π (π -1), we obtain a piecewise linear sigmoid, Unlike the logistic function, it can reach the exact values 0 or 1. However, the function has two kinks, where the function is non-differentiable.

<!-- chunk {"id": "body-0877", "role": "body", "section": "Link between smoothed ReLU functions and sigmoids", "weight": 1.0} -->

It turns out that the three sigmoids we presented above (step, logistic, sparsesigmoid) are all equal to the derivative of their corresponding smoothed ReLU function: and more generally This is a consequence of Danskin's theorem; see Example 11.2. We illustrate the smoothed ReLU functions and relaxed step functions (sigmoids) in Fig. 13.8.

<!-- chunk {"id": "body-0878", "role": "body", "section": "Relaxed argmax operators", "weight": 1.0} -->

We now turn to argmax operators, which are a generalization of step functions. With a slight notation overloading, let us now define where φ (j) = onehot(j) = e j is used to embed any integer j ∈ [M] into R M. Following the previous discussion, we have the variational form Figure 13.8: Smoothed ReLU functions and relaxed step functions (sigmoids). Differentiating the left functions gives the right functions. where the second equality uses that a linear function is maximized at one of the vertices of the simplex. This variational form suggests to define the relaxation Again, following Remark 13.1, argmax Ω (u) is guaranteed to be, at least, a differentiable almost everywhere function of u if Ω is strongly convex.

<!-- chunk {"id": "body-0879", "role": "body", "section": "Relaxed argmax operators", "weight": 1.0} -->

Similarly to sigmoids, it turns out that these mappings are equal to the gradient of their corresponding smoothed max operator: This is again a consequence of Danskin's theorem.

<!-- chunk {"id": "body-0880", "role": "body", "section": "The softargmax", "weight": 1.0} -->

When using Shannon's entropy Ω(π) = 〈 π, log π 〉, we obtain which is differentiable everywhere.

<!-- chunk {"id": "body-0881", "role": "body", "section": "The softargmax", "weight": 1.0} -->

Proof. We know that max Ω ( u ) = logsumexp( u ) and that ∇ max Ω ( u ) = argmax Ω ( u ). Differentiating logsumexp( u ) gives softargmax( u ).

<!-- chunk {"id": "body-0882", "role": "body", "section": "The sparseargmax", "weight": 1.0} -->

When using Gini's entropy Ω(π) = 1 2 〈 π, π -1 〉, which is up to a constant equal to 1 2 ‖ π ‖ 2 2, we obtain the sparseargmax which is nothing but the Euclidean projection onto the probability simplex (see also Section 16.3). The Euclidean projection onto the probability simplex △ M can be computed exactly using a medianfinding-like algorithm. The complexity is O (M) expected time and O (M log M) worst-case time. Computing the Euclidean projection onto the probability simplex boils down to computing τ ⋆ given in Eq. (13.5). Once we computed it, we have At its name indicates, and as the above equation shows, sparseargmax is sparse, but it is only differentiable almost everywhere. Note that the operator is originally known as sparsemax, but this is a misnomer, as it is really an approximation of the argmax. Therefore, in analogy with the softargmax, we use the name sparseargmax. We compare the argmax, softmax and sparseargmax in Fig. 13.9 and Fig. 13.10.

<!-- chunk {"id": "body-0883", "role": "body", "section": "Relaxed argmin operators", "weight": 1.0} -->

The argmin operator can be expressed in terms of the argmax operator, Figure 13.9: Values of argmax(u), softargmax(u), and sparseargmax(u) for u = (u 1, u 2, 0), when varying u 1 and u 2. The argmax is a piecewise constant, discontinuous function. The softargmax is a continuous and differentiable everywhere function, but it is always strictly positive and therefore dense. The sparseargmax is a continuous function and its output can be sparse, but it is only a differentiable almost everywhere function.

<!-- chunk {"id": "body-0884", "role": "body", "section": "Relaxed argmin operators", "weight": 1.0} -->

Given a relaxed argmax operator argmax Ω, we can therefore define a relaxed argmin by We then have for all u ∈ R M

<!-- chunk {"id": "body-0885", "role": "body", "section": "Summary", "weight": 1.0} -->

- When a function f is non-differentiable (or worse, discontinuous), a reasonable approach is to replace it by its smooth approximation (or continuous relaxation). - The first approach we reviewed is infimal convolution between f and primal regularization R. The Moreau envelope is a special case, obtained by using R = 1 2 ‖ · ‖ 2 2. - The second approach we reviewed is regularizing the convex conjugate f ∗ of f with some dual regularization Ω. We saw that the primal and dual approaches are equivalent when R = Ω ∗. - The Legendre-Fenchel transformation, a.k.a. convex conjugate, can be seen as a dual representation of a function: instead of representing f by its graph (u, f (u)) for u ∈ dom(f), we can represent it by the set of tangents with slope v and intercept -f ∗ (v) for v ∈ dom(f ∗) As its name indicates, it is convex, even if the original function is not.

<!-- chunk {"id": "body-0886", "role": "body", "section": "Summary", "weight": 1.0} -->

- We showed how to apply smoothing techniques to create smoothed ReLU functions and smoothed max operators. We also showed that taking their gradients allowed us to obtain generalized sigmoid functions and argmax operators.

<!-- chunk {"id": "body-0887", "role": "body", "section": "Smoothing by integration", "weight": 1.0} -->

In this chapter, we review smoothing techniques based on convolution.

<!-- chunk {"id": "body-0888", "role": "body", "section": "Convolution operators", "weight": 1.0} -->

The convolution between two functions f and g produces another function, denoted f ∗ g. It is defined by assuming that the integral is well defined. It is therefore the integral of the product of f and g after g is reflected about the y -axis and shifted. It can be seen as a generalization of the moving average. Using the change of variable u:= µ + z, which is again the location-scale transform, we can also write The convolution operator is therefore commutative.

<!-- chunk {"id": "body-0889", "role": "body", "section": "Convolution with a kernel", "weight": 1.0} -->

The convolution is frequently used together with a kernel κ to create a smooth approximation f ∗ κ of f. The most frequently used kernel is the Gaussian kernel with width σ, defined by This is the probability density function (PDF) of the normal distribution with zero mean and variance σ 2. The term 1 √ 2 πσ is a normalization constant, ensuring that the kernel sums to 1 for all σ. We therefore say that κ σ is a normalized kernel.

<!-- chunk {"id": "body-0890", "role": "body", "section": "Averaging perspective", "weight": 1.0} -->

Applying the definition of the convolution in Eq. (14.1), we obtain is the PDF of the Gaussian distribution with mean µ and variance σ 2. Therefore, we can see f ∗ κ σ as the expectation of f (u) over a Gaussian centered around µ. This property is true for all translationinvariant kernels, that correspond to a location-scale family distribution (e.g., the Laplace distribution). The convolution therefore performs an averaging with all points, with points nearby µ given more weight by the distribution. The parameter σ controls the importance we want to give to farther points. We call this viewpoint averaging, as we replace f (u) by E [f (U)].

<!-- chunk {"id": "body-0891", "role": "body", "section": "Perturbation perspective", "weight": 1.0} -->

Conversely, using the alternative definition of the convolution operator in Eq. (14.2), which stems from the commutativity of the convolution, we have where, in the third line, we used that p 0,σ is sign invariant, i.e., p 0,σ (z) = p 0,σ (-z). This viewpoint shows that smoothing by convolution with a Gaussian kernel can also be seen as injecting Gaussian noise or perturbations to the function's input.

<!-- chunk {"id": "body-0892", "role": "body", "section": "Limit case", "weight": 1.0} -->

When σ → 0, the kernel κ σ converges to a Dirac delta function, Since the Dirac delta is the multiplicative identity of the convolution algebra (this is also known as the sifting property), when σ → 0, f ∗ κ σ converges to f, i.e.,

<!-- chunk {"id": "body-0893", "role": "body", "section": "Discrete convolution", "weight": 1.0} -->

Many times, we work with functions whose convolution does not have an analytical form. In these cases, we can use a discrete convolution on a grid of values. For two functions f and g defined over Z, the discrete convolution is defined by As for its continuous counterpart, the discrete convolution is commutative, namely, Figure 14.1: Smoothing of the signal f [t]:= t 2 +0. 3 sin(6 πt) with a sampled and renormalized Gaussian kernel.

<!-- chunk {"id": "body-0894", "role": "body", "section": "Discrete convolution", "weight": 1.0} -->

When g has finite support over the set S:= {-M, -M +1,..., 0,..., M -1, M }, meaning that g [i] = 0 for all i ̸∈ S, a finite summation may be used instead, i.e., In practice, convolution between a discrete signal f: Z → R and a continuous kernel κ: R → R is implemented by discretizing the kernel. One of the simplest approaches consists in sampling points on an interval, evaluating the kernel at these points and renormalizing the obtained values, so that the sampled kernel sums to 1. This is illustrated with the Gaussian kernel in Fig. 14.1. Since the Gaussian kernel decays exponentially fast, we can choose a small interval around 0. For a survey of other possible discretizations of the Gaussian kernel, see Getreuer.

<!-- chunk {"id": "body-0895", "role": "body", "section": "Differentiation", "weight": 1.0} -->

Remarkably, provided that the two functions are integrable with integrable derivatives, the derivative of the convolution satisfies which simply stems from switching derivative and integral in the definition of the convolution. Moreover, we have the following proposition.

<!-- chunk {"id": "body-0896", "role": "body", "section": "Differentiation", "weight": 1.0} -->

Proposition 14.1 (Differentiability of the convolution). If g is n -times differentiable with compact support over R and f is locally integrable over R, then f ∗ g is n -times differentiable over R.

<!-- chunk {"id": "body-0897", "role": "body", "section": "Multidimensional convolution", "weight": 1.0} -->

So far, we studied the convolution of one-dimensional functions. The definition can be naturally extended to multidimensional functions f: R M → R and g: R M → R as assuming again that the integral exists. Typically, a Gaussian kernel with diagonal covariance matrix is used where, in the second equality, we assumed σ 1 = · · · = σ M. In an image processing context, where M = 2, it is approximated using a discrete convolution and it is called a Gaussian blur.

<!-- chunk {"id": "body-0898", "role": "body", "section": "Link between convolution and infimal convolution", "weight": 1.0} -->

The infimal convolution we studied in Section 13.1 takes the form In comparison, the classical convolution takes the form The two forms of convolution are clearly related. Infimal convolution performs an infimum and uses the sum of f and g: it uses a minplus algebra. Classical convolution performs an integral and uses the product of F and G: it uses a sum-product algebra.

<!-- chunk {"id": "body-0899", "role": "body", "section": "The soft infimal convolution", "weight": 1.0} -->

The link between the infimal convolution and the classical convolution can be further elucidated if we replace the infimum with a soft minimum in the definition of the infimal convolution.

<!-- chunk {"id": "body-0900", "role": "body", "section": "The soft infimal convolution", "weight": 1.0} -->

Definition 14.1 (Soft infimal convolution). The soft infimal convolution between f: R M → R and g: R M → R is where we defined the soft minimum (assuming that it exists) over S of any function h: S → R as We recover the infimal convolution as ε → 0.

<!-- chunk {"id": "body-0901", "role": "body", "section": "Computation using a convolution", "weight": 1.0} -->

We now show that we can rewrite the soft infimal convolution using a classical convolution. Indeed, by using the exponential change of variable (sometimes referred to as Cole-Hopf transformation in a partial differential equation context) we can define each function in the exponential domain, It is easy to check that we then have Back to log domain, we obtain Combining the transformation and its inverse, we can write What we have shown is that, after an exponential change of variable, the soft infimal convolution can be reduced to the computation of a convolution. This is useful as a discrete convolution on a grid of size n can be computed in O (n log n).

<!-- chunk {"id": "body-0902", "role": "body", "section": "The soft Moreau envelope", "weight": 1.0} -->

We saw in Section 13.1.2 that the infimal convolution between f and R (z) = 1 2 z 2 is the Moreau envelope, Replacing the infimal convolution with a soft infimal convolution, we can define the 'soft' Moreau envelope, We emphasize that this is operation is not the same as the convolution of f with a Gaussian kernel. Indeed, we have where κ σ is for instance defined in Eq. (14.3).

<!-- chunk {"id": "body-0903", "role": "body", "section": "The soft Moreau envelope", "weight": 1.0} -->

We saw that the Moreau envelope is a smooth function. One may therefore ask what do we gain from using a soft Moreau envelope. The benefit can be computational, as the latter can be approximated using a discrete convolution.

<!-- chunk {"id": "body-0904", "role": "body", "section": "Fourier and Laplace transforms", "weight": 1.0} -->

Let us define the Fourier transform of f by Note that F{ f } is a function transformation: it transforms f into another function F.

<!-- chunk {"id": "body-0905", "role": "body", "section": "Convolution theorem", "weight": 1.0} -->

Now, consider the convolution If we define the three transformations the convolution theorem states that Written differently, we have In words, in the Fourier domain, the convolution operation becomes a multiplication. Conversely, The convolution theorem also holds if we replace the Fourier transform with the Laplace transform or with the two-sided (bilateral) Laplace transform.

<!-- chunk {"id": "body-0906", "role": "body", "section": "Link between Fourier and Legendre transforms", "weight": 1.0} -->

In Section 13.2, we studied another function transformation: the convex conjugate, also known as Legendre-Fenchel transform. We recap the analogies between these transforms in Table 14.1. In particular, the counterpart of Table 14.1: Analogy between Fourier and Legendre transforms. See Proposition 13.3 for more conjugate calculus rules. for the infimal convolution is In words, the Legendre-Fenchel transform is to the infimal convolution what the Fourier transform is to the convolution.

<!-- chunk {"id": "body-0907", "role": "body", "section": "The soft Legendre-Fenchel transform", "weight": 1.0} -->

We saw in Section 13.2 that the Legendre-Fenchel transform (convex conjugate) of a function f: R M → R is If necessary, we can support constraints by including an indicator function in the definition of f. The conjugate can be smoothed out using a log-sum-exp, which plays the role of a soft maximum (Section 13.5).

<!-- chunk {"id": "body-0908", "role": "body", "section": "The soft Legendre-Fenchel transform", "weight": 1.0} -->

Definition 14.2 (Soft convex conjugate). where we defined the soft maximum (assuming that it exists) over S of any function g: S → R as In the limit ε → 0, we recover the convex conjugate.

<!-- chunk {"id": "body-0909", "role": "body", "section": "Computation using a convolution", "weight": 1.0} -->

We now show that this smoothed conjugate can be rewritten using a convolution if we apply a bijective transformation to f.

<!-- chunk {"id": "body-0910", "role": "body", "section": "Computation using a convolution", "weight": 1.0} -->

Proposition 14.2 (Smoothed convex conjugate as convolution). The smoothed conjugate can be rewritten as This insight was tweeted by Gabriel Peyré in April 2020.

<!-- chunk {"id": "body-0911", "role": "body", "section": "Computation using a convolution", "weight": 1.0} -->

What did we gain from this viewpoint? The convex conjugate can often be difficult to compute in closed form. If we replace R M with a discrete set S (i.e., a grid), we can then approximate the smoothed convex conjugate in O (n log n), where n = |S|, using a discrete convolution, where K is the n × n Gaussian kernel matrix whose entries correspond to exp(-1 2 ε ‖ u -u ′ ‖ 2 2) for u, u ′ ∈ S and q is the n -dimensional vector whose entries correspond to exp(1 ε (1 2 ‖ v ‖ 2 2 -f (u)) for u ∈ S. This provides a GPU-friendly alternative to the fast Legendre transform algorithm, discussed in Section 13.2. Of course, due to the curse of dimensionality, the technique is limited to functions defined on low-dimensional sets. We illustrate in Fig. 14.2 the application of the technique to computing an approximate biconjugate (convex envelope) of a function.

<!-- chunk {"id": "body-0912", "role": "body", "section": "Computation using a convolution", "weight": 1.0} -->

Remark 14.1 (Link with the two-sided Laplace transform). For one-dimensional functions, instead of using a convolution, we can also write the soft convex conjugate as where we defined the two-sided (bilateral) Laplace transform and where we assumed that the integral exists.

<!-- chunk {"id": "body-0913", "role": "body", "section": "Examples", "weight": 1.0} -->

In this section, we review practical examples for which the convolution with a Gaussian kernel enjoys an analytical solution.

<!-- chunk {"id": "body-0914", "role": "body", "section": "Smoothed step function", "weight": 1.0} -->

Example 14.1 (Smoothed Heaviside). The Heaviside step function is defined by With the Gaussian kernel, we therefore obtain where Φ σ (µ) is the CDF of the Gaussian distribution with zero mean and variance σ 2, and where we used the error function that we both already encountered in Chapter 3. Although there is no closed form for the error function, it is commonly available in numerical analysis software, such as SciPy.

<!-- chunk {"id": "body-0915", "role": "body", "section": "Smoothed ReLU function", "weight": 1.0} -->

Example 14.2 (Smoothed ReLU). The ReLU is defined by Figure 14.3: Smoothing of the ReLU and Heaviside functions by convolution with a Gaussian kernel, for three values of the width σ.

<!-- chunk {"id": "body-0916", "role": "body", "section": "Smoothed ReLU function", "weight": 1.0} -->

Similarly to the previous example, we obtain In the second integral, setting a:= 1 2 σ 2, we used To illustrate differentiation of the convolution, we show how to differentiate the smoothed ReLu.

<!-- chunk {"id": "body-0917", "role": "body", "section": "Smoothed ReLU function", "weight": 1.0} -->

Example 14.3 (Differentiating the smoothed ReLU). Differentiating the smoothed ReLU from Example 14.2, we obtain Therefore, unsurprisingly, the derivative of the smoothed ReLU is the smoothed Heaviside step function. Differentiating once again, we obtain, where the derivative h ′ is well-defined almost everywhere. We can arrive at the same result by using that h ∗ κ σ = Φ σ and Φ ′ σ = κ σ, since Φ σ and κ σ are the CDF and PDF of the Gaussian with zero mean and σ 2 variance.

<!-- chunk {"id": "body-0918", "role": "body", "section": "Perturbation of blackbox functions", "weight": 1.0} -->

In this section, we review how to approximately compute a convolution with a kernel and its gradient using Monte-Carlo estimation.

<!-- chunk {"id": "body-0919", "role": "body", "section": "Expectation in a location-scale family", "weight": 1.0} -->

A rather intuitive approach to smooth a function f: R M → R is to average its values on an input µ, perturbed by some additive noise Z ∼ p, for some noise distribution p. This defines the surrogate The parameter σ controls the perturbation strength: as σ → 0, we naturally recover f. An equivalent viewpoint is obtained by defining the transformation (change of variables) where p µ,σ is the location-family distribution generated by the noise distribution p. It is the pushforward distribution of Z through the transformation (see Section 12.4.4). In this notation, the initial noise distribution p is then simply p = p 0, 1. The perturbed function can then be expressed from these two perspectives as We then have Writing the expectation as the integral of a p.d.f, we naturally recover the smoothing by convolution presented earlier, where we defined the kernel In the sequel, we assume that the noise distribution decomposes as where ν (z) is the log-density of the noise distribution and C is a normalization constant.

<!-- chunk {"id": "body-0920", "role": "body", "section": "Expectation in a location-scale family", "weight": 1.0} -->

For instance, the Gaussian distribution with diagonal covariance matrix and the corresponding Gaussian kernel are obtained with ν (z) = 1 2 ‖ z ‖ 2 2 and C = √ 2 π M.

<!-- chunk {"id": "body-0921", "role": "body", "section": "Approximation by Monte-Carlo estimation", "weight": 1.0} -->

Instead of approximating the integral above (continuous convolution) with a discrete convolution on a grid, as we did in Section 14.1.3, the expectation perspective suggests that we can estimate f σ ( µ ) by Monte-Carlo estimation: we simply draw samples from the distribution, evaluate the function at these samples and average. Beyond mere MonteCarlo estimation, more elaborate approximation schemes are studied.

<!-- chunk {"id": "body-0922", "role": "body", "section": "Gradient estimation by reparametrization", "weight": 1.0} -->

Provided that the conditions for swapping differentiation and integration hold (see Section 12.1), we have Note that if f is only differentiable almost everywhere, the formula may still hold. For example, if f is the ReLU, then ∇ f is the Heaviside step function, and we obtain the correct gradient of f σ using the formula above; see Example 14.1. However, if f is not absolutely continuous, the formula may not hold. For example, if f is the Heaviside function, the right-hand side of (14.5) is 0 which does not match the gradient of f σ; see again Example 14.1.

<!-- chunk {"id": "body-0923", "role": "body", "section": "Gradient estimation by reparametrization", "weight": 1.0} -->

From the second expression of f σ in (14.4), we can see the formula of the gradient in (14.5) as a reparametrization trick U = µ + σZ; see Section 12.4. Namely, we have

<!-- chunk {"id": "body-0924", "role": "body", "section": "Gradient estimation by SFE, Stein's lemma", "weight": 1.0} -->

In some cases, we may not have access to ∇ f or f may not be absolutely continuous and therefore the formula in (14.5) cannot apply. For these cases, we can use the score function estimator (SFE) from Section 12.3. Here, for f σ (µ) = E U ∼ p µ,σ [f (U)], we obtain Since the PDF can be written as To summarize, we have shown that where we used the change of variable Z = (U -µ) /σ. The same technique can also be used if we want to estimate the gradient w.r.t. θ = (µ, σ) or if we want to estimate the Jacobian of the expectation of a vector-valued function.

<!-- chunk {"id": "body-0925", "role": "body", "section": "Gradient estimation by SFE, Stein's lemma", "weight": 1.0} -->

In the particular case of Gaussian noise, since ∇ ν (z) = z, we obtain This is known as Stein's lemma. It should be noted that the above is an unbiased estimator of the gradient of the smoothed function f σ, but a biased estimator of the gradient of the original function f (assuming that it exists). However, smoothing is usually a good thing, as it can accelerate the convergence of gradient-based algorithms. Computing the gradient of perturbed general programs is studied in detail.

<!-- chunk {"id": "body-0926", "role": "body", "section": "Link between reparametrization and SFE", "weight": 1.0} -->

Using the log-derivative identity, we have for any distribution with differentiable density p Using integration by parts and assuming that h (z) p (z) goes to zero when ‖ z ‖ → ∞, we have We have therefore the identity Importantly, contrary to the SFE estimator from Section 12.3, this identity uses gradients with respect to z, not with respect to the parameters of the distribution. Nevertheless, using the reparametrization Essentially, integration by parts allowed us to convert the reparametrization trick estimator into the SFE estimator. For more applications of integration by parts in machine learning, see Francis Bach's excellent blog post.

<!-- chunk {"id": "body-0927", "role": "body", "section": "Variance reduction and evolution strategies", "weight": 1.0} -->

As discussed in Chapter 12, the SFE suffers from high variance. We now apply variance reduction techniques to it. To do so, we assume that ∇ ν (Z) has zero mean for Z ∼ p 0, 1. This assumption for example holds for Gaussian noise. This assumption implies that This is an example of control variate discussed in Section 12.3. This can be interpreted as using a finite difference for computing a directional derivative in the random direction Z (see 'limit case' below). Inspired by a central finite difference, we can also use These estimators have been used as part of blackbox (zero-order) optimization algorithms, such as evolution strategies or random gradient-free optimization. For quadratic functions, it is easy to show that the second estimator achieves lower variance. The idea of sampling both Z and -Z simultaneously is called antithetic or mirrored sampling. Evolution strategies have also been used to obtain unbiased gradient estimators of partially unrolled computational graphs. We empirically compare the SFE with or without variance reduction for blackbox gradient estimation in Fig. 14.4.

<!-- chunk {"id": "body-0928", "role": "body", "section": "Zero-temperature limit", "weight": 1.0} -->

We now discuss the limit case σ → 0. That is, we assume that we do not want to perform smoothing and that ∇ f exists. We recall that the directional derivative of f at µ in the direction z is When σ → 0 and Z follows the standard Gaussian distribution, meaning that ∇ ν (z) = z, Eq. (14.8) therefore becomes This should not be too surprising, as we already know from the convolution perspective that f σ (µ) = (f ∗ κ σ)(µ) → f (µ) when σ → 0. This recovers the randomized forward-mode estimator already presented in Section 8.7.

<!-- chunk {"id": "body-0929", "role": "body", "section": "The Gumbel distribution", "weight": 1.0} -->

The Gumbel distribution is a distribution frequently used in extreme value theory. As illustrated in Fig. 14.5, we consider the shifted standard Gumbel distribution, whose PDF is defined by and where γ ≈ 0. 577 is Euler's constant. Note that in some formulations, the distribution is not shifted, i.e., γ is not added. If Z is distributed according to the shifted standard Gumbel distribution, we write Z ∼ Gumbel.

<!-- chunk {"id": "body-0930", "role": "body", "section": "The Gumbel distribution", "weight": 1.0} -->

To obtain a multivariate extension with location-scale parameters µ and σ, we take M independent random variables Z:= (Z 1,..., Z m) and apply the location-scale transform (Section 12.4.1). That is, As we used shifted standard Gumbel distributions, we naturally get that E [U] = µ and Var(U) = σ 2. We can use Gumbel noise as an alternative to the Gaussian noise used in Section 14.4. Thankfully, in particular cases, we can compute closed-form expressions of the expectation of perturbed functions.

<!-- chunk {"id": "body-0931", "role": "body", "section": "Remark 14.2 (Link between Gumbel and exponential distribution)", "weight": 1.0} -->

A random variable Z is distributed as Gumbel( µ, 1) if and only if exp( -Z ) is distributed as an exponential distribution Exp(exp( µ -γ )). To see this, one can simply compute the CDF of exp( -Z ) and recognize the CDF of Exp(exp( µ -γ )). Therefore, when comparing Gumbel distributions, we can use standard properties of the exponential distribution.

<!-- chunk {"id": "body-0932", "role": "body", "section": "Remark 14.2 (Link between Gumbel and exponential distribution)", "weight": 1.0} -->

Remark 14.3 (Sampling Gumbel noise). If U ∼ Uniform, then Z:= -log( -log( U )) -γ satisfies Z ∼ Gumbel, where we recall that we use Gumbel to denote the shifted standard Gumbel distribution. To see this, note that P ( Z ≤ t ) = P ( U ≤ exp(exp( -( γ + t )))) = exp(exp( -( γ + t ))), where the last expression matches the CDF of Gumbel.

<!-- chunk {"id": "body-0933", "role": "body", "section": "Perturbed comparison", "weight": 1.0} -->

To start, the Gumbel distribution can be used to smooth a binary comparison like the greater than or equal operators. Recall that the latter is defined for any µ 1, µ 2 ∈ R as where step is the Heaviside function. As shown below, by perturbing each variable with Gumbel noise, we recover logistic(a -b) = 1 / (1 + e -(a -b)) as an approximation of step(a -b).

<!-- chunk {"id": "body-0934", "role": "body", "section": "Perturbed argmax", "weight": 1.0} -->

Suppose we want to smooth with φ (i) is the one-hot encoding of i ∈ [M]. It turns out that the function y (u) perturbed using Gumbel noise enjoys a closed form expectation, which is nothing else than the softargmax.

<!-- chunk {"id": "body-0935", "role": "body", "section": "Perturbed argmax", "weight": 1.0} -->

Proposition 14.4 (Gumbel trick for categorical variables). Let us define M independent random variables Z ∼ Gumbel ∈ R M. Then, for µ ∈ R M and σ > 0, Proof. For k ∈ [M], we have that By Remark 14.2, we have that e -µ i /σ -Z i ∼ Exp(exp(µ i /σ -γ)). One easily verifies as an exercise, that, for U 1,..., U M independent exponential variables with parameters u 1,..., u m, we have P (arg min i ∈ [M] { U i } = k) = u k / ∑ i M =1 u i. Hence, we get The last claim follows from the distribution of Y and the definition of φ.

<!-- chunk {"id": "body-0936", "role": "body", "section": "Perturbed max", "weight": 1.0} -->

A similar result holds if we now wish to perturb the max instead of the argmax.

<!-- chunk {"id": "body-0937", "role": "body", "section": "Perturbed max", "weight": 1.0} -->

Proposition 14.5 (Link to log-sum-exp). Let us define M independent random variables Z ∼ Gumbel ∈ R M and Then, for µ ∈ R M and σ > 0, that is, Proof. We derive the CDF of f (µ + σ · Z) as We have e -(µ i /σ -Z i) ∼ Exp(exp(µ i /σ i) -γ) and for U 1,..., U M independent exponential random variables with parameters u i, we have min i ∈ [M] U i ∼ Exp(∑ i M =1 u i). Hence, We recognize the CDF of the shifted Gumbel distribution with locationscale parameters σ LSE(µ /σ) and σ.

<!-- chunk {"id": "body-0938", "role": "body", "section": "Perturbed max", "weight": 1.0} -->

For further reading on the Gumbel trick, see Tim Vieira's great blog.

<!-- chunk {"id": "body-0939", "role": "body", "section": "Gumbel trick for sampling", "weight": 1.0} -->

The Gumbel trick is also useful in its own right for sampling without computing the normalization constant of the softargmax. Indeed, Proposition 14.4 ensures that if Z is Gumbel noise, then Y is distributed according to Categorical(softargmax( µ /σ )). Computing the arg-maximum, as required to compute Y, can be done in one pass. Therefore, we obtain a one-pass algorithm to sample directly from the logits µ, without explicitly computing the probabilities softargmax( µ /σ ).

<!-- chunk {"id": "body-0940", "role": "body", "section": "Gumbel trick for sampling", "weight": 1.0} -->

One may wonder whether such trick could also be used with the normal distribution. Unfortunately, there is no closed form in this case because it would require integrating the CDF of the maximum of M -1 Gaussian distributions. However, other tricks can be defined such as using Weibull distributions, see Balog et al..

<!-- chunk {"id": "body-0941", "role": "body", "section": "Perturb-and-MAP", "weight": 1.0} -->

Previously, we discussed the Gumbel trick in the classification setting, where Y = [M]. In the structured prediction setting, outputs are typically embedded in R M but the output space is very large. That is, Y ⊆ R M but |Y| ≫ M. Structured outputs are then decoded using a maximum a-posteriori (MAP) oracle For this setting, the perturbed versions of f and y, no longer enjoy a closed form in general. However, we can approximate them using Monte-carlo estimation. For the gradient of ∇ f σ (µ), two estimators exist.

<!-- chunk {"id": "body-0942", "role": "body", "section": "Perturb-and-MAP", "weight": 1.0} -->

Proposition 14.6 (Gradient of perturbed max). Let Y ⊆ R M and Z be noise with density Then, f σ (µ) is smooth, and its gradient is given by The first estimator is simply a consequence of the reparametrization trick seen in Eq. (14.6) and of y = ∇ f, which follows from Danskin's theorem (see Section 11.2). The second estimator is just SFE seen in Eq. (14.7). The first estimator usually has lower variance, as it uses more information, namely that y = ∇ f.

<!-- chunk {"id": "body-0943", "role": "body", "section": "Perturb-and-MAP", "weight": 1.0} -->

The Jacobian of y σ ( µ ) also has two estimators.

<!-- chunk {"id": "body-0944", "role": "body", "section": "Perturb-and-MAP", "weight": 1.0} -->

Proposition 14.7 (Jacobian of perturbed argmax). Under the same notation as in Proposition 14.6, we have The first estimator uses SFE. The second estimator is obtained by differentiating through The first estimator usually has lower variance. Note that we cannot use the reparametrization trick this time, since y is discontinuous, contrary to f.

<!-- chunk {"id": "body-0945", "role": "body", "section": "Link between perturbation and regularization", "weight": 1.0} -->

As shown, assuming Y is a convex polytope with non-empty interior and p has a strictly positive density, the function is strictly convex and its convex conjugate f ∗ σ (y) is Legendre-type. We can therefore rewrite f σ (µ) from the regularization perspective as and ∇ f σ (µ) = y σ (µ) is a mirror map, a one-to-one mapping from R M to the interior of Y. Unfortunately, f ∗ σ (y) does not enjoy a closed form in general. Conversely, does any regularization has a corresponding noise distribution? The reciprocal is not true.

<!-- chunk {"id": "body-0946", "role": "body", "section": "Gumbel-softargmax", "weight": 1.0} -->

Suppose we want to smooth out the composition h (u):= g (y (u)) between some function g: { e 1,..., e M } → R and the argmax This is useful for instance to compute the expectation of a loss (instead of the loss of an expectation). To compute the gradient of h σ (µ), we can readily use the SFE. However, we saw that it suffers from high variance. Unfortunately, we cannot swap differentiation and integration (expectation) here, since y (u) is a discontinuous function. See Section 12.1 for more details regarding differentiation under the integral sign.

<!-- chunk {"id": "body-0947", "role": "body", "section": "Gumbel-softargmax", "weight": 1.0} -->

The key idea of the Gumbel-softargmax is to replace y (u) with a softargmax (with temperature parameter τ) to define Since the softargmax is a regularized argmax, we can see the Gumbelsoftargmax approach as using both regularization and perturbation. Note that the approach is also known as Gumbel-softmax. We use the name Gumbel-softargmax for consistency with the terminology of this book.

<!-- chunk {"id": "body-0948", "role": "body", "section": "Gumbel-softargmax", "weight": 1.0} -->

The use of the softargmax transformation defines a continuous distribution, that we now explain with σ = 1.

<!-- chunk {"id": "body-0949", "role": "body", "section": "Gumbel-softargmax", "weight": 1.0} -->

The key benefit is that we can now swap differentiation and integration (expectation) to get an unbiased estimator of ∇ h σ,τ ( µ ). However, this will be a biased estimator of ∇ h σ ( µ ), the amount of bias being controlled by the temperature τ. In particular, in the limit case τ → 0, we have h σ,τ ( µ ) → h σ ( µ ). One caveat, however, is that the function g needs to be well defined on △ M, instead of { e 1,..., e M }.

<!-- chunk {"id": "body-0950", "role": "body", "section": "Gumbel-softargmax", "weight": 1.0} -->

Proposition 14.8 (Gumbel-softargmax / Concrete distributions). Let us define the continuous random variable where Z is a Gumbel random variable. Then T is distributed according to a distribution with density We can extend the Gumbel softargmax to the structured setting by replacing with its regularized variant. Similarly as before, one caveat is that g needs to be well defined on conv(Y) instead of Y. Moreover, regularizing y is not always easy computationally.

<!-- chunk {"id": "body-0951", "role": "body", "section": "Summary", "weight": 1.0} -->

- We studied smoothing techniques based on function convolution with a kernel. Due to the commutativity of the convolution, we can alternatively see these as the expectation of the function, perturbed with noise, assuming the kernel corresponds to the PDF of some noise distribution. - Their gradients can be estimated using the path gradient estimator (PGE) or score function estimator (SFE), depending on whether the gradient of the original function is available or not. - We saw that Stein's lemma is a special case of SFE used with Gaussian noise. The so-called 'evolution strategies' are just a variant of that with variance reduction and can be interpreted as randomized finite difference. - When using Gumbel noise, we were able to derive closed-form expressions for the expectation in specific cases: perturbed comparison, perturbed argmax and perturbed max. - We also studied the connections between smoothing by optimization and smoothing by integration. Infimal convolution is the counterpart of convolution, and the Legendre-Fenchel transform is the counterpart of Fourier and Laplace's transforms.

<!-- chunk {"id": "body-0952", "role": "body", "section": "Summary", "weight": 1.0} -->

Infimal convolution uses a min-plus algebra in the log domain, while the convolution uses a sum-product algebra in the exponential domain.

<!-- chunk {"id": "body-0953", "role": "body", "section": "Objective functions", "weight": 1.0} -->

Consider a function L, for example evaluating the error or 'loss' L (w) achieved by a model with parameters w ∈ W, where W = R P. To find the best possible model parameterization, we seek to minimize L (w), that is, to compute approximately assuming that the infimum exists (i.e., L (w) is lower bounded). We will denote a solution, if it exists, by In general, an analytical solution is not available and computing such a minimum approximately requires an optimization algorithm. An optimization algorithm is an iterative procedure, which, starting from an initial point w 0, outputs after t iterations a point w t that approximates the minimum of L up to some accuracy ε, i.e.,

<!-- chunk {"id": "body-0954", "role": "body", "section": "Oracles", "weight": 1.0} -->

To produce iterates w 1, w 2,... that converge to a minimum, the algorithm naturally needs to have access to information about L. For example, the algorithm needs a priori to be able to evaluate L to know if it decreased its value or not. Such information about the function is formalized by the notion of oracles. Formally, oracles are procedures that an algorithm can call to access information about the objective L ( w ) at any given point w ∈ W. We usually mainly consider the following three oracles.

<!-- chunk {"id": "body-0955", "role": "body", "section": "Oracles", "weight": 1.0} -->

- Zero-order oracle: evaluating the function L (w) ∈ R. - Second-order oracle: evaluating the Hessian matrix ∇ 2 L (w), or evaluating the Hessian-vector product (HVP) ∇ 2 L (w) v ∈ W, for L twice differentiable and any vector v ∈ W. - First-order oracle: evaluating the gradient ∇ L (w) ∈ W for L differentiable.

<!-- chunk {"id": "body-0956", "role": "body", "section": "Oracles", "weight": 1.0} -->

Given an oracle O for a function L, we can formally define an optimization algorithm as a procedure which computes the next iterate as a function of all past and current information. Formally, an algorithm A builds a sequence w 1,..., w t from a starting point w 0 as where λ ∈ Λ ⊆ R Q encapsulates some hyperparameters of the algorithm, such as the stepsize. Oftentimes, algorithms build the next iterate simply from the information collected at the current iterate, without using all past iterates. That is, they take the form w t +1 = A (w t, O (w t), λ). A classical example is the gradient descent algorithm, that uses a first-order oracle to compute iterates of the form where the stepsize γ is a hyperparameter of the algorithm. The notion of oracle therefore delineates different classes of algorithms. For instance, we may consider zero-order algorithms or first-order algorithms.

<!-- chunk {"id": "body-0957", "role": "body", "section": "Variational perspective of optimization algorithms", "weight": 1.0} -->

One of the most basic optimization algorithms is the proximal point method, which produces w t +1 from w t by In words, the next iterate is produces by solving a trade-off between minimizing the function L and staying close to w t. Unfortunately, the optimization problem involved in performing this parameter update is as difficult as the original optimization problem, making the proximal point method impractical.

<!-- chunk {"id": "body-0958", "role": "body", "section": "Variational perspective of optimization algorithms", "weight": 1.0} -->

As we shall see in Chapter 16 and Chapter 17, many optimization algorithms can be seen as an approximation of the proximal point method, in the sense that they solve where ˜ L (w, w t) is an approximation of L (w) around w t and d (w, w ′) is some form of distance between w and w ′. Different choices of ˜ L and d lead to different optimization algorithms, and to different trade-offs.

<!-- chunk {"id": "body-0959", "role": "body", "section": "Classes of functions", "weight": 1.0} -->

When studying algorithms theoretically, stronger results can often be stated by restricting to certain classes of functions. We already covered continuous and differentiable functions in Chapter 2. We review a few important other classes in this section.

<!-- chunk {"id": "body-0960", "role": "body", "section": "Lipschitz functions", "weight": 1.0} -->

Lipschitz continuity is a stronger form of continuity. Intuitively, a Lipschitz continuous function is limited in how fast it can change.

<!-- chunk {"id": "body-0961", "role": "body", "section": "Lipschitz functions", "weight": 1.0} -->

Definition 15.1 (Lipschitz-continuous functions). Afunction g: W → F is β -Lipschitz continuous if for all w, v ∈ W Note that the definition is valid even for vector-valued functions.

<!-- chunk {"id": "body-0962", "role": "body", "section": "With respect to arbitrary norms", "weight": 1.0} -->

Thanks to dual norms reviewed in Section 18.1, we can state a more general definition of Lipschitz continuity based on arbitrary norms, instead of the 2-norm. Moreover, we may consider Lipschitz-continuity over a subset of the input domain.

<!-- chunk {"id": "body-0963", "role": "body", "section": "With respect to arbitrary norms", "weight": 1.0} -->

Definition 15.2 (Lipschitz continuous functions w.r.t. a norm). Afunction g: W → F is said to be β -Lipschitz w.r.t. a norm ‖ · ‖ over a set C ⊆ W if for all w, v ∈ C When ‖ · ‖ = ‖ · ‖ 2, we recover Definition 15.1, since the 2-norm is dual to itself.

<!-- chunk {"id": "body-0964", "role": "body", "section": "Smooth functions", "weight": 1.0} -->

A differentiable function L is said to be β -smooth if its gradients are β -Lipschitz continuous. Setting g ( w ) = ∇ L ( w ) in Definition 15.1, we obtain the following definition.

<!-- chunk {"id": "body-0965", "role": "body", "section": "Smooth functions", "weight": 1.0} -->

Definition 15.3 (Smooth functions). A differentiable function L: W → R is β -smooth for β > 0 if for all w, v ∈ W Smoothness ensures that the information provided by the gradient at some w is meaningful in a neighborhood of w, since its variations are upper-bounded. If the variations were not bounded, the gradient at v arbitrarily close to w could drastically change, rendering the information provided by a first-order oracle potentially useless.

<!-- chunk {"id": "body-0966", "role": "body", "section": "Smooth functions", "weight": 1.0} -->

Smoothness of a function can be interpreted as having a quadratic upper bound on the function as formalized below.

<!-- chunk {"id": "body-0967", "role": "body", "section": "Smooth functions", "weight": 1.0} -->

Proposition 15.1 (Smooth functions). If a differentiable function L: W → R is β -smooth then for all w, v ∈ W, Proof. This is shown by bounding | L (v) -L (w) - 〈∇ L (w), v -w 〉| using the integral representation of the objective along w -v, i.e., | L (v) -L (w) -〈∇ L (w), v -w 〉| = | ∫ 1 0 〈∇ L (w + s (v -w)), v -w 〉 ds -〈∇ L (w), v -w) 〉| ≤ ∫ 1 0 ‖∇ L (w + s (v -w)) ds -∇ L (w) ‖ 2 ‖ v -w ‖ 2 ≤ L ‖ w -v ‖ 2 2 / 2, where the last inequality follows from the smoothness assumption and standard integration.

<!-- chunk {"id": "body-0968", "role": "body", "section": "Smooth functions", "weight": 1.0} -->

In other words, L ( w ) is upper-bounded and lower-bounded around v by a quadratic function of w. We will see in Section 16.1 that this characterization gives rise to a variational perspective on gradient descent.

<!-- chunk {"id": "body-0969", "role": "body", "section": "With respect to arbitrary norms", "weight": 1.0} -->

We can generalize the definition of smoothness in Definition 15.3 to arbitrary norms.

<!-- chunk {"id": "body-0970", "role": "body", "section": "With respect to arbitrary norms", "weight": 1.0} -->

Definition 15.4 (Smooth functions w.r.t. a norm). A function L: W → R is β -smooth w.r.t. a norm ‖ · ‖ over a set C if for all w, v ∈ C An equivalent characterization, generalizing Proposition 15.1 to arbitrary norms, is given below (see, e.g. Beck).

<!-- chunk {"id": "body-0971", "role": "body", "section": "With respect to arbitrary norms", "weight": 1.0} -->

Proposition 15.2 (Smooth functions w.r.t. a norm). If a differentiable function L: W → R is β -smooth w.r.t. a norm ‖ · ‖ over a set C, then for all w, v ∈ C where B f is the Bregman divergence generated by f (Definition 18.2).

<!-- chunk {"id": "body-0972", "role": "body", "section": "Convex functions", "weight": 1.0} -->

A convex function is a function such that its value on the average of two or more points is smaller than the average of the values of the functions at these points. This is illustrated in Figure 15.2 and formalized below.

<!-- chunk {"id": "body-0973", "role": "body", "section": "Convex functions", "weight": 1.0} -->

Definition 15.5 (Convex functions). A function L: W → R is said to be convex if for all w, v ∈ W and τ ∈ The function L is strictly convex if the above inequality is strict for all w = v.

<!-- chunk {"id": "body-0974", "role": "body", "section": "Convex functions", "weight": 1.0} -->

The above characterization can easily be generalized to multiple points. Namely, for w 1,..., w n ∈ W and τ 1,... τ n ≥ 0 such that ∑ n i =1 τ i = 1 (that is, τ 1,..., τ n defines a probability distribution over [n]), we have if L is convex that The point ∑ n i =1 τ i w i is called a convex combination. This can be seen as comparing the function at the average point to the average of the values at theses points and can further be generalized to any random variable.

<!-- chunk {"id": "body-0975", "role": "body", "section": "Convex functions", "weight": 1.0} -->

Proposition 15.3 (Jensen's inequality). A function L: W → R is convex if it satisfies Jensen's inequality, that is, for any random variable W on W, provided that the expectations are well-defined.

<!-- chunk {"id": "body-0976", "role": "body", "section": "Convex functions", "weight": 1.0} -->

If the function considered is differentiable, an alternative characterization of convexity is to observe how linear approximations of the function lower bound the function. This is illustrated in Figure 15.2 and formalized below.

<!-- chunk {"id": "body-0977", "role": "body", "section": "Convex functions", "weight": 1.0} -->

Definition 15.6 (Convex differentiable functions). Adifferentiable function L: W → R is convex if and only if for all w, v ∈ W The function L is strictly convex if and only if the above inequality is strict for any w = v.

<!-- chunk {"id": "body-0978", "role": "body", "section": "Convex functions", "weight": 1.0} -->

The above characterization pinpoints the relevance of convex function in optimization: if we can find a point ˆ w with null gradient, then we know that we have found the minimum as we have This means that by having access to the gradient of the function or an approximation thereof, we have access to a sufficient criterion to know whether we found a global minimum. In the case of a gradient descent on a smooth function, convexity ensures convergence to a minimum at a sublinear rate as detailed below.

<!-- chunk {"id": "body-0979", "role": "body", "section": "Convex functions", "weight": 1.0} -->

Finally, if the function is twice differentiable, convexity of a function can be characterized in terms of the Hessian of the function.

<!-- chunk {"id": "body-0980", "role": "body", "section": "Convex functions", "weight": 1.0} -->

Proposition 15.4 (Convex twice differentiable functions). Atwice differentiable function L: W → R is convex if and only if its Hessian is positive semi-definite, The function L is strictly convex if and only if the Hessian is positivedefinite, ∀ w ∈ W, ∇ 2 L (w) ≻ 0, i.e., ∀ w, v ∈ W, 〈 v, ∇ 2 L (w) v 〉 > 0.

<!-- chunk {"id": "body-0981", "role": "body", "section": "Strongly-convex functions", "weight": 1.0} -->

Convexity can also be strengthened by considering µ -strongly convex functions.

<!-- chunk {"id": "body-0982", "role": "body", "section": "Strongly-convex functions", "weight": 1.0} -->

Definition 15.7 (Strongly-convex functions). A function L: W → R is µ -strongly convex for µ > 0 if for all w, v ∈ W and τ ∈ A differentiable function L is µ -strongly convex if and only if for all w, v ∈ W A twice differentiable function is µ -strongly convex if and only if its Hessian satisfies The characterization of strong convexity for differentiable functions states that L (w) is lower-bounded by a quadratic. This enables the design of linearly convergent algorithms as explained later. We naturally have the implications L strongly convex = ⇒ L strictly convex = ⇒ L convex.

<!-- chunk {"id": "body-0983", "role": "body", "section": "With respect to arbitrary norms", "weight": 1.0} -->

A function can be strongly convex w.r.t. an arbitrary norm, simply by replacing the 2-norm in Definition 15.7 with that norm. For differentiable strongly convex functions, we have the following alternative characterization, generalizing Definition 15.7 to arbitrary norms.

<!-- chunk {"id": "body-0984", "role": "body", "section": "With respect to arbitrary norms", "weight": 1.0} -->

Proposition 15.5 (Differentiable strongly-convex functions). If a differentiable function L: W → R is µ -strongly convex w.r.t. a norm ‖ · ‖ over a set C, then for all w, v ∈ C Obviously, if a function L is µ -strongly convex, then, λL is (µλ)-strongly convex. Because all norms are equivalent, if a function is strongly convex w.r.t. a norm, it is also strongly-convex w.r.t. another norm. However, stating the norm w.r.t. which strong convexity holds can lead to better constant µ (the higher, the better in terms of convergence rates of, e.g., a gradient descent). We also emphasize that it is important to mention over which set strong convexity holds. We give examples below.

<!-- chunk {"id": "body-0985", "role": "body", "section": "With respect to arbitrary norms", "weight": 1.0} -->

Example 15.1 (Strongly convex functions). The function f ( u ) = 1 2 ‖ u ‖ 2 2 is 1-strongly convex w.r.t. ‖ · ‖ 2 over R M.

<!-- chunk {"id": "body-0986", "role": "body", "section": "With respect to arbitrary norms", "weight": 1.0} -->

The function f (u) = 〈 u, log u 〉 is 1-strongly convex w.r.t. ‖ · ‖ 1 over △ M. Applying Proposition 15.5, we obtain for all p, q ∈ △ M which is known as Pinsker's inequality. We empirically verify the inequality in Fig. 15.1.

<!-- chunk {"id": "body-0987", "role": "body", "section": "With respect to arbitrary norms", "weight": 1.0} -->

More generally, f ( u ) is 1 µ -strongly convex w.r.t. ‖ · ‖ 1 over any bounded set C ⊂ R M + such that µ = sup u ∈C ‖ u ‖ 1. However, it is not strongly convex over R M +, as it is not bounded.

<!-- chunk {"id": "body-0988", "role": "body", "section": "Nonconvex functions", "weight": 1.0} -->

In general, the minimum of a function necessarily has a null gradient, that is, Figure 15.1: Graphical verification of Pinsker's inequality, 1 2 ‖ p -q ‖ 2 1 ≤ KL(p, q), with p:= (π, 1 -π) and q:= (0. 3, 0. 7).

<!-- chunk {"id": "body-0989", "role": "body", "section": "Nonconvex functions", "weight": 1.0} -->

To see this, consider the function F: t → L ( w ⋆ -t ∇ L ( w ∗ )). If ∇ L ( w ⋆ ) = 0, then F ′ = -‖∇ L ( w ⋆ ) ‖ 2 2 = 0. Therefore, there exists a small t > 0 such that F ( t ) < F, i.e., L ( w ⋆ ) is not the minimum. However, if the function is not convex, the converse is a priori not true: finding a point that has a null gradient does not ensure that we have found a global minimum as illustrated in Figure 15.3.

<!-- chunk {"id": "body-0990", "role": "body", "section": "Nonconvex functions", "weight": 1.0} -->

For non-convex functions, a point with null gradient is called a stationary point. A stationary point may define a local maximum or a local minimum. Formally, ˆ w is a local minimum if A local maximum is defined similarly, except that L (v) ≤ L (ˆ w) in a neighborhood of ˆ w. For non-convex functions, convergence rates are therefore generally expressed in terms of convergence of the norm of the gradient ‖∇ f (w t) ‖ 2 towards 0. Such theoretical results do not ensure convergence to the global minimum but rather convergence to a point where no further progress may a priori be possible with just gradient information.

<!-- chunk {"id": "body-0991", "role": "body", "section": "Performance guarantees", "weight": 1.0} -->

For a given class of functions, we can define the performance of an algorithm as the number of iterations the algorithm would need to find an ε -accurate solution as in Eq. (15.1). This is called the computational complexity of the algorithm, denoted Alternatively, the performance of an algorithm can be stated in terms of convergence rate, i.e., the accuracy that the algorithm reaches after t iterations, where R is a decreasing positive function vanishing as t → + ∞. Usually, R incorporates properties of the function minimized, such as its smoothness constant β and information on the initial point, such as its function value. The corresponding computational complexity T (ε) is then given as the minimum number of iterations t such that R (t) ≤ ε, Convergence rates can generally be classified by considering the progress ratio on iteration t, defined by Figure 15.3: Non-convex function: a point with zero gradient is not necessarily the global minimum.

<!-- chunk {"id": "body-0992", "role": "body", "section": "Performance guarantees", "weight": 1.0} -->

The asymptotic convergence rate is then defined by We can classify the rates as follows. 2. Linear convergence rates, ρ ∞ = c ∈: the algorithm eventually reaches a state of constant relative progress at each iteration, leading to an overall rate R (t) = O (exp(-ct)) for c depending on the properties of the objective. This corresponds to T (ε) = O (c -1 ln ε -1). 1. Sublinear convergence rates, ρ ∞ = 1: the longer the algorithm runs, the slower it makes progress. That is, the relative progress eventually tends to stall as t → + ∞. Examples of R (t) in this category include O (1 /t), O (1 /t 2) or more generally O (1 /t α) for some α > 0. This is equivalent to T (ε) = O (ε -1 /α). 3. Superlinear convergence rates, ρ ∞ = 0: the relative progress is better at each new iteration.

<!-- chunk {"id": "body-0993", "role": "body", "section": "Performance guarantees", "weight": 1.0} -->

This can happen, e.g., R (t) = O (exp(-t 2)), leading to T (ε) = O (√ ln ε -1) or = (exp(exp)), also called a quadratic rate, leading to This is illustrated in Fig. 15.4.

<!-- chunk {"id": "body-0994", "role": "body", "section": "Performance guarantees", "weight": 1.0} -->

Note that the term 'linear' may be misleading as the rates are in fact exponential. They are called 'linear' because of their behavior in log scale.

<!-- chunk {"id": "body-0995", "role": "body", "section": "Upper and lower bounds", "weight": 1.0} -->

The best performance of a class of algorithms equipped with a given oracle (e.g. first-order oracle) can be upper-bounded or lower-bounded. This allows to show that an algorithm with access limited to a certain type of oracle cannot theoretically do better than a certain number. For example, the computational complexity to minimize β -smooth functions restricted on P with first-order oracles is lower bounded by c ε P. For example, with P = 10 and ε = 10 -3, this gives 10 30 iterations. Note that these results are pessimistic by construction. The actual performance of an algorithm on a specific instance of this function class may be much better than this worst-case scenario, as it is the case with popular algorithms such as quasi-Newton methods. Better computational complexities can be achieved by further restricting the class of functions to the set of convex functions, which play a central role in optimization and many other fields.

<!-- chunk {"id": "body-0996", "role": "body", "section": "Zero-order vs. first-order", "weight": 1.0} -->

For the class of smooth strongly convex functions, the computational complexity of the best first-order algorithm is (up to constant and logarithmic factors) P times better than that of the best zero-order algorithm. This theoretical comparison shows that, while zero-order optimization algorithms may perform on par with first-order optimization algorithms for problems with a low dimension P, they can be much slower for high dimensional problems, i.e., P ≫ 1.

<!-- chunk {"id": "body-0997", "role": "body", "section": "Zero-order vs. first-order", "weight": 1.0} -->

In different settings, for example with stochastic oracles or for different classes of functions, slightly different comparisons may be achieved, such as a √ P factor instead of P. However, the same conclusion holds in the current frameworks considered: firstorder optimization algorithms can provide fast rates that are dimension independent while the rates of zero-order optimization algorithms gen- erally depend on the dimension of the problem, making them unfit for high-dimensional problems.

<!-- chunk {"id": "body-0998", "role": "body", "section": "Zero-order vs. first-order", "weight": 1.0} -->

This explains the immense success of first-order algorithms for training neural networks. Fortunately, using reverse-mode autodiff, as studied in Chapter 8, it can be shown that computing a gradient has roughly the same complexity as evaluating the function itself Section 8.3.3

<!-- chunk {"id": "body-0999", "role": "body", "section": "Summary", "weight": 1.0} -->

- The information available to us on a function can be formalized by the notion of oracle. Zero-order oracles can only evaluate the function; first-order oracles can also compute the gradient; secondorder oracles can also compute the Hessian or the Hessian-vector product (HVP). - Most optimization algorithms reviewed in this book can be viewed from a variational perspective, in which the next iteration is produced by optimizing a trade-off between an approximation of the function and a proximity term. Different approximations and different proximity terms lead to different algorithms. - We also reviewed different classes of functions, and performance guarantees.

<!-- chunk {"id": "body-1000", "role": "body", "section": "Gradient descent", "weight": 1.0} -->

Gradient descent is one of the simplest algorithms in our toolbox to minimize a function. At each iteration, it moves along the negative gradient direction, scaled by a stepsize γ: The path taken by a gradient descent on a simple quadratic is illustrated in Fig. 16.1 for different choices of the stepsize.

<!-- chunk {"id": "body-1001", "role": "body", "section": "Variational perspective", "weight": 1.0} -->

Consider the linear approximation of L (w) around w t, One can easily check that the gradient descent update in Eq. (16.1) can be rewritten as the solution of a minimization problem, namely, In words, a gradient descent update optimizes a trade-off between staying close to the current w t, thanks to the proximity term 1 2 γ ‖ w -w t ‖ 2 2, and minimizing the linearization of L around w t. Intuitively, by choosing γ sufficiently small, we ensure that the minimizer of the regularized linear approximation stays in a neighborhood where the linear approximation is valid. This viewpoint is useful to motivate gradient descent extensions.

<!-- chunk {"id": "body-1002", "role": "body", "section": "Convergence for smooth functions", "weight": 1.0} -->

As long as ∇ L (w t) = 0, the function L t (γ):= L (w t -γ ∇ L (w t)) has a negative derivative at 0, i.e., L ′ t = -‖∇ L (w t) ‖ 2 2. Hence, as long as ∇ L (w t) = 0, there exists a stepsize ensuring a decrease in objective values at each iterate. However, without further assumptions, such a stepsize may depend on each iterate and may be infinitesimally small. To quantify the convergence of gradient descent with a constant stepsize, we restrict to the class of smooth functions. By applying Proposition 15.1 on the iterate of gradient descent, we obtain that Therefore, for β -smooth functions, by selecting γ ≤ 1 β, we get that which illustrates the main mechanism behind gradient descent: each iteration decreases the objective by a constant times the norm of the gradient of the current iterate.

<!-- chunk {"id": "body-1003", "role": "body", "section": "Convergence for smooth functions", "weight": 1.0} -->

This equation can further be summed over all iterates up to T. This telescopes the objective values, leading to where we recall that L ⋆ is the infimum of L. Therefore, after sufficiently many iterations, gradient descent finds a point whose gradient norm is arbitrarily small.

<!-- chunk {"id": "body-1004", "role": "body", "section": "Non-convex case", "weight": 1.0} -->

Without further assumptions, i.e., in the non-convex case, the above result (i.e., convergence to a stationary point, measured by the gradient norm) is the best we may get in theory. Denoting T s ( ε ) the number of iterations needed for a gradient descent to output a point that is ε -stationary, i.e., ‖∇ L ( ˆ w ) ‖ 2 ≤ ε, we have T s ( ε ) ≤ O ( ε -2 ).

<!-- chunk {"id": "body-1005", "role": "body", "section": "Convex case", "weight": 1.0} -->

By adding a convexity assumption on the objective, we can use the lower bound provided by the convexity assumption to ensure convergence to a minimum. Namely, for a β -smooth and convex function f, and with stepsize γ ≤ 1 /β, we have that That is, we get a sublinear convergence rate, and the associated computational complexity to find a minimum is T (ε) = O (1 /ε).

<!-- chunk {"id": "body-1006", "role": "body", "section": "Strongly convex case", "weight": 1.0} -->

If we further strengthen the assumptions by considering β -smooth, µ -strongly convex functions, the convergence rate of a gradient descent can be shown to be, for any stepsize γ ≤ 1 /β, That is, we obtain a linear convergence rate and the associated computational complexity is T (ε) = O (ln ε -1). The above convergence rates may be further refined; we focused above on the simplest result for clarity.

<!-- chunk {"id": "body-1007", "role": "body", "section": "Strongly convex case", "weight": 1.0} -->

Strong convexity can also be replaced by a weaker assumption, gradient-dominating property, i.e., ‖∇ L ( v ) ‖ 2 2 ≥ c ( L ( v ) -L ⋆ ) for some constant c and any v ∈ W. A convex, gradient-dominating function can also be minimized at a linear rate.

<!-- chunk {"id": "body-1008", "role": "body", "section": "Momentum and accelerated variants", "weight": 1.0} -->

We started with gradient descent as a simple example of first-order optimization algorithm. However, different optimization algorithms can be designed from the access to first-order oracles and the knowledge of the class of functions considered. For example, consider quadratic convex functions w ↦→ 1 2 w ⊤ Aw + b ⊤ w, that are a basic example of smooth strongly convex functions if A is positive definite. An optimal method in this case is the heavy-ball method of Polyak, that can be written as The heavy-ball method uses an additional variable v t, that can be interpreted as the velocity of a ball driven by the negative gradient to converge towards a minimum. Intuitively, this additional velocity circumvents the oscillations that a gradient descent may present as illustrated in Fig. 16.2 compared to Fig. 16.1. For ν = 0, we recover usual gradient descent. For ν > 0, the velocities accumulate a form of an inertia momentum, where ν is interpreted as the 'mass' of the ball.

<!-- chunk {"id": "body-1009", "role": "body", "section": "Momentum and accelerated variants", "weight": 1.0} -->

In terms of convergence rates, the heavy-ball method can be shown to converge linearly similarly to gradient descent, but with a rate O (exp(-T √ µ/β)) for appropriate choices of ν, γ. In comparison, by choosing an optimal stepsize for the gradient descent, its convergence rate is O (exp(-Tµ/β)) which is provably worse, as we always have µ/β ≤ 1.

<!-- chunk {"id": "body-1010", "role": "body", "section": "Momentum and accelerated variants", "weight": 1.0} -->

Beyond the case of quadratic functions, accelerated variants of gradient descent for convex or strongly convex functions have been developed by Nesterov. Such variants have inspired the design of optimization algorithms in stochastic settings presented below.

<!-- chunk {"id": "body-1011", "role": "body", "section": "Stochastic gradient descent", "weight": 1.0} -->

In machine learning, we are usually interested in minimizing the expected loss of the model over the data distribution ρ: For example, L is often set to L (w; S):= ℓ (Y, f (X, w)), where ℓ is a loss function, f is a neural network and S = (X,Y) is a random pair, composed of an input X and an associated target Y, sampled from ρ. In this setting, since the data distribution ρ is generally unknown and may be infinite, we cannot exactly evaluate the expected loss L (w) or its gradient ∇ L (w).

<!-- chunk {"id": "body-1012", "role": "body", "section": "Stochastic gradient descent", "weight": 1.0} -->

In practice, we are often given a fixed dataset of n pairs s i = (x i, y i). This is a special case of the expected loss setting, since this can be seen as a empirical distribution ρ = ρ n The gradient of L (w) is then In this case, we see that the full gradient ∇ L (w), as needed by gradient descent, is the average of the individual gradients. That is, the cost of computing ∇ L (w) is proportional to the number of training points n. For n very large, that is a very large amount of samples, this computational cost can be prohibitive. Stochastic gradients circumvent this issue.

<!-- chunk {"id": "body-1013", "role": "body", "section": "Stochastic gradients", "weight": 1.0} -->

Usually, even if we do not know ρ, we can sample from it, i.e., we have access to samples S ∼ ρ. We can then use a stochastic gradient of the form ∇ L (w; S) as a random estimate of ∇ L (w). This may look like a rough estimate but, on average, this is a valid approximation since We say that ∇ L (w; S) is an unbiased estimator of ∇ L (w). To further improve the approximation, we may also consider mini-batch estimates by sampling m ≪ n data points S i:= (X i, Y i) and using 1 m ∑ m i =1 ∇ L (w; S i), whose expectation still matches ∇ L (w), while potentially reducing the approximation error by averaging multiple stochastic gradients. Computationally, the main advantage is that the cost is now proportional to m instead of n.

<!-- chunk {"id": "body-1014", "role": "body", "section": "Stochastic gradients", "weight": 1.0} -->

In whole generality, one can consider stochastic first-order oracles defined below.

<!-- chunk {"id": "body-1015", "role": "body", "section": "Stochastic gradients", "weight": 1.0} -->

Definition 16.1 (Stochastic first-order oracles). A stochastic firstorder oracle of an expected objective L (w) is a random estimate g (w; S) of ∇ L (w) with S sampled according to some distribution q. A stochastic gradient is said to be an unbiased estimator if The variance of a stochastic gradient is When q = ρ, we recover stochastic gradients. When q is the product of m independent samples according to p, we recover mini-batch stochastic gradients. First-order stochastic optimization algorithms build upon stochastic first-order oracles to approximately find the minimum of the expected objective. In such a setting, the iterates of the algorithm are by definition random. Convergence rates therefore need to be expressed in probabilistic terms by considering for example the expected objective value according to the randomness of the oracles.

<!-- chunk {"id": "body-1016", "role": "body", "section": "Vanilla SGD", "weight": 1.0} -->

Equipped with a stochastic first-order oracle, such as (mini-batch) stochastic gradients, we can define stochastic gradient descent as We assume that S t is independent of w t. Compared to the usual gradient descent, the main impediment of the stochastic setting is the additional noise induced by the stochastic estimates: their variance.

<!-- chunk {"id": "body-1017", "role": "body", "section": "Vanilla SGD", "weight": 1.0} -->

For example, consider applying a stochastic gradient descent on the expectation of β -smooth convex functions L (w; s) with unbiased oracles. To harness the randomness of the iterates, consider after T iterations outputting the average of the first T iterates, that is ¯ w T:= 1 T ∑ T t =1 w t. Moreover, suppose that the variance of the stochastic first-order oracles is bounded by σ 2 for all minimizers w ⋆ of L. Denoting by E S 0,...,S T -1 the randomness associated to the stochastic oracles, we have then that for a stepsize γ ≤ 1 / (4 β) The resulting convergence rate illustrates that a stochastic gradient descent converges to the minimum of the expected objective up to a constant term depending on the variance of the oracle and the stepsize. One can diminish the variance by considering mini-batches: if the variance of a single stochastic gradient is σ 2 1, considering a mini-batch of m gradients reduces the variance of the corresponding oracle to σ m = σ 2 1 /m.

<!-- chunk {"id": "body-1018", "role": "body", "section": "Vanilla SGD", "weight": 1.0} -->

To decrease the additional term, one may also decrease the stepsizes over the iterations. For example, by choosing a decreasing stepsize like γ t = t -1 / 2, the convergence rate is then of the order O ((‖ w 0 -w ⋆ ‖ 2 2 + σ 2 ln t) / √ (t)). The stepsize can also be selected as a constant γ 0 that decreases the average objective for the first T 0 iterations and reduced by a multiplicative factor at regular intervals like γ j = ργ j -1 for ρ ∈ to handle iterations between T j, T j +1. Alternative stepsize schedules such as a cosine decay have recently become popular.

<!-- chunk {"id": "body-1019", "role": "body", "section": "Vanilla SGD", "weight": 1.0} -->

The literature on alternative optimization schemes for stochastic optimization is still rapidly evolving, with new heuristics regularly proposed. We present below two popular techniques.

<!-- chunk {"id": "body-1020", "role": "body", "section": "Momentum variants", "weight": 1.0} -->

Accelerated optimization algorithms developed in the deterministic setting may be extended to the stochastic setting. For example, the heavy-ball method can be adapted to the stochastic setting, leading to stochastic gradient descent with momentum generally implemented as As mentioned earlier the momentum method can be modified to handle non-quadratic smooth strongly convex functions. This leads to Nesterov's accelerated method in the deterministic setting. This has been adapted to the stochastic with a so-called Nesterov momentum

<!-- chunk {"id": "body-1021", "role": "body", "section": "Adaptive variants", "weight": 1.0} -->

In any gradient descent-like algorithm, selecting the stepsize is key for good performance. While a constant stepsize may be used if the function is smooth, we may not know in advance the smoothness constant of the objective, which means that additional procedures may be required to select appropriately the stepsize. In the deterministic case, line-searches such as the Armijo or Wolfe's rules can be used to check whether the selected stepsize decreases sufficiently the objective at each iteration. Such rules have be adapted in the stochastic setting.

<!-- chunk {"id": "body-1022", "role": "body", "section": "Adaptive variants", "weight": 1.0} -->

Another way to decrease the sensitivity of the algorithm with respect to the stepsize has been to estimate first and second-order moments of the gradients and use the latter as a form of preconditioning to smooth the trajectory of the iterates. This led to the popular Adam optimizer. It takes the form, where g t:= g (w t; S t), (g t) 2 denotes the element-wise square of g t and ν 1, ν 2, γ, ε are hyper-parameters of the algorithm. Numerous variants exist, such as varying the stepsize γ above along the iterations.

<!-- chunk {"id": "body-1023", "role": "body", "section": "Projected gradient descent", "weight": 1.0} -->

Oftentimes, we seek to find the solution of a minimization problem subject to constraints on the variables, of the form where C ⊆ W = R P is a set of constraints. We say that an approximate solution ̂ w to Eq. (16.3) is feasible if ̂ w ∈ C. Naturally, the design of algorithms for the constrained setting now depends, not only on information about L, but also on information about C.

<!-- chunk {"id": "body-1024", "role": "body", "section": "Projected gradient descent", "weight": 1.0} -->

Similarly to L, different oracles can be considered about C. One of the most commonly used oracle is the Euclidean projection Definition 16.2 (Euclidean projection). The Euclidean projection onto the set C is defined by This projection, which is well-defined when C is a convex set, can be used in projected gradient descent, that we briefly review below. Typically, the projection on a particular set C requires a dedicated algorithm to compute it.

<!-- chunk {"id": "body-1025", "role": "body", "section": "Projected gradient descent", "weight": 1.0} -->

Other possible oracles are linear maximization oracles (LMO) used in Frank-Wolfe algorithms and Bregman projection oracles, used in mirror descent algorithms. The algorithm choice can be dictated by what oracle about C is available.

<!-- chunk {"id": "body-1026", "role": "body", "section": "Variational perspective", "weight": 1.0} -->

Projected gradient descent is a natural generalization of gradient descent, based on the Euclidean projection oracle. Its iterates read At each iteration, we attempt to decrease the objective by moving along the negative gradient direction, while ensuring that the next iterate remains feasible, thanks to the projection step.

<!-- chunk {"id": "body-1027", "role": "body", "section": "Variational perspective", "weight": 1.0} -->

Similarly to the variational perspective of gradient descent in Eq. (16.2), the projected gradient descent update is equivalent to This shows that projected gradient descent minimizes a trade-off between staying close to w t and minimizing the linearization of L around w t, while staying in C.

<!-- chunk {"id": "body-1028", "role": "body", "section": "Variational perspective", "weight": 1.0} -->

In terms of convergence rates, they remain the same as gradient descent. For example, projected gradient descent on a smooth convex function still converges at a rate R ( T ) = O (1 /T ).

<!-- chunk {"id": "body-1029", "role": "body", "section": "Variational perspective", "weight": 1.0} -->

There are numerous extensions of vanilla projected gradient descent. Similarly to gradient descent, the stepsize can be automatically adjusted using linesearch techniques and there exists accelerated variants. If we replace ∇ L ( w ) with a stochastic gradient ∇ L ( w; S ), we obtain a stochastic projected gradient descent.

<!-- chunk {"id": "body-1030", "role": "body", "section": "Optimality conditions", "weight": 1.0} -->

In the unconstrained case, a minimum necessarily has a zero gradient. In the constrained setting, there may not be any feasible parameters with zero gradient. Instead, the optimality of a point is characterized by the fact that no better solution can be found by moving along the gradient at that point, while staying in the constraints. Formally, it means that for any γ > 0, a minimizer w ⋆ of L on C satisfies It can be shown that this condition is equivalent to

<!-- chunk {"id": "body-1031", "role": "body", "section": "Commonly-used projections", "weight": 1.0} -->

We now briefly review a few useful Euclidean projections.

<!-- chunk {"id": "body-1032", "role": "body", "section": "Commonly-used projections", "weight": 1.0} -->

Therefore, in the unconstrained setting, projected gradient descent indeed recovers gradient descent.

<!-- chunk {"id": "body-1033", "role": "body", "section": "Commonly-used projections", "weight": 1.0} -->

- If C = [a, b] P (box constraints), we have where the min and max are applied coordinate-wise.

<!-- chunk {"id": "body-1034", "role": "body", "section": "Commonly-used projections", "weight": 1.0} -->

- As a special case of the above, if C = R P + (non-negative orthant), also known as non-negative part or ReLu.

<!-- chunk {"id": "body-1035", "role": "body", "section": "Commonly-used projections", "weight": 1.0} -->

- If C = △ P (unit probability simplex), where τ ∈ R is a constant ensuring that proj C (w) normalizes to 1. It is known that τ can be found in O (P log P) using a sort. This can be improved to O (P) using a median-finding like algorithm.

<!-- chunk {"id": "body-1036", "role": "body", "section": "Proximal gradient method", "weight": 1.0} -->

The constrained setting (with C a convex set) can be recast as unconstrained optimization, by extending our analysis to functions taking infinite values. Let us denote the indicator function of the set C by Clearly, the constrained problem in Eq. (16.3) can then be rewritten as This suggests that constrained optimization is a special case of composite objectives of the form where Ω is a convex but potentially non-differentiable function. We assume that we have access to an oracle associated with Ω called the proximal operator.

<!-- chunk {"id": "body-1037", "role": "body", "section": "Proximal gradient method", "weight": 1.0} -->

Definition 16.3 (Proximal operator). The proximal operator associated with Ω: W → R is This leads to the proximal gradient method, reviewed below.

<!-- chunk {"id": "body-1038", "role": "body", "section": "Variational perspective", "weight": 1.0} -->

With this method, the update reads This update again enjoys an intuitive variational perspective, namely, That is, we linearize L around w t, but keep Ω as is.

<!-- chunk {"id": "body-1039", "role": "body", "section": "Variational perspective", "weight": 1.0} -->

Convergence guarantees of the proximal gradient method remain the same as for gradient descent, such as a O (1 /T ) rate for smooth convex functions.

<!-- chunk {"id": "body-1040", "role": "body", "section": "Variational perspective", "weight": 1.0} -->

The proximal gradient method is popularly used when the objective function contains a sparsity-inducing regularizer Ω. For example, for the LASSO, which aims at predicting targets y = ( y 1,..., y n ) ⊤ ∈ R N from observations X = ( x 1,..., x n ) ⊤ ∈ R N × P, we set L ( w ) = 1 2 ‖ Xw -y ‖ 2 2 and Ω( w ) = λ ‖ w ‖ 1, where λ > 0 controls the regularization strength. In this case, prox Ω is the so-called softthresholding operator (see below).

<!-- chunk {"id": "body-1041", "role": "body", "section": "Optimality conditions", "weight": 1.0} -->

An optimal solution of the problem is characterized by the fixed point equation for all γ > 0. In other words, the proximal gradient method (which includes gradient descent and projected gradient descent as special cases), can be seen as fixed point iteration schemes. Such a viewpoint suggests using acceleration methods from the fixed point literature such as Anderson acceleration. It is also useful when designing implicit differentiation schemes as presented in Chapter 8.

<!-- chunk {"id": "body-1042", "role": "body", "section": "Commonly-used proximal operators", "weight": 1.0} -->

We now briefly review a few useful proximal operators.

<!-- chunk {"id": "body-1043", "role": "body", "section": "Commonly-used proximal operators", "weight": 1.0} -->

Therefore, with this proximal operator, the proximal gradient method recovers gradient descent.

<!-- chunk {"id": "body-1044", "role": "body", "section": "Commonly-used proximal operators", "weight": 1.0} -->

Therefore, with this proximal operator, the proximal gradient method recovers projected gradient descent. where the operations are applied coordinate-wise. This is the so-called soft-thresholding operator.

<!-- chunk {"id": "body-1045", "role": "body", "section": "Commonly-used proximal operators", "weight": 1.0} -->

- Ω(w) = λ ∑ g ∈ G ‖ w g ‖ 2 where G is a partition of [P] and w g denotes the subvector restricted to g, then we have which is used in the group lasso and can be used to encourage group sparsity.

<!-- chunk {"id": "body-1046", "role": "body", "section": "Commonly-used proximal operators", "weight": 1.0} -->

For a review of more proximal operators, see for instance.

<!-- chunk {"id": "body-1047", "role": "body", "section": "Summary", "weight": 1.0} -->

- From a variational perspective, gradient descent is the algorithm obtained when linearizing the objective function and using a quadratic regularization term.

<!-- chunk {"id": "body-1048", "role": "body", "section": "Summary", "weight": 1.0} -->

- Projected gradient descent is the algorithm obtained when there is an additional constraint (the Euclidean projection naturally appearing, due to the quadratic regularization term). - When the objective is the sum of a differentiable function and a non-differentiable function, proximal gradient is the algorithm obtained when the differentiable function is linearized but the non-differentiable function is kept as is. - We also reviewed various stochastic gradient based algorithms, including vanilla SGD, SGD with momentum and Adam.

<!-- chunk {"id": "body-1049", "role": "body", "section": "Second-order optimization", "weight": 1.0} -->

We review in this chapter methods whose iterations take the form where γ t is a stepsize and B t is a pre-conditioning matrix involving second-order derivatives.

<!-- chunk {"id": "body-1050", "role": "body", "section": "Variational perspective", "weight": 1.0} -->

We saw in Eq. (16.2) that gradient descent can be motivated from a variational perspective, in which we use a linear approximation of the objective around the current iterate, obtained from the current gradient. Similarly, if we have access not only to the gradient but also to the Hessian of the objective, we can use a quadratic approximation of the objective around the current iterate. More precisely, given a function L (w), we may consider minimizing the second-order Taylor approximation of L (w) around the current iterate w t, Newton's method simply iteratively minimizes this quadratic approximation around the current iteration w t, namely, If the Hessian is positive definite at w t, which we denote by ∇ 2 L (w t) ≻ 0, then the minimum is well-defined and unique (this is for example the case if L is strictly convex). The iterates can then be written analytically as If the Hessian is not positive definite, the minimum may not be defined.

<!-- chunk {"id": "body-1051", "role": "body", "section": "Variational perspective", "weight": 1.0} -->

Ignoring this issue and taking the analytical formulation could be dangerous, as it could amount to computing the maximum of the quadratic instead if, for example, the quadratic was strictly concave (i.e., ∇ 2 L (w) ≺ 0).

<!-- chunk {"id": "body-1052", "role": "body", "section": "Regularized Newton method", "weight": 1.0} -->

A simple technique to circumvent this issue consists in adding a regularization term to the Hessian. Namely, from a variational viewpoint, we can add a proximity term 1 2 ‖ w -w t ‖ 2 2, encouraging to stay close to the current w t. The iterates of this regularized Newton method then take the form where η t controls the regularization strength. Assuming η t > 0 is strong enough to make ∇ 2 L (w t) + η t I positive-definite, we have where we defined the direction Other techniques to circumvent this issue include using cubic regularization and modifying the spectral decomposition of the Hessian, by thresholding the eigenvalues or taking their absolute values. We refer the interested reader to, e.g., for more details.

<!-- chunk {"id": "body-1053", "role": "body", "section": "Approximate direction", "weight": 1.0} -->

We observe a main impediment for implementing such a second-order optimization algorithm: even if we had access to the Hessian of the objective for free and this Hessian was positive definite, computing the exact direction d t in Eq. (17.2) requires computing an inverse-Hessian vector product (IHVP) with the gradient ∇ L (w t). Doing so exactly requires solving a linear system which a priori takes O (P 3) time. In practice, however, we can compute IHVPs approximately, as explained in Section 9.4.

<!-- chunk {"id": "body-1054", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

While implementing Newton's method comes at a higher computational cost, it can also benefit from faster convergence rates. Briefly, if Newton's method is initialized at a point w 0 ∈ W close enough from the minimizer w ⋆ of a µ -strongly convex function with M -Lipschitz continuous Hessian (namely ‖ w 0 -w ∗ ‖ 2 ≤ 2 µ 3 M ), then Newton's method converges at a quadratic rate, that is, R ( t ) ≤ O (exp(exp( -t )) (see Section 15.5 for a brief introduction to performance guarantees). This is far superior to gradient descent. Such an efficiency motivated the development of interior point methods, that have been a breakthrough in constrained optimization, thanks to the use of log-barrier penalties.

<!-- chunk {"id": "body-1055", "role": "body", "section": "Linesearch", "weight": 1.0} -->

In practice, we may not have access to an initial point close enough from the minimizer. In that case, even for strictly convex functions for which Newton's steps are well-defined, taking w t +1 = w t -d t may not ensure a decrease of the objective values. Nevertheless, the direction d t may define a descent direction as defined below.

<!-- chunk {"id": "body-1056", "role": "body", "section": "Linesearch", "weight": 1.0} -->

Definition 17.1 (Descent direction). A point d ∈ W defines a descent direction -d for an objective L at w, if there exists a positive stepsize γ > 0 such that If L is differentiable, -d is a descent direction if 〈-d, ∇ L (w) 〉 < 0.

<!-- chunk {"id": "body-1057", "role": "body", "section": "Linesearch", "weight": 1.0} -->

For Newton's method without regularization, d t = ∇ 2 L (w t) -1 ∇ L (w t) is then a descent direction at w t, as long as ∇ L (w t) = 0 and ∇ 2 L (w t) ≻ 0. If ∇ 2 L (w t) ̸≻ 0, choosing η t > 0 such that ∇ 2 L (w t) + η t I ≻ 0, also ensures that d t = -(∇ 2 L (w t) + η t I) -1 ∇ L (w t) is a descent direction (as long as ∇ L (w t) = 0).

<!-- chunk {"id": "body-1058", "role": "body", "section": "Linesearch", "weight": 1.0} -->

Newton's method is then generally equipped with a linesearch method that attempts to take steps of the form x with γ t chosen as the largest stepsize among { ρ τ, τ ∈ N } for ρ ∈ until a sufficient decrease of the objective is satisfied such as, for c ∈, For strongly convex functions, such an implementation exhibits two phases: a first phase during which Newton's steps are 'damped' by using a stepsize γ t < 1 and a second phase of super-fast convergence during which stepsizes γ t = 1 are taken, and the objective decreases very fast. Even far from the optimum, Newton directions can advantageously adapt to the local geometry of the objective to speed-up convergence compared to a regular gradient descent as explained below.

<!-- chunk {"id": "body-1059", "role": "body", "section": "Geometric interpretation", "weight": 1.0} -->

To understand the efficiency of Newton's method compared to gradient descent, consider the minimization of a simple quadratic for a ≫ b ≥ 0, as illustrated in Fig. 17.1. A gradient descent moves along the directions ∇ L (w) = (aw 1, bw 2) ⊤ and its stepsize is limited by the variations in the first coordinate leading to some oscillations. If we were simply rescaling the gradient by (a, b), i.e., taking steps of the form the variations in both coordinates would be normalized to one and the stepsize could simply be chosen to γ = 1 to directly get w ⋆. In other words, by adapting the geometry of the directions with the geometry induced by the objective, we can circumvent the oscillations.

<!-- chunk {"id": "body-1060", "role": "body", "section": "Geometric interpretation", "weight": 1.0} -->

That's exactly what Newton's method does by modifying the gradient direction using the inverse of the Hessian. Formally, at iteration t, consider the modified objective with L strictly convex and A the inverse matrix square root of the Hessian. One easily verifies that a Newton step is equivalent to a gradient step on ˜ L, that is, In the geometry induced by A, the objective is generally better conditioned as illustrated in Fig. 17.1. This explains the efficiency of Newton's method. In particular for any strongly convex quadratic, a Newton step reaches the optimum in one iteration, while a gradient step can take many more iterations.

<!-- chunk {"id": "body-1061", "role": "body", "section": "Stochastic Newton's method", "weight": 1.0} -->

Consider now an expected loss In that case, an estimate of the Hessian can be constructed just like for the gradient using that Figure 17.1: Left: Minimization of a quadratic L (w):= 1 2 aw 2 1 + 1 2 bw 2 2 by gradient descent. For a ≫ b ≥ 0, gradient descent typically oscillates. Right: minimization by Newton's method amounts to change the geometry of the problem to avoid oscillations. some stochastic estimates of respectively of the gradient and the Hessian with S, S ′ independently drawn from p or from mini-batch approaximations with varying mini-batch sizes. One implementation of a stochastic Newton method can then be for η t ≥ 0 such that (H (w t; S ′) + η t) -1 ≻ 0 and γ t fixed or chosen to satisfy some sufficient decrease condition. We refer the interested reader to, e.g. for more details and variants.

<!-- chunk {"id": "body-1062", "role": "body", "section": "Gauss-Newton method", "weight": 1.0} -->

Newton's method (17.1) is usually not properly defined for non-convex objective functions, since the Hessian may not be positive definite at the current iterate. We saw in Section 9.2 that the Gauss-Newton matrix can be used to define a positive-semidefinite approximation of the Hessian. Here, we revisit the Gauss-Newton method from a variational and partial linearization perspective. While the original Gauss-Newton method originates from nonlinear least-squares, we will first describe an extension to arbitrary convex loss functions, since it is both more general and easier to explain.

<!-- chunk {"id": "body-1063", "role": "body", "section": "With exact outer function", "weight": 1.0} -->

Consider a composite objective of the form where ℓ: M→ R is a convex function, such as a convex loss function applied on a given sample, and f: W → M is a nonlinear function, such as a neural network with parameters w ∈ W, evaluated on the same sample. We saw that gradient descent and Newton's method amount to using linear and quadratic approximations of L (w) around the current iterate w t, respectively. As a middle ground between the two, the Gauss-Newton method uses the linearization of f around w t but keeps ℓ as is to obtain the objective where we defined the shorthands J t:= ∂f (w t) and δ t:= f (w t) -∂f (w t) w t. We call ℓ (J t w + δ t) the partial linearization of L = ℓ ◦ f at w t, as opposed to the full linearization of L used in gradient descent.

<!-- chunk {"id": "body-1064", "role": "body", "section": "With exact outer function", "weight": 1.0} -->

Since the composition of a convex function and of linear function is convex, this objective is convex even if L (w) is nonconvex. In practice, we often add a proximity term as regularization to define We can see this update as an approximation of the proximal point update where L (w) has been replaced by its partial linearization. Solving Eq. (17.3) using gradient-based solvers requires to compute the gradient of w ↦→ ℓ (J t w + δ t), which is w ↦→ (J t) ∗ ∇ ℓ (J t w + δ t). Computing this gradient by autodiff therefore requires to perform a forward pass to compute the JVP J t w and a backward pass to compute the VJP (J t) ∗ ∇ ℓ (z). See Section 2.3 for an introduction to these operators and Chapter 8 for an introduction to autodiff.

<!-- chunk {"id": "body-1065", "role": "body", "section": "With exact outer function", "weight": 1.0} -->

The Gauss-Newton method with arbitrary convex outer loss is often called modified Gauss-Newton or prox-linear. The classical Gauss-Newton and Levenberg-Marquardt methods originate from nonlinear least-squares and are recovered when ℓ ( z ) is quadratic, such as ℓ ( z ):= 1 2 ‖ z -y ‖ 2 2, for y some reference target. The Gauss-Newton method corresponds classically to not using regularization (i.e., η t = 0) and the Levenberg-Marquardt method uses regularization (usually called damping, potentially changing η t across iterations). See e.g. for a survey of different variants.

<!-- chunk {"id": "body-1066", "role": "body", "section": "With approximate outer function", "weight": 1.0} -->

Another variant of the Gauss-Newton method consists in replacing the convex loss ℓ with its quadratic approximation around z t:= f (w t), to define the update Notice that ℓ has been replaced by its quadratic approximation q t. This objective is always a convex quadratic, unlike the objective of the Newton method in Eq. (17.1), which is a priori a nonconvex quadratic, if f is nonlinear. Simple calculations show that where q t:= ∇ ℓ (f (w t)) ∈ M = R Z, Q t:= ∇ 2 ℓ (f (w t)) ∈ R Z × Z. The closed form solution is where we used the (generalized) Gauss-Newton matrix of L = ℓ ◦ f, defined in Section 9.2.

<!-- chunk {"id": "body-1067", "role": "body", "section": "Linesearch", "weight": 1.0} -->

Similarly to Newton's method, the iterates of a Gauss-Newton method may diverge when used alone. However, the direction -( ∇ 2 GN ( ℓ ◦ f )( w t )+ η t I) -1 ∇ L ( w t ) defines a descent direction for any η t > 0 and can be combined with a stepsize γ t (typically chosen using a linesearch) to obtain iterates of the form

<!-- chunk {"id": "body-1068", "role": "body", "section": "Stochastic Gauss-Newton", "weight": 1.0} -->

In deep learning, the objective generally consists in an expectation over samples of the composition between a loss function and a network function: where S = (X,Y) denotes a sample pair of input X with associated label Y. In that case, as already studied in Section 9.2, the GaussNewton matrix ∇ 2 GN L is the expectation of the individual Gauss-Newton matrices We can estimate the gradient and the Gauss-Newton matrix, respectively, g (w; S) ≈ ∇ L (w), and G (w; S ′) ≈ ∇ 2 GN L (w) for S, S ′ ∼ ρ or using mini-batch approximations. A stochastic Gauss-Newton method therefore performs iterates for η t ≥ 0 and γ t fixed or selected to satisfy some criterion.

<!-- chunk {"id": "body-1069", "role": "body", "section": "Natural gradient descent", "weight": 1.0} -->

Natural gradient descent follows a similar principle as gradient descent: linearize the objective around the current iterate and minimize this approximation together with a proximity term. It differs from gradient descent in the choice of the proximity term: rather than using a squared Euclidean distance between the parameters, it uses a Kullback-Leibler divergence between the probability distributions these parameters define.

<!-- chunk {"id": "body-1070", "role": "body", "section": "Negative log-likelihood", "weight": 1.0} -->

We consider objectives of the form where ρ is an unknown data distribution (but from which we can sample) and where q w is a probability distribution parameterized by w. As reviewed in Chapter 3, the negative log-likelihood can be used as a loss function (many loss functions can be seen from this perspective, including the squared and logistic loss functions). In the unsupervised setting, where S = Y, we simply use q w (Y) as is. In the supervised setting, where S = (X,Y), we use the product rule P (X,Y) = P (X) P (Y | X) to parameterize q w (S) as where ρ X is the marginal distribution for X, p θ (y) is the PMF/PDF of a probability distribution and θ = f (w; x) is for instance a neural network with parameters w ∈ W and input x ∈ X.

<!-- chunk {"id": "body-1071", "role": "body", "section": "Variational perspective", "weight": 1.0} -->

Natural gradient descent is motivated by updates of the form where KL(p, q):= ∫ p (z) log p (z) q (z) d z is the Kullback-Leibler (KL) divergence. Unlike gradient descent, the proximity term is therefore between the current distribution q w t and a candidate probability distribution q w. The above problem is intractable in general, as the KL may not have a closed form. Nevertheless, its quadratic approximation can be shown to admit a simple form, where we used the Fisher information matrix ∇ 2 F L (w), studied in Section 9.3. Equipped with this quadratic approximation of the KL divergence, natural gradient descent amounts to compute iterates as where a quadratic proximity-term was added to ensure a unique solution. This is a srictly convex problem as ∇ 2 F L (w t) is positive semi-definite. The closed-form solution is Because the Gauss-Newton and Fisher information matrices are equivalent when p θ is an exponential family distribution (Proposition 9.6), the Gauss-Newton and natural gradient methods coincide in this case.

<!-- chunk {"id": "body-1072", "role": "body", "section": "Stochastic natural gradient descent", "weight": 1.0} -->

In practice, we may not have access to ∇ L (w t) in closed form as it is an expectation over ρ. Moreover, ∇ 2 F L (w t) may not be computable in closed form either. To estimate the Fisher information matrix, we can use that (see Section 9.3) using the shorthand θ:= f (w, X), We can then build estimates g (w t; S) ≈ ∇ L (w t, S) and F (w t; S ′) ≈ ∇ 2 F L (w t) for S sampled from ρ and S ′ sampled from q w t (x, y) = p X (x) ρ θ (y). A stochastic natural gradient descent can then be implemented as where γ t is a stepsize, possibly chosen by linesearch.

<!-- chunk {"id": "body-1073", "role": "body", "section": "Stochastic natural gradient descent", "weight": 1.0} -->

In deep learning, the product with the inverse Fisher or GaussNewton matrices can remain costly to compute. Several approximations have been proposed, such as KFAC, which uses a computationally efficient structural approximation to these matrices.

<!-- chunk {"id": "body-1074", "role": "body", "section": "BFGS", "weight": 1.0} -->

A celebrated example of quasi-Newton method is the BFGS method, whose acronym follows from its author names. The rationale of the BFGS update stems once again from a variational viewpoint. We wish to build a simple quadratic model of the objective h t (w) = L (w t) + 〈∇ L (w t), w -w t 〉 + 1 2 〈 w -w t, Q t (w -w t) 〉 for some Q t built along the iterations rather than taken as ∇ 2 L (w t). One desirable property of such quadratic model would be that its gradients at consecutive iterates match the gradients of the original function, i.e., ∇ h t (w t) = ∇ L (w t) and ∇ h t (w t -1) = ∇ L (w t -1).

<!-- chunk {"id": "body-1075", "role": "body", "section": "BFGS", "weight": 1.0} -->

A simpler condition, called the secant condition consists in considering the differences of these vectors, that is, ensuring that for B t = (Q t) -1. Building B t, a surrogate of the inverse of the Hessian satisfying the secant equation, can then be done as A typical implementation of BFGS stores B t ∈ R P × P in memory, which is prohibitive when P is large.

<!-- chunk {"id": "body-1076", "role": "body", "section": "Limited-memory BFGS", "weight": 1.0} -->

In practice, the limited-memory counterpart of BFGS, called LBFGS, is often preferred. The key observation of LBFGS is that we do not need to materialize B t in memory: we only need to multiply it with the gradient ∇ L ( w t ). That is, we can see B t as a linear map. Fortunately, the product between B t and any vector v can be computed efficiently if we store ( s 1, y 1, ρ 1 ),..., ( s t, y t, ρ t ) in memory. In practice, a small history of past values is used to reduce memory and computational cost. Because LBFGS has the benefits of second-order-like methods with much reduced cost, it has become a defacto algorithm, outperforming most other algorithms for medium-scale problems without particular structure.

<!-- chunk {"id": "body-1077", "role": "body", "section": "Approximate Hessian diagonal inverse preconditionners", "weight": 1.0} -->

One application of the approximations of the Hessian diagonal developed in Section 9.7 is to obtain cheap approximations of the Hessian diagonal inverse, Such a scaling would for instance be sufficient to make the quadratic example presented in Fig. 17.1 work. Many optimization algorithms, including the popular ADAM, can be viewed as using a preconditioner that approximates the inverse of the Hessian's diagonal.

<!-- chunk {"id": "body-1078", "role": "body", "section": "Summary", "weight": 1.0} -->

- We reviewed Newton's method, the Gauss-Newton method, natural gradient descent, quasi-Newton methods and preconditioning methods. - We adopted a variational viewpoint, where the method's next iterate is computed as the solution of a trade-off between minimizing an approximation of the function (linear, partially linear, quadratic) and a proximity term (squared Euclidean, KL).

<!-- chunk {"id": "body-1079", "role": "body", "section": "Summary", "weight": 1.0} -->

- All methods were shown to use iterates of the form but have different trade-offs between the cost it takes to evaluate B t ∇ L (w t) and the richness of the information used about L.

<!-- chunk {"id": "body-1080", "role": "body", "section": "Duality", "weight": 1.0} -->

In this chapter, we review duality principles in optimization.

<!-- chunk {"id": "body-1081", "role": "body", "section": "Dual norms", "weight": 1.0} -->

We introduce in this section dual norms, since they are useful in this book.

<!-- chunk {"id": "body-1082", "role": "body", "section": "Dual norms", "weight": 1.0} -->

Definition 18.1 (Dual norms). Given a norm ‖ u ‖, its dual is Therefore, the dual norm of ‖ · ‖ is the support function of the unit ball induced by the norm ‖ · ‖, We give examples of pairs of dual norms below.

<!-- chunk {"id": "body-1083", "role": "body", "section": "Dual norms", "weight": 1.0} -->

Example 18.1 (Dual norm of p -norms). The p -norm is defined by Its dual is ‖ v ‖ q where q is such that 1 p + 1 q = 1. For instance, the dual norm of the 2-norm is itself, since 1 2 + 1 2 = 1. The 1-norm and the ∞ -norm are dual of each other, since 1 1 + 1 ∞ = 1.

<!-- chunk {"id": "body-1084", "role": "body", "section": "Dual norms", "weight": 1.0} -->

The definition of dual norm implies a generalization of Cauchy-Schwarz's inequality: for all u, v ∈ R D Proposition 18.1 (Conjugate of norms and squared norms). Weknow that the conjugate of the support function is the indicator function. Therefore, if f (u) = ‖ u ‖, then On the other hand, if f (u) = 1 2 ‖ u ‖ 2, then

<!-- chunk {"id": "body-1085", "role": "body", "section": "Fenchel duality", "weight": 1.0} -->

We consider in this section standard objectives of the form where f: W → M, ℓ: M → R and R: W → R. We first show that the minimization of this objective, called the primal, can be lower bounded by a concave maximization objective, called the dual, even if the primal is nonconvex.

<!-- chunk {"id": "body-1086", "role": "body", "section": "Fenchel duality", "weight": 1.0} -->

Proposition 18.2 (Weak duality). Let f: W → M (potentially nonlinear), ℓ: M→ R (potentially nonconvex) and R: W → R (potentially nonconvex). Then where we used the conjugate and the 'generalized conjugate' Moreover, ℓ ∗ and R f are both convex functions.

<!-- chunk {"id": "body-1087", "role": "body", "section": "Fenchel duality", "weight": 1.0} -->

We emphasize that the result in Proposition 18.2 is fully general, in the sense that it does not assume the linearity of f or the convexity of ℓ and R. The caveat, of course, is that R f and ℓ ∗ are difficult to compute in general, if f is nonlinear, and if ℓ and R are nonconvex.

<!-- chunk {"id": "body-1088", "role": "body", "section": "Fenchel duality", "weight": 1.0} -->

In the case when f ( w ) = A w, where A is a linear map, and when both ℓ and R are convex, we can state a much stronger result.

<!-- chunk {"id": "body-1089", "role": "body", "section": "Fenchel duality", "weight": 1.0} -->

Proposition 18.3 (Strong duality). Let A be a linear map from W to M. Let ℓ: M→ R and R: W → R be convex functions. Let A ∗ denote the adjoint of A (Section 2.3). Then, Furthermore, the primal solution satisfies When R is strictly convex, the primal solution is uniquely determined by Proof. Since f (w) = A w, we have Furthermore, the inequality in the proof of Proposition 18.2 is an equality, since the min max is that of a convex-concave function.

<!-- chunk {"id": "body-1090", "role": "body", "section": "Fenchel duality", "weight": 1.0} -->

The maximization problem in Proposition 18.3 is called the Fenchel dual. By strong duality, the value of the maximum and the value of the minimum are equal. We can therefore choose to equivalently solve the dual instead of the primal. This can be advantageous when the space M is smaller than W.

<!-- chunk {"id": "body-1091", "role": "body", "section": "Fenchel duality", "weight": 1.0} -->

We now apply the Fenchel dual to obtain the dual of regularized multiclass linear classification.

<!-- chunk {"id": "body-1092", "role": "body", "section": "Fenchel duality", "weight": 1.0} -->

Table 18.1: Examples of loss conjugates. For regression losses (squared, absolute), where y i ∈ R M, we define t i = φ ( y i ) = y i. For classification losses (logistic, perceptron, hinge), where y i ∈ [ M ], we define t i = φ ( y i ) = e y i. To simplify some expressions, we defined the change of variable µ i:= y i -α i.

<!-- chunk {"id": "body-1093", "role": "body", "section": "Fenchel duality", "weight": 1.0} -->

Example 18.2 (Sum of separable loss functions). When the loss is ℓ (θ):= ∑ N i =1 ℓ i (θ i), where θ = A w = (A 1 w,..., A N w) ∈ M N and A i is a linear map from W to M, we obtain where A ∗ α = (A ∗ 1 α 1,..., A ∗ N α N). Typically, we define where W ∈ R M × D is a reshaped version of w ∈ W, x i ∈ R D is a training sample, and M is the number of classes. In this case, we then have Examples of loss function conjugates are given in Table 18.1.

<!-- chunk {"id": "body-1094", "role": "body", "section": "Bregman divergences", "weight": 1.0} -->

Bregman divergences are a measure of difference between two points.

<!-- chunk {"id": "body-1095", "role": "body", "section": "Bregman divergences", "weight": 1.0} -->

Definition 18.2 (Bregman divergence). The Bregman divergence gen- erated by a differentiable convex function f: R D → R is Intuitively, the Bregman divergence is the difference between f (u) and its linearization u ↦→ f (v) + 〈∇ f (v), u -v 〉 around v. This is illustrated in Fig. 18.1.

<!-- chunk {"id": "body-1096", "role": "body", "section": "Bregman divergences", "weight": 1.0} -->

Example 18.3 (Examples of Bregman divergences). If f (u) = 1 2 ‖ u ‖ 2 2, where dom(f) = R D, then the squared Euclidean distance. If f (u) = 〈 u, log u 〉, where dom(f) = R D +, then the (generalized) Kullback-Leibler divergence.

<!-- chunk {"id": "body-1097", "role": "body", "section": "Properties", "weight": 1.0} -->

Bregman divergences enjoy several useful properties.

<!-- chunk {"id": "body-1098", "role": "body", "section": "Properties", "weight": 1.0} -->

Proposition 18.4 (Properties of Bregman divergences). Let f: R D → R be a differentiable convex function. 1. Non-negativity: B f (u, v) ≥ 0 for all u, v ∈ dom(f). 2. Positivity: B f (u, v) = 0 if and only if u = v (when f is strictly convex). 4. Dual-space form: B f (u, v) = B f ∗ (b, a), where b = ∇ f (v) ∈ Figure 18.1: The Bregman divergence generated by f is the difference between f (u) and its linearization around v.

<!-- chunk {"id": "body-1099", "role": "body", "section": "Properties", "weight": 1.0} -->

Proof. The properties follow immediately from the convexity of f (u). 2. From the unicity of minimizers. 3. From the fact that u ↦→ B f (u, v) is the sum of f (u) and a linear function of u.

<!-- chunk {"id": "body-1100", "role": "body", "section": "Properties", "weight": 1.0} -->

The Bregman divergence can be used to define natural generalizations of the Euclidean projection and proximal operators, reviewed in Section 16.3 and Section 16.4.

<!-- chunk {"id": "body-1101", "role": "body", "section": "Properties", "weight": 1.0} -->

Definition 18.3 (Bregman proximal and projection operators). Let v ∈ dom(f). The Bregman proximal operator is In particular, the Bregman projection onto C ⊆ dom(f) is It turns out that these operators are intimately connected to the gradient mapping of the convex conjugate.

<!-- chunk {"id": "body-1102", "role": "body", "section": "Properties", "weight": 1.0} -->

Proposition 18.5 (Link with conjugate's gradient). If Ω = f + g, then for all θ ∈ dom(f ∗) In particular, if Ω = f + ι C, then for all θ ∈ dom(f ∗) We give two examples below.

<!-- chunk {"id": "body-1103", "role": "body", "section": "Properties", "weight": 1.0} -->

Example 18.4 (Bregman projections on the simplex). If f (u) = 1 2 ‖ u ‖ 2 2, then Therefore, the softmax can be seen as a projection onto the probability simplex in the Kullback-Leilbler divergence sense!

<!-- chunk {"id": "body-1104", "role": "body", "section": "Fenchel-Young loss functions", "weight": 1.0} -->

We end this chapter with a brief review of the Fenchel-Young family of loss functions, which includes all loss functions in Table 18.1.

<!-- chunk {"id": "body-1105", "role": "body", "section": "Fenchel-Young loss functions", "weight": 1.0} -->

Definition 18.4 (Fenchel-Young loss). The Fenchel-Young loss function generated by Ω is where θ ∈ dom(Ω ∗) and t ∈ dom(Ω).

<!-- chunk {"id": "body-1106", "role": "body", "section": "Fenchel-Young loss functions", "weight": 1.0} -->

Typically, we set θ = f ( x, w ), where f is a model prediction function with parameters w and t = φ ( y ), where φ: Y → dom(Ω). For instance, suppose we work with categorical outputs y ∈ [ M ]. Then, we can set φ ( y ) = e y, where e y is the one-hot encoding of y.

<!-- chunk {"id": "body-1107", "role": "body", "section": "Fenchel-Young loss functions", "weight": 1.0} -->

The important point to notice is that the Fenchel-Young loss is defined over arguments in mixed spaces: θ belongs to the dual space, while t belongs to the primal space. In fact, the Fenchel-Young loss is intimately connected to the Bregman divergence, since B Ω ( t, v ) = Ω ∗ ( θ ) + Ω( t ) - 〈 θ, t 〉, if we set θ = ∇ Ω( v ). The key properties of Fenchel-Young loss functions are summarized below.

<!-- chunk {"id": "body-1108", "role": "body", "section": "Summary", "weight": 1.0} -->

- The convex conjugate serves as a powerful abstraction in Fenchal duality, decoupling the dual expression and function-specific terms. - The convex conjugate is also tightly connected to Bregman divergences and can be used to derive the family of FenchelYoung loss functions, which can be seen as primal-dual Bregman divergences.
