<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Provably Stable Learning Control of Linear Dynamics with Multiplicative Noise

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Control of linear dynamics with multiplicative noise naturally introduces robustness against dynamical uncertainty. Moreover, many physical systems are subject to multiplicative disturbances. In this work we show how these dynamics can be identified from state trajectories. The least-squares scheme enables exploitation of prior information and comes with practical data-driven confidence bounds and sample complexity guarantees. We complement this scheme with an associated control synthesis procedure for LQR which robustifies against distributional uncertainty, guaranteeing stability with high probability and converging to the true optimum at a rate inversely proportional with the sample count. Throughout we exploit the underlying multi-linear problem structure through tensor algebra and completely positive operators. The scheme is validated through numerical experiments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

This document is a template for LaTeX. If you are reading a paper or PDF version of this document, please download the electronic file, trans_jour.tex, from the IEEE Web site at so you can use it to prepare your manuscript. If you would prefer to use LaTeX, download IEEE's LaTeX style and sample files from the same Web page. You can also explore using the Overleaf editor at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

If your paper is intended for a conference, please contact your conference editor concerning acceptable word processor formats for your particular conference.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

IEEE will do the final formatting of your paper. If your paper is intended for a conference, please observe the conference page limits.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Abbreviations and Acronyms", "weight": 1.0} -->

Define abbreviations and acronyms the first time they are used in the text, even after they have already been defined in the abstract. Abbreviations such as IEEE, SI, ac, and dc do not have to be defined. Abbreviations that incorporate periods should not have spaces: write "C.N.R.S.," not "C. N. R. S." Do not use abbreviations in the title unless they are unavoidable (for example, "IEEE" in the title of this article).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Other Recommendations", "weight": 1.0} -->

