<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PWC-Net: CNNs for Optical Flow Using Pyramid, Warping, and Cost Volume

Topics include Optical flow, PWC-Net, Convolutional networks, Feature pyramid, Warping, Cost volume, Real-time inference.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

PWC-Net distills classical optical-flow structure into a compact learned architecture: feature pyramids for scale, warping for incremental alignment, and cost volumes for matching. It became a strong baseline because it was much smaller and easier to train than FlowNet2 while improving accuracy and speed.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a compact but effective CNN model for optical flow, called PWC-Net. PWC-Net has been designed according to simple and well-established principles: pyramidal processing, warping, and the use of a cost volume. Cast in a learnable feature pyramid, PWC-Net uses the current optical flow estimate to warp the CNN features of the second image. It then uses the warped features and features of the first image to construct a cost volume, which is processed by a CNN to estimate the optical flow. PWC-Net is 17 times smaller in size and easier to train than the recent FlowNet2 model. Moreover, it outperforms all published optical flow methods on the MPI Sintel final pass and KITTI 2015 benchmarks, running at about 35 fps on Sintel resolution (1024x436) images. Our models are available on

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optical flow estimation is a core computer vision problem and has many applications, e.g., action recognition, autonomous driving, and video editing. Decades of research efforts have led to impressive performances on challenging benchmarks. Most top-performing methods adopt the energy minimization approach introduced by Horn and Schunck. However, optimizing a complex energy function is usually computationally expensive for real-time applications.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

One promising approach is to adopt the fast, scalable, and end-to-end trainable convolutional neural network (CNN) framework, which has largely advanced the field of computer vision in recent years. Inspired by the successes of deep learning in high-level vision tasks, Dosovitskiy et al. propose two CNN models for optical flow, i.e., FlowNetS and FlowNetC, and introduce a paradigm shift. Their work shows the feasibility of directly estimating optical flow from raw images using a generic U-Net CNN architecture. Although their performances are below the state of the art, FlowNetS and FlowNetC models are the best among their contemporary real-time methods.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, Ilg et al. stack several FlowNetC and FlowNetS networks into a large model, called FlowNet2, which performs on par with state-of-the-art methods but runs much faster (Fig. 1). However, large models are more prone to the over-fitting problem, and as a result, the subnetworks of FlowNet2 have to be trained sequentially. Furthermore, FlowNet2 requires a memory footprint of 640MB and is not well-suited for mobile and embedded devices.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

SpyNet addresses the model size issue by combining deep learning with two classical optical flow estimation principles. SpyNet uses a spatial pyramid network and warps the second image toward the first one using the initial flow. The motion between the first and warped images is usually small. Thus SpyNet only needs a small network to estimate the motion from these two images. SpyNet performs on par with FlowNetC but below FlowNetS and FlowNet2 (Fig. 1). The results by FlowNet2 and SpyNet show a clear trade-off between accuracy and model size.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Is it possible to both increase the accuracy and reduce the size of a CNN model for optical flow? In principle, the trade-off between model size and accuracy imposes a fundamental limit for general machine learning algorithms. However, we find that combining domain knowledge with deep learning can achieve both goals simultaneously.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

SpyNet shows the potential of combining classical principles with CNNs. However, we argue that its performance gap with FlowNetS and FlowNet2 is due to the partial use of the classical principles. First, traditional optical flow methods often pre-process the raw images to extract features that are invariant to shadows or lighting changes. Fur- ther, in the special case of stereo matching, a cost volume is a more discriminative representation of the disparity (1D flow) than raw images or features. While constructing a full cost volume is computationally prohibitive for real-time optical flow estimation, this work constructs a 'partial' cost volume by limiting the search range at each pyramid level. We can link different pyramid levels using a warping layer to estimate large displacement flow.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our network, called PWC-Net, has been designed to make full use of these simple and well-established principles. It makes significant improvements in model size and accuracy over existing CNN models for optical flow (Figs. 1 and 2). At the time of writing, PWC-Net outperforms all published flow methods on the MPI Sintel final pass and KITTI 2015 benchmarks. Furthermore, PWC-Net is about 17 times smaller in size and provides 2 times faster inferencing than FlowNet2. It is also easier to train than SpyNet and FlowNet2 and runs at about 35 frames per second (fps) on Sintel resolution ( 1024 × 436 ) images.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Previous Work", "weight": 1.0} -->

