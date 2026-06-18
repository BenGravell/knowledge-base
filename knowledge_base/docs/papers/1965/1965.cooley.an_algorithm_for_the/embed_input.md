<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Algorithm for the Machine Calculation of Complex Fourier Series

Topics include Fast fourier transform, Cooley-Tukey algorithm, Fourier series, Numerical algorithms, Signal processing, Divide and conquer, In-place computation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Cooley and Tukey present the fast Fourier transform algorithm for computing complex Fourier series in O(N log N) operations when the number of points has a suitable factorization. The paper made Fourier methods computationally practical at scale and became one of the defining examples of algorithmic speedup through factorization and divide-and-conquer structure.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

An efficient method for the calculation of the interactions of a 2m factorial experiment was introduced by Yates and is widely known by his name.The generalization to 3m was given by Box et al..Good generalized these methods and gave elegant algorithms for which one class of applications is the calculation of Fourier series.In their full generality, Good's methods are applicable to certain problems in which one must multiply an JV-vector by an JV X N matrix which can be factored into m sparse matrices, where m is proportional to log JV.This results in a procedure requiring a number of operations proportional to JV log JV rather than JV2.These methods are applied here to the calculation of complex Fourier series.They are useful in situations where the number of data points is, or can be chosen to be, a highly composite number.The algorithm is here derived and presented in a rather different form.Attention is given to the choice of JV.It is also shown how special advantage can be obtained in the use of a binary computer with JV = 2m and how the entire calculation can be performed within the array of JV data storage locations used for the given Fourier coefficients.Consider the problem of calculating the complex Fourier

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

series
