<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Computational Inefficiency of Large Batch Sizes for Stochastic Gradient Descent

Topics include Stochastic gradient descent, Machine learning systems, Machine learning efficiency, Parallel computing, Optimization, Generalization, Neural networks.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Analyzes why increasing the batch size in stochastic gradient training can stop producing proportional wall-clock gains. The paper separates hardware utilization from optimization progress, giving a practical lens for deciding when large-batch training becomes computationally wasteful.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Increasing the mini-batch size for stochastic gradient descent offers significant opportunities to reduce wall-clock training time, but there are a variety of theoretical and systems challenges that impede the widespread success of this technique. We investigate these issues, with an emphasis on time to convergence and total computational cost, through an extensive empirical analysis of network training across several architectures and problem domains, including image classification, image segmentation, and language modeling. Although it is common practice to increase the batch size in order to fully exploit available computational resources, we find a substantially more nuanced picture. Our main finding is that across a wide range of network architectures and problem domains, increasing the batch size beyond a certain point yields no decrease in wall-clock time to convergence for either train or test loss. This batch size is usually substantially below the capacity of current systems. We show that popular training strategies for large batch size optimization begin to fail before we can populate all available compute resources, and we show that the point at which these methods break down depends more on attributes like model architecture and data complexity than it does directly on the size of the dataset.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Mini-batch stochastic gradient descent (SGD) is the dominant optimization method for training deep neural networks (DNNs). In the face of unprecedented growth in dataset size, a large body of work has attempted to scale SGD to train DNN models on increasingly large datasets, while keeping *wall-clock time* manageable. The most common approach to train large models at scale is distributed synchronous mini-batch SGD, which exploits additional computational resources through data parallelism. This technique reduces wall-clock training time by increasing the mini-batch size, i.e., the number of examples used to compute a stochastic estimate of the gradient of the loss function at each training iteration, while holding the number of epochs constant. Proponents of large batch size training often argue that the merits stem from its ability to decrease wall-clock training time while maintaining final model performance. Indeed, an enormous amount of work has gone into designing systems that seem to operate under an assumption that equates large batch size training with machine learning at scale.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Increasing the batch size improves the scaling performance of SGD per epoch, but there are significant challenges in building efficient distributed systems that are able to exploit additional computational resources to use large batch sizes. However, even if we were able to address these systems challenges, there are still more fundamental limitations to this approach. Large batch sizes often negatively impact important performance metrics of interest, including total computational cost (which usually determines monetary cost) and prediction quality.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we will measure the total computational cost as the number of training iterations times the work done per iteration---in order to simplify measurements, we use the number of training iterations as a proxy for the wall-clock time. We do this because the implementation of parallel algorithms depends on software and hardware choices, and our goal is to draw more general conclusions about the performance of SGD-based methods.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Based on this model for total computational cost and wall-clock time, the following should be clear: unless increasing the batch size leads to a commensurate decrease in the total number of training iterations *needed to find a good model*, large batch training will result in greater total computational cost with little-to-no decrease in wall-clock training time.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Linear: there is a small regime of batch sizes in which increasing the batch size results in linear gains in convergence speed;

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Diminishing returns: there is a larger regime of batch sizes that results in sublinear gains in convergence speed---in this regime, increasing the batch size can improve wall-clock training time at the expense of greater total computational cost;

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stagnation: eventually, we reach a third regime where a higher batch size results in marginal or non-existent reductions in convergence speed.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In our experiments, we find that this third regime begins at a batch size that is too small to fully populate the memory of all GPUs at our disposal, leading to low GPU utilization. *Even though training past this batch size allows for the GPU cycles to be fully utilized, doing so increases the total computational cost without reducing wall-clock training time or improving prediction quality.* While there has been considerable excitement around heuristics that have been shown to make large batch training practical for certain problems, we demonstrate that these techniques still suffer from the same convergence trends we observe, and they often decrease stability of the training process.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent work has observed that the final *test performance* of models trained with large batch sizes degrades after training for a fixed number of epochs. This phenomenon is known as the *generalization gap*. Previous work addressing this problem has focused on training for more iterations in the large batch case or adopting various heuristics to select a learning rate for larger batch sizes. Based on our empirical results, we find that existing techniques to mitigate the generalization gap do not work on some problems, and for other problems they only work for batch sizes that are too small to fully populate the memory of all GPUs at our disposal. Perhaps more importantly, they do little to affect the diminishing returns in rates of convergence for training loss as batch size increases.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our objective is to understand the behavior of SGD and existing large batch techniques for many network architectures and problem domains, e.g., image classification/segmentation and natural language processing (NLP). We observe markedly worse performance for these techniques in domains other than image classification, where large batch optimization has received the most attention. Because we eschew the challenges of an efficient distributed implementation by measuring number of iterations instead of wall-clock time, our results assume the most optimistic circumstances for large batch training.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Increasing the batch size beyond a certain point yields no improvement in wall-clock time to convergence, even for a system with perfect parallelism. We observe that larger batch sizes result in a limited reduction in the number of training iterations needed to achieve low training or test error, and that eventually these gains become near-zero.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Increasing the batch size leads to a significant increase in generalization error, which cannot be mitigated by existing techniques. We observe that these techniques often result in divergent training behavior or that they only mitigate degradation in test performance for small batch sizes relative to available compute.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Dataset size plays a less decisive role in determining training efficiency than factors such as model architecture and data complexity. We observe that both the diminishing returns in convergence speed and the failure of existing methods seem to correlate more with these other problem properties than dataset size alone.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 2, we review the formulation of SGD as well as existing strategies to train with large batch sizes. In Section 3, we review recent theoretical results regarding the convergence rates of SGD in highly over-parameterized settings and discuss the potential impact of these results on the computational efficiency of SGD for deep learning. Section 4 presents our empirical results that demonstrate the inefficiencies of training SGD with large batch sizes, and we show that these persist when using existing large batch optimization techniques.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Critical Batch Sizes and Diminishing Returns", "weight": 1.0} -->

