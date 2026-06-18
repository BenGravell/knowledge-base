BERTopic: Neural Topic Modeling with a Class-based TF-IDF Procedure

Topics include Transformers, Language models, Clustering, Benchmarks, BERTopic, Topic model, Tf-idf, Topic modeling.

Topic models can be useful tools to discover latent topics in collections of documents. Recent studies have shown the feasibility of approach topic modeling as a clustering task. We present BERTopic, a topic model that extends this process by extracting coherent topic representation through the development of a class-based variation of TF-IDF. More specifically, BERTopic generates document embedding with pre-trained transformer-based language models, clusters these embeddings, and finally, generates topic representations with the class-based TF-IDF procedure. BERTopic generates coherent topics and remains competitive across a variety of benchmarks involving classical models and those that follow the more recent clustering approach of topic modeling.

## Introduction

To uncover common themes and the underlying narrative in text, topic models have proven to be a powerful unsupervised tool. Conventional models, such as Latent Dirichlet Allocation (LDA) and Non-Negative Matrix Factorization (NMF), describe a document as a bag-of-words and model each document as a mixture of latent topics.

One limitation of these models is that through bag-of-words representations, they disregard semantic relationships among words. As these representations do not account for the context of words in a sentence, the bag-of-words input may fail to accurately represent documents.

In this paper, we introduce BERTopic, a topic model that leverages clustering techniques and a class-based variation of TF-IDF to generate coherent topic representations. More specifically, we first create document embeddings using a pre-trained language model to obtain document-level information. Second, we first reduce the dimensionality of document embeddings before creating semantically similar clusters of documents that each represent a distinct topic. Third, to overcome the centroid-based perspective, we develop a class-based version of TF-IDF to extract the topic representation from each topic.

## Discussion

Although we attempted to validate BERTopic across several experiments, topic modeling techniques can be validated through many other evaluation metrics, such as metrics for unsupervised and supervised modeling performance. Moreover, topic modeling techniques can be used across a variety of use cases, many of which are not covered in this study. For those reasons, we additionally discuss the strengths and weaknesses of BERTopic to further describe when, and perhaps most importantly, when not to use BERTopic.

## Conclusion

We developed BERTopic, a topic model that extends the cluster embedding approach by leveraging state-of-the-art language models and applying a class-based TF-IDF procedure for generating topic representations. By separating the process of clustering documents and generating topic representations, significant flexibility is introduced in the model allowing for ease of usability.
