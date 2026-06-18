<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

CRISPR-GPT for Agentic Automation of Gene-editing Experiments

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The introduction of genome engineering technology has transformed biomedical research, making it possible to make precise changes to genetic information. However, creating an efficient gene-editing system requires a deep understanding of CRISPR technology, and the complex experimental systems under investigation. While Large Language Models (LLMs) have shown promise in various tasks, they often lack specific knowledge and struggle to accurately solve biological design problems. In this work, we introduce CRISPR-GPT, an LLM agent augmented with domain knowledge and external tools to automate and enhance the design process of CRISPR-based gene-editing experiments. CRISPR-GPT leverages the reasoning ability of LLMs to facilitate the process of selecting CRISPR systems, designing guide RNAs, recommending cellular delivery methods, drafting protocols, and designing validation experiments to confirm editing outcomes. We showcase the potential of CRISPR-GPT for assisting non-expert researchers with gene-editing experiments from scratch and validate the agent's effectiveness in a real-world use case. Furthermore, we explore the ethical and regulatory considerations associated with automated gene-editing design, highlighting the need for responsible and transparent use of these tools.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our work aims to bridge the gap between beginner biological researchers and CRISPR genome engineering techniques, and demonstrate the potential of LLM agents in facilitating complex biological discovery tasks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Gene editing technology represents a groundbreaking scientific advancement that enables precise alterations to the genetic material of living organisms. This innovative technique has found extensive applications across various fields of biology and medicine, from correcting genetic defects responsible for disorders like cystic fibrosis, hemophilia, and sickle cell anemia, to offering new strategies in the battle against complex conditions such as cancer, cardiovascular diseases, neurodegenerative disorders, and infections. A most well-known gene editing system is called CRISPR-Cas9. It was adapted from a naturally occurring genome editing system that bacteria use as an immune defense. Beyond CRISPR-Cas9, recent advancements have led to the development of CRISPR activation/interference, CRISPR-based prime editing and base editing technologies. CRISPR activation/interference, also called CRISPRa/CRISPRi, are able to either enhance gene expression or silence the activities of specific genes via epigenetic regulation. Prime editing, considered a "search and replace" method for DNA, allows for precise editing capabilities without introducing double-stranded breaks. Base editing, on the other hand, enables the direct, irreversible conversion of one DNA base into another at targeted locations, further expanding the toolkit for precise genome modification.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

All these technologies hold potential for broad applications in medicine, agriculture, and beyond, enhancing the scope of genome editing in pursuing treatments for genetic diseases and other applications.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Designing gene-editing experiments requires deep understanding of the suite of technologies and the associated biology of target organs. CRISPR Cas-based editing works by interacting with the RNA of a short "guide" sequence (guide RNA) that binds to a specific target sequence in a cell's DNA, much like the RNA segments bacteria produce from the CRISPR array. When introduced into cells, the guide RNA recognizes the intended DNA sequence, and the Cas enzyme (often Cas9 or others) cuts the DNA at the targeted location, mirroring the process in bacteria. There are numerous considerations when designing such experiments, including the selection of a well-suited gene-editing system, the development of optimal guide sequences, and validation approach. This typically requires significant domain expertise, understanding of biology of the target organ, as well as trial-and-error efforts. Developing AI-assisted computation tools to aid gene-editing holds great promise to make the technology more accessible and accelerate both scientific and therapeutic developments.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Large language models (LLMs) have demonstrated exceptional capabilities in language skills and encapsulate a tremendous amount of world knowledge, approximating aspects of artificial general intelligence. Recent research has also explored enhancing LLMs with external tools, improving their problem-solving abilities and efficiency. LLMs have also demonstrated potential as tool makers and black-box optimizers. Researchers have explored LLM-based specialized models for various application domains, as well as for solving scientific and mathematical tasks. For example, ChemCrow uses tool-augmented LM for solving a range of chemistry-related tasks such as paracetamol synthesis, whereas Coscientist, also driven by GPT-4 and integrated automated experimentation, achieved successful optimization of palladium-catalyzed cross-coupling reaction.

<!-- chunk {"id": "body-0008", "role": "body", "section": "General-purpose LLMs do not know how to design biological experiments", "weight": 1.0} -->

While leveraging large language models (LLMs) for aiding in the design of gene-editing experiments presents an enticing prospect, the current state-of-the-art general-purpose models exhibit significant shortcomings in this specialized domain. These models, despite their vast knowledge base, lack the precise, up-to-date domain-specific knowledge essential for the accurate design of biological experiments.

<!-- chunk {"id": "body-0009", "role": "body", "section": "General-purpose LLMs do not know how to design biological experiments", "weight": 1.0} -->

