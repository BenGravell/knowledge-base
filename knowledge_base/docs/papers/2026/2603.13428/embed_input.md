<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

EvoClaw: Evaluating AI Agents on Continuous Software Evolution

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

With AI agents increasingly deployed as long-running systems, it becomes essential to autonomously construct and continuously evolve customized software to enable interaction within dynamic environments. Yet, existing benchmarks evaluate agents on isolated, one-off coding tasks, neglecting the temporal dependencies and technical debt inherent in real-world software evolution. To bridge this gap, we introduce DeepCommit, an agentic pipeline that reconstructs verifiable Milestone DAGs from noisy commit logs, where milestones are defined as semantically cohesive development goals. These executable sequences enable EvoClaw, a novel benchmark that requires agents to sustain system integrity and limit error accumulation, dimensions of long-term software evolution largely missing from current benchmarks. Our evaluation of 12 frontier models across 4 agent frameworks reveals a critical vulnerability: overall performance scores drop significantly from >80% on isolated tasks to at most 38% in continuous settings, exposing agents' profound struggle with long-term maintenance and error propagation.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Frontier LLM-powered agents (e.g., Claude Code, Codex ) are increasingly deployed as long-running systems (e.g., OpenClaw and Hermes ) into complex, open-ended environments. To operate effectively in these dynamic settings, such agents must treat their environment-facing interfaces as a maintainable software system---one that requires autonomous development and continuous refinement rather than a fixed, hand-crafted tool. As the agent iteratively adapts to successive requirements from end-users and ongoing environmental feedback, its continuous development efforts accumulate, naturally forming a complete repository evolution history.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Yet, evaluation for such long-running agent systems remains largely under-explored. While benchmarks for agents on coding tasks have advanced from isolated function completion to full-scale codebase generation (Table 1), they predominantly treat development as independent tasks. A critical dimension remains unaddressed: the temporal structure of software evolution. A true repository evolution benchmark must capture the full evolution itinerary---a continuous stream of dependent tasks where early implementation decisions constrain subsequent ones. Ignoring these dependencies allows agents to take expedient shortcuts that satisfy immediate tests but silently accumulate technical debt, undermining the long-term maintainability of the codebase, a failure mode that remains invisible to current isolated evaluations.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To capture these long-term dynamics, our benchmark replays the dependency-rich evolution of high-quality open-source repositories as a high-fidelity proxy for the continuous repository evolution that software as a skill demands. However, determining the appropriate task granularity is non-trivial (Figure˜1). Intuitively, one might attempt to measure evolution at the release-level. However, this granularity is too coarse: release snapshots collapse the hundreds of interdependent commits between versions into a single update, flattening the fine-grained dependency structure that drives evolutionary changes. In contrast, the commit-level history is too fine-grained and imbalanced: many commits are trivial (e.g., typo fixes) while a few are substantive, and the linear commit sequence encodes only chronological apply order, introducing spurious dependencies between unrelated changes.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this, we propose modeling software evolution at the Milestone-level. We define a milestone as a coherent functional unit that preserves dependency constraints. This granularity strikes a crucial balance: unlike releases, it retains the fine-grained development dependencies and structural evolution of the codebase; unlike commits, it encapsulates realistic and coherent functional goals. Functional dependencies among milestones naturally form a Directed Acyclic Graph (DAG), which captures genuine prerequisite constraints while allowing independent features to proceed in parallel. However, constructing Milestone DAGs requires reordering and grouping commits, which disrupts the native git history. This poses a severe challenge to correctness: applying reordered patches often breaks compilation and test collection, jeopardizing the benchmark's executability and realism.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To resolve this, we introduce DeepCommit, an automated agentic pipeline that reconstructs verifiable software evolution itineraries in the form of Milestone DAGs. By synergizing static analysis, LLM-agent-driven milestone construction, and runtime validation, DeepCommit ensures the synthesized milestones are executable and testable. Powered by Claude Opus 4.5, it achieves a high average test collection success rate of 87.1%, ensuring comprehensive verification coverage. Designed as a scalable agentic framework, DeepCommit is poised to leverage future LLM advancements to harvest increasingly accurate and extensive evolution itineraries from the vast open-source ecosystem.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Building on this foundation, we present EvoClaw, a benchmark for evaluating LLM agents under continuous software evolution. EvoClaw comprises 98 human-verified milestones across 7 evolution itineraries (Milestone DAGs), each from a release range of a unique high-impact open-source repository, and spanning five programming languages. Rather than solving independent tasks, agents in EvoClaw are tasked with evolving a codebase through streams of these dependency-constrained milestones, closely mirroring real-world development scenarios. A single full evaluation costs approximately \$500 with frontier models such as Claude Opus 4.5. To achieve a high score in this setting, an agent must maintain long-term context, manage architectural consistency, and prevent error accumulation across extended development horizons.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Using EvoClaw, we conduct a comprehensive evaluation of 4 frontier agent frameworks and 12 state-of-the-art LLMs. We assess performance using a unified Score (Section 5.1), which balances Recall (completeness of new feature implementation) and Precision (robustness against regressions), along with a strict Resolve Rate for fully completed milestones.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A fundamental performance gap: Continuous vs. Independent. (Section 5.2) Frontier models exhibit a substantial degradation from independent to continuous task evaluation. Scores drop from over $\sim$`<!-- -->`{=html}80% on isolated tasks to at most 38.03% (Claude Opus 4.6) in continuous environments, with a mere 13.37% Resolve Rate (Gemini 3 Pro).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recall grows linearly but Precision saturates. We identify a fundamental asymmetry in continuous software evolution (Section 5.4): while frontier agents retain the capability to implement new features (linear Recall growth), they fail to prevent regressions as the system evolves (saturated Precision). This indicates that agents struggle primarily with system-level maintenance rather than local implementation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Accumulated errors stall downstream progress. Unresolved regressions trigger a "snowball effect" where errors accumulate faster than agents can fix them (Section 5.5). Early bugs propagate through dependency chains to contaminate downstream tasks, eventually stalling development entirely.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Proactive exploration and verification mitigate technical debt. Behavioral analysis shows that successful sustained evolution relies on proactive codebase exploration and disciplined test verification, whereas both blind trial-and-error and the absence of verification accelerate failure (Section 5.6).

