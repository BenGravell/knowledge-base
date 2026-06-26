<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

CalArena: A Large-Scale Post-Hoc Calibration Benchmark

Topics include Calibration, Benchmarks, Post-hoc calibration, Classification, Reliability, Machine learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces a large standardized benchmark for post-hoc calibration across tabular and computer-vision classification settings. The paper is useful as an evaluation reference because it compares many calibration methods under consistent metrics and highlights where small-scale prior evaluations can mislead.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Reliable probability estimates are critical in many machine learning applications, yet modern classifiers are often poorly calibrated. Post-hoc calibration provides a simple and widely used solution, but the large number of proposed methods, combined with small-scale and inconsistent evaluations, makes it difficult to determine which approaches are truly effective in practice. We introduce a large-scale, standardized benchmark for post-hoc calibration, covering nearly 2000 experiments across tabular and computer vision tasks, including binary, multiclass, and large-scale classification settings. Our benchmark aggregates predictions from a diverse set of classical models, modern deep learning architectures, and foundation models, and provides unified, reproducible implementations of dozens of calibration methods within a common evaluation framework. We argue that Post-Hoc Improvement (PHI) in proper scoring rules offers a principled alternative to traditional calibration error estimators for comparing post-hoc methods, capturing both calibration quality and potential degradation to the model's predictive performance. Using this framework, we conduct the most comprehensive empirical study of post-hoc calibration to date.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our results reveal consistent patterns across domains: smooth calibration functions outperform binning-based approaches, dedicated multiclass methods are essential in high-dimensional settings, and generic machine learning models are not competitive without calibration-specific design. To facilitate future research, we release all data, code, and evaluation tools, providing a plug-and-play benchmark for developing and comparing calibration methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Accurate classification is central to many machine learning applications, ranging from medical diagnosis and fraud detection to autonomous driving and weather forecasting. Beyond predicting class labels, modern classifiers output probability distributions that reflect their confidence that the instance belongs to each class. These probabilistic predictions play a critical role in downstream decision-making, especially in high-stake settings where uncertainty must be explicitly accounted.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In practice, however, these predicted probabilities are often poorly calibrated: the predicted probabilities do not match observed class frequencies. This mismatch undermines the reliability and trustworthiness of machine learning systems. Miscalibration has been extensively documented across a wide range of models, from classical methods such as support vector machines and boosted trees to deep neural networks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A widely adopted approach to address this problem is *post-hoc calibration*, which adjusts predicted probabilities after training using a "calibration function" learned on a held-out validation set. A formal background on probability and post-hoc calibration is provided in Appendix˜A. Over the years, a large number of post-hoc calibration methods have been proposed for both binary and multiclass classification. Despite this abundance of methods, it remains unclear which approaches are most effective in practice, and under which conditions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

This lack of clarity stems from several key limitations in the current literature. First, existing empirical evaluations rely on small-scale or outdated benchmarks, limiting their representativeness of modern machine learning settings. Second, there is no consensus on how to properly evaluate calibration: commonly used metrics such as Expected Calibration Error (ECE) are known to be sensitive to design choices, making comparisons unreliable. Third, many proposed methods lack accessible, up-to-date implementations, preventing comprehensive and fair comparisons. As a result, two papers evaluating the same method can reach contradictory conclusions, and practitioners have no reliable basis for choosing a calibration method.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we address these challenges through the following contributions: We introduce a large-scale benchmark for post-hoc calibration, covering a diverse set of predictive settings, including classical and modern models, binary and multiclass tasks, and both tabular and computer vision domains (Section˜3).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We collect, standardize, and evaluate implementations of dozens of post-hoc calibration methods, enabling a comprehensive and reproducible comparison across methods and scenarios (Section˜4).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a well-grounded approach based on proper scores to compare post-hoc calibration methods, evaluating both the reduction in calibration error and degradation to the predictive performance (refinement error) of the initial model (Section˜5).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We derive actionable insights into the properties of effective calibration methods, providing guidance for practitioners and identifying promising directions for future research (Section˜7).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Figure˜1, we report leaderboards obtained by comparing binary and multiclass post-hoc calibration methods on benchmarks targeting different prediction settings. Details regarding our benchmark results are in Section˜6.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

