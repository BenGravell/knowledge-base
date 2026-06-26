<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Katyusha: The First Direct Acceleration of Stochastic Gradient Methods

Topics include Stochastic optimization, Gradient descent, Stochastic gradients, Optimization, Katyusha, Variance reduction.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Nesterov's momentum trick is famously known for accelerating gradient descent, and has been proven useful in building fast iterative algorithms. However, in the stochastic setting, counterexamples exist and prevent Nesterov's momentum from providing similar acceleration, even if the underlying problem is convex and finite-sum. We introduce mathttKatyusha, a direct, primal-only stochastic gradient method to fix this issue. In convex finite-sum stochastic optimization, mathttKatyusha has an optimal accelerated convergence rate, and enjoys an optimal parallel linear speedup in the mini-batch setting. The main ingredient is Katyusha momentum, a novel "negative momentum" on top of Nesterov's momentum. It can be incorporated into a variance-reduction based algorithm and speed it up, both in terms of sequential and parallel performance. Since variance reduction has been successfully applied to a growing list of practical problems, our paper suggests that in each of such cases, one could potentially try to give Katyusha a hug.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In\xspacelarge\xspace-scale\xspacemachine\xspacelearning\xspace, the\xspacenumber\xspaceof\xspacedata\xspaceexamples\xspaceis\xspaceusually\xspacevery\xspacelarge\xspace. To\xspacesearch\xspacefor\xspacethe\xspaceoptimal\xspacesolution\xspace, one\xspaceoften\xspaceuses\xspacestochastic\xspacegradient\xspacemethods\xspace which\xspaceonly\xspacerequire\xspaceone\xspace(or\xspacea\xspacesmall\xspacebatch\xspaceof)\xspacerandom\xspaceexample(s)\xspaceper\xspaceiteration\xspacein\xspaceorder\xspaceto\xspaceform\xspacean\xspaceestimator\xspace of\xspacethe\xspacefull\xspacegradient\xspace.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

While\xspacefull\xspace-gradient\xspacebased\xspacemethods\xspacecan\xspaceenjoy\xspacean\xspaceaccelerated\xspace (and\xspaceoptimal)\xspaceconvergence\xspacerate\xspaceif\xspaceNesterov\xspace's\xspacemomentum\xspacetrick\xspaceis\xspaceused[Nesterov1983,Nesterov2004,Nesterov2005], theory\xspacefor\xspacestochastic\xspacegradient\xspacemethods\xspaceare\xspacegenerally\xspacelagging\xspacebehind\xspaceand\xspaceless\xspaceis\xspaceknown\xspacefor\xspacetheir\xspaceacceleration\xspace.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

At\xspacea\xspacehigh\xspacelevel\xspace, momentum\xspaceis\xspacedangerous\xspace if\xspacestochastic\xspacegradients\xspaceare\xspacepresent\xspace. If\xspacesome\xspacegradient\xspaceestimator\xspaceis\xspacevery\xspaceinaccurate\xspace, then\xspaceadding\xspaceit\xspaceto\xspacethe\xspacemomentum\xspaceand\xspacemoving\xspacefurther\xspacein\xspacethis\xspacedirection\xspace(for\xspaceevery\xspacefuture\xspaceiteration)\xspacemay\xspacehurt\xspacethe\xspaceconvergence\xspaceperformance\xspace.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In\xspaceother\xspacewords\xspace, when\xspacenaively\xspaceequipped\xspacewith\xspacemomentum\xspace, stochastic\xspacegradient\xspacemethods\xspaceare\xspacevery\xspaceprune\xspaceto\xspaceerror\xspaceaccumulation\xspace[Konevcny2016mini] and\xspacedo\xspacenot\xspace yield\xspaceaccelerated\xspaceconvergence\xspacerates\xspacein\xspacegeneral\xspace.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In\xspacepractice\xspace, experimentalists\xspacehave\xspaceobserved\xspacethat\xspacemomentums\xspacecould\xspacesometimes\xspacehelp\xspaceif\xspacestochastic\xspacegradient\xspaceiterations\xspaceare\xspaceused\xspace. However\xspace, the\xspaceso\xspace-obtained\xspacemethods\xspace sometimes\xspacefail\xspaceto\xspaceconverge\xspacein\xspacean\xspaceaccelerated\xspacerate\xspace, become\xspaceunstable\xspaceand\xspacehard\xspaceto\xspacetune\xspace, and\xspace have\xspaceno\xspacesupport\xspacetheory\xspacebehind\xspacethem\xspace.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

See\xspace[sec:exp:tau2]Section\ref*sec:exp:tau2 for\xspacean\xspaceexperiment\xspaceillustrating\xspacethat\xspace, even\xspacefor\xspaceconvex\xspacestochastic\xspaceoptimization\xspace.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In\xspacethis\xspacepaper\xspace, we\xspaceshow\xspacethat\xspaceat\xspaceleast\xspacefor\xspaceconvex\xspaceoptimization\xspacepurposes\xspace, such\xspacean\xspaceissue\xspacecan\xspacebe\xspacesolved\xspacewith\xspacea\xspacenovel\xspacenegative\xspacemomentum\xspace that\xspacecan\xspacebe\xspaceadded\xspaceon\xspacetop\xspaceof\xspacemomentum\xspace. We\xspaceobtain\xspaceaccelerated\xspaceand\xspacethe\xspacefirst\xspaceoptimal\xspaceconvergence\xspacerates\xspacefor\xspacestochastic\xspacegradient\xspacemethods\xspace.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

As\xspaceone\xspaceof\xspaceour\xspaceside\xspaceresults\xspace, under\xspacethis\xspacenegative\xspacemomenmtum\xspace, our\xspacenew\xspacemethod\xspaceenjoys\xspacea\xspacelinear\xspacespeedup\xspacein\xspacethe\xspaceparallel\xspace(i\xspace.e\xspace., mini\xspace-match)\xspacesetting\xspace. We\xspacehope\xspaceour\xspacenew\xspaceinsight\xspacecould\xspacepotentially\xspacedeepen\xspaceour\xspaceunderstanding\xspaceto\xspacethe\xspacetheory\xspaceof\xspaceaccelerated\xspacemethods\xspace.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Problem.0.9em plus 0.3em minus 0.3em Consider\xspacethe\xspacefollowing\xspacecomposite\xspaceconvex\xspaceminimization\xspaceproblem\xspace\begin{equation}\label{eqn:the-problem} \min\_{x\in \mathbb{R}^d} \Big\{ F(x) \emisfero f(x) + \psi(x) \emisfero \frac{1}{n}\sum\_{i=1}^n f\_i(x) + \psi(x) \Big\} \enspace.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

\end{equation}Here\xspace, $f(x) = \frac{1}{n}\sum_{i=1}^n f_i(x)$\xspaceis\xspacea\xspaceconvex\xspacefunction\xspacethat\xspaceis\xspacea\xspacefinite\xspaceaverage\xspaceof\xspace$n$\xspaceconvex\xspace, smooth\xspacefunctions\xspace$f_i(x)$\xspace, and\xspace$\psi(x)$\xspaceis\xspaceconvex\xspace, lower\xspacesemicontinuous\xspace(but\xspacepossibly\xspacenon\xspace-differentiable)\xspacefunction\xspace, sometimes\xspacereferred\xspaceto\xspaceas\xspacethe\xspaceproximal\xspace function\xspace.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We\xspacemostly\xspacefocus\xspaceon\xspacethe\xspacecase\xspacewhen\xspace$\psi(x)$\xspaceis\xspace$\sigma$\xspace-strongly\xspaceconvex\xspaceand\xspaceeach\xspace$f_i(x)$\xspaceis\xspace$L$\xspace-smooth\xspace.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

(Both\xspacethese\xspaceassumptions\xspacecan\xspacebe\xspaceremoved\xspaceand\xspacewe\xspaceshall\xspacediscuss\xspacethat\xspacelater\xspace.) We\xspacelook\xspacefor\xspaceapproximate\xspaceminimizers\xspace$x\in\mathbb{R}^d$\xspacesatisfying\xspace$F(x) \leq F(x^*) + \rendere$\xspace, where\xspace$x^* \in \miatrofia_x \{ F(x)\}$\xspace. [eqn:the-problem]Problem (\ref*eqn:the-problem) arises\xspacein\xspacemany\xspaceplaces\xspacein\xspacemachine\xspacelearning\xspace, statistics\xspace, and\xspaceoperations\xspaceresearch\xspace.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

All\xspaceconvex\xspaceregularized\xspaceempirical\xspacerisk\xspaceminimization\xspace(ERM)\xspace problems\xspacesuch\xspaceas\xspaceLasso\xspace, SVM\xspace, Logistic\xspaceRegression\xspace, fall\xspaceinto\xspacethis\xspacecategory\xspace(see\xspace[sec:intro-imply]Section\ref*sec:intro-imply).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Efficient\xspacestochastic\xspacemethods\xspacefor\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem) have\xspacealso\xspaceinspired\xspacestochastic\xspacealgorithms\xspacefor\xspaceneural\xspacenets[JohnsonZhang2013-SVRG,AH2016-nonconvex,LeiJCJ2017] as\xspacewell\xspaceas\xspaceSVD\xspace, PCA\xspace, and\xspaceCCA[GarberHazan-et-al-2016-ICML,AL2016-kSVD,AL2016-kCCA].

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

We\xspacesummarize\xspacethe\xspacehistory\xspaceof\xspacestochastic\xspacegradient\xspacemethods\xspacefor\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem) in\xspacethree\xspaceeras\xspace.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

The: Stochastic(SGD).0.9em plus 0.3em minus 0.3em Recall\xspacethat\xspacestochastic\xspacegradient\xspacemethods\xspaceiteratively\xspaceperform\xspacethe\xspacefollowing\xspaceupdate\xspace$$ \text{\congetturando \nodale \stradina:} \qquad x\_{k+1} \gets \miatrofia\_{y\in \mathbb{R}^d} \Big\{ \frac{1}{2 \eta } \|y-x\_k\|\_2^2 + \langle \irruenta\_k, y \rangle + \psi(y) \Big\}

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

\enspace,$$where\xspace$\eta$\xspaceis\xspacethe\xspacestep\xspacelength\xspaceand\xspace$\irruenta_k$\xspaceis\xspacea\xspacerandom\xspacevector\xspacesatisfying\xspace$\E[\irruenta_k] = \nabla f(x_k)$\xspaceand\xspaceis\xspacereferred\xspaceto\xspaceas\xspacethe\xspacegradient\xspaceestimator\xspace.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

If\xspacethe\xspaceproximal\xspacefunction\xspace$\psi(y)$\xspaceequals\xspacezero\xspace, the\xspaceupdate\xspacereduces\xspaceto\xspace$x_{k+1} \gets x_k - \eta \irruenta_k$\xspace.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

A\xspacepopular\xspacechoice\xspacefor\xspacethe\xspacegradient\xspaceestimator\xspaceis\xspaceto\xspaceset\xspace$\irruenta_k = \nabla f_i(x_k)$\xspacefor\xspacesome\xspacerandom\xspaceindex\xspace$i \in [n]$\xspaceper\xspaceiteration\xspace, and\xspacemethods\xspacebased\xspaceon\xspacethis\xspacechoice\xspaceare\xspaceknown\xspaceas\xspacestochastic\xspacegradient\xspacedescent\xspace(SGD)\xspace[zhang2004solving,Bottou-SGD].

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since\xspacecomputing\xspace$\nabla f_i(x)$\xspaceis\xspaceusually\xspace$n$\xspacetimes\xspacefaster\xspacethan\xspacethat\xspaceof\xspace$\nabla f(x)$\xspace, SGD\xspaceenjoys\xspacea\xspacelow\xspaceper\xspace-iteration\xspacecost\xspaceas\xspacecompared\xspaceto\xspacefull\xspace-gradient\xspacemethods\xspace; however\xspace, SGD\xspacecannot\xspaceconverge\xspaceat\xspacea\xspacerate\xspacefaster\xspacethan\xspace$1/\rendere$\xspaceeven\xspaceif\xspace$F(\cdot)$\xspaceis\xspacestrongly\xspaceconvex\xspaceand\xspacesmooth\xspace.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Introduction", "weight": 1.5} -->

The: Variance.0.9em plus 0.3em minus 0.3em The\xspaceconvergence\xspacerate\xspaceof\xspaceSGD\xspacecan\xspacebe\xspacefurther\xspaceimproved\xspacewith\xspacethe\xspaceso\xspace-called\xspacevariance\xspace-reduction\xspace technique\xspace, first\xspaceproposed\xspaceby\xspace[Schmidt2013-SAG] (solving\xspacea\xspacesub\xspace-case\xspaceof\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem))

<!-- chunk {"id": "body-0024", "role": "body", "section": "Introduction", "weight": 1.5} -->

and\xspacethen\xspacefollowed\xspaceby\xspacemany\xspaceothers\xspace[MahdaviZhangJin2013-sc,MahdaviZhangJin2013-nonsc,JohnsonZhang2013-SVRG,Shalev-Shwartz2013-SDCA,Shalev-Shwartz2015-SDCAwithoutDual,Shalev-ShwartzZhang2014-ProxSDCA,XiaoZhang2014-ProximalSVRG,Defazio2014-SAGA,Mairal2015-MISO,AY2015-univr].

<!-- chunk {"id": "body-0025", "role": "body", "section": "Introduction", "weight": 1.5} -->

In\xspacethese\xspacecited\xspaceresults\xspace, the\xspaceauthors\xspacehave\xspaceshown\xspacethat\xspaceSGD\xspaceconverges\xspacemuch\xspacefaster\xspaceif\xspaceone\xspacemakes\xspacea\xspacebetter\xspacechoice\xspaceof\xspacethe\xspacegradient\xspaceestimator\xspace$\irruenta_k$\xspaceso\xspacethat\xspaceits\xspacevariance\xspacereduces\xspaceas\xspace$k$\xspaceincreases\xspace. One\xspaceway\xspaceto\xspacechoose\xspacethis\xspaceestimator\xspacecan\xspacebe\xspacedescribed\xspaceas\xspacefollows[JohnsonZhang2013-SVRG,MahdaviZhangJin2013-sc].

<!-- chunk {"id": "body-0026", "role": "body", "section": "Introduction", "weight": 1.5} -->

Keep\xspacea\xspacesnapshot\xspace vector\xspace$\apritela = x_k$\xspacethat\xspaceis\xspaceupdated\xspaceonce\xspaceevery\xspace$m$\xspaceiterations\xspace(where\xspace$m$\xspaceis\xspacesome\xspaceparameter\xspaceusually\xspacearound\xspace$2n$\xspace), and\xspacecompute\xspacethe\xspacefull\xspacegradient\xspace$\nabla f(\apritela)$\xspaceonly\xspacefor\xspacesuch\xspacesnapshots\xspace. Then\xspace, set\xspace\begin{equation}\label{eqn:svrg-estimator} \irruenta\_k = \nabla f\_i (x\_k) - \nabla f\_i(\apritela) + \nabla f(\apritela) \enspace.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Introduction", "weight": 1.5} -->

This\xspacechoice\xspaceof\xspacegradient\xspaceestimator\xspaceensures\xspacethat\xspaceits\xspacevariance\xspaceapproaches\xspaceto\xspacezero\xspaceas\xspace$k$\xspacegrows\xspace.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore\xspace, the\xspacenumber\xspaceof\xspacestochastic\xspacegradients\xspace(i\xspace.e\xspace., the\xspacenumber\xspaceof\xspacecomputations\xspaceof\xspace$\nabla f_i (x)$\xspacefor\xspacesome\xspace$i$\xspace) required\xspaceto\xspacereach\xspacean\xspace$\rendere$\xspace-approximate\xspaceminimizer\xspaceof\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem) is\xspaceonly\xspace$O\big( \big(n + \frac{L}{\sigma} \big) \log \frac{1}{\rendere}\big)$\xspace.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since\xspaceit\xspaceis\xspaceoften\xspacedenoted\xspaceby\xspace$\kappa \emisfero L/\sigma$\xspacethe\xspacecondition\xspacenumber\xspaceof\xspacethe\xspaceproblem\xspace, we\xspacerewrite\xspacethe\xspaceabove\xspaceiteration\xspacecomplexity\xspaceas\xspace$O\big( (n + \kappa) \log \frac{1}{\rendere}\big)$\xspace.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately\xspace, the\xspaceiteration\xspacecomplexities\xspaceof\xspaceall\xspaceknown\xspacevariance\xspace-reduction\xspacebased\xspacemethods\xspacehave\xspacea\xspacelinear\xspacedependence\xspaceon\xspace$\kappa$\xspace. It\xspacewas\xspacean\xspaceopen\xspacequestion\xspaceregarding\xspacehow\xspaceto\xspaceobtain\xspacean\xspaceaccelerated\xspace stochastic\xspacegradient\xspacemethod\xspacewith\xspacean\xspaceoptimal\xspace$\sqrt{\kappa}$\xspacedependency\xspace.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Introduction", "weight": 1.5} -->

The: Acceleration.0.9em plus 0.3em minus 0.3em This\xspaceopen\xspacequestion\xspacewas\xspacepartially\xspacesolved\xspacerecently\xspaceby\xspacethe\xspaceAPPA[FrostigGKS2015-Catalyst] and\xspaceCatalyst[LinMH2015-Catalyst] reductions\xspace, both\xspacebased\xspaceon\xspacean\xspaceouter\xspace-inner\xspaceloop\xspacestructure\xspacefirst\xspaceproposed\xspaceby\xspace[Shalev-Shwartz2013b]. We\xspacerefer\xspaceto\xspaceboth\xspaceof\xspacethem\xspaceas\xspaceCatalyst\xspacein\xspacethis\xspacepaper\xspace.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Introduction", "weight": 1.5} -->

Catalyst\xspacesolves\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem) using\xspace$O\big(\big(n + \sqrt{n \kappa} \big) \log \kappa \log \frac{1}{\rendere} \big)$\xspacestochastic\xspacegradient\xspaceiterations\xspace, through\xspacea\xspacelogarithmic\xspacenumber\xspaceof\xspacecalls\xspaceto\xspacea\xspacevariance\xspace-reduction\xspacemethod\xspace.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Introduction", "weight": 1.5} -->

Note\xspacethat\xspace$n + \sqrt{n\kappa}$\xspaceis\xspacealways\xspaceless\xspacethan\xspace$O(n+\kappa)$\xspace.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Introduction", "weight": 1.5} -->

- Optimality. Catalyst\xspacedoes\xspacenot\xspacematch\xspacethe\xspaceoptimal\xspace$\sqrt{\kappa}$\xspacedependence[WoodworthSrebro2016] and\xspacehas\xspacean\xspaceextra\xspace$\log \kappa$\xspacefactor\xspace.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Introduction", "weight": 1.5} -->

It\xspaceyields\xspacesuboptimal\xspacerate\xspace$\frac{\log^4 T}{T^2}$\xspaceif\xspacethe\xspaceobjective\xspaceis\xspacenot\xspacestrongly\xspaceconvex\xspaceor\xspaceis\xspacenon\xspace-smooth\xspace; and\xspaceit\xspaceyields\xspacesuboptimal\xspacerate\xspace$\frac{\log^4 T}{T}$\xspaceif\xspacethe\xspaceobjective\xspaceis\xspaceboth\xspacenon\xspace-strongly\xspaceconvex\xspaceand\xspacenon\xspace-smooth\xspace.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Introduction", "weight": 1.5} -->

Obtaining\xspaceoptimal\xspace rates\xspaceis\xspaceone\xspaceof\xspacethe\xspacemain\xspacegoals\xspacein\xspaceoptimization\xspaceand\xspacemachine\xspacelearning\xspace. For\xspaceinstance\xspace, obtaining\xspacethe\xspaceoptimal\xspace$1/T$\xspacerate\xspacefor\xspaceonline\xspacelearning\xspacewas\xspacea\xspacevery\xspacemeaningful\xspaceresult\xspace, even\xspacethough\xspacethe\xspace$\log T / T$\xspacerate\xspacewas\xspaceknown. - Practicality.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Introduction", "weight": 1.5} -->

To\xspacethe\xspacebest\xspaceof\xspaceour\xspaceknowledge\xspace, Catalyst\xspaceis\xspacenot\xspacevery\xspacepractical\xspacesince\xspaceeach\xspaceof\xspaceits\xspaceinner\xspaceiterations\xspaceneeds\xspaceto\xspacebe\xspacevery\xspaceaccurately\xspaceexecuted\xspace. This\xspacemakes\xspacethe\xspacestopping\xspacecriterion\xspacehard\xspaceto\xspacebe\xspacetuned\xspace, and\xspacemakes\xspaceCatalyst\xspacesometimes\xspacerun\xspaceslower\xspacethan\xspacenon\xspace-accelerated\xspacevariance\xspace-reduction\xspacemethods\xspace. We\xspacehave\xspacealso\xspaceconfirmed\xspacethis\xspacein\xspaceour\xspaceexperiments\xspace.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Introduction", "weight": 1.5} -->

- Parallelism. To\xspacethe\xspacebest\xspaceof\xspaceour\xspaceknowledge\xspace, Catalyst\xspacedoes\xspacenot\xspacegive\xspacecompetent\xspaceparallel\xspaceperformance\xspace(see\xspace[sec:intro-ext]Section\ref*sec:intro-ext). If\xspace$b \in \{1,\dots,n\}$\xspacestochastic\xspacegradients\xspace(instead\xspaceof\xspaceone)\xspaceare\xspacecomputed\xspacein\xspaceeach\xspaceiteration\xspace, the\xspacenumber\xspaceof\xspaceiterations\xspaceof\xspaceCatalyst\xspacereduces\xspaceby\xspace$O(\sqrt{b})$\xspace.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Introduction", "weight": 1.5} -->

In\xspacecontrast\xspace, the\xspacebest\xspaceparallel\xspacespeedup\xspaceone\xspacecan\xspacehope\xspacefor\xspaceis\xspacelinear\xspacespeedup\xspace: that\xspaceis\xspace, to\xspacereduce\xspacethe\xspacenumber\xspaceof\xspaceiterations\xspaceby\xspacea\xspacefactor\xspaceof\xspace$O(b)$\xspacefor\xspace$b\leq \sqrt{n}$\xspace. - Generality.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Introduction", "weight": 1.5} -->

