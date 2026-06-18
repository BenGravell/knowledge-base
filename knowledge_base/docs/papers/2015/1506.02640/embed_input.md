<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

You Only Look Once: Unified, Real-Time Object Detection

Topics include Neural networks, Object detection, Regression, Classifiers, Datasets, Real-time systems, Once.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

This paper presents YOLO, a new approach to object detection. The abstract also notes that prior work on object detection repurposes classifiers to perform detection.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present YOLO, a new approach to object detection. Prior work on object detection repurposes classifiers to perform detection. Instead, we frame object detection as a regression problem to spatially separated bounding boxes and associated class probabilities. A single neural network predicts bounding boxes and class probabilities directly from full images in one evaluation. Since the whole detection pipeline is a single network, it can be optimized end-to-end directly on detection performance. Our unified architecture is extremely fast. Our base YOLO model processes images in real-time at 45 frames per second. A smaller version of the network, Fast YOLO, processes an astounding 155 frames per second while still achieving double the mAP of other real-time detectors. Compared to state-of-the-art detection systems, YOLO makes more localization errors but is far less likely to predict false detections where nothing exists. Finally, YOLO learns very general representations of objects. It outperforms all other detection methods, including DPM and R-CNN, by a wide margin when generalizing from natural images to artwork on both the Picasso Dataset and the People-Art Dataset.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Humans glance at an image and instantly know what objects are in the image, where they are, and how they interact. The human visual system is fast and accurate, allowing us to perform complex tasks like driving with little conscious thought. Fast, accurate algorithms for object detection would allow computers to drive cars without specialized sensors, enable assistive devices to convey real-time scene information to human users, and unlock the potential for general purpose, responsive robotic systems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Current detection systems repurpose classifiers to perform detection. To detect an object, these systems take a classifier for that object and evaluate it at various locations and scales in a test image. Systems like deformable parts models (DPM) use a sliding window approach where the classifier is run at evenly spaced locations over the entire image.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

More recent approaches like R-CNN use region proposal methods to first generate potential bounding boxes in an image and then run a classifier on these proposed boxes. After classification, post-processing is used to refine the bounding boxes, eliminate duplicate detections, and rescore the boxes based on other objects in the scene. These complex pipelines are slow and hard to optimize because each individual component must be trained separately.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We reframe object detection as a single regression problem, straight from image pixels to bounding box coordinates and class probabilities. Using our system, you only look once (YOLO) at an image to predict what objects are present and where they are.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

YOLO is refreshingly simple: see Figure 1. A single convolutional network simultaneously predicts multiple bounding boxes and class probabilities for those boxes. YOLO trains on full images and directly optimizes detection performance. This unified model has several benefits over traditional methods of object detection.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

First, YOLO is extremely fast. Since we frame detection as a regression problem we don't need a complex pipeline. We simply run our neural network on a new image at test time to predict detections. Our base network runs at 45 frames per second with no batch processing on a Titan X GPU and a fast version runs at more than 150 fps. This means we can process streaming video in real-time with less than 25 milliseconds of latency. Furthermore, YOLO achieves more than twice the mean average precision of other real-time systems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, YOLO reasons globally about the image when making predictions. Unlike sliding window and region proposal-based techniques, YOLO sees the entire image during training and test time so it implicitly encodes contextual information about classes as well as their appearance. Fast R-CNN, a top detection method, mistakes background patches in an image for objects because it can't see the larger context. YOLO makes less than half the number of background errors compared to Fast R-CNN.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Third, YOLO learns generalizable representations of objects. When trained on natural images and tested on artwork, YOLO outperforms top detection methods like DPM and R-CNN by a wide margin. Since YOLO is highly generalizable it is less likely to break down when applied to new domains or unexpected inputs.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

YOLO still lags behind state-of-the-art detection systems in accuracy. While it can quickly identify objects in images it struggles to precisely localize some objects, especially small ones. We examine these tradeoffs further in our experiments.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