We introduce a suite of benchmarks designed to rigorously evaluate post-hoc calibration methods. These benchmarks cover diverse data modalities (tabular and computer vision), task types (binary, multiclass, and large-scale multiclass), and model architectures (classical models, deep learning, and foundation models). Each benchmark comprises multiple experiments, where an experiment is defined as a dataset-model pair with associated validation and test set predictions. Validation set predictions are used to fit post-hoc calibration methods, while test set predictions allow us to evaluate and compare their performance.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Data Sources and Benchmark Construction", "weight": 1.0} -->

Table 1 summarizes the roughly 2000 classification experiments included in our study. To the best of our knowledge, this constitutes the most comprehensive collection dedicated to post-hoc calibration evaluation available in the literature. We construct these benchmarks by consolidating and structuring predictions from several data sources, as detailed below.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Data Sources and Benchmark Construction", "weight": 1.0} -->

#Models

<!-- chunk {"id": "body-0017", "role": "body", "section": "Data Sources and Benchmark Construction", "weight": 1.0} -->

#Datasets

<!-- chunk {"id": "body-0018", "role": "body", "section": "Data Sources and Benchmark Construction", "weight": 1.0} -->

#Experiments

<!-- chunk {"id": "body-0019", "role": "body", "section": "Data Sources and Benchmark Construction", "weight": 1.0} -->

*Includes eight native binary experiments plus five additional binarized CIFAR-10 experiments. Table 1: Summary of post-hoc calibration benchmarks constructed.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Classical Tabular Models (TabRepo)", "weight": 1.0} -->

We construct the TabRepo-binary and TabRepo-multiclass benchmarks using predictions from TabRepo, similar to. It stores predictions obtained by training classical machine learning and deep learning models on dozens of tabular datasets for a variety of hyperparameter configurations. We use predictions from eight widely used machine learning models: six classical algorithms (logistic regression, random forests, ExtraTrees, XGBoost, LightGBM, CatBoost ) and two neural networks from FastAI and AutoGluon. Predictions are stored for 104 binary datasets (yielding 832 experiments) and 65 multiclass datasets (yielding 520 experiments). We consider one classification task per dataset-model pair and select the hyperparameter configuration that achieves the lowest validation logloss (the *tuned* configuration).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Advanced Tabular Models (TabArena)", "weight": 1.0} -->

To target the post-hoc calibration of advanced tabular architectures, we create the TabArena-binary and TabArena-multiclass benchmarks using predictions from the large-scale tabular machine learning benchmark TabArena, similar to. We select 11 highly competitive models achieving over 1300 Elo on the TabArena leaderboard, excluding ensembles and models already present in TabRepo. This selection includes tabular foundation models (RealTabPFN-2.5, TabPFN-2.6, TabICL, TabICLv2, LimiX, BetaTabPFN, Mitra, TabDPT ) and deep learning models (RealMLP, TabM, ModernNCA ). As predictions are not available for every dataset-model pair, selecting the tuned configuration (based on validation ROC-AUC for binary and logloss for multiclass) results in 314 binary experiments across 30 datasets and 84 multiclass experiments across 8 datasets.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Computer Vision (CV) Models", "weight": 1.0} -->

Our vision benchmarks consolidate predictions from deep neural networks provided by Kull et al., which have become ubiquitous in post-hoc calibration evaluation, and Hekler et al., which cover more recent computer vision architectures like vision transformers. All provided logits are converted to probabilities prior to evaluation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Computer Vision (CV) Models", "weight": 1.0} -->

