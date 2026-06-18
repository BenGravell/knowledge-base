## Introduction

Frontier LLM-powered agents (e.g., Claude Code, Codex ) are increasingly deployed as long-running systems (e.g., OpenClaw and Hermes ) into complex, open-ended environments. To operate effectively in these dynamic settings, such agents must treat their environment-facing interfaces as a maintainable software system---one that requires autonomous development and continuous refinement rather than a fixed, hand-crafted tool. As the agent iteratively adapts to successive requirements from end-users and ongoing environmental feedback, its continuous development efforts accumulate, naturally forming a complete repository evolution history.

Yet, evaluation for such long-running agent systems remains largely under-explored. While benchmarks for agents on coding tasks have advanced from isolated function completion to full-scale codebase generation (Table 1), they predominantly treat development as independent tasks. A critical dimension remains unaddressed: the temporal structure of software evolution. A true repository evolution benchmark must capture the full evolution itinerary---a continuous stream of dependent tasks where early implementation decisions constrain subsequent ones. Ignoring these dependencies allows agents to take expedient shortcuts that satisfy immediate tests but silently accumulate technical debt, undermining the long-term maintainability of the codebase, a failure mode that remains invisible to current isolated evaluations.

Codebase + Oracle Test

Codebase + Dev History

Table 1: Representative software engineering benchmarks for LLMs. Unlike other categories of benchmarks that evaluate agents on isolated snapshots or against ground-truth states at each step, Repository Evolution requires agents to continuously build upon their own accumulated development history, exposing them to error propagation across tasks. EvoClaw adopts the Milestone-level granularity, a functionally coherent group of commits that collectively advance a development objective, avoiding the noise of individual commits and the excessive scope of full releases. Dev History denotes the agent’s own development trace accumulated from preceding tasks.

To capture these long-term dynamics, our benchmark replays the dependency-rich evolution of high-quality open-source repositories as a high-fidelity proxy for the continuous repository evolution that software as a skill demands. However, determining the appropriate task granularity is non-trivial (Figure˜1). Intuitively, one might attempt to measure evolution at the release-level. However, this granularity is too coarse: release snapshots collapse the hundreds of interdependent commits between versions into a single update, flattening the fine-grained dependency structure that drives evolutionary changes. In contrast, the commit-level history is too fine-grained and imbalanced: many commits are trivial (e.g., typo fixes) while a few are substantive, and the linear commit sequence encodes only chronological apply order, introducing spurious dependencies between unrelated changes.

To address this, we propose modeling software evolution at the Milestone-level. We define a milestone as a coherent functional unit that preserves dependency constraints. This granularity strikes a crucial balance: unlike releases, it retains the fine-grained development dependencies and structural evolution of the codebase; unlike commits, it encapsulates realistic and coherent functional goals. Functional dependencies among milestones naturally form a Directed Acyclic Graph (DAG), which captures genuine prerequisite constraints while allowing independent features to proceed in parallel. However, constructing Milestone DAGs requires reordering and grouping commits, which disrupts the native git history. This poses a severe challenge to correctness: applying reordered patches often breaks compilation and test collection, jeopardizing the benchmark's executability and realism.

To resolve this, we introduce DeepCommit, an automated agentic pipeline that reconstructs verifiable software evolution itineraries in the form of Milestone DAGs. By synergizing static analysis, LLM-agent-driven milestone construction, and runtime validation, DeepCommit ensures the synthesized milestones are executable and testable. Powered by Claude Opus 4.5, it achieves a high average test collection success rate of 87.1%, ensuring comprehensive verification coverage. Designed as a scalable agentic framework, DeepCommit is poised to leverage future LLM advancements to harvest increasingly accurate and extensive evolution itineraries from the vast open-source ecosystem.

Building on this foundation, we present EvoClaw, a benchmark for evaluating LLM agents under continuous software evolution. EvoClaw comprises 98 human-verified milestones across 7 evolution itineraries (Milestone DAGs), each from a release range of a unique high-impact open-source repository, and spanning five programming languages. Rather than solving independent tasks, agents in EvoClaw are tasked with evolving a codebase through streams of these dependency-constrained milestones, closely mirroring real-world development scenarios. A single full evaluation costs approximately \$500 with frontier models such as Claude Opus 4.5. To achieve a high score in this setting, an agent must maintain long-term context, manage architectural consistency, and prevent error accumulation across extended development horizons.

Using EvoClaw, we conduct a comprehensive evaluation of 4 frontier agent frameworks and 12 state-of-the-art LLMs. We assess performance using a unified Score (Section 5.1), which balances Recall (completeness of new feature implementation) and Precision (robustness against regressions), along with a strict Resolve Rate for fully completed milestones. Our evaluation reveals the following key findings regarding agent capabilities in continuous software evolution:

A fundamental performance gap: Continuous vs. Independent. (Section 5.2) Frontier models exhibit a substantial degradation from independent to continuous task evaluation. Scores drop from over $\sim$`<!-- -->`{=html}80% on isolated tasks to at most 38.03% (Claude Opus 4.6) in continuous environments, with a mere 13.37% Resolve Rate (Gemini 3 Pro).

Recall grows linearly but Precision saturates. We identify a fundamental asymmetry in continuous software evolution (Section 5.4): while frontier agents retain the capability to implement new features (linear Recall growth), they fail to prevent regressions as the system evolves (saturated Precision). This indicates that agents struggle primarily with system-level maintenance rather than local implementation.