The convergence rate of SGD, denoted by $k_{\epsilon}{(m)}$, is the number of iterations needed to achieve training error less than a fixed constant $\epsilon > 0$ by using SGD with batch size $m$ (we will drop the subscript $\epsilon$ when it is unambiguous). In order to guarantee that large batch sizes speed up training, $k{(m)}$ should continue to decrease near-linearly with $m$. Otherwise, a larger batch size increases computational cost with only limited reductions in wall-clock training time. For near-constant $k{(m)}$, the benefit of large batch sizes becomes near-zero.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Critical Batch Sizes and Diminishing Returns", "weight": 1.0} -->

showed theoretically that in convex, over-parameterized settings, the reduction in convergence time obtained by increasing the batch size decays dramatically to a near-constant level after a critical batch size that is independent of the dataset size. This speedup is measured with respect to the number of SGD iterations required to reach some fixed loss error for some baseline batch size $m_{0}$, and for this purpose we define the speedup ratio ${s{(m;m_{0})}} = {{{k{(m_{0})}}/k}{(m)}}$. The speedup ratio represents the amount of time we save by increasing the batch size to $m$. Beyond the critical batch size mentioned above, even with no communication overhead and unlimited resources (where each batch size requires the same amount of wall-clock time to process) we would prefer to use the critical batch size because it requires less overall computation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Critical Batch Sizes and Diminishing Returns", "weight": 1.0} -->

This result is surprising because researchers have asserted that it should be possible to achieve linear gains in convergence speed so long as the batch size is small relative to dataset size. This will present significant difficulties for future optimization work (large mini-batch training) because it prevents us from using large batch sizes as a catch-all approach to quickly train models as datasets grow larger.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Empirical Evaluation", "weight": 1.0} -->

Recent work studying large batch training has looked primarily at image classification, especially on the ImageNet dataset. We perform large batch size experiments across both traditional image classification (IC) tasks (such as on CIFAR-10/100 ), as well as previously unexplored tasks like image segmentation (IS) using the Cityscapes dataset, and natural language processing (NLP) using the WikiText-2 dataset. We also test how these results vary across other modern DNN architectures, namely ResNets, LSTMs, AlexNet, VGG, Dilated Residual Networks, and MobileNetV2. We tested all of the large batch training techniques described in Section 2. We tried training longer based on the work of, but we found that this necessarily cannot improve the convergence speed and often does not improve final test performance. The two other techniques include the square root scaling rule strategy (SRSR) and the linear scaling rule strategy (LSR). For the latter, we used a warm-up period at the start of training as suggested. Table 1 reports our datasets, models and different training strategies.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Empirical Evaluation", "weight": 1.0} -->

For each model, we evaluated against a base learning rate strategy (BLR) that used the same learning rate across all batch sizes. We selected this learning rate based on its performance on a small baseline batch size.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Diminishing Returns in Rates of Convergence", "weight": 1.0} -->