<!-- chunk {"id": "body-0014", "role": "body", "section": "From Raw Commits to Milestone DAGs", "weight": 1.0} -->

Software repositories encode rich evolutionary trajectories, yet raw commit histories remain noisy, fragmented, and inadequate as executable development sequences. Commits vary widely in granularity, semantic clarity, and dependency structure, while parallel branches, squash merges, and non-functional changes obscure true developmental relationships. Relying on documentation or release notes alone lacks sufficient resolution to reconstruct precise code evolution. DeepCommit addresses this challenge by transforming linear git histories into structured, verifiable Milestone DAGs, where each node represents a coherent, testable unit of development and edges encode dependency constraints across evolution phases.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Overall Agent-Driven Pipeline", "weight": 1.0} -->

As illustrated in Figure˜2, DeepCommit reconstructs software evolution itineraries through an end-to-end pipeline that sequentially integrates: commit history preprocessing, Milestone DAG construction, and executable environment resolution.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Commit History Preprocessing", "weight": 1.0} -->

We model each repository's main-branch range between release tags as a linear sequence of commits. This linearization aligns naturally with the squash-and-merge workflow, the most widely adopted convention in actively-maintained, high-quality repositories, where each main-branch commit maps to a Pull Request (PR) or Issue together with its internal sub-commits. We collect all main-branch commits and their PR, Issue, and Release metadata. An LLM agent then prepares a per-repo configuration of source directories, test patterns, and exclusion rules that separates product-logic source from test code and filters out commits touching only non-source files such as docs, CI configs, and build assets (Appendix A.1). To enable downstream milestone discovery and dependency inference, we extract three structural signals via static analysis: (i) a commit-level DAG built with git blame to capture line-level textual dependencies, (ii) symbol-level modifications identifying changes in classes and functions, and (iii) file-level co-change statistics reflecting evolutionary coupling.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Milestone DAG Construction", "weight": 1.0} -->

Organizing hundreds of discrete commits into functionally coherent milestones requires integrating structural dependencies with code-level reasoning. We employ a four-stage LLM-agent-driven process to progressively construct the Milestone DAG. Each stage is orchestrated with automated data preparation, agent-accessible validation tools, and a post-stage quality gate. A stage runs in a forward pass and may iterate internally against its self-checks. At stage boundaries, the pipeline can also fan out into multiple parallel instantiations of the next stage and retain the variant that best satisfies the downstream quality gate.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Milestone DAG Construction", "weight": 1.0} -->

Seed Discovery. Each milestone is initiated by a seed commit, namely a foundational anchor that introduces a distinct development theme. An LLM agent identifies such seeds by jointly evaluating commit semantics (commit messages and linked discussion context) and structural signals (DAG topology, including out-degree and descendant count), filtering out cosmetic edits, hotfixes, and follow-up patches that lack downstream structural influence.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Milestone DAG Construction", "weight": 1.0} -->

Milestone Consolidation. For each seed, parallel sub-agents expand the milestone boundary using shared file modifications, temporal proximity, and PR/Issue references, growing each seed into a milestone that bundles all commits realizing its development theme. Since the sub-agents operate independently, the same commit may be claimed by several milestones. A coordinating agent then resolves these overlapping claims so that each commit belongs to exactly one milestone, enforces complete coverage of the range, and certifies acyclicity.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Milestone DAG Construction", "weight": 1.0} -->

