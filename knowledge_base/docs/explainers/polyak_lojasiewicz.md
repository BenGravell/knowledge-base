# Linear Convergence of Gradient and Proximal-Gradient Methods Under the Polyak-Łojasiewicz Condition

*Work by Hamed Karimi, Julie Nutini, and Mark Schmidt, ECML PKDD 2016*

## Summary

The authors re-explore the Polyak-Lojasiewicz inequality [first analyzed by Polyak in 1963](https://www.sciencedirect.com/science/article/abs/pii/0041555363903823) by deriving convergence results under various descent methods for various modern machine learning tasks and establishing equivalences and sufficiency-necessity relationships with several other nonconvex function classes. A highlight of the paper is a beautifully simple proof of linear convergence using gradient descent on PL functions, which we walk through here.

## Convergence of gradient descent under the Polyak-Lojasiewicz inequality

This proof is extremely short and simple, requiring only a few assumptions and a basic mathematical background. It is strange that it is not as universally known as the [theory related to convex optimization](https://web.stanford.edu/~boyd/cvxbook/).

Relating to the theory of Lyapunov stability for nonlinear systems, the PL inequality essentially means that the function value itself is a valid Lyapunov function for exponential stability of the global minimum under the nonlinear gradient descent dynamics.

[Lieven Vandenberghe’s ECE236C Spring 2022 lecture notes on the gradient method](https://www.seas.ucla.edu/~vandenbe/236C/lectures/gradient.pdf) for the case of strongly convex functions are an excellent supplement.

The setting we consider is that of minimizing a function $f(x)$.

### Lipschitz continuity

#### Definitions

A function is **Lipschitz continuous** with constant $L$ if

$$
\| f(y) - f(x) \| \leq L \| y - x \| \quad \forall x, y \in \operatorname{dom}(f)
$$

Likewise, the **gradient** (first derivative) of a function is Lipschitz continuous with constant $L$ if

$$
\| \nabla f(y) - \nabla f(x) \| \leq L \|y - x \| \quad \forall x, y \in \operatorname{dom}(f)
$$

#### Deriving a quadratic upper bound

For the next steps we follow slide 1.13 of [Lieven Vandenberghe’s ECE236C Spring 2022 lecture notes on the gradient method](https://www.seas.ucla.edu/~vandenbe/236C/lectures/gradient.pdf)

Recall the Cauchy-Schwarz inequality

$$
|\langle x, y \rangle| \leq \| x \| \| y \|
$$

Applying the Cauchy-Schwartz inequality to the Lipschitz gradient condition gives

$$
\langle \nabla f(y) - \nabla f(x), y - x \rangle \leq L \|y - x\|^2 \qquad \forall x, y \in \operatorname{dom}(f)
$$

Define the function $g(t)$ as

$$
g(t) = f(x + t(y - x))
$$

If the domain of $f$ is convex, then $g(t)$ is well-defined $\forall t \in [0, 1]$.

Using the definition of $g(t)$, the chain rule of multivariate calculus, and the previous inequality we have

$$
\begin{aligned}
g'(t) - g'(0) &= \langle \nabla f(x + t(y-x)) - \nabla f(x), x + t(y-x) - x \rangle \\
&\leq L \| x + t(y-x) - x \|^2 \\
&= L \| t(y-x) \|^2 \\
&= t^2 L\|y-x\|^2 \\
&\leq tL\|y-x\|^2 \quad \text{for } t \in [0,1] \\
\to g'(t) &\leq g'(0) + tL\|y-x\|^2 \quad \text{for } t \in [0,1]
\end{aligned}
$$

Using the definition of $g(t)$ we can rewrite $f(y)$ in terms of an integral by using the fundamental theorem of calculus

$$
f(y) = g(1) = g(0) + \int_0^1 g'(t),dt
$$

Integrating the second term from $0$ to $t$ and using the previous inequality and the derivative of $g(t)$ we obtain

$$
\begin{aligned}
\int_0^1 g'(t) dt &\leq \int_0^1 \left(g'(0) + tL\|y-x\|^2\right)dt \\
&= \langle \nabla f(x) , y-x \rangle + \frac{L}{2}\|y-x\|^2
\end{aligned}
$$

Substituting back into the expression for $f(y)$ we obtain the **quadratic upper bound**

$$
f(y) \leq f(x) + \langle \nabla f(x) , y - x \rangle + \frac{L}{2}\|y - x\|^2 \quad \forall x, y \in \operatorname{dom}(f)
$$

> This means that the function value grows no faster than a quadratic.

### The Polyak-Lojasiewicz inequality

A function is said to satisfy the **Polyak-Lojasiewicz inequality** if the following condition holds:

$$
\|\nabla f(x)\|^2 \geq \mu\left(f(x) - f^*\right) \quad \forall x
$$

where $f^*$ is the minimum function value.

> This means that the [norm of the gradient] grows at least as fast as a quadratic as the function value moves away from the optimal function value.

> Additionally, this implies that every stationary point of $f(x)$ is a global minimum.

### Gradient descent

The gradient descent update simply takes a step in the direction of the negative gradient:

$$
x_{k+1} = x_k - \eta \nabla f(x_k)
$$

We are now ready to prove convergence of gradient descent under the PL inequality i.e. [Theorem 1 of Karimi et al.](https://arxiv.org/abs/1608.04636)

Rearranging the gradient descent update gives the difference

$$
x_{k+1} - x_k = - \eta \nabla f(x_k)
$$

Using the gradient descent update rule in the quadratic upper bound condition (from Lipschitz continuity of the gradient) we obtain

$$
\begin{aligned}
f(x_{k+1}) &\leq f(x_k) + \langle \nabla f(x_k) , x_{k+1} - x_k \rangle + \frac{L}{2}\|x_{k+1} - x_k\|^2 \\
&= f(x_k) + \langle \nabla f(x_k) , -\eta \nabla f(x_k) \rangle + \frac{L}{2}\|- \eta \nabla f(x_k)\|^2 \\
&= f(x_k) - \eta|\nabla f(x_k)|^2 + \eta^2 \left(\frac{L}{2}\right)\|\nabla f(x_k)\|^2 \\
&= f(x_k) + \left(-\eta + \eta^2 \left(\frac{L}{2}\right)\right)\|\nabla f(x_k)\|^2 \\
\to; f(x_{k+1}) - f(x_k) &\leq \left(-\eta + \eta^2 \left(\frac{L}{2}\right)\right)\|\nabla f(x_k)\|^2
\end{aligned}
$$

If the stepsize is chosen so that the coefficient on the righthand side is negative, then using the Polyak-Lojasiewicz inequality gives

$$
f(x_{k+1}) - f(x_k) \leq \left(-\eta + \frac{\eta^2 L}{2}\right)\mu\left(f(x_k) - f^*\right)
$$

The range of permissible stepsizes is $[0, 2/L]$ with the best rate achieved with a stepsize of $1/L$. Under this choice, we obtain

$$
f(x_{k+1}) - f(x_k) \leq -\frac{\mu}{2L}\left(f(x_k) - f^*\right)
$$

Adding $f(x_k) – f^*$ to both sides gives

$$
f(x_{k+1}) - f^* \leq \left(1 - \frac{\mu}{2L}\right)\left(f(x_k) - f^*\right)
$$

Dividing by $f(x_k) – f^*$ gives the linear (geometric) convergence rate

$$
\frac{f(x_{k+1}) - f^*}{f(x_k) - f^*} \leq 1 - \frac{\mu}{2L}
$$

> This shows that the [difference between the current function value and the minimum] decreases at least as fast as a geometric series, with a rate determined by the ratio of the PL and Lipschitz constants.

## Why would control systems researchers care about this?

The Polyak-Lojasiewicz inequality is key to [analysis of convergence of policy gradient for LQR](https://arxiv.org/abs/1801.05039) and [LQR with multiplicative noise](https://arxiv.org/abs/1905.13547).

## Links

- [Karimi et al. 2016 on arXiv](https://arxiv.org/abs/1608.04636)
- [Polyak 1963 on ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/0041555363903823)

## Keywords

- Nonconvex
- Optimization
- Polyak-Lojasiewicz inequality
- Gradient domination
- Convergence
- Global
