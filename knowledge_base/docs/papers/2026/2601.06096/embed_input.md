The Hessian of Tall-skinny Networks Is Easy to Invert

Topics include Linear systems.

We describe an exact algorithm to solve linear systems of the form Hx = b where H is the Hessian of a deep net. The method computes Hessian-inverse-vector products without storing the Hessian or its inverse. It requires time and storage that scale linearly in the number of layers. This is in contrast to the naive approach of first computing the Hessian, then solving the linear system, which takes storage and time that are respectively quadratic and cubic in the number of layers. The Hessian-inverse-vector product method scales roughly like Pearlmutter's algorithm for computing Hessian-vector products.
