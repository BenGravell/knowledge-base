Left-Leaning Red-Black Trees

Topics include Balanced trees, Red-black tree, Data structures, Symbol tables, Algorithm, Binary search trees.

Presents left-leaning red-black trees as a simpler formulation of balanced binary search trees that mirrors 2-3 tree structure. The implementation style reduces case complexity while preserving logarithmic search, insertion, and deletion.

The red-black tree model for implementing balanced search trees, introduced by Guibas and Sedgewick thirty years ago, is now found throughout our computational infrastructure. Red-black trees are described in standard textbooks and are the underlying data structure for symbol-table implementations within C++, Java, Python, BSD Unix, and many other modern systems. However, many of these implementations have sacrificed some of the original design goals (primarily in order to develop an effective implementation of the delete operation, which was incompletely specified in the original paper), so a new look is worthwhile. In this paper, we describe a new variant of red-black trees that meets many of the original design goals and leads to substantially simpler code for insert/delete, less than one-fourth as much code as in implementations in common use.
