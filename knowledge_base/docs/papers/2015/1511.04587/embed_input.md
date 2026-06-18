Accurate Image Super-Resolution Using Very Deep Convolutional Networks

Topics include Image super-resolution, Convolutional networks, Very deep networks, Residual learning, Gradient clipping, High learning rate, VGG-style networks, VDSR.

VDSR shows that much deeper CNNs can improve single-image super-resolution when trained as residual predictors with aggressive learning rates and gradient clipping. It marks an important transition from shallow SRCNN-style mappings to deeper residual restoration networks.

We present a highly accurate single-image super-resolution (SR) method. Our method uses a very deep convolutional network inspired by VGG-net used for ImageNet classification \cite{simonyan2015very}. We find increasing our network depth shows a significant improvement in accuracy. Our final model uses 20 weight layers. By cascading small filters many times in a deep network structure, contextual information over large image regions is exploited in an efficient way. With very deep networks, however, convergence speed becomes a critical issue during training. We propose a simple yet effective training procedure. We learn residuals only and use extremely high learning rates (10^ times higher than SRCNN \cite{dong2015image}) enabled by adjustable gradient clipping. Our proposed method performs better than existing methods in accuracy and visual improvements in our results are easily noticeable.

## Introduction

We address the problem of generating a high-resolution (HR) image given a low-resolution (LR) image, commonly referred as single image super-resolution (SISR). SISR is widely used in computer vision applications ranging from security and surveillance imaging to medical imaging where more image details are required on demand.

Many SISR methods have been studied in the computer vision community. Early methods include interpolation such as bicubic interpolation and Lanczos resampling more powerful methods utilizing statistical image priors or internal patch recurrence.

## Conclusion

In this work, we have presented a super-resolution method using very deep networks. Training a very deep network is hard due to a slow convergence rate. We use residual-learning and extremely high learning rates to optimize a very deep network fast. Convergence speed is maximized and we use gradient clipping to ensure the training stability. We have demonstrated that our method outperforms the existing method by a large margin on benchmarked images. We believe our approach is readily applicable to other image restoration problems such as denoising and compression artifact removal.

Figure 5: (Top) Our results using a single network for all scale factors. Super-resolved images over all scales are clean and sharp. (Bottom) Results of Dong et al. (×3 model used for all scales). Result images are not visually pleasing. To handle multiple scales, existing methods require multiple networks.

We now describe the objective to minimize in order to find optimal parameters of our model. Let $\mathbf{x}$ denote an interpolated low-resolution image and $\mathbf{y}$ a high-resolution image. Given a training dataset ${\{\mathbf{x}^{(i)},\mathbf{y}^{(i)}\}}_{i = 1}^{N}$, our goal is to learn a model $f$ that predicts values $\hat{\mathbf{y}} = {f{(\mathbf{x})}}$, where $\hat{\mathbf{y}}$ is an estimate of the target HR image. We minimize the mean squared error $\frac{1}{2}{\|{\mathbf{y} - {f{(\mathbf{x})}}}\|}^{2}$ averaged over the training set is minimized.

### Residual-Learning

Currently, learning methods are widely used to model a mapping from LR to HR patches. Neighbor embedding methods interpolate the patch subspace. Sparse coding methods use a learned compact dictionary based on sparse signal representation....