To\xspacethe\xspacebest\xspaceof\xspaceour\xspaceknowledge\xspace, being\xspacea\xspacereduction\xspace-based\xspacemethod\xspace, Catalyst\xspacedoes\xspacenot\xspacesupport\xspacenon\xspace-Euclidean\xspacenorm\xspacesmoothness\xspace(see\xspace[sec:intro-ext]Section\ref*sec:intro-ext).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another\xspaceacceleration\xspacemethod\xspaceby\xspace[LanZhou2015] is\xspacebased\xspaceon\xspacea\xspaceprimal\xspace-dual\xspaceanalysis\xspacethat\xspacealso\xspacehas\xspacesuboptimal\xspaceconvergence\xspacerates\xspaceand\xspacesuboptimal\xspaceparallel\xspacespeedup\xspacelike\xspaceCatalyst\xspace. Their\xspacemethod\xspacerequires\xspace$n$\xspacetimes\xspacemore\xspacestorage\xspacecompared\xspacewith\xspaceCatalyst\xspacefor\xspacesolving\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Introduction", "weight": 1.5} -->

In\xspacesum\xspace, it\xspaceis\xspacedesirable\xspaceand\xspacealso\xspacean\xspaceopen\xspacequestion\xspaceto\xspacedevelop\xspacea\xspacedirect\xspace, primal\xspace-only\xspace, and\xspaceoptimal\xspace accelerated\xspacestochastic\xspacegradient\xspacemethod\xspacewithout\xspaceusing\xspacereductions\xspace.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Introduction", "weight": 1.5} -->

This\xspacecould\xspacehave\xspaceboth\xspacetheoretical\xspaceand\xspacepractical\xspaceimpacts\xspaceto\xspacethe\xspaceproblems\xspacethat\xspacefall\xspaceinto\xspacethe\xspacegeneral\xspaceframework\xspaceof\xspace\arenaria, and\xspacepotentially\xspacedeepen\xspaceour\xspaceunderstanding\xspaceto\xspaceacceleration\xspacein\xspacestochastic\xspacesettings\xspace.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Our Main Results and High-Level Ideas", "weight": 1.0} -->

We\xspacedevelop\xspacea\xspacedirect\xspace, accelerated\xspacestochastic\xspacegradient\xspacemethod\xspace$\stupefaceva$\xspacefor\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem) in\xspace$$ O\big(\big(n + \sqrt{n \kappa} \big) \log (1/\rendere) \big) \text{ stochastic gradient iterations (see \liquefaceva{thm:accvr:sc}).} $$This\xspacegives\xspaceboth\xspaceoptimal\xspacedependency\xspaceon\xspace$\kappa$\xspaceand\xspaceon\xspace$\rendere$\xspacewhich\xspacewas\xspacenot\xspaceobtained\xspacebefore\xspacefor\xspacestochastic\xspacegradient\xspacemethods\xspace.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Our Main Results and High-Level Ideas", "weight": 1.0} -->

In\xspaceaddition\xspace, if\xspace$F(\cdot)$\xspaceis\xspacenon\xspace-strongly\xspaceconvex\xspace(non\xspace-SC)\xspace, $\stupefaceva$\xspaceconverges\xspaceto\xspacean\xspace$\rendere$\xspace-minimizer\xspacein\xspace$$ \boxed{O\big(n \log (1/\rendere) + \sqrt{ n L / \rendere} \,\big) \text{ stochastic gradient iterations (see \ricadremmo{cor:accvr:nonsc}).}} $$This\xspacegives\xspacean\xspaceoptimal\xspace$\rendere \propto \frac{n}{T^2}$\xspacerate\xspacewhere\xspacein\xspacecontrast\xspaceCatalyst\xspacehas\xspacerate\xspace$\rendere \propto \frac{n

<!-- chunk {"id": "body-0046", "role": "body", "section": "Our Main Results and High-Level Ideas", "weight": 1.0} -->

\log^4 T}{T^2}$\xspace. The\xspacelower\xspacebound\xspacefrom\xspace[WoodworthSrebro2016] is\xspace$\Omega\big(n + \sqrt{n L / \rendere} \big)$\xspace.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Our Main Results and High-Level Ideas", "weight": 1.0} -->

Above\xspace, $\apritela$\xspaceis\xspacea\xspacesnapshot\xspacepoint\xspacewhich\xspaceis\xspaceupdated\xspaceevery\xspace$m$\xspaceiterations\xspace, $\irruenta_{k+1}$\xspaceis\xspacethe\xspacegradient\xspaceestimator\xspacedefined\xspacein\xspacethe\xspacesame\xspaceway\xspaceas\xspace\arenaria, $\tau_1,\tau_2 \in $\xspaceare\xspacetwo\xspacemomentum\xspaceparameters\xspace, and\xspace$\alpha$\xspaceis\xspacea\xspaceparameter\xspacethat\xspaceis\xspaceequal\xspaceto\xspace$\frac{1}{3 \tau_1 L}$\xspace.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Our Main Results and High-Level Ideas", "weight": 1.0} -->

The\xspacereason\xspacefor\xspacekeeping\xspacethree\xspacevector\xspacesequences\xspace$(x_k, y_k, z_k)$\xspaceis\xspacea\xspacecommon\xspaceingredient\xspacethat\xspacecan\xspacebe\xspacefound\xspacein\xspaceall\xspaceexisting\xspaceaccelerated\xspacemethods\xspace.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Our Main Results and High-Level Ideas", "weight": 1.0} -->

One\xspacecan\xspaceof\xspacecourse\xspacerewrite\xspacethe\xspacealgorithm\xspaceand\xspacekeep\xspacetrack\xspaceof\xspaceonly\xspacetwo\xspacevectors\xspaceper\xspaceiteration\xspaceduring\xspaceimplementation\xspace. This\xspacewill\xspacemake\xspacethe\xspacealgorithm\xspacestatement\xspaceless\xspaceclean\xspaceso\xspacewe\xspacerefrain\xspacefrom\xspacedoing\xspaceso\xspacein\xspacethis\xspacepaper\xspace.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Our Main Results and High-Level Ideas", "weight": 1.0} -->

OurKatyusha.0.9em plus 0.3em minus 0.3em The\xspacemost\xspaceinteresting\xspaceingredient\xspaceof\xspace$\stupefaceva$\xspaceis\xspacethe\xspacenovel\xspacechoice\xspaceof\xspace$x_{k+1}$\xspacewhich\xspaceis\xspacea\xspaceconvex\xspacecombination\xspaceof\xspace$y_k$\xspace, $z_k$\xspace, and\xspace$\apritela$\xspace.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Our Main Results and High-Level Ideas", "weight": 1.0} -->

Our\xspacetheory\xspacesuggests\xspacethe\xspaceparameter\xspacechoices\xspace$\tau_2 = 0.5$\xspaceand\xspace$\tau_1 = \min\{\sqrt{n \sigma/L}, 0.5\}$\xspaceand\xspacethey\xspacework\xspacewell\xspacein\xspacepractice\xspacetoo\xspace. To\xspaceexplain\xspacethis\xspacenovel\xspacecombination\xspace, let\xspaceus\xspacerecall\xspacethe\xspaceclassical\xspacemomentum\xspace view\xspaceof\xspaceaccelerated\xspacemethods\xspace.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Our Main Results and High-Level Ideas", "weight": 1.0} -->

In\xspacea\xspaceclassical\xspaceaccelerated\xspacegradient\xspacemethod\xspace, $x_{k+1}$\xspaceis\xspaceonly\xspacea\xspaceconvex\xspacecombination\xspaceof\xspace$y_k$\xspaceand\xspace$z_k$\xspace(or\xspaceequivalently\xspace, $\tau_2=0$\xspacein\xspaceour\xspaceformulation)\xspace. At\xspacea\xspacehigh\xspacelevel\xspace, $z_{k}$\xspaceplays\xspacethe\xspacerole\xspaceof\xspacemomentum\xspace which\xspaceadds\xspacea\xspaceweighted\xspacesum\xspaceof\xspacethe\xspacegradient\xspacehistory\xspaceinto\xspace$y_{k+1}$\xspace.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Our Main Results and High-Level Ideas", "weight": 1.0} -->

As\xspacean\xspaceillustrative\xspaceexample\xspace, suppose\xspace$\tau_2=0$\xspace, $\tau_1 = \tau$\xspace, and\xspace$x_0 = y_0 = z_0$\xspace.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Our Main Results and High-Level Ideas", "weight": 1.0} -->

\big) \irruenta\_1}, & \hbox{$k=3$.} $$Since\xspace$\alpha$\xspaceis\xspaceusually\xspacemuch\xspacelarger\xspacethan\xspace$1/3L$\xspace, the\xspaceabove\xspacerecursion\xspacesuggests\xspacethat\xspacethe\xspacecontribution\xspaceof\xspacea\xspacefixed\xspacegradient\xspace$\irruenta_t$\xspacegradually\xspaceincreases\xspaceas\xspacetime\xspacegoes\xspace.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Our Main Results and High-Level Ideas", "weight": 1.0} -->

For\xspaceinstance\xspace, the\xspaceweight\xspaceon\xspace$\irruenta_1$\xspaceis\xspaceincreasing\xspacebecause\xspace$\frac{1}{3L} < \big((1-\tau)\frac{1}{3L} + \tau \alpha \big) < \big((1-\tau)^2\frac{1}{3L} + (1-(1-\tau)^2) \alpha \big) \enspace.$\xspaceThis\xspaceis\xspaceknown\xspaceas\xspacemomentum\xspace which\xspaceis\xspaceat\xspacethe\xspaceheart\xspaceof\xspaceall\xspaceaccelerated\xspacefirst\xspace-order\xspacemethods\xspace.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Our Main Results and High-Level Ideas", "weight": 1.0} -->

In\xspace$\stupefaceva$\xspace, we\xspaceput\xspacea\xspacemagnet\xspace around\xspace$\apritela$\xspace, where\xspacewe\xspacechoose\xspace$\apritela$\xspaceto\xspacebe\xspaceessentially\xspacethe\xspaceaverage\xspace$x_t$\xspaceof\xspacethe\xspacemost\xspacerecent\xspace$n$\xspaceiterations\xspace. Whenever\xspacewe\xspacecompute\xspacethe\xspacenext\xspace$x_{k+1}$\xspace, it\xspacewill\xspacebe\xspaceattracted\xspaceby\xspacethe\xspacemagnet\xspace$\apritela$\xspacewith\xspaceweight\xspace$\tau_2 = 0.5$\xspace.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Our Main Results and High-Level Ideas", "weight": 1.0} -->

This\xspaceis\xspacea\xspacestrong\xspacemagnet\xspace: it\xspaceensures\xspacethat\xspace$x_{k+1}$\xspaceis\xspacenot\xspacetoo\xspacefar\xspaceaway\xspacefrom\xspace$\apritela$\xspaceso\xspacethe\xspacegradient\xspaceestimator\xspaceremains\xspaceaccurate\xspaceenough\xspace.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Our Main Results and High-Level Ideas", "weight": 1.0} -->

This\xspacecan\xspacebe\xspaceviewed\xspaceas\xspacea\xspacenegative\xspacemomentum\xspace component\xspace, because\xspacethe\xspacemagnet\xspaceretracts\xspace$x_{k+1}$\xspaceback\xspaceto\xspace$\apritela$\xspaceand\xspacethis\xspacecan\xspacebe\xspaceunderstood\xspaceas\xspacecounteracting\xspacea\xspacefraction\xspaceof\xspacethe\xspacepositive\xspacemomentum\xspaceincurred\xspacefrom\xspaceearlier\xspaceiterations\xspace.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Our Main Results and High-Level Ideas", "weight": 1.0} -->

We\xspacecall\xspaceit\xspacethe\xspaceKatyusha momentum.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Our Main Results and High-Level Ideas", "weight": 1.0} -->

This\xspacesummarizes\xspacethe\xspacehigh\xspace-level\xspaceidea\xspacebehind\xspaceour\xspace$\stupefaceva$\xspacemethod\xspace. We\xspaceremark\xspacehere\xspaceif\xspace$\tau_1=\tau_2=0$\xspace, $\stupefaceva$\xspacebecomes\xspacealmost\xspaceidentical\xspaceto\xspaceSVRG[JohnsonZhang2013-SVRG,MahdaviZhangJin2013-sc] which\xspaceis\xspacea\xspacevariance\xspace-reduction\xspacebased\xspacemethod\xspace.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Our Side Results", "weight": 1.0} -->

Parallelism /-batch.0.9em plus 0.3em minus 0.3em Instead\xspaceof\xspaceusing\xspacea\xspacesingle\xspace$\nabla f_i(\cdot)$\xspaceper\xspaceiteration\xspace, for\xspaceany\xspacestochastic\xspacegradient\xspacemethod\xspace, one\xspacecan\xspacereplace\xspaceit\xspacewith\xspacethe\xspaceaverage\xspaceof\xspace$b$\xspacestochastic\xspacegradients\xspace$\frac{1}{b}\sum_{i\in S} \nabla f_i(\cdot)$\xspace, where\xspace$S$\xspaceis\xspacea\xspacerandom\xspacesubset\xspaceof\xspace$[n]$\xspacewith\xspacecardinality\xspace$b$\xspace.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Our Side Results", "weight": 1.0} -->

This\xspaceis\xspaceknown\xspaceas\xspacethe\xspacemini\xspace-batch\xspace technique\xspaceand\xspaceit\xspaceallows\xspacethe\xspacestochastic\xspacegradients\xspaceto\xspacebe\xspacecomputed\xspacein\xspacea\xspacedistributed\xspacemanner\xspace, using\xspaceup\xspaceto\xspace$b$\xspaceprocessors\xspace.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Our Side Results", "weight": 1.0} -->

Our\xspace$\stupefaceva$\xspacemethod\xspacetrivially\xspaceextends\xspaceto\xspacethis\xspacemini\xspace-batch\xspacesetting\xspace. For\xspaceinstance\xspace, at\xspaceleast\xspacefor\xspace$b\in\{1,2,\dots,\lceil \sqrt{n} \rceil \}$\xspace, $\stupefaceva$\xspaceenjoys\xspacea\xspacelinear\xspacespeedup\xspace in\xspacethe\xspaceparallel\xspacerunning\xspacetime\xspace.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Our Side Results", "weight": 1.0} -->

In\xspaceother\xspacewords\xspace, if\xspaceignoring\xspacecommunication\xspaceoverhead\xspace, \boxed{ \text{$\stupefaceva$ can be distributed to $b \leq \sqrt{n}$ machines with a parallel speed-up factor $b$.} } $$In\xspacecontrast\xspace, to\xspacethe\xspacebest\xspaceof\xspaceour\xspaceknowledge\xspace, without\xspaceany\xspaceadditional\xspaceassumption\xspace, non\xspace-accelerated\xspacemethods\xspacesuch\xspaceas\xspaceSVRG\xspaceor\xspaceSAGA\xspaceare\xspacenot\xspaceknown\xspaceto\xspaceenjoy\xspaceany\xspaceparallel\xspacespeed\xspace-up\xspace;

<!-- chunk {"id": "body-0065", "role": "body", "section": "Our Side Results", "weight": 1.0} -->

Catalyst\xspaceenjoys\xspacea\xspaceparallel\xspacespeed\xspace-up\xspacefactor\xspaceof\xspaceonly\xspace$\sqrt{b}$\xspace. Details\xspaceare\xspacein\xspace[sec:full]Section\ref*sec:full.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Our Side Results", "weight": 1.0} -->

Non-Uniform.0.9em plus 0.3em minus 0.3em If\xspaceeach\xspace$f_i(\cdot)$\xspacehas\xspacea\xspacepossibly\xspacedifferent\xspacesmooth\xspaceparameter\xspace$L_i$\xspaceand\xspace$\crisoprasio = \frac{1}{n}\sum_{i=1}^n L_i$\xspace, then\xspacean\xspacenaive\xspaceimplementation\xspaceof\xspace$\stupefaceva$\xspaceonly\xspacegives\xspacea\xspacecomplexity\xspacethat\xspacedepends\xspaceon\xspace$\max_i L_i$\xspacebut\xspacenot\xspace$\crisoprasio$\xspace.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Our Side Results", "weight": 1.0} -->

In\xspacesuch\xspacea\xspacecase\xspace, we\xspacecan\xspaceselect\xspacethe\xspacerandom\xspaceindex\xspace$i \in [n]$\xspacewith\xspaceprobability\xspaceproportional\xspaceto\xspace$L_i$\xspaceper\xspaceiteration\xspaceto\xspaceslightly\xspaceimprove\xspacethe\xspacetotal\xspacerunning\xspacetime\xspace.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Our Side Results", "weight": 1.0} -->

Furthermore\xspace, suppose\xspace$f(x) = \frac{1}{n} \sum_{i=1}^n f_i(x)$\xspaceis\xspacesmooth\xspacewith\xspaceparameter\xspace$L$\xspace, it\xspacesatisfies\xspace$\crisoprasio \in [L, n L]$\xspace. One\xspacecan\xspaceask\xspacewhether\xspaceor\xspacenot\xspace$L$\xspaceinfluences\xspacethe\xspaceperformance\xspaceof\xspace$\stupefaceva$\xspace.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Our Side Results", "weight": 1.0} -->

We\xspaceshow\xspacethat\xspace, in\xspacethe\xspacemini\xspace-batch\xspacesetting\xspacewhen\xspace$b$\xspaceis\xspacelarge\xspace, the\xspacetotal\xspacecomplexity\xspacebecomes\xspacea\xspacefunction\xspaceon\xspace$L$\xspaceas\xspaceopposed\xspaceto\xspace$\crisoprasio$\xspace. The\xspacedetails\xspaceare\xspacein\xspace[sec:full]Section\ref*sec:full.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Our Side Results", "weight": 1.0} -->

Taking\xspaceinto\xspaceaccount\xspaceboth\xspacethe\xspacemini\xspace-batch\xspaceparameter\xspace$b$\xspaceand\xspacethe\xspacenon\xspace-uniform\xspacesmoothness\xspaceparameters\xspace$L$\xspaceand\xspace$\crisoprasio$\xspace, we\xspaceshow\xspace$\stupefaceva$\xspacesolves\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem) in\xspace$$ O\Big(\big(n + b \sqrt{L /\sigma} + \sqrt{n \crisoprasio / \sigma} \big) \cdot \log \frac{1}{\rendere} \Big) \text{ stochastic gradient computations (see \liquefaceva{thm:full:accvr:sc})} Non-Euclidean.0.9em plus 0.3em minus 0.3em

<!-- chunk {"id": "body-0071", "role": "body", "section": "Our Side Results", "weight": 1.0} -->

If\xspacethe\xspacesmoothness\xspaceof\xspaceeach\xspace$f_i(x)$\xspaceis\xspacewith\xspacerespect\xspaceto\xspacea\xspacenon\xspace-Euclidean\xspacenorm\xspace(such\xspaceas\xspacethe\xspacewell\xspaceknown\xspace$\ell_1$\xspacenorm\xspacecase\xspaceover\xspacethe\xspacesimplex)\xspace, our\xspacemain\xspaceresult\xspacestill\xspaceholds\xspace.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Our Side Results", "weight": 1.0} -->

Our\xspaceupdate\xspaceon\xspacethe\xspace$y_{k+1}$\xspaceside\xspacebecomes\xspacethe\xspacenon\xspace-Euclidean\xspacenorm\xspacegradient\xspacedescent\xspace, and\xspaceour\xspaceupdate\xspaceon\xspacethe\xspace$z_{k+1}$\xspaceside\xspacebecomes\xspacethe\xspacenon\xspace-Euclidean\xspacenorm\xspacemirror\xspacedescent\xspace. We\xspaceinclude\xspacesuch\xspacedetails\xspacein\xspace[sec:ext]Section\ref*sec:ext.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Our Side Results", "weight": 1.0} -->

To\xspacethe\xspacebest\xspaceof\xspaceour\xspaceknowledge\xspace, most\xspaceknown\xspaceaccelerated\xspacemethods\xspace(including\xspaceCatalyst\xspace, AccSDCA\xspaceand\xspaceAPCG)\xspacedo\xspacenot\xspacework\xspacewith\xspacenon\xspace-Euclidean\xspacenorms\xspace. SPDC\xspacecan\xspacebe\xspacerevised\xspaceto\xspacework\xspacewith\xspacenon\xspace-Euclidean\xspacenorms\xspace, see[ALY2016-geometry].

<!-- chunk {"id": "body-0074", "role": "body", "section": "Our Side Results", "weight": 1.0} -->

Remark$\tau_2$.0.9em plus 0.3em minus 0.3em To\xspaceprovide\xspacethe\xspacesimplest\xspaceproof\xspace, we\xspacechoose\xspace$\tau_2 = 1/2$\xspacewhich\xspacealso\xspaceworks\xspacewell\xspacein\xspacepractice\xspace. Our\xspaceproof\xspacetrivially\xspacegeneralizes\xspaceto\xspaceall\xspaceconstant\xspacevalues\xspace$\tau_2 \in $\xspace, and\xspaceit\xspacecould\xspacebe\xspacebeneficial\xspaceto\xspacetune\xspace$\tau_2$\xspacefor\xspacedifferent\xspacedatasets\xspace.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Our Side Results", "weight": 1.0} -->

However\xspace, for\xspacea\xspacestronger\xspacecomparison\xspace, in\xspaceour\xspaceexperiments\xspacewe\xspacerefrain\xspacefrom\xspacetuning\xspace$\tau_2$\xspace: by\xspacefixing\xspace$\tau_2 = 1/2$\xspaceand\xspacewithout\xspaceincreasing\xspaceparameter\xspacetuning\xspacedifficulties\xspace, $\stupefaceva$\xspacealready\xspaceoutperforms\xspacemost\xspaceof\xspacethe\xspacestate\xspace-of\xspace-the\xspace-arts\xspace.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Our Side Results", "weight": 1.0} -->

