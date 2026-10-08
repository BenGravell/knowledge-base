<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Entropic Portfolio Optimization: A Disciplined Convex Programming Framework

Topics include Portfolio optimization, Entropic value at risk, Convex optimization, Exponential cones, Drawdown risk.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Expresses entropic value-at-risk and drawdown risk using exponential cones, enabling convex portfolio objectives, risk constraints, and risk parity with standard solvers.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This work presents a disciplined convex programming framework for entropic value at risk (EVaR) based on exponential cone programming. This framework allows us to use EVaR in several convex portfolio optimization problems like maximize the EVaR adjusted return, constraints on EVaR or risk parity EVaR. Also, we propose a new portfolio optimization framework based on an extension of EVaR but applied to drawdowns distribution that we called entropic drawdown at risk (EDaR). Then, we run some numerical examples of EVaR and EDaR portfolio optimization frameworks using Python, Riskfolio-Lib package and MOSEK solver. Finally, we test the efficiency of EVaR and EDaR frameworks in large scale problems respect to conditional value at risk (CVaR) and conditional drawdown at risk (CDaR).
