A Cookbook of Self-Supervised Learning

Topics include Self-supervised learning, Supervised learning, Learning.

Self-supervised learning, dubbed the dark matter of intelligence, is a promising path to advance machine learning. Yet, much like cooking, training SSL methods is a delicate art with a high barrier to entry. While many components are familiar, successfully training a SSL method involves a dizzying set of choices from the pretext tasks to training hyper-parameters. Our goal is to lower the barrier to entry into SSL research by laying the foundations and latest SSL recipes in the style of a cookbook. We hope to empower the curious researcher to navigate the terrain of methods, understand the role of the various knobs, and gain the know-how required to explore how delicious SSL can be.

## What is Self-Supervised Learning and Why Bother?

Self-supervised learning, dubbed "the dark matter of intelligence" ^11^1 is a promising path to advance machine learning. As opposed to supervised learning, which is limited by the availability of labeled data, self-supervised approaches can learn from vast unlabeled data. Self-supervised learning (SSL) underpins deep learning's success in natural language processing leading to advances from automated machine translation to large language models trained on web-scale corpora of unlabeled text. In computer vision, SSL pushed new bounds on data size with models such as SEER trained on 1 billion images.

Self-supervised learning defines a pretext task based on unlabeled inputs to produce descriptive and intelligible representations. In natural language, a common SSL objective is to mask a word in the text and predict the surrounding words. This objective of predicting the context surrounding a word encourages the model to capture relationships among words in the text without the need for any labels. The same SSL model representations can be used across a range of downstream tasks such as translating text across languages, summarizing, or even generating text, along with many others.

With the power to train on vast unlabeled data comes many benefits. While traditional supervised learning methods are trained on a specific task often known a priori based on the available labeled data, SSL learns generic representations useful across many tasks. SSL can be especially useful in domains such as medicine where labels are costly or the specific task can not be known a priori. There's also evidence SSL models can learn representations that are more robust to adversarial examples, label corruption, and input perturbations---and are more fair---compared to their supervised counterparts.

## Conclusion

Self-supervised learning (SSL) established a new paradigm for advancing machine intelligence. Despite many successes, SSL remains a daunting field with a dizzying array of methods each with intricate implementations. Due to the fast moving research and the breadth of SSL methods, it remains a challenge to navigate the field. This becomes an issue for researchers and practitioners who joined the field only recently, in turn creating a high barrier to entry for SSL research and deployment.