We demonstrate the rapidly diminishing returns in rates of convergence across various problem domains and network configurations. Researchers increase the batch size in an attempt to achieve nearly linear speedups in convergence compared to a small mini-batch size. In particular, if the speedup is near-linear, i.e. ${s{(m;m_{0})}} = {{{k{(m_{0})}}/k}{(m)}} \approx {m/m_{0}}$, then the computational cost remains nearly constant for large and small mini-batch SGD. However, if ${s{(m)}} \ll {m/m_{0}}$, then the benefit of using large batch size training is negligible.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Diminishing Returns in Rates of Convergence", "weight": 1.0} -->

In Figure 1, we show contour plots of training loss as a function of both the batch size and the number of training iterations of on CIFAR-10, an LSTM on WikiText-2, and DRN-D-22 on Cityscapes. Consider, for example, the contour plot for trained on CIFAR-10. We can see that as the batch size increases from 16 to roughly 2048, in the reasonably well-trained model regime, the number of SGD iterations needed to achieve a particular loss value decreases linearly. Exceeding this regime, however, the speedup ratio becomes increasingly sublinear and soon we have ${s{(m;m_{0})}} \ll {m/m_{0}}$. For batch size roughly 4096, the training procedure does not achieve the lowest training loss. From this perspective, even if we did not care about computational cost or training time, we would not be able to find an accurate model. We observe even worse scaling behavior for test performance (please see Figure 5 for details).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Diminishing Returns in Rates of Convergence", "weight": 1.0} -->

For NLP and IS, note that the gain from large batch training diminishes even faster. Neither the LSTM on WikiText-2 nor DRN-D-22 on Cityscapes can reach their respective baseline performances after reasonably small batch sizes of about $32$ and $64$, respectively. Although showed that training on the Amazon Reviews dataset can be done within 4 hours, they tune hyper-parameters heavily. This poses an issue for many practical deployments because these problems are often already slow to train.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Existing Strategies Break Down for Large Batch Sizes", "weight": 1.0} -->

We further explore how training with the linear and square root scaling rules compares to training with a fixed baseline learning rate (BLR) that does not change with batch size. In the left subfigure of Figure 2, we show the speedup curves of BLR, LSR, and SRSR strategies for on CIFAR-10. Note that LSR and SRSR outperform BLR from batch size 256 to 2048 which implies that LSR and SRSR can help the model train for small-to-medium batch sizes. However, the speedup of LSR and SRSR is still worse than the ideal linear case, and the curves plateau quickly after a batch size of 2048, at which point BLR becomes better than LSR and SRSR. This means that for certain problems, scaling up the learning rate to compensate for an increased batch size hurts performance.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Existing Strategies Break Down for Large Batch Sizes", "weight": 1.0} -->

