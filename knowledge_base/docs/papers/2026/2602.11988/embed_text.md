## Introduction

Coding agents are being rapidly adopted across the software engineering industry, and providing context files like AGENTS.md, a README specifically targeting agents, has become common practice. With various industry leaders recommending this approach to adapt their agents to specific repositories, context files are now supported by most popular agent frameworks, and included in over 60'000 open-source repositories at the time of writing, as reported by AGENTS.md.

These context files typically contain a repository overview and information on relevant developer tooling, aiming to help coding agents to navigate a given repository more efficiently, run build and test commands correctly, adhere to style guides and design patterns, and ultimately to solve tasks to the user's satisfaction more frequently. To date, despite their widespread adoption, the impact of context files on the coding agent's ability to solve complex software engineering tasks has not been rigorously studied. This is due to two key challenges: i) because of their recent introduction, context files are not available for instances of prior benchmarks, and ii) popular, well-known repositories, typically used to create such benchmarks, are not representative of most codebases. As a result, a rigorous evaluation of the context files used in practice requires a new, complementary benchmark that contains only issues from less popular repositories with developer-committed context files.

Figure 1: Overview of our evaluation pipeline. We begin with real-world repositories and tasks derived from past pull requests. For each repository state, we generate three settings: \tiny{1}⃝ If a developer-provided context file exists, we include it in the repository. In \tiny{2}⃝, we omit the context file. \tiny{3}⃝ We use the coding agent’s recommended settings to generate the context file. Then we pass the repository and context file to the coding agent and instruct it to autonomously resolve the task. We finally analyze the trace for behavioral changes and apply the generated patch to check for task resolution success.

### This work: Benchmarking context files' impact on resolving GitHub issues

In this work, we investigate the effect of actively used context files on the resolution of real-world coding tasks. We evaluate agents both in popular and less-known repositories, and, importantly, with context files provided by repository developers. For this purpose, we construct a novel benchmark (Figure˜1, left), AGENTbench, comprising Python software engineering tasks, created specifically from real GitHub issues. The benchmark contains $138$ unique instances, covering both bug-fixing and feature addition tasks across $12$ recent and niche repositories, which all feature developer-written context files. AGENTbench complements SWE-bench Lite, which we leverage for the evaluation of automatically generated context files on popular repositories. We evaluate coding agents in three settings (Figure˜1, middle): without any context file, with context files automatically generated using agent-developer recommendations, and with the developer-provided context file. Our code to generate AGENTbench instances and evaluate coding agents is available here.

Surprisingly, we observe that *developer-provided files only marginally improve performance* compared to omitting them entirely (an increase of 4% on average), while *LLM-generated context files have a small negative effect* on agent performance (a decrease of 3% on average). These observations are robust across different LLMs and prompts used to generate the context files. In a more detailed analysis (Figure˜1, right), we observe that context files lead to increased exploration, testing, and reasoning by coding agents, and, as a result, increase costs by over 20%. We therefore suggest omitting LLM-generated context files for the time being, contrary to agent developers' recommendations, and including only minimal requirements (e.g., specific tooling to use with this repository). We hope our evaluation framework will aid agent and model developers to improve the helpfulness of LLM-generated context files.

### Key contributions

Our key contributions are:

AGENTbench, a new curated benchmark for the impact of actively used context files on agents' ability to solve real-world software engineering tasks.

An extensive evaluation of different coding agents and underlying models on AGENTbench and SWE-bench Lite, showing that LLM-generated context files tend to decrease agent performance, across models or prompts used to generate them, while developer-written context files tend to slightly improve it.

A detailed investigation of agent traces, showing that context files lead to more thorough testing and exploration by coding agents.

## Background and Related Work

### Coding agents

Coding agents are LLM-based systems designed for autonomous resolution of coding tasks. Typically, they consist of a harness that allows an LLM to interact with its environment using specialized tools , e.g., executing bash commands, conducting web searches, or reading, creating, or modifying files.

