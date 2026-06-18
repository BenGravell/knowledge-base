<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

FlowNet 2.0: Evolution of Optical Flow Estimation with Deep Networks

Topics include Optical flow, FlowNet 2.0, Convolutional networks, Network stacking, Warping, Small displacement, Training schedule.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

FlowNet 2.0 shows that learned optical flow can match classical methods when the architecture, training schedule, and small-motion handling are engineered carefully. Its stacked networks with intermediate warping turned FlowNet from an intriguing proof of concept into a practical high-speed optical-flow system.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The FlowNet demonstrated that optical flow estimation can be cast as a learning problem. However, the state of the art with regard to the quality of the flow has still been defined by traditional methods. Particularly on small displacements and real-world data, FlowNet cannot compete with variational methods. In this paper, we advance the concept of end-to-end learning of optical flow and make it work really well. The large improvements in quality and speed are caused by three major contributions: first, we focus on the training data and show that the schedule of presenting data during training is very important. Second, we develop a stacked architecture that includes warping of the second image with intermediate optical flow. Third, we elaborate on small displacements by introducing a sub-network specializing on small motions. FlowNet 2.0 is only marginally slower than the original FlowNet but decreases the estimation error by more than 50%. It performs on par with state-of-the-art methods, while running at interactive frame rates. Moreover, we present faster variants that allow optical flow computation at up to 140fps with accuracy matching the original FlowNet.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The FlowNet by Dosovitskiy *et al*. represented a paradigm shift in optical flow estimation. The idea of using a simple convolutional CNN architecture to directly learn the concept of optical flow from data was completely disjoint from all the established approaches. However, first implementations of new ideas often have a hard time competing with highly fine-tuned existing methods, and FlowNet was no exception to this rule. It is the successive consolidation that resolves the negative effects and helps us appreciate the benefits of new ways of thinking.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

At the same time, it resolves problems with small displacements and noisy artifacts in estimated flow fields. This leads to a dramatic performance improvement on real-world applications such as action recognition and motion segmentation, bringing FlowNet 2.0 to the state-of-the-art level.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The way towards FlowNet 2.0 is via several evolutionary, but decisive modifications that are not trivially connected to the observed problems. First, we evaluate the influence of dataset schedules. Interestingly, the more sophisticated training data provided by Mayer *et al*. leads to inferior results if used in isolation. However, a learning schedule consisting of multiple datasets improves results significantly. In this scope, we also found that the FlowNet version with an explicit correlation layer outperforms the version without such layer. This is in contrast to the results reported in Dosovitskiy *et al*..

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

As a second contribution, we introduce a warping operation and show how stacking multiple networks using this operation can significantly improve the results. By varying the depth of the stack and the size of individual components we obtain many network variants with different size and runtime. This allows us to control the trade-off between accuracy and computational resources. We provide networks for the spectrum between $8$fps and $140$fps.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we focus on small, subpixel motion and real-world data. To this end, we created a special training dataset and a specialized network. We show that the architecture trained with this dataset performs well on small motions typical for real-world videos. To reach optimal performance on arbitrary displacements, we add a network that learns to fuse the former stacked network with the small displacement network in an optimal manner.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The final network outperforms the previous FlowNet by a large margin and performs on par with state-of-the-art methods on the Sintel and KITTI benchmarks. It can estimate small and large displacements with very high level of detail while providing interactive frame rates.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Dataset Schedules", "weight": 1.0} -->

High quality training data is crucial for the success of supervised training. We investigated the differences in the quality of the estimated optical flow depending on the presented training data. Interestingly, it turned out that not only the kind of data is important but also the order in which it is presented during training.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Dataset Schedules", "weight": 1.0} -->

The original FlowNets were trained on the FlyingChairs dataset (we will call it Chairs). This rather simplistic dataset contains about $22$k image pairs of chairs superimposed on random background images from Flickr. Random affine transformations are applied to chairs and background to obtain the second image and ground truth flow fields. The dataset contains only planar motions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Dataset Schedules", "weight": 1.0} -->

