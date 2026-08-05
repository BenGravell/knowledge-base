<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Newton Methods for K-order Markov Constrained Motion Problems

Topics include Robotics, Optimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This is a documentation of a framework for robot motion optimization that aims to draw on classical constrained optimization methods. With one exception the underlying algorithms are classical ones: Gauss-Newton (with adaptive step size and damping), Augmented Lagrangian, log-barrier, etc. The exception is a novel any-time version of the Augmented Lagrangian. The contribution of this framework is to frame motion optimization problems in a way that makes the application of these methods efficient, especially by defining a very general class of robot motion problems while at the same time introducing abstractions that directly reflect the API of the source code.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Paper Body", "weight": 1.0} -->

#1%$\blacktriangleleft~~$

<!-- chunk {"id": "body-0004", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\newcommand{\mytitle}{\title\newcommand{\thetitle}}%\@title} \newcommand{\header}{\begin{document}\mytitle\cleardefs} \newcommand{\contents}{{\tableofcontents}\renewcommand{\contents}{}} \newcommand{\footer}{\small\bibliography{marc,bibs}\end{document}} \newcommand{\widepaper}{\usepackage{geometry}\geometry{a4paper,hdivide={25mm,*,25mm},vdivide={25mm,*,25mm}}} \newcommand{\moviex}{\movie[externalviewer]} %\pdflatex\usepackage{multimedia} \newcommand{\rbox}{\fboxrule2mm\fcolorbox[rgb]{1,.85,.85}{1,.85,.85}}

