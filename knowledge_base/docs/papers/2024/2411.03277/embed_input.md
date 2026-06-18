<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Asymptotic Stability Equals Exponential Stability - While You Twist Your Eyes

Topics include Stability analysis, GAS, Exponential stability.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Suppose that two vector fields on a smooth manifold render some equilibrium point globally asymptotically stable (GAS). We show that there exists a homotopy between the corresponding semiflows such that this point remains GAS along this homotopy.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the context of what we call today Conley index theory (see Section A), Conley posed the following "converse question" in the 1970s: "To what extent does the homotopy index *\[Conley index\]* itself determine the equivalence class of isolated invariant sets which are related by continuation?" \[ref:conley1978isolated, p. 83\]. Recently, Kvalheim proved that uniquely integrable $C^{0}$ vector fields, on a $C^{\infty}$ manifold $M$, rendering a compact set $A \subseteq M$ asymptotically stable, are homotopic on an open neighbourhood $U \supseteq A$ such that throughout the homotopy the vector fields do not vanish on $U \smallsetminus A$ \[ref:kvalheim2022obstructions, Thm. 1\].

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Connecting this result to Conley, a follow-up question (revitalized) by Kvalheim---which is the central question of this note---is the following.\
Question: "Are dynamical systems that render a set $A$ asymptotically stable, homotopic through dynamical systems that preserve this notion of stability?"\
This question, in one form or another, inspired several works, for instance, \[ref:reineck1992continuation, ref:mrozek2000conley, ref:JongeneelSchwan2024TAC\]. Here, we will elaborate on commentary by the author in \[ref:JongeneelSchwan2024TAC\].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, in the seminal paper "Asymptotic stability equals exponential stability, and ISS equals finite energy gain---if you twist your eyes" from 1999, Grüne, Sontag and Wirth showed that asymptotic stability "equals" exponential stability in the sense that if an equilibrium point is asymptotically stable under some vector field on ${\mathbb{R}}^{n}$, then, there is a suitable change of coordinates rendering this point exponentially stable \[ref:grune1999asymptotic\]. Such a change of coordinates is understood to be instantaneous. However, by leveraging their work, we show that asymptotic stability can be continuously "transformed" into exponential stability, while preserving asymptotic stability throughout the transformation, see Theorem 3.6. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes"). Differently put, asymptotic stability equals exponential stability---not only if you twist your eyes, but while you twist your eyes.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The key to this is to observe that we can select the transformation from \[ref:grune1999asymptotic\] to be an orientation-preserving homeomorphism on ${\mathbb{R}}^{n}$, not just any homeomorphism cf. \[ref:JongeneelSchwan2024TAC, Sec. III\], see the proof of Proposition 3.2. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes").

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This result provides a partial solution to Conley's converse question as it turns out that the asymptotically stable systems under consideration can be continuously transformed into the same exponentially stable system and hence, by transitivity, into each other. Concurrently, we discuss extensions to discontinuous vector fields throughout, plus we illustrate how to go about extensions to ISS. We also discuss intimate connections with optimization and optimal transport (e.g., see Example 3.4. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes") and 5.1. ‣ 5 A view from optimal transport ‣ Asymptotic stability equals exponential stability—while you twist your eyes")).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Example 1.1 (Trivial convex combinations can fail)", "weight": 1.0} -->

Consider a linear differential equation $\overset{˙}{x} = {A{(s)}x}$ on ${\mathbb{R}}^{2}$ parametrized by the matrices

<!-- chunk {"id": "body-0009", "role": "body", "section": "Example 1.1 (Trivial convex combinations can fail)", "weight": 1.0} -->

Both $A{}$ and $A{}$ correspond to global asymptotically stable systems, yet, for $s = \frac{1}{2}$, the system $\overset{˙}{x} = {A{(s)}x}$ is unstable. Hence, we cannot simply construct straight-line homotopies between stable vector fields and expect that stability is preserved. Instead, we know from \[ref:JongeneelSchwan2024TAC\] that for vector fields with convex Lyapunov functions we should homotope via the canonical ODE $\overset{˙}{x} = {- x}$. Explicitly, consider the following path of vector fields defined by

