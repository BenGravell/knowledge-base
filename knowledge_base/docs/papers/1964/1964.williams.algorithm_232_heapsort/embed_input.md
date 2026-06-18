<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Algorithm 232: Heapsort

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Williams introduces heapsort as an array-based sorting procedure built around a binary heap, first arranging the input into a heap and then repeatedly removing the largest element to produce the sorted order. The note is historically important as the original presentation of heapsort: a comparison sort with worst-case O(n log n) running time and in-place operation using only a small amount of auxiliary storage.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The following procedures are related to TREESORT [R. W. Floyd, Alg. 113, Comm. ACM 5, 434; and A. F. Kaupe, Jr., Alg. 143 and 144, Comm. ACM 5, 604] but avoid the use of pointers and so preserve storage space. All the procedures operate on single word items, stored as elements 1 to n of the array A. The elements are normally so arranged that A[j]≤A[i] for 2≤j≤n, i=j÷2. Such an arrangement will be called a heap. A is always the least element of the heap. The procedure SETHEAP arranges n elements as a heap, INHEAP adds a new element to an existing heap, OUTHEAP extracts the least element from a heap, and SWOPHEAP is effectively the result of INHEAP followed by OUTHEAP. In all cases the array A contains elements arranged as a heap on exit. SWOPHEAP is essentially the same as the tournament sort described by K. E. Iverson - A Programming Language, 1962, pp.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

223-226 - which is a top to bottom method, but it uses an improved storage allocation and initialisation. INHEAP resembles TREESORT in being a bottom to top method. HEAPSORT can thus be considered as a marriage of these two methods. The procedures may be used for replacement-selection sorting, for sorting the elements of an array, or for choosing the current minimum of any set of items to which new items are added from time to time. The procedures are the more useful because the active elements of the array are maintained densely packed, as elements A to A[n];