The CV-binary benchmark (13 experiments) includes four models trained on the Breast dataset, four on the Pneumonia dataset, and five experiments generated by binarizing multiclass predictions on CIFAR-10. We obtain binary predictions by summing the probabilities for all the "animal" classes (bird, cat, deer, dog, frog, horse) versus all the "machine" classes (airplane, automobile, ship, truck). This grouping creates a semantically meaningful and approximately balanced binary task.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Computer Vision (CV) Models", "weight": 1.0} -->

The CV-multiclass benchmark (20 experiments) spans predictions on CIFAR-10, CIFAR-100, SVHN, Caltech-UCSD Birds, Derma, and OCT.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Computer Vision (CV) Models", "weight": 1.0} -->

The ImageNet-multiclass benchmark (8 experiments) isolates ImageNet predictions, targeting the calibration of high-dimensional classification models (1000 classes).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Computer Vision (CV) Models", "weight": 1.0} -->

These benchmarks cover a broad spectrum of architectures, including classical convolutional networks (e.g., ResNet, DenseNet, Wide-ResNet, LeNet, ConvNeXt ) and modern vision transformers (e.g., ViT, BEiT, Swin, EVA ).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Data Availability and Reproducibility", "weight": 1.0} -->

Our benchmarks are constructed from predictions gathered across large external repositories. While all original predictions are publicly available, accessing them from TabRepo and TabArena requires downloading hundreds of gigabytes of data, making full reproduction from scratch highly resource-intensive. To eliminate this barrier, we republish the specific model predictions used in our benchmark on Hugging Face.^11^1We gratefully acknowledge the original creators for their permission to republish this data. The licenses for the original repositories can be found together with the benchmark files on our Hugging Face dataset. Each of our seven benchmarks is provided as a single HDF5 file, together with a CSV table enumerating every experiment it contains (dataset name, model name, calibration set size, test set size, number of classes, and specific configuration chosen from the original data source) so the scope and composition of each benchmark are fully transparent. The total download size of our benchmark is 1.71GB.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Evaluating a new calibration method", "weight": 1.0} -->

A key design goal of CalArena is to make evaluating a new calibration method as frictionless as possible. After downloading the benchmark files, a user only needs to implement two methods, fit(p_cal, y_cal) and predict_proba(p_test), and register the method in our dedicated custom_calibrators.py file. The evaluation script then handles data loading, applies the calibrator to every experiment in the chosen benchmark, computes all metrics, and writes the results to a CSV file. Running the full benchmark on a single calibrator requires a single command: python run_benchmark.py --benchmark tabrepo-binary --calibrator MyCalibrator For large-scale evaluation across all calibrators in parallel, we additionally provide SLURM batch scripts that submit one job per calibrator, isolating runtimes and enabling straightforward wall-clock comparisons on a compute cluster.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Analysis and visualization utilities", "weight": 1.0} -->

Beyond the benchmark runner, we provide a suite of analysis utilities covering the statistical tools used in this paper: bootstrap confidence intervals for winrates, Bradley--Terry Elo ratings, per-metric absolute improvements over the uncalibrated baseline, and the plotting functions used to generate all figures in this paper.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Call for contributions", "weight": 1.0} -->

We designed CalArena specifically to assist researchers in rigorously evaluating new post-hoc calibration techniques. To foster open community development and well-grounded research, we invite practitioners to contribute their methods directly to our repository or primary calibration package, probmetrics. By routinely executing the benchmarks on our compute cluster, we intend to maintain a regularly updated leaderboard, establishing a living infrastructure dedicated to the long-term advancement of post-hoc calibration.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Call for contributions", "weight": 1.0} -->

All the benchmark code is available at and the data can be downloaded from

<!-- chunk {"id": "body-0032", "role": "body", "section": "Post-hoc calibration methods", "weight": 1.0} -->

In this section we provide a short overview of the post-hoc calibration methods included in our benchmark. A complete description of each method is provided in Appendix˜B. We collect and standardize implementations of every post-hoc calibration method listed below in our open-source calibration package probmetrics at

<!-- chunk {"id": "body-0033", "role": "body", "section": "Binary methods", "weight": 1.0} -->

