<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sample Efficient Actor-Critic with Experience Replay

Topics include Reinforcement learning, Optimization, Control, Learning, Sampling.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents an actor-critic deep reinforcement learning agent with experience replay that is stable, sample efficient, and performs remarkably well on challenging environments, including the discrete 57-game Atari domain and several continuous control problems. To achieve this, the paper introduces several innovations, including truncated importance sampling with bias correction, stochastic dueling network architectures, and a new trust region policy optimization method.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

The abstract paragraph should be indented $1/2$ inch (3 picas) on both the left- and right-hand margins. Use 10 point type, with a vertical spacing (leading) of 11 points. The word Abstract must be centered, bold, and in point size 12. Two line spaces precede the abstract. The abstract must be limited to one paragraph.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Submission of papers to NIPS 2016", "weight": 1.0} -->

There is a new style file for papers submitted in 2016!

<!-- chunk {"id": "body-0005", "role": "body", "section": "Submission of papers to NIPS 2016", "weight": 1.0} -->

NIPS requires electronic submissions. The electronic submission site is Please read carefully the instructions below and follow them faithfully.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Style", "weight": 1.0} -->

Papers to be submitted to NIPS 2016 must be prepared according to the instructions presented here. Papers may only be up to eight pages long, including figures. Since 2009 an additional ninth page *containing only acknowledgments and/or cited references* is allowed. Papers that exceed nine pages will not be reviewed, or in any other way considered for presentation at the conference.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Style", "weight": 1.0} -->

The margins in 2016 are the same as since 2007, which allow for $\sim$$15\%$ more words in the paper compared to earlier years.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Style", "weight": 1.0} -->

Authors are required to use the NIPS LaTeX style files obtainable at the NIPS website as indicated below. Please make sure you use the current files and not previous versions. Tweaking the style files may be grounds for rejection.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Retrieval of style files", "weight": 1.0} -->

The style files for NIPS and other conference information are available on the World Wide Web at The file `nips_2016.pdf` contains these instructions and illustrates the various formatting requirements your NIPS paper must satisfy.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Retrieval of style files", "weight": 1.0} -->

The only supported style file for NIPS 2016 is `nips_2016.sty`, rewritten for LaTeX 2ε. Previous style files for LaTeX 2.09, Microsoft Word, and RTF are no longer supported!

<!-- chunk {"id": "body-0011", "role": "body", "section": "Retrieval of style files", "weight": 1.0} -->

The new LaTeX style file contains two optional arguments: `final`, which creates a camera-ready copy, and `nonatbib`, which will not load the `natbib` package for you in case of package clash.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Retrieval of style files", "weight": 1.0} -->

At submission time, please omit the `final` option. This will anonymize your submission and add line numbers to aid review. Please do *not* refer to these line numbers in your paper as they will be removed during generation of camera-ready copies.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Retrieval of style files", "weight": 1.0} -->

The file `nips_2016.tex` may be used as a "shell" for writing your paper. All you have to do is replace the author, title, abstract, and text of the paper with your own.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Retrieval of style files", "weight": 1.0} -->

The formatting instructions contained in these style files are summarized in Sections 2, 3, and 4 below.

<!-- chunk {"id": "body-0015", "role": "body", "section": "General formatting instructions", "weight": 1.0} -->

The text must be confined within a rectangle 5.5 inches (33 picas) wide and 9 inches (54 picas) long. The left margin is 1.5 inch (9 picas). Use 10 point type with a vertical spacing (leading) of 11 points. Times New Roman is the preferred typeface throughout, and will be selected for you by default. Paragraphs are separated by $1/2$ line space (5.5 points), with no indentation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "General formatting instructions", "weight": 1.0} -->

The paper title should be 17 point, initial caps/lower case, bold, centered between two horizontal rules. The top rule should be 4 points thick and the bottom rule should be 1 point thick. Allow $1/4$ inch space above and below the title to rules. All pages should start at 1 inch (6 picas) from the top of the page.

<!-- chunk {"id": "body-0017", "role": "body", "section": "General formatting instructions", "weight": 1.0} -->

For the final version, authors' names are set in boldface, and each name is centered above the corresponding address. The lead author's name is to be listed first (left-most), and the co-authors' names (if different address) are set to follow. If there is only one co-author, list both author and co-author side by side.

<!-- chunk {"id": "body-0018", "role": "body", "section": "General formatting instructions", "weight": 1.0} -->

Please pay special attention to the instructions in Section 4 regarding figures, tables, acknowledgments, and references.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Headings: first level", "weight": 1.0} -->

All headings should be lower case (except for first word and proper nouns), flush left, and bold.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Headings: first level", "weight": 1.0} -->

First-level headings should be in 12-point type.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Headings: second level", "weight": 1.0} -->

Second-level headings should be in 10-point type.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Headings: third level", "weight": 1.0} -->

Third-level headings should be in 10-point type.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Paragraphs", "weight": 1.0} -->

There is also a `\paragraph` command available, which sets the heading in bold, flush left, and inline with the text, with the heading followed by 1 em of space.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Citations within the text", "weight": 1.0} -->