Variational approach. Horn and Schunck pioneer the variational approach to optical flow by coupling the brightness constancy and spatial smoothness assumptions using an energy function. Black and Anandan introduce a robust framework to deal with outliers, i.e., brightness inconstancy and spatial discontinuities. As it is computationally impractical to perform a full search, a coarse-tofine, warping-based approach is often adopted. Brox et al. theoretically justify the warping-based estimation process. Sun et al. review the models, optimization, and implementation details for methods derived from Horn and Schunck and propose a non-local term to recover motion details. The coarse-to-fine, variational approach is the most popular framework for optical flow. However, it requires solving complex optimization problems and is computationally expensive for real-time applications.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Previous Work", "weight": 1.0} -->

One conundrum for the coarse-to-fine approach is small and fast moving objects that disappear at coarse levels. To address this issue, Brox and Malik embed feature matching into the variational framework, which is further improved by follow-up methods. In particular, the EpicFlow method can effectively interpolate sparse matches to dense optical flow and is widely used as a postprocessing method. Zweig and Wolf use CNNs for sparse-to-dense interpolation and obtain consistent improvement over EpicFlow.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Previous Work", "weight": 1.0} -->

Most top-performing methods use CNNs as a component in their system. For example, DCFlow, the best published method on MPI Sintel final pass so far, learns CNN features to construct a full cost volume and uses sophisticated post-processing techniques, including EpicFlow, to estimate the optical flow. The next-best method, FlowFieldsCNN, learns CNN features for sparse matching and densifies the matches by EpicFlow. The third-best method, MRFlow uses a CNN to classify a scene into rigid and non-rigid regions and estimates the geometry and camera motion for rigid regions using a plane + parallax formulation. However, none of them are real-time or end-to-end trainable.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Previous Work", "weight": 1.0} -->

Early work on learning optical flow. Simoncelli and Adelson study the data matching errors for optical flow. Freeman et al. learn parameters of an MRF model for image motion using synthetic blob world examples. Roth and Black study the spatial statistics of optical flow using sequences generated from depth maps. Sun et al. learn a full model for optical flow, but the learning has been limited to a few training sequences. Li and Huttenlocker use stochastic optimization to tune the parameters for the Black and Anandan method, but the number of parameters learned is limited. Wulff and Black learn PCA motion basis of optical flow estimated by GPUFlow on real movies. Their method is fast but produces over-smoothed flow.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Previous Work", "weight": 1.0} -->

Recent work on learning optical flow. Inspired by the success of CNNs on high-level vision tasks, Dosovitskiy et al. construct two CNN networks, FlowNetS and FlowNetC, for estimating optical flow based on the U-Net denoising autoencoder. The networks are pre-trained on a large synthetic FlyingChairs dataset but can surprisingly capture the motion of fast moving objects on the Sintel dataset. The raw output of the network, however, contains large errors in smooth background regions and requires variational refinement. Mayer et al. apply the FlowNet architecture to disparity and scene flow esti- mation. Ilg et al. stack several basic FlowNet models into a large one, i.e., FlowNet2, which performs on par with state of the art on the Sintel benchmark. Ranjan and Black develop a compact spatial pyramid network, called SpyNet. SpyNet achieves similar performance as the FlowNetC model on the Sintel benchmark, which is good but not state-of-the-art.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Previous Work", "weight": 1.0} -->