Our benchmark covers a diverse set of binary post-hoc calibration methods, beginning with foundational binning-based techniques. We include histogram regression using both fixed-sized bins (Hist-uniform) and a fixed number of samples per bin (Hist-quantile). We evaluate Bayesian Binning into Quantiles (BBQ), a well-known extension that addresses the sensitivity of choosing the number of bins by marginalizing over different binning schemes in a Bayesian fashion. Additionally, we include the hybrid Scaling-Binning approach by Kumar et al., which applies Platt scaling prior to binning.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Binary methods", "weight": 1.0} -->

Next, we evaluate order-preserving methods, exemplified by Isotonic Regression, arguably the most widely adopted nonparametric calibration technique. To explore improvements over this standard formulation, we also benchmark variants: Centered Isotonic Regression (CIR), and Venn-Abers calibration.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Binary methods", "weight": 1.0} -->

For parametric methods, we feature the widely used Platt Scaling, which applies an affine logistic transformation on the initial model's scores. Following the scikit-learn implementation, we try applying Platt scaling on predicted probabilities directly (Platt-probs), which we compare with the more natural idea of applying the transformation on logits instead (Platt-logits). We include Temperature Scaling (TS), as well as recent extensions, including Ensemble Temperature Scaling (ETS), and Quadratic Scaling. Finally, we also consider Beta calibration.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Binary methods", "weight": 1.0} -->

Our selection is further diversified by two spline-based methods: Spline Calibration, which models the recalibration mapping directly, and CDF-Spline, which maps probabilities by approximating the cumulative distribution function. We also adapt Kernel-based calibration-error estimation ideas from Popordanoska et al. into a post-hoc Nadaraya-Watson recalibration method.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Binary methods", "weight": 1.0} -->

Finally, we include tree-based post-hoc calibration with CatBoost, LightGBM and XGBoost classifiers.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Multiclass methods", "weight": 1.0} -->

For multiclass methods, we begin with natively multiclass calibration methods. The most widely used option is arguably temperature scaling (TS). Vector scaling (VS) and matrix scaling (MS) are extensions with additional parameters that were introduced by Guo et al.. Ensemble Temperature Scaling (ETS) is another variant that is multiclass compatible. Kull et al. propose adding regularization to matrix scaling, referring to the resulting method as Dirichlet calibration. Recently, Berta et al. revisited matrix and vector scaling regularization, introducing Structured Matrix Scaling (SMS) and Structured Vector Scaling (SVS). Finally, the Nadaraya-Watson Kernel estimator has been extended to the multiclass simplex with a Dirichlet kernel.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Multiclass methods", "weight": 1.0} -->

Beyond native multiclass methods, a widely used alternative is to apply binary calibration methods in a one-versus-rest (OvR) fashion, meaning that we fit one binary calibration function per class to calibrate the binary probability that the class, rather than any other class, is realized. Given a new sample, a calibrated probability vector is constructed by evaluating each binary calibrator once and normalizing the vector obtained to sum to one. We consider several binary methods applied OvR, namely: Hist-uniform, Hist-quantile, BBQ, Isotonic, CIR, Venn-Abers and Spline.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Metrics", "weight": 1.0} -->

Comparing the calibration performance of these methods on our benchmarks requires addressing the challenge of choosing meaningful metrics for comparison.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Calibration error estimators", "weight": 1.0} -->

Estimating the true calibration error of a classifier is notoriously hard. Most commonly, this is quantified by the Expected Calibration Error (ECE), popularized by Naeini et al. and Guo et al.. However, subsequent work has demonstrated theoretically and empirically the limits of such binning-based estimators. While significant effort has been dedicated to circumventing these limitations with smooth estimators, there are often difficulties in extending them to multiclass calibration error and no estimator is widely recognized as satisfactory by the calibration community. In this section we argue that this issue, while an open challenge in general, does not need to be resolved in the specific setting of comparing post-hoc calibration methods on a fixed benchmark.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Comparing post-hoc calibration methods with proper scoring rules", "weight": 1.0} -->

