<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

BehaviorGPT at Work: A Foundation Model for Workforce Actions & Dynamics through Large Behavioral Modeling

Topics include Behavioral foundation models, Workforce dynamics, Employee attrition, Next-event prediction, Self-supervised learning, Transformers.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends BehaviorGPT to workforce data by modeling employee-employer interactions as chronological sequences of behavioral tokens. The article trains a Transformer on millions of workplace events, reports strong attrition-prediction performance, and argues that logged actions such as schedules, breaks, and productive hours can reveal organizational dynamics more reliably than surveys or top-down analytics, while also noting the ethical sensitivity of employee behavior modeling.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We applied language modeling techniques to detailed workforce behavioral data, creating BehaviorGPT-v2: a foundation model treating employee behaviors as a language to predict future actions and outcomes. We expand BehaviorGPT into a foundation model for understanding and predicting workforce behaviors and dynamics. We apply language modeling principles to employee and employer interactions by representing behaviors as sequences of tokens, effectively capturing the implicit “language” of workforce dynamics. Using this approach, our model achieves 91% accuracy (F1 score: 0.93) in predicting employee attrition (whether an employee would quit within the next month and why). This represents a substantial improvement over traditional data analyses and survey-based methods, which previously provided minimal predictive value, clearly demonstrating that actions speak louder than words. Our results suggest employee-employer interactions contain semantic structure akin to language, and thus can be modeled effectively. Specifically, we train a Transformer-based model variant on a dataset of approximately 43 million behavioral events involving 80,000 employees over a four-year period. Although dense embeddings were generated for visualization and analytical purposes, attrition predictions are performed directly through end-to-end modeling, analogous to predicting words in language models.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Crucially, BehaviorGPT is not specifically optimized for a particular downstream task, but rather trained with the guiding principle: “predicting what you will do, means understanding who you are.” Building upon our earlier consumption and transaction-focused work, we now model employers as “merchants” and employees as their “customers,” interpreting their interactions through this behavioral language. Highlights: • We demonstrate that workforce actions constitute a predictable implicit language, significantly outperforming traditional survey-based and analytic methods. • We achieve 91% accuracy in predicting whether employees would quit within the following month.