Accumulated errors stall downstream progress. Unresolved regressions trigger a "snowball effect" where errors accumulate faster than agents can fix them (Section 5.5). Early bugs propagate through dependency chains to contaminate downstream tasks, eventually stalling development entirely.

Proactive exploration and verification mitigate technical debt. Behavioral analysis shows that successful sustained evolution relies on proactive codebase exploration and disciplined test verification, whereas both blind trial-and-error and the absence of verification accelerate failure (Section 5.6).

## Related Work

LLM-Driven Coding Agents. While basic Bash tools alone can drive an LLM through software tasks, specialized scaffolding is what unlocks reliable, efficient, and user-friendly behavior. Scaffolds have evolved from predefined pipelines to fully autonomous systems. Commercial deployments span complementary use cases: Devin, GitHub Copilot, Cursor, Trae, and Antigravity integrate agents into IDE and cloud workflows, while Claude Code, Codex, and Gemini CLI run in the terminal. While these agents are well-validated on independent, interactive tasks, their reliability under long-horizon, fully autonomous operation remains a formidable challenge. EvoClaw addresses this gap with a standardized, quantitative evaluation that surfaces fine-grained progress-level feedback.

Automated SWE Environment Synthesis. A growing line of work automatically constructs testable Dockerized environments from open-source repository snapshots. These environments primarily serve to continuously refresh evaluation data and scale agent training. Unlike these snapshot-based approaches, DeepCommit preserves the temporal structure of development trajectories by reorganizing commit histories into Milestone DAGs, thereby synthesizing long-horizon tasks with verifiable progress checkpoints.

Issue Resolution Tasks. Unlike Terminal-Bench, which tests agents on shell commands isolated from any codebase, SWE benchmarks require modifying real-world GitHub repositories. SWE-bench pioneered this line by pairing issues with hidden tests, followed by SWE-bench Pro for data hygiene and Multi-SWE-bench for multilingual coverage.

Codebase Generation Tasks. Codebase generation benchmarks pursue longer-horizon evaluation by progressively enlarging the scope of a single task. At the feature level, SWE-Dev and FeatureBench require agents to implement complete features against curated test suites. At the release level, SWE-EVO bundles all changes between consecutive release tags into a single task. At the repository level, Commit0, NL2Repo, and ProgramBench push agents toward synthesizing entire repositories from scratch. Despite the enlarged scope, these benchmarks evaluate task instances in isolation on a reset codebase, leaving inter-task dependencies and accumulated technical debt unmodeled. EvoClaw instead links milestones through a dependency DAG over a persistent repository, making both intermediate progress and cross-task error propagation directly measurable.

Continuous SWE Tasks. Real software development involves a stream of dependent tasks on the same codebase. While LLMs are known to degrade in this setting relative to single-shot evaluation, dedicated benchmarks remain nascent. SlopCodeBench measures structural erosion and verbosity drift on hand-crafted tasks where an agent extends a codebase built from scratch. A complementary thread evaluates agents via continuous integration (CI) loops on real repositories. SWE-CI, for instance, chains commit-to-commit CI rounds by exposing ground-truth tests to a dual-agent protocol following the native commit order. EvoClaw instead adopts a coarser, functionally coherent granularity by grouping commits into self-contained milestones whose dependencies form a DAG. This approach offers a more faithful and flexible model of continuous software evolution than scattered commit-level CI.

Performance Optimization Tasks. A parallel direction evaluates whether agents can speed up code across repositories, numerical algorithms, and GPU kernels. While these works instantiate long-horizon evaluation, they focus on closed-ended optimization objectives, such as wall-clock time against an expert reference. In contrast, EvoClaw addresses the open-ended challenge of general functional software development.

Figure 2: The DeepCommit pipeline architecture. Phase 1 extracts structured data from commit history through static analysis, including source filtering, commit extraction, PR/Issues, releases, commit DAG, code metrics, and symbol changes. Phase 2 employs an LLM agent to construct a Milestone DAG via four iterative stages: seed discovery, milestone consolidation, dependency inference, and milestone decomposition. Phase 3 resolves runtime dependencies through testbed construction and test collection, with DAG refinement and fallback patches as repair strategies, followed by flaky test filtering to produce an executable testbed. Quality Assurance validates outputs at textual, compilation, and test collection levels. See Appendix B.4 for all DAG visualizations.

## DeepCommit: An Automated Pipeline for Reconstructing Software Evolution

### From Raw Commits to Milestone DAGs

Software repositories encode rich evolutionary trajectories, yet raw commit histories remain noisy, fragmented, and inadequate as executable development sequences. Commits vary widely in granularity, semantic clarity, and dependency structure, while parallel branches, squash merges, and non-functional changes obscure true developmental relationships. Relying on documentation or release notes alone lacks sufficient resolution to reconstruct precise code evolution. DeepCommit addresses this challenge by transforming linear git histories into structured, verifiable Milestone DAGs, where each node represents a coherent, testable unit of development and edges encode dependency constraints across evolution phases.

### Overall Agent-Driven Pipeline

As illustrated in Figure˜2, DeepCommit reconstructs software evolution itineraries through an end-to-end pipeline that sequentially integrates: commit history preprocessing, Milestone DAG construction, and executable environment resolution.

### Commit History Preprocessing

