Accelerating the Super-Resolution Convolutional Neural Network

Topics include Image super-resolution, Convolutional networks, Efficient inference, Deconvolution, Low-resolution feature extraction, Shrinking and expanding layers, Transfer strategy, FSRCNN.

FSRCNN reworks SRCNN for speed by operating before bicubic upsampling, adding a final deconvolution layer, and using a compact hourglass mapping. The design makes the classic CNN super-resolution pipeline much more practical for real-time CPU inference.

As a successful deep model applied in image super-resolution (SR), the Super-Resolution Convolutional Neural Network (SRCNN) has demonstrated superior performance to the previous hand-crafted models either in speed and restoration quality. However, the high computational cost still hinders it from practical usage that demands real-time performance (24 fps). In this paper, we aim at accelerating the current SRCNN, and propose a compact hourglass-shape CNN structure for faster and better SR. We re-design the SRCNN structure mainly in three aspects. First, we introduce a deconvolution layer at the end of the network, then the mapping is learned directly from the original low-resolution image (without interpolation) to the high-resolution one. Second, we reformulate the mapping layer by shrinking the input feature dimension before mapping and expanding back afterwards. Third, we adopt smaller filter sizes but more mapping layers. The proposed model achieves a speed up of more than 40 times with even superior restoration quality. Further, we present the parameter settings that can achieve real-time performance on a generic CPU while still maintaining good performance....

## Introduction

Single image super-resolution (SR) aims at recovering a high-resolution (HR) image from a given low-resolution (LR) one. Recent SR algorithms are mostly learning-based (or patch-based) methods that learn a mapping between the LR and HR image spaces. Among them, the Super-Resolution Convolutional Neural Network (SRCNN) has drawn considerable attention due to its simple network structure and excellent restoration quality. Though SRCNN is already faster than most previous learning-based methods, the processing speed on large images is still unsatisfactory....

Figure 1: The proposed FSRCNN networks achieve better super-resolution quality than existing methods, and are tens of times faster. Especially, the FSRCNN-s can run in real-time ( &gt; 24 fps) on a generic CPU. The chart is based on the results summarized in Tables 3 and 4.

## Conclusion

While observing the limitations of current deep learning based SR models, we explore a more efficient network structure to achieve high running speed without the loss of restoration quality. We approach this goal by re-designing the SRCNN structure, and achieves a final acceleration of more than 40 times. Extensive experiments suggest that the proposed method yields satisfactory SR performance, while superior in terms of run time. The proposed model can be adapted for real-time video SR, and motivate fast deep models for other low-level vision tasks.

Cost function: Following SRCNN, we adopt the mean square error (MSE) as the cost function. The optimization objective is represented as

We refer to SRCNN on the choice of parameters -- $f_{1},n_{1},c_{1}$. In SRCNN, the filter size of the first layer is set to be 9. Note that these filters are performed on the upscaled image $Y$. As most pixels in $Y$ are interpolated from $Y_{s}$, a $5 \times 5$ patch in $Y_{s}$ could cover almost all information of a $9 \times 9$ patch in $Y$. Therefore, we can adopt a smaller filter size $f_{1} = 5$ with little information loss. For the number of channels, we follow SRCNN to set $c_{1} = 1$. Then we only need to determine the filter number $n_{1}$....

## Experiments

First, as a pre-processing step, the original LR image needs to be upsampled to the desired size using bicubic interpolation to form the input....
