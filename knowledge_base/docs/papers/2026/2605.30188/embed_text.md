<!-- arxiv-full-text:v1 {"arxiv_id": "2605.30188", "source": "arxiv-html"} -->

## Introduction

Accurate classification is central to many machine learning applications, ranging from medical diagnosis and fraud detection to autonomous driving and weather forecasting. Beyond predicting class labels, modern classifiers output probability distributions that reflect their confidence that the instance belongs to each class. These probabilistic predictions play a critical role in downstream decision-making, especially in high-stake settings where uncertainty must be explicitly accounted .

In practice, however, these predicted probabilities are often poorly calibrated: the predicted probabilities do not match observed class frequencies. This mismatch undermines the reliability and trustworthiness of machine learning systems. Miscalibration has been extensively documented across a wide range of models, from classical methods such as support vector machines and boosted trees to deep neural networks.

A widely adopted approach to address this problem is *post-hoc calibration*, which adjusts predicted probabilities after training using a "calibration function" learned on a held-out validation set. A formal background on probability and post-hoc calibration is provided in Appendix˜A. Over the years, a large number of post-hoc calibration methods have been proposed for both binary and multiclass classification. Despite this abundance of methods, it remains unclear which approaches are most effective in practice, and under which conditions.

This lack of clarity stems from several key limitations in the current literature. First, existing empirical evaluations rely on small-scale or outdated benchmarks, limiting their representativeness of modern machine learning settings. Second, there is no consensus on how to properly evaluate calibration: commonly used metrics such as Expected Calibration Error (ECE) are known to be sensitive to design choices, making comparisons unreliable. Third, many proposed methods lack accessible, up-to-date implementations, preventing comprehensive and fair comparisons. As a result, two papers evaluating the same method can reach contradictory conclusions, and practitioners have no reliable basis for choosing a calibration method.

In this work, we address these challenges through the following contributions: We introduce a large-scale benchmark for post-hoc calibration, covering a diverse set of predictive settings, including classical and modern models, binary and multiclass tasks, and both tabular and computer vision domains (Section˜3).

We collect, standardize, and evaluate implementations of dozens of post-hoc calibration methods, enabling a comprehensive and reproducible comparison across methods and scenarios (Section˜4).

We propose a well-grounded approach based on proper scores to compare post-hoc calibration methods, evaluating both the reduction in calibration error and degradation to the predictive performance (refinement error) of the initial model (Section˜5).

We derive actionable insights into the properties of effective calibration methods, providing guidance for practitioners and identifying promising directions for future research (Section˜7).

In Figure˜1, we report leaderboards obtained by comparing binary and multiclass post-hoc calibration methods on benchmarks targeting different prediction settings. Details regarding our benchmark results are in Section˜6.

## Related work

We discuss the calibration methods considered in this work in Section˜4 and provide additional background in Appendix˜B. Here, we focus on prior large-scale empirical studies of calibration and calibration evaluation. highlights the sensitivity of calibration evaluations to metric design choices, demonstrating that different calibration measures can lead to markedly different conclusions about the effectiveness of recalibration methods. performed a large-scale empirical study on calibration properties using Neural Architecture Search, examining, among other things, the reliability of calibration metrics. These findings highlight the importance of robust evaluation protocols when comparing calibration methods. investigate the effect of dataset shift on predictive uncertainty, including calibration. While not focused on post-hoc calibration, provide a standardized and reproducible benchmarking framework for uncertainty estimation that illustrates the value of shared implementations, evaluation pipelines, and leaderboards.

Regarding the evaluation of post-hoc calibration methods, provide one of the earliest widely recognized empirical comparisons of post-hoc calibration techniques on neural network predictions. released computer vision model predictions that have since been widely reused as a benchmark dataset. More recently, evaluated several binary and multiclass calibration methods using tabular predictions from the large-scale repository TabRepo. In a similar spirit, benchmark five calibration techniques on binary tabular classification tasks from TabArena, a follow-up to TabRepo.

