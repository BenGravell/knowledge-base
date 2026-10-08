<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Backpropagation Applied to Handwritten Zip Code Recognition

Topics include Convolutional neural network, Backpropagation, Handwritten digit recognition, Optical character recognition, Weight sharing, Local receptive fields, Supervised learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Demonstrates end-to-end handwritten digit recognition using a backpropagation network whose local receptive fields and shared weights encode spatial prior knowledge. The architecture learns directly from normalized U.S. Postal Service digit images and shows how task-specific constraints improve generalization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The ability of learning networks to generalize can be greatly enhanced by providing constraints from the task domain. This paper demonstrates how such constraints can be integrated into a backpropagation network through the architecture of the network. This approach has been successfully applied to the recognition of handwritten zip code digits provided by the U.S. Postal Service. A single network learns the entire recognition operation, going from the normalized image of the character to the final classification.