Dependency Inference. The majority of inter-milestone edges follow directly from the line-level textual dependencies extracted during preprocessing. More subtle dependencies, such as call relationships that share no common hunk, are proposed and validated by an LLM agent using symbol-level analysis and file co-change patterns. Even so, certain dependencies surface only when milestones are built and executed. These residual edges are recovered later during runtime environment resolution (Section˜3.2.3).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Milestone DAG Construction", "weight": 1.0} -->

Milestone Decompose. Oversized milestones are decomposed into functionally independent sub-milestones while underspecified ones are merged into adjacent neighbors, with dependencies synchronously updated to preserve a valid DAG. When an oversized milestone is dominated by a single squashed PR-commit, the agent further re-segments the commit's diff along feature boundaries and remaps the affected dependency edges via line-level blame, promoting the resulting sub-units to first-class milestones. The pipeline targets a coefficient of variation ${CV} < 1.0$ over per-milestone LoC, achieving ${CV} = 0.96$ on EvoClaw (Appendix A.2).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Runtime Environment Resolution", "weight": 1.0} -->

To transform the Milestone DAG into an executable evaluation environment, a MainAgent orchestrates a multi-agent workflow that produces, for every milestone, a reproducible Docker image that yields stable test signals. From a whole-evolution perspective, the MainAgent balances testbed quality against the cost of automated resolution. To achieve high quality at reasonable cost, the pipeline additionally relies on human-expert guidance to steer the MainAgent at key decision points. The MainAgent then dispatches sub-agents for batch analysis and problem localization, routing the surfaced issues to two specialized repair modules that iterate together until every milestone reaches a stable, fully collected state.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Runtime Environment Resolution", "weight": 1.0} -->

Milestone DAG Optimization and Testbed Preparation. A MilestoneAgent reconstructs each milestone's code state by cherry-picking its commits in topological order onto the codebase at the base release tag. When a cherry-pick conflict arises, the agent repairs the DAG, primarily by adding the missing cross-milestone dependency edge and, when necessary, relocating misattributed commits to the correct milestone. Commits that still cannot be applied are marked as deferred, so that every milestone is reconstructed into a complete, DAG-consistent state.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Runtime Environment Resolution", "weight": 1.0} -->

Environment Configuration and Test Collection. For each milestone, an EnvAgent generates a Dockerfile from the repository's CI/CD workflows and enforces three hard gates: the source compiles, the test framework collects successfully, and as many tests referenced by the milestone's patch as possible are captured in the collected set. A characteristic failure mode arises when the configured test environment runs ahead of the cherry-picked source state, so that functional modules referenced by the collected tests do not yet exist. These cases cannot be fixed locally and are deferred to the DAG optimization module for refinement (Appendix A.3).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Automated Quality Assurance", "weight": 1.0} -->

To ensure the reliability and reproducibility of our evaluation, we rigorously validate each milestone testbed and report the aggregate evidence across three core dimensions, complementing the per-milestone gates enforced in Section˜3.2.3:

<!-- chunk {"id": "body-0026", "role": "body", "section": "Automated Quality Assurance", "weight": 1.0} -->

Milestone Graph Validity. We verify the structural integrity of the reconstructed history. This includes confirming commit completeness (100% coverage of the target range), dependency consistency (ensuring milestone dependencies respect underlying commit dependencies), and DAG correctness (validating acyclicity).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Automated Quality Assurance", "weight": 1.0} -->

Runtime Executability. We ensure that errors stem from agent code, not infrastructure. We verify testbed compilability by ensuring successful build and test collection in both states. We also strictly monitor execution logs to ensure environment-induced errors remain negligible ($\leq$`<!-- -->`{=html}0.10%).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Automated Quality Assurance", "weight": 1.0} -->

Evaluation Reliability. We assess the stability of the test suites. We achieve a high test collection rate (87.1%). We ensure test consistency by validating a negligible Pass-to-Fail rate ($\leq$`<!-- -->`{=html}0.026%) and filtering flaky tests through three repeated runs. Finally, we require each retained milestone to expose at least one F2P or N2P test signal (details in Appendix A.4).

<!-- chunk {"id": "body-0029", "role": "body", "section": "EvoClaw: Benchmarking Continuous Software Evolution", "weight": 1.0} -->

EvoClaw introduces a novel evaluation paradigm designed to assess an agent's ability to evolve and maintain a software codebase over an extended lifecycle. As shown in Figure˜3, unlike traditional benchmarks that focus on resolving independent issues, EvoClaw simulates a realistic, continuous development process where requirements arrive as a stream, and tasks have strict sequential dependencies.