CalArena extends this line of benchmarking efforts by providing a substantially broader experimental scope, covering binary, multiclass, and large-scale multiclass settings across both tabular (we use both TabRepo and TabArena) and vision domains, while evaluating a larger set of calibration methods. Beyond expanding the scope of experiments, CalArena is designed as a reusable and extensible benchmarking framework, with unified implementations and standardized evaluation protocols intended to facilitate reproducible comparison of both existing and newly proposed post-hoc calibration methods.

## Benchmarks

We introduce a suite of benchmarks designed to rigorously evaluate post-hoc calibration methods. These benchmarks cover diverse data modalities (tabular and computer vision), task types (binary, multiclass, and large-scale multiclass), and model architectures (classical models, deep learning, and foundation models). Each benchmark comprises multiple experiments, where an experiment is defined as a dataset-model pair with associated validation and test set predictions. Validation set predictions are used to fit post-hoc calibration methods, while test set predictions allow us to evaluate and compare their performance.

### Data Sources and Benchmark Construction

Table 1 summarizes the roughly 2000 classification experiments included in our study. To the best of our knowledge, this constitutes the most comprehensive collection dedicated to post-hoc calibration evaluation available in the literature. We construct these benchmarks by consolidating and structuring predictions from several data sources, as detailed below.

#Models

#Datasets

#Experiments

*Includes eight native binary experiments plus five additional binarized CIFAR-10 experiments. Table 1: Summary of post-hoc calibration benchmarks constructed.

### Classical Tabular Models (TabRepo)

We construct the TabRepo-binary and TabRepo-multiclass benchmarks using predictions from TabRepo, similar to. It stores predictions obtained by training classical machine learning and deep learning models on dozens of tabular datasets for a variety of hyperparameter configurations. We use predictions from eight widely used machine learning models: six classical algorithms (logistic regression, random forests, ExtraTrees, XGBoost, LightGBM, CatBoost ) and two neural networks from FastAI and AutoGluon. Predictions are stored for 104 binary datasets (yielding 832 experiments) and 65 multiclass datasets (yielding 520 experiments). We consider one classification task per dataset-model pair and select the hyperparameter configuration that achieves the lowest validation logloss (the *tuned* configuration).

### Advanced Tabular Models (TabArena)

To target the post-hoc calibration of advanced tabular architectures, we create the TabArena-binary and TabArena-multiclass benchmarks using predictions from the large-scale tabular machine learning benchmark TabArena, similar to. We select 11 highly competitive models achieving over 1300 Elo on the TabArena leaderboard, excluding ensembles and models already present in TabRepo. This selection includes tabular foundation models (RealTabPFN-2.5, TabPFN-2.6, TabICL, TabICLv2, LimiX, BetaTabPFN, Mitra, TabDPT ) and deep learning models (RealMLP, TabM, ModernNCA ). As predictions are not available for every dataset-model pair, selecting the tuned configuration (based on validation ROC-AUC for binary and logloss for multiclass) results in 314 binary experiments across 30 datasets and 84 multiclass experiments across 8 datasets.

### Computer Vision (CV) Models

Our vision benchmarks consolidate predictions from deep neural networks provided by Kull et al., which have become ubiquitous in post-hoc calibration evaluation, and Hekler et al., which cover more recent computer vision architectures like vision transformers. All provided logits are converted to probabilities prior to evaluation.

The CV-binary benchmark (13 experiments) includes four models trained on the Breast dataset, four on the Pneumonia dataset, and five experiments generated by binarizing multiclass predictions on CIFAR-10. We obtain binary predictions by summing the probabilities for all the "animal" classes (bird, cat, deer, dog, frog, horse) versus all the "machine" classes (airplane, automobile, ship, truck). This grouping creates a semantically meaningful and approximately balanced binary task.

The CV-multiclass benchmark (20 experiments) spans predictions on CIFAR-10, CIFAR-100, SVHN, Caltech-UCSD Birds, Derma, and OCT.

The ImageNet-multiclass benchmark (8 experiments) isolates ImageNet predictions, targeting the calibration of high-dimensional classification models (1000 classes).

These benchmarks cover a broad spectrum of architectures, including classical convolutional networks (e.g., ResNet, DenseNet, Wide-ResNet, LeNet, ConvNeXt ) and modern vision transformers (e.g., ViT, BEiT, Swin, EVA ).

### Data Availability and Reproducibility

