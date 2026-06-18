<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

STAR-Tree: An Efficient Self-Adjusting Index for Moving Objects

Topics include Moving object indexing, STAR-tree, Spatial databases, Nearest neighbor search, Range queries, Self-adjusting indexes, R-trees.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces STAR-tree, a self-adjusting spatial index for moving points that reorganizes itself locally when query performance deteriorates. The data structure targets range, time-slice, and nearest-neighbor queries for moving-object databases while balancing storage, update cost, and query speed.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a new technique called STAR-tree, based on R*-tree, for indexing a set of moving points so that various queries, including range queries, time-slice queries, and nearest-neighbor queries, can be answered efficiently. A novel feature of the index is that it is self-adjusting in the sense that it re-organizes itself locally whenever its query performance deteriorates. The index provides tradeoffs between storage and query performance and between time spent in updating the index and in answering queries. We present detailed performance studies and compare our methods with the existing ones under a varying type of data sets and queries. Our experiments show that the index proposed here performs considerably better than the previously known ones.