<!-- chunk {"id": "body-0030", "role": "body", "section": "The Continuous Task Evaluation Framework", "weight": 1.0} -->

The framework orchestrates a continuous development pipeline: an external planner dynamically unlocks tasks based on a dependency graph, the agent implements them in a persistent codebase, and the framework asynchronously evaluates snapshots upon submission. This design explicitly decouples roadmap planning from implementation, allowing us to assess the agent's ability to maintain and evolve software within a structured workflow.

<!-- chunk {"id": "body-0031", "role": "body", "section": "The Continuous Task Evaluation Framework", "weight": 1.0} -->

Dependency-Driven Task Stream. Requirements are not presented in a static batch but are unlocked dynamically. The system maintains a DAG-based task scheduler where a new milestone $M_{i}$ becomes available to the agent if and only if all its prerequisite milestones $\{ M_{j} \mid M_{i}{depends}{on}M_{j}\}$ have been completed. This simulates real-world constraints in which foundational features must be established before dependent features are implemented.

<!-- chunk {"id": "body-0032", "role": "body", "section": "The Continuous Task Evaluation Framework", "weight": 1.0} -->

Continuous Evolution Environment. The agent operates within a persistent, stateful environment where modifications from each task persist into the next. This compels the agent to maintain the long-term health of the codebase, as early technical debt or latent bugs can accumulate and impede future progress.

<!-- chunk {"id": "body-0033", "role": "body", "section": "The Continuous Task Evaluation Framework", "weight": 1.0} -->

Snapshot-Based Isolated Evaluation. To reconcile the need for a continuous development flow with rigorous verification, we employ a "develop-in-place, evaluate-in-isolation" strategy. Upon task completion, the agent's implementation state is snapshotted and transferred to an isolated evaluation container to run the test suite. This ensures that the scoring process is reproducible and unaffected by the agent's ongoing development, while the agent's working environment remains uninterrupted.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Benchmark Construction", "weight": 1.0} -->

We construct a high-quality dataset through a rigorous pipeline that transforms open-source repositories into verified evolutionary suites.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Benchmark Construction", "weight": 1.0} -->

Repository and Range Selection. We identify projects with high community impact and diverse programming languages. We specifically select release ranges that exhibit rich dependency structures, ensuring the benchmark captures complex, non-linear development scenarios rather than trivial sequences.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Benchmark Construction", "weight": 1.0} -->

Itinerary Extraction via DeepCommit. Leveraging the DeepCommit pipeline (Section 3), we mine the evolutionary history of selected projects. To guarantee the benchmark's quality and evaluation efficiency, we apply strict post-processing filters to the generated milestones. We retain only milestones that: represent core functional changes (filtering out pure documentation updates); possess executable F2P tests to serve as definitive success criteria; and fall within a manageable context window to maintain task solvability. This step ensures that every task in the benchmark is grounded in a verified, executable state transition.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Benchmark Construction", "weight": 1.0} -->

Reverse-Engineering Software Requirement Specifications (SRS). Relying solely on original GitHub issues or PR descriptions is often insufficient, as they can be underspecified, outdated, or disconnected from the final code implementation. To bridge this gap, we employ an agent-driven reverse-engineering approach to synthesize high-fidelity Software Requirement Specifications (SRS). We first dispatch an LLM agent to analyze the ground-truth patches to draft precise functional requirements. This draft then undergoes a refinement phase to align acceptance criteria strictly with the verified Fail-to-Pass tests. Finally, environment-specific instructions (e.g., dependency updates) are appended by analyzing build configuration changes, ensuring a complete execution context.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Benchmark Construction", "weight": 1.0} -->

Human-in-the-Loop Verification. Automated generation can yield logical inconsistencies and misalignment with edge cases. To mitigate this, expert annotators conduct a final review focused on task solvability. Annotators verify that the SRS provides all necessary information to solve the problem without leaking implementation details and that the acceptance criteria are unambiguous. Simultaneously, we validate the stability of the test suites to rule out flaky tests. This hybrid verification ensures that EvoClaw provides a fair assessment, distinguishing genuine agent errors from artifacts of ambiguous specifications (Appendix B.1).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Benchmark Construction", "weight": 1.0} -->

(a) Distribution of milestones across the 7 repositories in EvoClaw. Each bar represents the number of verified milestones extracted from the corresponding open-source project.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Benchmark Construction", "weight": 1.0} -->

(b) Distribution of SRS word counts (left) and gold patch LOC (right), stratified by estimated human effort.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Benchmark Statistics", "weight": 1.0} -->