<!-- chunk {"id": "body-0005", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\newcommand{\mpage}{{\begin{minipage}#2\end{minipage}}} \newcommand{\redbox}{\fboxrule1mm\fcolorbox[rgb]{1,.7,.7}{1,.7,.7}{\begin{minipage}\center#2\end{minipage}}} \begin{minipage}[c]#2\end{minipage}} \begin{minipage}[c]#4\end{minipage}\hspace*% \begin{minipage}[c]#5\end{minipage}} \begin{minipage}[c]#5\end{minipage}\hspace*% \begin{minipage}[c]#6\end{minipage}\hspace*% \begin{minipage}[c]#7\end{minipage}} \begin{minipage}[#1]#5\end{minipage}% \begin{minipage}[#1]#6\end{minipage}%

<!-- chunk {"id": "body-0006", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{minipage}[#1]#7\end{minipage}} \begin{minipage}[t]#5\end{minipage}\hspace*% \begin{minipage}[t]#6\end{minipage}\hspace*% \begin{minipage}[t]#7\end{minipage}} \begin{minipage}[c]#6\end{minipage}\hspace*% \begin{minipage}[c]#7\end{minipage}\hspace*% \begin{minipage}[c]#8\end{minipage}\hspace*% \begin{minipage}[c]#9\end{minipage}} \newcommand{\helvetica}{\setlength{\unitlength}{1pt}\fontsize\linespread\usefont{OT1}{phv}} \newcommand{\helve}{\helvetica{1.5}{m}{n}}

<!-- chunk {"id": "body-0007", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\renewcommand{\show}[.8]{\centerline{\includegraphics[width=#1\columnwidth]}} \newcommand{\showh}[.8]{\includegraphics[width=#1\columnwidth]} \newcommand{\shows}[.8]{\centerline{\includegraphics[scale=#1]}} \newcommand{\showhs}[.8]{\includegraphics[scale=#1]} \newcommand{\mov}{\movie[externalviewer]{{\color{blue}\small #1}}{movies/#2}}%\newcommand{\movgb}{\hfill\movie[externalviewer]{\small[movie]}{/home/mtoussai/movies/10-goalDirectedBehavior/#1}} \newcommand{\cen}{\centerline} \newenvironment{code}{\smallskip\newline%

<!-- chunk {"id": "body-0008", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{lrbox}{\@tempboxa}\begin{minipage}\helvetica{7}{1.1}{m}{n} \end{minipage}\end{lrbox}% \colorbox[rgb]{\usebox{\@tempboxa}}\smallskip\newline%\graphicspath{{pics/}{figs/}{~/write/tex/pics/}{~/write/tex/figs/}} \newcommand{\refeq}{(\ref)} \algrenewcommand{\algorithmicrequire}{\textbf{Input:~~}} \algrenewcommand{\algorithmicensure}{\textbf{Output:}} \algrenewcommand{\algorithmiccomment}{\qquad\hfill~\hspace*{-5ex}\textit{// #1}}

<!-- chunk {"id": "body-0009", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\algrenewcommand{\alglinenumber}{\helvetica{6}{1.3}{m}{n}#1:} \quad\begin{minipage}\helvetica{1.3}{m}{n} \medskip\hrule\medskip \medskip\hrule\medskip%% \renewcommand{\algorithmicrequire}{\textbf{Input:~~}}%% \renewcommand{\algorithmicensure}{\textbf{Output:}} \newcommand{\draft}{\usepackage[light,first]{draftcopy}\draftcopyName{draft}{350}} \newcommand{\labels}{\usepackage{showlabels}} \newcommand{\maple}{\usepackage{maple2e}} \newcommand{\makeidx}{\usepackage{makeidx}\makeindex}

<!-- chunk {"id": "body-0010", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\newcommand{\chicago}{\usepackage{chicago}\bibliographystyle{chicago} \renewcommand{\refname}{References\renewcommand{\refname}{}}} \newcommand{\natbib}{\usepackage[round]{natbib}\bibliographystyle{abbrvnat}} \usepackage[modulo]{lineno} %options: pagewise, modulo, mathlines \renewcommand{\BM}{\begin{linenomath}} \renewcommand{\EM}{\end{linenomath}} \definecolor{bluecol}{rgb}{0,0,.5} \definecolor{greencol}{rgb}{0,.4,0}%% backref, %link from bibliography back to sections%% pagebackref, %link from bibliography back to pages%% pdfstartview=FitH, %fitwidth instead of fit window pdfpagemode=UseNone, %UseOutlines, %bookmarks are displayed by acrobat

<!-- chunk {"id": "body-0011", "role": "body", "section": "Paper Body", "weight": 1.0} -->

pdfauthor={Marc Toussaint}%\renewcommand{\Chapter}{\chapter}%\renewcommand{\Subsection}{\subsection} \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{corollary}[theorem]{Corollary} \newtheorem{proposition}{Proposition} \newtheorem{conjecture}{Conjecture} \newtheorem{result}{Result}[section] \newtheorem{hypothesis}{Hypothesis}[section] \newtheorem{definition}{Definition} \newtheorem{remark}{Remark}[section] \newtheorem{example}{Example}[section] \newtheorem{algoTheo}{Algorithm} \newtheorem{testTheo}{Test} \renewcommand{\labelenumi}{\textbf{(\roman{enumi})}} \renewcommand{\theenumi}{(\roman{enumi})} %for

<!-- chunk {"id": "body-0012", "role": "body", "section": "Paper Body", "weight": 1.0} -->

ref%\renewcommand{\labelenumi}{${}^{\bf (\roman{enumi})}$}%\renewcommand{\labelitemi}{\bf $\cdot$} \newcommand{\itemdot}{\renewcommand{\labelitemi}{\bf $\cdot$}} \newcommand{\enumA}{\renewcommand{\labelenumi}{\textbf{\Alph{enumi}}}}%\setlength{\jot}{0pt} %zwischen den math zeilen% Lists and paragraphs \topsep 4pt plus 1pt minus 2pt \partopsep 1pt plus 0.5pt minus 0.5pt \itemsep 2pt plus 1pt minus 0.5pt \parsep 2pt plus 1pt minus 0.5pt \parskip.5pc %add \_in\_ {thebibliography} environment in *.bbl

<!-- chunk {"id": "body-0013", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\geometry{a4paper,hdivide={35mm,*,35mm},vdivide={35mm,*,35mm}} \renewcommand{\headrulewidth}\renewcommand{\footrulewidth}\cfoot{} \fancyhead[OL,EC]{\it\theauthor---\today}%\usepackage{layout}\layout {\vspace*{5ex}\begin{rblock}\hrule\vspace{1.5ex}{\bf Abstract.~}\small} {\vspace{2ex}\hrule\end{rblock}\vspace{5ex}} \begin{list}{}{\leftmargin3ex \rightmargin3ex \topsep0ex \parsep0ex}\item {\fontsize{18}{25}\selectfont{\thetitle\\}}\vspace{5ex}

<!-- chunk {"id": "body-0014", "role": "body", "section": "Paper Body", "weight": 1.0} -->

{\fontsize{14}{16}\selectfont{\theauthor\\}}\vspace{1ex} {\footnotesize{\sl \addressFUB}\\ \emailBerlin} \renewcommand{\maketitle}{\chapter{\thetitle}}% \documentclass[#1pt,fleqn,twoside]{article} \documentclass[10pt,twocolumn,fleqn]{article} \geometry{a4paper,headsep=7mm,hdivide={15mm,*,15mm},vdivide={20mm,*,15mm}} \fancyhead[OL,ER]{\thetitle, \textit{Marc Toussaint}---\today} \usepackage{nips07submit\_e,times}%\usepackage{nips06,times}

<!-- chunk {"id": "body-0015", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\documentclass[10pt,twocolumn]{ijcnn}%\documentclass[10pt,twocolumn]{article}\usepackage{wcci} \documentclass{springer\_llncs} \renewcommand{\theenumi}{\alph{enumi}} \renewcommand{\labelenumi}{(\alph{enumi})} \renewcommand{\labelitemi}{$\bullet$} \documentclass[journal,twoside]{IEEEtran} \renewcommand{\theenumi}{\roman{enumi}} \renewcommand{\labelenumi}{(\roman{enumi})}%\renewcommand{\labelitemi}{$\bullet$} \bibliographystyle{IEEEtran.bst} \documentclass[a4paper, 10pt, conference]{ieeeconf} \bibliographystyle{IEEEtran.bst} \renewcommand{\theenumi}{\roman{enumi}}

<!-- chunk {"id": "body-0016", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\renewcommand{\labelenumi}{(\roman{enumi})} \documentclass[#1pt,twoside,fleqn]{book} \newenvironment{abstract}{\begin{rblock}{\bf Abstract.~}\small}{\end{rblock}}%\renewcommand{\thechapter}{\Roman{chapter}} \renewcommand{\familydefault}{\sfdefault}

<!-- chunk {"id": "body-0017", "role": "body", "section": "Paper Body", "weight": 1.0} -->

#1

<!-- chunk {"id": "body-0018", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\mbox{}~\hfill Prof.\ Dr.\ Marc Toussaint\\\mbox{}~\hfill Freie Universit\"at Berlin\\\mbox{}~\hfill Arnimallee 7\\\mbox{}~\hfill 14195 Berlin, Germany\\\mbox{}~\hfill marc-toussaint@fu-berlin.de% \mbox{}~\hfill Honda Research Institute Europe\\% \mbox{}~\hfill Carl-Legien-Strasse 30\\% \mbox{}~\hfill 63073 Offenbach/Main\\% \mbox{}~\hfill Telefon: ++49-69-89011-717\\% %\mbox{}~\hfill 10117 Berlin\\% %\mbox{}~\hfill Telefon: +49-30-39494-833\\% \mbox{}~\hfill

<!-- chunk {"id": "body-0019", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Christian Goerick%Honda Research Institute Europe GmbH%63073 Offenbach/Main Fax: ++49 69 89011-759%Christian.Goerick@honda-ri.de \vspace*{5mm}\hfill #3, \today\\\newcommand{\thepage}{\arabic{mypage}} \documentclass[t,hyperref={bookmarks=true}]{beamer} \usefonttheme[onlymath]{serif} \setbeamertemplate{navigation symbols}{} \setbeamersize{text margin left=5mm} \setbeamersize{text margin right=5mm} \setbeamertemplate{itemize items}{{\color{black}$\bullet$}}%%% geometry/spacing issues \definecolor{bluecol}{rgb}{0,0,.5}

<!-- chunk {"id": "body-0020", "role": "body", "section": "Paper Body", "weight": 1.0} -->

#1 \\

<!-- chunk {"id": "body-0021", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Machine Learning \& Robotics Lab -- University of Stuttgart\\marc.toussaint@informatik.uni-stuttgart.de%\includegraphics[scale=.1]{pics/eushield-fullcolour} \begin{itemize}\item~\\

<!-- chunk {"id": "body-0022", "role": "body", "section": "Paper Body", "weight": 1.0} -->

#4

<!-- chunk {"id": "body-0023", "role": "body", "section": "Paper Body", "weight": 1.0} -->

#3

<!-- chunk {"id": "body-0024", "role": "body", "section": "Paper Body", "weight": 1.0} -->

#2

<!-- chunk {"id": "body-0025", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\incpage\begin{frame}%\addtocontents{toc}{\protect\contentsline{section}{\protect\numberline{\thepage}#1}{\thepage}{section.\thepage}}%\addtocontents{toc}{\contentsline{section}{section.\thepage}} \addcontentsline{toc}{section}% \centerline{\headerfont #1} \vspace*{-2ex} \begin{itemize}\item~\\

<!-- chunk {"id": "body-0026", "role": "body", "section": "Paper Body", "weight": 1.0} -->

#2

<!-- chunk {"id": "body-0027", "role": "body", "section": "Paper Body", "weight": 1.0} -->

#2

<!-- chunk {"id": "body-0028", "role": "body", "section": "Paper Body", "weight": 1.0} -->

#2

<!-- chunk {"id": "body-0029", "role": "body", "section": "Paper Body", "weight": 1.0} -->

#2

<!-- chunk {"id": "body-0030", "role": "body", "section": "Paper Body", "weight": 1.0} -->

#2

<!-- chunk {"id": "body-0031", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\documentclass[fleqn]{article}%\textheight 108cm % Paper=???, banner=5cm \renewcommand{\labelitemi}{\rule[.4ex]~} \definecolor{grey}{rgb} \definecolor{main}{rgb}{1,1,1} \author{Marc Toussaint} \newcommand{\inilogo}[.25]{\includegraphics[scale=#1]{INI}} \newcommand{\rublogo}[.25]{\includegraphics[scale=#1]{RUB}} \newcommand{\edinlogo}[.25]{\includegraphics[scale=#1]{pics/eushield-fullcolour}}%\newcommand{\edinlogo}[.25]{\includegraphics[scale=#1]{pics/eushield}} Institute for Theoretical Physics\\{\tt www.thp.uni-koeln.de/\~{}mt/}

<!-- chunk {"id": "body-0032", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\newcommand{\emailINI}{mt@neuroinformatik.ruhr-uni-bochum.de} \newcommand{\urlINI}{\texttt{www.neuroinformatik.rub.de/PEOPLE/mt/}} \newcommand{\emailANC}{mtoussai@inf.ed.ac.uk} \newcommand{\urlANC}{homepages.inf.ed.ac.uk/mtoussai} Institute for Adaptive and Neural Computation,\\University of Edinburgh, 5 Forrest Hill,\\%Institute~for~Adaptive~and~Neural~Computation\\University~of~Edinburgh, 5~Forrest~Hill\\Machine Learning \& Robotics group\\Machine~Learning~\&~Robotics~group, TU~Berlin\\\small Franklinstr.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Paper Body", "weight": 1.0} -->

28/29,~FR~6-9, 10587~Berlin, Germany Machine~Learning~\&~Robotics~lab, FU~Berlin\\\small Arnimallee 7, 14195~Berlin, Germany Machine~Learning~\&~Robotics~lab, U~Stuttgart\\\small Universit{\"a}tsstra{\ss}e 38, 70569~Stuttgart, Germany \newcommand{\emailBerlin}{mtoussai@cs.tu-berlin.de} Honda Research Institute Europe\\Honda~Research~Institute~Europe~GmbH,\\\small Carl-Legien-Strasse~30, 63073~Offenbach/Main% special sectioning, markings, environments, commands \protect\setlength{\subsecwidth}{\textwidth}\protect\addtolength{\subsecwidth}{-27ex} \protect\vspace*{-1.5ex}\protect\hspace*{20ex}

<!-- chunk {"id": "body-0034", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\protect\begin{minipage}[t]{\subsecwidth}\protect\footnotesize\protect\textsf\protect\end{minipage} \begin{rblock}\it #1\end{rblock}\medskip\noindent \addtocontents{toc}{\protect\bigskip} \chapter*\thispagestyle{empty} \addcontentsline{toc}{chapter}{\protect\numberline{}#1} \addcontentsline{toc}{section}{\protect\numberline{}#1} \addcontentsline{toc}{subsection}{\protect\numberline{}#1}% \begin{rblock}\it #1\end{rblock}\medskip% \addtocontents{toc}{\protect\begin{list}{}{\leftmargin9ex% \rightmargin9ex \topsep-2ex \parsep.5ex}}% \addtocontents{toc}{\protect\item

<!-- chunk {"id": "body-0035", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\newcommand{\Pref}{[\emph{\ref}\,]} \begin{list}{--}{\leftmargin4ex \rightmargin0ex \labelsep1ex \labelwidth2ex \topsep0pt \parsep0ex \itemsep0pt} \small%fontsize{9}{9}\linespread{1.2} \begin{list}{--}{\leftmargin4ex \rightmargin0ex \labelsep1ex \labelwidth2ex \topsep0pt \parsep0ex \itemsep3pt}% * \topsep amount of extra vertical space at top of list% * \partopsep extra length at top if environment is prececed by a blank line (it should be a rubber length)% * \itemsep amount of extra vertical space between items% * \parsep amount of vertical space between paragraphs within an item% * \leftmargin horizontal distance between the left margins of the environment and the list; must be nonnegative% * \rightmargin horizontal distance betwen the right margins of

<!-- chunk {"id": "body-0036", "role": "body", "section": "Paper Body", "weight": 1.0} -->

the enviroment and the list; must be nonnegative% * \listparindent amount of extra space for paragraph indent after the first in an item; can be negative% * \itemindent indentation of first line of an item; can be negative% * \labelsep separation between end of the box containing the label and the text of the first line of an item% * \labelwidth normal width of the box containing the label; if the actual label is bigger, the natural width is used, extending into the space for the first line of the item's text% * \makelabel{label} generates the label printed by the \item command% * \usecounter{ctr} enables the counter ctr to be used for% numbering items; it is initialized to zero and stepped when% executing an \item command that has no optional label argument.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\newenvironment{block}{{\noindent\bf #1} \begin{list}{}{\leftmargin\blockindent \topsep-\parskip} \begin{list}{}{\leftmargin\blockindent \rightmargin\blockindent \topsep-\parskip}\item}{\end{list}}%\renewcommand{\thealgoi}{\textbf{\arabic{enumi}.}}%\newcommand{\labelenumi}{\textbf{(\roman{enumi})}} \begin{list}{{(\thealgoi)}} {\usecounter{algoi} \leftmargin7ex \rightmargin3ex \labelsep1ex \labelwidth5ex \topsep-.5ex \parsep.5ex \itemsep0pt} \end{list}\vspace*{1ex}%% \begin{algoTheo}[#1]~\begin{algoList}%%

<!-- chunk {"id": "body-0038", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\end{algoList}\end{algoTheo} \medskip\begin{testTheo}[#1]~\begin{algoList} \end{algoList}\end{testTheo} \begin{list}{\textbf{\thealgoi.}} {\usecounter{algoi} \leftmargin2ex \rightmargin0ex \labelsep1ex \labelwidth1ex \topsep0ex \parsep.5ex \itemsep0pt} \item[\textsf{Q\thequesti:}]%\newenvironment{keywords}{\paragraph{Keywords}\begin{rblock}\small}{\end{rblock}} \begin{minipage}{\columnwidth} \begin{list}{}{\leftmargin3ex \topsep0ex \itemsep0ex} \begin{quote} \begin{picture} \end{picture} \end{quote} \begin{bibunit}[chicago]

<!-- chunk {"id": "body-0039", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\renewcommand{\refname}{\vspace{-\parskip}} \let\chapter\phantom \let\section\phantom \end{bibunit}%use \setcounter{enumiv}{xx} in thebibliography environment%\newcommand{\theauthor}{Marc Toussaint}%\renewcommand{\author}{\renewcommand{\theauthor}}%\@author}%\renewcommand{\title}{\newcommand{\thetitle}}%\@title} \newcommand{\boxpage}[\textwidth]{ \renewcommand{\theequation}{A.\arabic{equation}}

<!-- chunk {"id": "body-0040", "role": "body", "section": "Paper Body", "weight": 1.0} -->

#2

<!-- chunk {"id": "body-0041", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\noindent \textit{Proof.~} language=C, % choose the language of the code basicstyle=\normalfont\small, % the size of the fonts that are used for the code frame=none, % adds a frame around the code tabsize=4, % sets default tabsize to 2 spaces captionpos=b, % sets the caption-position to bottom numbers=left, numberstyle=\footnotesize, stepnumber=1, numbersep=3ex
