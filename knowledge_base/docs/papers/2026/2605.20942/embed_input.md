<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Bridging Structure and Language: Graph-Based Visual Reasoning for Autonomous Road Understanding

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Structured road understanding of lane geometry, topology, and traffic element relationships is foundational to safe autonomous driving. While vision-language models (VLMs) offer promising semantic flexibility, they lack the geometric and relational grounding required for precise road reasoning. Conversely, traditional modular systems, e.g., HD maps and topological road graphs, provide structural precision but remain semantically rigid. To bridge this gap, we introduce the Combined Road Substrate (CRS), a graph-grounded framework that makes geometric road structure and open-vocabulary semantics jointly executable in a single representation. CRS enables the automatic generation of compositionally complex and linguistically varied question-answer pairs via recursive graph queries, augmented with a "grounding for free" mechanism that ensures logical traceability to specific map elements, and procedurally extracted chain-of-thought supervision traces. We demonstrate that state-of-the-art VLMs - including large, closed-source models - struggle significantly with structured road reasoning, yet training a small 2- or 4-billion-parameter model with as few as 20 to 80 CRS-enriched scenes yields stable gains in compositional reasoning tasks of varying depth.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Analysis of model behavior via verifiable reasoning traces reveals a systematic shift in failure modes: whereas baseline models fail at relational scene understanding, CRS-trained models reduce failures to attribute recognition, suggesting that the primary bottleneck in road understanding is not model scale, but the absence of structured supervision.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

For self-driving cars to operate safely, they must be able to reason about the roads they are onunderstanding lane structure and geometry, interconnectivity, and relationships between traffic elements such as signs and lightsto determine what behaviors are permitted. This geometrical and relational substrate’’ of road understanding forms the foundation for downstream decision-making, and has motivated extensive work in road map prediction [li2022hdmapnet,liu2023vectormapnet,liao2022maptr], topology reasoning [wang2023openlane,li2023graph], and methods for incorporating high- and standard-definition maps into downstream tasks [yang2018hdnet]. In such pipelines, structured road understanding is explicitly represented and can be directly supervised.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

More recently, however, end-to-end driving approaches [casas2021mp3, hu2023planning] have gained traction, learning policies that map observations directly to actions. While effective, these methods often do not rely on explicit intermediate road representations, obscuring the causal link between road structure and vehicle behavior. Similarly, foundation models such as vision-language models (VLMs) [liu2023visual, bai2023qwen] exhibit strong generalist capabilities, but often rely on coarse visual and semantic correlations, without explicit mechanisms to ensure precise geometric and relational grounding required for road reasoning [deitke2025molmo, chen2026babyvision, stanfordhai2026technical].

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

At the same time, VLMs offer a unique opportunity. Unlike modular approaches, which rely on fixed schemas and often compress road structure into predefined, vectorized representations (HD maps, road graphs), VLMs support open-vocabulary reasoning and capture long-tail, semantically rich scene details such as faded markings, temporary changes, or ambiguous road configurations [radford2021learning,alayrac2022flamingo,addepalli2024leveraging]. We hence identify a fundamental representation gap: traditional modular systems are structurally precise but semantically rigid, whereas VLMs today are semantically flexible but structurally ungrounded. The challenge is therefore not only to recover the geometrical and topological “substrate” of road understanding in modular approaches, but to extend it beyond the constraints of traditional representations by combining geometric precision with semantic flexibility.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this, we introduce the Combined Road Substrate (CRS), a graph-grounded supervision framework for visual reasoning in road scenes. By enforcing a fixed compositional structure while allowing open-vocabulary semantic instantiationand crucially, by making both directly queryable in a single graph representationthe CRS ensures that semantic expressivity remains grounded, and constrained, the underlying road structure. Concretely, reasoning tasks are formulated as queries over the spatio-temporal graph, allowing extraction of precise, compositional, and verifiable supervision signals in natural language in the form of question-answer pairs with hard negative mining. In moving beyond simple QA extraction, the CRS framework enables two key technical capabilities. First, it introduces a grounding for free mechanism via Recursive Uniqueness, which ensures that every generated reasoning task remains logically traceable to specific map elements with unambiguous spatial anchoring. Second, it allows for procedural extraction of the Chain-of-Thought (CoT), providing a verifiable supervision trace to align the model’s internal reasoning process.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that while even massive closed-source models [google2026gemini31,openai2026gpt54,anthropic2025claudesonnet45] struggle to reason about complex road scenes, training on a remarkably small set (20–80) of CRS-enriched scenes enables VLMs to overcome inherent struggles with road understanding, achieving stable gains in compositional reasoning tasks of varying reasoning depth. Leveraging the verifiable CoT traces provided by CRS, we further analyze model behavior and localize reasoning failures to specific stages of the reasoning process. This reveals a systematic shift in failure modes: whereas standard models fail predominantly at relational reasoning (\textit{i.e.}\@, navigating the scene structure), failures in models trained with CRS are no longer caused primarily by lack of scene understanding, but reduced to failures in attribute recognition (\textit{i.e.}\@, visual perception). Taken together, these findings suggest that the key bottleneck in structured road understanding is not model scale, but the lack of structured supervision.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

- We introduce the Combined Road Substrate (CRS), a graph-based representation that unifies geometric structure and open-vocabulary semantics in a jointly executable form, enabling grounded and compositional reasoning over road scenes. - To make the CRS executable, we formulate reasoning tasks as recursive queries over the graph, enabling automatic generation of compositionally complex question–answer pairs with hard negatives. Grounding comes for free via recursive uniqueness, and verifiable CoT traces are derived directly from the graph in natural language. - We demonstrate that state-of-the-art VLMs struggle with structured road understanding, and that training a smaller model on as few as 20–80 CRS-enriched scenes yields substantial gains in compositional reasoning, indicating that the key bottleneck in road understanding is structured supervision rather than model scale.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