EvoClaw comprises 98 verified milestones across 7 diverse open-source repositories, spanning five programming languages (Go, Rust, Java, TypeScript, Python) with a total of 109 inter-milestone dependencies. As shown in Figure˜4(a), the milestones are distributed across repositories with varying complexity, ranging from 9 to 23 milestones per repository. The dataset captures diverse real-world development patterns, including major architectural changes (e.g., multi-library support), feature-rich iterations (e.g., cloud-native enhancements), stability-focused releases (e.g., compatibility fixes), and large-scale refactoring (e.g., type system overhauls). This ensures EvoClaw evaluates agents across the full spectrum of software engineering tasks.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Benchmark Statistics", "weight": 1.0} -->

Figure˜4(b) illustrates the distribution of task complexity. The dataset exhibits substantial diversity in both specification length (SRS mean: 1,348 words) and implementation scope (gold patch LOC ranging from $< 100$ to $> {1,500}$). On average, each milestone modifies 27.4 files and involves 17.1 Fail-to-Pass tests for verification alongside 6,218 Pass-to-Pass tests for regression prevention. Detailed per-repository statistics are provided in Appendix B.3, and the full Milestone DAG visualizations for all repositories are shown in Appendix B.4.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Evaluation Settings", "weight": 1.0} -->

To isolate how error accumulation across milestones affects agent performance, we evaluate methods under two different settings based on the Milestone DAG: Continuous Task Evaluation, the standard EvoClaw setting where agents continuously evolve a codebase under streaming requirements. This setting introduces real-world challenges such as error accumulation and technical debt management. Independent Task Evaluation, a stateless baseline (similar to SWE-bench ) in which each milestone is treated as an isolated task by providing agents with the canonical codebase snapshot, thereby decoupling performance from the cumulative effects of prior modifications.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

Evaluating agents in a continuous evolution setting requires metrics that capture two competing objectives: implementing new functionality and preserving existing behavior. Traditional benchmarks such as SWE-bench rely on binary success criteria (all tests pass or fail), which are too coarse-grained to capture the nuance of incremental progress and regression. Simple pass-rate metrics conflate these two objectives, failing to distinguish an agent that implements features but introduces regressions from one that avoids regressions but makes no progress.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

Recall measures feature implementation completeness: the proportion of required functional changes successfully implemented by the agent.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