Our benchmarks are constructed from predictions gathered across large external repositories. While all original predictions are publicly available, accessing them from TabRepo and TabArena requires downloading hundreds of gigabytes of data, making full reproduction from scratch highly resource-intensive. To eliminate this barrier, we republish the specific model predictions used in our benchmark on Hugging Face.^11^1We gratefully acknowledge the original creators for their permission to republish this data. The licenses for the original repositories can be found together with the benchmark files on our Hugging Face dataset. Each of our seven benchmarks is provided as a single HDF5 file, together with a CSV table enumerating every experiment it contains (dataset name, model name, calibration set size, test set size, number of classes, and specific configuration chosen from the original data source) so the scope and composition of each benchmark are fully transparent. The total download size of our benchmark is 1.71GB.

### Evaluating a new calibration method

A key design goal of CalArena is to make evaluating a new calibration method as frictionless as possible. After downloading the benchmark files, a user only needs to implement two methods, fit(p_cal, y_cal) and predict_proba(p_test), and register the method in our dedicated custom_calibrators.py file. The evaluation script then handles data loading, applies the calibrator to every experiment in the chosen benchmark, computes all metrics, and writes the results to a CSV file. Running the full benchmark on a single calibrator requires a single command: python run_benchmark.py --benchmark tabrepo-binary --calibrator MyCalibrator For large-scale evaluation across all calibrators in parallel, we additionally provide SLURM batch scripts that submit one job per calibrator, isolating runtimes and enabling straightforward wall-clock comparisons on a compute cluster.

### Analysis and visualization utilities

Beyond the benchmark runner, we provide a suite of analysis utilities covering the statistical tools used in this paper: bootstrap confidence intervals for winrates, Bradley--Terry Elo ratings, per-metric absolute improvements over the uncalibrated baseline, and the plotting functions used to generate all figures in this paper.

### Call for contributions

We designed CalArena specifically to assist researchers in rigorously evaluating new post-hoc calibration techniques. To foster open community development and well-grounded research, we invite practitioners to contribute their methods directly to our repository or primary calibration package, probmetrics. By routinely executing the benchmarks on our compute cluster, we intend to maintain a regularly updated leaderboard, establishing a living infrastructure dedicated to the long-term advancement of post-hoc calibration.

All the benchmark code is available at and the data can be downloaded from

## Post-hoc calibration methods

In this section we provide a short overview of the post-hoc calibration methods included in our benchmark. A complete description of each method is provided in Appendix˜B. We collect and standardize implementations of every post-hoc calibration method listed below in our open-source calibration package probmetrics at

### Binary methods

Our benchmark covers a diverse set of binary post-hoc calibration methods, beginning with foundational binning-based techniques. We include histogram regression using both fixed-sized bins (Hist-uniform) and a fixed number of samples per bin (Hist-quantile). We evaluate Bayesian Binning into Quantiles (BBQ), a well-known extension that addresses the sensitivity of choosing the number of bins by marginalizing over different binning schemes in a Bayesian fashion. Additionally, we include the hybrid Scaling-Binning approach by Kumar et al., which applies Platt scaling prior to binning.

Next, we evaluate order-preserving methods, exemplified by Isotonic Regression, arguably the most widely adopted nonparametric calibration technique. To explore improvements over this standard formulation, we also benchmark variants: Centered Isotonic Regression (CIR), and Venn-Abers calibration.

For parametric methods, we feature the widely used Platt Scaling, which applies an affine logistic transformation on the initial model's scores. Following the scikit-learn implementation, we try applying Platt scaling on predicted probabilities directly (Platt-probs), which we compare with the more natural idea of applying the transformation on logits instead (Platt-logits). We include Temperature Scaling (TS), as well as recent extensions, including Ensemble Temperature Scaling (ETS), and Quadratic Scaling. Finally, we also consider Beta calibration.

Our selection is further diversified by two spline-based methods: Spline Calibration, which models the recalibration mapping directly, and CDF-Spline, which maps probabilities by approximating the cumulative distribution function. We also adapt Kernel-based calibration-error estimation ideas from Popordanoska et al. into a post-hoc Nadaraya-Watson recalibration method.