All of our training and testing code is open source. A variety of pretrained models are also available to download.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Unified Detection", "weight": 1.0} -->

We unify the separate components of object detection into a single neural network. Our network uses features from the entire image to predict each bounding box. It also predicts all bounding boxes across all classes for an image simultaneously. This means our network reasons globally about the full image and all the objects in the image. The YOLO design enables end-to-end training and real-time speeds while maintaining high average precision.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Unified Detection", "weight": 1.0} -->

Our system divides the input image into an $S \times S$ grid. If the center of an object falls into a grid cell, that grid cell is responsible for detecting that object.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Unified Detection", "weight": 1.0} -->

Each grid cell predicts $B$ bounding boxes and confidence scores for those boxes. These confidence scores reflect how confident the model is that the box contains an object and also how accurate it thinks the box is that it predicts. Formally we define confidence as ${\Pr{(\text{Object})}} \ast \text{IOU}_{\text{pred}}^{\text{truth}}$. If no object exists in that cell, the confidence scores should be zero. Otherwise we want the confidence score to equal the intersection over union (IOU) between the predicted box and the ground truth.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Unified Detection", "weight": 1.0} -->

Each bounding box consists of 5 predictions: $x$, $y$, $w$, $h$, and confidence. The $(x,y)$ coordinates represent the center of the box relative to the bounds of the grid cell. The width and height are predicted relative to the whole image. Finally the confidence prediction represents the IOU between the predicted box and any ground truth box.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Unified Detection", "weight": 1.0} -->

Each grid cell also predicts $C$ conditional class probabilities, $\Pr{({\left. \text{Class}_{i} \right|\text{Object}})}$. These probabilities are conditioned on the grid cell containing an object. We only predict one set of class probabilities per grid cell, regardless of the number of boxes $B$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Unified Detection", "weight": 1.0} -->

At test time we multiply the conditional class probabilities and the individual box confidence predictions,

<!-- chunk {"id": "body-0020", "role": "body", "section": "Unified Detection", "weight": 1.0} -->

which gives us class-specific confidence scores for each box. These scores encode both the probability of that class appearing in the box and how well the predicted box fits the object.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Unified Detection", "weight": 1.0} -->

For evaluating YOLO on Pascal VOC, we use $S = 7$, $B = 2$. Pascal VOC has 20 labelled classes so $C = 20$. Our final prediction is a $7 \times 7 \times 30$ tensor.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Network Design", "weight": 1.0} -->

We implement this model as a convolutional neural network and evaluate it on the Pascal VOC detection dataset. The initial convolutional layers of the network extract features from the image while the fully connected layers predict the output probabilities and coordinates.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Network Design", "weight": 1.0} -->

Our network architecture is inspired by the GoogLeNet model for image classification. Our network has 24 convolutional layers followed by 2 fully connected layers. Instead of the inception modules used by GoogLeNet, we simply use $1 \times 1$ reduction layers followed by $3 \times 3$ convolutional layers, similar to Lin et al. The full network is shown in Figure 3.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Network Design", "weight": 1.0} -->

We also train a fast version of YOLO designed to push the boundaries of fast object detection. Fast YOLO uses a neural network with fewer convolutional layers (9 instead of 24) and fewer filters in those layers. Other than the size of the network, all training and testing parameters are the same between YOLO and Fast YOLO.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Network Design", "weight": 1.0} -->

The final output of our network is the $7 \times 7 \times 30$ tensor of predictions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Training", "weight": 1.0} -->

We pretrain our convolutional layers on the ImageNet 1000-class competition dataset. For pretraining we use the first 20 convolutional layers from Figure 3 followed by a average-pooling layer and a fully connected layer. We train this network for approximately a week and achieve a single crop top-5 accuracy of 88% on the ImageNet 2012 validation set, comparable to the GoogLeNet models in Caffe's Model Zoo. We use the Darknet framework for all training and inference.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Training", "weight": 1.0} -->