The FlyingThings3D (Things3D) dataset proposed by Mayer *et al*. can be seen as a three-dimensional version of the FlyingChairs. The dataset consists of $22$k renderings of random scenes showing 3D models from the ShapeNet dataset moving in front of static 3D backgrounds. In contrast to Chairs, the images show true 3D motion and lighting effects and there is more variety among the object models.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Dataset Schedules", "weight": 1.0} -->

We tested the two network architectures introduced by Dosovitskiy *et al*.: FlowNetS, which is a straightforward encoder-decoder architecture, and FlowNetC, which includes explicit correlation of feature maps. We trained FlowNetS and FlowNetC on Chairs and Things3D and an equal mixture of samples from both datasets using the different learning rate schedules shown in Figure 3. The basic schedule $S_{short}$ ($600$k iterations) corresponds to Dosovitskiy *et al*. except some minor changes^11^1 We do not start with a learning rate of ${1e} - 6$ and increase it first, but we start with ${1e} - 4$ immediately. We fix the learning rate for $300$k iterations and then divide it by $2$ every $100$k iterations.. Apart from this basic schedule $S_{short}$, we investigated a longer schedule $S_{long}$ with $1.2$M iterations, and a schedule for fine-tuning $S_{fine}$ with smaller learning rates.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Dataset Schedules", "weight": 1.0} -->

Results of networks trained on Chairs and Things3D with the different schedules are given in Table 1.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Dataset Schedules", "weight": 1.0} -->

The order of presenting training data with different properties matters. Although Things3D is more realistic, training on Things3D alone leads to worse results than training on Chairs. The best results are consistently achieved when first training on Chairs and only then fine-tuning on Things3D. This schedule also outperforms training on a mixture of Chairs and Things3D. We conjecture that the simpler Chairs dataset helps the network learn the general concept of color matching without developing possibly confusing priors for 3D motion and realistic lighting too early. The result indicates the importance of training data schedules for avoiding shortcuts when learning generic concepts with deep networks.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Dataset Schedules", "weight": 1.0} -->

FlowNetC outperforms FlowNetS. The result we got with FlowNetS and $S_{short}$ corresponds to the one reported in Dosovitskiy *et al*.. However, we obtained much better results on FlowNetC. We conclude that Dosovitskiy *et al*. did not train FlowNetS and FlowNetC under the exact same conditions. When done so, the FlowNetC architecture compares favorably to the FlowNetS architecture.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Dataset Schedules", "weight": 1.0} -->

Improved results. Just by modifying datasets and training schedules, we improved the FlowNetS result reported by Dosovitskiy *et al*. by $\sim {25\%}$ and the FlowNetC result by $\sim {30\%}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Dataset Schedules", "weight": 1.0} -->

In this section, we did not yet use specialized training sets for specialized scenarios. The trained network is rather supposed to be generic and to work well in various scenarios. An additional optional component in dataset schedules is fine-tuning of a generic network to a specific scenario, such as the driving scenario, which we show in Section 6.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Stacking Two Networks for Flow Refinement", "weight": 1.0} -->

All state-of-the-art optical flow approaches rely on iterative methods. Can deep networks also benefit from iterative refinement? To answer this, we experiment with stacking multiple FlowNetS and FlowNetC architectures.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Stacking Two Networks for Flow Refinement", "weight": 1.0} -->

The first network in the stack always gets the images $I_{1}$ and $I_{2}$ as input. Subsequent networks get $I_{1}$, $I_{2}$, and the previous flow estimate $w_{i} = {(u_{i},v_{i})}^{\top}$, where $i$ denotes the index of the network in the stack.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Stacking Two Networks for Flow Refinement", "weight": 1.0} -->

To make assessment of the previous error and computing an incremental update easier for the network, we also optionally warp the second image $I_{2}{(x,y)}$ via the flow $w_{i}$ and bilinear interpolation to ${{\overset{\sim}{I}}_{2,i}{(x,y)}} = {I_{2}{({x + u_{i}},{y + v_{i}})}}$. This way, the next network in the stack can focus on the remaining increment between $I_{1}$ and ${\overset{\sim}{I}}_{2,i}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Stacking Two Networks for Flow Refinement", "weight": 1.0} -->