Finally, we include tree-based post-hoc calibration with CatBoost, LightGBM and XGBoost classifiers.

### Multiclass methods

For multiclass methods, we begin with natively multiclass calibration methods. The most widely used option is arguably temperature scaling (TS). Vector scaling (VS) and matrix scaling (MS) are extensions with additional parameters that were introduced by Guo et al.. Ensemble Temperature Scaling (ETS) is another variant that is multiclass compatible. Kull et al. propose adding regularization to matrix scaling, referring to the resulting method as Dirichlet calibration. Recently, Berta et al. revisited matrix and vector scaling regularization, introducing Structured Matrix Scaling (SMS) and Structured Vector Scaling (SVS). Finally, the Nadaraya-Watson Kernel estimator has been extended to the multiclass simplex with a Dirichlet kernel.

Beyond native multiclass methods, a widely used alternative is to apply binary calibration methods in a one-versus-rest (OvR) fashion, meaning that we fit one binary calibration function per class to calibrate the binary probability that the class, rather than any other class, is realized. Given a new sample, a calibrated probability vector is constructed by evaluating each binary calibrator once and normalizing the vector obtained to sum to one. We consider several binary methods applied OvR, namely: Hist-uniform, Hist-quantile, BBQ, Isotonic, CIR, Venn-Abers and Spline.

## Metrics

Comparing the calibration performance of these methods on our benchmarks requires addressing the challenge of choosing meaningful metrics for comparison.

### Calibration metrics

### Calibration error estimators

Estimating the true calibration error of a classifier is notoriously hard. Most commonly, this is quantified by the Expected Calibration Error (ECE), popularized by Naeini et al. and Guo et al.. However, subsequent work has demonstrated theoretically and empirically the limits of such binning-based estimators. While significant effort has been dedicated to circumventing these limitations with smooth estimators, there are often difficulties in extending them to multiclass calibration error and no estimator is widely recognized as satisfactory by the calibration community. In this section we argue that this issue, while an open challenge in general, does not need to be resolved in the specific setting of comparing post-hoc calibration methods on a fixed benchmark.

### Comparing post-hoc calibration methods with proper scoring rules

The risk (expected loss) measured with a proper score such as the Brier score or logloss, evaluates the general quality of probabilistic forecasts, measuring both calibration error and refinement error. Smaller risk can indicate smaller calibration error but also smaller refinement error, making it hard to draw conclusions on whether a model is well calibrated. In the context of post-hoc calibration (see Appendix˜A for a short introduction), however, where a function $g\colon\Delta_{K}\to\Delta_{K}$ is applied on top of a classifier $f(X)\in\Delta_{K}$, it is known (see for example Appendix A in Berta et al. ) that the post-hoc transformation cannot decrease the refinement error of the classifier: $\mathrm{Refinement}(g\circ f)\geq\mathrm{Refinement}(f)$. Specifically, the refinement error of $g\circ f$ is equal to that of $f$ if $g$ is an injection and can be larger otherwise. A smaller risk after post-hoc calibration thus necessarily comes from a reduced calibration error. Obviously, the post-hoc transformation might also increase the refinement error, which would also be reflected in the risk of $g\circ f$. We argue that this should be taken into account when evaluating $g$.

Considering only calibration error after post-hoc calibration can indeed be misleading. The easiest way to post-hoc calibrate any classifier $f$ is to make a constant prediction matching the empirical frequency of $Y$ on the calibration set $g(f(X))=\frac{1}{n_{\mathrm{cal}}}\sum_{i=1}^{n_{\mathrm{cal}}}Y_{i}$. This produces a roughly calibrated model $g\circ f$ but the discrimination power of the initial model $f$ is completely degraded; the refinement error of $g\circ f$ is maximized. A post-hoc calibration function $g$ should be judged by its capacity to reduce the calibration error of the initial classifier, while preserving its refinement error. This is easily measured by the difference in risk before and after calibration (for any proper loss $\ell$), or Post-Hoc Improvement (PHI, that we write $\Phi$), which we use as our metric of interest: $\Phi_{\ell}(g)=\mathbb{E}[\ell(f(X),Y)]-\mathbb{E}[\ell(g\circ f(X),Y)]$. Empirically, we evaluate $\Phi_{\ell}$ on the test set $(X_{i},Y_{i})_{1\leq i\leq n_{\mathrm{test}}}$: We subtract the risk after post-hoc calibration so that the metric is positively oriented, with larger improvement values indicating better recalibration. Generally we define $\Phi_{s}$ for any metric $s$, subtracting the metric evaluated before or after calibration depending on the orientation of $s$ so that $\Phi_{s}$ is always positively oriented, with positive values indicating improvement (larger accuracy or smaller Brier score for example) after post-hoc calibration and negative values indicating degradation.