<!-- chunk {"id": "body-0010", "role": "body", "section": "Dynamical systems", "weight": 1.0} -->

The focus on semiflows instead of flows allows us to look at sufficiently regular discontinuous vector fields. This is relevant, as the introduction of feedback usually results in a closed-loop vector field that cannot be assumed to be continuous (e.g., think of optimal control^22^2One might also think of topological obstructions, however, the type of discontinuities we consider do not allow for overcoming those obstructions, in general \[ref:ryan1994brockett\].). This choice of setting is also motivated by other recent work. For instance, the research question in \[ref:ozaslan2024exponential\] is: "Given an exponentially stable optimization algorithm, can it be modified to obtain a finite/fixed-time stable algorithm?". Some sufficient conditions are provided in \[ref:ozaslan2024exponential\], we will show a generic, yet less constructive, viewpoint.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Dynamical systems", "weight": 1.0} -->

Let $X$ be some vector field on ${\mathbb{R}}^{n}$, possibly discontinuous. To study $X$, we usually pass to some differential inclusion

<!-- chunk {"id": "body-0012", "role": "body", "section": "Dynamical systems", "weight": 1.0} -->

where the set-valued map $F:{{\mathbb{R}}^{n}\rightarrow 2^{{\mathbb{R}}^{n}}}$, with $2^{S}$ denoting the power set of a set $S$, is in some precise sense related to $X$. The rationale is to pass from an irregular single-valued map, to a more regular set-valued map.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Dynamical systems", "weight": 1.0} -->

Let $\lambda^{d}$ denote the Lebesgue measure on ${\mathbb{R}}^{d}$, then, solutions $\mathcal{I} \ni t\mapsto{\xi{(t)}}$ to these differential inclusions, are absolutely continuous (AC) on each compact subinterval of $\mathcal{I}$ and such that ${\overset{˙}{\xi}{(t)}} \in {F{({\xi{(t)}})}}$ for $\lambda^{1}$-a.e. $t \in \mathcal{I}$. Typically, $F$ is assumed to be upper semi-continuous and compact, convex valued. With those assumptions in mind, then, under mild conditions on $X$, a valuable solution framework follows by applying Filippov's operator $\mathcal{F}$, that is,

<!-- chunk {"id": "body-0014", "role": "body", "section": "Stability", "weight": 1.0} -->

In this section we will characterize stability under (1.2). Starting with the regular case, for simplicity, let the vector field $F$ be single-valued and smooth. In that case, $F$ generates a flow, denoted $\varphi{( \cdot;F)}$. A point $x^{\star} \in {\mathbb{R}}^{n}$ is an equilibrium point of $F$ when ${F{(x^{\star})}} = 0$ or equivalently ${\varphi^{t}{(x^{\star};F)}} = x^{\star}$ ${\forall t} \in {\mathbb{R}}$. We will set $x^{\star}:=0$, unless stated otherwise. Then, $0$ is said to be globally asymptotically stable (GAS) (under $F$) when

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark 1.2 (On global stability)", "weight": 1.0} -->

Although we merely work with equilibria and ${\mathbb{R}}^{n}$ (or $M^{n} \simeq_{d}{\mathbb{R}}^{n}$) we take a topological approach akin to \[ref:bhatiahajek2006local\] and hence GAS is defined as above. One can turn Property (s.i) truly global, however, e.g., see \[ref:wilson1969smoothing, ref:lin1996smoothV2\].

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 1.2 (On global stability)", "weight": 1.0} -->

