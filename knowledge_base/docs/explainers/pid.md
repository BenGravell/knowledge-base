# Proportional Integral Derivative (PID) control

*Proportional Integral Derivative (PID)* is a feedback control scheme which generates control actions as a weighted linear combination of three terms:

1. Proportional to the error
2. Integral of the error
3. Derivative of the error

The weights are referred to as feedback gains, and can be tuned according to model-free heuristics e.g. the [Ziegler–Nichols method](https://en.wikipedia.org/wiki/Ziegler%E2%80%93Nichols_method).

Despite its simplicity, PID is extremely (often surprisingly) effective in practice on a wide variety of systems, even when stochastic disturbances, plant nonlinearities, input delays, and other challenging aspects are present.

Learn more with these resources:

- ["Advanced PID Control" by Karl J. Åström & Tore Hägglund](https://www.isa.org/products/advanced-pid-control)
- [Proportional–integral–derivative controller - Wikipedia](https://en.wikipedia.org/wiki/Proportional%E2%80%93integral%E2%80%93derivative_controller)
- [Proportional-Integral-Derivative (PID) Controllers - MATLAB](https://www.mathworks.com/help/control/ug/proportional-integral-derivative-pid-controllers.html)
- Benjamin Recht's blog posts, emphasizing the relationship between PID and gradient-based optimization
  - [The Best Things in Life Are Model Free](https://archives.argmin.net/2018/04/19/pid/)
  - [Integral Action](https://www.argmin.net/p/integral-action)
  - [Advanced Simplicity](https://www.argmin.net/p/advanced-simplicity)