The risk (expected loss) measured with a proper score such as the Brier score or logloss, evaluates the general quality of probabilistic forecasts, measuring both calibration error and refinement error. Smaller risk can indicate smaller calibration error but also smaller refinement error, making it hard to draw conclusions on whether a model is well calibrated. In the context of post-hoc calibration (see Appendix˜A for a short introduction), however, where a function $g\colon\Delta_{K}\to\Delta_{K}$ is applied on top of a classifier $f(X)\in\Delta_{K}$, it is known (see for example Appendix A in Berta et al. ) that the post-hoc transformation cannot decrease the refinement error of the classifier: $\mathrm{Refinement}(g\circ f)\geq\mathrm{Refinement}(f)$. Specifically, the refinement error of $g\circ f$ is equal to that of $f$ if $g$ is an injection and can be larger otherwise.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Comparing post-hoc calibration methods with proper scoring rules", "weight": 1.0} -->

A smaller risk after post-hoc calibration thus necessarily comes from a reduced calibration error. Obviously, the post-hoc transformation might also increase the refinement error, which would also be reflected in the risk of $g\circ f$. We argue that this should be taken into account when evaluating $g$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Comparing post-hoc calibration methods with proper scoring rules", "weight": 1.0} -->

Considering only calibration error after post-hoc calibration can indeed be misleading. The easiest way to post-hoc calibrate any classifier $f$ is to make a constant prediction matching the empirical frequency of $Y$ on the calibration set $g(f(X))=\frac{1}{n_{\mathrm{cal}}}\sum_{i=1}^{n_{\mathrm{cal}}}Y_{i}$. This produces a roughly calibrated model $g\circ f$ but the discrimination power of the initial model $f$ is completely degraded; the refinement error of $g\circ f$ is maximized. A post-hoc calibration function $g$ should be judged by its capacity to reduce the calibration error of the initial classifier, while preserving its refinement error.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Comparing post-hoc calibration methods with proper scoring rules", "weight": 1.0} -->

This is easily measured by the difference in risk before and after calibration (for any proper loss $\ell$), or Post-Hoc Improvement (PHI, that we write $\Phi$), which we use as our metric of interest: $\Phi_{\ell}(g)=\mathbb{E}[\ell(f(X),Y)]-\mathbb{E}[\ell(g\circ f(X),Y)]$. Empirically, we evaluate $\Phi_{\ell}$ on the test set $(X_{i},Y_{i})_{1\leq i\leq n_{\mathrm{test}}}$: We subtract the risk after post-hoc calibration so that the metric is positively oriented, with larger improvement values indicating better recalibration.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Comparing post-hoc calibration methods with proper scoring rules", "weight": 1.0} -->

Generally we define $\Phi_{s}$ for any metric $s$, subtracting the metric evaluated before or after calibration depending on the orientation of $s$ so that $\Phi_{s}$ is always positively oriented, with positive values indicating improvement (larger accuracy or smaller Brier score for example) after post-hoc calibration and negative values indicating degradation.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Comparing post-hoc calibration methods with proper scoring rules", "weight": 1.0} -->

For the choice of proper loss $\ell$, we follow Selten, Dimitriadis et al. and many others in the probabilistic forecasting literature in considering that the potentially infinite value taken by logloss is problematic and we favor Brier score, making Post-Hoc Improvement in Brier score ($\Phi_{\mathrm{BS}}$) the main metric in our benchmark.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Other metrics", "weight": 1.0} -->

We also report PHI in logloss ($\Phi_{\mathrm{log}}$), ECE with 15 bins ($\Phi_{\mathrm{ECE-15}}$), accuracy ($\Phi_{\mathrm{Accuracy}}$) and, for binary experiments, the Kuiper calibration metric ($\Phi_{\mathrm{Kuiper}}$). For the multiclass experiments, we report the top-label version of the ECE for which probabilities assigned to the top class only are used for computing the calibration error.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Result aggregation", "weight": 1.0} -->