We then convert the model to perform detection. Ren et al. show that adding both convolutional and connected layers to pretrained networks can improve performance. Following their example, we add four convolutional layers and two fully connected layers with randomly initialized weights. Detection often requires fine-grained visual information so we increase the input resolution of the network from $224 \times 224$ to $448 \times 448$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Training", "weight": 1.0} -->

Our final layer predicts both class probabilities and bounding box coordinates. We normalize the bounding box width and height by the image width and height so that they fall between 0 and 1. We parametrize the bounding box $x$ and $y$ coordinates to be offsets of a particular grid cell location so they are also bounded between 0 and 1.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Training", "weight": 1.0} -->

We optimize for sum-squared error in the output of our model. We use sum-squared error because it is easy to optimize, however it does not perfectly align with our goal of maximizing average precision. It weights localization error equally with classification error which may not be ideal. Also, in every image many grid cells do not contain any object. This pushes the "confidence" scores of those cells towards zero, often overpowering the gradient from cells that do contain objects. This can lead to model instability, causing training to diverge early.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Training", "weight": 1.0} -->

To remedy this, we increase the loss from bounding box coordinate predictions and decrease the loss from confidence predictions for boxes that don't contain objects. We use two parameters, $\lambda_{\text{coord}}$ and $\lambda_{\text{noobj}}$ to accomplish this. We set $\lambda_{\text{coord}} = 5$ and $\lambda_{\text{noobj}} =.5$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Training", "weight": 1.0} -->

Sum-squared error also equally weights errors in large boxes and small boxes. Our error metric should reflect that small deviations in large boxes matter less than in small boxes. To partially address this we predict the square root of the bounding box width and height instead of the width and height directly.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Training", "weight": 1.0} -->

YOLO predicts multiple bounding boxes per grid cell. At training time we only want one bounding box predictor to be responsible for each object. We assign one predictor to be "responsible" for predicting an object based on which prediction has the highest current IOU with the ground truth. This leads to specialization between the bounding box predictors. Each predictor gets better at predicting certain sizes, aspect ratios, or classes of object, improving overall recall.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Training", "weight": 1.0} -->

where $\mathbb{1}_{i}^{\text{obj}}$ denotes if object appears in cell $i$ and $\mathbb{1}_{ij}^{\text{obj}}$ denotes that the $j$th bounding box predictor in cell $i$ is "responsible" for that prediction.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Training", "weight": 1.0} -->

Note that the loss function only penalizes classification error if an object is present in that grid cell (hence the conditional class probability discussed earlier). It also only penalizes bounding box coordinate error if that predictor is "responsible" for the ground truth box (i.e. has the highest IOU of any predictor in that grid cell).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Training", "weight": 1.0} -->

We train the network for about 135 epochs on the training and validation data sets from Pascal VOC 2007 and 2012. When testing on 2012 we also include the VOC 2007 test data for training. Throughout training we use a batch size of 64, a momentum of $0.9$ and a decay of $0.0005$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Training", "weight": 1.0} -->

Our learning rate schedule is as follows: For the first epochs we slowly raise the learning rate from $10^{- 3}$ to $10^{- 2}$. If we start at a high learning rate our model often diverges due to unstable gradients. We continue training with $10^{- 2}$ for 75 epochs, then $10^{- 3}$ for 30 epochs, and finally $10^{- 4}$ for 30 epochs.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Training", "weight": 1.0} -->

To avoid overfitting we use dropout and extensive data augmentation. A dropout layer with rate =.5 after the first connected layer prevents co-adaptation between layers. For data augmentation we introduce random scaling and translations of up to 20% of the original image size. We also randomly adjust the exposure and saturation of the image by up to a factor of $1.5$ in the HSV color space.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Inference", "weight": 1.0} -->

