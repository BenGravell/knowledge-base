<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Planning by Simulation: Motion Planning with Learning-Based Parallel Scenario Prediction for Autonomous Driving

Topics include Autonomous driving, Motion planning, Scenario generation, Simulation, Trajectory prediction.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces Planning by Simulation, where parallel learned scenario prediction evaluates candidate ego plans by simulating how surrounding agents may respond. The paper targets the feedback loop between planning and prediction rather than treating forecast accuracy as a standalone objective.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Planning safe trajectories for autonomous vehicles is essential for operational safety but remains extremely challenging due to the complex interactions among traffic participants. Recent autonomous driving frameworks have focused on improving prediction accuracy to explicitly model these interactions. However, some methods overlook the significant influence of the ego vehicle's planning on the possible trajectories of other agents, which can alter prediction accuracy and lead to unsafe planning decisions. In this paper, we propose a novel motion Planning approach by Simulation with learning-based parallel scenario prediction (PS). PS deduces predictions iteratively based on Monte Carlo Tree Search (MCTS), jointly inferring scenarios that cooperate with the ego vehicle's planning set. Our method simulates possible scenes and calculates their costs after the ego vehicle executes potential actions. To balance and prune unreasonable actions and scenarios, we adopt MCTS as the foundation to explore possible future interactions encoded within the prediction network. Moreover, the query-centric trajectory prediction streamlines our scene generation, enabling a sophisticated framework that captures the mutual influence between other agents' predictions and the ego vehicle's planning. We evaluate our framework on the Argoverse 2 dataset, and the results demonstrate that our approach effectively achieves parallel ego vehicle planning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This template provides authors with most of the formatting specifications needed for preparing electronic versions of their papers. All standard paper components have been specified for three reasons: ease of use when formatting individual papers, automatic compliance to electronic requirements that facilitate the concurrent or later production of electronic products, and conformity of style throughout a conference proceedings. Margins, column widths, line spacing, and type styles are built-; examples of the type styles are provided throughout this document and are identified in italic type, within parentheses, following the example. Some components, such as multi-leveled equations, graphics, and tables are not prescribed, although the various table text styles are provided. The formatter will need to create these components, incorporating the applicable criteria that follow.

<!-- chunk {"id": "body-0005", "role": "body", "section": "II-A Selecting a Template (Heading 2)", "weight": 1.0} -->

First, confirm that you have the correct template for your paper size. This template has been tailored for output on the US-letter paper size. It may be used for A4 paper size if the paper size setting is suitably modified.

<!-- chunk {"id": "body-0006", "role": "body", "section": "II-B Maintaining the Integrity of the Specifications", "weight": 1.0} -->

The template is used to format your paper and style the text. All margins, column widths, line spaces, and text fonts are prescribed; please do not alter them. You may note peculiarities. For example, the head margin in this template measures proportionately more than is customary. This measurement and others are deliberate, using specifications that anticipate your paper as one part of the entire proceedings, and not as an independent document. Please do not revise any of the current designations

<!-- chunk {"id": "body-0007", "role": "body", "section": "MATH", "weight": 1.0} -->

Before you begin to format your paper, first write and save the content as a separate text file. Keep your text and graphic files separate until after the text has been formatted and styled. Do not use hard tabs, and limit use of hard returns to only one return at the end of a paragraph. Do not add any kind of pagination anywhere in the paper. Do not number text heads-the template will do that for you.

<!-- chunk {"id": "body-0008", "role": "body", "section": "MATH", "weight": 1.0} -->

Finally, complete content and organizational editing before formatting.

<!-- chunk {"id": "body-0009", "role": "body", "section": "III-A Abbreviations and Acronyms", "weight": 1.0} -->

Define abbreviations and acronyms the first time they are used in the text, even after they have been defined in the abstract. Abbreviations such as IEEE, SI, MKS, CGS, sc, dc, and rms do not have to be defined. Do not use abbreviations in the title or heads unless they are unavoidable.

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-B Units", "weight": 1.0} -->

Use either SI (MKS) or CGS as primary units. (SI units are encouraged.) English units may be used as secondary units (in parentheses). An exception would be the use of English units as identifiers in trade, such as Ò3.5-inch disk driveÓ.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-B Units", "weight": 1.0} -->

Avoid combining SI and CGS units, such as current in amperes and magnetic field in oersteds. This often leads to confusion because equations do not balance dimensionally. If you must use mixed units, clearly state the units for each quantity that you use in an equation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-B Units", "weight": 1.0} -->

Do not mix complete spellings and abbreviations of units: ÒWb/m2Ó or Òwebers per square meterÓ, not Òwebers/m2Ó. Spell out units when they appear in text: Ò... a few henriesÓ, not Ò... a few HÓ.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-B Units", "weight": 1.0} -->

Use a zero before decimal points: Ò0.25Ó, not Ò.25Ó. Use Òcm3Ó, not ÒccÓ. (bullet list)

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-C Equations", "weight": 1.0} -->