A critical limitation of general-purpose LLMs is their propensity for "hallucinations" or generating confident yet inaccurate responses when tasked with specialized biological queries. For instance, when tasked with designing a guide RNA (gRNA) sequence for targeting specific human genes, such as EMX1 or EGFR, general-purpose LLMs like ChatGPT-3/ChatGPT-4 can respond incorrect sequence with high confidence. However, the gRNA sequences they provide often do not correspond to any known genomic region. This discrepancy can be readily identified by comparing the LLM-generated sequences with reference sequences in databases such as the NCBI's BLAST tool, which aligns sequences to the human genome and transcriptome. Such hallucinated design sequences not only lack utility but can mislead researchers, potentially leading to wasted resources and time if not properly vetted.

<!-- chunk {"id": "body-0010", "role": "body", "section": "General-purpose LLMs do not know how to design biological experiments", "weight": 1.0} -->

In addition, responses generated from general-purpose LLMs usually lack essential details necessary for the experimental design, such as specific materials, protocols, considerations for off-target effects, gRNA efficiency, and specificity. Such gaps in information can leave researchers, especially those new to the field of gene editing, unprepared for the practical execution of experiments.

<!-- chunk {"id": "body-0011", "role": "body", "section": "General-purpose LLMs do not know how to design biological experiments", "weight": 1.0} -->

Furthermore, it is crucial to note that responses generated may contain overwhelming information that does not directly contribute to the gene-editing experimental designs. Such irrelevant text can lead to confusion and misdirection, complicating the researcher's task of identifying the most pertinent and practical information for their gene-editing objectives.

<!-- chunk {"id": "body-0012", "role": "body", "section": "General-purpose LLMs do not know how to design biological experiments", "weight": 1.0} -->

All of these limitations underscore the necessity for a new class of LLMs tailored specifically for the gene-editing experimental designs (We refer readers to Appendix A for more examples of failures). Such models would need to integrate deep, accurate domain knowledge with the ability to critically evaluate and generate experimentally viable solutions, thereby overcoming the current barriers faced by general-purpose LLMs in the design of CRISPR gene-editing experiments.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Overview of CRISPR-GPT", "weight": 1.0} -->

In the rapidly evolving field of genetic engineering, CRISPR technology has become a pivotal tool for precise gene editing. Despite its promise, the intricacy of designing CRISPR experiments---from guide RNA (gRNA) selection to predicting off-target effects---presents significant challenges, especially to those new to the field. To bridge this gap, we introduce CRISPR-GPT, a novel solution that combines the strengths of Large Language Models (LLMs) with domain-specific knowledge and computational tools, specifically tailored for CRISPR gene editing tasks.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Overview of CRISPR-GPT", "weight": 1.0} -->

CRISPR-GPT is centered around a tailor-made LLM-powered design and planning agent. This engine of the agent not only draws upon expert knowledge from leading practitioners in gene editing but also integrates a broad review of recent literature and a suite of computational toolkits including guideRNA design tool.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Overview of CRISPR-GPT", "weight": 1.0} -->

Selection of CRISPR System: Tailoring the choice of CRISPR system to the experiment's needs.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Overview of CRISPR-GPT", "weight": 1.0} -->

gRNA Design: Optimizing guide RNA sequences for efficiency and specificity based on the Broad Institute's gold-standard guideRNA library and CRISPRPick toolkit, including pre-designed gRNA libraries.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Overview of CRISPR-GPT", "weight": 1.0} -->

Delivery Approach Selection: Advising on the most effective methods to introduce the CRISPR components into target cells.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Overview of CRISPR-GPT", "weight": 1.0} -->

Prediction of Off-target Effects: Assessing potential unintended alterations alongside desired edits.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Overview of CRISPR-GPT", "weight": 1.0} -->

Recommendation of Experimental Protocols: Outlining step-by-step procedures tailored to the experiment's objectives.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Overview of CRISPR-GPT", "weight": 1.0} -->

Validation Approach Recommendation and Primer Design: Recommending gest ways to validate the edits and help design the associated primers.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Overview of CRISPR-GPT", "weight": 1.0} -->

This approach, leveraging a chain-of-thought reasoning model and state machines, ensures that even individuals new to gene editing can iteratively refine their experimental designs to achieve protocols that meet their specific research needs.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Overview of CRISPR-GPT", "weight": 1.0} -->

A Freestyle Q&A Mode for addressing ad hoc queries with precision,

<!-- chunk {"id": "body-0023", "role": "body", "section": "Overview of CRISPR-GPT", "weight": 1.0} -->

An Off-target Prediction Mode for in-depth analysis of pre-designed gRNAs.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Overview of CRISPR-GPT", "weight": 1.0} -->