Another interesting line of research takes the unsupervised learning approach. Memisevic and Hinton propose the gated restricted Boltzmann machine to learn image transformations in an unsupervised way. Long et al. learn CNN models for optical flow by interpolating frames. Yu et al. train models to minimize a loss term that combines a data constancy term with a spatial smoothness term. While inferior to supervised approaches on datasets with labeled training data, existing unsupervised methods can be used to (pre-)train CNN models on unlabeled data.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Previous Work", "weight": 1.0} -->

Cost volume. A cost volume stores the data matching costs for associating a pixel with its corresponding pixels at the next frame. Its computation and processing are standard components for stereo matching, a special case of optical flow. Recent methods investigate cost volume processing for optical flow. All build the full cost volume at a single scale, which is both computationally expensive and memory intensive. By contrast, our work shows that constructing a partial cost volume at multiple pyramid levels leads to both effective and efficient models.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Previous Work", "weight": 1.0} -->

Datasets. Unlike many other vision tasks, it is extremely difficult to obtain ground truth optical flow on real-world sequences. Early work on optical flow mainly relies on synthetic datasets, e.g., the famous 'Yosemite'. Methods may over-fit to the synthetic data and do not perform well on real data. Baker et al. capture real sequences under both ambient and UV lights in a controlled lab environment to obtain ground truth, but the approach does not work for outdoor scenes. Liu et al. use human annotations to obtain ground truth motion for natural video sequences, but the labeling process is time-consuming.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Previous Work", "weight": 1.0} -->

KITTI and Sintel are currently the most challenging and widely-used benchmarks for optical flow. The KITTI benchmark is targeted for autonomous driving applications and its semi-dense ground truth is collected using LIDAR. The 2012 set only consists of static scenes. The 2015 set is extended to dynamic scenes via human annotations and more challenging to existing methods because of the large motion, severe illumination changes, and occlusions. The Sintel benchmark is created using the open source graphics movie 'Sintel' with two passes, clean and final. The final pass contains strong atmospheric effects, motion blur, and camera noise, which cause severe problems to existing methods. All published, topperforming methods rely heavily on traditional techniques. By embedding the classical principles into the network architecture, we show that a fully end-to-end method can outperform all published methods on both the KITTI 2015 and Sintel final pass benchmarks.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Previous Work", "weight": 1.0} -->

CNN models for dense prediction tasks in vision. The denoising autoencoder has been commonly used for dense prediction tasks in computer vision, especially with skip connections between the encoder and decoder. Recent work shows that dilated convolution layers can better exploit contextual information and refine details for semantic segmentation. Here we use dilated convolutions to integrate contextual information for optical flow and obtain moderate performance improvement. The DenseNet architecture directly connects each layer to every other layer in a feedforward fashion and has been shown to be more accurate and easier to train than traditional CNN layers in image classification tasks. We test this idea for dense optical flow prediction.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Approach", "weight": 1.0} -->

Next, we will explain the main ideas for each component, including pyramid feature extractor, optical flow estimator, and context networks. Please refer to the supplementary material for details of the networks.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Approach", "weight": 1.0} -->

Feature pyramid extractor. Given two input images I 1 and I 2, we generate L -level pyramids of feature representations, with the bottom (zeroth) level being the input images, i.e., c 0 t = I t. To generate feature representation at the l th layer, c l t, we use layers of convolutional filters to downsample the features at the l -1 th pyramid level, c l -1 t, by a factor of 2. From the first to the sixth levels, the number of feature channels are respectively 16, 32, 64, 96, 128, and 196.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Approach", "weight": 1.0} -->

Warping layer. At the l th level, we warp features of the second image toward the first image using the × 2 upsampled flow from the l +1 th level: where x is the pixel index and the upsampled flow up 2 (w l +1) is set to be zero at the top level. We use bilinear interpolation to implement the warping operation and compute the gradients to the input CNN features and flow for backpropagation according to. For nontranslational motion, warping can compensate for some geometric distortions and put image patches at the right scale.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Approach", "weight": 1.0} -->