In\xspacethe\xspacemini\xspace-batch\xspacesetting\xspace, it\xspaceturns\xspaceout\xspacethe\xspacebest\xspacetheoretical\xspacechoice\xspaceis\xspaceessentially\xspace$\tau_2 = \frac{1}{2b}$\xspace, where\xspace$b$\xspaceis\xspacethe\xspacesize\xspaceof\xspacethe\xspacemini\xspace-batch\xspace. In\xspaceother\xspacewords\xspace, the\xspacelarger\xspacethe\xspacemini\xspace-batch\xspacesize\xspace, the\xspacesmaller\xspaceweight\xspacewe\xspacewant\xspaceto\xspacegive\xspaceto\xspaceKatyusha\xspacemomentum\xspace.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Our Side Results", "weight": 1.0} -->

This\xspaceshould\xspacebe\xspaceintuitive\xspace, because\xspacewhen\xspace$b=n$\xspacewe\xspaceare\xspacealmost\xspacein\xspacethe\xspacefull\xspace-gradient\xspacesetting\xspaceand\xspacedo\xspacenot\xspaceneed\xspaceKatyusha\xspacemomentum\xspace.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

Suppose\xspacewe\xspaceare\xspacegiven\xspace$n$\xspacefeature\xspacevectors\xspace$a_1,\dots,a_n \in \mathbb{R}^d$\xspacecorresponding\xspaceto\xspace$n$\xspacedata\xspacesamples\xspace.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

Then\xspace, the\xspaceempirical\xspacerisk\xspaceminimization\xspace(ERM)\xspace problem\xspaceis\xspaceto\xspacestudy\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem) when\xspaceeach\xspace$f_i(x)$\xspaceis\xspacerank\xspace-one\xspace structured\xspace: $f_i(x) \emisfero g_i(\langle a_i, x\rangle)$\xspacefor\xspacesome\xspaceloss\xspacefunction\xspace$g_i \colon \mathbb{R}\to \mathbb{R}$\xspace. Slightly\xspaceabusing\xspacenotation\xspace, we\xspacewrite\xspace$f_i(x) = f_i(\langle a_i, x\rangle)$\xspace.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

Assuming\xspacerank\xspace-one\xspace simplifies\xspacethe\xspacenotations\xspace; all\xspaceof\xspacethe\xspaceresults\xspacestated\xspacein\xspacethis\xspacesubsection\xspacegeneralize\xspaceto\xspaceconstant\xspace-rank\xspacestructured\xspacefunctions\xspace$f_i(x)$\xspace.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

In\xspacesuch\xspacea\xspacecase\xspace, [eqn:the-problem]Problem (\ref*eqn:the-problem) becomes\xspace\begin{equation}\label{eqn:the-problem2} \textstyle \textsc{ERM:}\quad \min\_{x\in \mathbb{R}^d} \Big\{ F(x) \emisfero f(x) + \psi(x) \emisfero \frac{1}{n}\sum\_{i=1}^n f\_i(\langle a\_i, x \rangle) + \psi(x) \Big\} \enspace.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

\end{equation}Without\xspaceloss\xspaceof\xspacegenerality\xspace, we\xspaceassume\xspaceeach\xspace$a_i$\xspacehas\xspacenorm\xspace1 because\xspaceotherwise\xspaceone\xspacecan\xspacescale\xspace$f_i(\cdot)$\xspaceaccordingly\xspace.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

- $\psi(x)$\xspaceis\xspace$\sigma$\xspace-SC\xspaceand\xspace$f_i(x)$\xspaceis\xspace$L$\xspace-smooth\xspace. Examples\xspace: ridge\xspaceregression\xspace, elastic\xspacenet\xspace; - $\psi(x)$\xspaceis\xspacenon\xspace-SC\xspaceand\xspace$f_i(x)$\xspaceis\xspace$L$\xspace-smooth\xspace. Examples\xspace: Lasso\xspace, logistic\xspaceregression\xspace; - $\psi(x)$\xspaceis\xspace$\sigma$\xspace-SC\xspaceand\xspace$f_i(x)$\xspaceis\xspacenon\xspace-smooth\xspace.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

Examples\xspace: support\xspacevector\xspacemachine\xspace; - $\psi(x)$\xspaceis\xspacenon\xspace-SC\xspaceand\xspace$f_i(x)$\xspaceis\xspacenon\xspace-smooth\xspace. Examples\xspace: $\ell_1$\xspace-SVM\xspace.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

Known.0.9em plus 0.3em minus 0.3em For\xspaceall\xspaceof\xspacethe\xspacefour\xspaceERM\xspacecases\xspaceabove\xspace, accelerated\xspacestochastic\xspacemethods\xspacewere\xspaceintroduced\xspacein\xspacethe\xspaceliterature\xspace, most\xspacenotably\xspaceAccSDCA[Shalev-Shwartz2013b], APCG[LLX2014-ProxSDCA-APCG], SPDC[ZhangXiao2015-SPDC]. All\xspacethese\xspacemethods\xspacerely\xspaceon\xspacedual\xspaceanalysis\xspaceso\xspacehave\xspacesuboptimal\xspaceconvergence\xspacerates\xspacefor\xspaceCases\xspace2, 3 and\xspace4.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

(In\xspacefact\xspace, they\xspacealso\xspacehave\xspacethe\xspacesuboptimal\xspacedependence\xspaceon\xspacethe\xspacecondition\xspacenumber\xspace$L/\sigma$\xspacefor\xspaceCase\xspace1.)

<!-- chunk {"id": "body-0087", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

The\xspacebest\xspaceknown\xspacerate\xspacewas\xspace$\frac{\log(1/\rendere)}{\sqrt{\rendere}}, \frac{\log(1/\rendere)}{\sqrt{\rendere}}$\xspace, or\xspace$\frac{\log(1/\rendere)}{\rendere}$\xspacerespectively\xspacefor\xspaceCases\xspace2, 3, or\xspace4, and\xspaceis\xspacea\xspacefactor\xspace$\log (1/\rendere)$\xspaceworse\xspacethan\xspaceoptimal[WoodworthSrebro2016]. It\xspaceis\xspaceopen\xspaceto\xspacedesign\xspacea\xspacestochastic\xspacegradient\xspacemethod\xspaceto\xspacematch\xspacethe\xspaceoptimal\xspacerates\xspace.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

In\xspaceparticular\xspace, [LanDang2014] provided\xspacean\xspaceinteresting\xspaceattempt\xspaceto\xspaceremove\xspacesuch\xspacelog\xspacefactors\xspacebut\xspaceusing\xspacea\xspacenon\xspace-classical\xspacenotion\xspaceof\xspaceconvergence\xspace.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

work\xspacein\xspacea\xspaceprimal\xspace-dual\xspace$\phi(x,y)$\xspaceformulation\xspaceof\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem), and\xspaceproduce\xspacea\xspaceprimal\xspace-dual\xspacepair\xspace$(x,y)$\xspaceso\xspacethat\xspacefor\xspaceevery\xspacefixed\xspace$(u,v)$\xspace, the\xspaceexpectation\xspace$\baltico[\phi(x,v)-\phi(u,y)] \leq \rendere$\xspace.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

Unfortunately\xspace, to\xspaceensure\xspace$x$\xspaceis\xspacean\xspace$\rendere$\xspace-approximate\xspaceminimizer\xspaceof\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem), one\xspaceneeds\xspacethe\xspacestronger\xspace$\baltico[\max_{(u,v)} \phi(x,v) - \phi(u,y)]\leq \rendere$\xspaceto\xspacehold\xspace.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

Besides\xspacethe\xspacelog\xspacefactor\xspaceloss\xspacein\xspacethe\xspacerunning\xspacetime\xspace, In\xspacefact\xspace, dual\xspace-based\xspacemethods\xspacehave\xspaceto\xspacesuffer\xspacefrom\xspacea\xspacelog\xspacefactor\xspaceloss\xspacein\xspacethe\xspaceconvergence\xspacerate\xspace.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

This\xspaceis\xspaceso\xspacebecause\xspaceeven\xspacefor\xspaceCase\xspace1 of\xspace[eqn:the-problem2]Problem (\ref*eqn:the-problem2), converting\xspacean\xspace$\rendere$\xspace-maximizer\xspacefor\xspacethe\xspacedual\xspaceobjective\xspaceto\xspacethe\xspaceprimal\xspace, one\xspaceonly\xspaceobtains\xspacean\xspace$n \kappa \rendere$\xspace-minimizer\xspaceon\xspacethe\xspaceprimal\xspaceobjective\xspace.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

As\xspacea\xspaceresult\xspace, algorithms\xspacelike\xspaceAPCG\xspacewho\xspacedirectly\xspacework\xspaceon\xspacethe\xspacedual\xspace, algorithms\xspacelike\xspaceSPDC\xspacewho\xspacemaintain\xspaceboth\xspaceprimal\xspaceand\xspacedual\xspacevariables\xspace, and\xspacealgorithms\xspacelike\xspaceRPDG that\xspaceare\xspaceprimal\xspace-like\xspacebut\xspacestill\xspaceuse\xspacedual\xspaceanalysis\xspace, have\xspaceto\xspacesuffer\xspacefrom\xspacea\xspacelog\xspaceloss\xspacein\xspacethe\xspaceconvergence\xspacerates\xspace.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

the\xspaceaforementioned\xspacemethods\xspacesuffer\xspacefrom\xspaceseveral\xspaceother\xspaceissues\xspacethat\xspacemost\xspacedual\xspace-based\xspacemethods\xspacealso\xspacesuffer\xspace. First\xspace, they\xspaceonly\xspaceapply\xspaceto\xspaceERM\xspaceproblems\xspacebut\xspacenot\xspaceto\xspacethe\xspacemore\xspacegeneral\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem).