When using warping, we additionally provide ${\overset{\sim}{I}}_{2,i}$ and the error $e_{i} = {\|{{\overset{\sim}{I}}_{2,i} - I_{1}}\|}$ as input to the next network; see Figure 2. Thanks to bilinear interpolation, the derivatives of the warping operation can be computed (see supplemental material for details). This enables training of stacked networks end-to-end.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Stacking Two Networks for Flow Refinement", "weight": 1.0} -->

Table 2 shows the effect of stacking two networks, the effect of warping, and the effect of end-to-end training. We take the best FlowNetS from Section 3 and add another FlowNetS on top. The second network is initialized randomly and then the stack is trained on Chairs with the schedule $S_{long}$. We experimented with two scenarios: keeping the weights of the first network fixed, or updating them together with the weights of the second network. In the latter case, the weights of the first network are fixed for the first 400k iterations to first provide a good initialization of the second network. We report the error on Sintel train clean and on the test set of Chairs. Since the Chairs test set is much more similar to the training data than Sintel, comparing results on both datasets allows us to detect tendencies to over-fitting.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Stacking Two Networks for Flow Refinement", "weight": 1.0} -->

We make the following observations: Just stacking networks without warping improves results on Chairs but decreases performance on Sintel, i.e. the stacked network is over-fitting. With warping included, stacking always improves results. Adding an intermediate loss after Net1 is advantageous when training the stacked network end-to-end. The best results are obtained when keeping the first network fixed and only training the second network after the warping operation.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Stacking Two Networks for Flow Refinement", "weight": 1.0} -->

Clearly, since the stacked network is twice as big as the single network, over-fitting is an issue. The positive effect of flow refinement after warping can counteract this problem, yet the best of both is obtained when the stacked networks are trained one after the other, since this avoids over-fitting while having the benefit of flow refinement.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Stacking Multiple Diverse Networks", "weight": 1.0} -->

Rather than stacking identical networks, it is possible to stack networks of different type (FlowNetC and FlowNetS). Reducing the size of the individual networks is another valid option. We now investigate different combinations and additionally also vary the network size.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Stacking Multiple Diverse Networks", "weight": 1.0} -->

We call the first network the bootstrap network as it differs from the second network by its inputs. The second network could however be repeated an arbitray number of times in a recurrent fashion. We conducted this experiment and found that applying a network with the same weights multiple times and also fine-tuning this recurrent part does not improve results (see supplemental material for details). As also done, we therefore add networks with different weights to the stack. Compared to identical weights, stacking networks with different weights increases the memory footprint, but does not increase the runtime. In this case the top networks are not constrained to a general improvement of their input, but can perform different tasks at different stages and the stack can be trained in smaller pieces by fixing existing networks and adding new networks one-by-one. We do so by using the Chairs $\rightarrow$Things3D schedule from Section 3 for every new network and the best configuration with warping from Section 4.1. Furthermore, we experiment with different network sizes and alternatively use FlowNetS or FlowNetC as a bootstrapping network.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Stacking Multiple Diverse Networks", "weight": 1.0} -->

We use FlowNetC only in case of the bootstrap network, as the input to the next network is too diverse to be properly handeled by the Siamese structure of FlowNetC. Smaller size versions of the networks were created by taking only a fraction of the number of channels for every layer in the network. Figure 4 shows the network accuracy and runtime for different network sizes of a single FlowNetS. Factor $\frac{3}{8}$ yields a good trade-off between speed and accuracy when aiming for faster networks.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Stacking Multiple Diverse Networks", "weight": 1.0} -->

Notation: We denote networks trained by the Chairs $\rightarrow$Things3D schedule from Section 3 starting with FlowNet2. Networks in a stack are trained with this schedule one-by-one. For the stack configuration we append upper- or lower-case letters to indicate the original FlowNet or the thin version with $\frac{3}{8}$ of the channels. E.g: FlowNet2-CSS stands for a network stack consisting of one FlowNetC and two FlowNetS. FlowNet2-css is the same but with fewer channels.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Stacking Multiple Diverse Networks", "weight": 1.0} -->