Cost volume layer. Next, we use the features to construct a cost volume that stores the matching costs for associating a pixel with its corresponding pixels at the next frame. We define the matching cost as the correlation between features of the first image and warped features of the second image: where T is the transpose operator and N is the length of the column vector c l 1 (x 1). For an L -level pyramid setting, we only need to compute a partial cost volume with a limited range of d pixels, i.e., | x 1 -x 2 | ∞ ≤ d. Aone-pixel motion at the top level corresponds to 2 L -1 pixels at the full resolution images. Thus we can set d to be small. The dimension of the 3D cost volume is d 2 × H l × W l, where H l and W l denote the height and width of the l th pyramid level, respectively.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Approach", "weight": 1.0} -->

Optical flow estimator. It is a multi-layer CNN. Its input are the cost volume, features of the first image, and upsampled optical flow and its output is the flow w l at the l th level. The numbers of feature channels at each convolutional layers are respectively 128, 128, 96, 64, and 32, which are kept fixed at all pyramid levels. The estimators at different levels have their own parameters instead of sharing the same parameters. This estimation process is repeated until the desired level, l 0.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Approach", "weight": 1.0} -->

The estimator architecture can be enhanced with DenseNet connections. The inputs to every convolutional layer are the output of and the input to its previous layer. DenseNet has more direct connections than traditional layers and leads to significant improvement in image classification. We test this idea for dense flow prediction.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Approach", "weight": 1.0} -->

Context network. Traditional flow methods often use contextual information to post-process the flow. Thus we employ a sub-network, called the context network, to effectively enlarge the receptive field size of each output unit at the desired pyramid level. It takes the estimated flow and features of the second last layer from the optical flow estimator and outputs a refined flow.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Approach", "weight": 1.0} -->

The context network is a feed-forward CNN and its design is based on dilated convolutions. It consists of 7 convolutional layers. The spatial kernel for each convolutional layer is 3 × 3. These layers have different dilation constants. A convolutional layer with a dilation constant k means that an input unit to a filter in the layer are k -unit apart from the other input units to the filter in the layer, both in vertical and horizontal directions. Convolutional layers with large dilation constants enlarge the receptive field of each output unit without incurring a large computational burden. From bottom to top, the dilation constants are 1, 2, 4, 8, 16, 1, and 1.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Approach", "weight": 1.0} -->

Training loss. Let Θ be the set of all the learnable parameters in our final network, which includes the feature pyramid extractor and the optical flow estimators at different pyramid levels (the warping and cost volume layers have no learnable parameters). Let w l Θ denote the flow field at the l th pyramid level predicted by the network, and w l GT the corresponding supervision signal. We use the same multiscale training loss proposed in FlowNet: where |·| 2 computes the L2 norm of a vector and the second term regularizes parameters of the model. For fine-tuning, we use the following robust training loss: where | · | denotes the L1 norm, q < 1 gives less penalty to outliers, and ϵ is a small constant.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Implementation details. The weights in the training loss are set to be α 6 =0. 32, α 5 =0. 08, α 4 =0. 02, α 3 = 0. 01, and α 2 =0. 005. The trade-off weight γ is set to be 0. 0004. We scale the ground truth flow by 20 and downsample it to obtain the supervision signals at different levels. Note that we do not further scale the supervision signal at each level, the same as. As a result, we need to scale the upsampled flow at each pyramid level for the warping layer. For example, at the second level, we scale the upsampled flow from the third level by a factor of 5 ( =20 / 4 ) before warping features of the second image. We use a 7-level pyramid and set l 0 to be 2, i.e., our model outputs a quarter resolution optical flow and uses bilinear interpolation to obtain the full-resolution optical flow. We use a search range of 4 pixels to compute the cost volume at each level.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We first train the models using the FlyingChairs dataset in Caffe using the S long learning rate schedule introduced, i.e., starting from 0. 0001 and reducing the learning rate by half at 0. 4 M, 0. 6 M, 0. 8 M, and 1 M iterations. The data augmentation scheme is the same as that. We crop 448 × 384 patches during data augmentation and use a batch size of 8. We then fine-tune the models on the FlyingThings3D dataset using the S fine schedule while excluding image pairs with extreme motion (magnitude larger than 1000 pixels). The cropped image size is 768 × 384 and the batch size is 4. Finally, we finetune the models using the Sintel and KITTI training set and will explain the details below.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Main Results", "weight": 1.0} -->

