<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Neural Nearest Neighbors Networks

Topics include Neural networks, Convolutional networks, Nearest neighbors, Classification, Rely on k-nearest neighbors, KNN, Convolutional neural network.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Non-local methods exploiting the self-similarity of natural signals have been well studied, for example in image analysis and restoration. Existing approaches, however, rely on k-nearest neighbors (KNN) matching in a fixed feature space. The main hurdle in optimizing this feature space w.r.t. application performance is the non-differentiability of the KNN selection rule. To overcome this, we propose a continuous deterministic relaxation of KNN selection that maintains differentiability w.r.t. pairwise distances, but retains the original KNN as the limit of a temperature parameter approaching zero. To exploit our relaxation, we propose the neural nearest neighbors block (N3 block), a novel non-local processing layer that leverages the principle of self-similarity and can be used as building block in modern neural network architectures. We show its effectiveness for the set reasoning task of correspondence classification as well as for image restoration, including image denoising and single image super-resolution, where we outperform strong convolutional neural network (CNN) baselines and recent non-local models that rely on KNN selection in hand-chosen features spaces.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The ongoing surge of convolutional neural networks (CNNs) has revolutionized many areas of machine learning and its applications by enabling unprecedented predictive accuracy. Most network architectures focus on local processing by combining convolutional layers and element-wise operations. In order to draw upon information from a sufficiently broad context, several strategies, including dilated convolutions or hourglass-shaped architectures, have been explored to increase the receptive field size. Yet, they trade off context size for localization accuracy. Hence, for many dense prediction tasks, *e. g.* in image analysis and restoration, stacking ever more convolutional blocks has remained the prevailing choice to obtain bigger receptive fields.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, traditional algorithms in image restoration increase the receptive field size via non-local processing, leveraging the self-similarity of natural signals. They exploit that image structures tend to re-occur within the same image, giving rise to a strong prior for image restoration. Hence, methods like non-local means or BM3D aggregate information across the whole image to restore a local patch. Here, matching patches are usually selected based on some hand-crafted notion of similarity, *e. g.* the Euclidean distance between patches of input intensities. Incorporating this kind of non-local processing into neural network architectures for image restoration has only very recently been considered. These methods replace the filtering of matched patches with a trainable network, while the feature space on which $k$-nearest neighbors selection is carried out is taken to be fixed. But why should we rely on a predefined matching space in an otherwise end-to-end trainable neural network architecture? In this paper, we demonstrate that we can improve non-local processing considerably by also optimizing the feature space for matching.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main technical challenge is imposed by the non-differentiability of the KNN selection rule. To overcome this, we make three contributions. First, we propose a continuous deterministic relaxation of the KNN rule, which allows differentiating the output *w. r. t.* pairwise distances in the input space, such as between image patches. The strength of the novel relaxation can be controlled by a temperature parameter whose gradients can be obtained as well. Second, from our relaxation we develop a novel neural network layer, called *neural nearest neighbors block* ($\text{N}^{3}$ block), which enables end-to-end trainable non-local processing based on the principle of self-similarity. Third, we demonstrate that the accuracy of image denoising and single image super-resolution (SISR) can be improved significantly by augmenting strong local CNN architectures with our novel $\text{N}^{3}$ block, also outperforming strong non-local baselines.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, for the task of correspondence classification, we obtain significant improvements by simply augmenting a recent neural network baseline with our $\text{N}^{3}$ block, showing its effectiveness on set-valued data.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Differentiable *k*-Nearest Neighbors", "weight": 1.0} -->

We first detail our continuous and differentiable relaxation of the $k$-nearest neighbors (KNN) selection rule. Here, we will make few assumptions on the data to derive a very general result that can be used with many kinds of data, including text or sets. In the next section, we will then define a non-local neural network layer based on our relaxation. Let us start by precisely defining KNN selection. Assume that we are given a query item $q$, a database of candidate items ${(x_{i})}_{i \in I}$ with indices $I = {\{ 1,\ldots,M\}}$ for matching, and a distance metric $d{( \cdot, \cdot )}$ between pairs of items. Assuming that $q$ is not in the database, $d$ yields a ranking of the database items according to the distance to the query.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Differentiable *k*-Nearest Neighbors", "weight": 1.0} -->