In the right subfigure of Figure 2, we plot the test performance and the approximation error for LSR of on CIFAR-10. We measure the approximation error at the end of training, with final weights $\mathbf{w}^{\ast}$. We take this error to be the absolute difference between the true loss value $L{(\mathbf{w})}$ and the linear approximation at $\mathbf{w}^{\ast}$, given by ${\hat{L}{(\mathbf{w})}} = {{L{(\mathbf{w}^{\ast})}} + {\langle{\mathbf{g}_{m}{(\mathbf{w}^{\ast})}},{\mathbf{w} - \mathbf{w}^{\ast}}\rangle}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Existing Strategies Break Down for Large Batch Sizes", "weight": 1.0} -->

The approximation is calculated for $\mathbf{w} = {\mathbf{w}^{\ast} - {\eta\frac{m}{m_{0}}\mathbf{g}_{m}{(\mathbf{w}^{\ast})}}}$ to understand the behavior of the approximation along the trajectory for a single SGD iterate using the LSR. It appears that there exists a strong relationship between linear approximation error and test accuracy: as the linear approximation error increases, the test accuracy drops. Note the transition that happens at the critical batch size of 2048. After this point, the test accuracy drops significantly and the linear approximation error exceeds $1$, showing that we quickly exit the regime in which the linear approximation is valid.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Convergence speed has a weak dependence on dataset size", "weight": 1.0} -->

Previous works have conjectured that the maximum batch size that can result in a good model is proportional to the size of the whole dataset. However, for convex, over-parameterized problems, show that there is a model-dependent critical batch size after which we observe rapidly diminishing returns in convergence speed. In this section, to observe if a similar critical batch size exists in the non-convex case, we compare how changing model architecture or data complexity affects the shapes of speedup curves compared to changing the dataset size alone.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Convergence speed has a weak dependence on dataset size", "weight": 1.0} -->

First, in order to show that these diminishing returns depend on data complexity and DNN architecture, we plot speedup curves in Figure 3 to compare the scaling behaviors across different models and dataset configurations. For the error threshold $\epsilon$, we chose the lowest quartile loss value reached by the largest batch size to make a fair comparison across configurations. This setup actually favors the large batch case, because there are lower loss thresholds that are attainable only in the small batch case. On the left, for the CIFAR-10 dataset, we compared four model architectures. For each architecture, we plotted the speedup curve obtained by training this model on the dataset for various batch sizes. The variety of speedup curve shapes indicates that model architecture is an important factor in determining the convergence speed of training for large batch sizes. For MobileNetV2/AlexNet, the diminishing returns become visible when batch size is 1024. However, for /, the speedup does not flatten out until batch size 8196. Hence, in practice, the choice of model strongly affects our ability to use large batch sizes in SGD.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Convergence speed has a weak dependence on dataset size", "weight": 1.0} -->

On the right, in order to investigate the effect of problem complexity, we compared the performance of on four datasets of the same size: CIFAR-10, CIFAR-100, MNIST, and the SVHN dataset (we cut off MNIST and SVHN to $50k$ training examples each). Although all problems display diminishing returns in rates of convergence, the point at which the curves plateau varies according to problem complexity. It is not hard to see that, for simpler problems such as SVHN, the curves flatten out later than for harder problems (e.g. CIFAR-10/100).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Convergence speed has a weak dependence on dataset size", "weight": 1.0} -->

In all of the above cases, the diminishing rates of return in convergence speed become visible after only moderate increases in the batch size. Previous works have only studied convergence behavior for a fairly limited range of batch sizes (e.g., up to $4096$ for CIFAR-10). By increasing the batch size past this point, it becomes immediately apparent that the primary issue with large batch size optimization is training speed, not the generalization gap.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Convergence speed has a weak dependence on dataset size", "weight": 1.0} -->

In order to test whether the sublinear behavior of $s{(m;m_{0})}$ depends primarily on dataset size, we compare the speedup curves obtained when training a single model on different fractions of the original training data. We trained models on the CIFAR-10 and SVHN datasets (for SVHN in this experiment, we train on all $600k$ available training images). For each dataset, we trained on $100\%$, $50\%$, and then $25\%$ of the available training data.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Convergence speed has a weak dependence on dataset size", "weight": 1.0} -->

In Figure 4, we plot the resulting speedup curves for the various partitions. In order to maintain a fair comparison (as baseline loss values change for different dataset sizes), we again choose the loss threshold to be the lower quartile of loss values obtained by the largest batch size.^11^1We observed that the loss threshold for a smaller partition is higher than that of the full dataset. This may be because, as we decrease dataset size, the large batch behavior that determines our threshold approaches that of vanilla gradient descent, which typically displays poor training convergence speed for DNN problems. Notably, the batch size at which the curves begin to plateau remains constant as dataset size changes. For on CIFAR-10, the linear speedup behavior breaks around batch size 128 for all three curves. By a batch size of 1024, all curves have flattened. We can see similar behavior for on SVHN. Overall, looking back to Figure 3, the choice of model and the complexity of the dataset appear to be more related to the shape of speedup curve than dataset size alone.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusion", "weight": 1.5} -->

By experimenting across a wide range of network architectures and problem domains, we find that, after a certain point, increasing the batch size fails to decrease wall-clock time to convergence and results in low computational efficiency, even assuming perfect parallelism. The critical batch size after which these returns diminish tends to be small relative to existing system capabilities. These trends present impediments to progress in developing effective machine learning systems that are capable of handling growing data demands.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Recent works also suggest heuristics to decrease the generalization gap, but we find that these heuristics cannot be used to solve the underlying issue of training convergence speed. Moreover, we find that they usually only help decrease the generalization error in a small-to-medium batch size regime. There does not seem to be a simple training heuristic to improve large batch performance in general.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusion", "weight": 1.5} -->

These results suggest that we should not assume that increasing the batch size for larger datasets will keep training times manageable for all problems. Even though it is a natural form of data parallelism for large-scale optimization, alternative forms of parallelism should be explored to utilize all of our data more efficiently.
