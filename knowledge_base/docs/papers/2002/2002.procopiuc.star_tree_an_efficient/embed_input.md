STAR-Tree: An Efficient Self-Adjusting Index for Moving Objects

Topics include Moving object indexing, STAR-tree, Spatial databases, Nearest neighbor search, Range queries, Self-adjusting indexes, R-trees.

Introduces STAR-tree, a self-adjusting spatial index for moving points that reorganizes itself locally when query performance deteriorates. The data structure targets range, time-slice, and nearest-neighbor queries for moving-object databases while balancing storage, update cost, and query speed.

We present a new technique called STAR-tree, based on R*-tree, for indexing a set of moving points so that various queries, including range queries, time-slice queries, and nearest-neighbor queries, can be answered efficiently. A novel feature of the index is that it is self-adjusting in the sense that it re-organizes itself locally whenever its query performance deteriorates. The index provides tradeoffs between storage and query performance and between time spent in updating the index and in answering queries. We present detailed performance studies and compare our methods with the existing ones under a varying type of data sets and queries. Our experiments show that the index proposed here performs considerably better than the previously known ones.