Given a metric of interest that we can compute for each calibration method on each experiment, we now ask how we should aggregate these results into a single informative ranking of post-hoc calibration methods.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Winrates", "weight": 1.0} -->

Given $m$ different methods, we compute the *winrate* of method $i$ as the proportion, between 0 and 1, of competing methods that are beaten. Denoting $s_{j}$ the metric of interest for method $j$, and assuming that larger $s$ is better, We aggregate results by averaging winrates for each method over all experiments in one benchmark. We compute 95% confidence intervals (CIs) on the winrate of each calibration method by bootstrapping datasets (when the benchmark contains enough different datasets) or experiments directly. We present results obtained in Section˜6. A strength of winrates is interpretability: to each calibration method, we assign a score between 0 and 1, estimating the probability that it beats another randomly chosen method from the benchmark on a new experiment.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Elo scores in a Bradley-Terry model", "weight": 1.0} -->

Following a trend in recent benchmarks, an alternative option is to compute Elo scores for each post-hoc calibration method by treating each experiment as a set of one-vs-one matches where method $i$ beats method $j$ if $s_{i}>s_{j}$. Elo scores for each method are computed using a Bradley-Terry model using the arena_rank Python package. We compute 95% CIs on the Elo scores by bootstrapping datasets or experiments directly. We present leaderboards for our benchmarks in Appendix˜F.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Absolute improvements", "weight": 1.0} -->

One issue with such rank-based aggregations is that the scale of the improvement is not considered. If $\Phi_{\mathrm{BS}}$ for method $i$ is marginally larger than for method $j$, this is still considered a win, and has the same impact on the final ranking as if the improvement is large. To account for this, we present raw improvement results in Appendix˜G, where we report post-hoc improvements for each method, averaged over all benchmark experiments. One weakness of this aggregation is that the scale of improvement varies a lot with models and datasets, making classical CIs less informative and giving more influence to experiments for which the initial loss is larger.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Statistical analysis", "weight": 1.0} -->

Finally, one can raise the issue of statistical significance. When comparing several classifiers over multiple experiments (which is what we do by comparing classifiers post-processed with different calibration functions), a standard approach is the evaluation procedure proposed by Demšar. We present results obtained with this procedure in Appendix˜H. We first reject the null hypothesis that all post-hoc calibration methods are equivalent with a Friedman test, and then perform pairwise comparisons with Nemenyi post-hoc tests to determine which methods are statistically distinguishable. We use the scikit-posthocs Python package, and communicate results with Critical Differences (CD) diagrams for each benchmark.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Results", "weight": 1.0} -->

In this section we present average winrates for each post-hoc calibration method on every benchmark where it is applicable. To put results in perspective, we include predictions from the non-calibrated model and treat them as an independent method (Base-model). While we only discuss performance here, we report the average runtimes of every calibration method considered in Appendix˜E.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Binary benchmarks", "weight": 1.0} -->

In Figure˜1 (top), we plot the leaderboard obtained when aggregating winrates for the TabRepo-binary, TabArena-binary and CV-binary benchmarks, targeting respectively the post-hoc calibration of classical binary classifiers on tabular datasets, advanced binary classifiers on tabular datasets and deep learning binary classifiers on CV datasets.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Binary benchmarks", "weight": 1.0} -->

Performance varies little on the TabRepo-binary benchmark---the maximum winrate is around 0.6 while the base model is around 0.5. This indicates that no method manages to consistently improve over the non-calibrated model or other post-hoc calibration methods. Platt-probs, XGBoost and binning-based methods even degrade the performance of the initial model. Three methods slightly outperform the others: Spline calibration, Quadratic scaling and Beta calibration.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Binary benchmarks", "weight": 1.0} -->

On the TabArena-binary benchmark, results are clearer, with the same three methods achieving more than 0.7 average winrate while the base model is below 0.5. Once again, several methods underperform the base model.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Binary benchmarks", "weight": 1.0} -->

