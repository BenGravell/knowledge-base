<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Green AI

Topics include Green artificial intelligence, Sustainable artificial intelligence, Machine learning efficiency, Deep learning, Carbon footprint, Computational cost, Model evaluation, Energy efficiency, Research incentives, Artificial intelligence accessibility.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Schwartz, Dodge, Smith, and Etzioni introduce the Green AI framing, arguing that machine learning research should report and optimize computational efficiency rather than rewarding accuracy at any compute cost. The paper is influential because it gives the community a compact vocabulary for the environmental and equity costs of deep learning, and it helped make compute, energy, and financial cost routine considerations in later AI evaluation and reporting work.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The computations required for deep learning research have been doubling every few months, resulting in an estimated 300,000x increase from 2012 to 2018. These computations have a surprisingly large carbon footprint. Ironically, deep learning was inspired by the human brain, which is remarkably energy efficient. Moreover, the financial cost of the computations can make it difficult for academics, students, and researchers, in particular those from emerging economies, to engage in deep learning research. This position paper advocates a practical solution by making efficiency an evaluation criterion for research alongside accuracy and related measures. In addition, we propose reporting the financial cost or "price tag" of developing, training, and running models to provide baselines for the investigation of increasingly efficient methods. Our goal is to make AI both greener and more inclusive - enabling any inspired undergraduate with a laptop to write high-quality research papers.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction and Motivation", "weight": 1.5} -->

Since 2012, the field of artificial intelligence has reported remarkable progress on a broad range of capabilities including object recognition, game playing, machine translation, and more. This progress has been achieved by increasingly large and computationally-intensive deep learning models.^11^1For brevity, we refer to AI throughout this paper, but our focus is on AI research that relies on deep learning methods. Figure 1 reproduced from plots training cost increase over time for state-of-the-art deep learning models starting with AlexNet in 2012 to AlphaZero in 2017. The chart shows an overall increase of 300,000x, with training cost doubling every few months. An even sharper trend can be observed in NLP word embedding approaches by looking at ELMo followed by BERT, openGPT-2, and XLNet. An important paper has estimated the carbon footprint of several NLP models and argued that this trend is both environmentally unfriendly (which we refer to as Red AI) and expensive, raising barriers to participation in NLP research.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction and Motivation", "weight": 1.5} -->

This trend is driven by the strong focus of the AI community on obtaining "state-of-the-art" results,^22^2Meaning, in practice, that a system's accuracy on some benchmark is greater than any previously reported system's accuracy. as exemplified by the rising popularity of leaderboards, which typically report accuracy measures but omit any mention of cost or efficiency (see, for example, leaderboards.allenai.org). Despite the clear benefits of improving model accuracy in AI, the focus on this single metric ignores the economic, environmental, or social cost of reaching the reported accuracy.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction and Motivation", "weight": 1.5} -->

We advocate increasing research activity in Green AI\-\--AI research that is more environmentally friendly and inclusive. We emphasize that Red AI research has been yielding valuable contributions to the field of AI, but it's been overly dominant. We want to shift the balance towards the Green AI option\-\--to ensure that any inspired undergraduate with a laptop has the opportunity to write high-quality papers that could be accepted at premier research conferences. Specifically, we propose making efficiency a more common evaluation criterion for AI papers alongside accuracy and related measures.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction and Motivation", "weight": 1.5} -->

AI research can be computationally expensive in a number of ways, but each provides opportunities for efficient improvements; for example, papers could be required to plot accuracy as a function of computational cost and of training set size, providing a baseline for more data-efficient research in the future. Reporting the computational price tag of finding, training, and running models is a key Green AI practice (see Equation 2). In addition to providing transparency, price tags are baselines that other researchers could improve.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction and Motivation", "weight": 1.5} -->

Our empirical analysis in Figure 2 suggests that the AI research community has paid relatively little attention to computational efficiency. In fact, as Figure 1 illustrates, the computational cost of research is increasing exponentially, at a pace that far exceeds Moore's Law. Red AI is on the rise despite the well-known diminishing returns of increased cost (e.g., Figure 3). This paper identifies key factors that contribute to Red AI and advocates the introduction of a simple, easy-to-compute efficiency metric that could help make some AI research greener, more inclusive, and perhaps more cognitively plausible. Green AI is part of a broader, long-standing interest in environmentally-friendly scientific research (e.g., see the journal *Green Chemistry*). Computer science, in particular, has a long history of investigating sustainable and energy-efficient computing (e.g., see the journal *Sustainable Computing: Informatics and Systems*).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction and Motivation", "weight": 1.5} -->