The KNN of $q$ are then given by the set of the first $k$ items *w. r. t.* the permutation $\pi_{q}$

<!-- chunk {"id": "body-0009", "role": "body", "section": "Differentiable *k*-Nearest Neighbors", "weight": 1.0} -->

The KNN selection rule is deterministic but not differentiable. This effectively hinders to derive gradients *w. r. t.* the distances $d{( \cdot, \cdot )}$. We will alleviate this problem in two steps. First, we interpret the deterministic KNN rule as a limit of a parametric family of discrete stochastic sampling processes. Second, we derive continuous relaxations for the discrete variables, thus allowing to backpropagate gradients through the neighborhood selection while still preserving the KNN rule as a limit case.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Differentiable *k*-Nearest Neighbors", "weight": 1.0} -->

KNN rule as limit distribution. We proceed by interpreting the KNN selection rule as the limit distribution of $k$ categorical distributions that are constructed as follows. As in Neighborhood Component Analysis, let $\text{Cat}{(\left. w^{1} \middle| {\alpha^{1},t} \right.)}$ be a categorical distribution over the indices $I$ of the database items, obtained by deriving logits $\alpha_{i}^{1}$ from the negative distances to the query item $d{(q,x_{i})}$, scaled with a temperature parameter $t$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Differentiable *k*-Nearest Neighbors", "weight": 1.0} -->

Here, we treat $w^{1}$ as a one-hot coded vector and denote with $w^{1} = i$ that the $i$-th entry is set to one while the others are zero. In the limit of $t\rightarrow 0$, $\text{Cat}{(\left. w^{1} \middle| {\alpha^{1},t} \right.)}$ will converge to a deterministic ("Dirac delta") distribution centered at the index of the database item with smallest distance to $q$. Thus we can regard sampling from $\text{Cat}{(\left. w^{1} \middle| {\alpha^{1},t} \right.)}$ as a stochastic relaxation of 1-NN. We now generalize this to arbitrary $k$ by proposing an iterative scheme to construct further conditional distributions $\text{Cat}{(\left. w^{j + 1} \middle| {\alpha^{j + 1},t} \right.)}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Differentiable *k*-Nearest Neighbors", "weight": 1.0} -->

From the index vectors $w^{j}$, we can define the *stochastic nearest neighbors* $\{ X^{1},\ldots,X^{k}\}$ of $q$ using

<!-- chunk {"id": "body-0013", "role": "body", "section": "Differentiable *k*-Nearest Neighbors", "weight": 1.0} -->

When the temperature parameter $t$ approaches zero, the distribution over the $\{ X^{1},\ldots,X^{k}\}$ will be a deterministic distribution centered on the $k$ nearest neighbors of $q$. Using these stochastic nearest neighbors directly within a deep neural network is problematic, since gradient estimators for expectations over discrete variables are known to suffer from high variance. Hence, in the following we consider a continuous deterministic relaxation of the discrete random variables.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Differentiable *k*-Nearest Neighbors", "weight": 1.0} -->

Continuous deterministic relaxation. Our basic idea is to replace the one-hot coded weight vectors with their continuous expectations. This will yield a deterministic and continuous relaxation of the stochastic nearest neighbors that still converges to the hard KNN selection rule in the limit case of $t\rightarrow 0$. Concretely, the expectation ${\overline{w}}^{1}$ of the first index vector $w^{1}$ is given by

<!-- chunk {"id": "body-0015", "role": "body", "section": "Differentiable *k*-Nearest Neighbors", "weight": 1.0} -->