We model each repository's main-branch range between release tags as a linear sequence of commits. This linearization aligns naturally with the squash-and-merge workflow, the most widely adopted convention in actively-maintained, high-quality repositories, where each main-branch commit maps to a Pull Request (PR) or Issue together with its internal sub-commits. We collect all main-branch commits and their PR, Issue, and Release metadata. An LLM agent then prepares a per-repo configuration of source directories, test patterns, and exclusion rules that separates product-logic source from test code and filters out commits touching only non-source files such as docs, CI configs, and build assets (Appendix A.1). To enable downstream milestone discovery and dependency inference, we extract three structural signals via static analysis: (i) a commit-level DAG built with git blame to capture line-level textual dependencies, (ii) symbol-level modifications identifying changes in classes and functions, and (iii) file-level co-change statistics reflecting evolutionary coupling.

### Milestone DAG Construction

Organizing hundreds of discrete commits into functionally coherent milestones requires integrating structural dependencies with code-level reasoning. We employ a four-stage LLM-agent-driven process to progressively construct the Milestone DAG. Each stage is orchestrated with automated data preparation, agent-accessible validation tools, and a post-stage quality gate. A stage runs in a forward pass and may iterate internally against its self-checks. At stage boundaries, the pipeline can also fan out into multiple parallel instantiations of the next stage and retain the variant that best satisfies the downstream quality gate.

Seed Discovery. Each milestone is initiated by a seed commit, namely a foundational anchor that introduces a distinct development theme. An LLM agent identifies such seeds by jointly evaluating commit semantics (commit messages and linked discussion context) and structural signals (DAG topology, including out-degree and descendant count), filtering out cosmetic edits, hotfixes, and follow-up patches that lack downstream structural influence.

Milestone Consolidation. For each seed, parallel sub-agents expand the milestone boundary using shared file modifications, temporal proximity, and PR/Issue references, growing each seed into a milestone that bundles all commits realizing its development theme. Since the sub-agents operate independently, the same commit may be claimed by several milestones. A coordinating agent then resolves these overlapping claims so that each commit belongs to exactly one milestone, enforces complete coverage of the range, and certifies acyclicity.

Dependency Inference. The majority of inter-milestone edges follow directly from the line-level textual dependencies extracted during preprocessing. More subtle dependencies, such as call relationships that share no common hunk, are proposed and validated by an LLM agent using symbol-level analysis and file co-change patterns. Even so, certain dependencies surface only when milestones are built and executed. These residual edges are recovered later during runtime environment resolution (Section˜3.2.3).

Milestone Decompose. Oversized milestones are decomposed into functionally independent sub-milestones while underspecified ones are merged into adjacent neighbors, with dependencies synchronously updated to preserve a valid DAG. When an oversized milestone is dominated by a single squashed PR-commit, the agent further re-segments the commit's diff along feature boundaries and remaps the affected dependency edges via line-level blame, promoting the resulting sub-units to first-class milestones. The pipeline targets a coefficient of variation ${CV} < 1.0$ over per-milestone LoC, achieving ${CV} = 0.96$ on EvoClaw (Appendix A.2).

### Runtime Environment Resolution

To transform the Milestone DAG into an executable evaluation environment, a MainAgent orchestrates a multi-agent workflow that produces, for every milestone, a reproducible Docker image that yields stable test signals. From a whole-evolution perspective, the MainAgent balances testbed quality against the cost of automated resolution. To achieve high quality at reasonable cost, the pipeline additionally relies on human-expert guidance to steer the MainAgent at key decision points. The MainAgent then dispatches sub-agents for batch analysis and problem localization, routing the surfaced issues to two specialized repair modules that iterate together until every milestone reaches a stable, fully collected state.

Milestone DAG Optimization and Testbed Preparation. A MilestoneAgent reconstructs each milestone's code state by cherry-picking its commits in topological order onto the codebase at the base release tag. When a cherry-pick conflict arises, the agent repairs the DAG, primarily by adding the missing cross-milestone dependency edge and, when necessary, relocating misattributed commits to the correct milestone. Commits that still cannot be applied are marked as deferred, so that every milestone is reconstructed into a complete, DAG-consistent state.

Environment Configuration and Test Collection. For each milestone, an EnvAgent generates a Dockerfile from the repository's CI/CD workflows and enforces three hard gates: the source compiles, the test framework collects successfully, and as many tests referenced by the milestone's patch as possible are captured in the collected set. A characteristic failure mode arises when the configured test environment runs ahead of the cherry-picked source state, so that functional modules referenced by the collected tests do not yet exist. These cases cannot be fixed locally and are deferred to the DAG optimization module for refinement (Appendix A.3).

### Automated Quality Assurance

To ensure the reliability and reproducibility of our evaluation, we rigorously validate each milestone testbed and report the aggregate evidence across three core dimensions, complementing the per-milestone gates enforced in Section˜3.2.3:

Milestone Graph Validity. We verify the structural integrity of the reconstructed history. This includes confirming commit completeness (100% coverage of the target range), dependency consistency (ensuring milestone dependencies respect underlying commit dependencies), and DAG correctness (validating acyclicity).

Runtime Executability. We ensure that errors stem from agent code, not infrastructure. We verify testbed compilability by ensuring successful build and test collection in both states. We also strictly monitor execution logs to ensure environment-induced errors remain negligible ($\leq$`<!-- -->`{=html}0.10%).

