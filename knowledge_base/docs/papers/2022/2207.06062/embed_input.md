Provably Stable Learning Control of Linear Dynamics with Multiplicative Noise

Control of linear dynamics with multiplicative noise naturally introduces robustness against dynamical uncertainty. Moreover, many physical systems are subject to multiplicative disturbances. In this work we show how these dynamics can be identified from state trajectories. The least-squares scheme enables exploitation of prior information and comes with practical data-driven confidence bounds and sample complexity guarantees. We complement this scheme with an associated control synthesis procedure for LQR which robustifies against distributional uncertainty, guaranteeing stability with high probability and converging to the true optimum at a rate inversely proportional with the sample count. Throughout we exploit the underlying multi-linear problem structure through tensor algebra and completely positive operators. The scheme is validated through numerical experiments.

## Introduction

This document is a template for LaTeX. If you are reading a paper or PDF version of this document, please download the electronic file, trans_jour.tex, from the IEEE Web site at so you can use it to prepare your manuscript. If you would prefer to use LaTeX, download IEEE's LaTeX style and sample files from the same Web page. You can also explore using the Overleaf editor at

If your paper is intended for a conference, please contact your conference editor concerning acceptable word processor formats for your particular conference.

A conclusion section is not required. Although a conclusion may review the main points of the paper, do not replicate the abstract as the conclusion. A conclusion might elaborate on the importance of the work or suggest applications and extensions.

Appendixes, if needed, appear before the acknowledgment.

magnetic flux density, magnetic induction

Figure 1: Magnetization as a function of applied field. It is good practice to explain the significance of the figure in the caption.

In order to preserve the figures' integrity across multiple computer platforms, we accept files in the following formats:.EPS/.PDF/.PS. All fonts must be embedded or text converted to outlines in order to achieve the best-quality results.

IEEE will do the final formatting of your paper. If your paper is intended for a conference, please observe the conference page limits.

### Abbreviations and Acronyms

Define abbreviations and acronyms the first time they are used in the text, even after they have already been defined in the abstract. Abbreviations such as IEEE, SI, ac, and dc do not have to be defined. Abbreviations that incorporate periods should not have spaces: write "C.N.R.S.," not "C. N. R. S." Do not use abbreviations in the title unless they are unavoidable (for example, "IEEE" in the title of this article).

### Other Recommendations

Use one space after periods and colons. Hyphenate complex modifiers: "zero-field-cooled magnetization." Avoid dangling participles, such as, "Using (1")), the potential was calculated." \It is not clear who or what used ([1")).\] Write instead, "The potential was calculated by using (1"))," or "Using (1")), we calculated the potential."

Use a zero before decimal points: "0.25," not ".25." Use "cm^3^," not "cc." Indicate sample dimensions as "0.1 cm $\times$ 0.2 cm," not "0.1 $\times$ 0.2...