Their impressive performance on repository-level coding tasks like SWE-bench led to rapid adoption in the software engineering community and the development of new agents by specialized companies and model providers. Model providers now train their LLMs to use the tools exposed by their harnesses, which can substantially improve coding ability relative to simpler harnesses. Accordingly, in Section˜4, we evaluate each LLM only within its corresponding harness.

### Context files

As coding agents were more broadly adopted, a common need arose to provide the agent with additional context about novel and little-known codebases. To address this issue, model and agent developers recommend including *context files*, such as AGENTS.md or CLAUDE.md, with codebases. Many agent harnesses provide built-in commands to initialize such context files automatically using the coding agent itself, e.g., by providing a dedicated /init command in the agent interface. At the time of writing, AGENTS.md report that over 60'000 public GitHub repositories include a context file.

### Evaluating context files

Prior work collected and categorized the content of context files, deriving mostly descriptive metrics about their content without investigating their effectiveness. While individual developers report anecdotal evidence of better alignment and solution capabilities when providing context files, we are the first to investigate the impact of actively used context files on agent behavior and performance at scale.

### Repository-level evaluation

Spearheaded by Jimenez et al., evaluating coding agents on the autonomous resolution of real-world repository-level tasks quickly became the gold standard for assessing their capabilities. While initial work focuses on issue resolution, follow-up work proposed benchmarks on feature addition, unit test generation, function generation, code performance, and security. Our work evaluates whether autonomous issue resolution and feature addition capabilities improve with actively used context files.

Orthogonally, benchmarks have also been extended by mining more recent and more difficult problems, as well as instances focusing on end-user applications. We follow their approaches to mining novel task instances to obtain a specialized set of tasks in repositories that feature context files.

## AGENTbench

In this Section, we discuss the requirements for AGENTbench, a SWE-Bench-like benchmark that targets the evaluation of developer-provided context files, its generation process, and its statistics.

### Notation and Definitions

We first introduce the notation to describe codebases, their test suites, and changes to these codebases in the form of patches. Following the notation of Mündler et al., we denote a codebase, or repository $R$ after applying patch $X$ as $R \circ X$. Several patches can be applied sequentially, i.e., $R \circ X \circ Y$ is the codebase $R$ after applying a first patch $X$ and then a second one $Y$.

A *test suite* $\mathcal{T}$ is a collection of tests that is used to validate the functionality of code in the repository. Executing a test suite $\mathcal{T}$ on repository state $R$ returns ${{exec}_{R}{(\mathcal{T})}} \in {\{\text{pass},\text{fail}\}}$ either indicating that all tests in the suite passed or that at least one test failed. An *issue* $I$ is a task for autonomous completion by the coding agent, such as resolving a bug or implementing a requested feature. We denote quadruples of $(I,R,\mathcal{T},X^{\ast})$ as *instances*, where the coding agent is tasked with predicting a patch $\hat{X}$ given issue $I$ and repository state $R$ such that ${{exec}_{R \circ \hat{X}}{(\mathcal{T})}} = \text{pass}$, and $X^{\ast}$ is the golden patch for that instance. We define the *success rate* $\mathcal{S}$ as the percentage of predicted patches ${\hat{X}}_{i}$ for instances $(I_{i},R_{i},\mathcal{T}_{i},X_{i}^{\ast})$ where ${{exec}_{R_{i} \circ {\hat{X}}_{i}}{(\mathcal{T}_{i})}} = \text{pass}$.

### Generation of AGENTbench Instances

To construct AGENTbench, we use a five-stage construction process summarized below. We defer all the prompts used for this process to Appendix˜B.

### Requirements

We aim to evaluate the impact of both automatically generated context files and developer-written context files on the success rate of coding agents on real-world tasks and codebases. The primary source for real-world codebases is open-source projects and their publicly tracked and documented changes, so-called pull requests (PRs). In order to obtain developer-written context files, we need to source PRs from projects that adopted context files. This is challenging, because context files have only been formalized in August 2025, and have not been frequently used before. Further, the adoption of context file is not uniform across the industry: even at the time of writing, many repositories do not include context files.

### Finding repositories

