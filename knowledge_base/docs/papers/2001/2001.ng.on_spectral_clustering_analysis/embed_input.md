<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On Spectral Clustering: Analysis and an Algorithm

Topics include Spectral clustering, Graph laplacians, Eigenvectors, Matrix perturbation, Clustering, Machine learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents a simple spectral clustering algorithm based on eigenvectors of an affinity-derived matrix and analyzes conditions under which it recovers meaningful clusters. The paper helped standardize the normalized spectral clustering recipe and connected its empirical success to matrix perturbation arguments.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Despite many empirical successes of spectral clustering methods - algorithms that cluster points using eigenvectors of matrices derived from the data - there are several unresolved issues. First, there are a wide variety of algorithms that use the eigenvectors in slightly different ways. Second, many of these algorithms have no proof that they will actually compute a reasonable clustering. In this paper, we present a simple spectral clustering algorithm that can be implemented using a few lines of Matlab. Using tools from matrix perturbation theory, we analyze the algorithm, and give conditions under which it can be expected to do well. We also show surprisingly good experimental results on a number of challenging clustering problems.