The remainder of this paper is organized as follows. Section 2 analyzes practices that move deep-learning research into the realm of Red AI. Section 3 discusses our proposals for Green AI. Section 4 considers related work, and we conclude with a discussion of directions for future research.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Red AI", "weight": 1.0} -->

Red AI refers to AI research that seeks to obtain state-of-the-art results in accuracy (or related measures) through the use of massive computational power\-\--essentially ''buying\" stronger results. Yet the relationship between model performance and model complexity (measured as number of parameters or inference time) has long been understood to be at best logarithmic; for a linear gain in performance, an exponentially larger model is required. Similar trends exist with increasing the quantity of training data and the number of experiments. In each of these cases, diminishing returns come at increased computational cost.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Red AI", "weight": 1.0} -->

This section analyzes the factors contributing to Red AI and shows how it is resulting in diminishing returns over time (see Figure 3). We note again that Red AI work is valuable, and in fact, much of it contributes to what we know by pushing the boundaries of AI. Our exposition here is meant to highlight areas where computational expense is high, and to present each as an opportunity for developing more efficient techniques.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Red AI", "weight": 1.0} -->

To demonstrate the prevalence of Red AI, we sampled 60 papers from top AI conferences. For each paper we noted whether the authors claim their main contribution to be (a) an improvement to accuracy or some related measure, (b) an improvement to efficiency, (c) both, or (d) other. As shown in Figure 2, in all conferences we considered, a large majority of the papers target accuracy (90% of ACL papers, 80% of NeurIPS papers and 75% of CVPR papers). Moreover, for both empirical AI conferences (ACL and CVPR) only a small portion (10% and 20% respectively) argue for a new efficiency result.^66^6Interestingly, many NeurIPS papers included convergence rates or regret bounds which describe performance as a function of examples or iterations, thus targeting efficiency (55%). This indicates an increased awareness of the importance of this concept, at least in theoretical analyses. This highlights the focus of the AI community on measures of performance such as accuracy, at the expense of measures of efficiency such as speed or model size. In this paper we argue that a larger weight should be given to the latter.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Red AI", "weight": 1.0} -->

To better understand the different ways in which AI research can be red, consider an AI result reported in a scientific paper. This result typically includes a model trained on a training dataset and evaluated on a test dataset. The process of developing that model often involves multiple experiments to tune its hyperparameters. When considering the different factors that increase the computational and environmental cost of producing such a result, three factors come to mind: the cost of executing the model on a single ($E$)xample (either during training or at inference time); the size of the training ($D$)ataset, which controls the number of times the model is executed during training, and the number of ($H$)yperparameter experiments, which controls how many times the model is trained during model development. The total cost of producing a ($R$)esult in machine learning increases linearly with each of these quantities.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Red AI", "weight": 1.0} -->

\[h\] $${Cost(R)} \propto {E \cdot D \cdot H}$$ The equation of Red AI: The cost of an AI ($R$)esult grows linearly with the cost of processing a single ($E$)xample, the size of the training ($D$)ataset and the number of ($H$)yperparameter experiments.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Red AI", "weight": 1.0} -->

Equation 2 is a simplification (e.g., different hyperparameter assignments can lead to different costs for processing a single example). It also ignores other factors such as the number of training epochs. Nonetheless, it illustrates three quantities that are each an important factor in the total cost of generating a result. Below, we consider each quantity separately.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Expensive processing of one example", "weight": 1.0} -->

Our focus is on neural models, where it is common for each training step to require inference, so we discuss training and inference cost together as ''processing'' an example. Some works have used increasingly expensive models which require great amounts of resources, and as a result, in these models, performing inference can require a lot of computation, and training even more so. For instance, Google's BERT-large contains roughly 350 million parameters. openAI's openGPT2-XL model contains 1.5 billion parameters. AI2, our home organization, recently released Grover, also containing 1.5 billion parameters. In the computer vision community, a similar trend is observed (Figure 1).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Expensive processing of one example", "weight": 1.0} -->