We first use GitHub search to build a list of potential candidate repositories to extract instances . Specifically, we select codebases that contain a context file such as AGENTS.md or CLAUDE.md at the root directory. Next, we filter down to those using Python as the main language and featuring a test suite. Finally, we filter for projects with many publicly documented changes, requiring at least $400$ PRs. This criterion allows us to select codebases from which we can extract at least $10$ instances after our rigorous post-processing.

### Filtering pull requests

Given a repository, we filter PRs to retain those that are most likely to generate higher-quality instances using a combination of rule-based checks and an LLM agent. We only keep PRs that satisfy the following two criteria: they should reference at least one issue, and they should modify at least one Python file. Further, we filter for PRs that are assessed by the agent to introduce deterministic, testable behaviors that are suitable for SWE-bench Lite-like regression tests. We notice that, because the use of context files is a recently emerging trend, most repositories containing context files are niche. These niche repositories have less strict rules regarding pull requests, and thus most PRs may not include specific tests. To enable building instances from these more niche repositories, we therefore do not require PRs to edit unit tests that validate the code changes, in contrast to SWE-bench Lite, which focused on large and popular repositories and requires PRs to contain unit tests.

### Environment Set-Up

For every PR and corresponding repository state, we set up an execution environment such that its test suite can be run, using a coding agent. Specifically, we ask the agent to produce a small script that i) sets up the execution environment, ii) runs the test suite and iii) stores the results as a machine-readable dictionary at the root of the repository. We only keep PRs where the resulting dictionary contains at least one passing test, which corresponds to $87\%$ of the filtered instances.

### Task Descriptions

Many of the smaller repositories we used to source AGENTbench do not enforce strict requirements on the quality of PR and issue descriptions. As a result, many issues are too imprecise and underspecified to solve the task in a testable manner (e.g., in some cases, the PR body is empty). Further, some PRs implement new features, which would require detailed descriptions about expected behavior and interfaces. We therefore use a third LLM agent to produce a standardized and detailed task description $I$ based on the PR description, associated issues if available, and the original patch $X^{\ast}$. This standardized task description is divided into 6 sections: description, steps to reproduce, expected behavior, observed behavior, specification, and additional information. Importantly, we ask the agent not to leak the solution in the generated task description, and to provide precise specifications. We randomly sampled and inspected 10% of the generated instances, and found that none of them leaked the solution.

### Generating Unit Tests

As most collected PRs do not modify or add unit tests that we could use to check the correctness of any given implementation, we use an LLM agent to generate such unit tests. We provide the agent with the standardized task description $I$, the test files modified by the PR, if available, the original code changes $X^{\ast}$ made by the PR, and the base state of the repository $R$. We then ask it to generate tests that pass for any implementation that resolves the described task. We verify that the added tests fail on $R$ and pass on $R \circ X^{\ast}$. Finally, we manually improve tests that are over-specified (i.e., tests that check for implementation details not specified in the task description), resulting in newly generated tests $\mathcal{T}_{i}^{X}$. We further determine all tests of the repository test suite $\mathcal{T}_{i}^{R}$ that pass on the patched code, i.e., the maximal set $\mathcal{T}_{i}^{R \ast} \subseteq \mathcal{T}_{i}^{R}$, such that ${{exec}_{R_{i} \circ X_{i}^{\ast}}{(\mathcal{T}_{i}^{R \ast})}} = \text{pass}$, and obtain the final test set $\mathcal{T}_{i} = {\mathcal{T}_{i}^{X} \uplus \mathcal{T}_{i}^{R \ast}}$. The resulting tests achieve an average coverage of 75% of the modified code (see Table˜1).

### Evaluation

We thus obtain AGENTbench instances $i$, each consisting of a task description $I_{i}$, a codebase $R_{i}$, golden patch $X_{i}^{\ast}$, and a set of tests $\mathcal{T}_{i}$. During evaluation, we first set up the environment before prompting the coding agent with the task description $I_{i}$, retrieving the predicted patch ${\hat{X}}_{i}$, and measuring ${exec}_{R_{i} \circ {\hat{X}}_{i}}{(\mathcal{T}_{i})}$.

Figure 2: Distribution of AGENTbench instances across 12 open-source GitHub repositories, each containing context files.