The equations are an exception to the prescribed specifications of this template. You will need to determine whether or not your equation should be typed using either the Times New Roman or the Symbol font (please no other font). To create multileveled equations, it may be necessary to treat the equation as a graphic and insert it into the text after your paper is styled. Number equations consecutively. Equation numbers, within parentheses, are to position flush right, as, using a right tab stop. To make your equations more compact, you may use the solidus (/), the exp function, or appropriate exponents. Italicize Roman symbols for quantities and variables, but not Greek symbols. Use a long dash rather than a hyphen for a minus sign. Punctuate equations with commas or periods when they are part of a sentence, as in Note that the equation is centered using a center tab stop. Be sure that the symbols in your equation have been defined before or immediately following the equation. Use ÒÓ, not ÒEq. Ó or Òequation Ó, except at the beginning of a sentence: ÒEquation is...Ó

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-D Some Common Mistakes", "weight": 1.0} -->

The word ÒdataÓ is plural, not singular.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-D Some Common Mistakes", "weight": 1.0} -->

The subscript for the permeability of vacuum ?0, and other common scientific constants, is zero with subscript formatting, not a lowercase letter ÒoÓ.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-D Some Common Mistakes", "weight": 1.0} -->

In American English, commas, semi-/colons, periods, question and exclamation marks are located within quotation marks only when a complete thought or name is cited, such as a title or full quotation. When quotation marks are used, instead of a bold or italic typeface, to highlight a word or phrase, punctuation should appear outside of the quotation marks. A parenthetical phrase or statement at the end of a sentence is punctuated outside of the closing parenthesis (like this). (A parenthetical sentence is punctuated within the parentheses.)

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-D Some Common Mistakes", "weight": 1.0} -->

A graph within a graph is an ÒinsetÓ, not an ÒinsertÓ. The word alternatively is preferred to the word ÒalternatelyÓ (unless you really mean something that alternates).

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-D Some Common Mistakes", "weight": 1.0} -->

Do not use the word ÒessentiallyÓ to mean ÒapproximatelyÓ or ÒeffectivelyÓ.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-D Some Common Mistakes", "weight": 1.0} -->

In your paper title, if the words Òthat usesÓ can accurately replace the word ÒusingÓ, capitalize the ÒuÓ; if not, keep using lower-cased.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-D Some Common Mistakes", "weight": 1.0} -->

Be aware of the different meanings of the homophones ÒaffectÓ and ÒeffectÓ, ÒcomplementÓ and ÒcomplimentÓ, ÒdiscreetÓ and ÒdiscreteÓ, ÒprincipalÓ and ÒprincipleÓ.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-D Some Common Mistakes", "weight": 1.0} -->

Do not confuse ÒimplyÓ and ÒinferÓ.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-D Some Common Mistakes", "weight": 1.0} -->

The prefix ÒnonÓ is not a word; it should be joined to the word it modifies, usually without a hyphen.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-D Some Common Mistakes", "weight": 1.0} -->

There is no period after the ÒetÓ in the Latin abbreviation Òet al.Ó.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-D Some Common Mistakes", "weight": 1.0} -->

The abbreviation Òi.e.Ó means Òthat isÓ, and the abbreviation Òe.g.Ó means Òfor exampleÓ.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

Use this sample document as your LaTeX source file to create your document. Save this file as root.tex. You have to make sure to use the cls file that came with this distribution. If you use a different style file, you cannot expect to get required margins. Note also that when you are creating your out PDF file, the source file is only part of the equation. Your TeX $\rightarrow$ PDF filter determines the output file size. Even if you make all the specifications to output a letter file in the source - if your filter is set to produce A4, you will only get A4 output.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

It is impossible to account for all possible situation, one would encounter using TeX. If you are using multiple TeX files you must make sure that the "MAIN" source file is called root.tex - this is particularly important if your conference is using PaperPlaza's built in TeX to PDF conversion tool.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A Headings, etc", "weight": 1.0} -->

Text heads organize the topics on a relational, hierarchical basis. For example, the paper title is the primary text head because all subsequent material relates and elaborates on this one topic. If there are two or more sub-topics, the next level head (uppercase Roman numerals) should be used and, conversely, if there are not at least two sub-topics, then no subheads should be introduced. Styles named ÒHeading 1Ó, ÒHeading 2Ó, ÒHeading 3Ó, and ÒHeading 4Ó are prescribed.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Figures and Tables", "weight": 1.0} -->

Positioning Figures and Tables: Place figures and tables at the top and bottom of columns. Avoid placing them in the middle of columns. Large figures and tables may span across both columns. Figure captions should be below the figures; table heads should appear above the tables. Insert figures and tables after they are cited in the text. Use the abbreviation ÒFig. 1Ó, even at the beginning of a sentence.

<!-- chunk {"id": "body-0030", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

A conclusion section is not required. Although a conclusion may review the main points of the paper, do not replicate the abstract as the conclusion. A conclusion might elaborate on the importance of the work or suggest applications and extensions.