We can now relax the update of the logits (Eq. 5) by using the expected weight vector instead of the discrete sample as

<!-- chunk {"id": "body-0016", "role": "body", "section": "Differentiable *k*-Nearest Neighbors", "weight": 1.0} -->

In the limit of $t\rightarrow 0$, the expectation ${\overline{w}}^{1}$ of the first sampled index vector will approach a one-hot encoding of the index of the closest neighbor. As a consequence, the logit update in Eq. 9 will also converge to the hard update from Eq. 5. By induction it follows that the other ${\overline{w}}^{j}$ will converge to a one-hot encoding of the closest indices of the $j$-th nearest neighbor. In summary, this means that our continuous deterministic relaxation still contains the hard KNN selection rule as a limit case.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Differentiable *k*-Nearest Neighbors", "weight": 1.0} -->

Discussion. Figure 1 shows the relation between the deterministic KNN selection, stochastic nearest neighbors, and our proposed continuous nearest neighbors. Note that the continuous nearest neighbors are differentiable *w. r. t.* the pairwise distances as well as the temperature $t$. This allows making the temperature a trainable parameter. Moreover, the temperature can depend on the query item $q$, thus allowing to learn for which query items it is beneficial to average more uniformly across the database items, *i. e.* by choosing a high temperature, and for which query items the continuous nearest neighbors should be close to the discrete nearest neighbors, *i. e.* by choosing a low temperature. Both cases have their justification. A more uniform averaging effectively allows to aggregate information from many neighbors at once. On the other hand, the more distinct neighbors obtained with a low temperature allow to first non-linearly process the information before eventually fusing it.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Differentiable *k*-Nearest Neighbors", "weight": 1.0} -->

From Eq. 11 it becomes apparent that the continuous nearest neighbors effectively take $k$ weighted averages over the database items. Thus, prior work such as non-local networks, differentiable relaxations of the KNN classifier, or soft attention-based architectures can be realized as a special case of our architecture with $k = 1$. We also experimented with a continuous relaxation of the stochastic nearest neighbors based on approximating the discrete distributions with Concrete distributions. This results in a stochastic sampling of weighted averages as opposed to our deterministic nearest neighbors. For the dense prediction tasks considered in our experiments, we found the deterministic variant to give significantly better results, see Sec. 5.1.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Neural Nearest Neighbors Block", "weight": 1.0} -->

In the previous section we made no assumptions about the source of query and database items. Here, we propose a new network block, called *neural nearest neighbors block* ($\text{N}^{3}$ block, Fig. 2(a)), which integrates our continuous and differentiable nearest neighbors selection into feed-forward neural networks based on the concept of *self-similarity*, *i. e.* query set and database are derived from the same features (*e. g.*, feature patches of an intermediate layer within a CNN). An $\text{N}^{3}$ block consists of two important parts. First, an embedding network takes the input and produces a feature embedding as well as temperature parameters. These are used in a second step to compute continuous nearest neighbors feature volumes that are aggregated with the input. We interleave $\text{N}^{3}$ blocks with existing local processing networks to form neural nearest neighbors networks ($\text{N}^{3}$Net) as shown in Fig. 2(b).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Neural Nearest Neighbors Block", "weight": 1.0} -->

In the following, we take a closer look at the components of an $\text{N}^{3}$ block and their design choices.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Neural Nearest Neighbors Block", "weight": 1.0} -->

Embedding network. A first branch of the embedding network calculates a feature embedding $E = {f_{\text{E}}{(Y)}}$. For image data, we use CNNs to parameterize $f_{\text{E}}$; for set input we use multi-layer perceptrons. The pairwise distance matrix $D$ can now be obtained by $D_{ij} = {d{(E_{i},E_{j})}}$, where $E_{i}$ denotes the embedding of the $i$-th item and $d$ is a differentiable distance function. We found that the Euclidean distance works well for the tasks that we consider. In practice, for each query item, we confine the set of potential neighbors to a subset of all items, *e. g.* all image patches in a certain local region. This allows our $\text{N}^{3}$ block to scale linearly in the number of items instead of quadratically.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Neural Nearest Neighbors Block", "weight": 1.0} -->