These functions help the users when they meet additional issues during the experimental design process.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Overview of CRISPR-GPT", "weight": 1.0} -->

Mindful of the ethical and safety considerations surrounding gene editing, especially in human applications, we have integrated safeguards into CRISPR-GPT. These include restrictions on its use in human subjects, measures to ensure the privacy of genetic information, and alerts for potential unintended consequences, reflecting our commitment to responsible use in alignment with the broader scientific and ethical discourse on gene editing technologies.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Large Language Model", "weight": 1.0} -->

The CRISPR-GPT agent consists of the following 4 core modules: LLM planner, Tool provider, Task executor, and the LLM Agent that serve as the interface with users for taking inputs and communicate outputs.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Task Executor operates as state machines, providing robust subgoal decomposition and progress control", "weight": 1.0} -->

We implement 22 tasks, summarized in Table, in the form of state machines for CRISPR-GPT. The state machines are responsible for providing sufficient instruction for the current task and guiding the user to fulfill the decision-making through multiple rounds of textual interactions. Through these state machines, we manually decompose each task into sub-goals for the task executor. Specifically, each state is responsible for one particular sub-goal. The transition logic is well-defined so the task executor can properly transit to another sub-goal based on the current progress.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Task Executor operates as state machines, providing robust subgoal decomposition and progress control", "weight": 1.0} -->

We have 4 predefined Meta-Tasks that support the full pipelines of 4 gene-editing-related experiments; see Table. Besides, the LLM planner can generate a customized list of tasks depending on the user's meta-request. The state machines of the corresponding tasks are chained together as a bigger state machine to support the entire pipeline.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Tool Provider connects Task Executor with external APIs", "weight": 1.0} -->

To connect language models with external functionalities, the system needs to analyze the current situation and judge whether it's suitable to call an external tool; know what kinds of tools are available and choose the best from them. Instead of directly exposing the interfaces of the APIs to LLMs, in CRISPR-GPT, we wrap the usage of APIs inside the states and expose more user-friendly and LLM-friendly textual interfaces through hand-written instructions and responses. In plain words, we are teaching users (human agents & LLM agents) to use the tools. The tools include Google web search, running programs like Primer3, as well as retrieval from external guide RNA libraries, research papers, and experiment protocols.

<!-- chunk {"id": "body-0030", "role": "body", "section": "LLM-planner automatically generates a list of tasks based on the user's request", "weight": 1.0} -->

Large Language Models (LLMs) such as GPT-4, Gemini, and Claude can serve as the reasoning core of the LLM-powered agent to solve real-world decision-making problems. We adopt the popular ReAct prompting technique, where the LLM is prompted to output the chain-of-thought reasoning path and the final action from the plausible action set. To let LLMs perform task decomposition, we provide a table of the descriptions and the dependencies of all the tasks as a prompt to the LLM. Based on LLM's internal knowledge as well as our manually written descriptions of tasks and instruction of task decomposition, LLM can intelligently analyze the user's request and decompose the user's request into a sequence of tasks, respecting the dependencies of the tasks. After the decomposition, the corresponding state machines are chained together to complete all the tasks. The prompt format of the task decomposition can be found in Appendix B.

<!-- chunk {"id": "body-0031", "role": "body", "section": "LLM-planner automatically generates a list of tasks based on the user's request", "weight": 1.0} -->

For robustness, we do not allow LLMs to dynamically add/delete new tasks (new state machines) during the automatic execution. However, we believe this is an important step toward a more intelligent CRISPR-GPT version and leave this as future work.

<!-- chunk {"id": "body-0032", "role": "body", "section": "LLM-Agent automatically interacts with the Task Executor based on the user's meta request", "weight": 1.0} -->

In addressing the complex challenge of automating CRISPR gene editing tasks, we conceptualize the problem through the lens of sequential decision-making. This perspective frames the interaction between the user and the automated system as a series of steps, each requiring precise decisions to progress towards the ultimate goal of experiment design and execution. Central to our system is the LLM-agent, which acts as an intermediary between the user and a state machine. This state machine is derived from an initial task decomposition step, effectively breaking down the gene editing process into a structured sequence of actions and decisions. At each step in this sequence, the state machine presents a current state to the LLM-agent. This state encapsulates a description of the task at hand and specifies any input required from the user to move forward.

<!-- chunk {"id": "body-0033", "role": "body", "section": "LLM-Agent automatically interacts with the Task Executor based on the user's meta request", "weight": 1.0} -->

The LLM-agent's role is to interpret the current state and make informed decisions on behalf of the user.

