<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Rectifier Nonlinearities Improve Neural Network Acoustic Models

Topics include Activation functions, ReLU activations, Leaky ReLU, Acoustic models, Speech recognition, Neural networks, Sparse activations.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

This workshop paper helped popularize leaky rectified linear units by comparing standard rectifiers, leaky rectifiers, and sigmoidal activations in deep acoustic models. Its main evidence is that rectifier networks train well without pretraining on a large speech-recognition task and produce sparser, more dispersed hidden representations than tanh networks.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Deep neural network acoustic models produce substantial gains in large vocabulary continuous speech recognition systems. Emerging work with rectified linear (ReL) hidden units demonstrates additional gains in final system performance relative to more commonly used sigmoidal nonlinearities. In this work, we explore the use of deep rectifier networks as acoustic models for the 300 hour Switchboard conversational speech recognition task. Using simple training procedures without pretraining, networks with rectifier nonlinearities produce 2% absolute reductions in word error rates over their sigmoidal counterparts. We analyze hidden layer representations to quantify differences in how ReL units encode inputs as compared to sigmoidal units. Finally, we evaluate a variant of the ReL unit with a gradient more amenable to optimization in an attempt to further improve deep rectifier networks.