where $N_{\text{required},m}$ denotes the total number of Fail-to-Pass (F2P) tests for milestone $m$ (tests that transition from failing at the start state to passing after the milestone's gold patch is applied), and $N_{\text{fixed},m}$ is the count of such tests that the agent successfully fixes.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

Precision measures modification reliability: the proportion of test status changes that are improvements rather than regressions, quantifying the safety of the agent's edits.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

where $N_{\text{broken},m}$ is the number of Pass-to-Pass (P2P) tests (tests that pass at the start state and must remain passing after the agent's changes) that regress (fail or error out) due to the agent's changes. The term $\epsilon = 1$ is a smoothing factor to handle cases where the agent makes no impact (i.e., when both fixed and broken counts are zero).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

The final reported metric is the average Score across all milestones: $\text{Score} = {\frac{1}{|M|}{\sum_{m \in M}\text{Score}_{m}}}$. This ensures that neither dimension can be neglected: an agent that implements all features but introduces severe regressions will score as poorly as one that preserves existing functionality but fails to implement any changes.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

Consistent with prior work like SWE-bench, we also report the Milestone Resolve Rate, where a milestone is considered resolved only if the agent passes all associated F2P and P2P tests. We report the average resolve rate across all repositories. While Score quantifies partial progress, Resolve Rate assesses whether the task was fully resolved.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Evaluated Models and Agents", "weight": 1.0} -->

We evaluate a diverse set of frontier LLMs across four agent frameworks. Specifically, we test Claude Code with Claude Opus 4.5, Claude Sonnet 4.5, Claude Opus 4.6, and Claude Sonnet 4.6, Codex CLI with GPT 5.2, GPT 5.2-Codex, and GPT 5.3-Codex (all set to xhigh reasoning effort), Gemini CLI with Gemini 3 Pro, Gemini 3.1 Pro, and Gemini 3 Flash (all by default with 1M context), and OpenHands with Claude Opus 4.6, GPT 5.3-Codex, Gemini 3 Flash, Kimi K2.5, and MiniMax M2.5. Detailed framework versions, context management configurations, and the unified agent system prompt (Figure 18) are provided in Section˜B.2.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Overall Performance", "weight": 1.0} -->

Table 2 presents results across 15 agent-model configurations. Claude Opus 4.6 achieves the highest Score (38.03% in Openhands and 36.29% in Claude Code), followed by Claude Sonnet 4.6 (29.58%) and GPT 5.3-Codex (28.88%). Across all models, the gap between Score ($\sim$`<!-- -->`{=html}38% at best) and Resolve Rate ($\sim$`<!-- -->`{=html}13%) is substantial: agents achieve partial progress on most milestones but rarely complete them fully. Moreover, the resolved milestones are predominantly early ones with few upstream dependencies, confirming that accumulated upstream errors increasingly hinder downstream task completion. Unless otherwise noted, subsequent analyses focus on configurations where each model is paired with its vendor-provided agent framework.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Overall Performance", "weight": 1.0} -->

Across model families, generational improvements emerge: Claude 4.6 models significantly outperform their 4.5 predecessors, and GPT 5.3-Codex substantially improves over its predecessors. However, comparing GPT 5.2 and GPT 5.2-Codex reveals that Codex-specific optimization may be counterproductive for long-horizon development, where sustained codebase maintenance demands broader analytical capabilities beyond isolated task solving. The three Gemini models achieve comparable scores, with Gemini 3 Flash matching Gemini 3 Pro at one-ninth the cost. Gemini 3 Pro uses the fewest turns, possibly indicating insufficient exploration. Figure 6 visualizes the cost-score trade-off. Higher cost does not uniformly translate into higher performance: Gemini 3 Pro exceeds \$100 per evolution range yet scores below Opus 4.6 (\$88), and Sonnet 4.6 (\$69) trails Opus 4.6 by 6.7 points despite a similar cost tier. On the Pareto frontier, Gemini 3 Flash (\$12, 24.2%) and GPT 5.3-Codex (\$25, 28.9%) offer the best cost-effectiveness, achieving competitive scores at a fraction of the cost of top-performing models.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Overall Performance", "weight": 1.0} -->

OpenHands trials exhibit notably longer execution times (e.g., 18.49 h for GPT 5.3-Codex) because its runner permits up to 3,000 iterations per milestone with automatic session resumption, allowing the agent to retry extensively when stuck. This additional compute does not consistently improve scores: Claude Code with Opus 4.6 achieves a comparable score in under 4 hours.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Overall Performance", "weight": 1.0} -->

Overall, these results highlight that EvoClaw poses a significant challenge to current frontier models, and reliable long-horizon continuous development remains an open problem.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Task Complexity and Topological Effects", "weight": 1.0} -->

Beyond these static factors, the continuous evaluation setting introduces structural complexity unique to EvoClaw. Both the milestone execution order and the DAG topological layer show statistically significant negative correlations with the score. Later milestones and deeper topological layers consistently yield lower performance. This reflects the compounding effect of upstream errors, as agents must build upon their own (potentially flawed) prior work. These topological factors are absent in independent evaluation and represent the distinctive challenge of long-horizon software evolution. The Resolve Rate (bottom row of Figure 7) makes this effect even starker: it drops drastically beyond the earliest milestones and the shallowest DAG layers, indicating that current agents can only fully resolve milestones that appear early in the sequence or have no upstream dependencies. Once prior errors accumulate, agents may still achieve partial progress (reflected in Score) but rarely produce a completely correct solution.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Evolution Dynamics: Recall Scales while Precision Saturates", "weight": 1.0} -->

The declining performance at later milestones raises a natural question: does agent capability degrade over time, or does accumulated technical debt overwhelm otherwise competent agents?

<!-- chunk {"id": "body-0058", "role": "body", "section": "Evolution Dynamics: Recall Scales while Precision Saturates", "weight": 1.0} -->

To answer this, we model cumulative score trajectories using a saturation function $y = {a{({1 - e^{- {bx}}})}}$, where a small $b$ yields near-linear growth while a large $b$ produces rapid saturation toward the ceiling $a$. As shown in Figure 8 (left), all models under exhibit clear performance ceilings, and multi-window extrapolation (fitting the saturation model to progressively larger subsets of milestones and projecting forward) confirms that these ceilings persist beyond the observed window. Comparing continuous and independent evaluation (middle, right), independent scores grow near-linearly while continuous scores saturate, with the gap widening monotonically as evolution progresses.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Evolution Dynamics: Recall Scales while Precision Saturates", "weight": 1.0} -->

We decompose the cumulative score into Recall (successful feature implementation) and Precision (preservation of existing functionality) to isolate the underlying mechanism. Figure 9 reveals a fundamental asymmetry: Recall continues to grow near-linearly across all models (especially frontier models), indicating that agents retain the ability to solve newly assigned tasks. Precision, however, saturates rapidly across all evaluated configurations. This means the performance ceiling is not caused by agents forgetting how to code, but by their inability to prevent regressions from accumulating. Stronger models achieve higher Precision plateaus, yet none avoid saturation entirely. This Recall-Precision divergence provides a mechanistic explanation for the snowball effect: as unresolved regressions compound, each new milestone operates on an increasingly degraded codebase, eventually overwhelming the agent's capacity for productive development.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Failure Analysis: Error Generation and Propagation", "weight": 1.0} -->

Understanding why agents fail in continuous evaluation is inherently difficult. A single early mistake can trigger cascading test failures across dozens of downstream milestones, making it challenging to disentangle root causes from their propagated consequences. To enable systematic analysis, we introduce the concept of error chains: for each test that transitions from passing to failing during the evolution, we trace its status across all subsequent milestones until it is either healed or the trial ends. This yields a per-test timeline that captures the full lifecycle of an error. We focus this analysis on the strongest configuration, Claude Opus 4.6, to characterize failure mechanisms at the frontier of current agent capabilities.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Failure Analysis: Error Generation and Propagation", "weight": 1.0} -->

We decompose error chains along two orthogonal dimensions. The first, Propagation Type, captures how a fault affects downstream milestones. This is determined statistically from evaluation results: we track each test's status across the milestone timeline and classify events as P0 Root Cause (the originating failure), P0 Induced (cross-chain contamination from unrelated changes), P1 Inherited (propagated through dependency), PX Missing (skipped execution), or PH Healed (successfully recovered). Figure 10 (right) shows that propagation events (P1, PX) increasingly dominate in later stages, confirming the compounding degradation observed in Section 5.3. The left panel visualizes representative error chain patterns across repositories, illustrating how a single root cause event can cascade through the entire remaining evolution.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Failure Analysis: Error Generation and Propagation", "weight": 1.0} -->

The second dimension, Root Cause Type, captures why the initial fault originates. Since root cause attribution requires understanding the agent's intent, we employ Claude Sonnet 4.6 as a reviewer agent that compares the task agent's code changes against the ground-truth patch, the SRS specification, and evaluation artifacts. The reviewer classifies each error chain's root cause into three categories: Logic Error (correct target, buggy implementation), Omission (missing a required component), or Extraneous (unnecessary modifications that break existing functionality). Figure 11 presents the joint distribution of Root Cause Type $\times$ Propagation Type. Logic Error is the dominant root cause ($\sim$`<!-- -->`{=html}57% of all error chain events), with its chains exhibiting both the highest inherited propagation (P1, 12%) and the highest proportion of missing test execution (PX Missing, 17%), indicating that buggy implementations frequently prevent downstream tests from running at all.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Agent Behavior: The Struggle Against Accumulating Complexity", "weight": 1.0} -->

Beyond aggregate scores, we examine how agents allocate effort and manage state when facing accumulating technical debt during long-horizon iterations. By instrumenting tool calls, context usage, and interaction turns, we reveal distinct behavioral patterns.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Agent Behavior: The Struggle Against Accumulating Complexity", "weight": 1.0} -->

Effort Fluctuation and Extremes. As shown in Figure 12, all evaluated agents exhibit a shared trend in their effort allocation (measured by the continuous-to-independent turns ratio). In the initial phase (progress $\sim$`<!-- -->`{=html}0.1), continuous effort is slightly higher than independent effort, as agents must conduct large-scale exploration to build a mental model of the unfamiliar repository. During the middle phase (progress 0.1--0.5), the ratio drops below $1 \times$ (with the median falling to $\sim$`<!-- -->`{=html}0.83$\times$): agents successfully reuse their established context, bypassing the redundant exploration required in independent evaluation. However, in the late stage (progress 0.6--0.9), effort rises significantly as accumulating errors demand extensive debugging. Finally, near completion (progress $\sim$`<!-- -->`{=html}1.0), agent behavior diverges sharply. Some agents resort to frantic thrashing, while others prematurely give up.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Agent Behavior: The Struggle Against Accumulating Complexity", "weight": 1.0} -->

Notably, GPT 5.3-Codex demonstrates the most stable effort profile, maintaining consistent variance throughout the project lifecycle.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Agent Behavior: The Struggle Against Accumulating Complexity", "weight": 1.0} -->

Context Stability and Exploration Patterns. To sustain this fluctuating effort, agents must effectively manage their context. Figure 13 illustrates this using Claude Code with Opus 4.6 as a representative example. The context window shows stable, controllable wave patterns, demonstrating that modern agent frameworks paired with frontier models can effectively support long-horizon programming without catastrophic context overflow. The framework employs two compression strategies: partial compression (evicting specific tool results) and heavy compaction (summarizing extensive histories). Crucially, agent exploration behavior (reading and searching) tightly couples with this state management. Exploration surges at the beginning of each new milestone and immediately following major context compaction events, as the agent works to rebuild its mental model.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Agent Behavior: The Struggle Against Accumulating Complexity", "weight": 1.0} -->

The Impact of Exploration. This exploration behavior directly dictates downstream success. Figure 14 demonstrates that within their respective agent frameworks, models from the same family exhibit a consistent pattern: higher exploration counts correlate with better performance. For instance, Claude Opus 4.6 and Claude Sonnet 4.6 hold a distinct advantage because they aggressively dispatch subagents to analyze the codebase, executing over 7,000 exploration commands. Conversely, models like Gemini 3 Pro allocate too little effort to reading, indicating that many current models still lack proactive exploration for long-horizon tasks.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Agent Behavior: The Struggle Against Accumulating Complexity", "weight": 1.0} -->

Verification vs. Blind Thrashing. Alongside exploration, we analyze verification behavior (test execution). Figure 15 shows that average verification effort generally follows an inverted-U shape, increasing as the codebase grows more complex before declining near the end. However, this masks two problematic extremes: Gemini 3.1 Pro verifies excessively, while GPT 5.2-Codex rarely verifies at all, and both achieve lower scores. Figure 16 further isolates this dynamic by mapping the score landscape against edit thrashing and verification frequency. A clear sweet spot emerges for moderate, disciplined verification. In contrast, the worst outcomes concentrate in the high-thrash and low-verify quadrant---a blind thrashing trap where agents repeatedly modify the same files without executing tests to guide them, effectively accelerating the snowball effect.

<!-- chunk {"id": "body-0069", "role": "body", "section": "DeepCommit vs Human-Annotated Milestone DAG", "weight": 1.0} -->

We conducted a case study (Appendix C.3) that compares the human-annotated and DeepCommit Milestone DAGs for the scikit-learn v1.5.2--v1.6.0 release interval. The Human DAG organizes milestones by semantic release intent, whereas DeepCommit derives groups from dependency topology in the commit graph. As a result, DeepCommit covers a smaller but tightly connected subset of commits, recovers human-like boundaries when technical structure is clear (e.g., documentation), but tends to fragment cross-module, intent-defined milestones into topological phases. Overall, this case study shows that the Human DAG captures semantically coherent and process-aware milestone structure, whereas DeepCommit more strongly reflects dependency topology and phase-wise code organization.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced DeepCommit, a pipeline that distills verifiable software evolution into coherent Milestone DAGs from noisy, fine-grained git histories, and EvoClaw, a benchmark for evaluating LLM agents under continuous, dependency-driven development. Our results reveal a fundamental gap between independent task-solving and continuous evolution: frontier models achieve over 80% on isolated milestones but drop below 38% in continuous settings. This degradation stems from a critical inability to maintain code integrity: while agents can implement new features, they fail to prevent regressions, causing a snowball effect of accumulating technical debt. Even the strongest agents resolve only $\sim$`<!-- -->`{=html}13% of milestones in full evolutionary sequences, establishing sustained, maintainable repository evolution as a central open challenge for autonomous software agents.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Limitations", "weight": 1.5} -->

EvoClaw and the DeepCommit pipeline have several limitations that bound the conclusions to be drawn and the settings to which they currently apply.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Test-Suite Dependency", "weight": 1.0} -->

Our construction relies on repositories with well-maintained, executable test suites that provide reliable F2P and P2P signals. Projects that lack rich test coverage, or whose tests depend on inaccessible external services, cannot currently be incorporated into the benchmark.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Filtering Bias", "weight": 1.0} -->

The pipeline retains only commits that touch source code with non-trivial inter-commit dependencies, dropping documentation-only commits and commits without resolvable structural ties. This filtering improves DAG quality and evaluation tractability, but it may bias the resulting benchmark toward dependency-rich evolution and underrepresent independent maintenance work.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Data Contamination Risk", "weight": 1.0} -->

The repositories used in EvoClaw are high-impact open-source projects whose commit histories may have appeared in the pretraining corpora of frontier models. The substantial performance gaps we observe among frontier models suggest contamination has limited impact on relative ranking, but we cannot fully rule out memorization on individual milestones. Continuously refreshing the benchmark with newly merged commits, or applying DeepCommit to private repositories, would mitigate this risk.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Human-in-the-Loop Reliance", "weight": 1.0} -->

Two stages of DeepCommit still require human-expert oversight: (i) the MainAgent's scheduling decisions during runtime environment resolution, where humans guide the trade-off between testbed quality and resolution cost, and (ii) the SRS verification stage, where human annotators run the three-step refinement loop described in Appendix B.1. Fully automating these stages remains an open engineering problem.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Scale Limit", "weight": 1.0} -->

The current pipeline targets release ranges whose source-code gold patch is under roughly 30k LoC. Larger ranges produce Milestone DAGs that exceed the agent's resolution budget and frequently fail the testbed-construction gates. Scaling DeepCommit to longer histories will require further improvements to both DAG construction and runtime resolution.
