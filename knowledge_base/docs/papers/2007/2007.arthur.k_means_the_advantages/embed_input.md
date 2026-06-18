k-means++: The Advantages of Careful Seeding

Topics include Clustering, k-means, Initialization, Approximation algorithms, Randomized algorithms, Unsupervised learning.

Introduces k-means++, a randomized seeding strategy that samples new centers proportional to squared distance from existing centers. This small change gives an expected logarithmic approximation guarantee and usually improves both speed and final clustering quality in practice.

The k-means method is a widely used clustering technique that seeks to minimize the average squared distance between points in the same cluster. Although it offers no accuracy guarantees, its simplicity and speed are very appealing in practice. By augmenting k-means with a very simple, randomized seeding technique, we obtain an algorithm that is O(log k)-competitive with the optimal clustering. Preliminary experiments show that our augmentation improves both the speed and the accuracy of k-means, often quite dramatically.
