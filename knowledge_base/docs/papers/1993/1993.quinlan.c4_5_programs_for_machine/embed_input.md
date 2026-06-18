<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

C4.5: Programs for Machine Learning

Topics include Decision trees, C4.5, Classification, Machine learning, Gain ratio, Pruning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends the ID3 algorithm into C4.5, adding gain ratio (to correct ID3's bias toward high-cardinality attributes), cost-sensitive learning, handling of continuous attributes, pruning by estimated error rate, and direct handling of missing values. C4.5 was historically one of the most used decision-tree systems and the basis for Weka's J48 classifier.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Classifier systems play a major role in machine learning and knowledge-based systems, and Ross Quinlan's work on ID3 and C4.5 is widely acknowledged to have made some of the most significant contributions to their development. This book is a complete guide to the C4.5 system as implemented in C for the UNIX environment. It contains a comprehensive guide to the system's use, the source code (about 8,800 lines), and implementation notes. The source code and sample datasets are also available on a 3.5-inch floppy diskette for a Sun workstation. C4.5 starts with large sets of cases belonging to known classes. The cases, described by any mixture of nominal and numeric properties, are scrutinized for patterns that allow the classes to be reliably discriminated. These patterns are then expressed as models, in the form of decision trees or sets of if-then rules, that can be used to classify new cases, with emphasis on making the models understandable as well as accurate. The system has been applied successfully to tasks involving tens of thousands of cases described by hundreds of properties.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The book starts from simple core learning methods and shows how they can be elaborated and extended to deal with typical problems such as missing data and over hitting. Advantages and disadvantages of the C4.5 approach are discussed and illustrated with several case studies. This book and software should be of interest to developers of classification-based intelligent systems and to students in machine learning and expert systems courses.
