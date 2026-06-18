Learning Parametric Convex Functions

Topics include Convex optimization, Optimization, Learning, Convex function.

A parametrized convex function depends on a variable and a parameter, and is convex in the variable for any valid value of the parameter. Such functions can be used to specify parametrized convex optimization problems, i.e., a convex optimization family, in domain specific languages for convex optimization. In this paper we address the problem of fitting a parametrized convex function that is compatible with disciplined programming, to some given data. This allows us to fit a function arising in a convex optimization formulation directly to observed or simulated data. We demonstrate our open-source implementation on several examples, ranging from illustrative to practical.

## Parametrized convex functions

A *parametrized convex function* (PCF) $f$ has the form

where $\Theta \subseteq \text{R}^{p}$. To be a PCF, $f$ must be continuous in $\theta$, and for each $i = {1,\ldots,d}$, $f_{i}{(x,\theta)}$ is convex in $x$ for any $\theta \in \Theta$. We refer to the first argument $x$ of the PCF $f$ as the *variable*, and the second argument $\theta$ as the *parameter*. When $d = 1$, we refer to $f$ as a scalar PCF.

## Disciplined convex programming

The terms variable and parameter in a PCF are taken from disciplined convex programming (DCP), a method for expressing a PCF as an expression in a domain specific language (DSL) constructed from variables, constants, parameters, and a small library of functions called atoms \[, \]. In DCP, the expression must be constructed in a specific way that corresponds to a composition rule that establishes convexity of the function with respect to the variable, for any valid parameter.

Functions expressed in DCP form can be used to form a parametrized convex optimization problem or convex optimization family. When the parameters are given specific numerical values, we obtain a problem instance, which can be solved by automatically transforming the problem instance to a canonical form, solving the canonical form, and then retrieving the solution of the original problem instance from the solution of the canonicalized problem instance. Examples of DSLs that leverage DCP for modeling convex optimization problems (and support parameters) include CVXPY (in Python), CVXR (in R), Convex.jl \[UMZ^+^14\] and JuMP (in Julia).