Another network branch computes a tensor $T = {f_{\text{T}}{(Y)}}$ containing the temperature $t$ for each item. Note that $f_{\text{E}}$ and $f_{\text{T}}$ can potentially share weights to some degree. We opted for treating them as separate networks as this allows for an easier implementation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Neural Nearest Neighbors Block", "weight": 1.0} -->

Continuous nearest neighbors selection. From the distance matrix $D$ and the temperature tensor $T$, we compute $k$ continuous nearest neighbors feature volumes $N_{1},\ldots,N_{k}$ from the input features $Y$ by applying Eqs. 8, 9, 10 and 11 to each item. Since $Y$ and each $N_{i}$ have equal dimensionality, we could use any element-wise operation to aggregate the original features $Y$ and the neighbors. However, a reduction at this stage would mean a very early fusion of features. Hence, we instead simply concatenate $Y$ and the $N_{i}$ along the feature dimension, which allows further network layers to learn how to fuse the information effectively in a non-linear way.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Neural Nearest Neighbors Block", "weight": 1.0} -->

$\text{N}^{3}$ block for image data. The $\text{N}^{3}$ block described above is very generic and not limited to a certain input domain. We now describe minor technical modifications when applying the $\text{N}^{3}$ block to image data. Traditionally, non-local methods in image processing have been applied at the patch-level, *i. e.* the items to be matched consist of image patches instead of pixels. This has the advantage of using a broader local context for matching and aggregation. We follow this reasoning and first apply a strided im2col operation on $E$ before calculating pairwise distances. The temperature parameter for each patch is obtained by taking the corresponding center pixel in $T$. Each nearest neighbor volume $N_{i}$ is converted from the patch domain to the image domain by applying a col2im operation, where we average contributions of different patches to the same pixel.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experiments", "weight": 1.0} -->

We now analyze the properties of our novel $\text{N}^{3}$Net and show its benefits over state-of-the-art baselines. We use image denoising as our main test bed as non-local methods have been well studied there. Moreover, we evaluate on single image super-resolution and correspondence classification.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our baseline architecture is the DnCNN model of Zhang *et al.*, consisting of $16$ blocks, each with a sequence of a $3 \times 3$ convolutional layer with $64$ feature maps, batch normalization, and a ReLU activation function. In the end, a final $3 \times 3$ convolution is applied, the output of which is added back to the input through a global skip connection.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

We use the DnCNN architecture to create our $\text{N}^{3}$Net for image denoising. Specifically, we use three DnCNNs with six blocks each, *cf.* Fig. 2(b). The first two blocks output $8$ feature maps, which are fed into a subsequent $\text{N}^{3}$ block that computes $7$ neighbor volumes. The concatenated output again has a depth of $64$ feature channels, matching the depth of the other intermediate blocks. The $\text{N}^{3}$ blocks extract $10 \times 10$ patches with a stride of $5$. Patches are matched to other patches in a $80 \times 80$ region, yielding a total of $224$ candidate patches for matching each query patch. More details on the architecture can be found in the supplemental material.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments", "weight": 1.0} -->

Training details. We follow the protocol of Zhang *et al.* and use the 400 images in the train and test split of the BSD500 dataset for training. Note that these images are strictly separate from the validation images. For each epoch, we randomly crop $512$ patches of size $80 \times 80$ from each training image. We use horizontal and vertical flipping as well as random rotations $\in {\{{0{^\circ}},{90{^\circ}},{180{^\circ}},{270{^\circ}}\}}$ as further data augmentation. In total, we train for $50$ epochs with a batch size of $32$, using the Adam optimizer with default parameters ${\beta_{1} = 0.9},{\beta_{2} = 0.999}$ to minimize the squared error. The learning rate is initially set to $10^{- 3}$ and exponentially decreased to $10^{- 8}$ over the course of training.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