The CV-binary benchmark contains fewer experiments so uncertainty is larger. Because the number of datasets is small, we compute CIs by bootstrapping experiments directly. One method is above 0.8 winrate while the base model is below 0.2, indicating that post-hoc calibration can yield consistent improvement. Interestingly, while Quadratic, Spline and Beta are still very good, other methods are also competitive: Platt-logits ranks first, CatBoost second and Venn-Abers (which barely improves upon the base model for tabular benchmarks) fourth.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Binary benchmarks", "weight": 1.0} -->

Averaging win rates across the three benchmarks, Quadratic scaling, Platt scaling on the logits, and Beta calibration emerge as the top-performing methods. All three apply logistic transformations on log probabilities predicted by the base model, with slightly different parameterizations (see Appendix˜B). These results suggest a strong advantage for parametric logistic approaches in binary post-hoc calibration. However, the non-parametric Spline calibration method ranks fourth and performs consistently well across all three benchmarks, indicating that carefully tuned non-parametric approaches may also be capable of achieving state-of-the-art performance in the binary setting.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Multiclass benchmarks", "weight": 1.0} -->

In Figure˜1 (bottom), we plot the results obtained for the multiclass calibration benchmarks.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Multiclass benchmarks", "weight": 1.0} -->

On the TabRepo-multiclass benchmark, which targets post-hoc calibration of classical tabular models on multiclass classification problems, one method stands out: SMS achieves over 0.7 winrate while the base model is below 0.5. SVS, which is a less parametrized version of SMS, ranks second. As in the binary benchmark, binning-based techniques (applied OvR here), are worse than the base model. This is also the case for XGBoost, Venn-Abers and Kernel. Not all OvR methods are disappointing, however, as CIR and Spline rank fourth and fifth, performing equivalently to VS.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Multiclass benchmarks", "weight": 1.0} -->

On the TabArena-multiclass benchmark, which mostly contains datasets with few classes, Spline, SMS and VS take the top three places, performing equivalently. This suggests that good OvR methods can be competitive, especially in low-dimensional settings and off-diagonal parameters and regularization are less crucial in these low-dimensional settings.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Multiclass benchmarks", "weight": 1.0} -->

On the CV-multiclass benchmark, the results are more pronounced. The base model is below 0.2 winrate, showing that post-hoc calibration is very effective. SMS ranks first with close to 0.95 winrate. SVS and VS complete the podium. Spline is still the best OvR method but lags far behind native multiclass methods on this benchmark, which includes high-dimensional datasets such as CIFAR-100.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Multiclass benchmarks", "weight": 1.0} -->

We defer results on our large-scale multiclass benchmark ImageNet-multiclass to Appendix˜D.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Multiclass benchmarks", "weight": 1.0} -->

Averaging win rates across the three benchmarks, SMS emerges as the clear winner, followed by SVS and VS. Once again, Spline calibration (applied OvR here) ranks fourth and achieves strong performance across the three benchmarks, although its results are noticeably weaker than the three leading methods on the CV benchmark. These findings further support the effectiveness of parametric logistic models for recalibration across a broad range of predictive settings. However, the comparatively poor performance of MS and Dirichlet calibration, despite their $k(k+1)$ parameters, reminds us that increased model flexibility does not necessarily translate into better calibration. In fact, neither method improves substantially over TS, which uses only a single parameter, highlighting the well-known susceptibility of highly parameterized calibration models to overfitting.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Smoothness matters", "weight": 1.0} -->

Smooth calibration functions clearly outperform binning-based methods on our benchmarks. This is well illustrated by the large performance gap observed between standard isotonic regression and CIR, which is a simple modification of the initial function that linearizes the jumps introduced by the PAV algorithm. This effect is also observed on multiclass predictions.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Smoothness matters", "weight": 1.0} -->

