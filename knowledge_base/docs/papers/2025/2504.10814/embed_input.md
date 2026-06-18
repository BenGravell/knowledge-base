An Operator Splitting Method for Large-Scale CVaR-Constrained Quadratic Programs

We introduce a fast and scalable method for solving quadratic programs with conditional value-at-risk (CVaR) constraints. While these problems can be formulated as standard quadratic programs, the number of variables and constraints grows linearly with the number of scenarios, making general-purpose solvers impractical for large-scale problems. Our method combines operator splitting with a specialized O(mlog m) algorithm for projecting onto CVaR constraints, where m is the number of scenarios. The method alternates between solving a linear system and performing parallel projections, onto CVaR constraints using our specialized algorithm and onto box constraints by simple clipping. Numerical examples from several application domains demonstrate that our method outperforms general-purpose solvers by several orders of magnitude on problems with up to millions of scenarios. Our method is implemented in an open-source package called CVQP.

## Introduction

Many applications in finance and engineering require controlling the risk of extreme outcomes. A widely used measure for tail risk is the *conditional value-at-risk* (CVaR), defined as the expected value of losses exceeding a given quantile. CVaR is a coherent and convex risk measure, so optimization problems involving CVaR can be reliably and efficiently solved.

Many practical applications, from portfolio optimization to quantile regression, can be formulated as quadratic programs with CVaR constraints. While these problems are convex and can be reformulated as standard quadratic programs, the number of variables and constraints grows linearly with the number of scenarios. For problems with many scenarios, general-purpose solvers become prohibitively slow or fail entirely. To address this challenge, we develop a fast and scalable method for solving quadratic programs with CVaR constraints.

We present two main contributions. First, we develop an $O{({m{\log m}})}$ algorithm for projecting onto CVaR constraints, where $m$ is the number of scenarios. Building on this algorithm, our second contribution is an operator splitting method for solving large-scale CVaR-constrained quadratic programs. The method alternates between solving a linear system and performing parallel projections, onto CVaR constraints using our specialized algorithm and onto box constraints by simple clipping.

## Conditional value-at-risk (CVaR)

The conditional value-at-risk (CVaR) at level $\beta$ is a risk measure that captures the expected value over the worst $({1 - \beta})$ fraction of outcomes of a real-valued random variable. For a random variable $X$ representing losses (where larger values are worse), we first define the value-at-risk (VaR) at level $\beta$ as
