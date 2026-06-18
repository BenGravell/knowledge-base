<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Gaussian Networks for Direct Adaptive Control

Topics include Adaptive control, Radial basis functions, Neural control, Lyapunov stability, Nonlinear systems, Tracking control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes a direct adaptive nonlinear controller that uses Gaussian radial basis function networks to compensate unknown plant nonlinearities when a linear parameterization is unavailable. The work links smoothness assumptions to network construction and derives a Lyapunov-stable weight update, making it an early neural adaptive control template.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A direct adaptive tracking control architecture is proposed and evaluated for a class of continuous-time nonlinear dynamic systems for which an explicit linear parameterization of the uncertainty in the dynamics is either unknown or impossible. The architecture employs a network of gausian radial basis functions to adaptively compensate for the plant nonlinearities. Under mild assumptions about the degree of smoothness exhibited by the nonlinear functions, the algorithm is proven to be stable, with tracking errors converging to a neighborhood of zero. A constructive procedure is detailed, which directly translates the assumed smoothness properties of the nonlinearities involved into a specification of the network required to represent the plant to a chosen degree of accuracy. A stable weight adjustment mechanism is then determined using Lyapunov theory. The network construction and performance of the resulting controller are illustrated through simulations with an example system.