Just like in training, predicting detections for a test image only requires one network evaluation. On Pascal VOC the network predicts 98 bounding boxes per image and class probabilities for each box. YOLO is extremely fast at test time since it only requires a single network evaluation, unlike classifier-based methods.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Inference", "weight": 1.0} -->

The grid design enforces spatial diversity in the bounding box predictions. Often it is clear which grid cell an object falls in to and the network only predicts one box for each object. However, some large objects or objects near the border of multiple cells can be well localized by multiple cells. Non-maximal suppression can be used to fix these multiple detections. While not critical to performance as it is for R-CNN or DPM, non-maximal suppression adds 2-3% in mAP.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Limitations of YOLO", "weight": 1.5} -->

YOLO imposes strong spatial constraints on bounding box predictions since each grid cell only predicts two boxes and can only have one class. This spatial constraint limits the number of nearby objects that our model can predict. Our model struggles with small objects that appear in groups, such as flocks of birds.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Limitations of YOLO", "weight": 1.5} -->

Since our model learns to predict bounding boxes from data, it struggles to generalize to objects in new or unusual aspect ratios or configurations. Our model also uses relatively coarse features for predicting bounding boxes since our architecture has multiple downsampling layers from the input image.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Limitations of YOLO", "weight": 1.5} -->

Finally, while we train on a loss function that approximates detection performance, our loss function treats errors the same in small bounding boxes versus large bounding boxes. A small error in a large box is generally benign but a small error in a small box has a much greater effect on IOU. Our main source of error is incorrect localizations.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Comparison to Other Detection Systems", "weight": 1.0} -->

Object detection is a core problem in computer vision. Detection pipelines generally start by extracting a set of robust features from input images (Haar, SIFT, HOG, convolutional features ). Then, classifiers or localizers are used to identify objects in the feature space. These classifiers or localizers are run either in sliding window fashion over the whole image or on some subset of regions in the image. We compare the YOLO detection system to several top detection frameworks, highlighting key similarities and differences.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Comparison to Other Detection Systems", "weight": 1.0} -->

Deformable parts models. Deformable parts models (DPM) use a sliding window approach to object detection. DPM uses a disjoint pipeline to extract static features, classify regions, predict bounding boxes for high scoring regions, etc. Our system replaces all of these disparate parts with a single convolutional neural network. The network performs feature extraction, bounding box prediction, non-maximal suppression, and contextual reasoning all concurrently. Instead of static features, the network trains the features in-line and optimizes them for the detection task. Our unified architecture leads to a faster, more accurate model than DPM.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Comparison to Other Detection Systems", "weight": 1.0} -->

R-CNN. R-CNN and its variants use region proposals instead of sliding windows to find objects in images. Selective Search generates potential bounding boxes, a convolutional network extracts features, an SVM scores the boxes, a linear model adjusts the bounding boxes, and non-max suppression eliminates duplicate detections. Each stage of this complex pipeline must be precisely tuned independently and the resulting system is very slow, taking more than 40 seconds per image at test time.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Comparison to Other Detection Systems", "weight": 1.0} -->

YOLO shares some similarities with R-CNN. Each grid cell proposes potential bounding boxes and scores those boxes using convolutional features. However, our system puts spatial constraints on the grid cell proposals which helps mitigate multiple detections of the same object. Our system also proposes far fewer bounding boxes, only 98 per image compared to about 2000 from Selective Search. Finally, our system combines these individual components into a single, jointly optimized model.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Comparison to Other Detection Systems", "weight": 1.0} -->

Other Fast Detectors Fast and Faster R-CNN focus on speeding up the R-CNN framework by sharing computation and using neural networks to propose regions instead of Selective Search. While they offer speed and accuracy improvements over R-CNN, both still fall short of real-time performance.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Comparison to Other Detection Systems", "weight": 1.0} -->