<!-- chunk {"id": "body-0034", "role": "body", "section": "LLM-Agent automatically interacts with the Task Executor based on the user's meta request", "weight": 1.0} -->

The instruction inherent to the current state,

<!-- chunk {"id": "body-0035", "role": "body", "section": "LLM-Agent automatically interacts with the Task Executor based on the user's meta request", "weight": 1.0} -->

The specific request made by the user,

<!-- chunk {"id": "body-0036", "role": "body", "section": "LLM-Agent automatically interacts with the Task Executor based on the user's meta request", "weight": 1.0} -->

A history of past interactions within the current task session,

<!-- chunk {"id": "body-0037", "role": "body", "section": "LLM-Agent automatically interacts with the Task Executor based on the user's meta request", "weight": 1.0} -->

Results from external computational tools that have been integrated into the system.

<!-- chunk {"id": "body-0038", "role": "body", "section": "LLM-Agent automatically interacts with the Task Executor based on the user's meta request", "weight": 1.0} -->

This information is synthesized into a prompt for the LLM-agent, which then uses its capabilities to determine the most appropriate next action. The format and structure of these prompts, designed to optimize the decision-making process, are detailed in Appendix B.

<!-- chunk {"id": "body-0039", "role": "body", "section": "LLM-Agent automatically interacts with the Task Executor based on the user's meta request", "weight": 1.0} -->

User oversight is a critical component of this system. While the LLM-agent operates autonomously, the user is not removed from the process. Instead, they are encouraged to monitor the progression of tasks and interact with the agent. This setup ensures that any errors or misinterpretations by the LLM-agent can be quickly identified and corrected by the user, maintaining the accuracy and integrity of the gene editing experiment design. This approach to automation emphasizes a collaborative synergy between human expertise and artificial intelligence. By leveraging the LLM-agent's ability to process and act on complex information, we facilitate a more efficient and user-friendly experience in designing CRISPR gene editing experiments. The sequential decision-making framework not only streamlines the task execution process but also ensures that user input remains a cornerstone of experiment planning and design.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Human evaluation", "weight": 1.0} -->

To evaluate the CRISPR-GPT agent's effectiveness in aiding gene editing and experimental design, we assembled a diverse group of 12 experts in the field of CRISPR and gene editing research. Each of the 12 experts rated the responses to the experimental design tasks from three modes on a scale from 1 (Poor) to 5 (Excellent) according to the established criteria (all rubrics for the human evaluation are detailed in Appendix C). To offer a comparative perspective, outputs from both ChatGPT 3.5 and ChatGPT 4.0 (model version gpt-4-0613) were generated using similar prompts and evaluated using the same criteria.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Biological experiment and wet-lab validation", "weight": 1.0} -->

We performed biological experiments through human-agent collaboration using CRISPR-GPT with ChatGPTv4 API, as wet-lab based real world validation of our approach. Specifically, we have independent scientist who are not familiar with gene-editing experiment to use CRISPR-GPT to facilitate their knock-out (KO) gene-editing experiments in a cancer research project. Detailed methods are provided below.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Biological experiment and wet-lab validation", "weight": 1.0} -->

Cell line and cell culture. A375 cell line was cultured in DMEM, high glucose, GlutaMAX (Gibco) supplemented with 10% fetal bovine serum (FBS, Gemini Bio), 100 U/ml penicillin and 100ug/ml streptomycin (Gibco) at 37 ^∘^C with 5% CO2.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Biological experiment and wet-lab validation", "weight": 1.0} -->

crRNA cloning. Cloning of 4 crRNAs (TGFBR1/SNAI1/BAX/BCL2L1) was performed with BbsI or Esp3I (NEB) through a Golden Gate assembly approach into a expressing backbone backbone. Constructs were sequence verified by Sanger sequencing using a U6 sequencing primer: 5'-GACTATCATATGCTTACCGT-3'.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Biological experiment and wet-lab validation", "weight": 1.0} -->

Lentivirus packaging and transduction. Lentivirus was produced by co-transfecting the assembled lentiviral vector with VSV-G envelope and Delta-Vpr packaging plasmids into HEK-293T cells using PEI transfection reagent (Sigma-Aldrich). Supernatant was harvested 48 hr after transfection. A375 cells were transduced at low MOI with 8$µg$/mL polybrene using a spin-infection at 1000\*g for 45 minutes. After 24 hours, cells were selected with 1$µg$/mL puromycin to establish stably expressing cell lines.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Biological experiment and wet-lab validation", "weight": 1.0} -->

