<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

WebGPT: Browser-assisted Question-answering with Human Feedback

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We fine-tune GPT-3 to answer long-form questions using a text-based web-browsing environment, which allows the model to search and navigate the web. By setting up the task so that it can be performed by humans, we are able to train models on the task using imitation learning, and then optimize answer quality with human feedback. To make human evaluation of factual accuracy easier, models must collect references while browsing in support of their answers. We train and evaluate our models on ELI5, a dataset of questions asked by Reddit users. Our best model is obtained by fine-tuning GPT-3 using behavior cloning, and then performing rejection sampling against a reward model trained to predict human preferences. This model's answers are preferred by humans 56% of the time to those of our human demonstrators, and 69% of the time to the highest-voted answer from Reddit.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A rising challenge in NLP is long-form question-answering (LFQA), in which a paragraph-length answer is generated in response to an open-ended question. LFQA systems have the potential to become one of the main ways people learn about the world, but currently lag behind human performance. Existing work tends to focus on two core components of the task, information retrieval and synthesis.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work we leverage existing solutions to these components: we outsource document retrieval to the Microsoft Bing Web Search API,^11^1 and utilize unsupervised pre-training to achieve high-quality synthesis by fine-tuning GPT-3. Instead of trying to improve these ingredients, we focus on combining them using more faithful training objectives. Following Stiennon et al., we use human feedback to directly optimize answer quality, allowing us to achieve performance competitive with humans.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We create a text-based web-browsing environment that a fine-tuned language model can interact. This allows us to improve both retrieval and synthesis in an end-to-end fashion using general methods such as imitation learning and reinforcement learning.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We generate answers with references: passages extracted by the model from web pages while browsing. This is crucial for allowing labelers to judge the factual accuracy of answers, without engaging in a difficult and subjective process of independent research.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our models are trained primarily to answer questions from ELI5, a dataset of questions taken from the "Explain Like I'm Five" subreddit. We collect two additional kinds of data: demonstrations of humans using our web-browsing environment to answer questions, and comparisons between two model-generated answers to the same question (each with their own set of references). Answers are judged for their factual accuracy, coherence, and overall usefulness.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We use this data in four main ways: behavior cloning (i.e., supervised fine-tuning) using the demonstrations, reward modeling using the comparisons, reinforcement learning against the reward model, and rejection sampling against the reward model. Our best model uses a combination of behavior cloning and rejection sampling. We also find reinforcement learning to provide some benefit when inference-time compute is more limited.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate our best model in three different ways. First, we compare our model's answers to answers written by our human demonstrators on a held-out set of questions. Our model's answers are preferred 56% of the time, demonstrating human-level usage of the text-based browser. Second, we compare our model's answers (with references stripped, for fairness) to the highest-voted answer provided by the ELI5 dataset. Our model's answers are preferred 69% of the time. Third, we evaluate our model on TruthfulQA, an adversarial dataset of short-form questions. Our model's answers are true 75% of the time, and are both true and informative 54% of the time, outperforming our base model (GPT-3), but falling short of human performance.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

(a) Screenshot from the demonstration interface.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

How can I train the crows in my neighborhood to bring me gifts?

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

From Gifts From Crows | Outside My Window (www.birdsoutsidemywindow.org)
&gt; Many animals give gifts to members of their own species but crows and
other corvids are the only ones known to give gifts to humans.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Search how to train crows to bring you gifts
Click Gifts From Crows | Outside My Window www.birdsoutsidemywindow.org

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Search results: how to train crows to bring you gifts

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

0How to Make Friends With Crows - PetHelpfulpethelpful.com
If you did this a few times, your crows would learn your new place, but
as I said, I’m not sure if they will follow or visit you there since it’s
probably not in their territory. The other option is simply to make new
crow friends with the crows that live in your new neighborhood.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

1Gifts From Crows | Outside My Windowwww.birdsoutsidemywindow.org
The partial piece of apple may have been left behind when the crow was
startled rather than as a gift. If the crows bring bright objects youll
know for sure that its a gift because its not something they eat.
Brandi Williams says: May 28, 2020 at 7:19 am.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

(b) Corresponding text given to the model.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 2, we describe our text-based web-browsing environment and how our models interact with it.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 3, we explain our data collection and training methods in more detail.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 4, we evaluate our best-performing models (for different inference-time compute budgets) on ELI5 and TruthfulQA.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 5, we provide experimental results comparing our different methods and how they scale with dataset size, parameter count, and inference-time compute.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 6, we discuss the implications of our findings for training models to answer questions truthfully, and broader impacts.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Environment design", "weight": 1.0} -->