MPI Sintel. When fine-tuning on Sintel, we crop 768 × 384 image patches, add horizontal flip, and remove additive noise during data augmentation. The batch size is 4. We use the robust loss function in Eq. with ϵ = 0. 01 and q = 0. 4. We test two schemes of fine-tuning. The first one, PWC-Net-ft, uses the clean and final passes of the Sintel training data throughout the fine-tuning process. The second one, PWC-Net-ft-final, uses only the final pass for the second half of fine-tuning. We test the second scheme because the DCFlow method learns the features using only the final pass of the training data. Thus we test the performance of PWC-Net when the final pass of the training data is given more weight.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Main Results", "weight": 1.0} -->

At the time of writing, PWC-Net has lower average end-point error (EPE) than all published methods on the final pass of the MPI-Sintel benchmark (Table 1). It is the first time that an end-to-end method outperforms wellengineered and highly fine-tuned traditional methods on this benchmark. Further, PWC-Net is the fastest among all the top-performing methods (Fig. 1). We can further reduce the running time by dropping the DenseNet connections. The resulting PWC-Net-small model is about 5% less accurate but 40% faster than PWC-Net.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Main Results", "weight": 1.0} -->

PWC-Net is less accurate than traditional approaches on the clean pass. Many traditional methods use image edges to refine motion boundaries, because the two are perfectly aligned in the clean pass. However, image edges in the final pass are corrupted by motion blur, atmospheric changes, and noise. Thus, the final pass is more realistic and challenging. The results on the final and clean sets suggest that PWC-Net may be better suited for real images, where the image edges are often corrupted.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Main Results", "weight": 1.0} -->

PWC-Net has higher errors on the training set but lower errors on the test set than FlowNet2, suggesting that PWCNet may have a more appropriate capacity for this task. Table 2 summarizes errors in different regions. PWC-Net performs relatively better in regions with large motion and away from the motion boundaries, probably because it has been trained using only data with large motion. Figure 4 shows the visual results of different variants of PWC-Net on the training and test sets of MPI Sintel. PWC-Net can recover sharp motion boundaries but may fail on small and rapidly moving objects, such as the left arm in 'Market 5'.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Main Results", "weight": 1.0} -->

KITTI. When fine-tuning on KITTI, we crop 896 × 320 image patches and reduce the amount of rotation, zoom, and squeeze during data augmentation. The batch size is 4 too. The large patches can capture the large motion in the KITTI dataset. Since the ground truth is semi-dense, we upsample the predicted flow at the quarter resolution to compare with the scaled ground truth at the full resolution. We exclude the invalid pixels in computing the loss function.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Main Results", "weight": 1.0} -->

At the time of writing, PWC-Net outperforms all published two-frame optical flow methods on the 2015 set, as shown in Table 3. It has the lowest percentage of flow outliers (Fl-all) in both all and non-occluded pixels (Table 4). PWC-Net has the second lowest percentage of outliers in non-occluded regions (Fl-noc) on the 2012 set, only inferior to SDF that assumes a rigidity constraint for the background. Although the rigidity assumption works well on the static scenes in the 2012 set, PWC-Net outperforms SDF in the 2015 set which mainly consists of dynamic scenes and is more challenging. The visual results in Fig. 5 qualitatively demonstrate the benefits of using the context network, DenseNet connections, and fine-tuning respectively. In particular, fine-tuning fixes large regions of errors in the test set, demonstrating the benefit of learning when the training and test data share similar statistics.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Main Results", "weight": 1.0} -->