gDNA extraction, PCR and sequencing. Genomic DNA was extracted from selected cells 7 days later using QuickExtract (Lucigen). The targeted loci were then amplified using Phusion Flash High-Fidelity PCR Master Mix (ThermoFisher Scientific) according to the manufacturer's instructions with primers containing Illumina sequencing adapters. Paired-end reads (150 bp) were generated on an Illumina MiSeq platform.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Results", "weight": 1.0} -->

CRISPR-GPT leverages the reasoning abilities of LLM, domain knowledge, retrieval techniques and external tools to provide a comprehensive solution to gene-editing experimental design tasks. It supports a wide arrange of gene editing scenarios, including single gene knockout, base editing without double strand breaks, insertions/deletions/replacement via prime editing, epigenetic editing for activation or repression of genes (CRISPRa and CRISPRi).

<!-- chunk {"id": "body-0047", "role": "body", "section": "CRISPR-GPT assists researchers with gene-editing experimental design through three modules", "weight": 1.0} -->

The CRISPR-GPT agent aids researchers in designing gene-editing experiments via three distinct modules. "Meta Mode" equips users, especially newcomers to the gene-editing field, with expertly defined pipelines for general gene editing scenarios (termed Meta-tasks). "Auto Mode" automatically generates a tailored list of necessary design tasks based on user input, facilitating goal achievement for users of all experience levels. "Q&A Mode" functions as an advanced GPT-4 chatbot, addressing users' CRISPR and gene-editing related queries throughout the design process.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Meta Mode", "weight": 1.0} -->

"Meta Mode" involves the planning and implementation of 22 unique gene-editing experimental design tasks utilizing four types of CRISPR-based gene editing systems (Meta-tasks). It leverages predefined pipelines to help users complete a Meta-task thoroughly. In this mode, the CRISPR-GPT agent guides users through each task necessary for designing gene editing experiments. This includes selecting the appropriate CRISPR system, recommending delivery methods, designing the sgRNA, predicting sgRNA off-target efficiency, selecting experimental protocols, and planning validation experiments.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Meta Mode", "weight": 1.0} -->

For every design task, the CRISPR-GPT agent interacts with users, applying various techniques and external tools to deliver the optimal solution. For example, in choosing CRISPR systems, CRISPR-GPT continuously interacts with users, providing instructions and collecting information to suggest options based on published protocols. For context-sensitive tasks like delivery method recommendations, CRISPR-GPT not only suggests common methods but also offers customized solutions based on the user's requests through web search. For sgRNA/pegRNA designs, a multi-species database derived from existing designs and publications enables CRISPR-GPT to swiftly suggest pre-designed sgRNA based on user information. Following sgRNA/pegRNA design, users can evaluate designed guides' potential off-target effects with detailed instructions and code from CRISPR-GPT. After completing design tasks, CRISPR-GPT offers selected protocols based on the interaction history, including CRISPR system selection and delivery methods. Finally, for the validation task, CRISPR-GPT utilizes external APIs, like Primer3, to assist users in designing primers for validation experiments.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Meta Mode", "weight": 1.0} -->

Gene editing scenarios
Individual Design Tasks

<!-- chunk {"id": "body-0051", "role": "body", "section": "Meta Mode", "weight": 1.0} -->

Single/multiple genes knockout, deletion of gene fragments
CRISPR/Cas system selection

<!-- chunk {"id": "body-0052", "role": "body", "section": "Meta Mode", "weight": 1.0} -->

validation protocol recommendation and primer design for sequencing

<!-- chunk {"id": "body-0053", "role": "body", "section": "Meta Mode", "weight": 1.0} -->

CRISPR activation /interference
Gene activation and repression
CRISPR/Cas Activation/Interference system selection

<!-- chunk {"id": "body-0054", "role": "body", "section": "Meta Mode", "weight": 1.0} -->

sgRNA design for activation/interference

<!-- chunk {"id": "body-0055", "role": "body", "section": "Meta Mode", "weight": 1.0} -->

validation protocol recommendation and primer design for qPCR

<!-- chunk {"id": "body-0056", "role": "body", "section": "Meta Mode", "weight": 1.0} -->

CRISPR Base Editing
Single base replacement from CG to AT or AT to CG and broad mutagenesis
Base editing system selection

<!-- chunk {"id": "body-0057", "role": "body", "section": "Meta Mode", "weight": 1.0} -->

sgRNA design for base editing

<!-- chunk {"id": "body-0058", "role": "body", "section": "Meta Mode", "weight": 1.0} -->

validation protocol recommendation and primer design for sequencing

<!-- chunk {"id": "body-0059", "role": "body", "section": "Meta Mode", "weight": 1.0} -->

CRISPR Prime Editing
Small fragment insertion, replacement, and deletion
Prime editing system selection