## words

## words

## files

## lines edited

## files edited

## words

## sections

Table 1: Average, minimum, and maximum of key statistics of AGENTbench across the 138 instances. For context files, a section is the content between Markdown headers.

### Overview of AGENTbench

Using this process, we obtained 138 instances from a total of 5694 PRs from 12 repositories that meet our criteria, using GPT-5.2 with Codex as the agent. We visualize the distribution over repositories in Figure˜2 and show key statistics of AGENTbench in Table˜1. In comparison to SWE-bench Lite, our dataset is both more evenly distributed over repositories and has otherwise similar statistics.

## Experimental Evaluation

In this Section, we investigate what effect context files have on the behavior of coding agents and how strong this effect is. To this end, we conduct an extensive evaluation of various coding agents on SWE-bench Lite and AGENTbench, considering both automatically generated and developer-provided context files.

Figure 3: Resolution rate for 4 different models, without context files, with LLM-generated context files, and with developer-written context files, on SWE-bench Lite (left) and AGENTbench (right).

### Experimental Setup

We describe the experimental setup below, deferring further details to Section˜A.1.

### Coding Agents

We consider four coding agents, paired with suitable models: Claude Code with Sonnet-4.5, Codex with GPT-5.2 and GPT-5.1 mini, and Qwen Code with Qwen3-30b-coder. For Claude Code, we use the default settings and set the temperature of Sonnet-4.5 to $0$. Similarly, for Codex, we also use the default settings and set the temperature of GPT-5.2 and GPT-5.1 mini to $0$. For Qwen Code, we enable chat compression upon reaching $60$% of the total context limit (set to $256$K tokens), restrict shell outputs to $2000$ tokens, and set the temperature of Qwen3-30b-coder to $0.7$ with top-$p$ sampling at $0.8$. We deploy Qwen3-30b-coder locally using vLLM. We sample completions for each agent once. For all agents, the context file is fed into their context, either by writing it to AGENTS.md for Codex and Qwen Code, or to CLAUDE.md for Claude Code.

### Datasets

We use SWE-bench Lite, which consists of 300 tasks sourced from GitHub issues across 11 popular Python repositories, none containing developer-written context files, and our novel AGENTbench, consisting of 138 instances from 12 repositories, all containing developer-provided context files (see Section˜3).

### Settings

We consider three context file settings:

None: No context files are available, i.e., we remove developer-provided files for AGENTbench.

LLM: An LLM-generated context file is available. We use the recommended initialization command and model for each agent individually to generate the context file using the pre-patch repository state $R$.

Human: A developer-provided context file is available. We use the context file of the pre-patch repository state $R$. Only available for AGENTbench.

### Metrics

The main metric for agent performance is success rate (Section˜3.1), i.e., the portion of instances for which the agent produces a patch that leads to all tests passing. We additionally consider the number of *steps* the agent requires to complete a task. Each step is one interaction with the environment, e.g., calling a shell tool or modifying a file. Finally, we report the total *cost* of LLM inference required to complete a task. For Qwen3-30b-coder, we estimate the cost from the average OpenRouter API price.

### Main Results

Figure 4: Number of steps before the first interaction between the agent and a file included in the PR patch (lower is better) is generally lower without context files than with LLM-generated context files or with developer-written context files (Human) on SWE-bench Lite (left) and AGENTbench (right).

SWE- Bench Lite

Table 2: The average number of steps (lower is better) and execution cost (in USD — lower is better) per SWE-bench Lite and AGENTbench instance without context files (None), with LLM-generated context files (LLM), and with developer-written context files (Hum). We bold the best setting.

### LLM-generated context files increase cost and reduce performance

LLM-generated context files cause performance drops in 5 out of 8 settings across SWE-bench Lite and AGENTbench (see Figure˜3). In more detail, the average resolution rate is reduced by $0.5\%$ and $2\%$ on average on SWE-bench Lite and AGENTbench, respectively. Meanwhile, the context files increase the \# steps in every setting on average by $2.45$ and $3.92$ steps, respectively, which leads to a cost increase of 20% and 23% on average, respectively (see Table˜2).