Following the publicly available implementation of DnCNN, we apply a weight decay with strength $10^{- 4}$ to the weights of the convolution layers and the scaling of batch normalization layers.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate our full model on three different datasets: *(i)* a set of twelve commonly used benchmark images, *(ii)* the 68 images subset of the BSD500 validation set, and *(iii)* the Urban100 dataset, which contains images of urban scenes where repetitive patterns are abundant.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Ablation study", "weight": 1.0} -->

We begin by discerning the effectiveness of the individual components. We compare our full $\text{N}^{3}$Net against several baselines: *(i,ii)* The baseline DnCNN network with depths $17$ (default) and $18$ (matching the depth of $\text{N}^{3}$Net). *(iii)* A baseline where we replace the $\text{N}^{3}$ blocks with KNN selection ($k = 7$) to obtain neighbors for each patch. Distance calculation is done on the noisy input patches. *(iv)* The same baseline as *(iii)* but where distances are calculated on denoised patches. Here we use the pretrained $17$-layer DnCNN as strong denoiser. The task specific hand-chosen distance embedding for this baseline should intuitively yield more sensible nearest neighbors matches than when matching noisy input patches. *(v)* A baseline where we use Concrete distributions to approximately reparameterize the stochastic nearest neighbors sampling. The resulting Concrete block has an additional network for estimating the annealing parameter of the Concrete distribution.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Ablation study", "weight": 1.0} -->

Table 1 shows the results on the Urban100 test set ($\sigma = 25$) from which we can infer four insights: First, the KNN baselines *(iii)* and *(iv)* improve upon the plain DnCNN model, showing that allowing the network to access non-local information is beneficial. Second, matching denoised patches (baseline *(iv)*) does not improve significantly over matching noisy patches (baseline *(iii)*). Third, *learning* a patch embedding with our novel $\text{N}^{3}$ block shows a clear improvement over all baselines. We, moreover, evaluate a smaller version of $\text{N}^{3}$Net with only two DnCNN blocks of depth $6$ (*ours light*). This model already outperforms the baseline DnCNN with depth $17$ despite having *fewer layers* ($12$ *vs.* $17$) and *fewer parameters* ($427$k *vs.* $556$k).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Ablation study", "weight": 1.0} -->

Fourth, reparameterization with Concrete distributions (baseline *(v)*) performs worse than our continuous nearest neighbors. This is probably due to the Concrete distribution introducing stochasticity into the forward pass, leading to a less stable training. Additional ablations are given in the the supplemental material.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Ablation study", "weight": 1.0} -->

Next, we compare $\text{N}^{3}$Nets with a varying number of selected neighbors. Table 2 shows the results on Urban100 with $\sigma \in {\{ 25,50\}}$. We can observe that, as expected, more neighbors improve denoising results. However, the effect diminishes after roughly four neighbors and accuracy starts to deteriorate again. As we refrain from selecting optimal hyper-parameters on the test set, we will stick to the architecture with $k = 7$ for the remaining experiments on image denoising and SISR.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Comparison to the state of the art", "weight": 1.0} -->

We compare our full $\text{N}^{3}$Net against state-of-the-art local denoising methods, *i. e.* the DnCNN baseline, the very deep and wide ($30$ layers, $128$ feature channels) model, and the recent FFDNet. Moreover, we compare against competing non-local denoisers. These include the classical BM3D, which uses a hand-crafted denoising pipeline, and the state-of-the-art trainable non-local models NLNet and UNLNet, both learning to process non-locally aggregated patches. We also compare against NN3D, which applies a non-local step on top of a pretrained network. For fair comparison, we apply a single denoising step for NN3D using our 17-layer baseline DnCNN. As a crucial difference to our proposed $\text{N}^{3}$Net, all of the compared non-local methods use KNN selection on a fixed feature space, thus not being able to learn an embedding for matching.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Comparison to the state of the art", "weight": 1.0} -->