Table 3 shows the performance of different network stacks. Most notably, the final FlowNet2-CSS result improves by $\sim {30\%}$ over the single network FlowNet2-C from Section 3 and by $\sim {50\%}$ over the original FlowNetC. Furthermore, two small networks in the beginning always outperform one large network, despite being faster and having fewer weights: FlowNet2-ss ($11$M weights) over FlowNet2-S ($38$M weights), and FlowNet2-cs ($11$M weights) over FlowNet2-C ($38$M weights). Training smaller units step by step proves to be advantageous and enables us to train very deep networks for optical flow. At last, FlowNet2-s provides nearly the same accuracy as the original FlowNet, while running at $140$ frames per second.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Datasets", "weight": 1.0} -->

While the original FlowNet performed well on the Sintel benchmark, limitations in real-world applications have become apparent. In particular, the network cannot reliably estimate small motions (see Figure 1). This is counter-intuitive, since small motions are easier for traditional methods, and there is no obvious reason why networks should not reach the same performance in this setting. Thus, we examined the training data and compared it to the UCF101 dataset as one example of real-world data. While Chairs are similar to Sintel, UCF101 is fundamentally different (we refer to our supplemental material for the analysis): Sintel is an action movie and as such contains many fast movements that are difficult for traditional methods, while the displacements we see in the UCF101 dataset are much smaller, mostly smaller than $1$ pixel. Thus, we created a dataset in the visual style of Chairs but with very small displacements and a displacement histogram much more like UCF101. We also added cases with a background that is homogeneous or just consists of color gradients. We call this dataset ChairsSDHom and will release it upon publication.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Small Displacement Network and Fusion", "weight": 1.0} -->

We fine-tuned our FlowNet2-CSS network for smaller displacements by further training the whole network stack on a mixture of Things3D and ChairsSDHom and by applying a non-linearity to the error to downweight large displacements^22^2For details we refer to the supplemental material. We denote this network by FlowNet2-CSS-ft-sd. This increases performance on small displacements and we found that this particular mixture does not sacrifice performance on large displacements. However, in case of subpixel motion, noise still remains a problem and we conjecture that the FlowNet architecture might in general not be perfect for such motion. Therefore, we slightly modified the original FlowNetS architecture and removed the stride $2$ in the first layer. We made the beginning of the network deeper by exchanging the $7 \times 7$ and $5 \times 5$ kernels in the beginning with multiple $3 \times 3$ kernels^22^footnotemark: 2. Because noise tends to be a problem with small displacements, we add convolutions between the upconvolutions to obtain smoother estimates as. We denote the resulting architecture by FlowNet2-SD; see Figure 2.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Small Displacement Network and Fusion", "weight": 1.0} -->

Finally, we created a small network that fuses FlowNet2-CSS-ft-sd and FlowNet2-SD (see Figure 2). The fusion network receives the flows, the flow magnitudes and the errors in brightness after warping as input. It contracts the resolution two times by a factor of $2$ and expands again^22^footnotemark: 2. Contrary to the original FlowNet architecture it expands to the full resolution. We find that this produces crisp motion boundaries and performs well on small as well as on large displacements. We denote the final network as FlowNet2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

We compare the best variants of our network to state-of-the-art approaches on public bechmarks. In addition, we provide a comparison on application tasks, such as motion segmentation and action recognition. This allows benchmarking the method on real data.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Speed and Performance on Public Benchmarks", "weight": 1.0} -->

We evaluated all methods^33^3An exception is EPPM for which we could not provide the required Windows environment and use the results. on a system with an Intel Xeon E5 with 2.40GHz and an Nvidia GTX 1080. Where applicable, dataset-specific parameters were used, that yield best performance. Endpoint errors and runtimes are given in Table 4.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Speed and Performance on Public Benchmarks", "weight": 1.0} -->