As shown in Table 4, FlowNet2 and PWC-Net have the most accurate results in the foreground regions, both outperforming the best published scene flow method, ISF.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Main Results", "weight": 1.0} -->

Scene flow methods, however, have much lower errors in the static background region. The results suggest that synergizing advances in optical flow and scene flow could lead to more accurate results.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

Feature pyramid extractor. PWC-Net uses a two-layer CNN to extract features at each pyramid level. Table 5a summarizes the results of two variants that use one layer ( ↓ ) and three layers ( ↑ ) respectively. A larger-capacity feature pyramid extractor leads to consistently better results on both the training and validation datasets.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

Table 1. Average EPE results on MPI Sintel set. '-ft' means finetuning on the MPI Sintel training set and the numbers in the parenthesis are results on the data the methods have been fine-tuned. ft-final gives more weight to the final pass during fine-tuning.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

| Methods | Training | Training | Test | Test | Time | Table 2. Detailed results on the Sintel benchmark for different regions, velocities (s), and distances from motion boundaries (d).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

Table 3. Results on the KITTI dataset. '-ft' means fine-tuning on the KITTI training set and the numbers in the parenthesis are results on the data the methods have been fine-tuned.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

| | KITTI 2012 | KITTI 2012 | KITTI 2012 | KITTI 2015 | KITTI 2015 | KITTI 2015 | Optical flow estimator. PWC-Net uses a five-layer CNN in the optical flow estimator at each level. Table 5b shows the results by two variants that use four layer (↓) and seven layers (↑) respectively. A larger-capacity optical flow estimator leads to better performance. However, we observe in our experiments that a deeper optical flow estimator might get stuck at poor local minima, which can be detected by checking the validation errors after a few thousand iterations and fixed by running from a different random initialization.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

Table 4. Detailed Results on the KITTI 2015 benchmark for the top three optical flow and two scene flow methods (below).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

| Methods | Non-occluded pixels | Non-occluded pixels | Non-occluded pixels | All pixels | All pixels | All pixels | Removing the context network results in larger errors on both the training and validation sets (Table 5c). Removing the DenseNet connections results in higher training error but lower validation errors when the model is trained on FlyingChairs. However, after the model is fine-tuned on FlyingThings3D, DenseNet leads to lower errors.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

We also test a residual version of the optical flow estimator, which estimates a flow increment and adds it to the initial flow to obtain the refined flow. As shown in Table 5f, this residual version slightly improves the performance.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

Cost volume. We test the search range to compute the cost volume, shown in Table 5d. A larger range leads to lower training error. However, all three settings have similar performance on Sintel, because a range of 2 at every level can already deal with a motion up to 200 pixels at the input resolution. A larger range has lower EPE on KITTI, likely because the images from the KITTI dataset have larger displacements than those from Sintel. A smaller range, however, seems to force the network to ignore pixels with extremely large motion and focus more on small-motion pixels, thereby achieving lower Fl-all scores.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

Warping. Warping allows for estimating a small optical flow (increment) at each pyramid level to deal with a large optical flow. Removing the warping layers results in a significant loss of accuracy (Table 5e). Without the warping layer, PWC-Net still produces reasonable results, because the default search range of 4 to compute the cost volume is large enough to capture the motion of most sequences at the low-resolution pyramid levels.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

Dataset scheduling. We also train PWC-Net using different dataset scheduling schemes, as shown in Table 6. Sequentially training on FlyingChairs, FlyingThings3D, and Sintel gradually improves the performance, consistent with the observations. Directly training using the test data leads to good 'over-fitting' results, but the trained model does not perform as well on other datasets.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

Model size and running time. Table 7 summarizes the model size for different CNN models. PWC-Net has about | | Chairs | Sintel | Sintel | KITTI 2012 | KITTI 2012 | KITTI 2015 | KITTI 2015 | (a) Larger-capacity feature pyramid extractor has better performance.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

