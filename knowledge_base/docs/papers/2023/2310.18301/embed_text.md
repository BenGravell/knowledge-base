## Introduction

This demo file is intended to serve as a "starter file" for the Robotics: Science and Systems conference papers produced under LATEX using IEEEtran.cls version 1.7a and later.

## Section

Section text here.

### II-A Subsection Heading Here

Subsection text here.

### II-A1 Subsubsection Heading Here

Subsubsection text here.

## RSS citations

Please make sure to include `natbib.sty` and to use the `plainnat.bst` bibliography style. `natbib` provides additional citation commands, most usefully `\citet`. For example, rather than the awkward construction

\cite{kalman1960new} demonstrated...

rendered as "\[kalman1960new\] demonstrated...," or the inconvenient

Kalman \cite{kalman1960new}

rendered as "Kalman \[kalman1960new\] demonstrated...", one can write

\citet{kalman1960new} demonstrated...

which renders as "kalman1960new demonstrated..." and is both easy to write and much easier to read.

### III-A RSS Hyperlinks

This year, we would like to use the ability of PDF viewers to interpret hyperlinks, specifically to allow each reference in the bibliography to be a link to an online version of the reference. As an example, if you were to cite "Passive Dynamic Walking" \[McGeer01041990\], the entry in the bibtex would read:

author = {McGeer, Tad},
title = {\href{http://ijr.sagepub.com/content/9/2/62.abstract}{Passive Dynamic Walking}},
URL = {http://ijr.sagepub.com/content/9/2/62.abstract},
eprint = {http://ijr.sagepub.com/content/9/2/62.full.pdf+html},
journal = {The International Journal of Robotics Research}

and the entry in the compiled PDF would look like:

Tad McGeer. [Passive Dynamic Walking](http://ijr.sagepub.com/content/9/2/62.abstract). The International Journal of Robotics Research, 9:62--82, 1990.

where the title of the article is a link that takes you to the article on IJRR's website.

Linking cited articles will not always be possible, especially for older articles. There are also often several versions of papers online: authors are free to decide what to use as the link destination yet we strongly encourage to link to archival or publisher sites (such as IEEE Xplore or Sage Journals). We encourage all authors to use this feature to the extent possible.

## Conclusion

The conclusion goes here.
