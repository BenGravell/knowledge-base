<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Decoding by Linear Programming

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper considers the classical error correcting problem which is frequently discussed in coding theory. We wish to recover an input vector f in R^(n) from corrupted measurements y = A f + e. Here, A is an m by n (coding) matrix and e is an arbitrary and unknown vector of errors. Is it possible to recover f exactly from the data y? We prove that under suitable conditions on the coding matrix A, the input f is the unique solution to the l_1-minimization problem (|x|_l_1: = sum_i |x_i|) min_g in R^(n) | y - Ag |_l_1 provided that the support of the vector of errors is not too large, |e|_l_0: = |i: e_i != 0| <= rho* m for some rho > 0. In short, f can be recovered exactly by solving a simple convex optimization problem (which one can recast as a linear program). In addition, numerical experiments suggest that this recovery procedure works unreasonably well; f is recovered exactly even in situations where a significant fraction of the output is corrupted.