### Human context files increase cost and performance

We observe that the developer-provided context files outperform the LLM-generated ones for all four agents, despite not being agent-specific, and improve the performance compared to no context files for all agents but Claude Code (see Figure˜3 right). However, developer-provided context files also increase the average number of steps and costs required to solve the task, on average by $3.34$ steps and at most 19%, respectively.

### Context files do not provide effective overviews

One recommendation for context files is to include a codebase overview. Across the 12 developer-provided context files in AGENTbench, 8 include a dedicated codebase overview, with 4 explicitly enumerating and describing the directories and subdirectories in the repository. Similarly, both the Codex and Qwen Code context file generation prompts explicitly instruct the agent to include an overview section, while the Claude Code prompt advocates for a high-level overview only and warns against listing components that are easily discoverable. We use GPT-OSS-120b to assess which of the LLM-generated context files contain codebase overviews. Surprisingly, $100\%$ of Sonnet-4.5-generated context files are flagged for overviews, and $95\%$ and $99\%$ for Qwen3-30b-coder and GPT-5.2 respectively. Only GPT-5.1 mini has significantly fewer overviews ($36\%$).

Figure 5: When removing all documentation-related files from the codebase, LLM-generated context files tend to outperform developer-provided (Human) ones on AGENTbench.

Figure 6: Increase in average tool use when including LLM-generated (bright green) or developer-provided (dark green) context files, compared to the average tool use without context files. For tool names, we map Codex and Qwen Code tools to the Claude Code equivalents (we detail the mapping in Appendix˜A).

To assess the usefulness of these overviews, we measure how quickly agents discover files relevant to the described issue $I$. Concretely, we measure the average number of steps before the coding agent interacts with any file modified in the original PR patch $X^{\ast}$. We exclude the $3\%$ of instances in which the agent never interacts with any file modified in $X^{\ast}$. Both on SWE-bench Lite and AGENTbench the presence of context files does not meaningfully reduce this metric, as shown in Figure˜4.

While context files appear to increase the number of required steps significantly for GPT-5.1 mini, we observe in manual trace inspection that this increase is due to it (i) issuing multiple commands to find the context files and (ii) reading them (multiple times) despite them being already included in the agent's context. Interestingly, we only observed this behavior if context files were present at all. We conclude that context files, even developer-provided ones, are not effective at providing a repository overview.

### Context files are redundant documentation

Our hypothesis is that LLM-generated context files are highly redundant with existing documentation, while developer-provided context files add additional information. To confirm this, we manually remove all documentation (files ending .md, example code, and the folder docs/) after generating the context file, and before evaluating the coding agents. We show the results in Figure˜5, excluding Claude Code due to its hight cost. In this setting, where context files are the only source of documentation available, LLM-generated context files not only consistently improve performance by $2.7$% on average, but also outperform developer-written documentation. This may explain anecdotal evidence reporting that coding agents perform better after adding context files, since many less popular repositories contain little to no documentation.

### Trace analysis

We now analyze the impact of context files on agent behavior in more detail by analysing the frequency of agent tool calls and length of reasoning traces. We describe our setup in more detail in Section˜B.2.

### Context files lead to more testing and exploration

In Figure˜6, we show the increase in average tool use when including LLM-generated (bright green) or developer-provided (dark green) context files. Negative values imply a decrease in tool use. We find that, across all models, when context files are present, the coding agents run more tests. They also tend to navigate the repository more: they search more files (grep), read more files, and write more files. Lastly, adding context files causes agents to use more repository-specific tooling (e.g., uv and repo_tool). In Figure˜10 (Appendix˜A), we perform a similar analysis using the intent of the tool call, leading to the same conclusion.

### Instructions in context files are typically followed

We find that agents generally follow instructions present in the context files. For instance, uv is used 1.6 times per instance on average when mentioned in the context files, compared to fewer than 0.01 times when it is not mentioned, and repository-specific tools are used 2.5 times per instance on average when mentioned, compared to fewer than 0.05 times when they are not mentioned. This effect is observable across almost all measured tools displayed in Figure˜6, as we show in a more in-depth analysis in Appendix˜A. In particular, this result implies that the absence of improvements with context files is not due to a lack of instruction-following.