Specifically, let $B_{r}{(x)}$ be some $r$-metric ball centered at $x$, then, require the existence of $\delta \in \mathcal{K}_{\infty}$ such that for any $\varepsilon \geq 0$ we have ${\varphi^{t}{({B_{\delta{(\varepsilon)}}{(x)}})}} \subseteq {B_{\varepsilon}{(x)}}$ ${\forall t} \in {\mathbb{R}}_{\geq 0}$. In general these definitions are not equivalent, however, for $0$ being GAS on ${\mathbb{R}}^{n}$, they are \[ref:andriano1997global\]. $\circ$

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 1.2 (On global stability)", "weight": 1.0} -->

Due to the work of Lyapunov \[ref:liapunov1892general\], we know that to reason about stability, it is worthwhile to look for "potential functions" that capture stability, illustrated by the fact that his theory effectively replaced the definitions of stability.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 1.2 (On global stability)", "weight": 1.0} -->

Property (V.ii) implies sublevel set compactness. We call such a function a (smooth, strict and proper) Lyapunov function (with respect to the pair $(F,0)$). This work is about GAS, so we will omit "strict" and "proper" from now. Then, based on converse theory, e.g., see \[ref:Massera1956, ref:kurzweil1963inversion, ref:wilson1969smoothing, ref:fathi2019smoothing\], we can appeal to the celebrated theorem stating that $0$ is GAS if and only if there is a (corresponding) smooth Lyapunov function \[ref:bacciotti2005liapunov, Thm. 2.4\].

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 1.2 (On global stability)", "weight": 1.0} -->

A generalization of the above to differential inclusions (1.2) is as follows.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example 1.4 (A semiflow corresponding to a vector field with bounded discontinuities)", "weight": 1.0} -->

One can check that $\varphi_{1}$ is a semiflow, describing a solution (e.g., in the sense of Filippov) to (1.3. ‣ 1.3 Stability ‣ 1 Introduction ‣ Asymptotic stability equals exponential stability—while you twist your eyes")). Regarding stability, consider the $C^{\infty}$ Lyapunov function $x\mapsto{V_{1}{(x)}}:={\frac{1}{2}x^{2}}$ and see that ${{\nabla V_{1}}{(x)}X_{1}{(x)}} = {- {|x|}} < 0$ on ${\mathbb{R}} \smallsetminus {\{ 0\}}$. This already shows that the existence of a smooth Lyapunov function, asserting that the origin is GAS, does not imply the existence of a flow, nor does it imply that convergence to $0$ is merely asymptotic.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Further comments on related work", "weight": 1.0} -->

Recently, we showed that when $0 \in {\mathbb{R}}^{n}$ is GAS under a continuous vector field $X$, and if this can be asserted using a $C^{1}$ convex Lyapunov function, then, $X$ is straight-line homotopic to $- \partial_{x}$, such that the origin remains GAS along the homotopy \[ref:JongeneelSchwan2024TAC\]. This is a convenient result, but not a general one.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Further comments on related work", "weight": 1.0} -->

Earlier, the following homotopy of vector fields, appeared in several works (e.g., see \[ref:ryan1994brockett, p. 1603\], \[ref:sontag2013mathematical, Thm. 21\], \[ref:coron2007control, p. 291\] and \[ref:jongeneel2023topological, Ex. 3.4\]):

<!-- chunk {"id": "body-0023", "role": "body", "section": "Further comments on related work", "weight": 1.0} -->

Unfortunately, for (2.1), $0 \in {\mathbb{R}}^{n}$ is not known to be GAS along the path ${\lbrack 0,1\rbrack} \ni s\mapsto{H{(s,x)}}$. The scalar and linear cases can be understood, however.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example 2.1 (Stability-preserving homotopies for $n = 1$)", "weight": 1.0} -->

As for any $t \in {\mathbb{R}}_{> 0}$, the only fixed point of $\varphi^{t}{( \cdot;X)}$ is $0$, it follows that for $n = 1$, the homotopy (2.1) preserves stability since the sign of $x\mapsto{H{(s,x)}}$ cannot flip, for otherwise, ${\varphi^{s/{({1 - s})}}{(x;X)}} = x$ must hold for some $s \in {}$ and $x \neq 0$. $\circ$

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example 2.2 (Stability preserving homotopies for linear ODEs)", "weight": 1.0} -->