Many research efforts focus on speeding up the DPM pipeline. They speed up HOG computation, use cascades, and push computation to GPUs. However, only 30Hz DPM actually runs in real-time.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Comparison to Other Detection Systems", "weight": 1.0} -->

Instead of trying to optimize individual components of a large detection pipeline, YOLO throws out the pipeline entirely and is fast by design.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Comparison to Other Detection Systems", "weight": 1.0} -->

Detectors for single classes like faces or people can be highly optimized since they have to deal with much less variation. YOLO is a general purpose detector that learns to detect a variety of objects simultaneously.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Comparison to Other Detection Systems", "weight": 1.0} -->

Deep MultiBox. Unlike R-CNN, Szegedy et al. train a convolutional neural network to predict regions of interest instead of using Selective Search. MultiBox can also perform single object detection by replacing the confidence prediction with a single class prediction. However, MultiBox cannot perform general object detection and is still just a piece in a larger detection pipeline, requiring further image patch classification. Both YOLO and MultiBox use a convolutional network to predict bounding boxes in an image but YOLO is a complete detection system.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Comparison to Other Detection Systems", "weight": 1.0} -->

OverFeat. Sermanet et al. train a convolutional neural network to perform localization and adapt that localizer to perform detection. OverFeat efficiently performs sliding window detection but it is still a disjoint system. OverFeat optimizes for localization, not detection performance. Like DPM, the localizer only sees local information when making a prediction. OverFeat cannot reason about global context and thus requires significant post-processing to produce coherent detections.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Comparison to Other Detection Systems", "weight": 1.0} -->

MultiGrasp. Our work is similar in design to work on grasp detection by Redmon et al. Our grid approach to bounding box prediction is based on the MultiGrasp system for regression to grasps. However, grasp detection is a much simpler task than object detection. MultiGrasp only needs to predict a single graspable region for an image containing one object. It doesn't have to estimate the size, location, or boundaries of the object or predict it's class, only find a region suitable for grasping. YOLO predicts both bounding boxes and class probabilities for multiple objects of multiple classes in an image.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Experiments", "weight": 1.0} -->

First we compare YOLO with other real-time detection systems on Pascal VOC 2007. To understand the differences between YOLO and R-CNN variants we explore the errors on VOC 2007 made by YOLO and Fast R-CNN, one of the highest performing versions of R-CNN. Based on the different error profiles we show that YOLO can be used to rescore Fast R-CNN detections and reduce the errors from background false positives, giving a significant performance boost. We also present VOC 2012 results and compare mAP to current state-of-the-art methods. Finally, we show that YOLO generalizes to new domains better than other detectors on two artwork datasets.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Comparison to Other Real-Time Systems", "weight": 1.0} -->

Many research efforts in object detection focus on making standard detection pipelines fast. However, only Sadeghi et al. actually produce a detection system that runs in real-time (30 frames per second or better). We compare YOLO to their GPU implementation of DPM which runs either at 30Hz or 100Hz. While the other efforts don't reach the real-time milestone we also compare their relative mAP and speed to examine the accuracy-performance tradeoffs available in object detection systems.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Comparison to Other Real-Time Systems", "weight": 1.0} -->

Fast YOLO is the fastest object detection method on Pascal; as far as we know, it is the fastest extant object detector. With $52.7\%$ mAP, it is more than twice as accurate as prior work on real-time detection. YOLO pushes mAP to $63.4\%$ while still maintaining real-time performance.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Comparison to Other Real-Time Systems", "weight": 1.0} -->

We also train YOLO using VGG-16. This model is more accurate but also significantly slower than YOLO. It is useful for comparison to other detection systems that rely on VGG-16 but since it is slower than real-time the rest of the paper focuses on our faster models.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Comparison to Other Real-Time Systems", "weight": 1.0} -->

Fastest DPM effectively speeds up DPM without sacrificing much mAP but it still misses real-time performance by a factor of 2. It also is limited by DPM's relatively low accuracy on detection compared to neural network approaches.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Comparison to Other Real-Time Systems", "weight": 1.0} -->