To couple the compositional structure required for reasoning (\textit{e.g.}\@, the lane that is left of the ego lane) with the semantic flexibility needed to capture real-world complexity in road reasoning, we introduce the Combined Road Substrate, a graph-based scene representation that makes structure and semantics jointly executable. Concretely, our framework consists of four key components: (i)graph primitives that define the minimal formal structure of the graph representation, (ii)canonical operators that act as an interface between the graph primitives and the open vocabulary language space that provides the content of the graph, (iii)well-posedness constraints that ensure linguistic references to graph elements are unambiguous, hence reasoning over the graph is executable; and (iv) a query instantiation mechanismthat defines reasoning tasks as structured answer retrieval through search queries over the graph, while mining hard negatives and chain-of-thought reasoning traces within the same framework.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}[\n box/.style={\n draw,\n fill=teal!100!black,\n text=white,\n align=center,\n inner sep=6pt,\n minimum height=2.2cm,\n text width=#1\n },\n graphbox/.style={\n draw,\n fill=teal!100!black,\n align=center,\n inner sep=4pt,\n minimum height=2.7cm,\n text width=#1\n },\n arrow/.style={-{Latex[length=3mm]}, thick}\n]\n\n\n\n% IMAGES\n% IMAGES: 3 stacked copies\n\\foreach \\i/\\dx/\\dy/\\op in {\n 1/0mm/0mm/0.1,\n 2/1mm/-1mm/0.2,\n

<!-- chunk {"id": "body-0012", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

3/2mm/-2mm/1\n} {\n\\node[\n draw=none,\n fill=none,\n align=center,\n inner sep=0pt,\n anchor=north west,\n opacity=\\op \n] (A\\i) at (\\dx,\\dy) {%\n\\scalebox{0.85}{%\n\\begin{minipage}[t]{0.18\\linewidth}\n\\centering\n\n% ===== Top full-width image =====\n\\begin{tikzpicture}\n\\node[inner sep=0, anchor=south west] (img) at {\n \\includegraphics[width=\\linewidth,height=3.3cm]{figures/method/center.png}\n};\n\n\\begin{scope}[x={(img.south east)}, y={(img.north

<!-- chunk {"id": "body-0013", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

\\includegraphics[width=\\linewidth,height=0.8cm]{figures/method/right.png}\n};\n\\end{tikzpicture}\n\\end{minipage}\n\n\\end{minipage}%\n}%\n};\n}\n\\node[\n font=\\fontsize{5}{7}\\selectfont,\n text=_gray,\n anchor=north,\n align=center\n] (m) at ([yshift=-0.5pt]A3.south) {multi-frame multi-view images};\n\n% GRAPH PRIMITIVES\n\\node[\n draw=_gray,\n dashed,\n line width=0.25pt,\n fill=white,\n rounded corners=2pt,\n align=center,\n inner sep=2pt,\n anchor=north west\n] at ([xshift=0pt,yshift=-5pt]m.south west)

<!-- chunk {"id": "body-0014", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

(C) {%\n\\begin{minipage}[c][1.45cm][c]{0.18\\linewidth} % fixed height \n\\centering\n\\begin{tikzpicture}[\n >=Latex,\n edge/.style={-, thin, draw=_gray, solid},\n edgelabel/.style={font=\\fontsize{3.5}{4}\\selectfont, inner sep=0.3pt, _gray},\n titlebase/.style={\n rounded corners=2pt,\n align=center,\n font=\\fontsize{5}{7}\\selectfont,\n inner xsep=4pt,\n inner ysep=2pt,\n minimum width=0.6cm\n },\n bodybase/.style={\n rounded corners=2pt,\n align=center,\n font=\\fontsize{4}{5}\\selectfont,\n inner

<!-- chunk {"id": "body-0015", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

sep=1pt,\n minimum width=0.6cm\n },\n primitiveTitle/.style={titlebase, draw=none, fill=_gray},\n primitiveBody/.style={bodybase, draw=none, fill=_gray!20}\n]\n\n% Node n: title + body\n\\coordinate (n1-pos);\n\\node[primitiveBody, anchor=north] (n1)\n at ([yshift=0.005cm]n1-pos) {%\n \\rule{0pt}{7pt}\n type: \\scalebox{0.7}{$\\tau(n)$}\\\\\n properties: \\scalebox{0.7}{$P_t(n)$}\n};\n\\node[primitiveTitle, anchor=center] (n1-title)\n at (n1-pos) {\\textbf{Node

<!-- chunk {"id": "body-0016", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

draw=none,\n font=\\bfseries\\tiny,\n text=_gray,\n inner xsep=2pt,\n inner ysep=0.5pt,\n anchor=north west\n] at ([xshift=0pt,yshift=4.5pt]C.north west) {(3.1) graph primitives};\n\n% CANONICAL OPERATORS\n\\node[\n draw=none,\n inner sep=0pt,\n anchor=north west\n] (B) at ([xshift=3mm]A1.north east) {%\n\\begin{tikzpicture}\n\n% Parameters\n\\def\\W{0.65} % width\n\\def\\H{2.6} % height\n\\pgfmathsetmacro{\\dx}{\\H / tan} \n\n% Shape\n\\fill[_lightgray, rounded corners=2pt]\n (0,0-\\dx)\n

<!-- chunk {"id": "body-0017", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

-- (\\W,0)\n -- (\\W,\\H-\\dx)\n -- (0,\\H)\n -- cycle;\n\n% Text\n\\node[\n rotate=90,\n font=\\bfseries\\tiny,\n text=_gray,\n anchor=center\n] at (0.2*\\W,0.3*\\H) {(3.2) Canonical Operators};\n\n\\node[\n draw=none,\n fill=none,\n rounded corners=1pt,\n font=\\fontsize{5}{6}\\selectfont,\n text=_gray,\n inner xsep=1.5pt,\n inner ysep=1pt,\n minimum width=0.2cm\n] at (0.4*\\W,0.50*\\H) {$\\Phi_n$};\n\n\\node[\n draw=none,\n

<!-- chunk {"id": "body-0018", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

fill=none,\n rounded corners=1pt,\n font=\\fontsize{5}{6}\\selectfont,\n text=_gray,\n inner xsep=1.5pt,\n inner ysep=1pt,\n minimum width=0.2cm\n] at (0.4*\\W,0.35*\\H) {$\\Phi_p$};\n\n\\node[\n draw=none,\n fill=none,\n rounded corners=1pt,\n font=\\fontsize{5}{6}\\selectfont,\n text=_gray,\n inner xsep=1.5pt,\n inner ysep=1pt,\n minimum width=0.2cm\n] at (0.4*\\W,0.20*\\H) {$\\Phi_e$};\n\n\\end{tikzpicture}};\n\n% QUERY INSTANTIATION\n\\node[\n

<!-- chunk {"id": "body-0019", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

draw=none,\n dashed,\n line width=0.1pt,\n fill=_lightgray!0,\n rounded corners=2pt,\n anchor=north west,\n at=(A1.north east),\n xshift=2mm,\n align=left,\n inner xsep=0pt,\n inner ysep=0pt,\n text width=0.8\\textwidth,\n](X){%\n};\n\n%GRAPH\n\\node[\n draw=none,\n fill=none,\n align=center,\n inner sep=4pt,\n anchor=north west,\n at=(B.north east),\n yshift=2mm,\n xshift=-1mm\n] (D) {%\n\\begin{tikzpicture}[\n >=Latex,\n edge/.style={-, thin, draw=_gray},\n

<!-- chunk {"id": "body-0020", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

edgelabel/.style={font=\\fontsize{3.5}{4}\\selectfont, inner sep=0.3pt, _gray},\n titlebase/.style={\n rounded corners=2pt,\n align=center,\n font=\\fontsize{5}{7}\\selectfont,\n inner xsep=4pt,\ninner ysep=2pt,\n minimum width=0.6cm\n },\n bodybase/.style={\n rounded corners=2pt,\n align=center,\n font=\\fontsize{4}{5}\\selectfont,\n inner sep=1pt,\n minimum width=0.6cm\n },\n laneTitle/.style={titlebase, draw=none, fill=_darkyellow},\n laneBody/.style={bodybase, draw=none, fill=_darkyellow!20},\n trafficTitle/.style={titlebase, draw=none,

<!-- chunk {"id": "body-0021", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

fill=_orange},\n trafficBody/.style={bodybase, draw=none, fill=_orange!20},\n markingTitle/.style={titlebase, draw=none, fill=_green},\n markingBody/.style={bodybase, draw=none, fill=_green!20},\n lanelineTitle/.style={titlebase, draw=none, fill=_teal},\n lanelineBody/.style={bodybase, draw=none, fill=_teal!20},\n intersectionTitle/.style={titlebase, draw=none, fill=_pink},\n intersectionBody/.style={bodybase, draw=none, fill=_pink!20},\n truckTitle/.style={titlebase, draw=none, fill=_darkgreen},\n truckBody/.style={bodybase, draw=none, fill=_darkgreen!20},\n signTitle/.style={titlebase, draw=none, fill=_purple},\n

<!-- chunk {"id": "body-0022", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

signBody/.style={bodybase, draw=none, fill=_purple!20},\n vehicleTitle/.style={titlebase, draw=none, fill=_red},\n vehicleBody/.style={bodybase, draw=none, fill=_red!20},\n egoTitle/.style={titlebase, draw=none, fill=_gray},\n egoBody/.style={bodybase, draw=none, fill=_gray!20}\n]\n\n% --- With body ---\n\n\\coordinate (tl1-pos) at (2,3.62);\n\\node[trafficBody, anchor=north] (tl1)\n at ([yshift=0.005cm]tl1-pos) {%\n \\rule{0pt}{7pt}\\textcolor{_orange}{status\\uni:} green \\\\ \\textcolor{_orange}{location\\uni:} pole to the

<!-- chunk {"id": "body-0023", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

left};\n\\node[trafficTitle, anchor=center] (tl1-title)\n at (tl1-pos) {\\textbf{TrafficLight-1$^*$}};\n\\Pin{tl1-title}{P1}{_orange}\n\n\\coordinate (lane4-pos) at (1.9,2.55);\n\\node[laneBody, anchor=north] (lane4)\n at ([yshift=0.005cm]lane4-pos) {%\n \\rule{0pt}{7pt}\\textcolor{_darkyellow}{direction:} opposite\\\\\n \\textcolor{_darkyellow}{type:} bike};\n\\node[laneTitle, anchor=center] (lane4-title)\n at (lane4-pos)

<!-- chunk {"id": "body-0024", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

{\\textbf{Lane-4}};\n\\Pin{lane4-title}{P2}{_darkyellow}\n\n\\coordinate (lane1-pos) at (6.3,2.65);\n\\node[laneBody, anchor=north] (lane1)\n at ([yshift=0.005cm]lane1-pos) {%\n \\rule{0pt}{7pt}\\textcolor{_darkyellow}{type:} bike\\\\\n \\textcolor{_darkyellow}{description\\uni:} rightmost lane};\n\\node[laneTitle, anchor=center] (lane1-title)\n at (lane1-pos) {\\textbf{Lane-1}};\n\\Pin{lane1-title}{P3}{_darkyellow}\n\n\\coordinate (bus1-pos) at

<!-- chunk {"id": "body-0025", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

(5.8,0.5);\n\\node[vehicleBody, anchor=north] (bus1)\n at ([yshift=0.005cm]bus1-pos) {%\n \\rule{0pt}{7pt}\\textcolor{_red}{number\\uni:} 54D};\n\\node[vehicleTitle, anchor=center] (bus1-title)\n at (bus1-pos) {\\textbf{Bus-1$^*$}};\n\\Pin{bus1-title}{P4}{_red}\n\n\\coordinate (truck-pos) at (5.7,3.68);\n\\node[truckBody, anchor=north] (truck)\n at ([yshift=0.005cm]truck-pos) {%\n \\rule{0pt}{7pt}\\textcolor{_darkgreen}{variant\\uni:} construction};\n\\node[truckTitle,

<!-- chunk {"id": "body-0026", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

anchor=center] (truck-title)\n at (truck-pos) {\\textbf{Truck-1$^*$}};\n\\Pin{truck-title}{P5}{_darkgreen}\n\n\\coordinate (sign-pos) at (6.2,1.78);\n\\node[signBody, anchor=north] (sign)\n at ([yshift=0.005cm]sign-pos) {%\n \\rule{0pt}{7pt}\\textcolor{_purple}{meaning\\uni:} no-left-turn};\n\\node[signTitle, anchor=center] (sign-title)\n at (sign-pos) {\\textbf{Sign-1}};\n\\Pin{sign-title}{P6}{_purple}\n\n\\coordinate (line1-pos) at (4.4,0.95);\n\\node[lanelineBody, anchor=north]

<!-- chunk {"id": "body-0027", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

(line1)\n at ([yshift=0.005cm]line1-pos) {%\n \\rule{0pt}{7pt}\\textcolor{_teal}{style\\uni:} double-solid\\\\\n \\textcolor{_teal}{color\\uni:} yellow};\n\\node[lanelineTitle, anchor=center] (line1-title)\n at (line1-pos) {\\textbf{LaneLine-1}};\n\\Pin{line1-title}{P7}{_teal}\n\n\\coordinate (mark1-pos);\n\\node[markingBody, anchor=north] (mark1)\n at ([yshift=0.005cm]mark1-pos) {%\n \\rule{0pt}{7pt}\\textcolor{_green}{type\\uni:} bike marking};\n\\node[markingTitle, anchor=center]

<!-- chunk {"id": "body-0028", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

(4,3.68);\n\\node[intersectionBody, anchor=north] (intersection1)\n at ([yshift=0.005cm]intersection-pos) {%\n \\rule{0pt}{7pt}\\textcolor{_pink}{type\\uni:} 1-way-stop};\n\\node[intersectionTitle, anchor=center] (intersection)\n at (intersection-pos) {\\textbf{Intersection-1$^*$}};\n\\Pin{intersection}{Q3}{_pink}\n\n\n% --- Edges ---\n\\draw[edge] (tl1) -- node[pos=0.7, above, sloped, edgelabel] {controls\\suni$\\rightarrow$} (lane2);\n\\draw[edge] (tl1) -- node[pos=0.8, above, sloped, edgelabel] {controls\\suni$\\rightarrow$}

<!-- chunk {"id": "body-0029", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

(lane1);\n\\begin{scope}[on background layer]\n\\draw[\n -, \n thin, \n draw=_gray\n]\n ([xshift=2mm]lane1.south west) -- node[pos=0.7,\n below,\n sloped,\n font=\\fontsize{3.5}{4}\\selectfont,\n inner sep=0.3pt,\n text=_gray\n] {is right of\\suni$\\rightarrow$}\n (bus1.north);\n\\end{scope}\n\\draw[edge] ([xshift=-1mm]sign.south east) -- node[above, sloped, edgelabel] {is controlled by\\suni$\\rightarrow$} (bus1-title);\n\\draw[edge] (lane3) -- node[above, sloped,edgelabel] {is left of\\suni$\\rightarrow$}

<!-- chunk {"id": "body-0030", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

(lane2);\n\\draw[edge] (lane1) -- node[above, sloped, edgelabel] {$\\leftarrow$is right of\\suni} (lane2);\n\\draw[edge] (sign) -- node[above, sloped, edgelabel] {$\\leftarrow$controls} (lane2);\n\\draw[edge] (sign) -- node[below, sloped, edgelabel] {is controlled by\\suni$\\rightarrow$} (lane2);\n\\draw[edge] (bus1-title) -- node[above, sloped, edgelabel] {$\\leftarrow$ is in\\suni} (lane2);\n\\draw[edge] (bus1-title) -- node[below, sloped, edgelabel] {contains\\suni $\\rightarrow$} (lane2);\n\\draw[edge] (ego) -- node[above, sloped, edgelabel] {is

<!-- chunk {"id": "body-0031", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

in\\suni$\\rightarrow$} (lane2);\n\\draw[edge] (ego) -- node[below, sloped, edgelabel] {$\\leftarrow$contains\\suni} (lane2);\n\\draw[edge] (line1-title) -- node[above, sloped, edgelabel] {$\\leftarrow$marks left of\\suni} (lane2);\n\\draw[edge] (mark1-title) -- node[below, sloped, edgelabel] {$\\leftarrow$controls\\suni} (lane4);\n\\draw[edge] (lane4) -- node[pos=0.3, above, sloped, edgelabel] {leaves$\\rightarrow$} (intersection1);\n\\draw[edge] (lane3) -- node[pos=0.3, above, sloped, edgelabel] {leaves$\\rightarrow$}

<!-- chunk {"id": "body-0032", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

(intersection1);\n\\draw[edge] (lane1) -- node[above, sloped, edgelabel] {$\\leftarrow$leads up to} (intersection1);\n\\draw[edge] (truck) -- node[above, sloped, edgelabel] {is right of\\suni$\\rightarrow$} (lane1-title);\n\n% --- Dotted graph envelope ---\n\\path (current bounding box.south) ++(0,-5mm) coordinate (dummy);\n\\useasboundingbox (current bounding box.north west) rectangle (dummy);\n\\end{tikzpicture}};\n\n% SELECTOR\n\\node[\n draw=none,\n fill=_lightgray!0,\n rounded corners=2pt,\n align=center,\n font=\\bfseries\\tiny,\n text=_gray,\n inner sep=0pt,\n minimum

<!-- chunk {"id": "body-0033", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

width=1.8cm,\n minimum height=0.01,\n anchor=west,\n rotate=90\n] (Selector) at ([xshift=0mm, yshift=0mm]D.south east) {};\n\n\n% SELECTED GRAPH NODES (title + body)\n\\node[\n draw=none,\n fill=_lightgray!40,\n rounded corners=1pt,\n inner sep=2pt,\n anchor=west\n] (SelectedNodes) at ([xshift=-0.02mm,yshift=0mm]Selector.south) {%\n\\begin{minipage}[t][1.5cm][c]{0.8cm}\n\\begin{tikzpicture}[\n titlebase/.style={\n rounded corners=2pt,\n align=center,\n font=\\fontsize{5}{7}\\selectfont,\n inner sep=2pt,\n minimum width=0.6cm\n

<!-- chunk {"id": "body-0034", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

},\n bodybase/.style={\n rounded corners=2pt,\n align=center,\n font=\\fontsize{4}{5}\\selectfont,\n inner sep=1pt,\n minimum width=0.6cm\n },\n laneTitle/.style={titlebase, draw=none, fill=_darkyellow},\n laneBody/.style={bodybase, draw=none, fill=_darkyellow!20}\n]\n\n\\node[\n font=\\fontsize{5}{7}\\selectfont,\n text=_gray,\n anchor=south\n] at (-0,0.55) {Selector $\\mathcal{S}$};\n\n% --- Lane-4 ---\n\\coordinate (l4);\n\\node[laneBody, anchor=north, fill=_darkyellow!10] (l4body)\n at

<!-- chunk {"id": "body-0035", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

([yshift=-0.125cm]l4)\n {type: bike};\n\\node[laneTitle, anchor=center, fill=_darkyellow!50] at (l4)\n {\\textbf{Lane-4}};\n\n% --- Lane-1 ---\n\\coordinate (l1) at (-0.15,-0.15);\n\\node[laneBody, anchor=north] (l1body)\n at ([yshift=-0.125cm]l1)\n {type: bike};\n\\node[laneTitle, anchor=center] at (l1)\n {\\textbf{Lane-1}};\n\n\\end{tikzpicture}\n \n\\end{minipage}\n};\n\n\\node[\n draw=none,\n inner sep=0pt,\n anchor=south west\n] (SelectorBoxes) at

<!-- chunk {"id": "body-0036", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

([xshift=0mm,yshift=0mm]SelectedNodes.south east) {%\n\\begin{tikzpicture}[\n smallbox/.style={\n draw=none,\n fill=_lightgray,\n rounded corners=1pt,\n minimum width=0.35cm,\n minimum height=0.28cm,\n inner sep=0pt,\n font=\\fontsize{4}{5}\\selectfont,\n text=black,\n align=center\n }\n]\n\\node[smallbox] (s1) at (0.4,0.99) {$\\mathcal{T}_a$};\n\\node[smallbox] (s2) at (0.55,0.66) {$\\mathcal{T}_a$};\n\\node[smallbox] (s3) at (0.55,0.33)

<!-- chunk {"id": "body-0037", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

{$\\mathcal{T}_a$};\n\\node[smallbox] (s4) at (0.55,0.00) {$\\mathcal{T}_a$};\n\n\\node[smallbox, fill=none] (spanbox) at (-0.2,0.00) {};\n\n\\draw[-, thin, draw=_gray] (spanbox.east) |- (s2.west);\n\\draw[-, thin, draw=_gray] (spanbox.east) |- (s3.west);\n\\draw[-, thin, draw=_gray] (spanbox.east) |- (s4.west);\n\n% ANSWERS NEXT TO b1--b4\n\\tikzset{\n answerpill/.style={\n draw=#1!60,\n fill=#1!30,\n rounded corners=1.2mm,\n line width=0.25pt,\n inner

<!-- chunk {"id": "body-0038", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

xsep=1mm,\n inner ysep=0.1mm,\n minimum width=1.7cm,\n text width=1.7cm, \n minimum height=0.28cm,\n font=\\tiny,\n align=left,\n anchor=west\n }\n}\n\n\\node[answerpill=_lightgray] (AnsA) at ([xshift=1.5mm]s2.east)\n {\\textbf{B}\\quad parking lane.};\n\n\\node[answerpill=_green] (AnsB) at ([xshift=3mm]s1.east)\n {{\\color{green!50!black}\\checkmark}\\quad bike lane.};\n\n\\node[answerpill=_lightgray] (AnsC) at ([xshift=1.5mm]s3.east)\n {\\textbf{C}\\quad bus

<!-- chunk {"id": "body-0039", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

lane.};\n\n\\node[answerpill=_lightgray] (AnsD) at ([xshift=1.5mm]s4.east)\n {\\textbf{D}\\quad vehicle lane.};\n\n\\draw[-, thin, draw=_gray] (s1.east) -- (AnsB.west);\n\\draw[-, thin, draw=_gray] (s2.east) -- (AnsA.west);\n\\draw[-, thin, draw=_gray] (s3.east) -- (AnsC.west);\n\\draw[-, thin, draw=_gray] (s4.east) -- (AnsD.west);\n\\end{tikzpicture}\n};\n\n% Box spanning b2--b4, placed between Selector and b2--b4\n\\node[\n draw=none,\n fill=_lightgray!60,\n rounded

<!-- chunk {"id": "body-0040", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

corners=1pt,\n minimum width=0.35cm,\n minimum height=0.94cm,\n inner sep=0pt,\n anchor=south west\n] (spanbox) at ([xshift=1.5mm,yshift=0mm]SelectedNodes.south east){%\n \\rotatebox{90}{\\scalebox{0.5}{$\\mathcal{O}(G_t)$}}%\n};\n\n\n\\node[\n draw=none,\n inner sep=0pt,\n anchor=south west\n] (SelectorTrap) at ([xshift=1.5mm,yshift=-0.5mm]SelectorBoxes.north west) {%\n\\begin{tikzpicture}\n\\def\\W{0.5}\n\\def\\H{0.35}\n\\def\\dx{0.12}\n\n\\fill[_red!20, rounded

<!-- chunk {"id": "body-0041", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

xsep=2pt,\n inner ysep=2pt,\n text width=2.3cm,\n anchor=west\n] (QuestionBox) at ([xshift=1mm,yshift=0mm]SelectorTrap.east) {"What is the \\textcolor{_darkyellow}{\\textbf{type}} of \\InlineEntity{Lane-1}{_darkyellow}{P1}?%\n};\n\n% UNIQUENESS\n\\node[\n draw=_purple,\n solid,\n line width=0.1pt,\n fill=_purple!10,\n align=center,\n inner sep=2pt,\n rounded corners=2pt,\n anchor=south west\n] (F) at ([yshift=5.5mm, xshift=-0.5mm]Selector.north east) {%\n\\begin{tikzpicture}[\n >=Latex,\n entity/.style={\n rounded

<!-- chunk {"id": "body-0042", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

corners=2pt,\n text=black,\n font=\\fontsize{5}{7}\\selectfont,\n inner xsep=2pt,\n inner ysep=2pt\n },\n spine/.style={_gray, line width=0.8pt},\n arrow/.style={-{Latex[length=2mm]}, _gray, line width=0.6pt},\n key/.style={text=gray!60, font=\\bfseries\\scriptsize},\n val/.style={text=black, font=\\scriptsize, align=left}\n]\n\n% Question\n\\node[entity, fill=_darkyellow] (v1) at (-0,0.1) {\\fontsize{5}{7}\\selectfont{\\textbf{Lane-1}}};\n\n\\node[entity, fill=_red] (BusFree) at (0,-0.6)

<!-- chunk {"id": "body-0043", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

{\\fontsize{5}{7}\\selectfont{\\textbf{Bus-1}}};\n\n\\node[entity, fill=_purple] (IntersectionFree) at (0,-1.3)\n {\\fontsize{5}{7}\\selectfont{\\textbf{Sign-1}}};\n\n% Columns\n\\def\\xA{0.8}\n\\def\\xB{0.8}\n\\draw[spine, thin, draw=_darkyellow, solid] (\\xA,0.3) -- (\\xA,-0.1);\n\\draw[spine, thin, draw=_darkyellow, solid] (\\xA,0.3) -- (\\xA-0.1,0.3);\n\\draw[spine, thin, draw=_purple, solid]

<!-- chunk {"id": "body-0044", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

{\\yOne,\\yTwo,\\yThree} {\n \\draw[thin, draw=_darkyellow, solid] (\\xA,\\y) -- ++(0.1,0);\n}\n\\foreach \\y in {\\yOne,\\yTwo,\\yThree} {\n \\draw[thin, draw=_red, solid] (\\xB,\\y+\\yFour-0.1) -- ++(0.1,0);\n}\n\n\n \\node[\n draw=_gray,\n fill=_lightgray!0,\n rounded corners=1pt,\n inner xsep=4pt,\n inner ysep=2pt,\n font=\\fontsize{4.5}{7}\\selectfont,\n anchor=west\n] (IntersectionDots) at (\\xB+0.05,-1.2)

<!-- chunk {"id": "body-0045", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

{$\\cdots$};\n\n% Grey grouping box around Lane uniqueness options\n\\node[\n draw=_gray,\n fill=_lightgray!0,\n rounded corners=1pt,\n inner xsep=1pt,\n inner ysep=1pt,\n fit={(\\xA+0.1,\\yOne+0.1) (\\xA+3.3,\\yThree-0.05)}\n] {};\n\n% Grey grouping box around Bus uniqueness options\n\\node[\n draw=_gray,\n fill=_lightgray!0,\n rounded corners=1pt,\n inner xsep=1pt,\n inner ysep=1pt,\n fit={(\\xB+0.1,\\yOne+\\yFour+0) (\\xB+3.3,\\yThree+\\yFour-0.1-0.05)}\n]

<!-- chunk {"id": "body-0046", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

draw=_red]\n(mid)\n -- node[\n pos=0.5,\n right,\n font=\\fontsize{3}{4}\\selectfont,\n text=_red\n] {(1 hop)}\n(BusFree.north);\n\\draw[line width=0.4pt, _darkyellow] (mid) -- ($(mid)!0.5!(BusFree.north)$);\n\n\n\\draw[->, thin, draw=_purple] (BusFree.south) -- node[\n pos=0.5,\n right,\n font=\\fontsize{3}{4}\\selectfont,\n text=_purple\n] {(2 hops)} (mid2);\n\\draw[line width=0.4pt, _red] (BusFree.south) --

<!-- chunk {"id": "body-0047", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

($(BusFree.south)!0.4!(mid2)$);\n\n\\end{tikzpicture}\n};\n\n\\node[\n fill=none,\n draw=none,\n font=\\bfseries\\tiny,\n text=_purple,\n inner xsep=2pt,\n inner ysep=0.5pt,\n anchor=north east\n] at ([xshift=-3pt,yshift=8pt]F.south east) {(3.3) recursive uniqueness};\n\n% REASONING\n\\node[\n draw=none,\n dashed,\n line width=0.25pt,\n fill=none,\n rounded corners=2pt,\n anchor=north west,\n at=(D.south west),\n inner sep=3pt,\n yshift=-0mm\n] (G)

<!-- chunk {"id": "body-0048", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

\\textcolor{_gray}}\n \\end{tcolorbox}\n}\n\n\\tikzset{\n answerpill/.style={\n draw=#1!60,\n fill=#1!30,\n solid,\n rounded corners=1.2mm,\n line width=0.25pt,\n inner xsep=1mm,\n inner ysep=0.1mm,\n minimum height=0.28cm,\n font=\\tiny,\n align=left\n }\n}\n\n\\newcommand{\\InlineAnswerPill}{%\n\\tikz[baseline=(a.base)]{\n\\node[\n answerpill=#2,\n anchor=base,\n inner xsep=1mm,\n inner ysep=0.1mm,\n minimum height=0.28cm,\n font=\\tiny,\n align=left\n]

<!-- chunk {"id": "body-0049", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

(a);\n}\n}\n\n\n\\PlainStepBox{%\n\\textbf{CoT extraction:} What is the \\textcolor{_darkyellow}{type} of \\InlineEntity{the lane that is right of\n\\InlineEntity{the bus with number 54D}{_red}{P4}}{_darkyellow}{P1}?\n}\n \n\\StepBox{\\textbf{\\quad Link 1: Anchor identification} Identify \\textcolor{_red}{the bus with number$^*$ 54D}, which is visible at \\TextPin{P4}{_red}, CENTER view.}\n\n\\StepBox{\\textbf{\\quad Link 2: Graph Traversal} The lane in question is \\textcolor{_darkyellow}{the lane that} \\textcolor{_gray}{$\\rightarrow$ is right of$^*$} \\textcolor{_red}{that bus}, and visible

<!-- chunk {"id": "body-0050", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

at \\TextPin{P3}{_darkyellow}.}\n\n\\StepBox{\\textbf{\\quad Link 3: Target} The lane\'s \\textcolor{_darkyellow}{description$^*$ is rightmost lane} and it \\textcolor{_gray}{$\\rightarrow$ is controlled by} \\textcolor{_orange}{a traffic light with status green} at \\TextPin{P1}{_orange}.

<!-- chunk {"id": "body-0051", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

}\n\n\\PlainStepBox{\\textbf{Conclusion:} The lane is a \n\\InlineAnswerPill{{\\color{green!50!black}\\checkmark}\\quad bike lane.}{_green}}\n\n\\vspace{-1mm}\n\n\\end{minipage}\n};\n\\node[\n fill=white,\n draw=none,\n font=\\bfseries\\tiny,\n text=_gray,\n inner xsep=2pt,\n inner ysep=0.5pt,\n anchor=south west\n] at ([xshift=2pt,yshift=0pt]G.north west) {};\n\n\\coordinate (p) at (4.2,-3.5);\n\\coordinate (q) at (3.1,-3.5);\n\\coordinate (a) at (2.8,-3.1);\n\n\n

<!-- chunk {"id": "body-0052", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

\\draw[-,thin,draw=_gray, rounded corners=0pt] (SelectorTrap.east) -- (QuestionBox.west);\n% Selector -> T_q\n\\begin{scope}[on background layer]\n\\draw[-, thin, draw=_gray]\n (SelectedNodes.north) |- (SelectorTrap.west);\n\n\\draw[-, thin, draw=_gray]\n (SelectedNodes.south) |- (spanbox.west);\n\\end{scope}\n\n\n% OUTER EXECUTION FORM\n\n\\coordinate (LtopLeft) at ([xshift=-2pt,yshift=8pt]SelectedNodes.north west);\n\\coordinate (LtopRight) at ([xshift=2pt,yshift=8pt]QuestionBox.north east);\n\\coordinate (LbotLeft) at ([xshift=-0pt,yshift=-0pt]G.south

<!-- chunk {"id": "body-0053", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

west);\n\\coordinate (LbotRight) at ([xshift=0pt,yshift=-0pt]G.south east);\n\\coordinate (LbotRight2) at ([xshift=0pt,yshift=-0pt]G.north west);\n\\coordinate (LtopLeft2) at ([xshift=-2pt,yshift=-3pt]SelectedNodes.south west);\n\n\\begin{scope}[on background layer]\n\\draw[\n _gray,\n fill=none,\n dashed,\n line width=0.25pt,\n rounded corners=4pt\n]\n (LtopLeft)\n -- (LtopRight)\n -- (LbotRight)\n -- (LbotLeft)\n -- (LbotRight2)\n -- (LtopLeft2)\n -- cycle;\n\\end{scope}\n\n\\node[\n fill=white,\n

<!-- chunk {"id": "body-0054", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

draw=none,\n font=\\bfseries\\tiny,\n text=_gray,\n inner xsep=2pt,\n inner ysep=0.5pt,\n anchor=north east\n] at ([xshift=-2pt,yshift=4pt]LtopRight) {(3.4) query instantiation mechanism};\n\n\\pgfdeclarelayer{foreground}\n\\pgfsetlayers{background,main,foreground}\n\n\\node[\n draw=_gray,\n fill=white,\n rounded corners=2pt,\n line width=0.25pt,\n font=\\tiny,\n text=_gray,\n inner xsep=4pt,\n inner ysep=5pt,\n anchor=north\n] (RoadSubstrate) at ([xshift=-2mm,yshift=7mm]D.south) {Combined Road Substrate};\n\n\\draw[->, thin,

<!-- chunk {"id": "body-0055", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

draw=_gray]\n (RoadSubstrate.east) -- ++(1.95cm,0)\n node[midway, below,_gray, yshift=0.7mm] {\\fontsize{5}{7}\\selectfont joint execution};\n\\draw[\n ->,\n thin,\n draw=_gray\n] ([yshift=-3mm]C.east)\n -- ([yshift=-3mm,xshift=1.5mm]C.east)\n |- node[pos=0.75, below, _gray, font=\\fontsize{5}{7}\\selectfont, yshift=0.5mm] {formal structure}\n ([yshift=-0.1cm] RoadSubstrate.west);\n\\draw[\n ->,\n thin,\n draw=_gray,\n rounded corners=0pt\n] (a) |- node[pos=0.75, above,

<!-- chunk {"id": "body-0056", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

_gray, font=\\fontsize{5}{7}\\selectfont, yshift=-0.5mm] {rich semantics} ([yshift=0.1cm] RoadSubstrate.west);\n\n \n\\coordinate (qtof) at ([xshift=3mm]QuestionBox.east);\n\\coordinate (ptof) at ([yshift=0mm, xshift=0.1mm]F.south east);\n\\coordinate (rtof) at (10.5,-4.6);\n\n\\draw[->, thin, draw=_gray, rounded corners=0pt]\n (QuestionBox.east)\n -- (qtof)\n |- node[\n pos=0.25,\n rotate=90,\n _gray,\n font=\\fontsize{5}{7}\\selectfont,\n yshift=-1mm\n] {Step 1: recursive construction}\n

<!-- chunk {"id": "body-0057", "role": "body", "section": "The Combined Road Substrate", "weight": 1.0} -->

([yshift=-4mm, xshift=0mm]F.north east);\n \n\\draw[->, thin, draw=_gray, rounded corners=0pt]\n ([yshift=0.75mm, xshift=0mm]F.south east)\n -- (ptof)\n |- node[pos=0.75, above, _gray, font=\\fontsize{5}{7}\\selectfont, yshift=-0.7mm]\n {Step 2: recursive deconstruction}(rtof);\n\n \\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Language descriptions of road scenes are matched to graph primitives through canonical operators to build a semantically rich graph. This Combined Road Substrate is executable and produces questions, answers, decoys and CoT from the same underlying scheme.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Graph Primitives", "weight": 1.0} -->

We represent each scene as a directed graph over time steps $t \in [0,..., T]$, G = \{G\_0, \dots, G\_T\} \quad \text{with} \quad G\_t = (N\_t, E\_t), where \(N\_t\) is the set of nodes and \(E\_t\) the set of directed edges at time $t$. Each node \(n \in N\_t\) has a type $\tau(n)$ and a set of properties where a property is a tuple \(with \(k^i \in \mathcal{K}\) its property key and \(y^i(t) \in \mathcal{Y}\) its corresponding value, which may be static for invariant properties (\(y^i(t) = y\_0\)).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Graph Primitives", "weight": 1.0} -->

Geometric grounding is represented as a special property \(p\_t^{\text{geo}} \in P\_t(n)\) with values in the image-space \(\mathbb{R}^2 \) or real world coordinates \(\mathbb{R}^3 \). Finally, each edge \(e\_t \in E\_t\) is defined as where \(n\_t, n'\_t \in N\_t\) are the source and target nodes, and \(\ell\_{n,n'}(t)\) is a (possibly time-dependent) edge label. This formulation provides a minimal structural backbone upon which language-grounded semantics are later imposed.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Canonical operators", "weight": 1.0} -->

A central design goal of CRS is to avoid defining a priori what real-world objects (lanes, vehicles, crossings, etc.) are mapped to the graph. Instead, types, property keys and values, and edge labels should be freely expressible within the open-language space. However, without a well-specified language-structure interface that defines how open-vocabulary statements translate into their graph counterparts, the representation risks becoming inconsistent, ambiguous, and ultimately non-executable. To resolve this, we impose structure not on what can be expressed, but on how it must be expressed through three canonical operators \(\Phi\_{n}, \Phi\_{p}, \Phi\_{e}\): An open language graph element is valid only if it produces a grammatical and semantically well-typed English sentence under one of the three canonical operators.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Canonical operators", "weight": 1.0} -->

For node types $\tau(n)$, we define $$\Phi_{\text{n}}(\tau(n)) = \texttt{``There exists a <}\tau(n)\texttt{>''}.$$ Thus, a node type is valid if it completes an existential statement denoting an identifiable entity or group of objects, \textit{e.g.}\@, There exists a traffic jam. For properties, each \(p\_t^i=(k^i,y^i(t)) \in P\_t(n)\) must satisfy \texttt{``The <}k^i\texttt{> of <}\tau(n)\texttt{> is `<}y^i(t)\texttt{>' ''}.$$ This rules out ill-typed encodings such as is\_closed\_for\_construction = true, since The is\_closed\_for\_construction of the lane is `true' is not a well-formed attribute statement.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Canonical operators", "weight": 1.0} -->

Instead, the same information should be represented as, for example, status = closed\_for\_construction. For relations, each edge \(e=(n,n',\ell\_{n,n'}(t))\) must satisfy $$\Phi_{\text{e}}(n,n',\ell_{n,n'}(t)) = \texttt{``The <}\tau(n)\texttt{> <}\ell_{n,n'}(t)\texttt{> the <}\tau(n')\texttt{>''}.$$ Thus, relation labels must form meaningful directed relational statements, which excludes forms such as `left of' or `controlling', but allows `is left of' or `controls'. By enforcing a fixed structural form while leaving the semantic space unconstrained, the canonical schema decouples compositional structure from linguistic expressivity. As a result, the graph remains consistent and queryable without restricting the richness or extensibility of its semantic content.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Well-definedness constraints", "weight": 1.0} -->

To make reasoning over \(G\_t\) executable, linguistic references to nodes must be unambiguous and the relevant parts of the graph sufficiently specified. This is non-trivial under our open-vocabulary design: multiple nodes may share the same type or properties (e.g., the traffic light with status `red' may refer to multiple nodes), making language-based references ambiguous. Furthermore, since we do not constrain the space of potential node types, the graph operates under an open-world assumption, where absence does not imply non-existence but rather unknown state, and queries requiring exhaustive knowledge (\textit{e.g.}\@, How many traffic lights are there?) could potentially be ill-posed. We address this through two conditions: uniqueness and completeness.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Well-definedness constraints", "weight": 1.0} -->

A node in the graph is well-defined only if it admits a unique descriptor for the corresponding object in the scene. A descriptor \(d\) is a language expression derived from \(G\_t\) that refers to the real-world object $n$ represented via node type-, property-, or edge-based descriptions (\textit{e.g.}\@, the traffic light, the traffic light with status `red', the traffic light that controls the ego lane). To ensure identifiability, we introduce uniqueness anchors (denoted by \(^\star\)), which signal that the marked node, property or edge can be used to produce a descriptor that refers to exactly one object in the image. We define uniqueness at

<!-- chunk {"id": "body-0065", "role": "body", "section": "Well-definedness constraints", "weight": 1.0} -->

- node-level, where the node's type \(\tau(n^\star)\) alone is sufficient to identify the object in the scene (\textit{e.g.}\@, the `only' sign), - property-level, where one of its properties \(p^\star\) uniquely identifies the node (\textit{e.g.}\@, the `only' sign with meaning no left turn), and - edge-level, \(e^\star\), where a node is uniquely identified through its relation to another node (\textit{e.g.}\@, the `only' sign that controls the lane.)

<!-- chunk {"id": "body-0066", "role": "body", "section": "Well-definedness constraints", "weight": 1.0} -->

Descriptors are constructed recursively by iterating over unique anchors, until uniqueness is achieved; if necessary, geometric grounding \(p\_t^{\text{geo}}\) is used for disambiguation. Objects that cannot be uniquely identified are excluded from well-defined queries. Further details are provided in app:recursive-unique-descriptors.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Well-definedness constraints", "weight": 1.0} -->

To assure that queries about completeness or cardinality of nodes remain compatible with our open-world assumption, we define a completeness indicator at node-type level. For a type \(\tau(n)\), let \(c\_t(\tau) \in \{0,1\} \) denote whether all instances of type \(\tau\) that are visible in the input image at time \(t\) are also present in \(N\_t\). A query \(q\) that requires exhaustive enumeration over nodes of type \(\tau\) is then considered valid only if \(c\_t(\tau) = 1\). Taken together, the first three components of the CRS framework yield a representation that is structurally well-defined yet remains semantically expressive, while ensuring that objects in the scene can be uniquely and unambiguously associated with individual nodes in the graph.

<!-- chunk {"id": "body-0068", "role": "body", "section": "The query instantiation mechanism", "weight": 1.0} -->

At the core of CRS is the query instantiation mechanism, which turns the graph representation into an executable framework, hence formulates reasoning tasks as structured computations over the graph. Each query extracts a question, its correct answer, and a set of plausible decoys, all expressed in natural language. Additionally, CoT traces are automatically derived in the same framework, while reasoning depth is controlled as a hyperparameter of the method.

<!-- chunk {"id": "body-0069", "role": "body", "section": "The query instantiation mechanism", "weight": 1.0} -->

Each query is defined by four components: (i) a selection operator $\mathcal{S}$ that retrieves a set of target nodes and associated attributes or relations from $G_t$, (ii) a question template $\mathcal{T}_q$ that maps the selected elements to a natural language question, (iii) an answer template $\mathcal{T}_a$ that renders the correct answer, and (iv) a perturbation operator $\mathcal{O}(G)$ that produces controlled variations of the graph or its attributes. To generate hard negatives, applying $\mathcal{T}_a$ to $\mathcal{O}(G)$yields semantically plausible but incorrect answer candidates.

<!-- chunk {"id": "body-0070", "role": "body", "section": "The query instantiation mechanism", "weight": 1.0} -->

While a virtually infinite set of queries can be defined to inquire different aspects of the graph, we identify five fundamental categories: queries targeting node properties, inter-node relations, counting and comparison, of nodes, and existence/positional queries. For our study, we instantiate 19 different queries targeting a broad range of graph properties (lane type, line color, counting of lanes and crossings, relationships between lanes, etc.). While all query types used in this study are detailed in sec:qa-types\_supplementary of the supplementary material, we discuss an example of property-related queries below together with edge-related queries the most fundamental operation on the graph. Furthermore, they are relatively simple and hence an important means for model analysis (see sec:experiments). arrows.meta, positioning, shapes.multipart Let us assume we have a road scene as illustrated in fig:method\_figure with the CRS.

<!-- chunk {"id": "body-0071", "role": "body", "section": "The query instantiation mechanism", "weight": 1.0} -->

Since property-related queries inquire the value of node properties for nodes of a certain type, our selector can be written as $$\mathcal{S}(N_t, \hat{\tau}, \hat{k})=\{n\in N_t, (k^i,y^i(t)) \in P_t(n) \ | \ \tau(n)=\hat{\tau} \ \cap \ k^i =\hat{k}\},$$ while the question template is $\mathcal{T}_q=$What is the <$\hat{k}$> of the $d^*(n)$? The answer template simply becomes the property value, $\mathcal{T}\_a=$$y(t)$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "The query instantiation mechanism", "weight": 1.0} -->

If we select $\tau(n)=\texttt{lane}$ and $\hat{k}=\texttt{type}$, $\mathcal{S}$ will extract exactly two matching nodes from the graph (Lane-1, Lane-4), while $\mathcal{T}\_a$ yields bike lane for both. For decoys, $\mathcal{O}$ perturbs the graph by substituting other potential types (bus lane, etc.). The semantic diversity (and variation) of our framework is then activated through the uniqueness mechanism inside $\mathcal{T}_q$. When resolving for $d^*(n)$ (Lane-1 in fig:method\_figure), we get a variety of unique options, ranging from What is the type of the lane that contains the bus with number 54D? to What is the type of the right curb lane?, for the same query and node.

<!-- chunk {"id": "body-0073", "role": "body", "section": "The query instantiation mechanism", "weight": 1.0} -->

Because queries refer to objects in the scene through the unique descriptor present in $\mathcal{T}_q$, $\mathcal{T}_a$, or both, the compositional complexity of a query is directly controlled by the maximum descriptor depth, \textit{i.e.}\@, a hyperparameter that defines how many neighboring nodes can be traversed to derive unique descriptors. Concretely, zero reasoning hops are necessary to resolve the right curb lane, while the lane that contains the bus with number 54D requires one. The consequences of this explicit dependency are threefold: Not only are semantically diverse multi-hop questions created automatically and with controlled reasoning depth, but a chain-of-thought reasoning trace can also be generated directly from the graph by traversing the descriptor in reverse order and grounding the nodes present in the descriptor chain.

<!-- chunk {"id": "body-0074", "role": "body", "section": "The query instantiation mechanism", "weight": 1.0} -->

- Anchor identification: We resolve the outermost element of $d^*(n)$ to a unique node $n_a \in N_t$, guaranteed by the uniqueness constraint. This provides an initial grounding in image space via $p_t^{\text{geo}}(n_a)$. For the example in fig:method\_figure, this would consist of identifying and grounding the bus with number 54D. - Graph traversal: We iteratively resolve the nested structure of $d^*(n)$ by traversing edges in $G_t$, producing a sequence of nodes $(n_a, \dots, n)$ that terminates at the target node (\textit{i.e.}\@, the lane that contains the bus with number 54D). - Target extraction: To help ground the target node, we first extract a brief description by combining - unique and non-unique - properties and edges of $n$ to also visually ground the target. Finally, we retrieve the attribute or relation from $n$ needed for the answer.

<!-- chunk {"id": "body-0075", "role": "body", "section": "The query instantiation mechanism", "weight": 1.0} -->

Each intermediate node in the traversal is grounded via its geometric property, ensuring that the entire reasoning trace is spatially anchored. This formulation yields three key properties. First, the CoT trace is deterministic, as it is uniquely defined by the query and the graph. Second, it is fully grounded, since each step corresponds to explicit nodes and relations in $G_t$. Third, it is compositional and can be potentially repeated multiple times for queries such as counting or comparison, where the procedure is applied once per enumerated element. Importantly, this CoT arises for free alongside question and answer generation, requiring no additional annotation effort. Implementation details about the three links and the specific CoT instantiations per query are provided in app:cot-construction.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Data sources and graph construction", "weight": 1.0} -->

To test the effectiveness of our framework, we instantiate CRS by integrating standard geometric and semantic representations from modular driving stacks, including HD maps (lane geometry and layout), topological annotations (lane connectivity and control relations), and object annotations (dynamic agents and scene elements), and subsequently enrich them with natural language. Concretely, we use the front-facing camera views from Argoverse2 [Argoverse2] as visual input, and combine the provided HD maps with the topological structure from OpenLane-V2 [wang2023openlane] to populate our graph. These sources are mapped into CRS using the canonical operators: map elements become nodes ($\Phi_n$), attributes are encoded as properties ($\Phi_p$), and relationships (\textit{e.g.}\@, adjacency, control) constitute edges ($\Phi_{e}$).

<!-- chunk {"id": "body-0077", "role": "body", "section": "Data sources and graph construction", "weight": 1.0} -->

Although these representations are available and compatible with the CRS, naive aggregation of all information would result in a graph that is overly dense with respect to number of nodes, poorly aligned with the selectiveness of human visual reasoning, and lacking in semantic richness. Rather than directly aggregating all data, we construct graphs through a selective enrichment process with human oversight. Starting from the initial graph, expert human annotators (i) filter for salience by removing irrelevant or non-visible elements, (ii) add entities that are important for scene understanding, including objects beyond existing annotations, (iii) enrich nodes with additional properties in natural language, and (iv) introducenew relations that capture context-specific interactions. This process also establishes uniqueness and completeness required for executable reasoning.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Data sources and graph construction", "weight": 1.0} -->

Using this pipeline, we construct 80 CRS graphs, from which we generate 22k training samples via 19 queries on a temporal window of 4 frames at 2 Hz. We also create a held-out validation set of 1000 expert-verified samples from 120 distinct scenes following [lilja2024localization], subsampling at most one sample per query and scene. Further details on graph construction and annotation are provided in sec:graph\_construction\_supplementary and sec:stats. The graph creation tool will be released together with the code and data.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Experiments", "weight": 1.0} -->

[col sep=comma]performance\_results.csv scale only axis, axis line style=-, axis x line*=bottom, symbolic x coords=qwen\_4b\_sft-80graphs, qwen\_4b\_sft\_cot, qwen-2b-sft-80graphs, openai\_gpt-5.4\_corrected, gemini-3.1-pro\_corrected, google\_gemma-4-31b-it\_corrected, google\_gemini-3.1-flash-lite-preview\_corrected, qwen\_qwen3-vl-235b-a22b-instruct\_corrected, openai\_gpt-4o-mini\_corrected, moonshotai\_kimi-k2.6\_corrected, tick style=draw=none, title style=anchor=north, tick label style=font=, label style=font=, unbounded coords=discard, x

<!-- chunk {"id": "body-0080", "role": "body", "section": "Experiments", "weight": 1.0} -->

filter/.code=bucketcountingmodelclaude-sonnet-4.5\_correctednannan unbounded coords=discard, x filter/.code=bucketcountingmodelgemini-3.1-pro\_correctednannan unbounded coords=discard, x filter/.code=bucketcountingmodelgoogle\_gemini-3.1-flash-lite-preview\_correctednannan unbounded coords=discard, x filter/.code=bucketcountingmodelgoogle\_gemma-4-31b-it\_correctednannan unbounded coords=discard, x filter/.code=bucketcountingmodelmoonshotai\_kimi-k2.6\_correctednannan unbounded coords=discard, x filter/.code=bucketcountingmodelopenai\_gpt-4o-mini\_correctednannan unbounded coords=discard, x

<!-- chunk {"id": "body-0081", "role": "body", "section": "Experiments", "weight": 1.0} -->

filter/.code=bucketcountingmodelopenai\_gpt-5.4\_correctednannan unbounded coords=discard, x filter/.code=bucketcountingmodelqwen-2b-sft-80graphsnannan unbounded coords=discard, x filter/.code=bucketcountingmodelqwen-2b-sft-rcotnannan unbounded coords=discard, x filter/.code=bucketcountingmodelqwen2bnannan unbounded coords=discard, x filter/.code=bucketcountingmodelqwen4bnannan unbounded coords=discard, x filter/.code=bucketcountingmodelqwen\_4b\_sft-80graphsnannan unbounded coords=discard, x filter/.code=bucketcountingmodelqwen\_4b\_sft\_cotnannan unbounded coords=discard, x

<!-- chunk {"id": "body-0082", "role": "body", "section": "Experiments", "weight": 1.0} -->

filter/.code=bucketcountingmodelqwen\_qwen3-vl-235b-a22b-instruct\_correctednannan How many lanes are there?

<!-- chunk {"id": "body-0083", "role": "body", "section": "Experiments", "weight": 1.0} -->

A. Just one lane in ego direction. B. One lane in ego and one in opposite direction. C. 2 lanes in ego direction.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Experiments", "weight": 1.0} -->

D. None of the above.[t]0.2 scale only axis, axis line style=-, axis x line*=bottom, symbolic x coords=qwen\_4b\_sft-80graphs, qwen\_4b\_sft\_cot, qwen-2b-sft-80graphs, openai\_gpt-5.4\_corrected, gemini-3.1-pro\_corrected, google\_gemma-4-31b-it\_corrected, google\_gemini-3.1-flash-lite-preview\_corrected, qwen\_qwen3-vl-235b-a22b-instruct\_corrected, openai\_gpt-4o-mini\_corrected, moonshotai\_kimi-k2.6\_corrected, tick style=draw=none, title style=anchor=north, tick label style=font=, label style=font=, unbounded coords=discard, x filter/.code=bucketpropertiesmodelclaude-sonnet-4.5\_correctednannan

<!-- chunk {"id": "body-0085", "role": "body", "section": "Experiments", "weight": 1.0} -->

unbounded coords=discard, x filter/.code=bucketpropertiesmodelgemini-3.1-pro\_correctednannan unbounded coords=discard, x filter/.code=bucketpropertiesmodelgoogle\_gemini-3.1-flash-lite-preview\_correctednannan unbounded coords=discard, x filter/.code=bucketpropertiesmodelgoogle\_gemma-4-31b-it\_correctednannan unbounded coords=discard, x filter/.code=bucketpropertiesmodelmoonshotai\_kimi-k2.6\_correctednannan unbounded coords=discard, x filter/.code=bucketpropertiesmodelopenai\_gpt-4o-mini\_correctednannan unbounded coords=discard, x filter/.code=bucketpropertiesmodelopenai\_gpt-5.4\_correctednannan unbounded coords=discard, x

<!-- chunk {"id": "body-0086", "role": "body", "section": "Experiments", "weight": 1.0} -->

filter/.code=bucketpropertiesmodelqwen-2b-sft-80graphsnannan unbounded coords=discard, x filter/.code=bucketpropertiesmodelqwen-2b-sft-rcotnannan unbounded coords=discard, x filter/.code=bucketpropertiesmodelqwen2bnannan unbounded coords=discard, x filter/.code=bucketpropertiesmodelqwen4bnannan unbounded coords=discard, x filter/.code=bucketpropertiesmodelqwen\_4b\_sft-80graphsnannan unbounded coords=discard, x filter/.code=bucketpropertiesmodelqwen\_4b\_sft\_cotnannan unbounded coords=discard, x filter/.code=bucketpropertiesmodelqwen\_qwen3-vl-235b-a22b-instruct\_correctednannan What lane is the right curb lane?

<!-- chunk {"id": "body-0087", "role": "body", "section": "Experiments", "weight": 1.0} -->

A. standard travel lane with street parking. B. bike lane. C. standard travel lane.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Experiments", "weight": 1.0} -->

D. lane reserved for bus.[t]0.2 scale only axis, axis line style=-, axis x line*=bottom, symbolic x coords=qwen\_4b\_sft-80graphs, qwen\_4b\_sft\_cot, qwen-2b-sft-80graphs, openai\_gpt-5.4\_corrected, gemini-3.1-pro\_corrected, google\_gemma-4-31b-it\_corrected, google\_gemini-3.1-flash-lite-preview\_corrected, qwen\_qwen3-vl-235b-a22b-instruct\_corrected, openai\_gpt-4o-mini\_corrected, moonshotai\_kimi-k2.6\_corrected, tick style=draw=none, title style=anchor=north, tick label style=font=, label style=font=, unbounded coords=discard, x filter/.code=bucketcomparisonmodelclaude-sonnet-4.5\_correctednannan

<!-- chunk {"id": "body-0089", "role": "body", "section": "Experiments", "weight": 1.0} -->

unbounded coords=discard, x filter/.code=bucketcomparisonmodelgemini-3.1-pro\_correctednannan unbounded coords=discard, x filter/.code=bucketcomparisonmodelgoogle\_gemini-3.1-flash-lite-preview\_correctednannan unbounded coords=discard, x filter/.code=bucketcomparisonmodelgoogle\_gemma-4-31b-it\_correctednannan unbounded coords=discard, x filter/.code=bucketcomparisonmodelmoonshotai\_kimi-k2.6\_correctednannan unbounded coords=discard, x filter/.code=bucketcomparisonmodelopenai\_gpt-4o-mini\_correctednannan unbounded coords=discard, x filter/.code=bucketcomparisonmodelopenai\_gpt-5.4\_correctednannan unbounded coords=discard, x

<!-- chunk {"id": "body-0090", "role": "body", "section": "Experiments", "weight": 1.0} -->

filter/.code=bucketcomparisonmodelqwen-2b-sft-80graphsnannan unbounded coords=discard, x filter/.code=bucketcomparisonmodelqwen-2b-sft-rcotnannan unbounded coords=discard, x filter/.code=bucketcomparisonmodelqwen2bnannan unbounded coords=discard, x filter/.code=bucketcomparisonmodelqwen4bnannan unbounded coords=discard, x filter/.code=bucketcomparisonmodelqwen\_4b\_sft-80graphsnannan unbounded coords=discard, x filter/.code=bucketcomparisonmodelqwen\_4b\_sft\_cotnannan unbounded coords=discard, x filter/.code=bucketcomparisonmodelqwen\_qwen3-vl-235b-a22b-instruct\_correctednannan Are the ego and the black sedan in the same lane?

<!-- chunk {"id": "body-0091", "role": "body", "section": "Experiments", "weight": 1.0} -->

A. No, the ego is right of the black sedan. B. No, the ego is left of the black sedan. C. Yes, the left-turn lane.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Experiments", "weight": 1.0} -->

D. None of the above.[t]0.2 scale only axis, axis line style=-, axis x line*=bottom, symbolic x coords=qwen\_4b\_sft-80graphs, qwen\_4b\_sft\_cot, qwen-2b-sft-80graphs, openai\_gpt-5.4\_corrected, gemini-3.1-pro\_corrected, google\_gemma-4-31b-it\_corrected, google\_gemini-3.1-flash-lite-preview\_corrected, qwen\_qwen3-vl-235b-a22b-instruct\_corrected, openai\_gpt-4o-mini\_corrected, moonshotai\_kimi-k2.6\_corrected, tick style=draw=none, title style=anchor=north, tick label style=font=, label style=font=, unbounded coords=discard, x

<!-- chunk {"id": "body-0093", "role": "body", "section": "Experiments", "weight": 1.0} -->

filter/.code=bucketlocalization+existancemodelclaude-sonnet-4.5\_correctednannan unbounded coords=discard, x filter/.code=bucketlocalization+existancemodelgemini-3.1-pro\_correctednannan unbounded coords=discard, x filter/.code=bucketlocalization+existancemodelgoogle\_gemini-3.1-flash-lite-preview\_correctednannan unbounded coords=discard, x filter/.code=bucketlocalization+existancemodelgoogle\_gemma-4-31b-it\_correctednannan unbounded coords=discard, x filter/.code=bucketlocalization+existancemodelmoonshotai\_kimi-k2.6\_correctednannan unbounded coords=discard, x filter/.code=bucketlocalization+existancemodelopenai\_gpt-4o-mini\_correctednannan unbounded coords=discard, x

<!-- chunk {"id": "body-0094", "role": "body", "section": "Experiments", "weight": 1.0} -->

filter/.code=bucketlocalization+existancemodelopenai\_gpt-5.4\_correctednannan unbounded coords=discard, x filter/.code=bucketlocalization+existancemodelqwen-2b-sft-80graphsnannan unbounded coords=discard, x filter/.code=bucketlocalization+existancemodelqwen-2b-sft-rcotnannan unbounded coords=discard, x filter/.code=bucketlocalization+existancemodelqwen2bnannan unbounded coords=discard, x filter/.code=bucketlocalization+existancemodelqwen4bnannan unbounded coords=discard, x filter/.code=bucketlocalization+existancemodelqwen\_4b\_sft-80graphsnannan unbounded coords=discard, x filter/.code=bucketlocalization+existancemodelqwen\_4b\_sft\_cotnannan unbounded

<!-- chunk {"id": "body-0095", "role": "body", "section": "Experiments", "weight": 1.0} -->

coords=discard, x filter/.code=bucketlocalization+existancemodelqwen\_qwen3-vl-235b-a22b-instruct\_correctednannan Is there a crossing straight ahead?

<!-- chunk {"id": "body-0096", "role": "body", "section": "Experiments", "weight": 1.0} -->

A. No but there is one to the left. B. Yes marked as zebra crossing. C. No there is no crossing.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Experiments", "weight": 1.0} -->

D. Yes, marked as outlined white rectangle.[t]0.2 scale only axis, axis line style=-, axis x line*=bottom, symbolic x coords=qwen\_4b\_sft-80graphs, qwen\_4b\_sft\_cot, qwen-2b-sft-80graphs, openai\_gpt-5.4\_corrected, gemini-3.1-pro\_corrected, google\_gemma-4-31b-it\_corrected, google\_gemini-3.1-flash-lite-preview\_corrected, qwen\_qwen3-vl-235b-a22b-instruct\_corrected, openai\_gpt-4o-mini\_corrected, moonshotai\_kimi-k2.6\_corrected, tick style=draw=none, title style=anchor=north, tick label style=font=, label style=font=, unbounded coords=discard, x

<!-- chunk {"id": "body-0098", "role": "body", "section": "Experiments", "weight": 1.0} -->

filter/.code=bucketrelationalmodelclaude-sonnet-4.5\_correctednannan unbounded coords=discard, x filter/.code=bucketrelationalmodelgemini-3.1-pro\_correctednannan unbounded coords=discard, x filter/.code=bucketrelationalmodelgoogle\_gemini-3.1-flash-lite-preview\_correctednannan unbounded coords=discard, x filter/.code=bucketrelationalmodelgoogle\_gemma-4-31b-it\_correctednannan unbounded coords=discard, x filter/.code=bucketrelationalmodelmoonshotai\_kimi-k2.6\_correctednannan unbounded coords=discard, x filter/.code=bucketrelationalmodelopenai\_gpt-4o-mini\_correctednannan unbounded coords=discard, x

<!-- chunk {"id": "body-0099", "role": "body", "section": "Experiments", "weight": 1.0} -->

filter/.code=bucketrelationalmodelopenai\_gpt-5.4\_correctednannan unbounded coords=discard, x filter/.code=bucketrelationalmodelqwen-2b-sft-80graphsnannan unbounded coords=discard, x filter/.code=bucketrelationalmodelqwen-2b-sft-rcotnannan unbounded coords=discard, x filter/.code=bucketrelationalmodelqwen2bnannan unbounded coords=discard, x filter/.code=bucketrelationalmodelqwen4bnannan unbounded coords=discard, x filter/.code=bucketrelationalmodelqwen\_4b\_sft-80graphsnannan unbounded coords=discard, x filter/.code=bucketrelationalmodelqwen\_4b\_sft\_cotnannan unbounded coords=discard, x

<!-- chunk {"id": "body-0100", "role": "body", "section": "Experiments", "weight": 1.0} -->

filter/.code=bucketrelationalmodelqwen\_qwen3-vl-235b-a22b-instruct\_correctednannan Which lane does the no-left-turn sign control? A. The ego lane. B. The lane left of the ego lane. C. The lane that contains the bus. D. The lane that has the 'BUS' marking.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Experiments", "weight": 1.0} -->

| [baseline=-0.5ex][m1, fill=m1] circle (1.7pt);Qwen3-VL-4b-sft | Model performance by bucket with example questions.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Experiments", "weight": 1.0} -->

confidence=None created_by=None text="\\begin{tikzpicture}\n\n\\node[inner sep=0,scale=0.99, transform shape] (wholefig) {\n\n\\newcommand{\\AnswerPill}{%\n \\tcbox[\n answerpill,\n colback=#3!30,\n colframe=#3!60\n]{%\n \\parbox{3.7cm}{\\tiny\\textbf\\quad #2} % slightly smaller than 5cm for padding\n }%\n \\vspace{0.5mm}\n}\n\\tikzset{\n point/.style={\n circle,\n fill=#1,\n draw=white,\n line width=0.35pt,\n inner sep=1.4pt,\n font=\\tiny\\bfseries,\n text=white\n

<!-- chunk {"id": "body-0103", "role": "body", "section": "Experiments", "weight": 1.0} -->

right=1mm,\n top=0.4mm,\n bottom=0.4mm,\n boxsep=0pt,\n width=4cm \n }\n}\n\n\n\\vspace{0.1cm}\n{\\tiny\\bfseries ANSWERS}\\par\n\\AnswerPill{A}{No, the metallic orange SUV is in the lane left of the regular vehicle.}{_lightgray}\\par\n\\AnswerPill{B}{No, the metallic orange SUV is in the lane that is right of the left curb lane and the regular vehicle is in the lane that is right of the lane that is right of the left curb lane.}{_lightgray}\\par\n\\AnswerPill{\\color{green!50!black}\\checkmark}{No, the metallic orange SUV is in the lane right of the regular vehicle.}{_green}\\par\n\\AnswerPill{D}{Yes, they are in the lane that is right of the lane that is right of the left curb

<!-- chunk {"id": "body-0104", "role": "body", "section": "Experiments", "weight": 1.0} -->

to identify the two actors: Actor\\_1 is the metallic orange SUV visible in the CENTER at \\TextPin{P2}{_green}.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Experiments", "weight": 1.0} -->

Actor\\_2 is the marked vehicle.}\n\n\\StepBox{\\textbf{Step 2:} Next, I describe their respective lanes. The lane that contains Actor\\_1 is visible in CENTER \\TextPin{P3}{_teal}. The lane's description is 2nd lane from the right. The lane contains the ego and is controlled by a traffic\\_light with status green located in CENTER \\TextPin{P4}{_pink}. The lane that contains Actor\\_2 is visible in LEFT/CENTER \\TextPin{P5}{_darkyellow}.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Experiments", "weight": 1.0} -->

The lane's description is 2nd lane from the left.}\n\n\\StepBox{\\textbf{Step 3:} Based on these observations, I infer the relative position of Actor\\_1 to be right of Actor\\_2.}\n\n\\StepBox{\\textbf{Conclusion:} Hence, the correct answer is: No, the metallic orange SUV is in the lane right of the regular vehicle.}\n}\n\n\\end{minipage}\n};\n\n% Overlay dashed grey box\n\n\\draw[\n dashed,\n _gray,\n line width=0.8pt,\n rounded corners=2pt\n]([xshift=0.5mm,yshift=1.5mm]wholefig.north west) rectangle ([xshift=-5.5cm,yshift=-0.5mm]wholefig.south east);\n\\node[\n anchor=south west,\n fill=white,\n text=_gray,\n

<!-- chunk {"id": "body-0107", "role": "body", "section": "Experiments", "weight": 1.0} -->

font=\\tiny\\bfseries,\n inner xsep=1.5mm,\n inner ysep=0.6mm,\n rounded corners=1pt\n]at ([xshift=0.3cm,yshift=-2mm]wholefig.south west)\n{image and text inputs};\n\\end{tikzpicture}" language=<CodeLanguageLabel.TIKZ: 'Tikz'> Example output of the qwen3-vl-4b model with CoT (additional examples in sec:additional\_results\_qualitative) We evaluate the effectiveness of CRS-based supervision by fine-tuning vision-language models on graph-derived training data and analyzing their behavior across multiple axes.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Experiments", "weight": 1.0} -->

In particular, we focus on (i) overall performance gains, (ii) data efficiency and scaling behavior, and (iii) robustness under increasing reasoning complexity. We fine-tune models from the Qwen family using full-parameter training on 4×H100 GPUs for 5 epochs, with a learning rate of $4 \times 10^{-5}$and cosine decay.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Experiments", "weight": 1.0} -->

Performance comparison with and without CRS supervision. We first evaluate the impact of CRS supervision by comparing models with and without graph-grounded supervision. To contextualize these gains, we additionally evaluate a range of state-of-the-art open- and closed-weight VLMs, which serve as a reference point for current capabilities on structured road reasoning. To disentangle perception from reasoning, we partition the evaluation data into perception-like and reasoning-heavy samples based on the hardness of decoy answers. In perception-like tasks, the primary challenge lies in identifying the correct object or attribute from the image, after which answer selection is largely straightforward (\textit{e.g.}\@, What is the status of the traffic light that controls the crossing to the right of the intersection?Walk / Stop / Countdown). In contrast, reasoning-heavy tasks require compositional grounding: models must resolve nested descriptors, identify relevant entities through relational structure, and perform multi-step reasoning (\textit{e.g.}\@, Which lane is the ego in?The lane that is left of the emergency vehicle's lane. / The lane that contains the arrow. / The right curb lane.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Experiments", "weight": 1.0} -->

/ None of the above). A breakdown of the query templates in each category and details on the question distribution are provided in sec:qa-types\_supplementary and sec:question-type-analysis. [tab:model\_accuracy\_detailed], performance across all models degrades substantially on reasoning-heavy samples, indicating that structured reasoning remains a key challenge. After fine-tuning with CRS-derived data, we observe substantial improvements in overall accuracy and robustness to reasoning complexity. Notably, even small models exhibit strong gains, particularly on reasoning-heavy tasks (see fig:type\_spider and fig:reasoning). We further train a baseline model without visual input (cf. $-$ images in tab:model\_accuracy\_detailed) on our CRS-derived data, and find that while the model captures some road structurebecause roads inherently contain structurethere remains a significant performance gap compared to vision-augmented models and human performance, highlighting the necessity of visual grounding.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Experiments", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}\n\\pgfplotsset{set layers}\n\n\\begin{axis}[\n width=0.75\\linewidth,\n height=2.7cm,\n scale only axis,\n xlabel={CRS Graphs},\n ylabel={Accuracy},\n xmin=0, xmax=80,\n ymin=0.38, ymax=0.76,\n xtick={0,20,40,60,80},\n tick label style={font=\\footnotesize},\n label style={font=\\footnotesize},\n every axis plot/.append style={thick, mark size=2pt},\n axis y line*=left,\n]\n\\addplot[name path=upper, draw=none] coordinates {\n (0,0.4753) (20,0.6115) (40,0.6578)

<!-- chunk {"id": "body-0112", "role": "body", "section": "Experiments", "weight": 1.0} -->

draw=none]\nfill between[of=upper and lower];\n\n\\addplot[fill=_red, fill opacity=0.15, draw=none]\nfill between[of=upper2b and lower2b];\n\n\\addplot[_teal, thick, mark=*] coordinates {\n (0,0.4428) (20,0.5819) (40,0.6292) (60,0.6864) (80,0.7110)\n};\n\n\\addplot[_red, thick, mark=*] coordinates {\n (0,0.420) (20,0.5720) (40,0.6114) (60,0.6637) (80,0.6923)\n};\n\n\\node[\n anchor=south east,\n font=\\tiny,\n align=left\n] at (axis description cs:0.98,0.02) {\n

<!-- chunk {"id": "body-0113", "role": "body", "section": "Experiments", "weight": 1.0} -->

\\tikz{\\draw[_red, fill=_red] circle (2pt);}~Qwen-2B-SFT\\\\\n \\tikz{\\draw[_teal, fill=_teal] circle (2pt);}~Qwen-4B-SFT\\\\\n\\tikz[baseline={}]{\\draw[dashed] (0,0.01) -- (2.7,0.01);}~\\#Samples\n};\n\\end{axis}\n\n\\begin{axis}[\n width=0.75\\linewidth,\n height=2.7cm,\n scale only axis,\n xmin=0, xmax=80,\n ymin=0, ymax=24,\n axis y line*=right,\n axis x line=none,\n ylabel={Number of Samples},\n ytick={0,5,10,15,20,25},\n

<!-- chunk {"id": "body-0114", "role": "body", "section": "Experiments", "weight": 1.0} -->

yticklabels={0,5k,10k,15k,20k,25k},\n tick label style={font=\\footnotesize},\n label style={font=\\footnotesize},\n every axis plot/.append style={thick, mark size=2pt},\n]\n\\addplot[\n gray,\n dashed,\n mark size=1.5pt\n] coordinates {\n (20,5.740) (40,10.512) (60,16.544) (80,22.833)\n};\n\\end{axis}\n\n\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Accuracy over number of CRS-scenes, with sample counts on the secondary axis.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Experiments", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}\n\\pgfplotsset{set layers}\n\n\\begin{axis}[\n width=0.75\\linewidth,\n height=2.7cm,\n scale only axis,\n ymin=0.23, ymax=0.88,\n xmin=0, xmax=3,\n xtick={0,1,2,3},\n xticklabels={1,2,3,{$>3$}},\n xlabel={Reasoning depth},\n ylabel={Accuracy},\n clip=false,\n tick label style={font=\\footnotesize},\n label style={font=\\footnotesize},\n every axis plot/.append style={thick, mark size=2pt},\n]\n\n\\addplot[name path=qwenCotUpper, draw=none] coordinates {\n

<!-- chunk {"id": "body-0116", "role": "body", "section": "Experiments", "weight": 1.0} -->

(0,0.856271) (1,0.825613) (2,0.865811) (3,0.7860882)\n};\n\\addplot[name path=qwenCotLower, draw=none] coordinates {\n (0,0.752064) (1,0.685581) (2,0.711649) (3,0.6261177)\n};\n\\addplot[fill=_red, fill opacity=0.15, draw=none]\nfill between[of=qwenCotUpper and qwenCotLower];\n\n\\addplot[name path=qwenUpper, draw=none] coordinates {\n (0,0.860206) (1,0.808710) (2,0.884865) (3,0.778117)\n};\n\\addplot[name path=qwenLower, draw=none] coordinates {\n

<!-- chunk {"id": "body-0117", "role": "body", "section": "Experiments", "weight": 1.0} -->

(0,0.760968) (1,0.653226) (2,0.740712) (3,0.618705)\n};\n\\addplot[fill=_teal, fill opacity=0.15, draw=none]\nfill between[of=qwenUpper and qwenLower];\n\n\\addplot[name path=gptUpper, draw=none] coordinates {\n (0,0.809525) (1,0.806452) (2,0.702703) (3,0.588235)\n};\n\\addplot[name path=gptLower, draw=none] coordinates {\n (0,0.706350) (1,0.664516) (2,0.522523) (3,0.426471)\n};\n\\addplot[fill=_green, fill opacity=0.15, draw=none]\nfill

<!-- chunk {"id": "body-0118", "role": "body", "section": "Experiments", "weight": 1.0} -->

between[of=gptUpper and gptLower];\n\n\\addplot[name path=baseUpper, draw=none] coordinates {\n (0,0.591270) (1,0.612903) (2,0.549549) (3,0.455882)\n};\n\\addplot[name path=baseLower, draw=none] coordinates {\n (0,0.468254) (1,0.458065) (2,0.369368) (3,0.294118)\n};\n\\addplot[fill=_orange, fill opacity=0.15, draw=none]\nfill between[of=baseUpper and baseLower];\n\n\\addplot+[solid, mark=*, color=_red, mark options={fill=_red}]\ncoordinates {\n (0,0.8030) (1,0.7582) (2,0.7884)

<!-- chunk {"id": "body-0119", "role": "body", "section": "Experiments", "weight": 1.0} -->

(3,0.7057)\n};\n\n\\addplot+[solid, mark=*, color=_teal, mark options={fill=_teal}]\ncoordinates {\n (0,0.8174) (1,0.7342) (2,0.8188) (3,0.7027)\n};\n\n\\addplot+[solid, mark=*, color=_green, mark options={fill=_green}]\ncoordinates {\n (0,0.7478) (1,0.7482) (2,0.625) (3,0.496)\n};\n\n\\addplot+[solid, mark=*, color=_orange, mark options={fill=_orange}]\ncoordinates {\n (0,0.5261) (1,0.5244) (2,0.4711)

<!-- chunk {"id": "body-0120", "role": "body", "section": "Experiments", "weight": 1.0} -->

(3,0.3588)\n};\n\n\\node[\n anchor=south west,\n font=\\tiny,\n align=left\n] at (axis description cs:0.02,0.02) {\n \\tikz{\\draw[_red, fill=_red] circle (2pt);}~Qwen-4B-SFT-CoT\\\\\n \\tikz{\\draw[_teal, fill=_teal] circle (2pt);}~Qwen-4B-SFT\\\\\n \\tikz{\\draw[_orange, fill=_orange] circle (2pt);}~Qwen-4B\\\\\n \\tikz{\\draw[_green, fill=_green] circle (2pt);}~GPT-5.4\n};\n\\end{axis}\n\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ:

<!-- chunk {"id": "body-0121", "role": "body", "section": "Experiments", "weight": 1.0} -->

'Tikz'> Accuracy by reasoning depth with 95% CI. Additional results in sec:additional\_results.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Experiments", "weight": 1.0} -->

Data efficiency and scaling. Next, we analyze how performance scales with the number of CRS graphs used for training by varying the number of scenes and measuring downstream accuracy. As shown in fig:scaling, performance improves consistently with additional data, while exhibiting diminishing returns at larger scales. Notably, training on as few as 40 scenes already surpasses the performance of strong closed-source baselines. This highlights the data efficiency of CRS supervision: even in the low-data regime, the compositional structure of graph-derived queries provides dense and informative training signals, while creating a large training set from just a few scenes.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Experiments", "weight": 1.0} -->

Reasoning depth analysis. A central question is whether CRS supervision improves robustness to increasing reasoning complexity. Leveraging the programmatic structure of CRS, we quantify reasoning depth directly from the graph by measuring the number of compositional steps required to resolve a query. While the maximum descriptor depth for individual nodes is limited to two, queries may involve multiple uniquely referenced objects across questions, answers, and distractors, resulting in a broad spectrum of effective reasoning depths. To evaluate the impact of CRS supervision, we partition the evaluation set by reasoning depth, \textit{i.e.}\@, number of hops on the graph required to solve the task. As shown in fig:accuracy\_by\_reasoning\_depth, models trained with CRS supervision maintain stable performance as reasoning depth increases, in contrast to both the base model and strong closed-source baselines, which exhibit a pronounced degradation. This indicates that CRS supervision enables models to reliably decompose nested descriptors and execute multi-step relational reasoning over the scene.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Experiments", "weight": 1.0} -->

Building on this, the CRS framework provides a unique opportunity to trace performance differences back to specific reasoning failures. While CoT supervision does not necessarily improve aggregate accuracy (cf. tab:model\_accuracy\_detailed), it enables fine-grained analysis of where and how models fail. For this analysis, we sample 250 questions from the validation set following the property-query schema (see sec:queries). These questions target relatively simple propertiessuch as lane direction, marking type, or colorbut require a well-defined sequence of reasoning steps. Importantly, each question can only be solved by completing the three links in the reasoning chain (cf. sec:reasoning): (i) Localizing the anchor object mentioned in the question, \textit{i.e.}\@, the last step in a multi-hop descriptor, (ii) resolving the relational description to identify the target node and (iii) retrieving the relevant property. Finally, the last step consists of (iv) choosing the correct option.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Experiments", "weight": 1.0} -->

We inspect, for both correct and incorrect predictions, which of these steps are executed correctly. For correct answers, this provides a measure of reasoning consistency: cases where the answer is correct despite incorrect intermediate reasoning indicate spurious correlations. For incorrect answers, the first failed step reveals the origin of the error. For correctly answered questions, our model exhibits higher consistency between reasoning and final predictions (fig:left\_hist). More importantly, the analysis of incorrect predictions reveals a qualitative difference: in our model, the first failure most often occurs at the property extraction stage, after successfully resolving the object through multi-hop reasoning (fig:first\_failure\_parts). In contrast, the closed-source model predominantly fails at earlier stages of anchor identification and descriptor decomposition, indicating difficulties in navigating the scene structured in the first place. This suggests that models fine-tuned with CRS-data have internalized the compositional structure of the road scene.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Experiments", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}\n\\begin{axis}[\n width=5cm,\n height=4cm,\n xbar,\n xmin=0, xmax=24,\n ytick=data,\n symbolic y coords={\n wrong answer selected,\n property not detected,\n deconstruction wrong,\n anchor misidentified\n},\nyticklabels={\n {\\renewcommand{\\arraystretch}{0.8}%\n \\shortstack[r]{\\scriptsize{wrong} \\\\ \\scriptsize{answer selected}}},\n {\\renewcommand{\\arraystretch}{0.8}%\n \\shortstack[r]{\\scriptsize{property} \\\\ \\scriptsize{not detected}}},\n {\\renewcommand{\\arraystretch}{0.8}%\n

<!-- chunk {"id": "body-0127", "role": "body", "section": "Experiments", "weight": 1.0} -->

\\shortstack[r]{\\scriptsize{deconstruction} \\\\ \\scriptsize{wrong}}},\n {\\renewcommand{\\arraystretch}{0.8}%\n \\shortstack[r]{\\scriptsize{anchor} \\\\ \\scriptsize{misidentified}}}\n},\n xlabel={Errors in reasoning for correct samples (\\%)},\n tick label style={font=\\scriptsize},\n label style={font=\\scriptsize},\n legend style={\n at={(0.5,1.05)},\n anchor=south,\n legend columns=1,\n font=\\tiny,\n draw=none\n },\n bar width=3pt,\n enlarge y limits=0.2,\n]\n\n% --- Qwen-4B ---\n\\addplot+[xbar, fill=_green,

<!-- chunk {"id": "body-0128", "role": "body", "section": "Experiments", "weight": 1.0} -->

draw=_green, yshift=0pt]\ncoordinates {\n (0.00,wrong answer selected)\n (0.71,property not detected)\n (22.3,deconstruction wrong)\n (14.3,anchor misidentified)\n};\n\n% --- GPT-5.4 ---\n\\addplot+[xbar, fill=_orange, draw=_orange, yshift=0pt]\ncoordinates {\n (0.00,wrong answer selected)\n (1.2,property not detected)\n (16.40,deconstruction wrong)\n (10.00,anchor misidentified)\n};\n\n\n% --- Qwen-4B-sft ---\n\\addplot+[xbar, fill=_red, draw=_red, yshift=0pt]\ncoordinates {\n (0.4,wrong answer selected)\n (0.8,property not detected)\n

<!-- chunk {"id": "body-0129", "role": "body", "section": "Experiments", "weight": 1.0} -->

(7.6,deconstruction wrong)\n (6.0,anchor misidentified)\n};\n\n\\node[\n anchor=south east,\n font=\\tiny,\n align=left\n] at (axis description cs:0.98,0.02) {\n \\tikz[baseline=-0.7ex]{\\draw[_red, fill=_red] (0pt,0pt) circle[radius=2pt];}~Qwen-4B-SFT\\\\\n \\tikz[baseline=-0.7ex]{\\draw[_orange, fill=_orange] (0pt,0pt) circle[radius=2pt];}~GPT-5.4\\\\\n \\tikz[baseline=-0.7ex]{\\draw[_green, fill=_green] (0pt,0pt)

<!-- chunk {"id": "body-0130", "role": "body", "section": "Experiments", "weight": 1.0} -->

circle[radius=2pt];}~Qwen-4B\n};\n\\end{axis}\n\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Distribution of all wrong links in the reasoning chain for samples where the model's final answer is correct.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Experiments", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}\n\n\\pgfplotsset{\n /pgfplots/legend image code/.code={\n \\draw[\n mark=*,\n mark size=0.5pt,\n only marks,\n draw=none,\n #1\n] plot coordinates {(0cm,0cm)};\n }\n}\n\n\\begin{axis}[\n width=5cm,\n height=1.7cm,\n scale only axis,\n xbar stacked,\n xmin=0, xmax=100,\n ytick=data,\n symbolic y coords={\n Qwen-4B-sft,\n GPT-5.4,\n Qwen-4B\n },\n yticklabels={\n Qwen-4B-sft,\n GPT-5.4,\n Qwen-4B\n },\n xlabel={First failure in

<!-- chunk {"id": "body-0132", "role": "body", "section": "Experiments", "weight": 1.0} -->

reasoning chain for incorrect samples (\\%)},\n xtick={0,25,50,75,100},\n tick label style={font=\\scriptsize},\n label style={font=\\scriptsize},\n legend style={\n at={(0.5,1.0)},\n anchor=south,\n legend columns=2,\n font=\\tiny,\n draw=none\n },\n legend cell align=left,\n legend image post style={draw=none},\n bar width=10pt,\n enlarge y limits=0.35,\n]\n\n\\addplot+[xbar, fill=_red, draw=_red]\ncoordinates {\n (13.16,Qwen-4B-sft)\n (31.15,GPT-5.4)\n (38.33,Qwen-4B)\n};\n\n\\addplot+[xbar, fill=_teal,

<!-- chunk {"id": "body-0133", "role": "body", "section": "Experiments", "weight": 1.0} -->

draw=_teal]\ncoordinates {\n (18.42,Qwen-4B-sft)\n (37.70,GPT-5.4)\n (38.33,Qwen-4B)\n};\n\n\\addplot+[xbar, fill=_orange, draw=_orange]\ncoordinates {\n (65.79,Qwen-4B-sft)\n (31.15,GPT-5.4)\n (20.00,Qwen-4B)\n};\n\n\\addplot+[xbar, fill=_green, draw=_green]\ncoordinates {\n (2.63,Qwen-4B-sft)\n (0.00,GPT-5.4)\n (3.33,Qwen-4B)\n};\n\n\\legend{\n anchor misidentified,\n deconstruction wrong,\n property not detected,\n wrong answer

<!-- chunk {"id": "body-0134", "role": "body", "section": "Experiments", "weight": 1.0} -->

selected\n}\n\\end{axis}\n\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Distribution of first wrong link in the reasoning chain for samples where the model's final answer is incorrect.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Discussion and conclusion", "weight": 1.5} -->

This work introduces the Combined Road Substrate (CRS), a graph-grounded framework that unifies geometric structure and open-vocabulary semantics in a jointly executable representation. By formulating reasoning as queries over this substrate, CRS enables the automatic generation of grounded, compositional supervision signals, yielding substantial gains in structured road reasoning even in low-data regimes. Our analysis further demonstrates that structured supervision fundamentally shifts model behavior, redirecting failures from relational reasoning to localized perceptual errors.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Discussion and conclusion", "weight": 1.5} -->

Limitations and future work.While CRS improves structural reasoning, performance remains bounded by the quality of underlying visual perception, indicating that further gains depend on advances in perception models. Additionally, CRS construction currently relies on human curation; future work could leverage reinforcement learning to automate selective abstraction and enrichment. Lastly, while this work focuses on the substrate of road understanding, we do not explicitly tackle downstream driving performance. However, we believe that CRS provides a promising grounded intermediate representation for future vision-language-action (VLA) driving systems, while executable and compositional structure may offer a natural interface between semantic reasoning and policy learning — an important direction left for future work.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Discussion and conclusion", "weight": 1.5} -->

AcknowledgementsThe research work was partially funded by the Swedish Foundation for Strategic Research (SSF) under the project DeltaMap (-0045). This work was partially supported by the Wallenberg AI, Autonomous Systems and Software Program (WASP) funded by the Knut and Alice Wallenberg Foundation. This material is based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Agreement Number 00011869. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the Defense Advanced research Projects Agency (DARPA). We thank Patric Jensfelt and Rafael Valencia for their feedback on this work.