Either way, the homotopy (2.1) does already show that there is a homotopy that does not introduce new equilibrium points, along the homotopy. Indeed, this has been generalized recently by Kvalheim to compact attractors on manifolds \[ref:kvalheim2022obstructions\]. On the other hand, it is known that there is no reason why stability must be preserved along such a homotopy. In the spirit of \[ref:eliashberg2002introduction, Sec. 4.1\],

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example 2.2 (Stability preserving homotopies for linear ODEs)", "weight": 1.0} -->

parametrizing a homotopy from ${X{( \cdot;0)}} = \partial_{x}$ to ${X{( \cdot;1)}} = {- \partial_{x}}$ along non-vanishing vector fields on ${\mathbb{R}}^{n} \smallsetminus {\{ 0\}}$. Note, the (Hopf) indices \[ref:milnor65, p. 32\] of these "qualitatively opposite" vector fields are equal, i.e., ${{ind}_{0}{(\partial_{x})}} = 1^{n} = {({- 1})}^{n} = {{ind}_{0}{({- \partial_{x}})}}$. It is this weakness of existing homotopy-invariants that we hope to overcome by studying more restrictive equivalence classes.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Stability preserving homotopies", "weight": 1.0} -->

Now, we will address our central research question in case $A$ is an equilibrium point. First, we consider $0 \in {\mathbb{R}}^{n}$ being GAS under some appropriately regular vector field on ${\mathbb{R}}^{n}$ and eventually generalize to smooth manifolds.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 3.1 (Vector field regularity on ${\\mathbb{R}}^{n}$)", "weight": 1.0} -->

Our vector fields are locally essentially bounded, possibly set-valued at $0$ and locally Lipschitz on ${\mathbb{R}}^{n} \smallsetminus {\{ 0\}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 3.1 (Vector field regularity on ${\\mathbb{R}}^{n}$)", "weight": 1.0} -->

If $X$ satisfies Assumption 3.1. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes"), $\mathcal{F}{\lbrack X\rbrack}$ is upper semi-continuous and compact, convex valued, which allows for a smooth converse Lyapunov theory, e.g., see \[ref:clarke1998asymptotic, ref:goebel2012hybrid\]. We focus on Filippov's framework, but in what follows, one may replace $\mathcal{F}{\lbrack X\rbrack}$ with any vector field $F$ that complies with Definition 1.3. ‣ 1.3 Stability ‣ 1 Introduction ‣ Asymptotic stability equals exponential stability—while you twist your eyes").

<!-- chunk {"id": "body-0030", "role": "body", "section": "Example 3.3 (Homotopic vector fields, preserving stability)", "weight": 1.0} -->

The purpose of the following example is to illustrate the construction of the homotopy that appears in the proof of Proposition 3.2. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes").

<!-- chunk {"id": "body-0031", "role": "body", "section": "Example 3.4 (Homotopy from invexity to convexity)", "weight": 1.0} -->

Consider a coercive, invex function (i.e., every critical point is a global minimizer) on $\mathbb{R}$ defined by $x\mapsto v_{i}{(x)}:=\frac{1}{2}x^{2} + \frac{3}{2}\sin{(x)}^{2}$. Along the lines of the proof of Proposition 3.2.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Example 3.4 (Homotopy from invexity to convexity)", "weight": 1.0} -->

‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes"), we can find a map $T$ such that ${v_{i}{({T^{- 1}{(x)}})}} = {\gamma{({|x|})}}:=\sqrt{|x|}$ (see that ${{{\gamma{(s)}}/\gamma^{\prime}}{(s)}} \geq s$ for all $s \geq 0$), and a path from $T$ to ${id}_{\mathbb{R}}$, as given by