Table 3 shows the results for three different noise levels. We make three important observations: First, our $\text{N}^{3}$Net significantly outperforms the baseline DnCNN network on all tested noise levels and all datasets. Especially for higher noise levels the margin is dramatic, *e. g.* $+ {0.54\text{dB~}{({\sigma = 50})}}$ or $+ {0.79\text{dB~}{({\sigma = 70})}}$ on Urban100. Even the deeper and wider model does not reach the accuracy of $\text{N}^{3}$Net. Second, our method is the only trainable non-local model that is able to outperform the local models DnCNN and FFDNet. The competing models NLNet and UNLNet do not reach the accuracy of DnCNN even on Urban100, whereas our $\text{N}^{3}$Net even fares better than the strongest local denoiser FFDNet.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Comparison to the state of the art", "weight": 1.0} -->

Third, the post-hoc non-local step applied by NN3D is very effective on Urban100 where self-similarity can intuitively shine. However, on the gains are noticeably smaller whilst on the non-local step can even result in degraded accuracy, *e. g.* NN3D achieves $- {0.04\text{dB}}$ compared to DnCNN while $\text{N}^{3}$Net achieves $+ {0.16\text{dB}}$ for $\sigma = 50$. This highlights the importance of integrating non-local processing into an end-to-end trainable pipeline. Figure 3 shows denoising results for an image from the Urban100 dataset. BM3D and UNLNet can exploit the recurrence of image structures to produce good results albeit introducing artifacts in the windows. DnCNN and FFDNet yield even more artifacts due to the limited receptive field and NN3D, as a post-processing method, cannot recover from the errors of DnCNN. In contrast, our $\text{N}^{3}$Net produces a significantly cleaner image where most of the facade structure is correctly restored.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Real image denoising", "weight": 1.0} -->

To further demonstrate the merits of our approach, we applied the same $\text{N}^{3}$Net architecture as before to the task of denoising real-world images with realistic noise. To this end, we evaluate on the recent Darmstadt Noise Dataset, consisting of $50$ noisy images shot with four different cameras at varying ISO levels. Realistic noise can be well explained by a Poisson-Gaussian distribution which, in turn, can be well approximated by a Gaussian distribution where the variance depends on the image intensity via a linear noise level function. We use this heteroscedastic Gaussian distribution to generate synthetic noise for training. Specifically, we use a broad range of noise level functions covering those that occur on the test images. For training, we use the $400$ images of the BSDS training and test splits, $800$ images of the DIV2K training set, and a training split of $3793$ images from the Waterloo database.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Real image denoising", "weight": 1.0} -->

where $Y{( \cdot )}$ computes luminance values from RGB, the exponentiation with $f_{e}$ aims at undoing compression of high image intensities, and scaling with $f_{c}$ aims at undoing the effect of white balancing. Further training details can be found in the supplemental material.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Real image denoising", "weight": 1.0} -->

We train both the DnCNN baseline as well as our $\text{N}^{3}$Net with the same training protocol and evaluate them on the benchmark website. Results are shown in Table 4. $\text{N}^{3}$Net sets a new state of the art for denoising raw images, outperforming DnCNN and BM3D by a significant margin. Moreover, the PSNR values, when evaluated on developed sRGB images, surpass those of the currently top performing methods in sRGB denoising, TWSC and CBDNet.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Single image super-resolution", "weight": 1.0} -->

We now show that we can also augment recent strong CNN models for SISR with our $\text{N}^{3}$ block. We particularly consider the common task of upsampling a low-resolution image that was obtained from a high-resolution image by bicubic downscaling. We chose the VDSR model as our baseline architecture, since it is conceptually very close to the DnCNN model for image denoising. The only notable difference is that it has $20$ layers instead of $17$. We derive our $\text{N}^{3}$Net for SISR from the VDSR model by stacking three VDSR networks with depth $7$ and inserting two $\text{N}^{3}$ blocks ($k = 7$) after the first two VDSR networks, *cf.* Fig. 2(b). Following, the input to our network is the bicubicly upsampled low-resolution image and we train a single model for super-resolving images with factors $2$, $3$, and $4$. Further details on the architecture and training protocol can be found in the supplemental material.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Single image super-resolution", "weight": 1.0} -->