Binning-based methods seem appealing when considering simple calibration error estimators only: on the absolute improvement tables in Appendix˜G, we see that they rank very well for ECE-15. They are, however, very detrimental to overall performance, which is revealed by our Brier score benchmark. We argue that model calibration should not come at the cost of general performance, especially when other (smooth) techniques effectively reduce calibration error while preserving refinement error, as highlighted by our results.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Native multiclass methods are required for high-dimensional settings", "weight": 1.0} -->

While OvR methods, especially Spline and CIR, demonstrate promising results when the number of classes is small, results on the computer vision datasets, and in particular ImageNet (see Appendix˜D), show that native multiclass methods are required to tackle higher-dimensional problems. To demonstrate this, we plot in Figure˜3 the winrate of SMS (best multiclass method) against Spline (best OvR method) on the TabRepo-multiclass benchmark when considering datasets with $k$ classes or fewer, where $k$ varies along the x-axis. As we introduce higher-dimensional datasets in the benchmark, the winrate of SMS increases. It is below 0.5 on datasets with only 3 classes but improves a lot with as few as 4, 5 and 6 classes.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Calibration-specific design is necessary", "weight": 1.0} -->

Post-hoc calibration can be framed as a supervised learning problem: given a $K$-dimensional input (the uncalibrated probabilities), predict a calibrated $K$-dimensional probability vector. This perspective might suggest using off-the-shelf classifiers such as gradient boosting models. However, our results show that even with the (arguably unfair) advantage of early stopping, models like XGBoost, LightGBM, and CatBoost are consistently outperformed by dedicated calibration methods, applied with default hyperparameters. This indicates that generic machine learning models are not well-suited for post-hoc calibration without additional structure, and that calibration-specific design principles are essential. To illustrate this, we conduct a small experiment on the TabRepo-binary benchmark (see Figure˜3).

<!-- chunk {"id": "body-0070", "role": "body", "section": "Calibration-specific design is necessary", "weight": 1.0} -->

We compare a standard CatBoost model (100 trees, default settings) with variants incorporating simple calibration-oriented modifications: reducing the maximum tree depth to three to enforce a lightweight, regularized model and mitigate overfitting (tiny); enforcing monotonicity of the calibrated probabilities with respect to the original predictions, preserving their ranking (monotone). Each modification improves performance individually, and their combination yields the best results. This suggests that adapting existing models with calibration-specific constraints is a promising direction for future work.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented a large-scale, standardized benchmark for post-hoc calibration, covering nearly 2000 experiments across diverse models, datasets, and prediction settings. By unifying data sources, implementations, and evaluation protocols, our benchmark provides a reliable and reproducible framework for comparing calibration methods, addressing key limitations of prior empirical studies.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The use of Post-Hoc Improvement in proper scoring rules provides a principled metric for comparing calibration methods. This perspective avoids the pitfalls of traditional calibration error estimators and enables meaningful comparisons that account for both calibration quality and potential decrease in predictive performance induced by post-processing.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our empirical study yields several insights. Although promising non-parametric alternatives exist, parametric logistic post-hoc calibration models consistently outperform other existing approaches in both binary and multiclass settings. Smooth calibration methods also systematically outperform binning-based approaches, which often degrade predictive performance despite improving standard, overly simple calibration error metrics. Despite being promising in low-dimensional settings, one-versus-rest strategies fail to scale effectively and native multiclass methods are essential when the number of classes grows. Finally, generic machine learning models are not competitive out of the box for post-hoc calibration, highlighting the importance of calibration-specific design principles such as adapted regularization and monotonicity.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Beyond these findings, our benchmark is intended as a practical tool for the community to drive ongoing investigation of the relative strengths and weaknesses of various calibration methods. By releasing all data, code, and evaluation utilities in a plug-and-play framework, we aim to facilitate future research and enable fair, large-scale comparisons of new calibration methods, as well as existing calibration methods that are missing in our benchmark. We hope this work will contribute to establishing more reliable evaluation standards and accelerate progress in post-hoc calibration.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We discuss limitations of our benchmark that should be addressed in future work in Appendix˜C.
