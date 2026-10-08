<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Portfolio Optimization of Relativistic Value at Risk

Topics include Portfolio optimization, Coherent risk measures, Kaniadakis entropy, Power cones, Drawdown risk.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces a coherent risk measure based on Kaniadakis entropy, derives power-cone formulations, and extends the approach to drawdown risk and convex portfolio optimization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This work presents a new risk measure that is a generalization of Entropic Value at Risk (EVaR). We define the Relativistic Value at Risk (RLVaR) as a special case of φ-divergence risk measures based on Kaniadakis entropy. The RLVaR is a coherent risk measure that is bounded between EVaR and essential supremum (ess sup). First, we define the RLVaR using the dual representation of φ-divergence risk measures, and we use the power cone to express the RLVaR as a conic problem. Due the limitations for modeling of dual formulation, we recover the primal formulation of RLVaR using the cone duality theorem. This primal formulation allows us to use RLVaR in several convex portfolio optimization problems like maximize the risk adjusted return ratio, constraints on risk or risk parity. Also, we extend these framework to drawdowns distribution, defining the relativistic drawdown at risk (RLDaR). Then, we run some numerical examples using Python, Riskfolio-Lib package and MOSEK solver.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, we test the efficiency of RLVaR and RLDaR portfolio optimization frameworks in large scale problems respect EVaR and entropic drawdown at risk (EDaR).