<!-- chunk {"id": "body-0033", "role": "body", "section": "Example 3.4 (Homotopy from invexity to convexity)", "weight": 1.0} -->

Next, consider the homotopy ${(s^{\prime},x)}\mapsto x^{{1/2} + {{({3/2})}s^{\prime}}}$ to construct the path from $v_{i}$ to $x\mapsto{v_{q}{(x)}}:=x^{2}$, along continuous functions such that $0$ is the global minimizer throughout^77^7For a simulation of this homotopy, see wjongeneel.nl/figinvex.gif., see Figure 3.1. For functions as simple as $v_{i}$ one can find simpler homotopies (e.g., a straight-line), however, to the best of our knowledge, being able to guarantee the mere existence of such a homotopy is new. Proposition 3.2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Example 3.4 (Homotopy from invexity to convexity)", "weight": 1.0} -->

‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes") provides us with the existence of a homotopy from a smooth Lyapunov function $V$ to $V_{q}$, along continuous^88^8It is not evident, and currently unknown, whether smoothness can be preserved throughout the homotopy, see Step (iii) of the proof of Proposition 3.2. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes"). Lyapunov functions that assert $0 \in {\mathbb{R}}^{n}$ is GAS along the homotopy. Differently put, we can find a homotopy from a coercive, invex function, to a convex function, such that along the homotopy the minimizer is preserved. This might be of independent interest. $\circ$

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 3.4 (Homotopy from invexity to convexity)", "weight": 1.0} -->

As we allow for a class of discontinuous vector fields, Proposition 3.2. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes") allows for an extension of the standard Hopf index, this has been pioneered by Gottlieb, e.g., see \[ref:gottlieb1995index\]. See also \[ref:casagrande2008conley\] for a Conley index applicable to discontinuous vector fields and see \[ref:Kvalheim2021PHhybrid\] for a hybrid Poincaré-Hopf theorem.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example 3.4 (Homotopy from invexity to convexity)", "weight": 1.0} -->

We point out that one could omit Step (i) of the proof of Proposition 3.2. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes"), yet, as is also shown in Example 3.3. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes"), it is typically convenient to pass through a gradient flow. We also remark that the origin plays no particular role in Proposition 3.2. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes"), as it should. In fact, if $X$ is such as in Proposition 3.2.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Example 3.4 (Homotopy from invexity to convexity)", "weight": 1.0} -->

‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes"), yet, the equilibrium point is now arbitrary, we can still construct a homotopy between $\varphi{( \cdot;{\mathcal{F}{\lbrack X\rbrack}})}$ and $\varphi{( \cdot;{- \partial_{x}})}$ such that along the homotopy some point is GAS.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Example 3.4 (Homotopy from invexity to convexity)", "weight": 1.0} -->

Next, we generalize Proposition 3.2. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes") to smooth manifolds, which is almost immediate as the GAS property heavily restricts the class of manifolds, e.g., see \[ref:bhatia1970stability, Ch. V.3\]. We assume that our manifolds are Hausdorff and second countable. Regarding our vector fields, we assume simply the following.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Assumption 3.5 (Vector field regularity on $M^{n}$)", "weight": 1.0} -->

Our vector fields are locally Lipschitz on $M^{n}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Assumption 3.5 (Vector field regularity on $M^{n}$)", "weight": 1.0} -->

Indeed, one can work with less regular vector fields and fully generalize Proposition 3.2. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes") to manifolds, i.e., via \[ref:mayhew2011topological, Cor. 13\]. We refrain from introducing further technicalities and work with Assumption 3.5. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes").

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example 3.7 (Equilibria on ${\\mathbb{S}}^{2}$)", "weight": 1.0} -->