R-CNN minus R replaces Selective Search with static bounding box proposals. While it is much faster than R-CNN, it still falls short of real-time and takes a significant accuracy hit from not having good proposals.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Comparison to Other Real-Time Systems", "weight": 1.0} -->

Fast R-CNN speeds up the classification stage of R-CNN but it still relies on selective search which can take around 2 seconds per image to generate bounding box proposals. Thus it has high mAP but at $0.5$ fps it is still far from real-time.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Comparison to Other Real-Time Systems", "weight": 1.0} -->

The recent Faster R-CNN replaces selective search with a neural network to propose bounding boxes, similar to Szegedy et al. In our tests, their most accurate model achieves 7 fps while a smaller, less accurate one runs at 18 fps. The VGG-16 version of Faster R-CNN is 10 mAP higher but is also 6 times slower than YOLO. The Zeiler-Fergus Faster R-CNN is only 2.5 times slower than YOLO but is also less accurate.

<!-- chunk {"id": "body-0062", "role": "body", "section": "VOC 2007 Error Analysis", "weight": 1.0} -->

To further examine the differences between YOLO and state-of-the-art detectors, we look at a detailed breakdown of results on VOC 2007. We compare YOLO to Fast R-CNN since Fast R-CNN is one of the highest performing detectors on Pascal and it's detections are publicly available.

<!-- chunk {"id": "body-0063", "role": "body", "section": "VOC 2007 Error Analysis", "weight": 1.0} -->

We use the methodology and tools of Hoiem et al. For each category at test time we look at the top N predictions for that category.

<!-- chunk {"id": "body-0064", "role": "body", "section": "VOC 2007 Error Analysis", "weight": 1.0} -->

Correct: correct class and $\text{IOU} >.5$

<!-- chunk {"id": "body-0065", "role": "body", "section": "VOC 2007 Error Analysis", "weight": 1.0} -->

Localization: correct class, $.1 < \text{IOU} <.5$

<!-- chunk {"id": "body-0066", "role": "body", "section": "VOC 2007 Error Analysis", "weight": 1.0} -->

Similar: class is similar, $\text{IOU} >.1$

<!-- chunk {"id": "body-0067", "role": "body", "section": "VOC 2007 Error Analysis", "weight": 1.0} -->

Other: class is wrong, $\text{IOU} >.1$

<!-- chunk {"id": "body-0068", "role": "body", "section": "VOC 2007 Error Analysis", "weight": 1.0} -->

Background: $\text{IOU} <.1$ for any object

<!-- chunk {"id": "body-0069", "role": "body", "section": "VOC 2007 Error Analysis", "weight": 1.0} -->

YOLO struggles to localize objects correctly. Localization errors account for more of YOLO's errors than all other sources combined. Fast R-CNN makes much fewer localization errors but far more background errors. 13.6% of it's top detections are false positives that don't contain any objects. Fast R-CNN is almost 3x more likely to predict background detections than YOLO.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Combining Fast R-CNN and YOLO", "weight": 1.0} -->

YOLO makes far fewer background mistakes than Fast R-CNN. By using YOLO to eliminate background detections from Fast R-CNN we get a significant boost in performance. For every bounding box that R-CNN predicts we check to see if YOLO predicts a similar box. If it does, we give that prediction a boost based on the probability predicted by YOLO and the overlap between the two boxes.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Combining Fast R-CNN and YOLO", "weight": 1.0} -->

The best Fast R-CNN model achieves a mAP of 71.8% on the VOC 2007 test set. When combined with YOLO, its mAP increases by 3.2% to 75.0%. We also tried combining the top Fast R-CNN model with several other versions of Fast R-CNN. Those ensembles produced small increases in mAP between.3 and.6%, see Table 2 for details.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Combining Fast R-CNN and YOLO", "weight": 1.0} -->