Note that we refrain from building our $\text{N}^{3}$Net for SISR from more recent networks, *e. g.* MemNet, MDSR, or WDnCNN, since they are too costly to train.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Single image super-resolution", "weight": 1.0} -->

We compare our $\text{N}^{3}$Net against VDSR and MemNet as well as two non-local models: SelfEx and the recent WSD-SR. Table 5 shows results on Set5. Again, we can observe a consistent gain of $\text{N}^{3}$Net compared to the strong baseline VDSR for all super-resolution factors, *e. g.* $+ {0.15\text{dB}}$ for $\times 4$ super-resolution. More importantly, the other non-local methods perform inferior compared to our $\text{N}^{3}$Net (*e. g.* $+ {0.36\text{dB}}$ compared to WSD-SR for $\times 2$ super-resolution), showing that learning the matching feature space is superior to relying on a hand-defined feature space. Further quantitative and visual results demonstrating the same benefits of $\text{N}^{3}$Net can be found in the supplemental material.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Correspondence classification", "weight": 1.0} -->

As a third application, we look at classifying correspondences between image features from two images as either correct or incorrect. Again, we augment a baseline network with our non-local block. Specifically, we build upon the context normalization network, which we call CNNet in the following. The input to this network is a *set of pairs of image coordinates* of putative correspondences and the output is a probability for each of the correspondences to be correct. CNNet consists of $12$ blocks, each comprised of a local fully connected layer with $128$ feature channels that processes each point individually, and a context normalization and batch normalization layer that pool information across the whole point set. We augment CNNet by introducing a $\text{N}^{3}$ block after the sixth original block. As opposed to the $\text{N}^{3}$ block for the previous two tasks, where neighbors are searched only in the vicinity of a query patch, here we search for nearest neighbors among all correspondences. We want to emphasize that this is a pure *set reasoning task*. Image features are used only to determine putative correspondences while the network itself is agnostic of any image content.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Correspondence classification", "weight": 1.0} -->

For training we use the publicly available code of. We consider two settings: First, we train on the training set of the outdoor sequence *St. Peter* and evaluate on the test set of *St. Peter* and another outdoor sequence called *Reichstag* to test generalization. Second, we train and test on the respective sets of the indoor sequence *Brown*. Table 6 shows the resulting mean average precision (MAP) values at different error thresholds (for details on this metric, see ). We compare our $\text{N}^{3}$Net to the original CNNet and a baseline that just uses all putative correspondences for pose estimation. As can be seen, by simply inserting our $\text{N}^{3}$ block we achieve a consistent and significant gain in all considered settings, increasing MAP scores by $10\%$ to $30\%$. This suggests that our $\text{N}^{3}$ block can enhance local processing networks in a wide range of applications and data domains.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Non-local methods have been well studied, *e. g.*, in image restoration. Existing approaches, however, apply KNN selection on a hand-defined feature space, which may be suboptimal for the task at hand. To overcome this limitation, we introduced the first continuous relaxation of the KNN selection rule that maintains differentiability *w. r. t.* the pairwise distances used for neighbor selection. We integrated continuous nearest neighbors selection into a novel network block, called $\text{N}^{3}$ block, which can be used as a general building block in neural networks. We exemplified its benefit in the context of image denoising, SISR, and correspondence classification, where we outperform state-of-the-art CNN-based methods and non-local approaches. We expect the $\text{N}^{3}$ block to also benefit end-to-end trainable architectures for other input domains, such as text or other sequence-valued data.