To exemplify Theorem 3.6. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes"), one might think of rendering the South Pole $S$ an attractor on ${\mathbb{S}}^{2} \smallsetminus {\{ N\}}$, for $N$ the North Pole. To that end, consider the vector fields $X$ and $Y$ on ${\mathbb{R}}^{2}$, defined through

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 3.7 (Equilibria on ${\\mathbb{S}}^{2}$)", "weight": 1.0} -->

The origin is GAS under both $X$ and $Y$ (e.g., consider the canonical quadratic Lyapunov function). Let $\Pi_{N}$ be the stereographic projection from ${\mathbb{S}}^{2} \smallsetminus {\{ N\}}$ to ${\mathbb{R}}^{2}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example 3.7 (Equilibria on ${\\mathbb{S}}^{2}$)", "weight": 1.0} -->

Then, to transform $X$ and $Y$ to vector fields on ${\mathbb{S}}^{2} \smallsetminus {\{ N\}}$, we construct the pushforwards ${(\Pi_{N}^{- 1})}_{\ast}X$ and ${(\Pi_{N}^{- 1})}_{\ast}Y$, see Figure 3.2. Exploiting this structure and our previous work \[ref:JongeneelSchwan2024TAC\], we can construct an explicit homotopy between these two vector fields that preserves stability of $S$ on ${\mathbb{S}}^{2} \smallsetminus {\{ N\}}$^99^9For a numerical simulation of the homotopy, see wjongeneel.nl/figStereoS2.gif. Note that the homotopy is through the canonical vector field indeed.. $\circ$

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 3.8 (Weaker notions of stability)", "weight": 1.0} -->

In general, one cannot relax GAS to mere stability. A reason being that the (Hopf) index of Lyapunov stable equilibria is not fixed \[ref:krasnosel1984geometrical, Sec. 52\], yet, this index is a homotopy invariant (e.g., for GAS the index is fixed). In Section, we do elaborate on ISS. $\circ$

<!-- chunk {"id": "body-0045", "role": "body", "section": "Input-to-State Stability", "weight": 1.0} -->

As in \[ref:grune1999asymptotic\], we can also study "disturbed" systems of the form

<!-- chunk {"id": "body-0046", "role": "body", "section": "Input-to-State Stability", "weight": 1.0} -->

where $f:{{{\mathbb{R}}^{n} \times D}\rightarrow{\mathbb{R}}^{n}}$, with $D \subseteq {\mathbb{R}}^{m}$, is continuous, and locally Lipschitz on ${\mathbb{R}}^{n} \smallsetminus {{\{ 0\}} \times D}$. We let $\mathcal{D}_{I}$ denote the set of measurable, locally essentially bounded functions ${\mathbb{R}} \supseteq I \ni t\mapsto{d{(t)}} \in D$, with ${d{( \cdot )}} \in \mathcal{D}$ overloading notation, indicating any function of appropriate length. Whenever relevant, we do assume that our solutions are forward complete (e.g., we can appeal to \[ref:angeli1999forward, Cor.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Input-to-State Stability", "weight": 1.0} -->

2.11\]), we denote them using semiflow notation as $\varphi^{t}{(x_{0},{d{( \cdot )}})}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Input-to-State Stability", "weight": 1.0} -->

Leveraging intuition from linear systems theory, input-to-state stability was derived as a stability notion invariant under coordinate transformations (homeomorphisms that fix $0$) \[ref:sontagbasicconcepts2008input\]. In particular, a system (4.1) is said to be Input-to-State Stable (ISS) when there are $\beta \in {\mathcal{K}\mathcal{L}}$ and $\gamma \in \mathcal{K}_{\infty}$ such that

<!-- chunk {"id": "body-0049", "role": "body", "section": "Input-to-State Stability", "weight": 1.0} -->

for all $t \geq 0$, $x_{0} \in {\mathbb{R}}^{n}$ and any ${d{( \cdot )}} \in \mathcal{D}$. For the corresponding Lyapunov theory, see \[ref:sontag1995characterizations\]. Constraining the transient, a system (4.1) is said to be Input-to-State Exponentially Stable (ISES) when there are constants ${M,a} \in {\mathbb{R}}_{> 0}$ and a $\alpha \in \mathcal{K}_{\infty}$ such that