Such large models have high costs for processing each example, which leads to large training costs. BERT-large was trained on 64 TPU chips for 4 days. Grover was trained on 256 TPU chips for two weeks, at an estimated cost of \$25,000. XLNet had a similar architecture to BERT-large, but used a more expensive objective function (in addition to an order of magnitude more data), and was trained on 512 TPU chips for 2.5 days.^77^7Some estimates for the cost of this process reach \$250,000 (twitter.com/eturner303/status/1143174828804857856). It is impossible to reproduce the best BERT-large results^88^8See or XLNet results^99^9See using a single GPU. Specialized models can have even more extreme costs, such as AlphaGo, the best version of which required 1,920 CPUs and 280 GPUs to play a single game of Go at a cost of over \$1,000 per hour.^1010^10Recent versions of AlphaGo are far more efficient.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Expensive processing of one example", "weight": 1.0} -->

When examining variants of a single model (e.g., BERT-small and BERT-large) we see that larger models can have stronger performance, which is a valuable scientific contribution. However, this implies the financial and environmental cost of increasingly large AI models will not decrease soon, as the pace of model growth far exceeds the resulting increase in model performance. As a result, more and more resources are going to be required to keep improving AI models by simply making them larger.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Processing many examples", "weight": 1.0} -->

Another way state-of-the-art performance has recently been progressing in AI is by successively increasing the amount of training data models are trained. BERT-large had top performance in 2018 across many NLP tasks after training on 3 billion word-pieces. XLNet recently outperformed BERT after training on 32 billion word-pieces, including part of Common Crawl; openGPT-2-XL trained on 40 billion words; FAIR's RoBERTa was trained on 160GB of text, roughly 40 billion word-pieces, requiring around 25,000 GPU hours to train. In computer vision, researchers from Facebook pretrained an image classification model on 3.5 billion images from Instagram, three orders of magnitude larger than existing labelled image datasets such as Open Images.^1111^11

<!-- chunk {"id": "body-0020", "role": "body", "section": "Processing many examples", "weight": 1.0} -->