Evaluation Reliability. We assess the stability of the test suites. We achieve a high test collection rate (87.1%). We ensure test consistency by validating a negligible Pass-to-Fail rate ($\leq$`<!-- -->`{=html}0.026%) and filtering flaky tests through three repeated runs. Finally, we require each retained milestone to expose at least one F2P or N2P test signal (details in Appendix A.4).

Figure 3: Illustration of the evaluation pipelines. (a) In the Independent Task Evaluation Workflow, the environment resets after each task. (b) In the Continuous Task Evaluation Workflow, tasks are organized as a dependency graph. The agent continuously evolves the Codebase from a base snapshot. Upon completing a task (e.g., M1 &amp; M2), the repository is snapshotted for Isolated Evaluation while the planner unlocks subsequent tasks (e.g., M3) for the agent to fetch, ensuring a continuous and stateful development loop.

## EvoClaw: Benchmarking Continuous Software Evolution

EvoClaw introduces a novel evaluation paradigm designed to assess an agent's ability to evolve and maintain a software codebase over an extended lifecycle. As shown in Figure˜3, unlike traditional benchmarks that focus on resolving independent issues, EvoClaw simulates a realistic, continuous development process where requirements arrive as a stream, and tasks have strict sequential dependencies.

### The Continuous Task Evaluation Framework

The framework orchestrates a continuous development pipeline: an external planner dynamically unlocks tasks based on a dependency graph, the agent implements them in a persistent codebase, and the framework asynchronously evaluates snapshots upon submission. This design explicitly decouples roadmap planning from implementation, allowing us to assess the agent's ability to maintain and evolve software within a structured workflow. The framework comprises three core components:

Dependency-Driven Task Stream. Requirements are not presented in a static batch but are unlocked dynamically. The system maintains a DAG-based task scheduler where a new milestone $M_{i}$ becomes available to the agent if and only if all its prerequisite milestones $\{ M_{j} \mid M_{i}{depends}{on}M_{j}\}$ have been completed. This simulates real-world constraints in which foundational features must be established before dependent features are implemented.

Continuous Evolution Environment. The agent operates within a persistent, stateful environment where modifications from each task persist into the next. This compels the agent to maintain the long-term health of the codebase, as early technical debt or latent bugs can accumulate and impede future progress.

Snapshot-Based Isolated Evaluation. To reconcile the need for a continuous development flow with rigorous verification, we employ a "develop-in-place, evaluate-in-isolation" strategy. Upon task completion, the agent's implementation state is snapshotted and transferred to an isolated evaluation container to run the test suite. This ensures that the scoring process is reproducible and unaffected by the agent's ongoing development, while the agent's working environment remains uninterrupted.

### Benchmark Construction

We construct a high-quality dataset through a rigorous pipeline that transforms open-source repositories into verified evolutionary suites.

Repository and Range Selection. We identify projects with high community impact and diverse programming languages. We specifically select release ranges that exhibit rich dependency structures, ensuring the benchmark captures complex, non-linear development scenarios rather than trivial sequences.

Itinerary Extraction via DeepCommit. Leveraging the DeepCommit pipeline (Section 3), we mine the evolutionary history of selected projects. To guarantee the benchmark's quality and evaluation efficiency, we apply strict post-processing filters to the generated milestones. We retain only milestones that: represent core functional changes (filtering out pure documentation updates); possess executable F2P tests to serve as definitive success criteria; and fall within a manageable context window to maintain task solvability. This step ensures that every task in the benchmark is grounded in a verified, executable state transition.

Reverse-Engineering Software Requirement Specifications (SRS). Relying solely on original GitHub issues or PR descriptions is often insufficient, as they can be underspecified, outdated, or disconnected from the final code implementation. To bridge this gap, we employ an agent-driven reverse-engineering approach to synthesize high-fidelity Software Requirement Specifications (SRS). We first dispatch an LLM agent to analyze the ground-truth patches to draft precise functional requirements. This draft then undergoes a refinement phase to align acceptance criteria strictly with the verified Fail-to-Pass tests. Finally, environment-specific instructions (e.g., dependency updates) are appended by analyzing build configuration changes, ensuring a complete execution context.

Human-in-the-Loop Verification. Automated generation can yield logical inconsistencies and misalignment with edge cases. To mitigate this, expert annotators conduct a final review focused on task solvability. Annotators verify that the SRS provides all necessary information to solve the problem without leaking implementation details and that the acceptance criteria are unambiguous. Simultaneously, we validate the stability of the test suites to rule out flaky tests. This hybrid verification ensures that EvoClaw provides a fair assessment, distinguishing genuine agent errors from artifacts of ambiguous specifications (Appendix B.1).

(a) Distribution of milestones across the 7 repositories in EvoClaw. Each bar represents the number of verified milestones extracted from the corresponding open-source project.

(b) Distribution of SRS word counts (left) and gold patch LOC (right), stratified by estimated human effort.

Figure 4: Dataset statistics and characteristics of EvoClaw.

### Benchmark Statistics

EvoClaw comprises 98 verified milestones across 7 diverse open-source repositories, spanning five programming languages (Go, Rust, Java, TypeScript, Python) with a total of 109 inter-milestone dependencies. As shown in Figure˜4(a), the milestones are distributed across repositories with varying complexity, ranging from 9 to 23 milestones per repository. The dataset captures diverse real-world development patterns, including major architectural changes (e.g., multi-library support), feature-rich iterations (e.g., cloud-native enhancements), stability-focused releases (e.g., compatibility fixes), and large-scale refactoring (e.g., type system overhauls). This ensures EvoClaw evaluates agents across the full spectrum of software engineering tasks.

