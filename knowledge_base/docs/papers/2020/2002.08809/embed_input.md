<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DDPNOpt: Differential Dynamic Programming Neural Optimizer

Topics include Optimal control, Trajectory optimization, Neural networks, Attention mechanisms, Online algorithms, Optimization, Control, DDPNOpt, Differential dynamic programming, Dynamic programming.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Interpretation of Deep Neural Networks (DNNs) training as an optimal control problem with nonlinear dynamical systems has received considerable attention recently, yet the algorithmic development remains relatively limited. In this work, we make an attempt along this line by reformulating the training procedure from the trajectory optimization perspective. We first show that most widely-used algorithms for training DNNs can be linked to the Differential Dynamic Programming (DDP), a celebrated second-order method rooted in the Approximate Dynamic Programming. In this vein, we propose a new class of optimizer, DDP Neural Optimizer (DDPNOpt), for training feedforward and convolution networks. DDPNOpt features layer-wise feedback policies which improve convergence and reduce sensitivity to hyper-parameter over existing methods. It outperforms other optimal-control inspired training methods in both convergence and complexity, and is competitive against state-of-the-art first and second order methods. We also observe DDPNOpt has surprising benefit in preventing gradient vanishing. Our work opens up new avenues for principled algorithmic design built upon the optimal control theory.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

The abstract paragraph should be indented 1/2 inch (3 picas) on both left and right-hand margins. Use 10 point type, with a vertical spacing of 11 points. The word Abstract must be centered, in small caps, and in point size 12. Two line spaces precede the abstract. The abstract must be limited to one paragraph.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Submission of conference papers to ICLR 2021", "weight": 1.0} -->

ICLR requires electronic submissions, processed by See ICLR's website for more instructions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Submission of conference papers to ICLR 2021", "weight": 1.0} -->

If your paper is ultimately accepted, the statement \\iclrfinalcopy should be inserted to adjust the format to the camera ready requirements.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Submission of conference papers to ICLR 2021", "weight": 1.0} -->

The format for the submissions is a variant of the NeurIPS format. Please read carefully the instructions below, and follow them faithfully.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Style", "weight": 1.0} -->

Papers to be submitted to ICLR 2021 must be prepared according to the instructions presented here.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Style", "weight": 1.0} -->

Authors are required to use the ICLR LaTeX style files obtainable at the ICLR website. Please make sure you use the current files and not previous versions. Tweaking the style files may be grounds for rejection.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Retrieval of style files", "weight": 1.0} -->

The style files for ICLR and other conference information are available online: The file `iclr2021_conference.pdf` contains these instructions and illustrates the various formatting requirements your ICLR paper must satisfy. Submissions must be made using LaTeX and the style files `iclr2021_conference.sty` and `iclr2021_conference.bst` (to be used with LaTeX2e). The file `iclr2021_conference.tex` may be used as a "shell" for writing your paper. All you have to do is replace the author, title, abstract, and text of the paper with your own.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Retrieval of style files", "weight": 1.0} -->

The formatting instructions contained in these style files are summarized in sections 2, 3, and 4 below.

<!-- chunk {"id": "body-0011", "role": "body", "section": "General formatting instructions", "weight": 1.0} -->

The text must be confined within a rectangle 5.5 inches (33 picas) wide and 9 inches (54 picas) long. The left margin is 1.5 inch (9 picas). Use 10 point type with a vertical spacing of 11 points. Times New Roman is the preferred typeface throughout. Paragraphs are separated by 1/2 line space, with no indentation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "General formatting instructions", "weight": 1.0} -->

Paper title is 17 point, in small caps and left-aligned. All pages should start at 1 inch (6 picas) from the top of the page.

<!-- chunk {"id": "body-0013", "role": "body", "section": "General formatting instructions", "weight": 1.0} -->

Authors' names are set in boldface, and each name is placed above its corresponding address. The lead author's name is to be listed first, and the co-authors' names are set to follow. Authors sharing the same address can be on the same line.

<!-- chunk {"id": "body-0014", "role": "body", "section": "General formatting instructions", "weight": 1.0} -->

Please pay special attention to the instructions in section 4 regarding figures, tables, acknowledgments, and references.

<!-- chunk {"id": "body-0015", "role": "body", "section": "General formatting instructions", "weight": 1.0} -->

There will be a strict upper limit of 8 pages for the main text of the initial submission, with unlimited additional pages for citations. Note that the upper page limit differs from last year!Authors may use as many pages of appendices (after the bibliography) as they wish, but reviewers are not required to read these. During the rebuttal phase and for the camera ready version, authors are allowed one additional page for the main text, for a strict upper limit of 9 pages.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Headings: first level", "weight": 1.0} -->

First level headings are in small caps, flush left and in point size 12. One line space before the first level heading and 1/2 line space after the first level heading.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Headings: second level", "weight": 1.0} -->