Figure 7: Number of reasoning tokens spent on average by GPT-5.2 and GPT-5.1 mini, without context files, with LLM-generated context files, and with developer-written context files, on SWE-bench Lite (left) and AGENTbench (right).

### Following context files requires more thinking

We hypothesize that these additional instructions make the task harder. To confirm this, we analyze the average number of reasoning tokens used by GPT-5.2 and GPT-5.1 mini, as their adaptive reasoning allows them to use more reasoning tokens for tasks that they deem harder. In Figure˜7, we show that LLM-generated context files indeed increase the average number of reasoning tokens by 22% for GPT-5.2 and 14% for GPT-5.1 mini on SWE-bench Lite (respectively 14% and 10% on AGENTbench), and that developer-written context files increase the number of reasoning tokens by 20% and 2% for GPT-5.2 and GPT-5.1 mini, respectively.

### Ablations

In this Section we analyze differences between the context files generated by different models, and the impact of the prompt used to create the context files.

Figure 8: On SWE-bench Lite, performance is improved with context files generated by GPT-5.2 compared to using the model underlying the agent, while on AGENTbench performance is degraded.

### Stronger models don't generate better context files

We compare context files generated with GPT-5.2 + Codex to those created by our standard agents in Figure˜8. This improves performance on SWE-bench Lite across all models (2% on average), but degrades performance on AGENTbench across all models (3% on average). We thus conclude that stronger models do not necessarily generate superior context files.

Figure 9: When generating context files using the prompt from Codex or from Claude Code on SWE-bench Lite and AGENTbench, there is no consistent impact on success rate.

### No difference between the specific prompts

We compare context files generated using the prompt of Codex and Claude Code across all agents and models in Figure˜9. Surprisingly, Claude Code performs better with context files generated using the Codex prompt, while both GPT-5.2 and GPT-5.1 mini perform better on SWE-bench Lite with the Codex prompt but worse on AGENTbench. Overall, neither the prompt matching the underlying model and agent, nor a specific prompt performs consistently best, indicating that sensitivity to different (good) prompts is generally small.

## Limitations and Future Work

While our work addresses important shortcomings in the literature, exciting opportunities for future research remain.

### Niche programming languages

The current evaluation is focused heavily on Python. Since this is a language that is widely represented in the training data, much detailed knowledge about tooling, dependencies, and other repository specifics might be present in the models' parametric knowledge, nullifying the effect of context files. Future work may investigate the effect of context files on more niche programming languages and toolchains that are less represented in the training data, and known to be more difficult for LLMs.

### Context files beyond task resolution

In this work, we evaluate the impact of context files on task resolution rate. However, there are many other relevant aspects of coding agents, such as code efficiency and security, that we believe could be explored in future work. Specifically, for security, prior work found that prompting LLMs to generate secure code significantly improves the security of generated code.

### Improving context file generation

Another interesting avenue opened by this work is how to improve the automatic generation of *useful* context files. Here, human developers appear to dominate per our evaluation. Several related works in the direction of planning and continuous learning from prior tasks may be applicable for this task. By tackling this challenge, future agents could gain a long-term capability at meaningful self-improvement.

## Conclusion

We present an extensive evaluation of the impact of context files on coding agent performance for four common coding agents on SWE-bench Lite and AGENTbench. The latter is a new benchmark we built from recent GitHub issues and less popular repositories containing developer-written context files. We find that all context files consistently increase the number of steps required to complete tasks. LLM-generated context files have a marginal negative effect on task success rates, while developer-written ones provide a marginal performance gain.

Our trace analyses show that instructions in context files are generally followed and lead to more testing and a broader exploration, however they do not function as effective repository overviews. Overall, our results suggest that context files have only marginal effect on agent behavior, and are likely only desirable when manually written. This highlights a concrete gap between current agent-developer recommendations and observed outcomes, and motivates future work on principled ways to automatically generate concise, task-relevant guidance for coding agents.