The use of massive data creates barriers for many researchers for reproducing the results of these models, or training their own models on the same setup (especially as training for multiple epochs is standard). For example, the June 2019 Common Crawl contains 242 TB of uncompressed data,^1212^12[ so even storing the data is expensive. Finally, as in the case of model size, relying on more data to improve performance is notoriously expensive because of the diminishing return of adding more data. For instance, Figure 3, taken, shows a logarithmic relation between the object recognition top-1 accuracy and the number of training examples.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Massive number of experiments", "weight": 1.0} -->

Some projects have poured large amounts of computation into tuning hyperparameters or searching over neural architectures, well beyond the reach of most researchers. For instance, researchers from Google trained over 12,800 neural networks in their neural architecture search to improve performance on object detection and language modeling. With a fixed architecture, researchers from DeepMind evaluated 1,500 hyperparameter assignments to demonstrate that an LSTM language model can reach state-of-the-art perplexity results. Despite the value of this result in showing that the performance of an LSTM does not plateau after only a few hyperparameter trials, fully exploring the potential of other competitive models for a fair comparison is prohibitively expensive.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Massive number of experiments", "weight": 1.0} -->

The topic of massive number of experiments is not as well studied as the first two discussed above. In fact, the number of experiments performed during model construction is often underreported. Nonetheless, evidence for a logarithmic relation exists here as well, between the number of experiments and performance gains.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Discussion", "weight": 1.5} -->

The benefits of pouring more resources into models are certainly of interest to the AI community. Indeed, there is value in pushing the limits of model size, dataset size, and the hyperparameter search space. Currently, despite the massive amount of resources put into recent AI models, such investment still pays off in terms of downstream performance (albeit at an increasingly lower rate). Finding the point of saturation (if such exists) is an important question for the future of AI.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our goal in this paper is to raise awareness of the cost of Red AI, as well as encourage the AI community to recognize the value of work by researchers that take a different path, optimizing efficiency rather than accuracy. Next we turn to discuss concrete measures for making AI more green.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Green AI", "weight": 1.0} -->

The term Green AI refers to AI research that yields novel results without increasing computational cost, and ideally reducing it. Whereas Red AI has resulted in rapidly escalating computational (and thus carbon) costs, Green AI has the opposite effect. If measures of efficiency are widely accepted as important evaluation metrics for research alongside accuracy, then researchers will have the option of focusing on the efficiency of their models with positive impact on both the environment and inclusiveness. This section reviews several measures of efficiency that could be reported and optimized, and advocates one particular measure\-\--FPO\-\--which we argue should be reported when AI research findings are published.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Measures of Efficiency", "weight": 1.0} -->

To measure efficiency, we suggest reporting the amount of work required to generate a result in AI, that is, the amount of work required to train a model, and if applicable, the sum of works for all hyperparameter tuning experiments. As the cost of an experiment decomposes into the cost of a processing a single example, the size of the dataset, and the number of experiments (Equation 2), reducing the amount of work in each of these steps will result in AI that is more green.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Measures of Efficiency", "weight": 1.0} -->

When reporting the amount of work done by a model, we want to measure a quantity that allows for a fair comparison between different models. As a result, this measure should ideally be stable across different labs, at different times, and using different hardware.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Carbon emission", "weight": 1.0} -->

Carbon emission is appealing as it is a quantity we want to directly minimize. Nonetheless it is impractical to measure the exact amount of carbon released by training or executing a model, and accordingly\-\--generating an AI result, as this amount depends highly on the local electricity infrastructure. As a result, it is not comparable between researchers in different locations or even the same location at different times.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Electricity usage", "weight": 1.0} -->

Electricity usage is correlated with carbon emission while being time- and location-agnostic. Moreover, GPUs often report the amount of electricity each of their cores consume at each time point, which facilitates the estimation of the total amount of electricity consumed by generating an AI result. Nonetheless, this measure is hardware dependent, and as a result does not allow for a fair comparison between different models.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Elapsed real time", "weight": 1.0} -->

The total running time for generating an AI result is a natural measure for efficiency, as all other things being equal, a faster model is doing less computational work. Nonetheless, this measure is highly influenced by factors such as the underlying hardware, other jobs running on the same machine, and the number of cores used. These factors hinder the comparison between different models, as well as the decoupling of modeling contributions from hardware improvements.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Number of parameters", "weight": 1.0} -->

Another common measure of efficiency is the number of parameters (learnable or total) used by the model. As with run time, this measure is correlated with the amount of work. Unlike the other measures described above, it does not depend on the underlying hardware. Moreover, this measure also highly correlates with the amount of memory consumed by the model. Nonetheless, different algorithms make different use of their parameters, for instance by making the model deeper vs. wider. As a result, different models with a similar number of parameters often perform different amounts of work.

<!-- chunk {"id": "body-0032", "role": "body", "section": "FPO", "weight": 1.0} -->

As a concrete measure, we suggest reporting the total number of floating point operations (FPO) required to generate a result.^1313^13Floating point operations are often referred to as FLOP(s), though this term is not uniquely defined. To avoid confusion, we use the term FPO. FPO provides an estimate to the amount of work performed by a computational process. It is computed analytically by defining a cost to two base operations, add and mul. Based on these operations, the FPO cost of any machine learning abstract operation (e.g., a tanh operation, a matrix multiplication, a convolution operation, or the BERT model) can be computed as a recursive function of these two operations. FPO has been used in the past to quantify the energy footprint of a model, but is not widely adopted in AI.

<!-- chunk {"id": "body-0033", "role": "body", "section": "FPO", "weight": 1.0} -->

FPO has several appealing properties. First, it directly computes the amount of work done by the running machine when executing a specific instance of a model, and is thus tied to the amount of energy consumed. Second, FPO is agnostic to the hardware on which the model is run. This facilitates fair comparisons between different approaches, unlike the measures described above. Third, FPO is strongly correlated with the running time of the model. Unlike asymptotic runtime, FPO also considers the amount of work done at each time step.

<!-- chunk {"id": "body-0034", "role": "body", "section": "FPO", "weight": 1.0} -->

Several packages exist for computing FPO in various neural network libraries,^1414^14E.g., though none of them contains all the building blocks required to construct all modern AI models. We encourage the builders of neural network libraries to implement such functionality directly.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Discussion", "weight": 1.5} -->

Efficient machine learning approaches have received attention in the research community, but are generally not motivated by being green. For example, a significant amount of work in the computer vision community has addressed efficient inference, which is necessary for real-time processing of images for applications like self-driving cars, or for placing models on devices such as mobile phones. Most of these approaches target efficient model inference,^1515^15Some very recent work also targeted efficient training. and thus only minimize the cost of processing a single example, while ignoring the other two red practices discussed in Section 2.^1616^16In fact, creating smaller models often results in longer running time, so mitigating the different trends might be at odds.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Discussion", "weight": 1.5} -->

The above examples indicate that the path to making AI green depends on how it is used. When developing a new model, much of the research process involves training many model variants on a training set and performing inference on a small development set. In such a setting, more efficient training procedures can lead to greater savings, while in a production setting more efficient inference can be more important. We advocate for a holistic view of computational savings which doesn't sacrifice in some areas to make advances in others.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Discussion", "weight": 1.5} -->

FPO has some limitations. First, it targets the electricity consumption of a model, while ignoring other potential limiting factors for researchers such as the memory consumption by the model, which can often lead to additional energy and monetary costs. Second, the amount of work done by a model largely depends on the *model implementation*, as two different implementations of the same model could result in very different amounts of processing work. Due to the focus on the modeling contribution, the AI community has traditionally ignored the quality or efficiency of models' implementation.^1717^17We consider this exclusive focus on the final prediction another symptom of Red AI. We argue that the time to reverse this norm has come, and that exceptionally good implementations that lead to efficient models should be credited by the AI community.

<!-- chunk {"id": "body-0038", "role": "body", "section": "FPO Cost of Existing Models", "weight": 1.0} -->

(b) Different layers of the ResNet model.

<!-- chunk {"id": "body-0039", "role": "body", "section": "FPO Cost of Existing Models", "weight": 1.0} -->

To demonstrate the importance of reporting the amount of work, we present FPO costs for several existing models.^1818^18These numbers represent FPO per inference, i.e., the work required to process a single example. Figure 4a shows the number of parameters and FPO of several leading object recognition models, as well as their performance on the ImageNet dataset.^1919^19Numbers taken from A few trends are observable. First, as discussed in Section 2, models get more expensive with time, but the increase in FPO does not lead to similar performance gains. For instance, an increase of almost 35% in FPO between ResNet and ResNext (second and third points in graph) resulted in a 0.5% top-1 accuracy improvement. Similar patterns are observed when considering the effect of other increases in model work. Second, the number of model parameters does not tell the whole story: AlexNet (first point in the graph) actually has more parameters than ResNet (second point), but dramatically less FPO, and also much lower accuracy.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Additional Ways to Promote Green AI", "weight": 1.0} -->

In addition to reporting the FPO cost of the final reported number, we encourage researchers to report the budget/accuracy curve observed during training. In a recent paper, we observed that selecting the better performing model on a given task depends highly on the amount of compute available during model development. We introduced a method for computing the expected best validation performance of a model as a function of the given budget. We argue that reporting this curve will allow users to make wiser decisions about their selection of models and highlight the stability of different approaches.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Additional Ways to Promote Green AI", "weight": 1.0} -->

We further advocate for making efficiency an official contribution in major AI conferences, by advising reviewers to recognize and value contributions that do not strictly improve state of the art, but have other benefits such as efficiency. Finally, we note that the trend of releasing pretrained models publicly is a green success, and we would like to encourage organizations to continue to release their models in order to save others the costs of retraining them.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The vision of Green AI raises many exciting research directions that help to overcome the inclusiveness challenges of Red AI. Progress will reduce the computational expense with a minimal reduction in performance, or even improve performance as more efficient methods are discovered. Also, it would seem that Green AI could be moving us in a more cognitively plausible direction as the brain is highly efficient.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

It's important to reiterate that we see Green AI as a valuable option not an exclusive mandate\-\--of course, both Green AI and Red AI have contributions to make. We want to increase the prevalence of Green AI by highlighting its benefits, advocating a standard measure of efficiency. Below, we point to a few important green research directions, and highlight a few open questions.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Research on building space or time efficient models is often motivated by fitting a model on a small device (such as a phone) or fast enough to process examples in real time, such as image captioning for the blind (see Section 3.1). Some modern models don't even fit on a single GPU (see Section 2). Here we argue for a far broader approach.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Data efficiency has received significant attention over the years. Modern research in vision and NLP often involves first pretraining a model on large ''raw'' (unannotated) data then fine-tuning it to a task of interest through supervised learning. A strong result in this area often involves achieving similar performance to a baseline with fewer training examples or fewer gradient steps. Most recent work has addressed fine-tuning data, but pretraining efficiency is also important. In either case, one simple technique to improve in this area is to simply report performance with different amounts of training data. For example, reporting performance of contextual embedding models trained on 10 million, 100 million, 1 billion, and 10 billion tokens would facilitate faster development of new models, as they can first be compared at the smallest data sizes. Research here is of value not just to make training less expensive, but because in areas such as low resource languages or historical domains it is extremely hard to generate more data, so to progress we must make more efficient use of what is available.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Finally, the total number of experiments run to get a final result is often underreported and underdiscussed. The few instances researchers have of full reporting of the hyperparameter search, architecture evaluations, and ablations that went into a reported experimental result have surprised the community. While many hyperparameter optimization algorithms exist which can reduce the computational expense required to reach a given level of performance, simple improvements here can have a large impact. For example, stopping training early for models which are clearly underperforming can lead to great savings.