Use one space after periods and colons. Hyphenate complex modifiers: "zero-field-cooled magnetization." Avoid dangling participles, such as, "Using (1")), the potential was calculated." \It is not clear who or what used ([1")).\] Write instead, "The potential was calculated by using (1"))," or "Using (1")), we calculated the potential."

<!-- chunk {"id": "body-0008", "role": "body", "section": "Other Recommendations", "weight": 1.0} -->

Use a zero before decimal points: "0.25," not ".25." Use "cm^3^," not "cc." Indicate sample dimensions as "0.1 cm $\times$ 0.2 cm," not "0.1 $\times$ 0.2 cm^2^." The abbreviation for "seconds" is "s," not "sec." Use "Wb/m^2^" or "webers per square meter," not "webers/m^2^." When expressing a range of values, write "7 to 9" or "7--9," not "7$\sim$`<!-- -->`{=html}9."

<!-- chunk {"id": "body-0009", "role": "body", "section": "Other Recommendations", "weight": 1.0} -->

A parenthetical statement at the end of a sentence is punctuated outside of the closing parenthesis (like this). (A parenthetical sentence is punctuated within the parentheses.) In American English, periods and commas are within quotation marks, like "this period." Other punctuation is "outside"! Avoid contractions; for example, write "do not" instead of "don't." The serial comma is preferred: "A, B, and C" instead of "A, B and C."

<!-- chunk {"id": "body-0010", "role": "body", "section": "Other Recommendations", "weight": 1.0} -->

If you wish, you may write in the first person singular or plural and use the active voice ("I observed that $\ldots$" or "We observed that $\ldots$" instead of "It was observed that $\ldots$"). Remember to check spelling. If your native language is not English, please get a native English-speaking colleague to carefully proofread your paper.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Other Recommendations", "weight": 1.0} -->

Try not to use too many typefaces in the same article. You're writing scholarly papers, not ransom notes. Also please remember that MathJax can't handle really weird typefaces.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Equations", "weight": 1.0} -->

Number equations consecutively with equation numbers in parentheses flush with the right margin, as in (1")). To make your equations more compact, you may use the solidus ( / ), the exp function, or appropriate exponents. Use parentheses to avoid ambiguities in denominators. Punctuate equations when they are part of a sentence, as in

<!-- chunk {"id": "body-0013", "role": "body", "section": "Equations", "weight": 1.0} -->

Be sure that the symbols in your equation have been defined before the equation appears or immediately following. Italicize symbols ($T$ might refer to temperature, but T is the unit tesla). Refer to "(1"))," not "Eq. (1"))" or "equation (1"))," except at the beginning of a sentence: "Equation (1")) is $\ldots$."

<!-- chunk {"id": "body-0014", "role": "body", "section": "LaTeX-Specific Advice", "weight": 1.0} -->

Please use "soft" (e.g., `\eqref{Eq}`) cross references instead of "hard" references (e.g., ``). That will make it possible to combine sections, add equations, or change the order of figures or citations without having to go through the file line by line.

<!-- chunk {"id": "body-0015", "role": "body", "section": "LaTeX-Specific Advice", "weight": 1.0} -->

Please don't use the `{eqnarray}` equation environment. Use `{align}` or `{IEEEeqnarray}` instead. The `{eqnarray}` environment leaves unsightly spaces around relation symbols.

<!-- chunk {"id": "body-0016", "role": "body", "section": "LaTeX-Specific Advice", "weight": 1.0} -->

Please note that the `{subequations}` environment in LaTeX will increment the main equation counter even when there are no equation numbers displayed. If you forget that, you might write an article in which the equation numbers skip from to, causing the copy editors to wonder if you've discovered a new method of counting.

<!-- chunk {"id": "body-0017", "role": "body", "section": "LaTeX-Specific Advice", "weight": 1.0} -->

BibTEX does not work by magic. It doesn't get the bibliographic data from thin air but.bib files. If you use BibTEX to produce a bibliography you must send the.bib files.

<!-- chunk {"id": "body-0018", "role": "body", "section": "LaTeX-Specific Advice", "weight": 1.0} -->

LaTeX can't read your mind. If you assign the same label to a subsubsection and a table, you might find that Table I has been cross referenced as Table IV-B3.

<!-- chunk {"id": "body-0019", "role": "body", "section": "LaTeX-Specific Advice", "weight": 1.0} -->

LaTeX does not have precognitive abilities. If you put a `\label` command before the command that updates the counter it's supposed to be using, the label will pick up the last counter to be cross referenced instead. In particular, a `\label` command should not go before the caption of a figure or a table.

<!-- chunk {"id": "body-0020", "role": "body", "section": "LaTeX-Specific Advice", "weight": 1.0} -->

Do not use `\nonumber` inside the `{array}` environment. It will not stop equation numbers inside `{array}` (there won't be any anyway) and it might stop a wanted equation number in the surrounding equation.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Units", "weight": 1.0} -->

Use either SI (MKS) or CGS as primary units. (SI units are strongly encouraged.) English units may be used as secondary units (in parentheses). This applies to papers in data storage. For example, write "15 Gb/cm^2^ (100 Gb/in${}_{}^{}{}$." An exception is when English units are used as identifiers in trade, such as "3½-in disk drive." Avoid combining SI and CGS units, such as current in amperes and magnetic field in oersteds. This often leads to confusion because equations do not balance dimensionally. If you must use mixed units, clearly state the units for each quantity in an equation.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Units", "weight": 1.0} -->

The SI unit for magnetic field strength $H$ is A/m. However, if you wish to use units of T, either refer to magnetic flux density $B$ or magnetic field strength symbolized as $\mu_{0}H$. Use the center dot to separate compound units, e.g., "A$\cdot$m^2^."

<!-- chunk {"id": "body-0023", "role": "body", "section": "Some Common Mistakes", "weight": 1.0} -->

The word "data" is plural, not singular. The subscript for the permeability of vacuum $\mu_{0}$ is zero, not a lowercase letter "o." The term for residual magnetization is "remanence"; the adjective is "remanent"; do not write "remnance" or "remnant." Use the word "micrometer" instead of "micron." A graph within a graph is an "inset," not an "insert." The word "alternatively" is preferred to the word "alternately" (unless you really mean something that alternates). Use the word "whereas" instead of "while" (unless you are referring to simultaneous events).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Some Common Mistakes", "weight": 1.0} -->

Do not use the word "essentially" to mean "approximately" or "effectively." Do not use the word "issue" as a euphemism for "problem." When compositions are not specified, separate chemical symbols by en-dashes; for example, "NiMn" indicates the intermetallic compound Ni~0.5~Mn~0.5~ whereas "Ni--Mn" indicates an alloy of some composition Ni~x~Mn~1-x~.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Some Common Mistakes", "weight": 1.0} -->

Be aware of the different meanings of the homophones "affect" (usually a verb) and "effect" (usually a noun), "complement" and "compliment," "discreet" and "discrete," "principal" (e.g., "principal investigator") and "principle" (e.g., "principle of measurement"). Do not confuse "imply" and "infer."

<!-- chunk {"id": "body-0026", "role": "body", "section": "Some Common Mistakes", "weight": 1.0} -->

Prefixes such as "non," "sub," "micro," "multi," and "ultra" are not independent words; they should be joined to the words they modify, usually without a hyphen. There is no period after the "et" in the Latin abbreviation "*et al.*" (it is also italicized). The abbreviation "i.e.," means "that is," and the abbreviation "e.g.," means "for example" (these abbreviations are not italicized).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Types of Graphics", "weight": 1.0} -->

The following list outlines the different types of graphics published in IEEE journals.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Color/Grayscale figures", "weight": 1.0} -->

Figures that are meant to appear in color, or shades of black/gray. Such figures may include photographs, illustrations, multicolor graphs, and flowcharts.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Line Art figures", "weight": 1.0} -->

Figures that are composed of only black lines and shapes. These figures should have no shades or half-tones of gray, only black and white.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Author photos", "weight": 1.0} -->

Head and shoulders shots of authors that appear at the end of our papers.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Tables", "weight": 1.0} -->

Data charts which are typically black and white, but sometimes include color.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Tables", "weight": 1.0} -->

Conversion from Gaussian and CGS EMU to SI a

<!-- chunk {"id": "body-0033", "role": "body", "section": "Tables", "weight": 1.0} -->

magnetic flux density, magnetic induction

<!-- chunk {"id": "body-0034", "role": "body", "section": "Tables", "weight": 1.0} -->

Vertical lines are optional in tables. Statements that serve as captions for the entire table do not need footnote letters.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Tables", "weight": 1.0} -->

aGaussian units are the same as cg emu for magnetostatics; Mx = maxwell, G = gauss, Oe = oersted; Wb = weber, V = volt, s = second, T = tesla, m = meter, A = ampere, J = joule, kg = kilogram, H = henry.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Multipart figures", "weight": 1.0} -->

Figures compiled of more than one sub-figure presented side-by-side, or stacked. If a multipart figure is made up of multiple figure types (one part is linear, and another is grayscale or color) the figure should meet the stricter guidelines.

<!-- chunk {"id": "body-0037", "role": "body", "section": "File Formats For Graphics", "weight": 1.0} -->

Format and save your graphics using a suitable graphics processing program that will allow you to create the images as PostScript (PS), Encapsulated PostScript (.EPS), Tagged Image File Format (.TIFF), Portable Document Format (.PDF), Portable Network Graphics (.PNG), or Metapost (.MPS), sizes them, and adjusts the resolution settings. When submitting your final paper, your graphics should all be submitted individually in one of these formats along with the manuscript.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Sizing of Graphics", "weight": 1.0} -->

Most charts, graphs, and tables are one column wide (3.5 inches/88 millimeters/21 picas) or page wide (7.16 inches/181 millimeters/43 picas). The maximum depth a graphic can be is 8.5 inches (216 millimeters/54 picas). When choosing the depth of a graphic, please allow space for a caption. Figures can be sized between column and page widths if the author chooses, however it is recommended that figures are not sized less than column width unless when necessary.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Sizing of Graphics", "weight": 1.0} -->

There is currently one publication with column measurements that do not coincide with those listed above. Proceedings of the IEEE has a column measurement of 3.25 inches (82.5 millimeters/19.5 picas).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Sizing of Graphics", "weight": 1.0} -->

The final printed size of author photographs is exactly 1 inch wide by 1.25 inches tall (25.4 millimeters$\times$`<!-- -->`{=html}31.75 millimeters/6 picas$\times$`<!-- -->`{=html}7.5 picas). Author photos printed in editorials measure 1.59 inches wide by 2 inches tall (40 millimeters$\times$`<!-- -->`{=html}50 millimeters/9.5 picas$\times$`<!-- -->`{=html}12 picas).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Resolution", "weight": 1.0} -->

The proper resolution of your figures will depend on the type of figure it is as defined in the "Types of Figures" section. Author photographs, color, and grayscale figures should be at least 300dpi. Line art, including tables should be a minimum of 600dpi.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Vector Art", "weight": 1.0} -->

In order to preserve the figures' integrity across multiple computer platforms, we accept files in the following formats:.EPS/.PDF/.PS. All fonts must be embedded or text converted to outlines in order to achieve the best-quality results.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Color Space", "weight": 1.0} -->

The term color space refers to the entire sum of colors that can be represented within the said medium. For our purposes, the three main color spaces are Grayscale, RGB (red/green/blue) and CMYK (cyan/magenta/yellow/black). RGB is generally used with on-screen graphics, whereas CMYK is used for printing purposes.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Color Space", "weight": 1.0} -->

All color figures should be generated in RGB or CMYK color space. Grayscale images should be submitted in Grayscale color space. Line art may be provided in grayscale OR bitmap colorspace. Note that "bitmap colorspace" and "bitmap file format" are not the same thing. When bitmap color space is selected,.TIF/.TIFF/.PNG are the recommended file formats.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Accepted Fonts Within Figures", "weight": 1.0} -->

When preparing your graphics IEEE suggests that you use of one of the following Open Type fonts: Times New Roman, Helvetica, Arial, Cambria, and Symbol. If you are supplying EPS, PS, or PDF files all fonts must be embedded. Some fonts may only be native to your operating system; without the fonts embedded, parts of the graphic may be distorted or missing.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Accepted Fonts Within Figures", "weight": 1.0} -->

A safe option when finalizing your figures is to strip out the fonts before you save the files, creating "outline" type. This converts fonts to artwork what will appear uniformly on any screen.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Figure Axis labels", "weight": 1.0} -->

Multipliers can be especially confusing. Write "Magnetization (kA/m)" or "Magnetization (10^3^ A/m)." Do not write "Magnetization (A/m)$\times$`<!-- -->`{=html}1000" because the reader would not know whether the top axis label in Fig. 1 meant 16000 A/m or 0.016 A/m. Figure labels should be legible, approximately 8 to 10 point type.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Subfigure Labels in Multipart Figures and Tables", "weight": 1.0} -->

Multipart figures should be combined and labeled before final submission. Labels should appear centered below each subfigure in 8 point Times New Roman font in the format of (a) (b) (c).

<!-- chunk {"id": "body-0049", "role": "body", "section": "File Naming", "weight": 1.0} -->

Figures (line artwork or photographs) should be named starting with the first 5 letters of the author's last name. The next characters in the filename should be the number that represents the sequential location of this image in your article. For example, in author "Anderson's" paper, the first three figures would be named ander1.tif, ander2.tif, and ander3.ps.

<!-- chunk {"id": "body-0050", "role": "body", "section": "File Naming", "weight": 1.0} -->

Tables should contain only the body of the table (not the caption) and should be named similarly to figures, except that '.t' is inserted in-between the author's name and the table number. For example, author Anderson's first three tables would be named ander.t1.tif, ander.t2.ps, ander.t3.eps.

<!-- chunk {"id": "body-0051", "role": "body", "section": "File Naming", "weight": 1.0} -->

Author photographs should be named using the first five characters of the pictured author's last name. For example, four author photographs for a paper may be named: oppen.ps, moshc.tif, chen.eps, and duran.pdf.

<!-- chunk {"id": "body-0052", "role": "body", "section": "File Naming", "weight": 1.0} -->

If two authors or more have the same last name, their first initial(s) can be substituted for the fifth, fourth, third$\ldots$ letters of their surname until the degree where there is differentiation. For example, two authors Michael and Monica Oppenheimer's photos would be named oppmi.tif, and oppmo.eps.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Referencing a Figure or Table Within Your Paper", "weight": 1.0} -->

When referencing your figures and tables within your paper, use the abbreviation "Fig." even at the beginning of a sentence. Do not abbreviate "Table." Tables should be numbered with Roman Numerals.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Checking Your Figures: The IEEE Graphics Analyzer", "weight": 1.0} -->

The IEEE Graphics Analyzer enables authors to pre-screen their graphics for compliance with IEEE Transactions and Journals standards before submission. The online tool, located at allows authors to upload their graphics in order to check that each file is the correct file format, resolution, size and colorspace; that no fonts are missing or corrupt; that figures are not compiled in layers or have transparency, and that they are named according to the IEEE Transactions and Journals naming convention. At the end of this automated process, authors are provided with a detailed report on each graphic within the web applet, as well as by email.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Checking Your Figures: The IEEE Graphics Analyzer", "weight": 1.0} -->

For more information on using the Graphics Analyzer or any other graphics related topic, contact the IEEE Graphics Help Desk by e-mail at graphics@ieee.org.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Submitting Your Graphics", "weight": 1.0} -->

Because IEEE will do the final formatting of your paper, you do not need to position figures and tables at the top and bottom of each column. In fact, all figures, figure captions, and tables can be placed at the end of your paper. In addition to, or even in lieu of submitting figures within your final manuscript, figures should be submitted individually, separate from the manuscript in one of the file formats listed above in Section 4.3"). Place figure captions below the figures; place table titles above the tables. Please do not include captions as part of the figures, or put them in "text boxes" linked to the figures. Also, do not place borders around the outside of your figures.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Color Processing/Printing in IEEE Journals", "weight": 1.0} -->

All IEEE Transactions, Journals, and Letters allow an author to publish color figures on IEEE Xplore® at no charge, and automatically convert them to grayscale for print versions. In most journals, figures and tables may alternatively be printed in color if an author chooses to do so. Please note that this service comes at an extra expense to the author. If you intend to have print color graphics, include a note with your final paper indicating which figures or tables you would like to be handled that way, and stating that you are willing to pay the additional fee.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

A conclusion section is not required. Although a conclusion may review the main points of the paper, do not replicate the abstract as the conclusion. A conclusion might elaborate on the importance of the work or suggest applications and extensions.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Appendixes, if needed, appear before the acknowledgment.
