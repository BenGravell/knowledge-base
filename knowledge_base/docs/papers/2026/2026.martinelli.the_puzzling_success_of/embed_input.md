<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Puzzling Success of Overparameterization: Lottery Tickets or Escape Dimensions?

Topics include Overparameterization, Loss landscapes, Neural networks, Optimization, Lottery ticket hypothesis.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Argues that the geometry of wider neural-network loss landscapes, including additional escape directions from poor minima, better explains overparameterization than isolated lottery-ticket subnetworks.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Lotteries and tickets are often used as a didactical analogy to explain the success of overparameterized neural networks: “larger networks succeed because they more likely contain a well-initialized subnetwork that can learn the task in isolation, much like buying more tickets increases the chances of winning a lottery.” This explanation is intuitive but misleading: it suggests that subnetworks can be treated in isolation from the rest of the network. Following this reasoning leads to interpreting learning in wide networks as a multi-start optimization process, where gradient descent simply conducts a parallel search over subnetworks. We argue that this view is flawed since, among other reasons, winning tickets can be made to fail by perturbing the rest of the network. We put forward a more accurate intuitive picture for the success of overparameterization based on the geometry of loss landscapes: increasing width expands the set of available dimensions for optimization, making it easier to escape bad local minima. Moreover, as width grows, bad minima become increasingly rare relative to good minima.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

As the field grows mature, it is important to refine the analogies we use to explain foundational phenomena, such as the apparent redundancy of large networks, reconciling practitioners’ intuitions with modern theoretical insights.