<!-- chunk {"id": "body-0050", "role": "body", "section": "Input-to-State Stability", "weight": 1.0} -->

for all $t \geq 0$, $x_{0} \in {\mathbb{R}}^{n}$ and any ${d{( \cdot )}} \in \mathcal{D}$. It can be shown \[ref:grune1999asymptotic, Thm. 3\], that there is always a coordinate transformation that brings an ISS system into one that is ISES with normalized constants, that is, $M = a = 1$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Input-to-State Stability", "weight": 1.0} -->

for all $t \geq 0$, $x_{0} \in {\mathbb{R}}^{n}$ and any ${d{( \cdot )}} \in \mathcal{D}$, e.g., see \[ref:AvdSL2, Ch. 8\]. However, this means that $\overset{˙}{x} = {{- x} + d}$ can be understood, in particular, as a canonical system with a finite (unitary) linear $L_{2}$ gain. Indeed, \[ref:grune1999asymptotic, Thm. 4\] shows that an ISES system can be transformed into a system with such an $L_{2}$ gain.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Input-to-State Stability", "weight": 1.0} -->

Here, we focus on homotopies through coordinate transformations of $x$ and $d$, for otherwise we could "remove" the disturbance, e.g., consider ${\lbrack 0,1\rbrack} \ni \theta\mapsto{f{(x,{\thetad})}}$. Now, to exemplify why the existence of a homotopy from any ISS system, through coordinate transformation, to $\overset{˙}{x} = {{- x} + d}$ is too strong, consider the following example. Example 4.1. ‣ 4 Input-to-State Stability ‣ Asymptotic stability equals exponential stability—while you twist your eyes") implies in particular that a naïve generalization of Section to ISS is impossible.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Example 4.1 (No canonical system)", "weight": 1.0} -->

Consider the linear ISS system

<!-- chunk {"id": "body-0054", "role": "body", "section": "Example 4.1 (No canonical system)", "weight": 1.0} -->

‣ 4 Input-to-State Stability ‣ Asymptotic stability equals exponential stability—while you twist your eyes")) satisfies ${\langle{\partial_{x}{S{(x)}}},{{Ax} + {R{(d)}}}\rangle} \leq {\frac{1}{2}{({{\| d\|}_{2}^{2} - {\| x\|}_{2}^{2}})}}$ and thus, (4.4. ‣ 4 Input-to-State Stability ‣ Asymptotic stability equals exponential stability—while you twist your eyes")) satisfies the canonical $L_{2}$ gain bound (4.3). $\circ$

<!-- chunk {"id": "body-0055", "role": "body", "section": "Example 4.1 (No canonical system)", "weight": 1.0} -->

The way to interpret the upcoming proposition is as follows. Given a solution under (4.1), assumed to be ISS. This solution is understood as fixed data and now someone gradually applies a change of coordinates to both $x$ and $d$. It turns out that by doing so, one can always transform this solution data into data satisfying (4.3), thus, into a system like $\overset{˙}{x} = {{- x} + d}$. Indeed, it follows directly that ISS is preserved throughout, e.g., see \[ref:kellett2015input\] for more on ISS and coordinate transformations. However, comparing again to Section, we cannot readily say more beyond paths of coordinate transformations, e.g., first one should topologize $\mathcal{D}$ to study continuity of ${d{( \cdot )}}\mapsto{\varphi^{t}{(x_{0},{d{( \cdot )}})}}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Example 4.1 (No canonical system)", "weight": 1.0} -->

In this work we refrain from completing this study as it does not add to the central message while it requires significant technical machinery, however, without doing so we cannot formally discuss homotopies of solutions^1010^10This is also why "and ISS equals finite energy" is not part of our title cf. \[ref:grune1999asymptotic\]..

