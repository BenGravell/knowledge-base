WebGPT: Browser-assisted Question-answering with Human Feedback

We fine-tune GPT-3 to answer long-form questions using a text-based web-browsing environment, which allows the model to search and navigate the web. By setting up the task so that it can be performed by humans, we are able to train models on the task using imitation learning, and then optimize answer quality with human feedback. To make human evaluation of factual accuracy easier, models must collect references while browsing in support of their answers. We train and evaluate our models on ELI5, a dataset of questions asked by Reddit users. Our best model is obtained by fine-tuning GPT-3 using behavior cloning, and then performing rejection sampling against a reward model trained to predict human preferences. This model's answers are preferred by humans 56% of the time to those of our human demonstrators, and 69% of the time to the highest-voted answer from Reddit.

## Introduction

A rising challenge in NLP is long-form question-answering (LFQA), in which a paragraph-length answer is generated in response to an open-ended question. LFQA systems have the potential to become one of the main ways people learn about the world, but currently lag behind human performance. Existing work tends to focus on two core components of the task, information retrieval and synthesis.

In this work we leverage existing solutions to these components: we outsource document retrieval to the Microsoft Bing Web Search API,^11^1 and utilize unsupervised pre-training to achieve high-quality synthesis by fine-tuning GPT-3. Instead of trying to improve these ingredients, we focus on combining them using more faithful training objectives. Following Stiennon et al., we use human feedback to directly optimize answer quality, allowing us to achieve performance competitive with humans.

Why did we decide that certain words were ”bad” and shouldn’t be used in social settings?

We have all been taught that there are certain words that should not be used in public, at least not without good reason. But why do some words fall into this category while others do not? It turns out that there is not a single answer to this question, as each word has a different history and carries different meanings in different cultures and families. However, there are some general categories that ”bad” words tend to fall into. ”Bad” words generally relate to parts of life that we don’t like talking about in public, like bathroom functions, or negative ways of talking about people’s religion, skin color, ability, or gender....

In Section 6, we discuss the implications of our findings for training models to answer questions truthfully, and broader impacts.

(b) Corresponding text given to the model.

Scroll to the top of the page

We create a text-based web-browsing environment that a fine-tuned language model can interact with. This allows us to improve both retrieval and synthesis in an end-to-end fashion using general methods such as imitation learning and reinforcement learning.

We generate answers with references: passages extracted by the model from web pages while browsing. This is crucial for allowing labelers to judge the factual accuracy of answers, without engaging in a difficult and subjective process of independent research.
