Data-Driven Robust Optimization

The last decade witnessed an explosion in the availability of data for operations research applications. Motivated by this growing availability, we propose a novel schema for utilizing data to design uncertainty sets for robust optimization using statistical hypothesis tests. The approach is flexible and widely applicable, and robust optimization problems built from our new sets are computationally tractable, both theoretically and practically. Furthermore, optimal solutions to these problems enjoy a strong, finite-sample probabilistic guarantee. \edit{We describe concrete procedures for choosing an appropriate set for a given application and applying our approach to multiple uncertain constraints. Computational evidence in portfolio management and queuing confirm that our data-driven sets significantly outperform traditional robust optimization techniques whenever data is available.

## Introduction

Robust optimization is a popular approach to optimization under uncertainty. The key idea is to define an uncertainty set of possible realizations of the uncertain parameters and then optimize against worst-case realizations within this set. Computational experience suggests that with well-chosen sets, robust models yield tractable optimization problems whose solutions perform as well or better than other approaches. With poorly chosen sets, however, robust models may be overly-conservative or computationally intractable. Choosing a good set is crucial.

On the other hand, the last decade witnessed an explosion in the availability of data. Massive amounts of data are now routinely collected in many industries. Retailers archive terabytes of transaction data. Suppliers track order patterns across their supply chains. Energy markets can access global weather data, historical demand profiles, and, in some cases, real-time power consumption information. These data have motivated a shift in thinking -- away from a priori reasoning and assumptions and towards a new data-centered paradigm. A natural question, then, is how should robust optimization techniques be tailored to this new paradigm?

In this paper, we propose a general schema for designing uncertainty sets for robust optimization from data. We consider uncertain constraints of the form ${f{(\overset{\sim}{\mathbf{u}},\mathbf{x})}} \leq 0$ where $\mathbf{x} \in {\mathbb{R}}^{k}$ is the optimization variable, and $\overset{\sim}{\mathbf{u}} \in {\mathbb{R}}^{d}$ is an uncertain parameter. We model this constraint by choosing a set $\mathcal{U}$ and forming the corresponding robust constraint

We assume throughout that $f{(\mathbf{u},\mathbf{x})}$ is concave in $\mathbf{u}$ for any $\mathbf{x}$.

Table 1 summarizes the a priori structural assumptions, hypothesis tests, and resulting uncertainty sets that we propose. Each set is convex and admits a tractable, explicit description; see the referenced equations.

Summary of data-driven uncertainty sets proposed in this paper. Assumptions on ℙ* Hypothesis Test \pbox20cmGeometric Description Eqs.