Sintel: On Sintel, FlowNet2 consistently outperforms DeepFlow and EpicFlow and is on par with FlowFields. All methods with comparable runtimes have clearly inferior accuracy. We fine-tuned FlowNet2 on a mixture of Sintel clean+final training data (FlowNet2--ft-sintel). On the benchmark, in case of clean data this slightly degraded the result, while on final data FlowNet2--ft-sintel is on par with the currently published state-of-the art method DeepDiscreteFlow.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Speed and Performance on Public Benchmarks", "weight": 1.0} -->

KITTI: On KITTI, the results of FlowNet2-CSS are comparable to EpicFlow and FlowFields. Fine-tuning on small displacement data degrades the result. This is probably due to KITTI containing very large displacements in general. Fine-tuning on a combination of the KITTI2012 and KITTI2015 training sets reduces the error roughly by a factor of $3$ (FlowNet2-ft-kitti). Among non-stereo methods we obtain the best EPE on KITTI2012 and the first rank on the KITTI2015 benchmark. This shows how well and elegantly the learning approach can integrate the prior of the driving scenario.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Speed and Performance on Public Benchmarks", "weight": 1.0} -->

Middlebury: On the Middlebury training set FlowNet2 performs comparable to traditional methods. The results on the Middlebury test set are unexpectedly a lot worse. Still, there is a large improvement compared to FlowNetS.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Speed and Performance on Public Benchmarks", "weight": 1.0} -->

Endpoint error vs. runtime evaluations for Sintel are provided in Figure 4. One can observe that the FlowNet2 family outperforms the best and fastest existing methods by large margins. Depending on the type of application, a FlowNet2 variant between 8 to 140 frames per second can be used.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Figures 6 and 7 show example results on Sintel and on real-world data. While the performance on Sintel is similar to FlowFields, we can see that on real world data FlowNet 2.0 clearly has advantages in terms of being robust to homogeneous regions (rows 2 and 5), image and compression artifacts (rows 3 and 4) and it yields smooth flow fields with sharp motion boundaries.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Performance on Motion Segmentation and Action Recognition", "weight": 1.0} -->

To assess performance of FlowNet 2.0 in real-world applications, we compare the performance of action recognition and motion segmentation. For both applications, good optical flow is key. Thus, a good performance on these tasks also serves as an indicator for good optical flow.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Performance on Motion Segmentation and Action Recognition", "weight": 1.0} -->

For motion segmentation, we rely on the well-established approach of Ochs *et al*. to compute long term point trajectories. A motion segmentation is obtained from these using the state-of-the-art method from Keuper *et al*.. The results are shown in Table 5. The original model in Ochs *et al*. was built on Large Displacement Optical Flow. We included also other popular optical flow methods in the comparison. The old FlowNet was not useful for motion segmentation. In contrast, the FlowNet2 is as reliable as other state-of-the-art methods while being orders of magnitude faster.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Performance on Motion Segmentation and Action Recognition", "weight": 1.0} -->

Optical flow is also a crucial feature for action recognition. To assess the performance, we trained the temporal stream of the two-stream approach from Simonyan *et al*. with different optical flow inputs. Table 5 shows that FlowNetS did not provide useful results, while the flow from FlowNet 2.0 yields comparable results to state-of-the art methods.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have presented several improvements to the FlowNet idea that have led to accuracy that is fully on par with state-of-the-art methods while FlowNet 2.0 runs orders of magnitude faster. We have quantified the effect of each contribution and showed that all play an important role. The experiments on motion segmentation and action recognition show that the estimated optical flow with FlowNet 2.0 is reliable on a large variety of scenes and applications. The FlowNet 2.0 family provides networks running at speeds from 8 to 140fps. This further extends the possible range of applications. While the results on Middlebury indicate imperfect performance on subpixel motion, FlowNet 2.0 results highlight very crisp motion boundaries, retrieval of fine structures, and robustness to compression artifacts. Thus, we expect it to become the working horse for all applications that require accurate and fast optical flow computation.