The `natbib` package will be loaded for you by default. Citations may be author/year or numeric, as long as you maintain internal consistency. As to the format of the references themselves, any style is acceptable as long as it is used consistently.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Citations within the text", "weight": 1.0} -->

The documentation for `natbib` may be found at Of note is the command ``, which produces citations appropriate for use in inline text. For example, If you wish to load the `natbib` package with options, you may add the following before loading the `nips_2016` package: \PassOptionsToPackage{options}{natbib} If `natbib` clashes with another package you load, you can add the optional argument `nonatbib` when loading the style file: \usepackage[nonatbib]{nips_2016} As submission is double blind, refer to your own published work in the third person. That is, use "In the previous work of Jones et al.," not "In our previous work." If you cite your other papers that are not widely available (e.g., a journal paper under review), use anonymous author names in the citation, e.g., an author of the form "A. Anonymous."

<!-- chunk {"id": "body-0026", "role": "body", "section": "Footnotes", "weight": 1.0} -->

Footnotes should be used sparingly. If you do require a footnote, indicate footnotes with a number^11^1Sample of the first footnote. in the text. Place the footnotes at the bottom of the page on which they appear. Precede the footnote with a horizontal rule of 2 inches (12 picas).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Footnotes", "weight": 1.0} -->

Note that footnotes are properly typeset *after* punctuation marks.^22^2As in this example.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Figures", "weight": 1.0} -->

All artwork must be neat, clean, and legible. Lines should be dark enough for purposes of reproduction. The figure number and caption always appear after the figure. Place one line space before the figure caption and one line space after the figure. The figure caption should be lower case (except for first word and proper nouns); figures are numbered consecutively.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Figures", "weight": 1.0} -->

You may use color figures. However, it is best for the figure captions and the paper body to be legible if the paper is printed in either black/white or in color.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Tables", "weight": 1.0} -->

All tables must be centered, neat, clean and legible. The table number and title always appear before the table. See Table 1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Tables", "weight": 1.0} -->

Place one line space before the table title, one line space after the table title, and one line space after the table. The table title must be lower case (except for first word and proper nouns); tables are numbered consecutively.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Tables", "weight": 1.0} -->

Note that publication-quality tables *do not contain vertical rules.* We strongly suggest the use of the `booktabs` package, which allows for typesetting high-quality, professional tables: This package was used to typeset Table 1.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Final instructions", "weight": 1.0} -->

Do not change any aspects of the formatting parameters in the style files. In particular, do not modify the width or length of the rectangle the text should fit into, and do not change font sizes (except perhaps in the References section; see below). Please note that pages should be numbered.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Preparing PDF files", "weight": 1.0} -->

Please prepare submission files with paper size "US Letter," and not, for example, "A4."

<!-- chunk {"id": "body-0035", "role": "body", "section": "Preparing PDF files", "weight": 1.0} -->

Fonts were the main cause of problems in the past years. Your PDF file must only contain Type 1 or Embedded TrueType fonts. Here are a few instructions to achieve this.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Preparing PDF files", "weight": 1.0} -->

You should directly generate PDF files using `pdflatex`.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Preparing PDF files", "weight": 1.0} -->

You can check which fonts a PDF files uses. In Acrobat Reader, select the menu Files$>$Document Properties$>$Fonts and select Show All Fonts. You can also use the program `pdffonts` which comes with `xpdf` and is available out-of-the-box on most Linux machines.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Preparing PDF files", "weight": 1.0} -->

The IEEE has recommendations for generating PDF files whose fonts are also acceptable for NIPS. Please see `xfig` \"patterned\" shapes are implemented with bitmap fonts. Use \"solid\" shapes instead.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Preparing PDF files", "weight": 1.0} -->

The `\bbold` package almost always uses bitmap fonts. You should use the equivalent AMS Fonts: followed, e.g., `\mathbb{R}`, `\mathbb{N}`, or `\mathbb{C}` for $\mathbb{R}$, $\mathbb{N}$ or $\mathbb{C}$. You can also use the following workaround for reals, natural and complex: \newcommand{\RR}{I\!\!R} %real numbers \newcommand{\Nat}{I\!\!N} %natural numbers \newcommand{\CC}{I\!\!\!\!C} %complex numbers Note that `amsfonts` is automatically loaded by the `amssymb` package.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Preparing PDF files", "weight": 1.0} -->

If your file contains type 3 fonts or non embedded TrueType fonts, we will ask you to fix it.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Margins in LaTeX", "weight": 1.0} -->

Most of the margin problems come from figures positioned by hand using `\special` or other commands. We suggest using the command `\includegraphics` from the `graphicx` package. Always specify the figure width as a multiple of the line width as in the example below: \usepackage[pdftex]{graphicx}... \includegraphics[width=0.8\linewidth]{myfile.pdf} See Section 4.4 in the graphics bundle documentation A number of width problems arise when LaTeX cannot properly hyphenate a line. Please give LaTeX hyphenation hints using the `\-` command when necessary.