Figure˜4(b) illustrates the distribution of task complexity. The dataset exhibits substantial diversity in both specification length (SRS mean: 1,348 words) and implementation scope (gold patch LOC ranging from $< 100$ to $> {1,500}$). On average, each milestone modifies 27.4 files and involves 17.1 Fail-to-Pass tests for verification alongside 6,218 Pass-to-Pass tests for regression prevention. Detailed per-repository statistics are provided in Appendix B.3, and the full Milestone DAG visualizations for all repositories are shown in Appendix B.4.

## Results and Analysis

### Experimental Setup

### Evaluation Settings

To isolate how error accumulation across milestones affects agent performance, we evaluate methods under two different settings based on the Milestone DAG: Continuous Task Evaluation, the standard EvoClaw setting where agents continuously evolve a codebase under streaming requirements. This setting introduces real-world challenges such as error accumulation and technical debt management. Independent Task Evaluation, a stateless baseline (similar to SWE-bench ) in which each milestone is treated as an isolated task by providing agents with the canonical codebase snapshot, thereby decoupling performance from the cumulative effects of prior modifications.

### Evaluation Metrics

Evaluating agents in a continuous evolution setting requires metrics that capture two competing objectives: implementing new functionality and preserving existing behavior. Traditional benchmarks such as SWE-bench rely on binary success criteria (all tests pass or fail), which are too coarse-grained to capture the nuance of incremental progress and regression. Simple pass-rate metrics conflate these two objectives, failing to distinguish an agent that implements features but introduces regressions from one that avoids regressions but makes no progress.

To address this limitation, we decompose agent performance along two complementary dimensions:

Recall measures feature implementation completeness: the proportion of required functional changes successfully implemented by the agent.