The boost from YOLO is not simply a byproduct of model ensembling since there is little benefit from combining different versions of Fast R-CNN. Rather, it is precisely because YOLO makes different kinds of mistakes at test time that it is so effective at boosting Fast R-CNN's performance.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Combining Fast R-CNN and YOLO", "weight": 1.0} -->

Unfortunately, this combination doesn't benefit from the speed of YOLO since we run each model seperately and then combine the results. However, since YOLO is so fast it doesn't add any significant computational time compared to Fast R-CNN.

<!-- chunk {"id": "body-0074", "role": "body", "section": "VOC 2012 Results", "weight": 1.0} -->

On the VOC 2012 test set, YOLO scores 57.9% mAP. This is lower than the current state of the art, closer to the original R-CNN using VGG-16, see Table 3. Our system struggles with small objects compared to its closest competitors. On categories like bottle, sheep, and tv/monitor YOLO scores 8-10% lower than R-CNN or Feature Edit. However, on other categories like cat and train YOLO achieves higher performance.

<!-- chunk {"id": "body-0075", "role": "body", "section": "VOC 2012 Results", "weight": 1.0} -->

Our combined Fast R-CNN + YOLO model is one of the highest performing detection methods. Fast R-CNN gets a 2.3% improvement from the combination with YOLO, boosting it 5 spots up on the public leaderboard.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Generalizability: Person Detection in Artwork", "weight": 1.0} -->

(b) Quantitative results on the VOC 2007, Picasso, and People-Art Datasets. The Picasso Dataset evaluates on both AP and best F1 score.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Generalizability: Person Detection in Artwork", "weight": 1.0} -->

Academic datasets for object detection draw the training and testing data from the same distribution. In real-world applications it is hard to predict all possible use cases and the test data can diverge from what the system has seen before. We compare YOLO to other detection systems on the Picasso Dataset and the People-Art Dataset, two datasets for testing person detection on artwork.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Generalizability: Person Detection in Artwork", "weight": 1.0} -->

R-CNN has high AP on VOC 2007. However, R-CNN drops off considerably when applied to artwork. R-CNN uses Selective Search for bounding box proposals which is tuned for natural images. The classifier step in R-CNN only sees small regions and needs good proposals.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Generalizability: Person Detection in Artwork", "weight": 1.0} -->

DPM maintains its AP well when applied to artwork. Prior work theorizes that DPM performs well because it has strong spatial models of the shape and layout of objects. Though DPM doesn't degrade as much as R-CNN, it starts from a lower AP.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Generalizability: Person Detection in Artwork", "weight": 1.0} -->

YOLO has good performance on VOC 2007 and its AP degrades less than other methods when applied to artwork. Like DPM, YOLO models the size and shape of objects, as well as relationships between objects and where objects commonly appear. Artwork and natural images are very different on a pixel level but they are similar in terms of the size and shape of objects, thus YOLO can still predict good bounding boxes and detections.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Real-Time Detection In The Wild", "weight": 1.0} -->

YOLO is a fast, accurate object detector, making it ideal for computer vision applications. We connect YOLO to a webcam and verify that it maintains real-time performance, including the time to fetch images from the camera and display the detections.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Real-Time Detection In The Wild", "weight": 1.0} -->

The resulting system is interactive and engaging. While YOLO processes images individually, when attached to a webcam it functions like a tracking system, detecting objects as they move around and change in appearance.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduce YOLO, a unified model for object detection. Our model is simple to construct and can be trained directly on full images. Unlike classifier-based approaches, YOLO is trained on a loss function that directly corresponds to detection performance and the entire model is trained jointly.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Fast YOLO is the fastest general-purpose object detector in the literature and YOLO pushes the state-of-the-art in real-time object detection. YOLO also generalizes well to new domains making it ideal for applications that rely on fast, robust object detection.