For the choice of proper loss $\ell$, we follow Selten, Dimitriadis et al. and many others in the probabilistic forecasting literature in considering that the potentially infinite value taken by logloss is problematic and we favor Brier score, making Post-Hoc Improvement in Brier score ($\Phi_{\mathrm{BS}}$) the main metric in our benchmark.

### Other metrics

We also report PHI in logloss ($\Phi_{\mathrm{log}}$), ECE with 15 bins ($\Phi_{\mathrm{ECE-15}}$), accuracy ($\Phi_{\mathrm{Accuracy}}$) and, for binary experiments, the Kuiper calibration metric ($\Phi_{\mathrm{Kuiper}}$). For the multiclass experiments, we report the top-label version of the ECE for which probabilities assigned to the top class only are used for computing the calibration error.

### Result aggregation

Given a metric of interest that we can compute for each calibration method on each experiment, we now ask how we should aggregate these results into a single informative ranking of post-hoc calibration methods.

### Winrates

Given $m$ different methods, we compute the *winrate* of method $i$ as the proportion, between 0 and 1, of competing methods that are beaten. Denoting $s_{j}$ the metric of interest for method $j$, and assuming that larger $s$ is better, We aggregate results by averaging winrates for each method over all experiments in one benchmark. We compute 95% confidence intervals (CIs) on the winrate of each calibration method by bootstrapping datasets (when the benchmark contains enough different datasets) or experiments directly. We present results obtained in Section˜6. A strength of winrates is interpretability: to each calibration method, we assign a score between 0 and 1, estimating the probability that it beats another randomly chosen method from the benchmark on a new experiment.

### Elo scores in a Bradley-Terry model

Following a trend in recent benchmarks, an alternative option is to compute Elo scores for each post-hoc calibration method by treating each experiment as a set of one-vs-one matches where method $i$ beats method $j$ if $s_{i}>s_{j}$. Elo scores for each method are computed using a Bradley-Terry model using the arena_rank Python package. We compute 95% CIs on the Elo scores by bootstrapping datasets or experiments directly. We present leaderboards for our benchmarks in Appendix˜F.

### Absolute improvements

One issue with such rank-based aggregations is that the scale of the improvement is not considered. If $\Phi_{\mathrm{BS}}$ for method $i$ is marginally larger than for method $j$, this is still considered a win, and has the same impact on the final ranking as if the improvement is large. To account for this, we present raw improvement results in Appendix˜G, where we report post-hoc improvements for each method, averaged over all benchmark experiments. One weakness of this aggregation is that the scale of improvement varies a lot with models and datasets, making classical CIs less informative and giving more influence to experiments for which the initial loss is larger.

### Statistical analysis

Finally, one can raise the issue of statistical significance. When comparing several classifiers over multiple experiments (which is what we do by comparing classifiers post-processed with different calibration functions), a standard approach is the evaluation procedure proposed by Demšar. We present results obtained with this procedure in Appendix˜H. We first reject the null hypothesis that all post-hoc calibration methods are equivalent with a Friedman test, and then perform pairwise comparisons with Nemenyi post-hoc tests to determine which methods are statistically distinguishable. We use the scikit-posthocs Python package, and communicate results with Critical Differences (CD) diagrams for each benchmark.

## Results

In this section we present average winrates for each post-hoc calibration method on every benchmark where it is applicable. To put results in perspective, we include predictions from the non-calibrated model and treat them as an independent method (Base-model). While we only discuss performance here, we report the average runtimes of every calibration method considered in Appendix˜E.

### Binary benchmarks

