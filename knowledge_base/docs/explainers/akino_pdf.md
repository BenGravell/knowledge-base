# AkinoPDF

This is my personal write-up of "Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness" by Duong, Ramsey, Kingston, Thomason, Kavraki (2026).

For more details, refer to the [site page for arXiv:2603.16059](../papers/2603_16059.md)

## Intro

The paper brings together two of my favorite concepts in motion planning: sampling-based trajectory planning and differentially flat systems. They also massage things (trajectory generation + collision/constraint checking) into a SIMD-amenable implementation which can give huge speedups on CPU-based hardware.

If you are not familiar with differential flatness, read these [grad school-level introductory notes by Marin Kobilarov](https://asco.lcsr.jhu.edu/docs/EN530_678_S2022/lectures/lecture6.pdf)

## Takeaways

### Takeaway 1: Planning in flat space is better than planning in the original space

See Algorithm 1.

### Takeaway 2: Steering in flat space is easy

See Algorithm 2.

I recommend starting with Section V. b) Example 4, which is a nice little self-contained steering method for differentially flat systems whose that only need up to second-order derivatives of flat outputs (includes unicycle dynamics) and a cost function that is quadratic in the control effort and linear in the duration. The main takeaway is that the optimal flat outputs are cubic polynomials of time, full stop. The optimal duration is computable by solving for the roots of a cubic polynomial - and why is that amazing and very lucky/cutting it close? Because quartic polynomials are the highest degree polynomials that admit closed-form solutions (which is a well-known fact c.f. [Abel–Ruffini theorem - Wikipedia](https://en.wikipedia.org/wiki/Abel%E2%80%93Ruffini_theorem))! That means that if the dynamics included one more higher derivative of the flat outputs (third order derivatives), we would end up needing to solve for roots of a polynomial numerically, which is far more expensive and less robust.

### Takeaway 3: Batch the collision & constraint checks and run them way faster using SIMD instructions

See Algorithm 3.

### Takeaway 4: Having a "complete" steering method that respects the actuation constraints is not necessary

The authors do not spend much time elaborating, so it can go unnoticed easily. But they are happy to reject lots of steering method output trajectories during tree expansion if they violate actuations constraints like velocity, acceleration, jerk. This is a "dumb" strategy that can greatly reduce sampling efficiency, but if the rest of the planner is strong and fast enough to overcome it, who cares?

See Line 5 of Algorithm 3.

### Takeaway 5: GPU is not necessary

You will notice that all the experiments are on commodity workstation CPUs. This is consistent with other modern state-of-the-art work on motion planning e.g. [judo](https://github.com/rai-opensource/judo) that also relies completely on CPU-based parallelization (although judo is thread-level / coarse-grained, compared to fine-grained SIMD parallelization in the OP paper). I think it is worth meditating on this, as we do not necessarily need to go all in on GPU for motion planning, especially in the classical / physics / model-based paradigm.

## Parting thoughts

There is no code available from this paper yet sadly. Hopefully we will see it in OMPL soon 🤞
