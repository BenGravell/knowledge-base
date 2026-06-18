<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Resemblance and Containment of Documents

Topics include Document similarity, Document containment, Minhash, Rabin fingerprints, Random sampling, Web indexing, Set similarity.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Defines document resemblance and containment measures that reduce near-duplicate detection to sampled set-intersection estimates. Using Rabin fingerprints and fixed-size sketches, the paper provides a scalable foundation for web-scale duplicate detection and later MinHash-style similarity search.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Given two documents A and B we define two mathematical notions: their resemblance r(A, B) and their containment c(A, B) that seem to capture well the informal notions of "roughly the same" and "roughly contained." The basic idea is to reduce these issues to set intersection problems that can be easily evaluated by a process of random sampling that can be done independently for each document. Furthermore, the resemblance can be evaluated using a fixed size sample for each document. This paper discusses the mathematical properties of these measures and the efficient implementation of the sampling process using Rabin fingerprints.