<!-- chunk {"id": "body-0060", "role": "body", "section": "Meta Mode", "weight": 1.0} -->

pegRNA design for prime editing

<!-- chunk {"id": "body-0061", "role": "body", "section": "Meta Mode", "weight": 1.0} -->

validation protocol recommendation and primer design for sequencing

<!-- chunk {"id": "body-0062", "role": "body", "section": "Auto Mode", "weight": 1.0} -->

"Auto Mode" also facilitates the planning and execution of 13 unique gene-editing experimental design tasks. Unlike "Meta Mode," it does not rely on predefined meta-tasks and pipelines; instead, it uses an LLM-planner to break down a user's request into a sequence of dependent tasks. For instance, if a user requests to "design sgRNA to knockout human EGFR," the CRISPR-GPT agent identifies the keywords from the request and lists the necessary design tasks, like "CRISPR/Cas system selection" and "sgRNA design for knockout." Additionally, it uses information from the initial request (e.g., target gene "EGFR" and species "human") to autofill relevant fields and generate sgRNA designs without needing repeated inputs from the user. Simultaneously, CRISPR-GPT elucidates the rationale behind its choices, allowing users to track the process and make corrections if necessary.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Q&A Mode", "weight": 1.0} -->

During the design tasks in "Meta Mode" and "Auto Mode," the CRISPR-GPT agent offers immediate responses or advice for CRISPR and gene editing related inquiries through "Q&A Mode." For example, after selecting a CRISPR system, users seeking more information about the chosen system (e.g., ) can quickly obtain answers by asking, "Q: What is ?". The CRISPR-GPT uses its knowledge base and document retrieval from expert-selected databases in the field to provide accurate and relevant information swiftly.

<!-- chunk {"id": "body-0064", "role": "body", "section": "CRISPR-GPT outperforms general LLMs in gene-editing design tasks through human expert evaluations", "weight": 1.0} -->

To evaluate the performance of CRISPR-GPT agent, we invited 12 researchers with expertise in CRISPR and gene editing to design sets of tasks to test the ability of CRISPR-GPT in assisting researchers with experimental design. The results are evaluated in four different aspects: Accuracy, Reasoning, Completeness and Conciseness (Appendix C). Accuracy reflects whether CRISPR-GPT could provide accurate information of current state of CRISPR research and methodologies. Reasoning evaluates if CRISPR-GPT could provide insightful, well-supported explanation of the suggested designs. Completeness makes sure users receive all required information needed for CRISPR experimental design. Lastly, conciseness ensures that CRISPR-GPT provides users with directly relevant information for the design tasks with minimal unnecessary information. All evaluators were asked to score sets of tasks with these four aspects from 1 (Poor) to 5 (Excellent) for all three modes. Responses from ChatGPT 3.5 and ChatGPT 4.0 were generated and scored alongside those of CRISPR-GPT, using equivalent prompts in all cases.

<!-- chunk {"id": "body-0065", "role": "body", "section": "CRISPR-GPT outperforms general LLMs in gene-editing design tasks through human expert evaluations", "weight": 1.0} -->

We observed that CRISPR-GPT achieved significantly higher accuracy in our designed sets of tasks over general LLM-agents across all three modes, as we employed vast domain knowledge in the CRISPR and gene editing field to ensure the robustness of the CRISPR-GPT agent. While, responses generated by general LLM agents including ChatGPT 3.5 and ChatGPT 4.0 contain more minor factual errors due to known issues including inadequate domain knowledge and hallucination. At the same time, we found both CRISPR-GPT and general LLM agents show good reasoning ability over different sets of tasks. For "Auto Mode" related tasks, CRISPR-GPT showed even better reasoning, potentially due to better prompting techniques encoded in the agent. As we expected, "Completeness" is the major issue for general LLM-agents to perform gene-editing experimental design tasks. They can usually provide general guides for designs while could not provide design details due to the lack of domain knowledge and external tools. On the opposite side, CRISPR-GPT showed much better "Completeness" performance scores in the design tasks, allowing the users to perform the gene-editing experiment solely based on the information provided by CRISPR-GPT.

<!-- chunk {"id": "body-0066", "role": "body", "section": "CRISPR-GPT outperforms general LLMs in gene-editing design tasks through human expert evaluations", "weight": 1.0} -->

It's worth noting that both ChatGPT 3.5 and 4.0 outperform CRISPR-GPT in the "Completeness" performance score in "Q&A" mode. Such a result is due to the intentional tradeoff between "Completeness" and "Conciseness". Answers directly generated by general LLM-agents usually include much irrelevant information in order to provide users with a more complete response. This usually confuses the users and makes it hard to catch the key information. In this case, we intentionally designed the CRISPR-GPT to provide concise accurate answers to the users across all different modes and accordingly CRISPR-GPT showed consistent better "Conciseness" performance scores.