| | Trained on FlyingChairs | Trained on FlyingChairs | Trained on FlyingChairs | Fine-tuned on FlyingThings | Fine-tuned on FlyingThings | Fine-tuned on FlyingThings | (c) Context network consistently helps; DenseNet helps after fine-tuning.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

| | Chairs | Sintel | Sintel Final | KITTI 2012 | KITTI 2012 | KITTI 2015 | KITTI 2015 | (e) Warping layer is a critical component for the performance.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

| | Chairs | Sintel | Sintel Final | KITTI 2012 | KITTI 2012 | KITTI 2015 | KITTI 2015 | (b) Larger-capacity optical flow estimator has better performance.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

| Max. | Chairs | Sintel | Sintel Final | KITTI 2012 | KITTI 2012 | KITTI 2015 | KITTI 2015 | (d) Cost volume. PWC-Net can handle large motion with small search range.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

| | Chairs | Sintel | Sintel | KITTI 2012 | KITTI 2012 | KITTI 2015 | KITTI 2015 | (f) Residual connections in the optical flow estimator are helpful.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

Table 5. Ablation experiments. Unless explicitly stated, the models have been trained on the FlyingChairs dataset.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

Table 6. Training dataset schedule leads to better local minima. indicates results on the dataset the method has been trained.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

| Data | Chairs | Sintel (AEPE) | Sintel (AEPE) | KITTI 2012 | KITTI 2012 | KITTI 2015 | KITTI 2015 | 17 times fewer parameters than FlowNet2. PWC-Net-small further reduces this by an additional 2 times via dropping DenseNet connections and is more suitable for memorylimited applications.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

The timings have been obtained on the same desktop with an NVIDIA Pascal TitanX GPU. For more precise timing, we exclude the reading and writing time when benchmarking the forward and backward inference time. PWCNet is about 2 times faster in forward inference and at least 3 times faster in training than FlowNet2.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

Table 7. Model size and running time. PWC-Net-small drops DenseNet connections. For training, the lower bound of 14 days for FlowNet2 is obtained by 6(FlowNetC) + 2 × 4 (FlowNetS).

<!-- chunk {"id": "body-0062", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

| Methods | FlowNetS | FlowNetC | FlowNet2 | SpyNet | PWC-Net | PWC-Net-small | Discussions. Both PWC-Net and SpyNet have been inspired by classical principles for flow and stereo but have significant differences. SpyNet uses image pyramids while PWC-Net learns feature pyramids. SpyNet feeds CNNs with images, while PWC-Net feeds a cost volume. As the cost volume is a more discriminative representation of the search space for optical flow, the learning task for CNNs becomes easier. Regarding performance, PWC-Net outperforms SpyNet by a significant margin. Additionally, SpyNet has been trained sequentially, while PWC-Net can be trained end-to-end from scratch.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Ablation Experiments", "weight": 1.0} -->

FlowNet2 achieves impressive performance by stacking several basic models into a large-capacity model. The much smaller PWC-Net obtains similar or better performance by embedding classical principles into the network architecture. It would be interesting to use PWC-Net as a building block to design large networks.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have developed a compact but effective CNN model for optical flow using simple and well-established principles: pyramidal processing, warping, and the use of a cost volume. Combining deep learning with domain knowledge not only reduces the model size but also improves the performance. PWC-Net is about 17 times smaller in size, 2 times faster in inference, and easier to train than FlowNet2. It outperforms all published optical flow methods to date on the Sintel final pass and KITTI 2015 benchmarks, running at about 35 fps on Sintel resolution ( 1024 × 436 ) images.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Given the compactness, efficiency, and effectiveness of PWC-Net, we expect it to be a useful component of many video processing systems. To enable comparison and further innovations, we make our models available on our project website.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Acknowledgements Wewould like to thank Eddy Ilg for clarifying details about the FlowNet2 paper, Ming-Hsuan Yang for helpful suggestions, Michael Pellauer for proofreading, and the anonymous reviewers for constructive comments.