<!-- chunk {"id": "body-0095", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

Second\xspace, they\xspacerequire\xspaceproximal\xspaceupdates\xspacewith\xspacerespect\xspaceto\xspacethe\xspaceFenchel\xspaceconjugate\xspace$f_i^*(\cdot)$\xspacewhich\xspaceis\xspacesometimes\xspaceunpleasant\xspaceto\xspacework\xspacewith\xspace. Third\xspace, their\xspaceperformances\xspacecannot\xspacebenefit\xspacefrom\xspacethe\xspaceimplicit\xspacestrong\xspaceconvexity\xspacein\xspace$f(\cdot)$\xspace.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

All\xspaceof\xspacethese\xspaceissues\xspacetogether\xspacemake\xspacethese\xspacemethods\xspacesometimes\xspaceeven\xspaceoutperformed\xspaceby\xspaceprimal\xspace-only\xspacenon\xspace-accelerated\xspaceones\xspace, such\xspaceas\xspaceSAGA[Defazio2014-SAGA] or\xspaceSVRG[JohnsonZhang2013-SVRG,MahdaviZhangJin2013-sc].

<!-- chunk {"id": "body-0097", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

Our.0.9em plus 0.3em minus 0.3em $\stupefaceva$\xspacesimultaneously\xspacecloses\xspacethe\xspacegap\xspacefor\xspaceall\xspaceof\xspacethe\xspacethree\xspaceclasses\xspaceof\xspaceproblems\xspacewith\xspacethe\xspacehelp\xspacefrom\xspacethe\xspaceoptimal\xspacereductions\xspacedeveloped\xspacein[AH2016-reduction].

<!-- chunk {"id": "body-0098", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

We\xspaceobtain\xspacean\xspace$\rendere$\xspace-approximate\xspaceminimizer\xspacefor\xspaceCase\xspace2 in\xspace$O\big(n \log \frac{1}{\rendere} + \frac{\sqrt{n L}}{\sqrt{\rendere}}\big)$\xspaceiterations\xspace, for\xspaceCase\xspace3 in\xspace$O\big(n \log \frac{1}{\rendere} + \frac{\sqrt{n}}{\sqrt{\sigma \rendere}}\big)$\xspaceiterations\xspace, and\xspacefor\xspaceCase\xspace4 in\xspace$O\big(n \log \frac{1}{\rendere} + \frac{\sqrt{n}}{\rendere}\big)$\xspaceiterations\xspace.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

None\xspaceof\xspacethe\xspaceexisting\xspaceaccelerated\xspacemethods\xspacecan\xspacelead\xspaceto\xspacesuch\xspaceoptimal\xspacerates\xspaceeven\xspaceif\xspacethe\xspaceoptimal\xspacereductions\xspaceare\xspaceused\xspace. [WoodworthSrebro2016] proved\xspacethe\xspacetightness\xspaceof\xspaceour\xspaceresults\xspace.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

They\xspaceshowed\xspacelower\xspacebounds\xspace$\Omega\big(n + \frac{\sqrt{n L}}{\sqrt{\rendere}}\big)$\xspace, $\Omega\big(n + \frac{\sqrt{n}}{\sqrt{\sigma \rendere}}\big)$\xspace, and\xspace$\Omega\big(n + \frac{\sqrt{n}}{\rendere}\big)$\xspacefor\xspaceCases\xspace2, 3, and\xspace4 respectively\xspace.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Applications: Optimal Rates for Empirical Risk Minimization", "weight": 1.0} -->

However\xspace, since\xspacethe\xspacevanilla\xspaceSGD\xspacerequires\xspace$O(\frac{1}{\sigma \rendere})$\xspaceand\xspace$O(\frac{1}{\rendere^2})$\xspaceiterations\xspacefor\xspaceCases\xspace3 and\xspace4, such\xspacelower\xspacebounds\xspaceare\xspacematched\xspaceby\xspacecombining\xspacethe\xspacebest\xspacebetween\xspace$\stupefaceva$\xspaceand\xspaceSGD\xspace.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Roadmap", "weight": 1.0} -->

- In\xspace[sec:accvr:sc]Section\ref*sec:accvr:sc, we\xspacestate\xspaceand\xspaceprove\xspaceour\xspacetheorem\xspaceon\xspace$\stupefaceva$\xspacefor\xspacethe\xspacestrongly\xspaceconvex\xspacecase\xspace. - In\xspace[sec:reductions]Section\ref*sec:reductions, we\xspaceapply\xspace$\stupefaceva$\xspaceto\xspacenon\xspace-strongly\xspaceconvex\xspaceor\xspacenon\xspace-smooth\xspacecases\xspaceby\xspacereductions\xspace.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Roadmap", "weight": 1.0} -->

- In\xspace[sec:accvr:nonsc]Section\ref*sec:accvr:nonsc, we\xspaceprovide\xspacea\xspacedirect\xspace algorithm\xspace$\giraffista$\xspacefor\xspacethe\xspacenon\xspace-strongly\xspacecase\xspace. - In\xspace[sec:full]Section\ref*sec:full, we\xspacegeneralize\xspace$\stupefaceva$\xspaceto\xspacemini\xspace-batch\xspaceand\xspacenon\xspace-uniform\xspacesmoothness\xspace. - In\xspace[sec:ext]Section\ref*sec:ext, we\xspacegeneralize\xspace$\stupefaceva$\xspaceto\xspacethe\xspacenon\xspace-Euclidean\xspacenorm\xspacesetting\xspace.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Roadmap", "weight": 1.0} -->

- In\xspace[sec:exp]Section\ref*sec:exp, we\xspaceprovide\xspacean\xspaceempirical\xspaceevaluation\xspaceto\xspaceillustrate\xspacethe\xspacenecessity\xspaceof\xspaceKatyusha\xspacemomentum\xspace, and\xspacethe\xspacepractical\xspaceperformance\xspaceof\xspace$\stupefaceva$\xspace.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Notations", "weight": 1.0} -->

Throughout\xspacethis\xspacepaper\xspace(except\xspace[sec:ext]Section\ref*sec:ext), we\xspacedenote\xspaceby\xspace$\|\cdot\|$\xspacethe\xspaceEuclidean\xspacenorm\xspace. We\xspacedenote\xspaceby\xspace$\nabla f(x)$\xspacethe\xspacefull\xspacegradient\xspaceof\xspacefunction\xspace$f$\xspaceif\xspaceit\xspaceis\xspacedifferentiable\xspace, or\xspaceany\xspaceof\xspaceits\xspacesubgradients\xspaceif\xspace$f$\xspaceis\xspaceonly\xspaceLipschitz\xspacecontinuous\xspace.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Notations", "weight": 1.0} -->

Recall\xspacesome\xspaceclassical\xspacedefinitions\xspaceon\xspacestrong\xspaceconvexity\xspace(SC)\xspaceand\xspacesmoothness\xspace.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Notations", "weight": 1.0} -->

For\xspacea\xspaceconvex\xspacefunction\xspace$f \colon \mathbb{R}^n \to \mathbb{R}$\xspace,

<!-- chunk {"id": "body-0108", "role": "body", "section": "Notations", "weight": 1.0} -->

- $f$\xspaceis\xspace$\sigma$\xspace-strongly\xspaceconvex\xspaceif\xspace$\forall x,y\in \mathbb{R}^n$\xspace, it\xspacesatisfies\xspace$f(y)\geq f(x)+ \langle \nabla f(x), y-x\rangle + \frac{\sigma}{2}\|x-y\|^2$\xspace. - $f$\xspaceis\xspace$L$\xspace-smooth\xspaceif\xspace$\forall x,y\in \mathbb{R}^n$\xspace, it\xspacesatisfies\xspace$\|\nabla f(x) - \nabla f(y)\|\leq L \|x - y\|$\xspace.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

We\xspaceformally\xspaceintroduce\xspaceour\xspace$\stupefaceva$\xspacealgorithm\xspacein\xspace[alg:acc-vr]Algorithm\ref*alg:acc-vr. It\xspacefollows\xspacefrom\xspaceour\xspacehigh\xspace-level\xspacedescription\xspacein\xspace[sec:intro:our-res]Section\ref*sec:intro:our-res, and\xspacewe\xspacemake\xspaceseveral\xspaceremarks\xspacehere\xspacebehind\xspaceour\xspacespecific\xspacedesign\xspace.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

- $\stupefaceva$\xspaceis\xspacedivided\xspaceinto\xspaceepochs\xspaceeach\xspaceconsisting\xspaceof\xspace$m$\xspaceiterations\xspace. In\xspacetheory\xspace, $m$\xspacecan\xspacebe\xspaceanything\xspacelinear\xspacein\xspace$n$\xspace. We\xspacelet\xspacesnapshot\xspace$\apritela$\xspacebe\xspacea\xspaceweighted\xspaceaverage\xspaceof\xspace$y_k$\xspacein\xspacethe\xspacemost\xspacerecent\xspaceepoch\xspace.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

- $\apritela$\xspaceand\xspace$\irruenta_k$\xspacecorrespond\xspaceto\xspacea\xspacestandard\xspacedesign\xspaceon\xspacevariance\xspace-reduced\xspacegradient\xspaceestimators\xspace, called\xspaceSVRG[JohnsonZhang2013-SVRG,MahdaviZhangJin2013-sc]. The\xspacepractical\xspacerecommendation\xspaceis\xspace$m=2n$\xspace[JohnsonZhang2013-SVRG].

<!-- chunk {"id": "body-0112", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

Our\xspacechoice\xspace$\irruenta_k$\xspaceis\xspaceindependent\xspacefrom\xspaceour\xspaceacceleration\xspacetechniques\xspace, and\xspacewe\xspaceexpect\xspaceour\xspaceresult\xspacecontinues\xspaceto\xspaceapply\xspaceto\xspaceother\xspacechoices\xspaceof\xspacegradient\xspaceestimators\xspace. We\xspacechoose\xspace$\apritela$\xspaceto\xspacebe\xspacea\xspaceweighted\xspaceaverage\xspace, rather\xspacethan\xspacethe\xspacelast\xspaceor\xspacethe\xspaceuniform\xspaceaverage\xspace, because\xspaceit\xspaceyields\xspacethe\xspacetightest\xspacepossible\xspaceresult\xspace.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

If\xspaceone\xspaceuses\xspacethe\xspaceuniform\xspaceaverage\xspace, in\xspacetheory\xspace, the\xspacealgorithm\xspaceneeds\xspaceto\xspacerestart\xspaceevery\xspacea\xspacenumber\xspaceof\xspaceepochs\xspace(that\xspaceis\xspace, by\xspaceresetting\xspace$k=0$\xspace, $s=0$\xspace, and\xspace$x_0=y_0=z_0$\xspace); we\xspacerefrain\xspacefrom\xspacedoing\xspaceso\xspacebecause\xspacewe\xspacewish\xspaceto\xspaceprovide\xspacea\xspacesimple\xspaceand\xspacedirect\xspacealgorithm\xspace.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

We\xspacecan\xspacealso\xspaceuse\xspacethe\xspacelast\xspaceiterate\xspace, then\xspacethe\xspacetotal\xspacecomplexity\xspaceloses\xspacea\xspacefactor\xspace$\log(L/\sigma)$\xspace. In\xspacepractice\xspace, it\xspacewas\xspacereported\xspacethat\xspaceeven\xspacefor\xspaceSVRG\xspace, choosing\xspaceaverage\xspaceworks\xspacebetter\xspacethan\xspacechoosing\xspacethe\xspacelast\xspaceiterate. - $\tau_1$\xspaceand\xspace$\alpha$\xspaceare\xspacestandard\xspaceparameters\xspacealready\xspacepresent\xspacein\xspaceNesterov\xspace's\xspacefull\xspace-gradient\xspacemethod.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

- We\xspacechoose\xspace$\alpha = 1/3 \tau_1 L$\xspaceto\xspacepresent\xspacethe\xspacesimplest\xspaceproof\xspace, and\xspacerecall\xspaceit\xspacewas\xspace$\alpha = 1/\tau_1 L$\xspacein\xspacethe\xspaceoriginal\xspaceNesterov\xspace's\xspacefull\xspace-gradient\xspacemethod\xspace.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

(Any\xspace$\alpha$\xspacethat\xspaceis\xspaceconstant\xspacefactor\xspacesmaller\xspacethan\xspace$1/\tau_1 L$\xspaceworks\xspacein\xspacetheory\xspace, and\xspacewe\xspaceuse\xspace$1/3$\xspaceto\xspaceprovide\xspacethe\xspacesimplest\xspaceproof\xspace.) In\xspacepractice\xspace, like\xspaceother\xspaceaccelerated\xspacemethods\xspace, it\xspacesuffices\xspaceto\xspacefix\xspace$\alpha = 1/3\tau_1 L$\xspaceand\xspaceonly\xspacetune\xspace$\tau_1$\xspaceand\xspacethus\xspace$\tau_1$\xspaceis\xspaceviewed\xspaceas\xspacethe\xspacelearning\xspacerate\xspace.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

- The\xspaceparameter\xspace$\tau_2$\xspaceis\xspaceour\xspacenovel\xspaceweight\xspacefor\xspacethe\xspaceKatyusha\xspacemomentum\xspace. Any\xspaceconstant\xspacein\xspace$$\xspaceworks\xspacefor\xspace$\tau_2$\xspace, and\xspacewe\xspacesimply\xspacechoose\xspace$\tau_2 = 1/2$\xspacefor\xspaceour\xspacetheoretical\xspaceand\xspaceexperimental\xspaceresults\xspace.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

compute\xspacesnapshot\xspace$\apritela$\xspace $\apritela^\paraonde$\xspace.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

We\xspacestate\xspaceour\xspacemain\xspacetheorem\xspacefor\xspace$\stupefaceva$\xspaceas\xspacefollows\xspace: If\xspaceeach\xspace$f_i(x)$\xspaceis\xspaceconvex\xspace, $L$\xspace-smooth\xspace, and\xspace$\psi(x)$\xspaceis\xspace$\sigma$\xspace-strongly\xspaceconvex\xspacein\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem), then\xspace$\stupefaceva(x_0, S, \sigma, L)$\xspacesatisfies\xspace\begin{align*} \baltico\big[F(\apritela^S)\big] - F(x^*) O\Big(\big(1+ \sqrt{\sigma / (3 L m) } \big)^{-S m} \Big) \cdot

<!-- chunk {"id": "body-0120", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

using\xspaceat\xspacemost\xspace$O\big(\big(n + \sqrt{n L / \sigma} \big) \cdot \log \frac{F(x_0)-F(x^*)}{\rendere} \big)$\xspaceiterations\xspace.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

The\xspaceproof\xspaceof\xspace[thm:accvr:sc]Theorem\ref*thm:accvr:sc is\xspaceincluded\xspacein\xspace[sec:one-iter]Section\ref*sec:one-iter and\xspace[app:thm:accvr:sc]. As\xspacediscussed\xspacein\xspace[sec:intro:our-res]Section\ref*sec:intro:our-res, the\xspacemain\xspaceidea\xspacebehind\xspaceour\xspacetheorem\xspaceis\xspacethe\xspacenegative\xspacemomentum\xspacethat\xspacehelps\xspacereduce\xspacethe\xspaceerror\xspaceoccurred\xspacefrom\xspacethe\xspacestochastic\xspacegradient\xspaceestimator\xspace.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

Because\xspace$m=2n$\xspace, each\xspaceiteration\xspaceof\xspace$\stupefaceva$\xspacecomputes\xspaceonly\xspace$1.5$\xspacestochastic\xspacegradients\xspace$\nabla f_i(\cdot)$\xspacein\xspacethe\xspaceamortized\xspacesense\xspace, the\xspacesame\xspaceas\xspacenon\xspace-accelerated\xspacemethods\xspacesuch\xspaceas\xspaceSVRG[JohnsonZhang2013-SVRG].

<!-- chunk {"id": "body-0123", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

The\xspaceclaim\xspaceSVRG\xspaceor\xspace$\stupefaceva$\xspacecomputes\xspace$1.5$\xspacestochastic\xspacegradients\xspace requires\xspaceone\xspaceto\xspacestore\xspace$\nabla_i f(\apritela)$\xspacein\xspacethe\xspacememory\xspacefor\xspaceeach\xspace$i\in [n]$\xspace, and\xspacethis\xspacecosts\xspace$O(d n)$\xspacespace\xspacein\xspacethe\xspacemost\xspacegeneral\xspacesetting\xspace.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

If\xspaceone\xspacedoes\xspacenot\xspacestore\xspace$\nabla_i f(\apritela)$\xspacein\xspacethe\xspacememory\xspace, then\xspaceeach\xspaceiteration\xspaceof\xspaceSVRG\xspaceor\xspace$\stupefaceva$\xspacecomputes\xspace$2.5$\xspacestochastic\xspacegradients\xspacefor\xspacethe\xspacechoice\xspace$m=2n$\xspace.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

Therefore\xspace, the\xspaceper\xspace-iteration\xspacecost\xspaceof\xspace$\stupefaceva$\xspaceis\xspacedominated\xspaceby\xspacethe\xspacecomputation\xspaceof\xspace$\nabla f_i(\cdot)$\xspace, the\xspaceproximal\xspaceupdate\xspacein\xspace[line:proximal]Line\ref*line:proximal of\xspace[alg:acc-vr]Algorithm\ref*alg:acc-vr, plus\xspacean\xspaceoverhead\xspace$O(d)$\xspace.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

If\xspace$\nabla f_i(\cdot)$\xspacehas\xspaceat\xspacemost\xspace$d' \leq d$\xspacenon\xspace-zero\xspaceentries\xspace, this\xspaceoverhead\xspace$O(d)$\xspaceis\xspaceimprovable\xspaceto\xspace$O(d')$\xspaceusing\xspacea\xspacesparse\xspaceimplementation\xspaceof\xspace$\stupefaceva$\xspace.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

This\xspacerequires\xspaceto\xspacedefer\xspacea\xspacecoordinate\xspaceupdate\xspaceto\xspacethe\xspacemoment\xspaceit\xspaceis\xspaceaccessed\xspace. Update\xspacedeferral\xspaceis\xspacea\xspacestandard\xspacetechnique\xspaceused\xspacein\xspacesparse\xspaceimplementations\xspaceof\xspaceall\xspacestochastic\xspacegradient\xspacemethods\xspace, including\xspaceSVRG\xspace, SAGA\xspace, APCG.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Katyusha in the Strongly Convex Setting", "weight": 1.0} -->

For\xspaceERM\xspaceproblems\xspacedefined\xspacein\xspace[eqn:the-problem2]Problem (\ref*eqn:the-problem2), the\xspaceamortized\xspaceper\xspace-iteration\xspacecomplexity\xspaceof\xspace$\stupefaceva$\xspaceis\xspace$O(d')$\xspacewhere\xspace$d'$\xspaceis\xspacethe\xspacesparsity\xspaceof\xspacefeature\xspacevectors\xspace, the\xspacesame\xspaceas\xspacethe\xspaceper\xspace-iteration\xspacecomplexity\xspaceof\xspaceSGD\xspace.

<!-- chunk {"id": "body-0129", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

In\xspacethis\xspacesubsection\xspace, we\xspacefirst\xspaceanalyze\xspacethe\xspacebehavior\xspaceof\xspace$\stupefaceva$\xspacein\xspacea\xspacesingle\xspaceiteration\xspace(i\xspace.e\xspace., for\xspacea\xspacefixed\xspace$k$\xspace). We\xspaceview\xspace$y_k, z_k$\xspaceand\xspace$x_{k+1}$\xspaceas\xspacefixed\xspacein\xspacethis\xspacesection\xspaceso\xspacethe\xspaceonly\xspacerandomness\xspacecomes\xspacefrom\xspacethe\xspacechoice\xspaceof\xspace$i$\xspacein\xspaceiteration\xspace$k$\xspace.

<!-- chunk {"id": "body-0130", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

We\xspaceabbreviate\xspacein\xspacethis\xspacesubsection\xspaceby\xspace$\apritela = \apritela^s$\xspacewhere\xspace$s$\xspaceis\xspacethe\xspaceepoch\xspacethat\xspaceiteration\xspace$k$\xspacebelongs\xspaceto\xspace, and\xspacedenote\xspaceby\xspace$\sigma_{k+1}^2 \emisfero \|\nabla f(x_{k+1}) - \irruenta_{k+1}\|^2$\xspaceso\xspace$\baltico[\sigma_{k+1}^2]$\xspaceis\xspacethe\xspacevariance\xspaceof\xspacethe\xspacegradient\xspaceestimator\xspace$\irruenta_{k+1}$\xspacein\xspacethis\xspaceiteration\xspace.

<!-- chunk {"id": "body-0131", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

Our\xspacefirst\xspacelemma\xspacelower\xspacebounds\xspacethe\xspaceexpected\xspaceobjective\xspacedecrease\xspace$F(x_{k+1}) - \baltico[F(y_{k+1})]$\xspace.

<!-- chunk {"id": "body-0132", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

Our\xspace$\madrigalico(x_{k+1})$\xspacedefined\xspacebelow\xspaceis\xspacea\xspacenon\xspace-negative\xspace, classical\xspacequantity\xspacethat\xspacewould\xspacebe\xspacea\xspacelower\xspacebound\xspaceon\xspacethe\xspaceamount\xspaceof\xspaceobjective\xspacedecrease\xspaceif\xspace$\irruenta_{k+1}$\xspacewere\xspaceequal\xspaceto\xspace$\nabla f(x_{k+1})$\xspace[AO-survey-nesterov].

<!-- chunk {"id": "body-0133", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

However\xspace, since\xspacethe\xspacevariance\xspace$\sigma_{k+1}^2$\xspaceis\xspacenon\xspace-zero\xspace, this\xspacelower\xspacebound\xspacemust\xspacebe\xspacecompensated\xspaceby\xspacea\xspacenegative\xspaceterm\xspacethat\xspacedepends\xspaceon\xspace$\baltico[\sigma_{k+1}^2]$\xspace.

<!-- chunk {"id": "body-0134", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

The\xspacefollowing\xspacelemma\xspaceprovides\xspacea\xspacenovel\xspaceupper\xspacebound\xspaceon\xspacethe\xspaceexpected\xspacevariance\xspaceof\xspacethe\xspacegradient\xspaceestimator\xspace.

<!-- chunk {"id": "body-0135", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

Note\xspacethat\xspaceall\xspaceknown\xspacevariance\xspacereduction\xspaceanalysis\xspacefor\xspaceconvex\xspaceoptimization\xspace, in\xspaceone\xspaceway\xspaceor\xspaceanother\xspace, upper\xspacebounds\xspacethis\xspacevariance\xspaceessentially\xspaceby\xspace$4L \cdot (f(\apritela)-f(x^*))$\xspace, the\xspaceobjective\xspacedistance\xspaceto\xspacethe\xspaceminimizer\xspace(c\xspace.f\xspace.[JohnsonZhang2013-SVRG,Defazio2014-SAGA]).

<!-- chunk {"id": "body-0136", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

The\xspacerecent\xspaceresult\xspaceof\xspace[AH2016-reduction] upper\xspacebounds\xspaceit\xspaceby\xspacethe\xspacepoint\xspacedistance\xspace$\|x_{k+1}-\apritela\|^2$\xspacefor\xspacenon\xspace-convex\xspaceobjectives\xspace, which\xspaceis\xspacetighter\xspaceif\xspace$\apritela$\xspaceis\xspaceclose\xspaceto\xspace$x_{k+1}$\xspacebut\xspaceunfortunately\xspacenot\xspaceenough\xspacefor\xspacethe\xspacepurpose\xspaceof\xspacethis\xspacepaper\xspace.

<!-- chunk {"id": "body-0137", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

In\xspacethis\xspacepaper\xspace, we\xspaceupper\xspacebound\xspaceit\xspaceby\xspacethe\xspacetightest\xspacepossible\xspacequantity\xspacewhich\xspaceis\xspaceessentially\xspace$2 L \cdot \big(f(\apritela) - f(x_{k+1})\big) \ll 4L \cdot \big(f(\apritela) - f(x^*)\big)$\xspace.

<!-- chunk {"id": "body-0138", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

Unfortunately\xspace, this\xspaceupper\xspacebound\xspaceneeds\xspaceto\xspacebe\xspacecompensated\xspaceby\xspacean\xspaceadditional\xspaceterm\xspace$\langle \nabla f(x_{k+1}), \apritela - x_{k+1}\rangle$\xspace, which\xspacecould\xspacebe\xspacepositive\xspacebut\xspacewe\xspaceshall\xspacecancel\xspaceit\xspaceusing\xspacethe\xspaceintroduced\xspaceKatyusha\xspacemomentum\xspace.

<!-- chunk {"id": "body-0139", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

Each\xspace$f_i(x)$\xspace, being\xspaceconvex\xspaceand\xspace$L$\xspace-smooth\xspace, implies\xspacethe\xspacefollowing\xspaceinequality\xspacewhich\xspaceis\xspaceclassical\xspacein\xspaceconvex\xspaceoptimization\xspaceand\xspacecan\xspacebe\xspacefound\xspacefor\xspaceinstance\xspacein\xspaceTheorem\xspace2.1.5 of\xspacethe\xspacetextbook\xspaceof\xspace[Nesterov2004].

<!-- chunk {"id": "body-0140", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

\end{align*}Above\xspace, \text{\ding{172}}\xspaceis\xspacebecause\xspacefor\xspaceany\xspacerandom\xspacevector\xspace$\zeta \in \mathbb{R}^d$\xspace, it\xspaceholds\xspacethat\xspace$\E\|\zeta - \E \zeta\|^2 = \E \|\zeta\|^2 - \|\E\zeta\|^2$\xspace; \text{\ding{173}}\xspacefollows\xspacefrom\xspacethe\xspacefirst\xspaceinequality\xspacein\xspacethis\xspaceproof\xspace.

<!-- chunk {"id": "body-0141", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

The\xspacenext\xspacelemma\xspaceis\xspacea\xspaceclassical\xspaceone\xspacefor\xspaceproximal\xspacemirror\xspacedescent\xspace.

<!-- chunk {"id": "body-0142", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

Suppose\xspace$\psi(\cdot)$\xspaceis\xspace$\sigma$\xspace-SC\xspace.

<!-- chunk {"id": "body-0143", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

By\xspacethe\xspaceminimality\xspacedefinition\xspaceof\xspace$z_{k+1}$\xspace, we\xspacehave\xspacethat\xspace$$ z\_{k+1} - z\_k + \alpha \irruenta\_{k+1} + \alpha g = 0$$where\xspace$g$\xspaceis\xspacesome\xspace subgradient\xspaceof\xspace$\psi(z)$\xspaceat\xspacepoint\xspace$z = z_{k+1}$\xspace.

<!-- chunk {"id": "body-0144", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

This\xspaceimplies\xspacethat\xspacefor\xspaceevery\xspace$u$\xspaceit\xspacesatisfies\xspace$$ 0 = \big\langle z\_{k+1} - z\_k + \alpha \irruenta\_{k+1} + \alpha g, z\_{k+1} - u \rangle \enspace.

<!-- chunk {"id": "body-0145", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

u\|^2$\xspacewhich\xspacecomes\xspacefrom\xspacethe\xspacestrong\xspaceconvexity\xspaceof\xspace$\psi(\cdot)$\xspace, we\xspacecan\xspacewrite\xspace\begin{align*} &\quad\; \alpha \langle \irruenta\_{k+1}, z\_{k+1} - u \rangle + \alpha \psi(z\_{k+1}) - \alpha \psi(u) \\- \langle \alpha g, z\_{k+1} - u \rangle + \alpha \psi(z\_{k+1}) - \alpha \psi(u) \\The\xspacefollowing\xspacelemma\xspacecombines\xspace[lemma:accvr:prox-grad-step]Lemma\ref*lemma:accvr:prox-grad-step,

<!-- chunk {"id": "body-0146", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

[lemma:accvr:variance-upper]Lemma\ref*lemma:accvr:variance-upper and\xspace[lemma:accvr:prox-mirr-step]Lemma\ref*lemma:accvr:prox-mirr-step all\xspacetogether\xspace, using\xspacethe\xspacespecial\xspacechoice\xspaceof\xspace$x_{k+1}$\xspacewhich\xspaceis\xspacea\xspaceconvex\xspacecombination\xspaceof\xspace$y_k, z_k$\xspaceand\xspace$\apritela$\xspace: If\xspace$x_{k+1} = \tau_1 z_k + \tau_2 \apritela + (1-\tau_1 - \tau_2) y_k$\xspace, where\xspace$\tau_1 \leq \frac{1}{3 \alpha L}$\xspaceand\xspace$\tau_2 =

<!-- chunk {"id": "body-0147", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

The\xspacenext\xspacelemma\xspacesimplifies\xspacethe\xspaceleft\xspacehand\xspaceside\xspaceof\xspace[lemma:accvr:coupling1]Lemma\ref*lemma:accvr:coupling1 using\xspacethe\xspaceconvexity\xspaceof\xspace$f(\cdot)$\xspace, and\xspacegives\xspacean\xspaceinequality\xspacethat\xspacerelates\xspacethe\xspaceobjective\xspace-distance\xspace-to\xspace-minimizer\xspacequantities\xspace$F(y_k)-F(x^*)$\xspace, $F(y_{k+1})-F(x^*)$\xspace,

<!-- chunk {"id": "body-0148", "role": "body", "section": "One-Iteration Analysis", "weight": 1.0} -->

and\xspace$F(\apritela)-F(x^*)$\xspaceto\xspacethe\xspacepoint\xspace-distance\xspace-to\xspace-minimizer\xspacequantities\xspace$\|z_k - x^*\|^2$\xspaceand\xspace$\|z_{k+1} - x^*\|^2$\xspace.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Corollaries on Non-Smooth or Non-SC Problems", "weight": 1.0} -->

In\xspacethis\xspacesection\xspacewe\xspaceapply\xspacereductions\xspaceto\xspacetranslate\xspaceour\xspace[thm:accvr:sc]Theorem\ref*thm:accvr:sc into\xspaceoptimal\xspacealgorithms\xspacealso\xspacefor\xspacenon\xspace-strongly\xspaceconvex\xspaceobjectives\xspaceand\xspace/or\xspacenon\xspace-smooth\xspaceobjectives\xspace.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Corollaries on Non-Smooth or Non-SC Problems", "weight": 1.0} -->

To\xspacebegin\xspacewith\xspace, recall\xspacethe\xspacefollowing\xspacedefinition\xspaceof\xspacethe\xspace\textsf{HOOD}\xspaceproperty\xspace: An\xspacealgorithm\xspacesolving\xspacethe\xspacestrongly\xspaceconvex\xspacecase\xspaceof\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem) satisfies\xspacethe\xspacehomogenous\xspaceobjective\xspacedecrease\xspace(\textsf{HOOD}\xspace) property\xspacewith\xspace$T(L,\sigma)$\xspace, if\xspacefor\xspaceevery\xspacestarting\xspacepoint\xspace$x_0$\xspace,

<!-- chunk {"id": "body-0151", "role": "body", "section": "Corollaries on Non-Smooth or Non-SC Problems", "weight": 1.0} -->

it\xspaceproduces\xspacean\xspaceoutput\xspace$x'$\xspacesatisfying\xspace$\baltico\big[F(x')\big] - F(x^*) \leq \frac{F(x_0) - F(x^*)}{4}$\xspacein\xspaceat\xspacemost\xspace$T(L,\sigma)$\xspacestochastic\xspacegradient\xspaceiterations\xspace.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Corollaries on Non-Smooth or Non-SC Problems", "weight": 1.0} -->

[thm:accvr:sc]Theorem\ref*thm:accvr:sc shows\xspacethat\xspace$\stupefaceva$\xspacesatisfies\xspacethe\xspace\textsf{HOOD}\xspaceproperty\xspace: $\stupefaceva$\xspacesatisfies\xspacethe\xspace\textsf{HOOD}\xspaceproperty\xspacewith\xspace$T(L,\sigma) = O \big(n + \frac{\sqrt{n L}}{\sqrt{\sigma}} \big)$\xspace.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Corollaries on Non-Smooth or Non-SC Problems", "weight": 1.0} -->

Existing\xspaceaccelerated\xspacestochastic\xspacemethods\xspacebefore\xspacethis\xspacework\xspace(even\xspacefor\xspacesimpler\xspace[eqn:the-problem2]Problem (\ref*eqn:the-problem2)) either\xspacedo\xspacenot\xspacesatisfy\xspace\textsf{HOOD}\xspaceor\xspacesatisfy\xspace\textsf{HOOD}\xspacewith\xspacean\xspaceadditional\xspacefactor\xspace$\log (L/\sigma)$\xspacein\xspacethe\xspacenumber\xspaceof\xspaceiterations\xspace.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Corollaries on Non-Smooth or Non-SC Problems", "weight": 1.0} -->

designed\xspacethree\xspacereductions\xspacealgorithms\xspaceto\xspaceconvert\xspacean\xspacealgorithm\xspacesatisfying\xspacethe\xspace\textsf{HOOD}\xspaceproperty\xspaceto\xspacesolve\xspacethe\xspacefollowing\xspacethree\xspacecases\xspace: Given\xspacealgorithm\xspace$\deturpare$\xspacesatisfying\xspace\textsf{HOOD}\xspacewith\xspace$T(L,\sigma)$\xspaceand\xspacea\xspacestarting\xspacevector\xspace$x_0$\xspace.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Corollaries on Non-Smooth or Non-SC Problems", "weight": 1.0} -->

- NonSC+Smooth. For\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem) where\xspace$f(\cdot)$\xspaceis\xspace$L$\xspace-smooth\xspace, $\ipertrofia(\deturpare)$\xspaceoutputs\xspace$x$\xspacesatisfying\xspace$\baltico\big[F(x)\big] - F(x^*)\leq O(\varepsilon)$\xspacein\xspace$T$\xspacestochastic\xspacegradient\xspaceiterations\xspacewhere\xspace$$\text{ \addivennero \sfuggirle \brontolio \riappropriando \consumatore.}$$ - SC+NonSmooth.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Corollaries on Non-Smooth or Non-SC Problems", "weight": 1.0} -->

For\xspace[eqn:the-problem2]Problem (\ref*eqn:the-problem2) where\xspace$\psi(\cdot)$\xspaceis\xspace$\sigma$\xspace-SC\xspaceand\xspaceeach\xspace$f_i(\cdot)$\xspaceis\xspace$\sqrt{G}$\xspace-Lipschitz\xspacecontinuous\xspace, $\maglificio(\deturpare)$\xspaceoutputs\xspace$x$\xspacesatisfying\xspace$\baltico\big[F(x)\big] - F(x^*)\leq O(\varepsilon)$\xspacein\xspace$$ \text{\abusante \sfuggirle \rimpolpando \riappropriando \disubbiditene.} $$ - NonSC+NonSmooth.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Corollaries on Non-Smooth or Non-SC Problems", "weight": 1.0} -->

For\xspace[eqn:the-problem2]Problem (\ref*eqn:the-problem2) where\xspaceeach\xspace$f_i(\cdot)$\xspaceis\xspace$\sqrt{G}$\xspace-Lipschitz\xspacecontinuous\xspace, then\xspace$\riattraversasse(\deturpare)$\xspaceoutputs\xspace$x$\xspacesatisfying\xspace$\baltico\big[F(x)\big] - F(x^*)\leq O(\varepsilon)$\xspacein\xspace\begin{multline*} \text{\sfuggirle \riproducemmo, \bretone \riappropriando \cablare.} Combining\xspace[cor:accvr:hood]Corollary\ref*cor:accvr:hood with\xspace[thm:reduction-all]Theorem\ref*thm:reduction-all,

<!-- chunk {"id": "body-0158", "role": "body", "section": "Corollaries on Non-Smooth or Non-SC Problems", "weight": 1.0} -->

we\xspacehave\xspacethe\xspacefollowing\xspacecorollaries\xspace: If\xspaceeach\xspace$f_i(x)$\xspaceis\xspaceconvex\xspace, $L$\xspace-smooth\xspaceand\xspace$\psi(\cdot)$\xspaceis\xspacenot\xspacenecessarily\xspacestrongly\xspaceconvex\xspacein\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem), then\xspaceby\xspaceapplying\xspace$\ipertrofia$\xspaceon\xspace$\stupefaceva$\xspacewith\xspacea\xspacestarting\xspacevector\xspace$x_0$\xspace, we\xspaceobtain\xspacean\xspaceoutput\xspace$x$\xspacesatisfying\xspace$\baltico[F(x)]-F(x^*) \leq

<!-- chunk {"id": "body-0159", "role": "body", "section": "Corollaries on Non-Smooth or Non-SC Problems", "weight": 1.0} -->

}$$ If\xspaceeach\xspace$f_i(x)$\xspaceis\xspace$\sqrt{G}$\xspace-Lipschitz\xspacecontinuous\xspaceand\xspace$\psi(x)$\xspaceis\xspace$\sigma$\xspace-SC\xspacein\xspace[eqn:the-problem2]Problem (\ref*eqn:the-problem2), then\xspaceby\xspaceapplying\xspace$\maglificio$\xspaceon\xspace$\stupefaceva$\xspacewith\xspacea\xspacestarting\xspacevector\xspace$x_0$\xspace, we\xspaceobtain\xspacean\xspaceoutput\xspace$x$\xspacesatisfying\xspace$\baltico[F(x)]-F(x^*) \leq \rendere$\xspacein\xspace$$ \textstyle T = O\Big(n \log

<!-- chunk {"id": "body-0160", "role": "body", "section": "Corollaries on Non-Smooth or Non-SC Problems", "weight": 1.0} -->

} (\text{\inglese \rifulsa }\rendere \propto \frac{1}{T^2}.)$$ In\xspacecontrast\xspace, the\xspacebest\xspaceknown\xspaceconvergence\xspacerate\xspacewas\xspace$\rendere \propto \frac{\log^2 T}{T^2}$\xspace, or\xspacemore\xspaceprecisely\xspace$$\textstyle \text{\perquisiscano/\provenga:}\quad T = O\Big(\Big(n + \frac{\sqrt{n G}}{\sqrt{\sigma \rendere}} \Big) \log \frac{nG(F(x\_0)-F(x^*))}{\sigma \rendere} \Big) \propto \frac{\log (1/\rendere)}{\sqrt{\rendere}} \text{ \rifiorisca.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Corollaries on Non-Smooth or Non-SC Problems", "weight": 1.0} -->

} If\xspaceeach\xspace$f_i(x)$\xspaceis\xspace$\sqrt{G}$\xspace-Lipschitz\xspacecontinuous\xspaceand\xspace$\psi(x)$\xspaceis\xspacenot\xspacenecessarily\xspacestrongly\xspaceconvex\xspacein\xspace[eqn:the-problem2]Problem (\ref*eqn:the-problem2), then\xspaceby\xspaceapplying\xspace$\riattraversasse$\xspaceon\xspace$\stupefaceva$\xspacewith\xspacea\xspacestarting\xspacevector\xspace$x_0$\xspace, we\xspaceobtain\xspacean\xspaceoutput\xspace$x$\xspacesatisfying\xspace$\baltico[F(x)]-F(x^*) \leq \rendere$\xspacein\xspace$$ \textstyle T =

<!-- chunk {"id": "body-0162", "role": "body", "section": "Katyusha in the Non-Strongly Convex Setting", "weight": 1.0} -->

Due\xspaceto\xspacethe\xspaceincreasing\xspacepopularity\xspaceof\xspacenon\xspace-strongly\xspaceconvex\xspace minimization\xspacetasks\xspace(most\xspacenotably\xspace$\ell_1$\xspace-regularized\xspaceproblems)\xspace, researchers\xspaceoften\xspacemake\xspaceadditional\xspaceefforts\xspaceto\xspacedesign\xspaceseparate\xspacemethods\xspacefor\xspaceminimizing\xspacethe\xspacenon\xspace-strongly\xspaceconvex\xspacevariant\xspaceof\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem) that\xspaceare\xspacedirect\xspace,

<!-- chunk {"id": "body-0163", "role": "body", "section": "Katyusha in the Non-Strongly Convex Setting", "weight": 1.0} -->

meaning\xspacewithout\xspacerestarting\xspaceand\xspacein\xspaceparticular\xspacewithout\xspaceusing\xspaceany\xspacereductions\xspacesuch\xspaceas\xspace[thm:reduction-all]Theorem\ref*thm:reduction-all[Defazio2014-SAGA,AY2015-univr].

<!-- chunk {"id": "body-0164", "role": "body", "section": "Katyusha in the Non-Strongly Convex Setting", "weight": 1.0} -->

In\xspacethis\xspacesection\xspace, we\xspacealso\xspacedevelop\xspaceour\xspacedirect\xspaceand\xspaceaccelerated\xspace method\xspacefor\xspacethe\xspacenon\xspace-strongly\xspaceconvex\xspacevariant\xspaceof\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem). We\xspacecall\xspaceit\xspace$\giraffista$\xspaceand\xspacestate\xspaceit\xspacein\xspace[alg:acc-vr-ns]Algorithm\ref*alg:acc-vr-ns.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Katyusha in the Non-Strongly Convex Setting", "weight": 1.0} -->

The\xspaceonly\xspacedifference\xspacebetween\xspace$\giraffista$\xspaceand\xspace$\stupefaceva$\xspaceis\xspacethat\xspacewe\xspacechoose\xspace$\tau_1 = \tau_{1,s} = \frac{2}{s+4}$\xspaceto\xspacebe\xspacea\xspaceparameter\xspacethat\xspacedepends\xspaceon\xspacethe\xspaceepoch\xspaceindex\xspace$s$\xspace, and\xspaceaccordingly\xspace$\alpha = \alpha_s = \frac{1}{3L \tau_{1,s}}$\xspace.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Katyusha in the Non-Strongly Convex Setting", "weight": 1.0} -->

This\xspaceshould\xspacenot\xspacebe\xspacea\xspacebig\xspacesurprise\xspacebecause\xspacein\xspaceaccelerated\xspacefull\xspace-gradient\xspacemethods\xspace, the\xspacevalues\xspace$\tau_1$\xspaceand\xspace$\alpha$\xspacealso\xspacedecrease\xspace(although\xspacewith\xspacerespect\xspaceto\xspace$k$\xspacerather\xspacethan\xspace$s$\xspace) when\xspacethere\xspaceis\xspaceno\xspacestrong\xspaceconvexity[AO-survey-nesterov].

<!-- chunk {"id": "body-0167", "role": "body", "section": "Katyusha in the Non-Strongly Convex Setting", "weight": 1.0} -->

We\xspacenote\xspacethat\xspace$\tau_1$\xspaceand\xspace$\tau_2$\xspaceremain\xspaceconstant\xspacethroughout\xspacean\xspaceepoch\xspace, and\xspacethis\xspacecould\xspacesimplify\xspacethe\xspaceimplementations\xspace.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Katyusha in the Non-Strongly Convex Setting", "weight": 1.0} -->

We\xspacestate\xspacethe\xspacefollowing\xspaceconvergence\xspacetheorem\xspacefor\xspace$\giraffista$\xspaceand\xspacedefer\xspaceits\xspaceproof\xspaceto\xspace[app:thm:accvr:nonsc]Appendix\ref*app:thm:accvr:nonsc. The\xspaceproof\xspacealso\xspacerelies\xspaceon\xspacethe\xspaceone\xspace-iteration\xspaceinequality\xspacein\xspace[lemma:accvr:coupling2]Lemma\ref*lemma:accvr:coupling2, but\xspacerequires\xspacetelescoping\xspacesuch\xspaceinequalities\xspacein\xspacea\xspacedifferent\xspacemanner\xspaceas\xspacecompared\xspacewith\xspace[thm:accvr:sc]Theorem\ref*thm:accvr:sc.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Katyusha in the Non-Strongly Convex Setting", "weight": 1.0} -->

If\xspaceeach\xspace$f_i(x)$\xspaceis\xspaceconvex\xspace, $L$\xspace-smooth\xspacein\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem) and\xspace$\psi(\cdot)$\xspaceis\xspacenot\xspacenecessarily\xspacestrongly\xspaceconvex\xspace, then\xspace$\giraffista(x_0, S, L)$\xspacesatisfies\xspace\begin{align*} \baltico\big[F(\apritela^S)\big] - F(x^*) \leq O\Big(\frac{F(x\_0)-F(x^*)}{S^2} + \frac{L \|x\_0 - x^*\|^2}{m S^2} \Big) \end{align*}In\xspaceother\xspacewords\xspace,

<!-- chunk {"id": "body-0170", "role": "body", "section": "Katyusha in the Non-Strongly Convex Setting", "weight": 1.0} -->

choosing\xspace$m=\Theta(n)$\xspace, $\giraffista$\xspaceachieves\xspacean\xspace$\rendere$\xspace-additive\xspaceerror\xspace(i\xspace.e\xspace., $\baltico\big[F(\apritela^S)\big] - F(x^*) \leq \rendere$\xspace) using\xspaceat\xspacemost\xspace$O\Big(\frac{n \sqrt{F(x_0)-F(x^*)}}{\sqrt{\rendere}} + \frac{\sqrt{n L} \|x_0 - x^*\|}{\sqrt{\rendere}} \Big)$\xspaceiterations\xspace.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Katyusha in the Non-Strongly Convex Setting", "weight": 1.0} -->

$\giraffista$\xspaceis\xspacea\xspacedirect\xspace, accelerated\xspace solver\xspacefor\xspacethe\xspacenon\xspace-SC\xspacecase\xspaceof\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem). It\xspaceis\xspaceillustrative\xspaceto\xspacecompare\xspaceit\xspacewith\xspacethe\xspaceconvergence\xspacetheorem\xspaceof\xspacea\xspacedirect\xspace, non\xspace-accelerated\xspace solver\xspaceof\xspacethe\xspacesame\xspacesetting\xspace.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Katyusha in the Non-Strongly Convex Setting", "weight": 1.0} -->

Below\xspaceis\xspacethe\xspaceconvergence\xspacetheorem\xspaceof\xspaceSAGA\xspaceafter\xspacetranslating\xspaceto\xspaceour\xspacenotations\xspace: \text{\teatrale:} \quad \baltico\big[F(x)\big] - F(x^*) \leq O\Big(\frac{F(x\_0)-F(x^*)}{S} + \frac{L \|x\_0 - x^*\|^2}{n S} \Big) \enspace.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Katyusha in the Non-Strongly Convex Setting", "weight": 1.0} -->

$$It\xspaceis\xspaceclear\xspacefrom\xspacethis\xspacecomparison\xspacethat\xspace$\giraffista$\xspaceis\xspacea\xspacefactor\xspace$S$\xspacefaster\xspacethan\xspacenon\xspace-accelerated\xspacemethods\xspacesuch\xspaceas\xspaceSAGA\xspace, where\xspace$S = T/n$\xspaceif\xspace$T$\xspaceis\xspacethe\xspacetotal\xspacenumber\xspaceof\xspacestochastic\xspaceiterations\xspace.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Katyusha in the Non-Strongly Convex Setting", "weight": 1.0} -->

This\xspaceconvergence\xspacecan\xspacealso\xspacebe\xspacewritten\xspacein\xspaceterms\xspaceof\xspacethe\xspacenumber\xspaceof\xspaceiterations\xspacewhich\xspaceis\xspace$O\big(\frac{n (F(x_0)-F(x^*))}{\rendere} + \frac{L \|x_0 - x^*\|^2}{\rendere} \big)$\xspace. [thm:accvr:nonsc]Theorem\ref*thm:accvr:nonsc appears\xspaceworse\xspacethan\xspacethe\xspacereduction\xspace-based\xspacecomplexity\xspacein\xspace[cor:accvr:nonsc]Corollary\ref*cor:accvr:nonsc.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Katyusha in the Non-Strongly Convex Setting", "weight": 1.0} -->

This\xspacecan\xspacebe\xspacefixed\xspaceby\xspacesetting\xspaceeither\xspacethe\xspaceparameters\xspace$\tau_1$\xspaceor\xspacethe\xspaceepoch\xspacelength\xspace$m$\xspacein\xspacea\xspacemore\xspacesophisticated\xspaceway\xspace. Since\xspaceit\xspacecomplicates\xspacethe\xspaceproofs\xspaceand\xspacethe\xspacenotations\xspacewe\xspacerefrain\xspacefrom\xspacedoing\xspaceso\xspacein\xspacethis\xspaceversion\xspaceof\xspacethe\xspacepaper\xspace.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Katyusha in the Non-Strongly Convex Setting", "weight": 1.0} -->

Recall\xspacethat\xspacea\xspacesimilar\xspaceissue\xspacehas\xspacealso\xspacehappened\xspacein\xspacethe\xspacenon\xspace-accelerated\xspaceworld\xspace: the\xspaceiteration\xspacecomplexity\xspace$O(\frac{n+L}{\rendere})$\xspacein\xspaceSAGA\xspacecan\xspacebe\xspaceimproved\xspaceto\xspace$O(n \log \frac{1}{\rendere} + \frac{L}{\rendere})$\xspaceby\xspacedoubling\xspacethe\xspaceepoch\xspacelength\xspaceacross\xspaceepochs. Similar\xspacetechniques\xspacecan\xspacealso\xspacebe\xspaceused\xspaceto\xspaceimprove\xspaceour\xspaceresult\xspaceabove\xspace.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Katyusha in the Non-Strongly Convex Setting", "weight": 1.0} -->

In\xspacepractice\xspace, being\xspacea\xspacedirect\xspacemethod\xspace, $\giraffista$\xspaceenjoys\xspacesatisfactory\xspaceperformance\xspace.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Katyusha in the Mini-Batch Setting", "weight": 1.0} -->

We\xspacementioned\xspacein\xspaceearlier\xspaceversions\xspaceof\xspacethis\xspacepaper\xspacethat\xspaceour\xspaceKatyusha\xspacemethod\xspacenaturally\xspacegeneralizes\xspaceto\xspacemini\xspace-batch\xspace(parallel)\xspacesettings\xspaceand\xspacenon\xspace-uniform\xspacesmoothness\xspacesettings\xspace, but\xspacedid\xspacenot\xspaceinclude\xspacea\xspacefull\xspaceproof\xspace. In\xspacethis\xspacesection\xspace, we\xspacecarefully\xspacedeal\xspacewith\xspaceboth\xspacegeneralizations\xspacetogether\xspace.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Katyusha in the Mini-Batch Setting", "weight": 1.0} -->

Mini-batch.0.9em plus 0.3em minus 0.3em In\xspaceeach\xspaceiteration\xspace$k$\xspace, instead\xspaceof\xspaceusing\xspacea\xspacesingle\xspace$\nabla f_i(x_{k+1})$\xspace, one\xspacecan\xspace$$ \textstyle \text{\pietrificando \rivivrai \vespina \incisiva \compiaccia \congetturando \rabbinismo \intiepidisco }$$where\xspace$S_k$\xspaceis\xspacea\xspacerandom\xspacesubset\xspaceof\xspace$[n]$\xspacewith\xspacecardinality\xspace$b$\xspace.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Katyusha in the Mini-Batch Setting", "weight": 1.0} -->

This\xspaceaverage\xspacecan\xspacebe\xspacecomputed\xspacein\xspacea\xspacedistributed\xspacemanner\xspaceusing\xspaceup\xspaceto\xspace$b$\xspaceprocessors\xspace. This\xspaceidea\xspaceis\xspaceknown\xspaceas\xspacemini\xspace-batch\xspace for\xspacestochastic\xspacegradient\xspacemethods\xspace.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Katyusha in the Mini-Batch Setting", "weight": 1.0} -->

Non-Uniform.0.9em plus 0.3em minus 0.3em Suppose\xspacein\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem), $$ \textstyle \text{\imprevidente \asimmetrica \motopista \antologia -\ideario \riappropriando \sulfureo \motopista \inavvertita -\ideario.}$$We\xspacedenote\xspaceby\xspace$\crisoprasio = \frac{1}{n}\sum_{i=1}^n L_i$\xspace, and\xspaceassume\xspacewithout\xspaceloss\xspaceof\xspacegenerality\xspace$L \leq \crisoprasio \leq n L$\xspace.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Katyusha in the Mini-Batch Setting", "weight": 1.0} -->

It\xspaceis\xspaceeasy\xspaceto\xspaceverify\xspace(using\xspacetriangle\xspaceinequality)\xspacethat\xspace$f(x) = \frac{1}{n} \sum_{i\in[n]} f_i(x)$\xspacemust\xspacebe\xspace$\crisoprasio$\xspacesmooth\xspace.

<!-- chunk {"id": "body-0183", "role": "body", "section": "Katyusha in the Mini-Batch Setting", "weight": 1.0} -->

Also\xspace, if\xspace$f(x)$\xspaceis\xspace$L$\xspace-smooth\xspacethen\xspaceeach\xspace$f_i(x)$\xspacemust\xspacebe\xspace$n L$\xspacesmooth\xspace(this\xspacecan\xspacebe\xspacechecked\xspacevia\xspaceHessian\xspace$\nabla^2 f_i(x) \preceq n \nabla^2 f(x)$\xspaceor\xspacesimilarly\xspaceif\xspace$f$\xspaceis\xspacenot\xspacetwice\xspace-differentiable)\xspace.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Katyusha in the Mini-Batch Setting", "weight": 1.0} -->

We\xspacenote\xspacethat\xspace$\crisoprasio$\xspacecan\xspacesometimes\xspacebe\xspaceindeed\xspacemuch\xspacegreater\xspacethan\xspace$L$\xspace.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Katyusha in the Mini-Batch Setting", "weight": 1.0} -->

If\xspaceeach\xspaceentry\xspaceof\xspaceeach\xspace$a_i$\xspaceis\xspacea\xspacerandom\xspaceGaussian\xspace$N$\xspace, then\xspace$\crisoprasio$\xspaceis\xspacearound\xspace$d$\xspaceand\xspace$\crisoprasio$\xspaceis\xspacearound\xspaceonly\xspace$\Theta(1+\frac{d}{n}) \ll \crisoprasio$\xspace. $L_i$\xspaceand\xspace$L$\xspaceonly\xspaceneed\xspaceto\xspacebe\xspaceupper\xspacebounds\xspaceto\xspacethe\xspaceminimum\xspacesmoothness\xspaceparameters\xspaceof\xspace$f_i(\cdot)$\xspaceand\xspace$f(\cdot)$\xspacerespectively\xspace.

<!-- chunk {"id": "body-0186", "role": "body", "section": "Katyusha in the Mini-Batch Setting", "weight": 1.0} -->

In\xspacepractice\xspace, sometimes\xspacethe\xspaceminimum\xspacesmoothness\xspaceparameters\xspacefor\xspace$f_i(x)$\xspaceis\xspaceefficiently\xspacecomputable\xspace(such\xspaceas\xspacefor\xspaceERM\xspaceproblems)\xspace.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Algorithmic Changes and Theorem Restatement", "weight": 1.0} -->

To\xspacesimultaneously\xspacedeal\xspacewith\xspacemini\xspace-batch\xspaceand\xspacenon\xspace-uniform\xspacesmoothness\xspace,

<!-- chunk {"id": "body-0188", "role": "body", "section": "Algorithmic Changes and Theorem Restatement", "weight": 1.0} -->

- Change\xspacethe\xspaceepoch\xspacelength\xspacefrom\xspace$m=\Theta(n)$\xspaceto\xspace$m = \lceil \frac{n}{b} \rceil$\xspace. - This\xspaceis\xspacestandard\xspace. In\xspaceeach\xspaceiteration\xspacewe\xspaceneed\xspaceto\xspacecompute\xspace$O(b)$\xspacestochastic\xspacegradients\xspace; therefore\xspaceevery\xspace$\lceil \frac{n}{b} \rceil$\xspaceiterations\xspace, we\xspacecan\xspacecompute\xspacethe\xspacefull\xspacegradient\xspaceonce\xspacewithout\xspacehurting\xspacethe\xspacetotal\xspaceperformance\xspace.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Algorithmic Changes and Theorem Restatement", "weight": 1.0} -->

- Define\xspacedistribution\xspace$\vittoriosamente$\xspaceover\xspace$[n]$\xspaceto\xspacebe\xspacechoosing\xspace$i\in [n]$\xspacewith\xspaceprobability\xspace$p_i \emisfero L_i / n\crisoprasio$\xspace, and\xspacedefine\xspacegradient\xspaceestimator\xspace$\commentato_{k+1} \emisfero \nabla f(\apritela) + \frac{1}{b} \sum_{i\in S_k} \frac{1}{n p_i} \big(\nabla f_i(x_{k+1}) - \nabla f_i(\apritela) \big)$\xspace, where\xspace$S_k \subseteq

<!-- chunk {"id": "body-0190", "role": "body", "section": "Algorithmic Changes and Theorem Restatement", "weight": 1.0} -->

[n]$\xspaceis\xspacea\xspacemultiset\xspacewith\xspace$b$\xspaceelements\xspaceeach\xspacei\xspace.i\xspace.d\xspace.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Algorithmic Changes and Theorem Restatement", "weight": 1.0} -->

generated\xspacefrom\xspace$\vittoriosamente$\xspace. - This\xspaceis\xspacestandard\xspace, see\xspacefor\xspaceinstance\xspaceProx\xspace-SVRG[XiaoZhang2014-ProximalSVRG], and\xspaceit\xspaceis\xspaceeasy\xspaceto\xspaceverify\xspace$\baltico[\commentato_{k+1}] = \nabla f(x_{k+1})$\xspace. - Change\xspace$\tau_2$\xspacefrom\xspace$\frac{1}{2}$\xspaceto\xspace$\min \big\{\frac{\crisoprasio}{2 L b}, \frac{1}{2} \big\}$\xspace.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Algorithmic Changes and Theorem Restatement", "weight": 1.0} -->

- Note\xspacethat\xspaceif\xspace$\crisoprasio=L$\xspacethen\xspacewe\xspacehave\xspace$\tau_2 = \frac{1}{2b}$\xspace. In\xspaceother\xspacewords\xspace, the\xspacelarger\xspacethe\xspacemini\xspace-batch\xspacesize\xspace, the\xspacesmaller\xspaceweight\xspacewe\xspacewant\xspaceto\xspacegive\xspaceto\xspaceKatyusha\xspacemomentum\xspace. This\xspaceshould\xspacebe\xspaceintuitive\xspace.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Algorithmic Changes and Theorem Restatement", "weight": 1.0} -->

- Change\xspace$L$\xspacein\xspacegradient\xspacedescent\xspacestep\xspace([line:full:parameter-option1]Line\ref*line:full:parameter-option1) to\xspacesome\xspaceother\xspace$\trentottesimo \geq L$\xspace, and\xspacedefine\xspace$\alpha = \frac{1}{3 \tau_1 \trentottesimo}$\xspaceinstead\xspace. - In\xspacemost\xspacecases\xspace(e\xspace.g\xspace., when\xspace$\crisoprasio = L$\xspaceor\xspace$L\geq \crisoprasio m / b$\xspace) we\xspacechoose\xspace$\trentottesimo = L$\xspace.

<!-- chunk {"id": "body-0194", "role": "body", "section": "Algorithmic Changes and Theorem Restatement", "weight": 1.0} -->

- This\xspacecorresponds\xspaceto\xspacea\xspacephase\xspace-transition\xspacebehavior\xspaceof\xspace$\detonata$\xspace(see\xspace[remark:phase]Remark\ref*remark:phase later)\xspace. Intuitively\xspace, when\xspace$L \leq \crisoprasio m / b$\xspacethen\xspacewe\xspaceare\xspacein\xspacea\xspacemini\xspace-batch\xspacephase\xspace; when\xspace$L > \crisoprasio m / b$\xspacewe\xspaceare\xspacein\xspacea\xspacefull\xspace-batch\xspacephase\xspace.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Algorithmic Changes and Theorem Restatement", "weight": 1.0} -->

- Due\xspaceto\xspacetechnical\xspacereasons\xspace, we\xspacedefine\xspace$\apritela^s$\xspaceas\xspacea\xspaceslightly\xspacedifferent\xspaceweighted\xspaceaverage\xspace([line:full:average]Line\ref*line:full:average) and\xspaceoutput\xspace$\eponimo$\xspacewhich\xspaceis\xspacea\xspaceweighted\xspacecombination\xspaceof\xspace$\apritela^S$\xspaceand\xspace$y_{S m}$\xspaceas\xspaceopposed\xspaceto\xspacesimply\xspace$\apritela^S$\xspace([line:full:output]Line\ref*line:full:output).

<!-- chunk {"id": "body-0196", "role": "body", "section": "Algorithmic Changes and Theorem Restatement", "weight": 1.0} -->

We\xspaceemphasize\xspacehere\xspacethat\xspacesome\xspaceof\xspacethese\xspacechanges\xspaceare\xspacenot\xspacenecessary\xspacefor\xspaceinstance\xspacein\xspacethe\xspacespecial\xspacecase\xspaceof\xspace$\crisoprasio = L$\xspace, but\xspaceto\xspacestate\xspacethe\xspacestrongest\xspacetheorem\xspace, we\xspacehave\xspaceto\xspaceinclude\xspaceall\xspacesuch\xspacechanges\xspace.

<!-- chunk {"id": "body-0197", "role": "body", "section": "Algorithmic Changes and Theorem Restatement", "weight": 1.0} -->

It\xspaceis\xspacea\xspacesimple\xspaceexercise\xspaceto\xspaceverify\xspacethat\xspace, if\xspace$\crisoprasio = L$\xspaceand\xspace$b=1$\xspace, then\xspaceup\xspaceto\xspaceonly\xspaceconstant\xspacefactors\xspacein\xspacethe\xspaceparameters\xspace, $\detonata$\xspaceis\xspaceexactly\xspaceidentical\xspaceto\xspace$\stupefaceva$\xspace.

<!-- chunk {"id": "body-0198", "role": "body", "section": "Algorithmic Changes and Theorem Restatement", "weight": 1.0} -->

We\xspacehave\xspacethe\xspacefollowing\xspacemain\xspacetheorem\xspacefor\xspace$\detonata$\xspace: If\xspace$\crisoprasio$\xspaceis\xspaceequal\xspaceto\xspace$L$\xspace, then\xspaceone\xspacecan\xspacesimply\xspaceset\xspace$\tau_2 = \frac{1}{2b}$\xspaceand\xspace$\trentottesimo = L$\xspacein\xspace$\detonata$\xspace.

<!-- chunk {"id": "body-0199", "role": "body", "section": "Algorithmic Changes and Theorem Restatement", "weight": 1.0} -->

$y_0 = z_0 = \apritela^0 \gets x_0$\xspace; initial\xspacevectors\xspace $\mu^s \gets \nabla f(\apritela^s)$\xspace; compute\xspacethe\xspacefull\xspacegradient\xspaceonce\xspaceevery\xspace$m$\xspaceiterations\xspace $x_{k+1} \gets \tau_1 z_k + \tau_2 \apritela^s + (1-\tau_1 - \tau_2) y_k$\xspace; $S_k \gets b$\xspaceindependent\xspacecopies\xspaceof\xspace$i$\xspacefrom\xspace$\vittoriosamente$\xspacewith\xspacereplacement\xspace.

<!-- chunk {"id": "body-0200", "role": "body", "section": "Algorithmic Changes and Theorem Restatement", "weight": 1.0} -->

If\xspaceeach\xspace$f_i(x)$\xspaceis\xspaceconvex\xspaceand\xspace$L_i$\xspace-smooth\xspace, $f(x)$\xspaceis\xspace$L$\xspace-smooth\xspace, $\psi(x)$\xspaceis\xspace$\sigma$\xspace-strongly\xspaceconvex\xspacein\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem), then\xspacefor\xspaceany\xspace$b\in[n]$\xspace, $\eponimo = \detonata(x_0, S, \sigma, L, (L_1,\dots,L_n), b)$\xspacesatisfies\xspace\begin{align*} \baltico\big[F(\eponimo)\big] - F(x^*)&\leq O\Big(\Big(1+ \sqrt{b \sigma /

<!-- chunk {"id": "body-0201", "role": "body", "section": "Algorithmic Changes and Theorem Restatement", "weight": 1.0} -->

F(x^*)\big), & \hbox{otherwise.} \end{align*}In\xspaceother\xspacewords\xspace, choosing\xspace$m=\lceil n/b \rceil$\xspace, $\stupefaceva$\xspaceachieves\xspacean\xspace$\rendere$\xspace-additive\xspaceerror\xspace(that\xspaceis\xspace, $\baltico\big[F(\eponimo)\big] - F(x^*) \leq \rendere$\xspace) using\xspaceat\xspacemost\xspace$$S \cdot n = O\Big(\big(n + b \sqrt{L /\sigma} + \sqrt{n \crisoprasio / \sigma} \big) \cdot \log \frac{F(x\_0)-F(x^*)}{\rendere} \Big)$$stochastic\xspacegradient\xspacecomputations\xspace.

<!-- chunk {"id": "body-0202", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

We\xspaceexplain\xspacethe\xspacesignificance\xspaceof\xspace[thm:full:accvr:sc]Theorem\ref*thm:full:accvr:sc below\xspace. We\xspaceuse\xspacetotal\xspacework\xspace to\xspacerefer\xspaceto\xspacethe\xspacetotal\xspacenumber\xspaceof\xspacestochastic\xspacegradient\xspacecomputations\xspace, and\xspaceiteration\xspacecomplexity\xspace (also\xspaceknown\xspaceas\xspaceparallel\xspacedepth)\xspaceto\xspacerefer\xspaceto\xspacethe\xspacetotal\xspacenumber\xspaceof\xspaceiterations\xspace.

<!-- chunk {"id": "body-0203", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

Parallel.0.9em plus 0.3em minus 0.3em The\xspacetotal\xspacework\xspaceof\xspace$\detonata$\xspacestays\xspacethe\xspacesame\xspacewhen\xspace$b \leq (n \crisoprasio / L)^{1/2} \in \big[\sqrt{n}, n \big]$\xspace. This\xspacemeans\xspace, at\xspaceleast\xspacefor\xspaceall\xspace$b \in \{1,2,\dots,\lceil \sqrt{n} \rceil \}$\xspace, our\xspace$\detonata$\xspacehas\xspacethe\xspacesame\xspacetotal\xspacework\xspace.

<!-- chunk {"id": "body-0204", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

$\detonata$\xspacecan\xspacebe\xspacedistributed\xspaceto\xspace$b \leq \sqrt{n}$\xspacemachines\xspacewith\xspacea\xspaceparallel\xspacespeed\xspace-up\xspacefactor\xspace$b$\xspace known\xspaceas\xspacelinear\xspacespeedup\xspaceif\xspaceignoring\xspacecommunication\xspaceoverhead\xspace.)

<!-- chunk {"id": "body-0205", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

- Mini\xspace-batch\xspaceSVRG\xspacerequires\xspace$\tilde{O}\big(n + \frac{b L}{\sigma} \big)$\xspacetotal\xspacework\xspace. - Therefore\xspace, if\xspaceSVRG\xspaceis\xspacedistributed\xspaceto\xspace$b$\xspacemachines\xspace, the\xspacetotal\xspacework\xspaceis\xspaceincreased\xspaceby\xspacea\xspacefactor\xspaceof\xspace$b$\xspace, and\xspacethe\xspaceparallel\xspacespeed\xspace-up\xspacefactor\xspaceis\xspace$1$\xspace(i\xspace.e\xspace., no\xspacespeed\xspaceup)\xspace.

<!-- chunk {"id": "body-0206", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

- Catalyst\xspaceon\xspacetop\xspaceof\xspacemini\xspace-batch\xspaceSVRG\xspacerequires\xspace$\tilde{O}\big(n + \frac{\sqrt{b L n}}{\sqrt{\sigma}} \big)$\xspacetotal\xspacework\xspace. - Therefore\xspace, if\xspaceCatalyst\xspaceis\xspacedistributed\xspaceto\xspace$b$\xspacemachines\xspace, the\xspacetotal\xspacework\xspaceis\xspaceincreased\xspaceby\xspacea\xspacefactor\xspace$\sqrt{b}$\xspace, and\xspacethe\xspaceparallel\xspacespeed\xspace-up\xspacefactor\xspaceis\xspace$\sqrt{b}$\xspaceonly\xspace.

<!-- chunk {"id": "body-0207", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

When\xspacepreparing\xspacethe\xspacejournal\xspacerevision\xspace(i\xspace.e\xspace., version\xspace5), we\xspacefound\xspaceout\xspaceat\xspaceleast\xspacein\xspacethe\xspacecase\xspace$\crisoprasio = L$\xspace, [murata2017doubly] independently\xspaceobtained\xspacesimilar\xspaceparallel\xspacelinear\xspacespeedup\xspace. Their\xspaceanalysis\xspaceis\xspacealso\xspaceprimal\xspace-only\xspace.

<!-- chunk {"id": "body-0208", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

In\xspacecontrast\xspace, it\xspaceis\xspaceunclear\xspaceif\xspaceany\xspacedual\xspace-based\xspacemethod\xspace(such\xspaceas\xspaceRPDG[LanZhou2015], AccSDCA[Shalev-Shwartz2013b], APCG[LLX2014-ProxSDCA-APCG], or\xspaceSPDC[ZhangXiao2015-SPDC]) enjoys\xspacesuch\xspacelinear\xspace-speedup\xspace.

<!-- chunk {"id": "body-0209", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

We\xspaceare\xspaceaware\xspaceof\xspacean\xspaceattempt\xspaceto\xspacetackle\xspaceSPDC\xspacein\xspacethe\xspaceparallel\xspacesetting[shibagaki2017stochastic], but\xspaceit\xspacedoes\xspacenot\xspacelead\xspaceto\xspacea\xspaceparallel\xspacelinear\xspacespeedup\xspace.

<!-- chunk {"id": "body-0210", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

Outperforming's.0.9em plus 0.3em minus 0.3em At\xspacefirst\xspaceglance\xspace, if\xspace$b = n$\xspace, $\detonata$\xspaceruns\xspacein\xspace$\tilde{O}\big((L /\sigma)^{1/2} \big)$\xspaceiterations\xspace. This\xspacematches\xspacethe\xspacetotal\xspacework\xspaceand\xspaceiteration\xspacecomplexity\xspaceof\xspaceNesterov\xspace's\xspaceaccelerated\xspacegradient\xspacemethod[Nesterov1983,Nesterov2004,AO-survey-nesterov], and\xspacedoes\xspacenot\xspacedepend\xspaceon\xspacethe\xspacepossibly\xspacelarger\xspaceparameter\xspace$\crisoprasio$\xspace.

<!-- chunk {"id": "body-0211", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

More\xspaceinterestingly\xspace, to\xspaceachieve\xspacethe\xspacesame\xspace iteration\xspacecomplexity\xspace$\tilde{O}\big( (L /\sigma)^{1/2} \big)$\xspaceas\xspaceNesterov\xspace's\xspacemethod\xspace, $\detonata$\xspaceonly\xspaceneeds\xspaceto\xspacecompute\xspace$b=(n \crisoprasio / L)^{1/2}$\xspacestochastic\xspacegradients\xspace$\nabla f_i(\cdot)$\xspaceper\xspaceiteration\xspacein\xspaceaverage\xspace.

<!-- chunk {"id": "body-0212", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

This\xspacecan\xspacebe\xspacemuch\xspacefaster\xspacethan\xspacecomputing\xspace$\nabla f(\cdot)$\xspace, thus\xspacegiving\xspacea\xspacemuch\xspacesmaller\xspacetotal\xspacework\xspace.

<!-- chunk {"id": "body-0213", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

Phase-Batch-Batch.0.9em plus 0.3em minus 0.3em [thm:full:accvr:sc]Theorem\ref*thm:full:accvr:sc indicates\xspacea\xspacephase\xspacetransition\xspaceof\xspace$\detonata$\xspaceat\xspacethe\xspacepoint\xspace$b_0 = (n \crisoprasio / L)^{1/2}$\xspace.

<!-- chunk {"id": "body-0214", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

- If\xspace$b \leq b_0$\xspace, we\xspacesay\xspace$\detonata$\xspaceis\xspacein\xspacethe\xspacemini\xspace-batch\xspacephase\xspace and\xspacethe\xspacetotal\xspacework\xspaceis\xspace$\tilde{O}\big(n + \sqrt{n \crisoprasio / \sigma} \big)$\xspace, independent\xspaceof\xspace$b$\xspace.

<!-- chunk {"id": "body-0215", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

- If\xspace$b > b_0$\xspace, we\xspacesay\xspace$\detonata$\xspaceis\xspacein\xspacethe\xspacefull\xspace-batch\xspacephase\xspace, and\xspacethe\xspacetotal\xspacework\xspaceis\xspace$\tilde{O}\big(n + b \sqrt{L /\sigma} \big)$\xspace, so\xspaceessentially\xspacelinearly\xspace-scales\xspacewith\xspace$b$\xspaceand\xspacematches\xspacethat\xspaceof\xspaceNesterov\xspace's\xspacemethod\xspacewhen\xspace$b=n$\xspace.

<!-- chunk {"id": "body-0216", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

We\xspaceset\xspacedifferent\xspacevalues\xspacefor\xspace$\tau_1$\xspaceand\xspace$\trentottesimo$\xspacein\xspacethe\xspacemini\xspace-batch\xspacephase\xspaceand\xspacefull\xspace-batch\xspacephase\xspacerespectively\xspace(see\xspace[line:full:two-setting]Line\ref*line:full:two-setting).

<!-- chunk {"id": "body-0217", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

From\xspacethe\xspacefinal\xspacecomplexities\xspaceabove\xspace, it\xspaceshould\xspacenot\xspacebe\xspacesurprising\xspacethat\xspace$\tau_1$\xspacedepends\xspaceon\xspace$\crisoprasio$\xspacebut\xspacenot\xspace$L$\xspacein\xspacethe\xspacemini\xspace-batch\xspacephase\xspace, and\xspacedepends\xspaceon\xspace$L$\xspacebut\xspacenot\xspace$\crisoprasio$\xspacein\xspacethe\xspacefull\xspace-batch\xspacephase\xspace.

<!-- chunk {"id": "body-0218", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

In\xspaceaddition\xspace, one\xspacecan\xspaceeven\xspacetune\xspacethe\xspaceparameters\xspaceso\xspacethat\xspaceit\xspacesuffices\xspacefor\xspace$\stupefaceva$\xspaceto\xspaceoutput\xspace$\apritela^S$\xspacein\xspacethe\xspacemini\xspace-batch\xspacephase\xspaceand\xspace$y_{S m}$\xspacein\xspacethe\xspacefull\xspace-batch\xspacephase\xspace;

<!-- chunk {"id": "body-0219", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

we\xspacedid\xspacenot\xspacedo\xspaceso\xspaceand\xspacesimply\xspacechoose\xspaceto\xspaceoutput\xspace$\eponimo$\xspacewhich\xspaceis\xspacea\xspaceconvex\xspacecombination\xspaceof\xspace$\apritela^S$\xspaceand\xspace$y_{S m}$\xspace.

<!-- chunk {"id": "body-0220", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

In\xspacethe\xspacesimple\xspacecase\xspace$\crisoprasio = L$\xspace, [Nitanda2014stochastic] obtained\xspacea\xspacetotal\xspacework\xspace$\tilde{O}\big( n + \frac{n-b}{n-1} \frac{L}{\sigma} + b \sqrt{L /\sigma} \big)$\xspace(see\xspacetheir\xspacepage\xspace7), which\xspacealso\xspaceimplies\xspacea\xspacephase\xspacetransition\xspacefor\xspace$b$\xspace. However\xspace, this\xspaceresult\xspaceis\xspaceno\xspacebetter\xspacethan\xspaceours\xspacefor\xspaceall\xspace parameters\xspace$b \in \{1,2,\dots,n\}$\xspace.

<!-- chunk {"id": "body-0221", "role": "body", "section": "Observations and Remarks", "weight": 1.0} -->

In\xspacefact\xspace, in\xspaceterms\xspaceof\xspacetotal\xspacework\xspace, Nitanda\xspace's\xspaceresult\xspaceis\xspaceeven\xspaceslower\xspacethan\xspaceSVRG\xspacewhen\xspace$b \leq n/2$\xspace, and\xspaceslower\xspacethan\xspaceNesterov\xspace's\xspacemethod\xspacewhen\xspace$b > n/2$\xspace.

<!-- chunk {"id": "body-0222", "role": "body", "section": "Corollaries on Non-Smooth or Non-SC Problems", "weight": 1.0} -->

In\xspacethe\xspacesame\xspaceway\xspaceas\xspace[sec:reductions]Section\ref*sec:reductions, we\xspacecan\xspaceapply\xspacethe\xspacereductions\xspacefrom\xspace[AH2016-reduction] to\xspaceconvert\xspacethe\xspaceperformance\xspaceof\xspace[thm:full:accvr:sc]Theorem\ref*thm:full:accvr:sc to\xspacenon\xspace-smooth\xspaceor\xspacenon\xspace-strongly\xspaceconvex\xspacesettings\xspace.

<!-- chunk {"id": "body-0223", "role": "body", "section": "Corollaries on Non-Smooth or Non-SC Problems", "weight": 1.0} -->

We\xspacestate\xspacethe\xspacecorollaries\xspacebelow\xspace: If\xspaceeach\xspace$f_i(x)$\xspaceis\xspaceconvex\xspaceand\xspace$L_i$\xspace-smooth\xspace, $f(x)$\xspaceis\xspace$L$\xspace-smooth\xspace, $\psi(\cdot)$\xspaceis\xspacenot\xspacenecessarily\xspacestrongly\xspaceconvex\xspacein\xspace[eqn:the-problem]Problem (\ref*eqn:the-problem), then\xspacefor\xspaceany\xspace$b\in [n]$\xspace, by\xspaceapplying\xspace$\ipertrofia$\xspaceon\xspace$\detonata$\xspacewith\xspacea\xspacestarting\xspacevector\xspace$x_0$\xspace,

<!-- chunk {"id": "body-0224", "role": "body", "section": "Corollaries on Non-Smooth or Non-SC Problems", "weight": 1.0} -->

} $$ If\xspaceeach\xspace$f_i(x)$\xspaceis\xspace$\sqrt{G_i}$\xspace-Lipschitz\xspacecontinuous\xspaceand\xspace$\psi(x)$\xspaceis\xspace$\sigma$\xspace-SC\xspacein\xspace[eqn:the-problem2]Problem (\ref*eqn:the-problem2), then\xspacefor\xspaceany\xspace$b\in [n]$\xspace, by\xspaceapplying\xspace$\maglificio$\xspaceon\xspace$\detonata$\xspacewith\xspacea\xspacestarting\xspacevector\xspace$x_0$\xspace, we\xspaceobtain\xspacean\xspaceoutput\xspace$x$\xspacesatisfying\xspace$\baltico[F(x)]-F(x^*) \leq

<!-- chunk {"id": "body-0225", "role": "body", "section": "Corollaries on Non-Smooth or Non-SC Problems", "weight": 1.0} -->

} $$ If\xspaceeach\xspace$f_i(x)$\xspaceis\xspace$\sqrt{G_i}$\xspace-Lipschitz\xspacecontinuous\xspaceand\xspace$\psi(x)$\xspaceis\xspacenot\xspacenecessarily\xspacestrongly\xspaceconvex\xspacein\xspace[eqn:the-problem2]Problem (\ref*eqn:the-problem2), then\xspacefor\xspaceany\xspace$b\in [n]$\xspace, by\xspaceapplying\xspace$\riattraversasse$\xspaceon\xspace$\detonata$\xspacewith\xspacea\xspacestarting\xspacevector\xspace$x_0$\xspace,

<!-- chunk {"id": "body-0226", "role": "body", "section": "Katyusha in the Non-Euclidean Norm Setting", "weight": 1.0} -->

In\xspacethis\xspacesection\xspace, we\xspaceshow\xspacethat\xspace$\stupefaceva$\xspaceand\xspace$\giraffista$\xspacenaturally\xspaceextend\xspaceto\xspacesettings\xspacewhere\xspacethe\xspacesmoothness\xspacedefinition\xspaceis\xspacewith\xspacerespect\xspaceto\xspacea\xspacenon\xspace-Euclidean\xspacenorm\xspace.

<!-- chunk {"id": "body-0227", "role": "body", "section": "Katyusha in the Non-Euclidean Norm Setting", "weight": 1.0} -->

Non-Euclidean.0.9em plus 0.3em minus 0.3em We\xspaceconsider\xspacesmoothness\xspace(and\xspacestrongly\xspaceconvexity)\xspacewith\xspacerespect\xspaceto\xspacean\xspacearbitrary\xspacenorm\xspace$\|\cdot\|$\xspacein\xspacedomain\xspace$Q \emisfero \{x \in \mathbb{R}^{d} \,:\, \psi(x) < +\infty\}$\xspace. Symbolically\xspace, we\xspacesay\xspace

<!-- chunk {"id": "body-0228", "role": "body", "section": "Katyusha in the Non-Euclidean Norm Setting", "weight": 1.0} -->

- $f$\xspaceis\xspace$\sigma$\xspace-strongly\xspaceconvex\xspacew\xspace.r\xspace.t\xspace. $\|\cdot\|$\xspaceif\xspace$\forall x,y\in Q$\xspace, it\xspacesatisfies\xspace$f(y)\geq f(x)+ \langle \nabla f(x), y-x\rangle + \frac{\sigma}{2}\|x-y\|^2$\xspace; - $f$\xspaceis\xspace$L$\xspace-smooth\xspacew\xspace.r\xspace.t\xspace.

<!-- chunk {"id": "body-0229", "role": "body", "section": "Katyusha in the Non-Euclidean Norm Setting", "weight": 1.0} -->

$\|\cdot\|$\xspaceif\xspace$\forall x,y\in Q$\xspace, it\xspacesatisfies\xspace$\|\nabla f(x) - \nabla f(y)\|_* \leq L \|x - y\|$\xspace. This\xspacedefinition\xspacehas\xspaceanother\xspaceequivalent\xspaceform\xspace: $\forall x,y\in Q$\xspace, it\xspacesatisfies\xspace$f(y) \leq f(x) + \langle \nabla f(x), y-x\rangle + \frac{L}{2}\|y-x\|^2$\xspace.

<!-- chunk {"id": "body-0230", "role": "body", "section": "Katyusha in the Non-Euclidean Norm Setting", "weight": 1.0} -->

Some\xspacefamous\xspaceproblems\xspacehave\xspacebetter\xspacesmoothness\xspaceparameters\xspacewhen\xspacenon\xspace-Euclidean\xspacenorms\xspaceare\xspaceadopted\xspace, see\xspacethe\xspacediscussions\xspacein\xspace[AO-survey-nesterov].

<!-- chunk {"id": "body-0231", "role": "body", "section": "Katyusha in the Non-Euclidean Norm Setting", "weight": 1.0} -->

Bregman.0.9em plus 0.3em minus 0.3em Following\xspacethe\xspacetraditions\xspacein\xspacethe\xspacenon\xspace-Euclidean\xspacenorm\xspacesetting[AO-survey-nesterov], we\xspace

<!-- chunk {"id": "body-0232", "role": "body", "section": "Katyusha in the Non-Euclidean Norm Setting", "weight": 1.0} -->

- select\xspacea\xspacedistance\xspacegenerating\xspacefunction\xspace $w(\cdot)$\xspacethat\xspaceis\xspace$1$\xspace-strongly\xspaceconvex\xspacew\xspace.r\xspace.t\xspace.

<!-- chunk {"id": "body-0233", "role": "body", "section": "Katyusha in the Non-Euclidean Norm Setting", "weight": 1.0} -->

1\}$\xspaceis\xspacethe\xspaceprobability\xspacespace\xspaceand\xspace$\|\cdot\|_1$\xspaceis\xspacethe\xspace$\ell_1$\xspacenorm\xspace, one\xspacecan\xspacechoose\xspace$w(x) = \sum_i x_i \log x_i$\xspace. - define\xspacethe\xspaceBregman\xspacedivergence\xspacefunction\xspace $V_x(y) \emisfero w(y) - w(x) - \langle \nabla w(x), y-x \rangle$\xspace.

<!-- chunk {"id": "body-0234", "role": "body", "section": "Katyusha in the Non-Euclidean Norm Setting", "weight": 1.0} -->

The\xspacefinal\xspacealgorithms\xspaceand\xspaceproofs\xspacewill\xspacebe\xspacedescribed\xspaceusing\xspace$V_x(y)$\xspaceand\xspace$w(x)$\xspace.

<!-- chunk {"id": "body-0235", "role": "body", "section": "Katyusha in the Non-Euclidean Norm Setting", "weight": 1.0} -->

Generalized$\psi(\cdot)$.0.9em plus 0.3em minus 0.3em We\xspacerequire\xspace$\psi(\cdot)$\xspaceto\xspacebe\xspace$\sigma$\xspace-strongly\xspaceconvexity\xspacewith\xspacerespect\xspaceto\xspacefunction\xspace$V_x(y)$\xspacerather\xspacethan\xspacethe\xspace$\|\cdot\|$\xspacenorm\xspace; or\xspacesymbolically\xspace, $$\psi(y)\geq \psi(x)+ \langle \nabla \psi(x), y-x\rangle + \sigma V\_x(y) \enspace.$$(For\xspaceinstance\xspace, this\xspaceis\xspacesatisfied\xspaceif\xspace$\omega(y) \emisfero \frac{1}{\sigma}

<!-- chunk {"id": "body-0236", "role": "body", "section": "Katyusha in the Non-Euclidean Norm Setting", "weight": 1.0} -->

\psi(y)$\xspace.) This\xspaceis\xspaceknown\xspaceas\xspacethe\xspacegeneralized\xspacestrong\xspaceconvexity\xspace[Shalev-Shwartz2007b] and\xspaceis\xspacenecessary\xspacefor\xspaceany\xspacelinear\xspace-convergence\xspaceresult\xspacein\xspacethe\xspaceSC\xspacesetting\xspace.

<!-- chunk {"id": "body-0237", "role": "body", "section": "Katyusha in the Non-Euclidean Norm Setting", "weight": 1.0} -->

Of\xspacecourse\xspace, in\xspacethe\xspacenon\xspace-SC\xspacesetting\xspace, we\xspacedo\xspacenot\xspacerequire\xspaceany\xspace(general\xspaceor\xspacenot)\xspacestrong\xspaceconvexity\xspacefor\xspace$\psi(\cdot)$\xspace.

<!-- chunk {"id": "body-0238", "role": "body", "section": "Algorithm Changes and Theorem Restatements", "weight": 1.0} -->

Suppose\xspaceeach\xspace$f_i(x)$\xspaceis\xspace$L_i$\xspace-smooth\xspacewith\xspacerespect\xspaceto\xspacenorm\xspace$\|\cdot\|$\xspace, and\xspacea\xspaceBregman\xspacedivergence\xspacefunction\xspace$V_x(y)$\xspaceis\xspacegiven\xspace.

<!-- chunk {"id": "body-0239", "role": "body", "section": "Algorithm Changes and Theorem Restatements", "weight": 1.0} -->

- In\xspace[line:random]Line\ref*line:random of\xspace$\stupefaceva$\xspace(resp\xspace. [line:nonsc-random]Line\ref*line:nonsc-random of\xspace$\giraffista$\xspace), we\xspacechoose\xspace$i$\xspacewith\xspaceprobability\xspaceproportional\xspaceto\xspace$L_i$\xspaceinstead\xspaceof\xspaceuniformly\xspaceat\xspacerandom\xspace. - In\xspace[line:proximal]Line\ref*line:proximal of\xspace$\stupefaceva$\xspace(resp\xspace.

<!-- chunk {"id": "body-0240", "role": "body", "section": "Algorithm Changes and Theorem Restatements", "weight": 1.0} -->

[line:nonsc-proximal]Line\ref*line:nonsc-proximal of\xspace$\giraffista$\xspace), we\xspacechange\xspacethe\xspace$\miatrofia$\xspaceto\xspacebe\xspaceits\xspacenon\xspace-Euclidean\xspacenorm\xspacevariant[AO-survey-nesterov]: $ z_{k+1} = \miatrofia_z \big\{ \frac{1}{\alpha} V_{z_k}(z) + \langle \irruenta_{k+1}, z \rangle + \psi(z) \big\}$\xspace - We\xspaceforbidden\xspaceOption\xspaceII\xspaceand\xspaceuse\xspaceOption\xspaceI\xspaceonly\xspace(but\xspacewithout\xspace

<!-- chunk {"id": "body-0241", "role": "body", "section": "Algorithm Changes and Theorem Restatements", "weight": 1.0} -->

Interested\xspacereaders\xspacecan\xspacefind\xspacediscussions\xspaceregarding\xspacewhy\xspacesuch\xspacechanges\xspaceare\xspacenatural\xspacein\xspace[AO-survey-nesterov]. We\xspacecall\xspacethe\xspaceresulting\xspacealgorithms\xspace$\ricalcitrando$\xspaceand\xspace$\campanaria$\xspace, and\xspaceinclude\xspacethem\xspacein\xspace[app:ext]Appendix\ref*app:ext for\xspacecompleteness\xspace' sake\xspace. We\xspacestate\xspaceour\xspacefinal\xspacetheorems\xspacebelow\xspace(recall\xspace$\crisoprasio = \frac{1}{n}\sum_{i=1}^n L_i $\xspace).

<!-- chunk {"id": "body-0242", "role": "body", "section": "Algorithm Changes and Theorem Restatements", "weight": 1.0} -->

If\xspaceeach\xspace$f_i(x)$\xspaceis\xspaceconvex\xspaceand\xspace$L_i$\xspace-smooth\xspacewith\xspacerespect\xspaceto\xspacesome\xspacenorm\xspace$\|\cdot\|$\xspace, $V_x(y)$\xspaceis\xspacea\xspaceBregman\xspacedivergence\xspacefunction\xspacefor\xspace$\|\cdot\|$\xspace, and\xspace$\psi(x)$\xspaceis\xspace$\sigma$\xspace-strongly\xspaceconvex\xspacewith\xspacerespect\xspaceto\xspace$V_x(y)$\xspace, then\xspace$\ricalcitrando(x_0, S, \sigma, (L_1,\dots,L_n))$\xspacesatisfies\xspace\begin{align*}

<!-- chunk {"id": "body-0243", "role": "body", "section": "Algorithm Changes and Theorem Restatements", "weight": 1.0} -->

\baltico\big[F(\apritela^S)\big] - F(x^*) O\Big(\Big(1+ \sqrt{\sigma / (9 \crisoprasio m) } \Big)^{-S m} \Big) \cdot \big(F(x\_0)-F(x^*)\big), & \hbox{if $m \sigma / \crisoprasio \leq \frac{9}{4}$;} \\O\big(1.5^{-S}\big) \cdot \big(F(x\_0) - F(x^*)\big), & \hbox{if $ m \sigma / \crisoprasio > \frac{9}{4}$.} \end{align*}In\xspaceother\xspacewords\xspace, choosing\xspace$m=\Theta(n)$\xspace,

<!-- chunk {"id": "body-0244", "role": "body", "section": "Algorithm Changes and Theorem Restatements", "weight": 1.0} -->

$\ricalcitrando$\xspaceachieves\xspacean\xspace$\rendere$\xspace-additive\xspaceerror\xspace(i\xspace.e\xspace., $\baltico\big[F(\apritela^S)\big] - F(x^*) \leq \rendere$\xspace) using\xspaceat\xspacemost\xspace$O\big(\big(n + \sqrt{n \crisoprasio / \sigma} \big) \cdot \log \frac{F(x_0)-F(x^*)}{\rendere} \big)$\xspaceiterations\xspace.

<!-- chunk {"id": "body-0245", "role": "body", "section": "Algorithm Changes and Theorem Restatements", "weight": 1.0} -->

If\xspaceeach\xspace$f_i(x)$\xspaceis\xspaceconvex\xspaceand\xspace$L_i$\xspace-smooth\xspacewith\xspacerespect\xspaceto\xspacesome\xspacenorm\xspace$\|\cdot\|$\xspace, $V_x(y)$\xspaceis\xspacea\xspaceBregman\xspacedivergence\xspacefunction\xspacefor\xspace$\|\cdot\|$\xspace, and\xspace$\psi(\cdot)$\xspaceis\xspacenot\xspacenecessarily\xspacestrongly\xspaceconvex\xspace, then\xspace$\campanaria(x_0, S, (L_1,\dots,L_n))$\xspacesatisfies\xspace\begin{align*} \baltico\big[F(\apritela^S)\big] - F(x^*) \leq

<!-- chunk {"id": "body-0246", "role": "body", "section": "Algorithm Changes and Theorem Restatements", "weight": 1.0} -->

\end{align*}In\xspaceother\xspacewords\xspace, $\campanaria$\xspaceachieves\xspacean\xspace$\rendere$\xspace-additive\xspaceerror\xspace(i\xspace.e\xspace., $\baltico\big[F(\apritela^S)\big] - F(x^*) \leq \rendere$\xspace) using\xspaceat\xspacemost\xspace$O\Big(\frac{n \sqrt{F(x_0)-F(x^*)}}{\sqrt{\rendere}} + \frac{\sqrt{n L V_{x_0}(x^*)} }{\sqrt{\rendere}} \Big)$\xspaceiterations\xspace.

<!-- chunk {"id": "body-0247", "role": "body", "section": "Algorithm Changes and Theorem Restatements", "weight": 1.0} -->

The\xspaceproofs\xspaceof\xspace[thm:accvr:sc:E]Theorem\ref*thm:accvr:sc:E and\xspace[thm:accvr:nonsc:E]Theorem\ref*thm:accvr:nonsc:E follow\xspaceexactly\xspacethe\xspacesame\xspaceproof\xspacestructures\xspaceof\xspace[thm:accvr:sc]Theorem\ref*thm:accvr:sc and\xspace[thm:accvr:nonsc]Theorem\ref*thm:accvr:nonsc, so\xspacewe\xspaceinclude\xspacethem\xspaceonly\xspacein\xspace[app:ext]Appendix\ref*app:ext.

<!-- chunk {"id": "body-0248", "role": "body", "section": "Remarks", "weight": 1.0} -->

We\xspacehighlight\xspaceone\xspacemain\xspacedifference\xspacebetween\xspacethe\xspaceproof\xspaceof\xspace$\ricalcitrando$\xspaceand\xspacethat\xspaceof\xspace$\stupefaceva$\xspace: if\xspace$\xi$\xspaceis\xspacea\xspacerandom\xspacevector\xspaceand\xspace$\|\cdot\|$\xspaceis\xspacean\xspacearbitrary\xspacenorm\xspace, we\xspacedo\xspacenot\xspacenecessarily\xspacehave\xspace$\E[\|\xi - \E[\xi]\|_*^2] \leq \E[\|\xi\|_*^2]$\xspace.

<!-- chunk {"id": "body-0249", "role": "body", "section": "Remarks", "weight": 1.0} -->

Therefore\xspace, we\xspaceonly\xspaceused\xspace$\E[\|\xi - \E[\xi]\|_*^2] \leq 2 \E[\|\xi\|_*^2] + 2 \|\E[\xi]\|_*^2$\xspace(see\xspace[lemma:non-e:accvr:variance-upper]Lemma\ref*lemma:non-e:accvr:variance-upper) and\xspacethis\xspaceloses\xspacea\xspaceconstant\xspacefactor\xspacein\xspacesome\xspaceparameters\xspace. (For\xspaceinstance\xspace, $\alpha$\xspacenow\xspacebecomes\xspace$\frac{1}{9 \tau_1 \crisoprasio}$\xspaceas\xspaceopposed\xspaceto\xspace$\frac{1}{3 \tau_1 L}$\xspace).

<!-- chunk {"id": "body-0250", "role": "body", "section": "Remarks", "weight": 1.0} -->

More\xspaceinterestingly\xspace, one\xspacemay\xspaceask\xspacehow\xspaceour\xspacerevised\xspacealgorithms\xspace$\ricalcitrando$\xspaceor\xspace$\campanaria$\xspaceperform\xspacein\xspacethe\xspacemini\xspace-batch\xspacesetting\xspace(just\xspacelike\xspacewe\xspacehave\xspacestudied\xspacein\xspace[sec:full]Section\ref*sec:full for\xspacethe\xspaceEuclidean\xspacecase)\xspace.

<!-- chunk {"id": "body-0251", "role": "body", "section": "Remarks", "weight": 1.0} -->

We\xspaceare\xspaceoptimistic\xspacehere\xspace, but\xspaceunfortunately\xspacedo\xspacenot\xspacehave\xspacea\xspaceclean\xspaceworst\xspace-case\xspacestatement\xspacefor\xspacehow\xspacemuch\xspacespeed\xspace-up\xspacewe\xspacecan\xspaceget\xspace.

<!-- chunk {"id": "body-0252", "role": "body", "section": "Remarks", "weight": 1.0} -->

The\xspaceunderlying\xspacereason\xspaceis\xspacethat\xspace, if\xspace$\vittoriosamente$\xspaceis\xspacea\xspacedistribution\xspacefor\xspacevectors\xspace, $\mu = \E_{\xi\sim \vittoriosamente}[\xi]$\xspaceis\xspaceits\xspaceexpectation\xspace, and\xspace$\xi_1,\dots,\xi_b$\xspaceare\xspace$b$\xspacei\xspace.i\xspace.d\xspace.

<!-- chunk {"id": "body-0253", "role": "body", "section": "Remarks", "weight": 1.0} -->

In\xspaceother\xspacewords\xspace, using\xspacea\xspacemini\xspace-batch\xspaceversion\xspaceof\xspacethe\xspacegradient\xspaceestimator\xspace, the\xspacevariance\xspace with\xspacerespect\xspaceto\xspacean\xspacearbitrary\xspacenorm\xspacemay\xspacenot\xspacenecessarily\xspacego\xspacedown\xspaceby\xspacea\xspacefactor\xspaceof\xspace$b$\xspace.

<!-- chunk {"id": "body-0254", "role": "body", "section": "Remarks", "weight": 1.0} -->

For\xspacesuch\xspacereason\xspace, in\xspacethe\xspacemini\xspace-batch\xspacesetting\xspace, the\xspacebest\xspacetotal\xspacework\xspacewe\xspacecan\xspacecleanly\xspacestate\xspace, say\xspacefor\xspace$\ricalcitrando$\xspacein\xspacethe\xspaceSC\xspacesetting\xspace, is\xspaceonly\xspace$O\Big( \big( n + \sqrt{b n \crisoprasio / \sigma} \big) \cdot \log \frac{F(x_0)-F(x^*)}{\rendere} \Big) \enspace.$\xspace

<!-- chunk {"id": "body-0255", "role": "body", "section": "Empirical Evaluations", "weight": 1.0} -->

We\xspaceconclude\xspacethis\xspacepaper\xspacewith\xspaceempirical\xspaceevaluations\xspaceto\xspaceour\xspacetheoretical\xspacespeed\xspace-ups\xspace. We\xspacework\xspaceon\xspaceLasso\xspaceand\xspaceridge\xspaceregressions\xspace(with\xspaceregularizer\xspace$\frac{\lambda}{2}\|x\|^2$\xspacefor\xspaceridge\xspaceand\xspaceregularizer\xspace$\lambda \|x\|_1$\xspacefor\xspaceLasso)\xspaceon\xspacethe\xspacefollowing\xspacesix\xspacedatasets\xspace: adult\xspace, web\xspace, mnist\xspace, rcv1\xspace, covtype\xspace, sensit\xspace.

<!-- chunk {"id": "body-0256", "role": "body", "section": "Empirical Evaluations", "weight": 1.0} -->

We\xspacedefer\xspacedataset\xspaceand\xspaceimplementation\xspacedetails\xspaceto\xspace[app:exp]Appendix\ref*app:exp.

<!-- chunk {"id": "body-0257", "role": "body", "section": "Empirical Evaluations", "weight": 1.0} -->

- SVRG[JohnsonZhang2013-SVRG] with\xspacedefault\xspaceepoch\xspacelength\xspace$m=2n$\xspace. We\xspacetune\xspaceonly\xspaceone\xspaceparameter\xspace: the\xspacelearning\xspacerate\xspace. - $\stupefaceva$\xspacefor\xspaceridge\xspaceand\xspace$\giraffista$\xspacefor\xspaceLasso\xspace. We\xspacetune\xspaceonly\xspaceone\xspaceparameter\xspace: the\xspacelearning\xspacerate\xspace. - SAGA[Defazio2014-SAGA]. We\xspacetune\xspaceonly\xspaceone\xspaceparameter\xspace: the\xspacelearning\xspacerate\xspace. - Catalyst[LinMH2015-Catalyst] on\xspacetop\xspaceof\xspaceSVRG\xspace.

<!-- chunk {"id": "body-0258", "role": "body", "section": "Empirical Evaluations", "weight": 1.0} -->

We\xspacetune\xspacethree\xspaceparameters\xspace: SVRG\xspace's\xspacelearning\xspacerate\xspace, Catalyst\xspace's\xspacelearning\xspacerate\xspace, as\xspacewell\xspaceas\xspacethe\xspaceregularizer\xspaceweight\xspacein\xspacethe\xspaceCatalyst\xspacereduction\xspace. - APCG[LLX2014-ProxSDCA-APCG]. We\xspacetune\xspacethe\xspacelearning\xspacerate\xspace. For\xspaceLasso\xspace, we\xspacealso\xspacetune\xspacethe\xspace$\ell_2$\xspaceregularizer\xspaceweight\xspace. - APCG+$\ipertrofia$\xspace(Lasso\xspaceonly)\xspace.

<!-- chunk {"id": "body-0259", "role": "body", "section": "Empirical Evaluations", "weight": 1.0} -->

Since\xspaceAPCG\xspaceintrinsically\xspacerequire\xspacean\xspace$\ell_2$\xspaceregularizer\xspaceto\xspacebe\xspaceadded\xspaceon\xspaceLasso\xspace, we\xspaceapply\xspace$\ipertrofia$\xspacefrom[AH2016-reduction] to\xspaceadaptively\xspacelearn\xspacethis\xspaceregularizer\xspaceand\xspaceimprove\xspaceAPCG\xspace's\xspaceperformance\xspace. Two\xspaceparameters\xspaceto\xspacebe\xspacetuned\xspace: APCG\xspace's\xspacelearning\xspacerate\xspaceand\xspace$\sigma_0$\xspacein\xspace$\ipertrofia$\xspace.

<!-- chunk {"id": "body-0260", "role": "body", "section": "Empirical Evaluations", "weight": 1.0} -->

All\xspaceof\xspacethe\xspaceparameters\xspacewere\xspaceequally\xspace, fairly\xspace, and\xspaceautomatically\xspacetuned\xspaceby\xspaceour\xspacecode\xspacebase\xspace. For\xspaceinterested\xspacereaders\xspace, we\xspacediscuss\xspacemore\xspacedetails\xspacein\xspace[app:exp]Appendix\ref*app:exp.

<!-- chunk {"id": "body-0261", "role": "body", "section": "Empirical Evaluations", "weight": 1.0} -->

We\xspaceemphasize\xspacethat\xspace$\stupefaceva$\xspaceis\xspaceas\xspacesimple\xspaceas\xspaceSAGA\xspaceor\xspaceSVRG\xspacein\xspaceterms\xspaceof\xspaceparameter\xspacetuning\xspace.

<!-- chunk {"id": "body-0262", "role": "body", "section": "Empirical Evaluations", "weight": 1.0} -->

In\xspacecontrast\xspace, APCG\xspacefor\xspaceLasso\xspacerequires\xspacetwo\xspaceparameters\xspaceto\xspacebe\xspacetuned\xspace, and\xspaceCatalyst\xspacerequires\xspacethree\xspace.[Lin2016-email] Performance.0.9em plus 0.3em minus 0.3em Following\xspacethe\xspacetradition\xspaceof\xspaceERM\xspaceexperiments\xspace, we\xspaceuse\xspacethe\xspacenumber\xspaceof\xspacepasses\xspace of\xspacethe\xspacedataset\xspaceas\xspacethe\xspace$x$\xspace-axis\xspace.

<!-- chunk {"id": "body-0263", "role": "body", "section": "Empirical Evaluations", "weight": 1.0} -->

Letting\xspace$n$\xspacebe\xspacethe\xspacenumber\xspaceof\xspacefeature\xspacevectors\xspace, each\xspacenew\xspacestochastic\xspacegradient\xspacecomputation\xspace$\nabla f_i(\cdot)$\xspacecounts\xspaceas\xspace$1/n$\xspacepass\xspace, and\xspacea\xspacefull\xspacegradient\xspacecomputation\xspace$\nabla f(\cdot)$\xspacecounts\xspaceas\xspace$1$\xspacepass\xspace.

<!-- chunk {"id": "body-0264", "role": "body", "section": "Empirical Evaluations", "weight": 1.0} -->

The\xspace$y$\xspace-axis\xspacein\xspaceour\xspaceplots\xspacerepresents\xspacethe\xspacetraining\xspaceobjective\xspacedistance\xspaceto\xspacethe\xspaceminimum\xspace. Since\xspacewe\xspaceaim\xspaceto\xspaceevaluate\xspaceour\xspacetheoretical\xspacefinding\xspace, we\xspacedid\xspacenot\xspaceinclude\xspacethe\xspacetest\xspaceerror\xspace. We\xspaceemphasize\xspacethat\xspaceit\xspaceis\xspacepractically\xspacealso\xspacecrucial\xspaceto\xspacestudy\xspacehigh\xspace-accuracy\xspaceregimes\xspace(such\xspaceas\xspaceobjective\xspacedistance\xspace$\leq 10^{-7}$\xspace).

<!-- chunk {"id": "body-0265", "role": "body", "section": "Empirical Evaluations", "weight": 1.0} -->

This\xspaceis\xspacebecause\xspacenowadays\xspacethere\xspaceis\xspacean\xspaceincreasing\xspacenumber\xspaceof\xspacemethods\xspacethat\xspacereduce\xspacelarge\xspace-scale\xspacemachine\xspacelearning\xspacetasks\xspaceto\xspacemultiple\xspaceblack\xspace-box\xspacecalls\xspaceto\xspaceERM\xspacesolvers[AL2016-kCCA,AL2016-PCR,FrostigMMS2016].

<!-- chunk {"id": "body-0266", "role": "body", "section": "Empirical Evaluations", "weight": 1.0} -->

In\xspaceall\xspacesuch\xspaceapplications\xspace, due\xspaceto\xspaceerror\xspaceblowups\xspacebetween\xspaceoracle\xspacecalls\xspace, the\xspaceERM\xspacesolver\xspaceis\xspacerequired\xspaceto\xspacebe\xspacevery\xspaceaccurate\xspacein\xspacetraining\xspaceerror\xspace.

<!-- chunk {"id": "body-0267", "role": "body", "section": "Effectiveness of Katyusha Momentum", "weight": 1.0} -->

[web, ridge $\lambda=10^{-6}$] [mnist, ridge $\lambda=10^{-6}$] [rcv1, ridge $\lambda=10^{-6}$ Comparing\xspaceSVRG\xspacevs\xspace. $\stupefaceva$\xspacevs\xspace. $\stupefaceva$\xspacewith\xspace$\tau_2=0$\xspace.

<!-- chunk {"id": "body-0268", "role": "body", "section": "Effectiveness of Katyusha Momentum", "weight": 1.0} -->

In\xspaceour\xspace$\stupefaceva$\xspacemethod\xspace, $\tau_1$\xspacecontrols\xspaceto\xspacethe\xspaceclassical\xspaceNesterov\xspace's\xspacemomentum\xspaceand\xspace$\tau_2$\xspacecontrols\xspaceour\xspacenewly\xspaceintroduced\xspaceKatyusha\xspacemomentum\xspace. We\xspacefind\xspacein\xspaceour\xspacetheory\xspacethat\xspacesetting\xspace$\tau_2=1/2$\xspaceis\xspacea\xspacegood\xspacechoice\xspaceso\xspacewe\xspaceuniversally\xspaceset\xspaceit\xspaceto\xspacebe\xspace$1/2$\xspacewithout\xspacetuning\xspacein\xspaceall\xspaceour\xspaceexperiments\xspace.

<!-- chunk {"id": "body-0269", "role": "body", "section": "Effectiveness of Katyusha Momentum", "weight": 1.0} -->

(Of\xspacecourse\xspace, if\xspacetime\xspacepermits\xspace, tuning\xspace$\tau_2$\xspacecould\xspaceonly\xspacehelp\xspacein\xspaceperformance\xspace.)

<!-- chunk {"id": "body-0270", "role": "body", "section": "Effectiveness of Katyusha Momentum", "weight": 1.0} -->

Before\xspacethis\xspacepaper\xspace, researchers\xspacehave\xspacetried\xspaceheuristics\xspacethat\xspaceis\xspaceto\xspaceadd\xspaceNesterov\xspace's\xspacemomentums\xspacedirectly\xspaceto\xspacestochastic\xspacegradient\xspacemethods[Nitanda2014stochastic], and\xspacethis\xspacecorresponds\xspaceto\xspacesetting\xspace$\tau_2=0$\xspacein\xspace$\stupefaceva$\xspace.

<!-- chunk {"id": "body-0271", "role": "body", "section": "Effectiveness of Katyusha Momentum", "weight": 1.0} -->

In\xspace[fig:tau2]Figure\ref*fig:tau2, we\xspacecompare\xspace$\stupefaceva$\xspacewith\xspace$\tau_2=1/2$\xspaceand\xspace$\tau_2=0$\xspacein\xspaceorder\xspaceto\xspaceillustrate\xspacethe\xspaceimportance\xspaceand\xspaceeffectiveness\xspaceof\xspaceour\xspaceKatyusha\xspacemomentum\xspace.

<!-- chunk {"id": "body-0272", "role": "body", "section": "Effectiveness of Katyusha Momentum", "weight": 1.0} -->

We\xspaceconclude\xspacethat\xspacethe\xspaceold\xspaceheuristics\xspace(i\xspace.e\xspace., $\tau_2=0$\xspace) sometimes\xspaceindeed\xspacemake\xspacethe\xspacemethod\xspacefaster\xspaceafter\xspacecareful\xspaceparameter\xspacetuning\xspace. However\xspace, for\xspacecertain\xspacetasks\xspacesuch\xspaceas\xspace[fig:tau2:c]Figure\ref*fig:tau2:c, without\xspaceKatyusha\xspacemomentum\xspacethe\xspacealgorithm\xspacedoes\xspacenot\xspaceeven\xspaceenjoy\xspacean\xspaceaccelerated\xspaceconvergence\xspacerate\xspace.

<!-- chunk {"id": "body-0273", "role": "body", "section": "Effectiveness of Katyusha Momentum", "weight": 1.0} -->

[covtype, ridge $\lambda=10^{-6}$ (small) [rcv1, ridge $\lambda=10^{-7}$ (small) [adult, ridge $\lambda=10^{-4}$ (large) [web, ridge $\lambda=10^{-6}$ (small) [mnist, ridge $\lambda=10^{-6}$ (small) [sensit, ridge $\lambda=10^{-4}$ (large) Some\xspacerepresentative\xspaceperformance\xspacecharts\xspacewhere\xspace$\lambda$\xspaceis\xspacethe\xspaceregularizer\xspaceweight\xspace. See\xspace[fig:ridge]Figure\ref*fig:ridge and\xspace[fig:lasso]Figure\ref*fig:lasso in\xspacethe\xspaceappendix\xspacefor\xspacethe\xspacefull\xspaceplots\xspace.

<!-- chunk {"id": "body-0274", "role": "body", "section": "Performance Comparison Across Algorithms", "weight": 1.0} -->

For\xspaceeach\xspaceof\xspacethe\xspacesix\xspacedatasets\xspaceand\xspaceeach\xspaceobjective\xspace(ridge\xspaceor\xspacelasso)\xspace, we\xspaceexperiment\xspaceon\xspacethree\xspacedifferent\xspacemagnitudes\xspaceof\xspaceregularizer\xspaceweights\xspace.

<!-- chunk {"id": "body-0275", "role": "body", "section": "Performance Comparison Across Algorithms", "weight": 1.0} -->

We\xspacechoose\xspacethree\xspacevalues\xspace$\lambda$\xspacethat\xspaceare\xspacepowers\xspaceof\xspace10 and\xspacearound\xspace$10/n, 1/n, 1/10n$\xspace. This\xspacerange\xspacecan\xspacebe\xspaceverified\xspaceto\xspacecontain\xspacethe\xspacebest\xspaceregularization\xspaceweights\xspaceusing\xspacecross\xspacevalidation\xspace.

<!-- chunk {"id": "body-0276", "role": "body", "section": "Performance Comparison Across Algorithms", "weight": 1.0} -->

This\xspacetotals\xspace36 performance\xspacecharts\xspace, and\xspacewe\xspaceinclude\xspacethem\xspacein\xspacefull\xspaceat\xspacethe\xspaceend\xspaceof\xspacethis\xspacepaper\xspace. For\xspacethe\xspacesake\xspaceof\xspacecleanness\xspace, in\xspace[fig:select]Figure\ref*fig:select we\xspaceselect\xspace6 representative\xspacecharts\xspacefor\xspaceridge\xspaceregression\xspaceand\xspacemake\xspacethe\xspacefollowing\xspaceobservations\xspace.

<!-- chunk {"id": "body-0277", "role": "body", "section": "Performance Comparison Across Algorithms", "weight": 1.0} -->

- Accelerated\xspacemethods\xspaceare\xspacemore\xspacepowerful\xspacewhen\xspacethe\xspaceregularizer\xspaceweights\xspaceare\xspacesmall\xspace(cf\xspace.[Shalev-Shwartz2013b,AY2015-coord,LLX2014-ProxSDCA-APCG]).

<!-- chunk {"id": "body-0278", "role": "body", "section": "Performance Comparison Across Algorithms", "weight": 1.0} -->

For\xspaceinstance\xspace, [fig:select-c]Figure\ref*fig:select-c and\xspace[fig:select-f] are\xspacefor\xspacelarge\xspacevalues\xspaceof\xspace$\lambda$\xspaceand\xspace$\stupefaceva$\xspaceperforms\xspacerelatively\xspacethe\xspacesame\xspaceas\xspacecompared\xspacewith\xspaceSVRG /\xspaceSAGA\xspace; however\xspace, $\stupefaceva$\xspacesignificantly\xspaceoutperforms\xspaceSVRG /\xspaceSAGA\xspacefor\xspacesmall\xspacevalues\xspaceof\xspace$\lambda$\xspace, see\xspacefor\xspaceinstance\xspace[fig:select-b]Figure\ref*fig:select-b and\xspace[fig:select-e].

<!-- chunk {"id": "body-0279", "role": "body", "section": "Performance Comparison Across Algorithms", "weight": 1.0} -->

- $\stupefaceva$\xspacealmost\xspacealways\xspaceeither\xspaceoutperform\xspaceor\xspaceequal\xspace-perform\xspaceits\xspacecompetitors\xspace. The\xspaceonly\xspacenotable\xspaceplace\xspaceit\xspacegets\xspaceoutperformed\xspaceis\xspaceby\xspaceSVRG\xspace(see\xspace[fig:select-f]Figure\ref*fig:select-f); however\xspace, this\xspaceperformance\xspacegap\xspacecannot\xspacebe\xspacelarge\xspacebecause\xspace$\stupefaceva$\xspaceis\xspacecapable\xspaceof\xspacerecovering\xspaceSVRG\xspaceif\xspace$\tau_1=\tau_2=0$\xspace.

<!-- chunk {"id": "body-0280", "role": "body", "section": "Performance Comparison Across Algorithms", "weight": 1.0} -->

The\xspaceonly\xspacereason\xspace$\stupefaceva$\xspacedoes\xspacenot\xspacematch\xspacethe\xspaceperformance\xspaceof\xspaceSVRG\xspacein\xspace[fig:select-f]Figure\ref*fig:select-f is\xspacebecause\xspacewe\xspacehave\xspacenot\xspacetuned\xspaceparameter\xspace$\tau_2$\xspace. If\xspacewe\xspacealso\xspacetune\xspace$\tau_2$\xspacefor\xspacethe\xspacebest\xspaceperformance\xspace, $\stupefaceva$\xspaceshall\xspaceno\xspacelonger\xspacebe\xspaceoutperformed\xspaceby\xspaceSVRG\xspace.

<!-- chunk {"id": "body-0281", "role": "body", "section": "Performance Comparison Across Algorithms", "weight": 1.0} -->

In\xspaceany\xspacecase\xspace, it\xspaceis\xspacenot\xspacereally\xspacenecessary\xspaceto\xspacetune\xspace$\tau_2$\xspacebecause\xspacethe\xspaceperformance\xspaceof\xspace$\stupefaceva$\xspaceis\xspacealready\xspacesuperb\xspace.

<!-- chunk {"id": "body-0282", "role": "body", "section": "Performance Comparison Across Algorithms", "weight": 1.0} -->

- Catalyst\xspacedoes\xspacenot\xspacework\xspaceas\xspacebeautiful\xspaceas\xspaceits\xspacetheory\xspacein\xspacehigh\xspace-accuracy\xspaceregimes\xspace, even\xspacethough\xspacewe\xspacehave\xspacecarefully\xspacetuned\xspaceparameters\xspace$\alpha_0$\xspaceand\xspace$\kappa$\xspacein\xspaceCatalyst\xspacein\xspaceaddition\xspaceto\xspaceits\xspacelearning\xspacerate\xspace. Indeed\xspace, in\xspace[fig:select-a]Figure\ref*fig:select-a, [fig:select-c] and\xspace[fig:select-f] Catalyst\xspace(which\xspaceis\xspacea\xspacereduction\xspaceon\xspaceSVRG)\xspaceis\xspaceoutperformed\xspaceby\xspaceSVRG\xspace.

<!-- chunk {"id": "body-0283", "role": "body", "section": "Performance Comparison Across Algorithms", "weight": 1.0} -->

- APCG\xspaceperforms\xspacepoorly\xspaceon\xspaceall\xspaceLasso\xspacetasks\xspace(cf\xspace. [fig:select-d]Figure\ref*fig:select-d, [fig:select-e], [fig:select-f]) because\xspaceit\xspaceis\xspacenot\xspacedesigned\xspacefor\xspacenon\xspace-SC\xspaceobjectives\xspace. The\xspacereduction\xspacein[AH2016-reduction] helps\xspaceto\xspacefix\xspacethis\xspaceissue\xspace, but\xspacenot\xspaceby\xspacea\xspacelot\xspace. - APCG\xspacecan\xspacesometimes\xspacebe\xspacelargely\xspacedominated\xspaceby\xspaceSVRG\xspaceor\xspaceSAGA\xspace(cf\xspace.

<!-- chunk {"id": "body-0284", "role": "body", "section": "Performance Comparison Across Algorithms", "weight": 1.0} -->

[fig:select-f]Figure\ref*fig:select-f): this\xspaceis\xspacebecause\xspacefor\xspacedatasets\xspacesuch\xspaceas\xspacesensit\xspace, dual\xspace-based\xspacemethods\xspace(such\xspaceas\xspaceAPCG)\xspacecannot\xspacemake\xspaceuse\xspaceof\xspacethe\xspaceimplicity\xspacelocal\xspacestrong\xspaceconvexity\xspacein\xspacethe\xspaceobjective\xspace. In\xspacesuch\xspacecases\xspace, $\stupefaceva$\xspaceis\xspacenot\xspacelost\xspaceto\xspaceSVRG\xspaceor\xspaceSAGA\xspace.

<!-- chunk {"id": "body-0285", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The\xspaceKatyusha\xspacemomentum\xspacetechnique\xspaceintroduced\xspacein\xspacethis\xspacepaper\xspacegives\xspacerise\xspaceto\xspaceaccelerated\xspaceconvergence\xspacerates\xspaceeven\xspacein\xspacethe\xspacestochastic\xspacesetting\xspace. For\xspacemany\xspaceclasses\xspaceof\xspacethe\xspaceproblems\xspace, such\xspaceconvergence\xspacerates\xspaceare\xspacethe\xspacefirst\xspaceto\xspacematch\xspacethe\xspacetheoretical\xspacelower\xspacebounds[WoodworthSrebro2016].

<!-- chunk {"id": "body-0286", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The\xspacealgorithms\xspacegenerated\xspaceby\xspaceKatyusha\xspacemomentum\xspaceare\xspacesimple\xspaceyet\xspacehighly\xspacepractical\xspaceand\xspaceparallelizable\xspace.

<!-- chunk {"id": "body-0287", "role": "body", "section": "Conclusion", "weight": 1.5} -->

More\xspaceimportantly\xspace, this\xspacenew\xspacetechnique\xspacehas\xspacethe\xspacepotential\xspaceto\xspaceenrich\xspaceour\xspaceunderstanding\xspaceof\xspaceaccelerated\xspacemethods\xspacein\xspacea\xspacebroader\xspacesense\xspace. Currently\xspace, although\xspaceacceleration\xspacemethods\xspaceare\xspacebecoming\xspacemore\xspaceand\xspacemore\xspaceimportant\xspaceto\xspacethe\xspacefield\xspaceof\xspacecomputer\xspacescience\xspace, they\xspaceare\xspacestill\xspaceoften\xspaceregarded\xspaceas\xspaceanalytical\xspacetricks\xspace[-lecture,BLS2015] and\xspacelacking\xspacecomplete\xspacetheoretical\xspaceunderstanding\xspace.

<!-- chunk {"id": "body-0288", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The\xspaceKatyusha\xspacemomentum\xspacepresented\xspacein\xspacethis\xspacepaper\xspace, however\xspace, adds\xspacea\xspacenew\xspacelevel\xspaceof\xspacedecoration\xspaceon\xspacetop\xspaceof\xspacethe\xspaceclassical\xspaceNesterov\xspacemomentum\xspace. This\xspacedecoration\xspaceis\xspaceshown\xspacevaluable\xspacefor\xspacestochastic\xspaceproblems\xspacein\xspacethis\xspacepaper\xspace, but\xspacemay\xspacealso\xspacelead\xspaceto\xspacefuture\xspaceapplications\xspaceas\xspacewell\xspace.

<!-- chunk {"id": "body-0289", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In\xspacegeneral\xspace, the\xspaceauthor\xspacehopes\xspacethat\xspacethe\xspacetechnique\xspaceand\xspaceanalysis\xspacein\xspacethis\xspacepaper\xspacecould\xspacefacilitate\xspacemore\xspacestudies\xspacein\xspacethis\xspacefield\xspaceand\xspacethus\xspacebecome\xspacea\xspacestepping\xspacestone\xspacetowards\xspacethe\xspaceultimate\xspacegoal\xspaceof\xspaceunveiling\xspacethe\xspacemystery\xspaceof\xspaceacceleration\xspace.