In Figure˜1 (top), we plot the leaderboard obtained when aggregating winrates for the TabRepo-binary, TabArena-binary and CV-binary benchmarks, targeting respectively the post-hoc calibration of classical binary classifiers on tabular datasets, advanced binary classifiers on tabular datasets and deep learning binary classifiers on CV datasets.

Performance varies little on the TabRepo-binary benchmark---the maximum winrate is around 0.6 while the base model is around 0.5. This indicates that no method manages to consistently improve over the non-calibrated model or other post-hoc calibration methods. Platt-probs, XGBoost and binning-based methods even degrade the performance of the initial model. Three methods slightly outperform the others: Spline calibration, Quadratic scaling and Beta calibration.

On the TabArena-binary benchmark, results are clearer, with the same three methods achieving more than 0.7 average winrate while the base model is below 0.5. Once again, several methods underperform the base model.

The CV-binary benchmark contains fewer experiments so uncertainty is larger. Because the number of datasets is small, we compute CIs by bootstrapping experiments directly. One method is above 0.8 winrate while the base model is below 0.2, indicating that post-hoc calibration can yield consistent improvement. Interestingly, while Quadratic, Spline and Beta are still very good, other methods are also competitive: Platt-logits ranks first, CatBoost second and Venn-Abers (which barely improves upon the base model for tabular benchmarks) fourth.

Averaging win rates across the three benchmarks, Quadratic scaling, Platt scaling on the logits, and Beta calibration emerge as the top-performing methods. All three apply logistic transformations on log probabilities predicted by the base model, with slightly different parameterizations (see Appendix˜B). These results suggest a strong advantage for parametric logistic approaches in binary post-hoc calibration. However, the non-parametric Spline calibration method ranks fourth and performs consistently well across all three benchmarks, indicating that carefully tuned non-parametric approaches may also be capable of achieving state-of-the-art performance in the binary setting.

### Multiclass benchmarks

In Figure˜1 (bottom), we plot the results obtained for the multiclass calibration benchmarks.

On the TabRepo-multiclass benchmark, which targets post-hoc calibration of classical tabular models on multiclass classification problems, one method stands out: SMS achieves over 0.7 winrate while the base model is below 0.5. SVS, which is a less parametrized version of SMS, ranks second. As in the binary benchmark, binning-based techniques (applied OvR here), are worse than the base model. This is also the case for XGBoost, Venn-Abers and Kernel. Not all OvR methods are disappointing, however, as CIR and Spline rank fourth and fifth, performing equivalently to VS.

On the TabArena-multiclass benchmark, which mostly contains datasets with few classes, Spline, SMS and VS take the top three places, performing equivalently. This suggests that good OvR methods can be competitive, especially in low-dimensional settings and off-diagonal parameters and regularization are less crucial in these low-dimensional settings.

On the CV-multiclass benchmark, the results are more pronounced. The base model is below 0.2 winrate, showing that post-hoc calibration is very effective. SMS ranks first with close to 0.95 winrate. SVS and VS complete the podium. Spline is still the best OvR method but lags far behind native multiclass methods on this benchmark, which includes high-dimensional datasets such as CIFAR-100.

We defer results on our large-scale multiclass benchmark ImageNet-multiclass to Appendix˜D.

Averaging win rates across the three benchmarks, SMS emerges as the clear winner, followed by SVS and VS. Once again, Spline calibration (applied OvR here) ranks fourth and achieves strong performance across the three benchmarks, although its results are noticeably weaker than the three leading methods on the CV benchmark. These findings further support the effectiveness of parametric logistic models for recalibration across a broad range of predictive settings. However, the comparatively poor performance of MS and Dirichlet calibration, despite their $k(k+1)$ parameters, reminds us that increased model flexibility does not necessarily translate into better calibration. In fact, neither method improves substantially over TS, which uses only a single parameter, highlighting the well-known susceptibility of highly parameterized calibration models to overfitting.

## Takeaways

### Smoothness matters

Smooth calibration functions clearly outperform binning-based methods on our benchmarks. This is well illustrated by the large performance gap observed between standard isotonic regression and CIR, which is a simple modification of the initial function that linearizes the jumps introduced by the PAV algorithm. This effect is also observed on multiclass predictions.