<!-- chunk {"id": "body-0067", "role": "body", "section": "CRISPR-GPT outperforms general LLMs in gene-editing design tasks through human expert evaluations", "weight": 1.0} -->

Overall, through experts' evaluation, we found CRISPR-GPT showed significantly improved performance over general LLM-agents for gene-editing experimental design tasks in all different aspects. Notwithstanding, CRISPR-GPT experienced difficulties in more complex gene editing scenarios and rare biological cases. It can be further extended and improved in the future with more up-to-date domain knowledge and better external tool sets.

<!-- chunk {"id": "body-0068", "role": "body", "section": "CRISPR-GPT demonstrates its efficacy through real-world application", "weight": 1.0} -->

To demonstrate CRISPR-GPT in assisting researchers with designing gene-editing experiments, we performed a gene knockout experiment in the human A375 cell line through continuous interaction with CRISPR-GPT.

<!-- chunk {"id": "body-0069", "role": "body", "section": "CRISPR-GPT demonstrates its efficacy through real-world application", "weight": 1.0} -->

In this experiment, we aimed to knock out a panel of 4 genes (TGFBR1, SNAI1, BAX, BCL2L1) individually in the human A375 cell line. To start, we selected the "Meta mode" to design the gene knockout experiment from scratch. Following the instruction of selecting the CRISPR system in the CRISPR-GPT, we selected as we hope to perform multiple-site edits and lower the potential off-target editing rate. For the delivery of the CRISPR system in A375 cells, we followed CRISPR-GPT's recommendation to use lentiviral transduction, ensuring stable expression of both the Cas enzyme and sgRNAs.

<!-- chunk {"id": "body-0070", "role": "body", "section": "CRISPR-GPT demonstrates its efficacy through real-world application", "weight": 1.0} -->

Then, based on this information, we were able to obtain the plasmid (previously owned). When it came to designing the sgRNAs, we specifically targeted the human TGFBR1/SNAI1/BAX/BCL2L1 genes, fully aware of the ethical ramifications of human gene editing raised by CRISPR-GPT. CRISPR-GPT provided 4 sgRNA sequences for each gene from a published library so we were able to order the sequences for synthesis.

<!-- chunk {"id": "body-0071", "role": "body", "section": "CRISPR-GPT demonstrates its efficacy through real-world application", "weight": 1.0} -->

Later, CRISPR-GPT offered protocols for gRNA cloning. Detailed instructions were then provided for producing lentivirus through calcium phosphate transfection in HEK293T cells, using the necessary plasmids and viral packaging components. Following this, we exactly followed the protocol generated by CRISPR-GPT, through the transduction process, which involved cell culture procedures, the addition of lentivirus, and the use of polybrene to facilitate efficient transduction. To perform validation, we chose next-generation sequencing (NGS) for mutation detection and validation of the knockout in CRISPR-GPT, guided by the protocol provided by CRISPR-GPT agent. To prepare for NGS, we extracted genomic DNA from cells using the DNeasy Blood & Tissue Kit based on the protocols. For the crucial step of PCR primer design, we provided detailed sequence information to CRISPR-GPT, which automatically returned a set of primers designed with Primer3 to specifically amplify the target site.

<!-- chunk {"id": "body-0072", "role": "body", "section": "CRISPR-GPT demonstrates its efficacy through real-world application", "weight": 1.0} -->

In the concluding stages of our experiment, CRISPR-GPT advised us to attach Illumina adaptors to the PCR products for library construction and emphasized the necessity of checking primer specificity with NCBI BLAST. This final validation step was crucial to prevent mis-priming and to ensure that the sequencing results would accurately reflect the intended genomic edits.

<!-- chunk {"id": "body-0073", "role": "body", "section": "CRISPR-GPT demonstrates its efficacy through real-world application", "weight": 1.0} -->

Finally, we analyzed the data from the NGS, and observed a consistent high rate of expected editing outcomes across all 4 targeted genes. Through this process, where CRISPR-GPT provided: CRISPR system selection guideRNA design delivery system recommendation plasmid and viral vector selection with cloning protocol tissue culture, cell transduction procedures cell harvesting and gene-editing efficiency quantification methods sequencing primer design and readout validation protocol. Thus, the dynamic interaction between our expertise and CRISPR-GPT's computational guidance was instrumental in executing a precise and ethically considerate gene-editing experiment.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Safety and Ethical Concerns", "weight": 1.0} -->

