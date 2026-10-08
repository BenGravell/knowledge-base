<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Identification for Predictive Control: A Multiple Model Approach

Topics include Model predictive control, System identification, Multiple models, Multistep prediction, Prediction error methods.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends predictive control to use separate models for different prediction horizons and studies identification procedures tuned to multistep prediction quality.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Predictive control relies on predictions of the future behaviour of the system to be controlled. These predictions are calculated from a model of this system, thus making the model the cornerstone of the predictive controller. Furthermore predictive control is the only advanced control methodology that has managed to become widely used in the industry. The necessity of good models in the predictive control context can thus be motivated both from the very nature of predictive control and from its widespread use in industry. This thesis is concerned with examining the use of multiple models in the predictive controller. In order to do this the standard predictive control formulation has been extended to incorporate the use of multiple models. The most general case of this new formulation allows the use of an individual model for each prediction horizon. The models are estimated using measurements of the input and output sequences from the true system. When using this data to find a good model of the system it is important to remember the intended purpose of the model. In this case the model is going to be used in a predictive controller and the most important feature of the models is to deliver good k-step ahead predictions. The identification algorithms used to estimate the models thus strives for estimating models good at calculating these predictions.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally this thesis presents some complete simulations of these ideas showing the potential of using multiple models in the predictive control framework.