Binning-based methods seem appealing when considering simple calibration error estimators only: on the absolute improvement tables in Appendix˜G, we see that they rank very well for ECE-15. They are, however, very detrimental to overall performance, which is revealed by our Brier score benchmark. We argue that model calibration should not come at the cost of general performance, especially when other (smooth) techniques effectively reduce calibration error while preserving refinement error, as highlighted by our results.

### Native multiclass methods are required for high-dimensional settings

While OvR methods, especially Spline and CIR, demonstrate promising results when the number of classes is small, results on the computer vision datasets, and in particular ImageNet (see Appendix˜D), show that native multiclass methods are required to tackle higher-dimensional problems. To demonstrate this, we plot in Figure˜3 the winrate of SMS (best multiclass method) against Spline (best OvR method) on the TabRepo-multiclass benchmark when considering datasets with $k$ classes or fewer, where $k$ varies along the x-axis. As we introduce higher-dimensional datasets in the benchmark, the winrate of SMS increases. It is below 0.5 on datasets with only 3 classes but improves a lot with as few as 4, 5 and 6 classes.

Figure 2: Winrate of SMS against Spline when filtering the benchmark with datasets with at most k classes, with k along the x-axis.

Figure 3: Adding calibration design principles to a 100-tree CatBoost (CB) classifier significantly improves performance on the TabRepo-binary benchmark.

### Calibration-specific design is necessary

Post-hoc calibration can be framed as a supervised learning problem: given a $K$-dimensional input (the uncalibrated probabilities), predict a calibrated $K$-dimensional probability vector. This perspective might suggest using off-the-shelf classifiers such as gradient boosting models. However, our results show that even with the (arguably unfair) advantage of early stopping, models like XGBoost, LightGBM, and CatBoost are consistently outperformed by dedicated calibration methods, applied with default hyperparameters. This indicates that generic machine learning models are not well-suited for post-hoc calibration without additional structure, and that calibration-specific design principles are essential. To illustrate this, we conduct a small experiment on the TabRepo-binary benchmark (see Figure˜3). We compare a standard CatBoost model (100 trees, default settings) with variants incorporating simple calibration-oriented modifications: reducing the maximum tree depth to three to enforce a lightweight, regularized model and mitigate overfitting (tiny); enforcing monotonicity of the calibrated probabilities with respect to the original predictions, preserving their ranking (monotone). Each modification improves performance individually, and their combination yields the best results. This suggests that adapting existing models with calibration-specific constraints is a promising direction for future work.

## Conclusion

We presented a large-scale, standardized benchmark for post-hoc calibration, covering nearly 2000 experiments across diverse models, datasets, and prediction settings. By unifying data sources, implementations, and evaluation protocols, our benchmark provides a reliable and reproducible framework for comparing calibration methods, addressing key limitations of prior empirical studies.

The use of Post-Hoc Improvement in proper scoring rules provides a principled metric for comparing calibration methods. This perspective avoids the pitfalls of traditional calibration error estimators and enables meaningful comparisons that account for both calibration quality and potential decrease in predictive performance induced by post-processing.

Our empirical study yields several insights. Although promising non-parametric alternatives exist, parametric logistic post-hoc calibration models consistently outperform other existing approaches in both binary and multiclass settings. Smooth calibration methods also systematically outperform binning-based approaches, which often degrade predictive performance despite improving standard, overly simple calibration error metrics. Despite being promising in low-dimensional settings, one-versus-rest strategies fail to scale effectively and native multiclass methods are essential when the number of classes grows. Finally, generic machine learning models are not competitive out of the box for post-hoc calibration, highlighting the importance of calibration-specific design principles such as adapted regularization and monotonicity.

Beyond these findings, our benchmark is intended as a practical tool for the community to drive ongoing investigation of the relative strengths and weaknesses of various calibration methods. By releasing all data, code, and evaluation utilities in a plug-and-play framework, we aim to facilitate future research and enable fair, large-scale comparisons of new calibration methods, as well as existing calibration methods that are missing in our benchmark. We hope this work will contribute to establishing more reliable evaluation standards and accelerate progress in post-hoc calibration.

We discuss limitations of our benchmark that should be addressed in future work in Appendix˜C.