Previous work on question-answering such as REALM and RAG has focused on improving document retrieval for a given query. Instead, we use a familiar existing method for this: a modern search engine (Bing). This has two main advantages. First, modern search engines are already very powerful, and index a large number of up-to-date documents. Second, it allows us to focus on the higher-level task of using a search engine to answer questions, something that humans can do well, and that a language model can mimic.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Environment design", "weight": 1.0} -->

For this approach, we designed a text-based web-browsing environment. The language model is prompted with a written summary of the current state of the environment, including the question, the text of the current page at the current cursor location, and some other information (see Figure 1(1(b))). In response to this, the model must issue one of the commands given in Table 1, which performs an action such as running a Bing search, clicking on a link, or scrolling around. This process is then repeated with a fresh context (hence, the only memory of previous steps is what is recorded in the summary).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Environment design", "weight": 1.0} -->

Send &lt;query&gt; to the Bing API and display a search results page

<!-- chunk {"id": "body-0026", "role": "body", "section": "Environment design", "weight": 1.0} -->

Clicked on link &lt;link ID&gt;
Follow the link with the given ID to a new page

<!-- chunk {"id": "body-0027", "role": "body", "section": "Environment design", "weight": 1.0} -->

Find in page: &lt;text&gt;
Find the next occurrence of &lt;text&gt; and scroll to it

<!-- chunk {"id": "body-0028", "role": "body", "section": "Environment design", "weight": 1.0} -->

If &lt;text&gt; is found in the current page, add it as a reference

<!-- chunk {"id": "body-0029", "role": "body", "section": "Environment design", "weight": 1.0} -->

Scroll to the top of the page

<!-- chunk {"id": "body-0030", "role": "body", "section": "Environment design", "weight": 1.0} -->

End browsing and move to answering phase

<!-- chunk {"id": "body-0031", "role": "body", "section": "Environment design", "weight": 1.0} -->

End: &lt;Nonsense, Controversial&gt;
End browsing and skip answering phase

<!-- chunk {"id": "body-0032", "role": "body", "section": "Environment design", "weight": 1.0} -->

While the model is browsing, one of the actions it can take is to quote an extract from the current page. When this is performed, the page title, domain name and extract are recorded to be used later as a reference. Browsing then continues until either the model issues a command to end browsing, the maximum number of actions has been reached, or the maximum total length of references has been reached. At this point, as long as there is at least one reference, the model is prompted with the question and the references, and must compose its final answer.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Environment design", "weight": 1.0} -->

Further technical details about our environment can be found in Appendix A.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Data collection", "weight": 1.0} -->

Guidance from humans is central to our approach. A language model pre-trained on natural language would not be able to use our text-based browser, since it does not know the format of valid commands. We therefore collected examples of humans using the browser to answer questions, which we call demonstrations. However, training on demonstrations alone does not directly optimize answer quality, and is unlikely to lead far beyond human performance. We therefore collected pairs of model-generated answers to the same question, and asked humans which one they preferred, which we call comparisons.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Data collection", "weight": 1.0} -->

For both demonstrations and comparisons, the vast majority of questions were taken from ELI5, a dataset of long-form questions. For diversity and experimentation, we also mixed in a small number of questions from other sources, such as TriviaQA. In total, we collected around 6,000 demonstrations, 92% of which were for questions from ELI5, and around 21,500 comparisons, 98% of which were for questions from ELI5. A more detailed breakdown of the questions we used along with post-processing details can be found in Appendix B.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Data collection", "weight": 1.0} -->

To make it easier for humans to provide demonstrations, we designed a graphical user interface for the environment (see Figure 1(1(a))). This displays essentially the same information as the text-based interface and allows any valid action to be performed, but is more human-friendly. For comparisons, we designed a similar interface, allowing auxiliary annotations as well as comparison ratings to be provided, although only the final comparison ratings (better, worse or equally good overall) were used in training.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Data collection", "weight": 1.0} -->

For both demonstrations and comparisons, we emphasized that answers should be relevant, coherent, and supported by trustworthy references. Further details about these criteria and other aspects of our data collection pipeline can be found in Appendix C.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Data collection", "weight": 1.0} -->

We are releasing a dataset of comparisons, the details of which can be found in Appendix K.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Data collection", "weight": 1.0} -->

Why did we decide that certain words were ”bad” and shouldn’t be used in social settings?

<!-- chunk {"id": "body-0040", "role": "body", "section": "Data collection", "weight": 1.0} -->

We have all been taught that there are certain words that should not be used in public, at least not without good reason. But why do some words fall into this category while others do not? It turns out that there is not a single answer to this question, as each word has a different history and carries different meanings in different cultures and families. However, there are some general categories that ”bad” words tend to fall into. ”Bad” words generally relate to parts of life that we don’t like talking about in public, like bathroom functions, or negative ways of talking about people’s religion, skin color, ability, or gender. Often, people say bad words when they are experiencing strong emotions, and those words are linked to our emotions.
