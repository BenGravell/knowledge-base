# Python

## Numerical & Scientific Computing

### Core Array & Math

- [NumPy](https://numpy.org/) - foundational N-dimensional array library; the lingua franca for numerical Python
- [SciPy](https://scipy.org/) - algorithms built on NumPy: optimization, integration, interpolation, signal processing, linear algebra, statistics
- [SymPy](https://www.sympy.org/) - symbolic mathematics (CAS) in pure Python

### DataFrames

- [Pandas](https://pandas.pydata.org/) - the classic DataFrame library; row-oriented, index-centric, mature ecosystem
- [Polars](https://pola.rs/) - fast DataFrame library written in Rust; lazy evaluation, Apache Arrow columnar memory, excellent for large datasets
- [cuDF](https://docs.rapids.ai/api/cudf/stable/) (RAPIDS) - GPU-accelerated DataFrames with a pandas-compatible API

### Linear Algebra & Array Backends

- [CuPy](https://cupy.dev/) - NumPy/SciPy-compatible array library running on CUDA GPUs
- [JAX](https://jax.readthedocs.io/) - NumPy on accelerators (CPU/GPU/TPU) with automatic differentiation and JIT via XLA; popular in ML research
- [Dask](https://dask.org/) - parallel and out-of-core computing; scales NumPy/Pandas workflows to clusters or large-memory machines

### Machine Learning & Deep Learning

- [scikit-learn](https://scikit-learn.org/) - classical ML: classification, regression, clustering, preprocessing, model selection
- [PyTorch](https://pytorch.org/) - dominant deep learning framework; dynamic graphs, strong research ecosystem
- [TensorFlow / Keras](https://www.tensorflow.org/) - production-oriented deep learning; Keras is its high-level API

### Visualization

- [Matplotlib](https://matplotlib.org/) - foundational plotting library; verbose but fully controllable
- [Seaborn](https://seaborn.pydata.org/) - statistical visualization built on Matplotlib; cleaner defaults
- [Plotly](https://plotly.com/python/) - interactive plots for notebooks and web; also powers Dash dashboards

## Specialized Packages

- [Rtree: Spatial indexing for Python](https://rtree.readthedocs.io/en/latest/) - R-tree spatial index for fast bounding-box queries
- [Faiss](https://faiss.ai/) - efficient similarity search and clustering of dense vectors
- [pqdict](https://pqdict.readthedocs.io/en/latest/intro.html) - an updatable priority queue backed by a dictionary


## Type Checking

- [mypy](https://mypy.readthedocs.io/) - the original and most widely adopted Python type checker; strict mode, plugin ecosystem, incremental checking; de facto standard for CI enforcement
- [Pyright](https://github.com/microsoft/pyright) - fast, accurate type checker from Microsoft written in TypeScript; powers Pylance in VS Code; strict mode goes further than mypy in several areas; excellent for large codebases
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) - VS Code language server built on Pyright; adds IntelliSense, auto-imports, and semantic highlighting on top of Pyright's type engine
- [Pyrefly](https://pyrefly.org/) - new type checker from Meta written in Rust; aims for extreme speed on very large monorepos; still maturing but very fast incremental analysis. [Used in the PyTorch repo internally](https://pytorch.org/blog/pyrefly-now-type-checks-pytorch/).
- [Ruff](https://docs.astral.sh/ruff/) - primarily a linter/formatter, but enforces many type-annotation style rules (e.g. `UP`/`ANN` rule sets) and is the fastest option for catching annotation anti-patterns at lint time