Safety and ethical concerns arise when using AI tools to guide genome editing, ranging from the risk of illegally altering human genomes to privacy issues when user genome information is involved.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Mitigation of the risk of human heritable editing", "weight": 1.0} -->

Technologies such as CRISPR-Cas9, have made it possible to alter human genomes, which pose a number of ethical and safety risks. In particular, germline cell and embryo genome editing bring up a number of ethical challenges, including whether it would be permissible to use this technology to enhance normal human traits (such as height or intelligence). Based on concerns about ethics and safety, germline cell and embryo genome editing are currently illegal in the United States and many other countries. To ensure CRISPR-GPT follows the guidelines given in a moratorium on heritable genome editing.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Mitigation of the risk of human heritable editing", "weight": 1.0} -->

CRISPR-GPT employs a mechanism to make sure in all tasks users cannot bypass the existing step asking which organism they are editing. The agent would check if the editing target belonged to human tissues or organs. If it is found that the editing target is a human organ, it will trigger the following solution: Warning note when users proceed with designing human gene-editing exp. Link to this international moratorium with note. Ask users to confirm they understand the risk and have read this international guideline before proceeding.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Protection of user genome data privacy", "weight": 1.0} -->

Other concerns are related to user data privacy issues, especially when human genome sequence information might be exchanged by using AI tools. We follow the data privacy and HIPAA privacy rule in healthcare. Although genome-scale sequences are fundamentally linked to identities, DNA segments of up to 20 bp length are considered safe and not able to identify human identity (REF). CPISPR-GPT is equipped with the following functionalities, to avoid supplying any identifiable private human/patient sequence to a public LLM model.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Protection of user genome data privacy", "weight": 1.0} -->

CRISPR-GPT would never store any identifiable long genome sequence in the server that would potentially reveal patient private information.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Protection of user genome data privacy", "weight": 1.0} -->

CRISPR-GPT implements a filter to detect if there is any $\geq$ 20bp of A/T/G/C/U sequence contained in the prompts before sending them to external LLMs. After detecting the existence of such a sequence, the agent would raise an error with a warning note, asking the user to manually delete such sequences in the input. In this way, it avoids leaking such sensitive information to the public LLM model.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Discussion", "weight": 1.5} -->

The CRISPR-GPT agent showcases the remarkable potential of LLMs in automating and enhancing the design process of complex biological experiments. By seamlessly integrating LLMs with domain knowledge, external tools, and a modular task execution system, CRISPR-GPT empowers researchers to navigate the intricate landscape of CRISPR gene editing experiments with unprecedented ease and efficiency. The multi-modal capabilities of CRISPR-GPT encompass meta-task pipelines, interactive prompts, and on-demand Q&A support. Researchers can leverage the agent's expertise to plan and execute gene editing experiments, from CRISPR system selection and guide RNA design to automated drafting of detailed protocol and validation strategies. This streamlined workflow not only accelerates the design process but also mitigates the risk of errors and oversights, thereby enhancing the quality and reproducibility of research outcomes.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Discussion", "weight": 1.5} -->

While there exist LLM agent in other scientific domains such as chemistry, the complexities of biological experiments involving living materials demand a distinct set of considerations. Unlike chemical reactions, which often follow well-defined protocols, biological experiments require intricate procedures that account for the dynamic nature of living systems. CRISPR-GPT addresses this challenge by providing detailed, step-by-step guidance tailored to the specific experimental context, ensuring that researchers can navigate the nuances of working with living cells and organisms effectively.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Discussion", "weight": 1.5} -->

Moreover, the free-style prompting and ad hoc Q&A capabilities of CRISPR-GPT set it apart from many existing agents. Researchers can pose unstructured queries and receive contextualized responses, facilitating a more natural and intuitive interaction with the agent. This feature is valuable in the face of unexpected challenges or unforeseen circumstances that may arise during the course of an experiment, enabling researchers to seek timely guidance and adapt their approach as needed.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Discussion", "weight": 1.5} -->

Despite its impressive capabilities, CRISPR-GPT is not without limitations. While the agent can design individual components, such as guide RNAs and primers, it currently lacks the ability to generate complete constructs or vectors from natural language input. This limitation highlights an area for future development. For example, recent advancements in the field of modular design of gene-editing, such as FragMID could be integrated with CRISPR-GPT to realize the potential for LLMs to empower researchers to explore and optimize CRISPR design and customized strategies, leading to more efficient gene-editing.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Discussion", "weight": 1.5} -->

Looking ahead, the integration of CRISPR-GPT with automated laboratory platforms and robotics holds immense promise. By bridging computational design and physical execution, researchers could leverage the agent's expertise to orchestrate end-to-end automated experiments, minimizing manual intervention and accelerating the pace of discovery.
