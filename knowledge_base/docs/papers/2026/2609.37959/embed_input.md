<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

TabFM: A Zero-Shot Foundation Model for Tabular Data

Topics include Tabular learning, Foundation models, In-context learning, Synthetic data, Classification, Regression.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces a tabular foundation model trained on synthetic causal datasets for zero-shot classification and regression. Evaluates frozen-model ensembling, calibration, and language-model-guided preprocessing extensions.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Tabular machine learning typically relies on per-dataset workflows, fitting tree ensembles or running AutoML searches from scratch for every task. We present TabFM, a 400M-parameter tabular foundation model that formulates supervised tabular prediction as in-context learning. TabFM produces calibrated zero-shot predictions in a single forward pass without task-specific tuning. Trained entirely on synthetic tables generated from structural causal models, TabFM learns general tabular representations that transfer zero-shot to real-world tasks. Across all 51 benchmark datasets in TabArena (38 classification and 13 regression), zero-shot TabFM ranks first among default tabular foundation models and outperforms tuned AutoML pipelines. Two extensions over the same frozen weights improve performance further on both tracks: multi-view feature expansion with ensembling and post-hoc calibration (TabFM+), and LLM-guided, dataset-specific data processing and feature engineering (TabFM-Auto).
