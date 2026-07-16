<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-Driven Critic-Free Policy Iteration for Continuous-Time Linear Quadratic Regulation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

For continuous-time linear quadratic regulation with unknown system matrices, data-driven off-policy policy iteration typically estimates the value matrix and the improved feedback gain through a joint critic - actor regression. We show that the critic is not needed in the policy-improvement step. The key is to anchor the Riccati equation at a known stabilizing gain and express optimality as a policy-space residual. An endpoint null-space projection then removes the value-matrix term from the integral data equation. This yields a critic-free, actor-only least-squares update computed directly from input-state data. Under a verifiable projected rank condition, the resulting data equation is equivalent to the policy-space residual equation, and each update coincides with the Kleinman iteration. Thus, the stabilizing and convergence properties of Kleinman iteration are retained without a critic regression. We further show that the conventional off-policy full-rank condition decomposes into an endpoint critic rank condition and a projected actor rank condition. The proposed method removes the rank requirement needed for critic identification while retaining the one needed for policy improvement. The repeated least-squares dimension is reduced from n(n+1)/2+mn to mn.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, comparative simulations validate the effectiveness of the proposed algorithm.