where $N_{\text{required},m}$ denotes the total number of Fail-to-Pass (F2P) tests for milestone $m$ (tests that transition from failing at the start state to passing after the milestone's gold patch is applied), and $N_{\text{fixed},m}$ is the count of such tests that the agent successfully fixes.

Precision measures modification reliability: the proportion of test status changes that are improvements rather than regressions, quantifying the safety of the agent's edits.

where $N_{\text{broken},m}$ is the number of Pass-to-Pass (P2P) tests (tests that pass at the start state and must remain passing after the agent's changes) that regress (fail or error out) due to the agent's changes. The term $\epsilon = 1$ is a smoothing factor to handle cases where the agent makes no impact (i.e., when both fixed and broken counts are zero).

We then define the score for each milestone as the harmonic mean of Recall and Precision:

The final reported metric is the average Score across all milestones: $\text{Score} = {\frac{1}{|M|}{\sum_{m \in M}\text{Score}_{m}}}$. This ensures that neither dimension can be neglected: an agent that implements all features but introduces severe regressions will score as poorly as one that preserves existing functionality but fails to implement any changes.

Consistent with prior work like SWE-bench, we also report the Milestone Resolve Rate, where a milestone is considered resolved only if the agent passes all associated F2P and P2P tests. We report the average resolve rate across all repositories. While Score quantifies partial progress, Resolve Rate assesses whether the task was fully resolved.

### Evaluated Models and Agents

We evaluate a diverse set of frontier LLMs across four agent frameworks. Specifically, we test Claude Code with Claude Opus 4.5, Claude Sonnet 4.5, Claude Opus 4.6, and Claude Sonnet 4.6, Codex CLI with GPT 5.2, GPT 5.2-Codex, and GPT 5.3-Codex (all set to xhigh reasoning effort), Gemini CLI with Gemini 3 Pro, Gemini 3.1 Pro, and Gemini 3 Flash (all by default with 1M context), and OpenHands with Claude Opus 4.6, GPT 5.3-Codex, Gemini 3 Flash, Kimi K2.5, and MiniMax M2.5. Detailed framework versions, context management configurations, and the unified agent system prompt (Figure 18) are provided in Section˜B.2.

Table 2: Performance of coding agents on EvoClaw under continuous task evaluation. All metrics are per-evolution-range averages. Out Tok. (K): total generated tokens in thousands, including reasoning where applicable. ⋆Primary metric (shaded). Bold: best in column. †Token tracking unavailable for some repos; averaged over available data.

### Overall Performance

Figure 5: Per-repository score comparison under two evaluation modes. High independent-task performance across all repositories confirms that milestones are individually solvable.

Table 2 presents results across 15 agent-model configurations. Claude Opus 4.6 achieves the highest Score (38.03% in Openhands and 36.29% in Claude Code), followed by Claude Sonnet 4.6 (29.58%) and GPT 5.3-Codex (28.88%). Across all models, the gap between Score ($\sim$`<!-- -->`{=html}38% at best) and Resolve Rate ($\sim$`<!-- -->`{=html}13%) is substantial: agents achieve partial progress on most milestones but rarely complete them fully. Moreover, the resolved milestones are predominantly early ones with few upstream dependencies, confirming that accumulated upstream errors increasingly hinder downstream task completion. Unless otherwise noted, subsequent analyses focus on configurations where each model is paired with its vendor-provided agent framework.

Figure 6: Overall Score vs. cost trade-off across all repositories.

Across model families, generational improvements emerge: Claude 4.6 models significantly outperform their 4.5 predecessors, and GPT 5.3-Codex substantially improves over its predecessors. However, comparing GPT 5.2 and GPT 5.2-Codex reveals that Codex-specific optimization may be counterproductive for long-horizon development, where sustained codebase maintenance demands broader analytical capabilities beyond isolated task solving. The three Gemini models achieve comparable scores, with Gemini 3 Flash matching Gemini 3 Pro at one-ninth the cost. Gemini 3 Pro uses the fewest turns, possibly indicating insufficient exploration. Figure 6 visualizes the cost-score trade-off. Higher cost does not uniformly translate into higher performance: Gemini 3 Pro exceeds \$100 per evolution range yet scores below Opus 4.6 (\$88), and Sonnet 4.6 (\$69) trails Opus 4.6 by 6.7 points despite a similar cost tier. On the Pareto frontier, Gemini 3 Flash (\$12, 24.2%) and GPT 5.3-Codex (\$25, 28.9%) offer the best cost-effectiveness, achieving competitive scores at a fraction of the cost of top-performing models. OpenHands trials exhibit notably longer execution times (e.g., 18.49 h for GPT 5.3-Codex) because its runner permits up to 3,000 iterations per milestone with automatic session resumption, allowing the agent to retry extensively when stuck. This additional compute does not consistently improve scores: Claude Code with Opus 4.6 achieves a comparable score in under 4 hours.

Figure 5 compares per-repository performance under both evaluation modes. High independent-task performance across all repositories confirms that milestones are individually solvable, indicating that the difficulty stems from long-horizon error accumulation rather than inherent task complexity. This effect varies significantly by repository. scikit-learn exhibits the largest degradation: Claude Sonnet 4.6 achieves 93.2% independently but only 21.1% under continuous evaluation.

Overall, these results highlight that EvoClaw poses a significant challenge to current frontier models, and reliable long-horizon continuous development remains an open problem.

Figure 7: Task complexity effects on Score (top) and Resolve Rate (bottom), binned by code size, specification length, execution order, and DAG layer. Dashed lines are per-bin averages across models.

### Task Complexity and Topological Effects

Figure 7 examines how milestone characteristics correlate with agent performance. Gold patch LOC, a traditional measure of task complexity, shows a clear monotonic relationship. Larger patches require more code changes and yield lower scores across all models. SRS (Software Requirements Specification) word count, however, exhibits a non-monotonic pattern, with a clear sweet spot for specifications of moderate length (around 500 to 1500 words). When specifications are concise, agents must autonomously locate relevant context from the repository, increasing exploration burden. When specifications are verbose, the sheer volume of requirements increases implementation workload. Milestones with moderate-length SRSs achieve the highest accuracy, suggesting that task difficulty depends not only on implementation effort but also on the cost of information acquisition.

Beyond these static factors, the continuous evaluation setting introduces structural complexity unique to EvoClaw. Both the milestone execution order and the DAG topological layer show statistically significant negative correlations with the score. Later milestones and deeper topological layers consistently yield lower performance. This reflects the compounding effect of upstream errors, as agents must build upon their own (potentially flawed) prior work. These topological factors are absent in independent evaluation and represent the distinctive challenge of long-horizon software evolution. The Resolve Rate (bottom row of Figure 7) makes this effect even starker: it drops drastically beyond the earliest milestones and the shallowest DAG layers, indicating that current agents can only fully resolve milestones that appear early in the sequence or have no upstream dependencies. Once prior errors accumulate, agents may still achieve partial progress (reflected in Score) but rarely produce a completely correct solution.

Figure 8: Evolution dynamics across models. (Left) Multi-window extrapolation of saturation curves fitted with y = a (1−e−b x), showing projected ceilings beyond the observed window. Legend annotations report init = a b (marginal efficiency at the onset of the sequence) and retain = e−b (fraction of efficiency preserved after each observation window). (Middle) Continuous vs. Independent comparison for GPT 5.3-Codex (better retain) and Gemini 3.1 Pro (better init). (Right) Continuous vs. Independent comparison for the Claude model family.

Figure 9: Per-model cumulative Recall (solid) and Precision (dotted) over evolution progress. Stronger models achieve near-linear Recall growth, yet Precision saturates across all evaluated configurations.

### Evolution Dynamics: Recall Scales while Precision Saturates

The declining performance at later milestones raises a natural question: does agent capability degrade over time, or does accumulated technical debt overwhelm otherwise competent agents?

To answer this, we model cumulative score trajectories using a saturation function $y = {a{({1 - e^{- {bx}}})}}$, where a small $b$ yields near-linear growth while a large $b$ produces rapid saturation toward the ceiling $a$. As shown in Figure 8 (left), all models under exhibit clear performance ceilings, and multi-window extrapolation (fitting the saturation model to progressively larger subsets of milestones and projecting forward) confirms that these ceilings persist beyond the observed window. Comparing continuous and independent evaluation (middle, right), independent scores grow near-linearly while continuous scores saturate, with the gap widening monotonically as evolution progresses.

We decompose the cumulative score into Recall (successful feature implementation) and Precision (preservation of existing functionality) to isolate the underlying mechanism. Figure 9 reveals a fundamental asymmetry: Recall continues to grow near-linearly across all models (especially frontier models), indicating that agents retain the ability to solve newly assigned tasks. Precision, however, saturates rapidly across all evaluated configurations. This means the performance ceiling is not caused by agents forgetting how to code, but by their inability to prevent regressions from accumulating. Stronger models achieve higher Precision plateaus, yet none avoid saturation entirely. This Recall-Precision divergence provides a mechanistic explanation for the snowball effect: as unresolved regressions compound, each new milestone operates on an increasingly degraded codebase, eventually overwhelming the agent's capacity for productive development.

Figure 10: Propagation type analysis for Opus 4.6. Left: Selected error chain patterns across repositories, where each column is an error chain and each row a milestone. Right: Distribution of propagation event types across milestone progress bins (averaged over all repositories), showing how inherited failures (P1) and infrastructure effects (PX) increasingly dominate in later stages.

### Failure Analysis: Error Generation and Propagation

Understanding why agents fail in continuous evaluation is inherently difficult. A single early mistake can trigger cascading test failures across dozens of downstream milestones, making it challenging to disentangle root causes from their propagated consequences. To enable systematic analysis, we introduce the concept of error chains: for each test that transitions from passing to failing during the evolution, we trace its status across all subsequent milestones until it is either healed or the trial ends. This yields a per-test timeline that captures the full lifecycle of an error. We focus this analysis on the strongest configuration, Claude Opus 4.6, to characterize failure mechanisms at the frontier of current agent capabilities.

We decompose error chains along two orthogonal dimensions. The first, Propagation Type, captures how a fault affects downstream milestones. This is determined statistically from evaluation results: we track each test's status across the milestone timeline and classify events as P0 Root Cause (the originating failure), P0 Induced (cross-chain contamination from unrelated changes), P1 Inherited (propagated through dependency), PX Missing (skipped execution), or PH Healed (successfully recovered). Figure 10 (right) shows that propagation events (P1, PX) increasingly dominate in later stages, confirming the compounding degradation observed in Section 5.3. The left panel visualizes representative error chain patterns across repositories, illustrating how a single root cause event can cascade through the entire remaining evolution.

Figure 11: Root Cause Type × Propagation Type heatmap. Each cell shows the macro-averaged event proportion across all repositories.

The second dimension, Root Cause Type, captures why the initial fault originates. Since root cause attribution requires understanding the agent's intent, we employ Claude Sonnet 4.6 as a reviewer agent that compares the task agent's code changes against the ground-truth patch, the SRS specification, and evaluation artifacts. The reviewer classifies each error chain's root cause into three categories: Logic Error (correct target, buggy implementation), Omission (missing a required component), or Extraneous (unnecessary modifications that break existing functionality). Figure 11 presents the joint distribution of Root Cause Type $\times$ Propagation Type. Logic Error is the dominant root cause ($\sim$`<!-- -->`{=html}57% of all error chain events), with its chains exhibiting both the highest inherited propagation (P1, 12%) and the highest proportion of missing test execution (PX Missing, 17%), indicating that buggy implementations frequently prevent downstream tests from running at all.

### Agent Behavior: The Struggle Against Accumulating Complexity

Beyond aggregate scores, we examine how agents allocate effort and manage state when facing accumulating technical debt during long-horizon iterations. By instrumenting tool calls, context usage, and interaction turns, we reveal distinct behavioral patterns.

Figure 12: Continuous-to-Independent turns ratio across normalized execution progress (10 bins). Values above 1× indicate the agent expends more effort under continuous evaluation than on the same milestone independently. The ratio remains near or below 1× for most of the sequence but rises sharply in the final bin. This reflects increased rework and error-recovery effort as accumulated technical debt compounds.

Figure 13: Exploration ratio and context wave for Claude Code (powered by Opus 4.6) on element-web. Top plot shows milestone progression (M1 to M18). Middle plot shows per-minute exploration ratio (read/search vs. write/execute). Bottom plot shows total context token usage over active time, with compaction and eviction events marked.

Effort Fluctuation and Extremes. As shown in Figure 12, all evaluated agents exhibit a shared trend in their effort allocation (measured by the continuous-to-independent turns ratio). In the initial phase (progress $\sim$`<!-- -->`{=html}0.1), continuous effort is slightly higher than independent effort, as agents must conduct large-scale exploration to build a mental model of the unfamiliar repository. During the middle phase (progress 0.1--0.5), the ratio drops below $1 \times$ (with the median falling to $\sim$`<!-- -->`{=html}0.83$\times$): agents successfully reuse their established context, bypassing the redundant exploration required in independent evaluation. However, in the late stage (progress 0.6--0.9), effort rises significantly as accumulating errors demand extensive debugging. Finally, near completion (progress $\sim$`<!-- -->`{=html}1.0), agent behavior diverges sharply. Some agents resort to frantic thrashing, while others prematurely give up. Notably, GPT 5.3-Codex demonstrates the most stable effort profile, maintaining consistent variance throughout the project lifecycle.

Context Stability and Exploration Patterns. To sustain this fluctuating effort, agents must effectively manage their context. Figure 13 illustrates this using Claude Code with Opus 4.6 as a representative example. The context window shows stable, controllable wave patterns, demonstrating that modern agent frameworks paired with frontier models can effectively support long-horizon programming without catastrophic context overflow. The framework employs two compression strategies: partial compression (evicting specific tool results) and heavy compaction (summarizing extensive histories). Crucially, agent exploration behavior (reading and searching) tightly couples with this state management. Exploration surges at the beginning of each new milestone and immediately following major context compaction events, as the agent works to rebuild its mental model.

Figure 14: Exploration tool-call count aggregated across all repositories, grouped by agent framework and sorted by count within each cluster. Diamond markers show average F1 score. Higher-performing agents consistently devote greater effort to exploration (e.g., reading and searching).

Figure 15: Average verification tool-call count per milestone progress bin (10 bins), for the six strongest agent configurations. Verification effort generally increases with progress. It peaks around 70% to 80% completion before declining in the final bin.

The Impact of Exploration. This exploration behavior directly dictates downstream success. Figure 14 demonstrates that within their respective agent frameworks, models from the same family exhibit a consistent pattern: higher exploration counts correlate with better performance. For instance, Claude Opus 4.6 and Claude Sonnet 4.6 hold a distinct advantage because they aggressively dispatch subagents to analyze the codebase, executing over 7,000 exploration commands. Conversely, models like Gemini 3 Pro allocate too little effort to reading, indicating that many current models still lack proactive exploration for long-horizon tasks.

Figure 16: Score landscape in the edit-thrashing (repeat edit ratio) vs. verification (test execution frequency) space, aggregated across all repositories. A sweet spot of moderate thrashing and moderate verification yields the highest scores. The blind thrashing quadrant (high thrash, low verify) produces the worst outcomes.

Verification vs. Blind Thrashing. Alongside exploration, we analyze verification behavior (test execution). Figure 15 shows that average verification effort generally follows an inverted-U shape, increasing as the codebase grows more complex before declining near the end. However, this masks two problematic extremes: Gemini 3.1 Pro verifies excessively, while GPT 5.2-Codex rarely verifies at all, and both achieve lower scores. Figure 16 further isolates this dynamic by mapping the score landscape against edit thrashing and verification frequency. A clear sweet spot emerges for moderate, disciplined verification. In contrast, the worst outcomes concentrate in the high-thrash and low-verify quadrant---a blind thrashing trap where agents repeatedly modify the same files without executing tests to guide them, effectively accelerating the snowball effect.

### DeepCommit vs Human-Annotated Milestone DAG

We conducted a case study (Appendix C.3) that compares the human-annotated and DeepCommit Milestone DAGs for the scikit-learn v1.5.2--v1.6.0 release interval. The Human DAG organizes milestones by semantic release intent, whereas DeepCommit derives groups from dependency topology in the commit graph. As a result, DeepCommit covers a smaller but tightly connected subset of commits, recovers human-like boundaries when technical structure is clear (e.g., documentation), but tends to fragment cross-module, intent-defined milestones into topological phases. Overall, this case study shows that the Human DAG captures semantically coherent and process-aware milestone structure, whereas DeepCommit more strongly reflects dependency topology and phase-wise code organization.

## Conclusion

We introduced DeepCommit, a pipeline that distills verifiable software evolution into coherent Milestone DAGs from noisy, fine-grained git histories, and EvoClaw, a benchmark for evaluating LLM agents under continuous, dependency-driven development. Our results reveal a fundamental gap between independent task-solving and continuous evolution: frontier models achieve over 80% on isolated milestones but drop below 38% in continuous settings. This degradation stems from a critical inability to maintain code integrity: while agents can implement new features, they fail to prevent regressions, causing a snowball effect of accumulating technical debt. Even the strongest agents resolve only $\sim$`<!-- -->`{=html}13% of milestones in full evolutionary sequences, establishing sustained, maintainable repository evolution as a central open challenge for autonomous software agents.

## Limitations

EvoClaw and the DeepCommit pipeline have several limitations that bound the conclusions to be drawn and the settings to which they currently apply.

### Test-Suite Dependency

Our construction relies on repositories with well-maintained, executable test suites that provide reliable F2P and P2P signals. Projects that lack rich test coverage, or whose tests depend on inaccessible external services, cannot currently be incorporated into the benchmark.

### Filtering Bias

The pipeline retains only commits that touch source code with non-trivial inter-commit dependencies, dropping documentation-only commits and commits without resolvable structural ties. This filtering improves DAG quality and evaluation tractability, but it may bias the resulting benchmark toward dependency-rich evolution and underrepresent independent maintenance work.

### Data Contamination Risk

The repositories used in EvoClaw are high-impact open-source projects whose commit histories may have appeared in the pretraining corpora of frontier models. The substantial performance gaps we observe among frontier models suggest contamination has limited impact on relative ranking, but we cannot fully rule out memorization on individual milestones. Continuously refreshing the benchmark with newly merged commits, or applying DeepCommit to private repositories, would mitigate this risk.

### Human-in-the-Loop Reliance

Two stages of DeepCommit still require human-expert oversight: (i) the MainAgent's scheduling decisions during runtime environment resolution, where humans guide the trade-off between testbed quality and resolution cost, and (ii) the SRS verification stage, where human annotators run the three-step refinement loop described in Appendix B.1. Fully automating these stages remains an open engineering problem.

### Scale Limit

The current pipeline targets release ranges whose source-code gold patch is under roughly 30k LoC. Larger ranges produce Milestone DAGs that exceed the agent's resolution budget and frequently fail the testbed-construction gates. Scaling DeepCommit to longer histories will require further improvements to both DAG construction and runtime resolution.
