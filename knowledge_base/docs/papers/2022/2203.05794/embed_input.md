BERTopic: Neural Topic Modeling with a Class-based TF-IDF Procedure

Topics include Transformers, Language models, Clustering, Benchmarks, BERTopic, Topic model, Tf-idf, Topic modeling.

Topic models can be useful tools to discover latent topics in collections of documents. Recent studies have shown the feasibility of approach topic modeling as a clustering task. We present BERTopic, a topic model that extends this process by extracting coherent topic representation through the development of a class-based variation of TF-IDF. More specifically, BERTopic generates document embedding with pre-trained transformer-based language models, clusters these embeddings, and finally, generates topic representations with the class-based TF-IDF procedure. BERTopic generates coherent topics and remains competitive across a variety of benchmarks involving classical models and those that follow the more recent clustering approach of topic modeling.

## Introduction

To uncover common themes and the underlying narrative in text, topic models have proven to be a powerful unsupervised tool. Conventional models, such as Latent Dirichlet Allocation (LDA) and Non-Negative Matrix Factorization (NMF), describe a document as a bag-of-words and model each document as a mixture of latent topics.

One limitation of these models is that through bag-of-words representations, they disregard semantic relationships among words. As these representations do not account for the context of words in a sentence, the bag-of-words input may fail to accurately represent documents.

We developed BERTopic, a topic model that extends the cluster embedding approach by leveraging state-of-the-art language models and applying a class-based TF-IDF procedure for generating topic representations. By separating the process of clustering documents and generating topic representations, significant flexibility is introduced in the model allowing for ease of usability.

We present in this paper an in-depth analysis of BERTopic, ranging from evaluation studies with classical topic coherence measures to analyses involving running times. Our experiments suggest that BERTopic learns coherent patterns of language and demonstrates competitive and stable performance across a variety of tasks.

To represent more recent data in a short-text form, we collected all tweets of Trump^55^5 before and during his presidency. The data contains 44253 tweets, excluding re-tweets, between 2009 and 2021. In both datasets, we lowercased all tokens.

In BERTopic, we can model this behavior by leveraging the c-TF-IDF representations of topics. Here, we assume that the temporal nature of topics should not influence the creation of global topics. The same topic might appear across different times, albeit possibly represented differently. As an example, a global topic about cars might contain words such as \"car\" and \"vehicle\" regardless of the temporal nature of specific documents....

## Results

As an answer to this issue, text embedding techniques have rapidly become popular in the natural language processing field. More specifically, Bidirectional Encoder Representations from Transformers (BERT) and its variations, have shown great results in generating contextual word- and sentence vector representations....