<!-- chunk {"id": "body-0057", "role": "body", "section": "A view from optimal transport", "weight": 1.0} -->

Suppose there is a smooth Lyapunov function $V$, asserting that $0 \in {\mathbb{R}}^{n}$ is GAS under some ODE $\overset{˙}{x} = {X{(x)}}$. To refine our understanding beyond Theorem 3.2. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes") and towards a similar result for vector fields, we note that our desire relates to optimal transport (OT). Let ${\mu_{0},\mu_{1}} \in {\mathcal{P}{({\mathbb{R}}^{n})}}$ be Borel probability measures on ${\mathbb{R}}^{n}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "A view from optimal transport", "weight": 1.0} -->

Now, if $f$ is sufficiently regular, we can conclude that ${{\nabla\log}f}{(x;s)}$ renders $0$ GAS, for each fixed $s$. It is particularly interesting that the standard Gaussian measure results in the canonical ODE $\overset{˙}{x} = {- x}$. In what follows we touch upon this viewpoint.

<!-- chunk {"id": "body-0059", "role": "body", "section": "A view from optimal transport", "weight": 1.0} -->

where $T\#\mu$ denotes the pushforward of $\mu$. Brenier \[ref:brenier1991polar\] showed that if $\mu \ll \lambda^{n}$, then, there is a convex map $\phi:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, being $\mu$-a.e. differentiable, such that ${\nabla{\phi\#\mu}} = \nu$ solves (5.1). We do a simple example.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion and future work", "weight": 1.5} -->

We have provided a step towards better understanding Conley's converse question in some generality, yet, many open problems remain. Although directly working with flows has benefits, e.g., see \[ref:aguiar2023universal\], the main open problem is the extension to vector fields and generic attractors. Several other questions are as follows.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion and future work", "weight": 1.5} -->

Open problem 1: characterize stability of (2.1) throughout the homotopy.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion and future work", "weight": 1.5} -->

Open problem 2: prove or disprove that Proposition 3.2. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes") holds for $n = 5$. A counterexample would disprove the smooth Poincaré conjecture for ${\mathbb{S}}^{4}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion and future work", "weight": 1.5} -->

Although we work with semiflows, to leverage converse Lyapunov theory we rely on vector fields generating them. Removing this condition is non-trivial, illustrated by \[ref:fathi2019smoothing, Sec. 7\], but also not futile, as illustrated below.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Example 6.1 (An attractor on the mapping torus)", "weight": 1.0} -->

To construct an example of a semiflow that does not correspond to a vector field, one can appeal to maps with a "negative orientation", e.g., a smooth vector field $X$ always results in a flow $\varphi{( \cdot;X)}$ such that the diffeomorphism $\varphi^{t}{( \cdot;X)}$ is isotopic to the identity^1111^11Consider the homotopy ${\lbrack 0,1\rbrack} \ni s\mapsto\varphi^{\tau{({1 - s})}}$ from $\varphi^{\tau}$ to $\varphi^{0} = {id}$..

<!-- chunk {"id": "body-0065", "role": "body", "section": "Example 6.1 (An attractor on the mapping torus)", "weight": 1.0} -->

Open problem 3: prove or disprove that Proposition 3.2. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes") holds for all semiflows that render $0$ GAS (not just the ones generated by vector fields).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Example 6.1 (An attractor on the mapping torus)", "weight": 1.0} -->

Section touched upon connections with OT. Motivated by work in the context of geometry processing \[ref:solomon2019optimalV\], we believe that more work is warranted.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Example 6.1 (An attractor on the mapping torus)", "weight": 1.0} -->

Open problem 4: elucidate what OT can tell us about the existence of stability preserving homotopies on the level of vector fields, and vice versa.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Example 6.1 (An attractor on the mapping torus)", "weight": 1.0} -->

Our work also benefits from more explicit results, e.g., see \[ref:bramburger2021deep\].