Second level headings are in small caps, flush left and in point size 10. One line space before the second level heading and 1/2 line space after the second level heading.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Headings: third level", "weight": 1.0} -->

Third level headings are in small caps, flush left and in point size 10. One line space before the third level heading and 1/2 line space after the third level heading.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Citations, figures, tables, references", "weight": 1.0} -->

These instructions apply to everyone, regardless of the formatter being used.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Citations within the text", "weight": 1.0} -->

Citations within the text should be based on the natbib package and include the authors' last names and year (with the "et al." construct for more than two authors). When the authors or the publication are included in the sentence, the citation should not be in parenthesis using `` (as in "See for more information."). Otherwise, the citation should be in parenthesis using `` (as in "Deep learning shows promise to make progress towards AI (Bengio+chapter2007).").

<!-- chunk {"id": "body-0021", "role": "body", "section": "Citations within the text", "weight": 1.0} -->

The corresponding references are to be listed in alphabetical order of authors, in the References section. As to the format of the references themselves, any style is acceptable as long as it is used consistently.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Footnotes", "weight": 1.0} -->

Indicate footnotes with a number^11^1Sample of the first footnote in the text. Place the footnotes at the bottom of the page on which they appear. Precede the footnote with a horizontal rule of 2 inches (12 picas).^22^2Sample of the second footnote

<!-- chunk {"id": "body-0023", "role": "body", "section": "Figures", "weight": 1.0} -->

All artwork must be neat, clean, and legible. Lines should be dark enough for purposes of reproduction; art work should not be hand-drawn. The figure number and caption always appear after the figure. Place one line space before the figure caption, and one line space after the figure. The figure caption is lower case (except for first word and proper nouns); figures are numbered consecutively.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Figures", "weight": 1.0} -->

Make sure the figure caption does not get separated from the figure. Leave sufficient space to avoid splitting the figure and figure caption.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Figures", "weight": 1.0} -->

You may use color figures. However, it is best for the figure captions and the paper body to make sense if the paper is printed either in black/white or in color.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Tables", "weight": 1.0} -->

All tables must be centered, neat, clean and legible. Do not use hand-drawn tables. The table number and title always appear before the table. See Table 1.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Tables", "weight": 1.0} -->

Place one line space before the table title, one line space after the table title, and one line space after the table. The table title must be lower case (except for first word and proper nouns); tables are numbered consecutively.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Tables", "weight": 1.0} -->

Cell body (contains cell nucleus) Table 1: Sample table title

<!-- chunk {"id": "body-0029", "role": "body", "section": "Default Notation", "weight": 1.0} -->

In an attempt to encourage standardized notation, we have included the notation file from the textbook, Deep Learning goodfellow2016deep available at Use of this style is not required and can be disabled by commenting out math_commands.tex.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Default Notation", "weight": 1.0} -->

Numbers and Arrays Sets and Graphs Probability and Information Theory

<!-- chunk {"id": "body-0031", "role": "body", "section": "Final instructions", "weight": 1.0} -->

Do not change any aspects of the formatting parameters in the style files. In particular, do not modify the width or length of the rectangle the text should fit into, and do not change font sizes (except perhaps in the References section; see below). Please note that pages should be numbered.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Preparing PostScript or PDF files", "weight": 1.0} -->

Please prepare PostScript or PDF files with paper size "US Letter", and not, for example, "A4". The -t letter option on dvips will produce US Letter files.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Preparing PostScript or PDF files", "weight": 1.0} -->

Consider directly generating PDF files using `pdflatex` (especially if you are a MiKTeX user). PDF figures must be substituted for EPS figures, however.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Preparing PostScript or PDF files", "weight": 1.0} -->

Otherwise, please generate your PostScript and PDF files with the following commands: dvips mypaper.dvi -t letter -Ppdf -G0 -o mypaper.ps ps2pdf mypaper.ps mypaper.pdf

<!-- chunk {"id": "body-0035", "role": "body", "section": "Margins in LaTeX", "weight": 1.0} -->

Most of the margin problems come from figures positioned by hand using `\special` or other commands. We suggest using the command `\includegraphics` from the graphicx package. Always specify the figure width as a multiple of the line width as in the example below using.eps graphics \usepackage[dvips]{graphicx}... \includegraphics[width=0.8\linewidth]{myfile.eps} \usepackage[pdftex]{graphicx}... \includegraphics[width=0.8\linewidth]{myfile.pdf}.pdf graphics. See section 4.4 in the graphics bundle documentation A number of width problems arise when LaTeX cannot properly hyphenate a line. Please give LaTeX hyphenation hints using the `\-` command.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Author Contributions", "weight": 1.0} -->

If you'd like to, you may include a section for author contributions as is done in many journals. This is optional and at the discretion of the authors.
