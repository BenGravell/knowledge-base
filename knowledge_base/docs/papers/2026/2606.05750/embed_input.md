<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Three Years of r/ChatGPT: Societal Impact Evaluations from Social Media Data

Topics include Large language models, Social networks, Survey data analysis, Human-computer interaction, Artificial intelligence, Societal-scale systems, Privacy.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Uses several years of r/ChatGPT social-media activity to evaluate how people discuss and experience the societal effects of generative AI. The paper is useful as an empirical complement to benchmark-centered AI evaluation, emphasizing public concerns, use cases, and community-level signals.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

ChatGPT was launched on November 30, 2022; the r/ChatGPT subreddit was created just one day later. Since then, chatbot-based AI products have gone from niche proofs-of-concept to widely-used household names. However, the ways in which adoption has developed among the public remains poorly understood. In this paper, we develop a framework for using social media as a data source for understanding the societal impact of widely-adopted consumer AI products, and propose PuLSE (Public and Longitudinal Signals for Evaluation), a general approach to monitoring for societally-impactful trends in real time. We apply our framework to conduct what is, to the best of our knowledge, the first longitudinal study of r/ChatGPT. We find that, overall, r/ChatGPT posts over time illustrate the normalization of ChatGPT as an everyday consumer product rather than an exceptional, novel technology.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

However, our retrospective analysis also finds that posts about using ChatGPT for mental health support, and posts about developing emotional attachments to ChatGPT, both rise steadily in frequency almost immediately after the launch of GPT-4o in May 2024. We show that PuLSE can detect the increase in emotional engagement as early as October 2024 - months before OpenAI made any (public) acknowledgment of this impact. An interactive site to explore our results and methods, updated daily with live data, is available at rchatgpt-pulse.github.io.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The launch of ChatGPT in late 2022 was a watershed moment for consumer AI products: ChatGPT reflected a step-change not only in the capabilities of AI products available to the general public, but in the degree to which any LLM-based product reached widespread consumer adoption. Now, a little more than three years after ChatGPT's launch, this recent history can be studied with the benefit of hindsight. To this end, recent works have sought to understand the realized impact of deploying LLM-based products on domains such as education, labor, and healthcare (e.g., Bastani et al.; Brynjolfsson et al.; Goh et al. ).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Domain-specific evaluations naturally give rise to well-defined measurement targets that can be pre-specified and tracked over time. However, a technology with a user base approaching a billion users will inevitably have unpredictable effects. How might we identify---and study---such effects?

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we turn to social media: beyond adoption, ChatGPT is also unique in the extent to which its rollout has been "online." Its users are highly active on social media---in fact, its early and explosive success can be attributed at least in part to virality on platforms like Twitter/X and Reddit. This makes social media a natural source of data for studying the societal impacts of ChatGPT in particular.^33^3OpenAI employees often interact directly with users online; in fact, Sam Altman and other company leadership have conducted multiple Reddit AMAs ("ask me anything" sessions, where subreddit members can post questions for AMA subjects to reply to). The first appears to have been in 2024.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our approach relies on the core assumption that social media posts from everyday users of a technology reflect those users' perceptions and priorities about that technology---that is, that social media provides signal about "societal impact." However, what those perspectives actually entail is unknown a priori. Our framework thus begins with an unsupervised step to identify potentially-relevant ideas surfaced among all posts. Our key proposal to formalize impact is to explicitly track how these concepts develop over time; this can be quantified by placing temporal behavior in context with known external events, such as model and product releases.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To the best of our knowledge, ours is the first longitudinal analysis of r/ChatGPT over this time period. Our substantive findings in Section 3 tell two parallel stories of adoption. On the one hand, ChatGPT has become normalized as a tool that is a part of users' routine workflows for everyday tasks. On the other, emotional engagement with ChatGPT also emerges as an increasingly compelling use-case; this appears to be driven in large part by the GPT-4o model, which was released in May 2024.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

One natural question is whether we might have known about these impacts sooner---and if so, how. Therefore, in Section 4 we also provide a prospective approach to real-time monitoring, which we call PuLSE (Public and Longitudinal Signals for Evaluation). PuLSE discovers statistically meaningful growth in emotional engagement as early as October 2024---long before OpenAI took any public action regarding the emotional-health impacts of their product (see Appendix A.2 for discussion of what was "known," and by whom, at various points in time).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Data", "weight": 1.0} -->

Data was collected using a mixture of Pushshift and the Reddit API. Posts from r/ChatGPT are collected from December 1, 2022 to November 30, 2025, inclusive. Comment and upvote/downvote counts for all posts were updated in January 2026 using the API. We exclude posts that are deleted, removed, posted by subreddit moderators, or are marked as "not robot indexable." As a lightweight spam filter, we also exclude posts with less than ten words (including title and post body) or two comments.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Data", "weight": 1.0} -->

In total, we work with 137,154 posts, with a median of 107 posts per day (and an average of 125); among the posts we analyze, we have posts from 89,346 unique users (see Appendix A for post volume over time with user information).^44^4This work is classified as not human-subjects research by our institutional IRB, as we are not intervening on the subreddit, nor are we seeking to identify individual users. Reddit cannot be thought of as a truly representative sample of the population of ChatGPT users---e.g., prior work has noted that it skews young, male, white, and educated. It is nevertheless valuable as an approximation of user feedback, especially without access to OpenAI's internal usage data. Throughout this work, when we say "users," we refer to the subset of ChatGPT users who post on r/ChatGPT, with the knowledge that the distribution of such users, and their experiences, is only a highly-imperfect proxy for the population of all ChatGPT users.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Featurization", "weight": 1.0} -->

This work rests on the ability to learn structured, human-interpretable features in an unsupervised fashion from unstructured text data. Formally, a featurization $C$ is a mapping $^{d}\to^{m}$ that represents $m$ features; for a $d$-dimensional representation of some text $X\in^{d}$, the output $C(X)\in^{m}$ quantifies the degree to which that text exhibits each of the $m$ features. We will use $C^{(i)}$ for any $i\in[m]$ to describe how $C$ represents the single feature $i$, so that $C^{(i)}(X)\in$ quantifies the degree to which $X$ exhibits feature $i$; we will sometimes refer to $C^{(i)}(X)$ as the "activation" of $i$ on $X$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Featurization", "weight": 1.0} -->

In some abuse of notation, we will use $X_{s}$ to denote all data from timestep $s$, and $X_{s:t}$ to denote the data from timesteps $s$ to $t$. Throughout this work, we use days as our unit of time, so that each sample $X_{s}$ is a "minibatch" of data from day $s$, and $C^{(i)}(X_{s}):=\frac{1}{|X_{s}|}\sum_{X\in X_{s}}C^{(i)}(X)$ is the average activation for feature $i$ for all texts from day $s$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Featurization", "weight": 1.0} -->

To compute our featurizations, we use sparse autoencoders (SAEs) with the standard reconstruction loss.^55^5That is, we choose $\widehat{C}$ to minimize the normalized MSE $\tfrac{\sum_{X}\|X-\widehat{C}(X))\|_{2}^{2}}{\sum_{X}\|X-\overline{X}\|_{2}^{2}}$, where $\overline{X}$ is the mean of $X$ over the training set. We concatenate post titles and texts, and embed them with OpenAI's text-embedding-3 model. We interpret these features with gpt-4.1-mini, using prompts from the implementation in Movva et al.; see Appendix G. For feature interpretation, we choose the best of three candidates, measured by F1 score.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Retrospective method", "weight": 1.0} -->

We use top-$K$ SAEs with $K=4$ and $M=128$ (128 features total, allowing each sample to associate with 4 features), with samples weighted by $\log(n_{\mathrm{upvotes}}-n_{\mathrm{downvotes}}+n_{\mathrm{comments}})$; see Appendix B for discussion of these design decisions, including consideration of PCA and $k$-means clustering as alternatives.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Retrospective method", "weight": 1.0} -->

After initially computing $M=128$ features, we remove some for focus: generic features, such as ChatGPT at the start of text (9 features); features that had very few positively-labeled samples; and features related to image and video generation or product releases. We annotate all samples with binary labels for the remaining features, using the majority vote from three candidate labels from gpt-4.1-mini.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Retrospective method", "weight": 1.0} -->

Characterizing temporal trajectories. Given a featurization $C$, we compute the historical frequency of any feature $i$ as a transcript $\{C^{(i)}(X_{t})\}_{t\in[T]}$ for feature $i$ at each day $t$. We use the labels from LLM annotation, so that $C^{(i)}(X_{t}):=\frac{1}{|X_{t}|}\sum_{X\in X_{t}}\mathbf{1}{[X\textit{ labeled as }i]}$. We treat the first month as a "burn-in" period and remove posts from those days, so that $T=1034$, and apply a 30-day rolling mean.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Retrospective method", "weight": 1.0} -->

To place all features in context with real-world events, we compile a timeline $\mathcal{T}=\{\tau_{1},\tau_{2},\dots\}$ of events that we may expect to affect the composition of posts online. Using OpenAI's official release notes, we choose twelve major model releases, listed in Table 12. ‣ Appendix F Complete results reference ‣ Three Years of r/ChatGPT: Societal Impact Evaluations from Social Media Data"). With transcripts and the timeline in hand, we can quantify the degree to which particular features evolve over time, and/or are reactive to events in $\mathcal{T}$. Specifically, we assume that, absent any "impact", a feature's frequency should be roughly constant. However, transcripts may suggest evidence of impact in two ways. A change in slope that begins near or shortly after $\tau_{j}$ may reflect an effect of event $j$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Retrospective method", "weight": 1.0} -->

On the other hand, long-run changes in a feature's frequency over the entire period of analysis---i.e., non-zero slope---suggest evidence of changing priorities that are not tied to specific external events, but reflect the progression of adoption more generally.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Retrospective method", "weight": 1.0} -->

To capture the former (reactivity to specific events in $\mathcal{T}$), we model each transcript as piecewise-linear, with candidate changepoints only from $\mathcal{T}$; for each feature $i$, we approximate its transcript at $t$ as with each $\gamma_{j}$ being the change in slope at $\tau_{j}$.^66^6This approach can be thought of as a simplified interrupted time series (ITS) analysis in which exogenous shocks may induce changes in level and/or slope (see, e.g., Box and Tiao; Bernal et al.). A fully-formal ITS approach that includes additional sensitivity and inference procedures, which would allow explicitly "causal" claims to be made (modulo standard ITS identification assumptions, which can be strong), is entirely consistent with our framework; however, doing so is beyond the scope of the current work. We fit Equation for each feature over 100 bootstrap samples, sampling posts with replacement, and report changepoints that are stable, i.e. selected in at least half of the bootstrap samples.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Retrospective method", "weight": 1.0} -->

To capture the latter (slope change over the full horizon), we use an OLS slope test for whether each feature's slope corresponds to at least a 10% change; we Bonferroni-correct over the total number of features, and use Newey-West HAC errors to handle autocorrelation in the time-series. For details of both changepoint fitting and slope tests, see Appendix B.2.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Retrospective method", "weight": 1.0} -->

Finding "families" of related features. While our final results inevitably require manual interpretation, we support our analysis by grouping features into "families" using quantitative methods. For all features $i$, we compute co-occurrences with other features (i.e., which other features appear among posts that are labeled with $i$), and trajectory similarity (i.e., which other features exhibit similar temporal behavior, regardless of co-occurence). We then use these similarities to compute a clustering over features.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Retrospective method", "weight": 1.0} -->

We show our final categorizations in Appendix C. In our data, the vast majority of features characterize either (mundane) adoption (Section 3.1) or emotional engagement (Section 3.2); only six features (of 86) do not fit cleanly into any part of our interpretation.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Retrospective findings", "weight": 1.0} -->

Our retrospective analysis reveals two major stories of adoption, which we present here. (For completeness, the full set of quantitative results from the method described in the previous section is given in Appendix C.)

<!-- chunk {"id": "body-0026", "role": "body", "section": "Retrospective findings", "weight": 1.0} -->

Our first finding is that ChatGPT has become normalized as a regular consumer technology (3.1). While this finding is likely broadly consistent with many readers' personal experiences, we highlight the degree to which it is visible in our data---across features about usage, user perspectives, and linguistic cues.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Retrospective findings", "weight": 1.0} -->

Our second main finding, previewed in Figure 2 and described further in Section 3.2, is more striking: the frequency of posts broadly related to emotional engagement---using ChatGPT for mental health support, or developing emotional attachments to models, for instance---began to rise in May 2024, shortly after the release of GPT-4o. This effect is visible long before the emotional and mental health aspects of LLM product usage had entered the public consciousness, and long before OpenAI publicly committed to any action regarding mental health implications of its product.

<!-- chunk {"id": "body-0028", "role": "body", "section": "The \"domestication\" of ChatGPT", "weight": 1.0} -->

Our first high-level finding is that, broadly speaking, r/ChatGPT dynamics illustrate the ways in which the ChatGPT product has become normalized as a consumer technology. We borrow the term "domestication" from science and technology studies (STS), where it is a well-studied theory that describes the processes by which novel technologies are absorbed into everyday use (see, e.g., Haddon ).^77^7In STS, the word choice of "domestication" is meant to evoke the sense of something "wild" and strange having been "tamed"; see discussion in Haddon. It is useful to keep in mind a key conceptual framing from this theory: posts on r/ChatGPT at any given time reflect what users feel is "worth posting about" at that point in time, and changes in the frequency of posts about different topics reflect changes in users' beliefs about postworthiness.

<!-- chunk {"id": "body-0029", "role": "body", "section": "The \"domestication\" of ChatGPT", "weight": 1.0} -->

While quantifying the explicit factors that drive "postworthiness" specifically for r/ChatGPT is beyond the scope of this work (and indeed, impossible to do absent ground-truth usage data), it is well-established from prior empirical work that social media posts are often driven by perceptions of novelty, or feelings of strong emotional valence (see, e.g., Vosoughi et al.; Wu and Huberman; Yu et al. ). Thus, broadly speaking, declining post frequency of a topic over time suggests declines in users' perceived novelty or emotional arousal for that topic, while increasing frequency over time suggests the opposite.

<!-- chunk {"id": "body-0030", "role": "body", "section": "The \"domestication\" of ChatGPT", "weight": 1.0} -->

Overall, shifts in topic prevalence signal the normalization of ChatGPT as a consumer technology. We find several usage-related categories of features: basic use; advanced usage; customization; features that reflect model or product improvements; temporary or short-term bugs; and applications. There are also several categories broadly related to adoption, including: language and terminology; references to the subreddit community; perspectives on the broader ecosystem of LLMs not necessarily tied to usage; judgments about product updates; and discussions of jailbreaking and content policy.

<!-- chunk {"id": "body-0031", "role": "body", "section": "The \"domestication\" of ChatGPT", "weight": 1.0} -->

Here, we briefly highlight some examples to illustrate the "domestication" story; see Tables 3 ‣ Appendix C Supporting materials for main results ‣ Three Years of r/ChatGPT: Societal Impact Evaluations from Social Media Data") and 4 ‣ Appendix C Supporting materials for main results ‣ Three Years of r/ChatGPT: Societal Impact Evaluations from Social Media Data") in Appendix C for all "domestication"-related features and more detailed quantitative results.

<!-- chunk {"id": "body-0032", "role": "body", "section": "The \"domestication\" of ChatGPT", "weight": 1.0} -->

Increasing expert (and declining basic) product usage. The frequency of posts related to questions about basic product use (e.g., login problems) decrease over the three-year window of time, while features that suggest advanced and frequent usage (e.g., organizing or searching chat histories) increase. Furthermore, while requests for help is a somewhat-generic feature, examining trends within the 5568 posts that were labeled with this feature reveals a shift in user expectations around product usage.

<!-- chunk {"id": "body-0033", "role": "body", "section": "The \"domestication\" of ChatGPT", "weight": 1.0} -->

Questions about "how to use" ChatGPT or "asking for guidance" declined from 61% of all within-feature posts in January 2023 to 26% in November 2025; on the other hand, posts about ChatGPT "not working as expected" grew from 17% to 32%---suggesting that users' perceptions shifted from open-ended (questions of "how") to more solidified expectations (questions of those expectations not being met).^88^8To arrive at these sub-features, we train a SAE with $M=4$ and $K=1$ (in other words, to find four features with each post corresponding only to one feature) for the $5568$ posts labeled as requests for help, and label each post with the corresponding sub-features. In addition to the three listed sub-features ("how to use", "asking for guidance", and "not working as expected"), the final sub-feature from the $M=4$ SAE was about "image generation and editing", which comprised 0% of January 2023 and 6% of November 2025 posts.

<!-- chunk {"id": "body-0034", "role": "body", "section": "The \"domestication\" of ChatGPT", "weight": 1.0} -->

26% of all posts labeled as request for help were not well-described by any of the four sub-features. These changes are not just about whether new users are still coming to the product or subreddit---in fact, we know from usage data that growth has yet to slow---but about the expectations that change as more users develop expertise.

<!-- chunk {"id": "body-0035", "role": "body", "section": "The \"domestication\" of ChatGPT", "weight": 1.0} -->

Declines in application-specific posts. Posts about applications (e.g., programming or D&D and role-playing games) also decline. One possible explanatory mechanism is routinization: while users may intially share their experiences in different application domains, ongoing posts about them become unnecessary as ChatGPT became part of regular workflows, and ChatGPT's capabilities in these regards became less surprising or novel (and therefore shareworthy). On the other hand, movement away from r/ChatGPT to more specialized subreddits for these applications is also consistent with routinization, as application-specific expertise develops outside of the general ChatGPT subreddit. A notable exception to the overall trend of declines in applications is a substantial increase in discussion of medical conditions or diagnoses; as we will discuss in Section 3.2, this is driven by its close relationship with emotional engagement features.

<!-- chunk {"id": "body-0036", "role": "body", "section": "The \"domestication\" of ChatGPT", "weight": 1.0} -->

Language usage suggests familiarization. Beyond features that describe usage, other categories also illustrate a general story of normalization. For instance, early users often compared ChatGPT to google search, while later users no longer found that reference point important. Usage of "bot" or "chatbot" in reference to ChatGPT declines substantially, suggesting an overall familiarization with ChatGPT specifically, as opposed to a generic chatbot product. Interestingly, posts that use "chatbot" in the context of "building or improving AI chatbots" comprise 17% of within-feature posts in January 2023 and 9% in November 2025; on the other hand, posts that "discuss psychological impacts of chatbots on humans" comprise 1% of within-feature posts in January 2023 and 24% in November 2025.^99^9As above, we train a SAE with $M=4$ and $K=1$ for each of the 2446 posts labeled as mentions "bot" or "chatbot"; in addition to the two identified sub-features above, the remaining sub-features are "user complaints or frustrations", and "expressions of anger".

<!-- chunk {"id": "body-0037", "role": "body", "section": "The \"domestication\" of ChatGPT", "weight": 1.0} -->

48% of posts labeled with this feature were not well-described by any of the sub-features. While the overall decline in "chatbot" usage suggests familiarization, the compositional shift within this feature suggests that usage of this defamiliarized framing is increasingly done in the context of raising concerns; this is especially notable as meta-discussion of emotional impact does not appear to be a substantial topic of conversation on the subreddit overall.

<!-- chunk {"id": "body-0038", "role": "body", "section": "The \"domestication\" of ChatGPT", "weight": 1.0} -->

Evolving user perspectives: declines in speculation, increases in privacy concerns. At the same time, predictions about future development and capabilities and discussions about how LLMs represent knowledge fall substantially. Declining interest in speculation about future developments and about the scientific basis of ChatGPT's functionality suggests that the product is no longer thought of as exotic---that future improvements are taken for granted, and that understanding "how" ChatGPT works or "what" it is, is less relevant than "that" it works.^1010^10In fact, domestication theory claims that when a technology is novel, users are interested in understanding, defining and contextualizing what it is; these questions become less important as adoption continues. On the other hand, privacy concerns grow, as users share more personal information and use the product for increasingly intimate applications; as we will discuss in Section 3.2, this often takes the form of emotional engagement.

<!-- chunk {"id": "body-0039", "role": "body", "section": "The emergence of emotional engagement", "weight": 1.0} -->

Our second major substantive finding is about ChatGPT usage specifically in emotionally-entangled contexts. While these features had been present prior to the GPT-4o release---previewing our results from Section 4, features related to therapy and emotional attachment appear as early as March 2023---their prevalences begin to grow dramatically after the release of GPT-4o in May 2024.

<!-- chunk {"id": "body-0040", "role": "body", "section": "The emergence of emotional engagement", "weight": 1.0} -->

A clear family of "emotional engagement" features emerges across trajectories, and co-occurrences, with GPT-4o as a critical inflection point. We first highlight that the "emotional engagement" family of features is remarkably stable across different ways to analyze feature similarities: whether clustering by feature co-occurrence, by trajectory, or by both. The two core features that anchor this family are personal attachments and therapy, as shown in Figure 2; both of these features have stable changepoints at May 13, 2024---the GPT-4o release date---after which their slopes, i.e. feature frequencies, increase.

<!-- chunk {"id": "body-0041", "role": "body", "section": "The emergence of emotional engagement", "weight": 1.0} -->

The full family of features also includes personal stories about positive impact, which also has a stable changepoint at the GPT-4o release; naming ChatGPT and romantic partners, both of which have statistically significant positive slopes; and poetic language and AI sentience, both of which have stable changepoints at July 30, 2024 (the release of Advanced Voice Mode, and the next entry in $\mathcal{T}$ after the GPT-4o release).^1111^11As mentioned in Section 2, we are not making causal claims in a formal sense, especially given that many product releases may be related; however, that so many "emotional engagement" features have a best-fit changepoint in this time period is striking.

<!-- chunk {"id": "body-0042", "role": "body", "section": "The emergence of emotional engagement", "weight": 1.0} -->

In Figure 3, we show features that we categorize as related to "emotional engagement," along with some representative example posts for each feature; note that the poetic language feature describes long, AI-generated prose narratives (rather than user-written content). In Appendix C.2 ‣ Appendix C Supporting materials for main results ‣ Three Years of r/ChatGPT: Societal Impact Evaluations from Social Media Data"), we provide more quantitative details and list additional features that at least one of our quantitative methods groups with this category.

<!-- chunk {"id": "body-0043", "role": "body", "section": "The emergence of emotional engagement", "weight": 1.0} -->

Therapy and companion capture distinct concepts. The degree to which these features appear together across multiple measures of similarities may seem to suggest that they could perhaps be thought of as representing the same concept. To the contrary, however, they are quite distinct. While therapy has 2253 unique posts from 2052 unique users, and companion has 2926 posts from 2665 users, the number of posts labeled as both is only 364, and the number of users who have ever posted about both is 446---thus, while these features have more overlap than most other pairs of features, the absolute degree of overlap is small.

<!-- chunk {"id": "body-0044", "role": "body", "section": "The emergence of emotional engagement", "weight": 1.0} -->

On a content level, basic vocabulary analysis (log-odds ratio; Monroe et al. ) also confirms semantic differences: therapy posts are more likely to include words like mental/health ($z$-score 18.8 and 18.1, respectively), help (16.2), support (14.3), trauma (11.1), anxiety (10.8), issues (10.5), and advice (10.5). On the other hand, companion posts contain words like personality ($z$-score 17.4), feels (14.6), human(s) (13.8), conversation (11.9), and friend (9.7); see Table 7 ‣ Appendix C Supporting materials for main results ‣ Three Years of r/ChatGPT: Societal Impact Evaluations from Social Media Data") for full lists of the most distinctive words for each feature.

<!-- chunk {"id": "body-0045", "role": "body", "section": "The emergence of emotional engagement", "weight": 1.0} -->

Posts about either therapy or companionship also exhibit distinct "profiles" in terms of what other features they tend to exhibit. In Table 1, we examine what other features are likely to co-occur with posts about therapy or companionship (excluding posts that are tagged as both). For instance, 20% and 4.9% of posts about therapy and companionship, respectively, are also tagged as personal stories about positive impact, which comprise 1.8% of all posts. While both exhibit a substantial "lift" for this feature, the lift for therapy features is over 4 times greater than for companion features. Interestingly, while therapy posts are over twice as likely to also mention privacy concerns compared to the baseline rate, companion posts are less than one third as likely. On the other hand, therapy posts are less than half as likely as baseline to either name ChatGPT or discuss AI sentience, while companion posts are 4.5 and 3.5 times more likely, respectively. Interestingly, companion posts are more than twice as likely as therapy posts to mention recent quality declines, suggesting that the former use case is more sensitive to model updates than the latter.

<!-- chunk {"id": "body-0046", "role": "body", "section": "The emergence of emotional engagement", "weight": 1.0} -->

$\frac{\textit{therapy}}{\textit{companion}}$ ratio recent quality decline Table 1: How frequently therapy-only and companion-only posts also exhibit other features (rows). Rate shows overall prevalence; lifts (×) show how much more frequently each column feature co-occurs with each row feature, compared to all posts. “Ratio” column compares therapy ÷ companion; 95% CIs for ratio, modeling counts as Bernoulli trials, shown in parentheses.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Emotional engagement shapes the trajectories of other features after GPT-4o release", "weight": 1.0} -->

Finally, we show that emotional engagement shapes the evolution of many other features, even when they do not appear to be overtly related to emotional engagement. For example, among posts that are asking about daily or repeated usage of ChatGPT, we find sub-features related to managing prompts, paid tiers, productivity, and personal and emotional disclosures. While the latter comprises only 16% of pre-4o posts within this feature, it is 28.8% of post-4o posts. Similarly, posts about the positive impact of ChatGPT are mainly about productivity and mental health; however, while the former exhibits no significant change before and after the launch of 4o (23%), the latter comprises 14% of all pre-4o posts and 41% of post-4o posts.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Emotional engagement shapes the trajectories of other features after GPT-4o release", "weight": 1.0} -->

The degree to which emotional engagement is a driver of ChatGPT usage is particularly pronounced when observing features which spike in the week after the GPT-5 release. Within this period, three of the top four features are complaints about GPT-5: frustration or hatred about a product version (598, or 12.2% of all posts), dissatisfaction with 4o removal and loss of control (552, 11.3%), and lost, deleted, or missing conversations (370, 7.6%); in total, 27.2% of all posts are labeled with at least one of these three features.^1212^12The second most frequent feature is pricing and free vs paid comparisons (582, 11.9%). This time period also experienced high post volume overall (4898 posts total, averaging 700 posts per day, compared to an average of 125 per day over all three years).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Emotional engagement shapes the trajectories of other features after GPT-4o release", "weight": 1.0} -->

Among these posts, 164 are also labeled with either therapy or companionship; analyzing the sub-features of dissatisfaction and lost conversations features yields an additional 242 posts that also involve emotional engagement but were not already counted in the previous 164.^1313^13The $M=4,K=1$ SAE for frustration or hatred did not have sub-features related to emotional engagement. For posts tagged with dissatisfaction with 4o removal and loss of control but not therapy or companion, 169 posts mention critiques of emotional limitations placed on models or emotional narratives about companion-like relationships (the remaining two sub-features are retiring Standard Voice Mode and mentions 4o). For lost, deleted, or missing conversations, 73 posts mention the sub-feature grief, mourning, or emotional loss (with the remaining sub-features being about UI features; sidebar features; and deletions). Thus, in total, emotional engagement is involved in at least 30.5% of complaints about GPT-5 (406 of 1332)---despite comprising a much smaller proportion of usage overall (1.8%, according to Chatterji et al. ).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Emotional engagement shapes the trajectories of other features after GPT-4o release", "weight": 1.0} -->

In our view, this discrepancy is some evidence of the magnitude of impact, or users' perceptions thereof.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Real-time monitoring with PuLSE", "weight": 1.0} -->

Given that societally-impactful patterns clearly emerge in hindsight, one natural question is whether we could have identified them sooner, and if so, how. In this section, we present PuLSE, a simple online monitoring approach that ensures both accuracy, in that it provides high-quality descriptions of subreddit content at any given time, and timeliness, in that it raises alerts when topics of interest change significantly.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Real-time monitoring with PuLSE", "weight": 1.0} -->

Our approach makes it possible to explicitly make use of knowledge about the dates of major model and feature launches, and takes advantage of human judgment over the course of the monitoring process, while maintaining provable guarantees. In Section 4.1, we give our high-level method and corresponding (informal) guarantees, and in Section 4.2, we show concrete results from applying this method to the data studied in Section 3. All proofs and formal statements of algorithms and results are given in Appendix D.

<!-- chunk {"id": "body-0053", "role": "body", "section": "PuLSE: Public and Longitudinal Signals for Evaluation", "weight": 1.0} -->

The backbone of PuLSE is a simple online monitoring algorithm that continually analyzes new data that arrives over time, and places it in context with prior observations. At every point in time $t$, we maintain a candidate featurization ${\widehat{C}_{\textrm{curr}}}$ that describes the current state of the data, as well as a set $S_{t}$ of "features of interest" that are currently being monitored. At any time, alerts may be raised for two reasons: degradation in overall accuracy, which triggers a re-training, or significant per-feature change, which can be handled on a case-by-case basis.

<!-- chunk {"id": "body-0054", "role": "body", "section": "PuLSE: Public and Longitudinal Signals for Evaluation", "weight": 1.0} -->

To track each of these goals, our method utilizes anytime-valid sequential hypothesis tests; these techniques provide a principled way to handle online streams of data. A sequential hypothesis test begins with a null hypothesis $\mathcal{H}_{0}$, then continually updates its internal state as new data arrives. A sequential hypothesis test is anytime-valid when, for a prespecified error rate $\alpha$, the likelihood that the test ever falsely rejects the null when the null is true is at most $\alpha$, even when given infinitely-many samples of data.^1414^14For the interested reader, further relevant material can be found, e.g., Ramdas and Wang. Altogether, PuLSE is summarized in Algorithm 1.

<!-- chunk {"id": "body-0055", "role": "body", "section": "PuLSE: Public and Longitudinal Signals for Evaluation", "weight": 1.0} -->

Input: Initial data Xinit; featurization algorithm 𝒜 1 Initialize accuracy test and feature tests; compute initial featurization Ĉcurr:= 𝒜(Xinit) 2 while new data Xt arrives do 3 if model or feature release at time t then 4 optionally reset tests 6 if accuracy test rejects with data Xt then 7 alert and update Ĉcurr and examine feature diffs; 8 start new accuracy test for current featurization 9 if there are active feature tests then 10 if feature tests reject then 11 alert (potentially, take other action) 13 optionally reset them, do nothing, or replace them Algorithm 1 Online monitoring with anytime-valid tests (formal statement in Algorithm 5) For the purposes of exposition in this section, we introduce some additional notation. A featurization algorithm $\mathcal{A}:\mathcal{X}\to\mathcal{C}$ takes in a set of data and computes a single featurization.

<!-- chunk {"id": "body-0056", "role": "body", "section": "PuLSE: Public and Longitudinal Signals for Evaluation", "weight": 1.0} -->

Featurization error ${\mathrm{err}}:\mathcal{C}(\mathcal{X})\to$ quantifies the quality of a featurization $C$ on a set of data $X$; for SAEs, for example, this is reconstruction error.

<!-- chunk {"id": "body-0057", "role": "body", "section": "PuLSE: Public and Longitudinal Signals for Evaluation", "weight": 1.0} -->

Establishing a baseline. Before the monitoring period begins, we begin with a featurization trained with an initial set of data $\widehat{C}_{0}=\mathcal{A}(X_{\text{init}})$, and compute its error $\varepsilon_{0}={\mathrm{err}}(C_{0}(X_{\text{init}}))$; we will let ${\widehat{C}_{\textrm{curr}}}=\widehat{C}_{0}$ and $\varepsilon_{curr}=\varepsilon_{0}$. Based on this initial featurization, we can also identify a set of initial features $S_{0}$ to monitor, or otherwise let $S_{0}=\emptyset$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "PuLSE: Public and Longitudinal Signals for Evaluation", "weight": 1.0} -->

Accuracy. To maintain good accuracy over the entire time horizon, we maintain a hypothesis test for whether the error of ${\widehat{C}_{\textrm{curr}}}$ on new data is close to the error of ${\widehat{C}_{\textrm{curr}}}$ on the data with which it was trained. That is, we test the following null hypothesis for some $\beta\geq 1$: For any time $t$ at which $\mathcal{H}_{0}^{\mathrm{acc}}$ is rejected, a new featurization is recomputed on all data seen thus far.

<!-- chunk {"id": "body-0059", "role": "body", "section": "PuLSE: Public and Longitudinal Signals for Evaluation", "weight": 1.0} -->

${\widehat{C}_{\textrm{curr}}}$ is updated as ${\widehat{C}_{\textrm{curr}}}:=\mathcal{A}(X_{1:t})$, the error benchmark is updated $\varepsilon_{curr}:={\mathrm{err}}({\widehat{C}_{\textrm{curr}}}(X_{1:t}))$, and the procedure continues with the null in updated with new values. We will sometimes refer to such a $t$ as a "reject and retrain" timestep, and use $\widehat{C}_{s}$ to denote the $s$-th featurization.

<!-- chunk {"id": "body-0060", "role": "body", "section": "PuLSE: Public and Longitudinal Signals for Evaluation", "weight": 1.0} -->

Qualitatively, a rejection at time $t$ means that the previous featurization ${\widehat{C}_{\textrm{curr}}}$ is no longer a high-quality representation of the most important features observed in all data up to $t$; in other words, the data stream has changed substantially. Thus, at the time of rejection, the most salient changes can also be computed---which features from the previous featurization stayed the same; which merged or split; or which became obsolete (in favor of entirely new features). Features tracked in $S_{t}$ should also be revisited at "reject and retrain" timesteps, either updating to the new representations or choosing different features altogether.

<!-- chunk {"id": "body-0061", "role": "body", "section": "PuLSE: Public and Longitudinal Signals for Evaluation", "weight": 1.0} -->

One important detail is the level $\alpha$ at which each test is run. For a single hypothesis test, $\alpha$ straightforwardly controls the expected Type I error, but some care must be taken when multiple tests are run consecutively. Specifically, the level $\alpha_{s}$ at which the $s$-th test is run must be set with an appropriate schedule; as long as this occurs, we have the following guarantee.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Application results", "weight": 1.0} -->

We now show the results of applying this framework to the data analyzed in Section 3. Within this section, we use SAEs with $M=64$. We fit the initial featurization $\widehat{C}_{0}$ with data from the first 16 weeks after ChatGPT's release. For both accuracy and feature monitoring, we use tolerance $\beta=1.05$ and target $\alpha=0.1$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Application results", "weight": 1.0} -->

Accuracy. Overall, our approach effectively maintains a sufficiently-accurate ${\widehat{C}_{\textrm{curr}}}$ over time. In Figure 4, we show the reconstruction error of the ${\widehat{C}_{\textrm{curr}}}$ maintained by our approach, compared to the reconstruction error of the "best-in-hindsight" $C_{\star}$, which was trained with all data at once, as well as the initial featurization $\widehat{C}_{0}$ computed on only $X_{\text{init}}$. "Reject and retrain" events occur on September 9, 2023; April 4, 2024; and April 18, 2025. That there are only three such events indicates that posts can be described by fairly stable representations over time, and validates that frequently re-computing featurizations is unnecessary.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Application results", "weight": 1.0} -->

The evolution of featurizations overall are broadly consistent with known external changes and with the in-hindsight clusterings (see Appendix B.4 for details on how we compare featurizations over time). For instance, between $\widehat{C}_{0}$ and $\widehat{C}_{1}$, two new features emerge corresponding to plugins and the ChatGPT API, both of which were product updates from March 2023; between $\widehat{C}_{1}$ and $\widehat{C}_{2}$, a feature corresponding to controversy, danger, or bans disappears, while one for low-quality AI-generated content emerges; between $\widehat{C}_{2}$ and $\widehat{C}_{3}$, meanwhile, features corresponding to Google Bard and medical topics disappear, while features corresponding to Gemini and personalized image requests emerge.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Application results", "weight": 1.0} -->

In Appendix E, we summarize all new and obsolete features across updates to ${\widehat{C}_{\textrm{curr}}}$ (Table 8), and visualize some examples of feature evolutions across featurization updates (Figure 10).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Application results", "weight": 1.0} -->

Feature monitoring. We would also like to monitor for changes within features, even when its overall representation in the featurization remains constant. Several features that may seem to be societally-impactful already emerge after the initial featurization $\widehat{C}_{0}$ computed in March 2023, including one feature explicitly about using ChatGPT as a therapist. For each featurization, we (manually) select the features that are most closely related to therapy as test candidates. We test for changes in the frequency of posts with non-zero activations; in Figure 5 (and Table 9), we show outcomes for various configurations (start dates, representations, and Bonferroni correction over $|S_{t}|$).

<!-- chunk {"id": "body-0067", "role": "body", "section": "Application results", "weight": 1.0} -->

Our alerts for the feature corresponding to therapy are raised as early as October 29, 2024. As we discuss in Appendix A.2, this is months earlier than OpenAI or the public seemed to be aware of psychological impact. Notably, the quality of feature representations does appear to affect alert times. Using representations $\widehat{C}_{0}$, no tests result in alerts, likely because the representations of the "therapy" feature in $\widehat{C}_{0}$ are too weak, or otherwise not fully capturing characteristics of later posts about therapy. (No tests result in alerts even for $n=1$; the bottleneck is the representation, rather than the testing of multiple features simultaneously.)

<!-- chunk {"id": "body-0068", "role": "body", "section": "Application results", "weight": 1.0} -->

On the other hand, while alerts for gratitude towards ChatGPT (using the $\widehat{C}_{1}$ representations) would have been raised at similar times to the $\widehat{C}_{2}$ therapy feature, it is unclear that, at the time, gratitude would have been considered a societally-relevant feature of interest; monitoring for the medical and psychological advice feature, meanwhile, would have led to delayed alert times. Varying the number of simultaneously-monitored features (i.e., Bonferroni correction) has only a modest effect on alert timing, typically shifting dates by a few weeks for tests with strong representations. The dominant factors are the quality of the underlying representations and the strength of the actual trend.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Discussion", "weight": 1.5} -->

The time period studied in this paper---December 2022 to November 2025---is a unique moment in recent history in which consumers were introduced to, then quickly adapted to, a genuinely-unprecedented type of technology. While Section 3.1 tells a story of adoption that may seem mundane in hindsight, Section 3.2 also suggests that emotional engagement is a crucial dimension of adoption that evolved in parallel. Of course, there is more to see: r/ChatGPT is an incredibly rich set of data, and there are a wide range of relevant further questions---such as more detailed analysis of emotional engagement or the development of intra-subreddit community norms---that we hope future work will explore.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Discussion", "weight": 1.5} -->

More generally, this work can be seen as a proof-of-concept for an approach to AI evaluation that makes use of public feedback. We began from the perspective that it is worth paying attention to what everyday users have to say about their experiences with real-world AI products. While analyzing such data has long been a cornerstone of the social sciences, we argue that feedback from the general public is not only sociologically interesting, but also a crucial means for identifying "unknown unknowns" in societally-consequential consumer AI products. While social media is one natural way to collect this type of data, it is worth considering the possibility of platforms that are purpose-built to seek feedback for evaluation directly, especially in light of recent regulatory movement towards allowing individuals to contest or report their experiences with AI systems.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Discussion", "weight": 1.5} -->

Better information can lead to better decisions. Understanding how users may be experiencing AI products---especially in unexpected ways, and especially in real time---is a pathway to steering the societal impact of these technologies, rather than reacting to them in hindsight. OpenAI's initial choice in August 2025 to sunset GPT-4o in favor of the "colder" GPT-5 was clearly deliberate, but the strength of users' emotional responses upon the GPT-5 release suggests that OpenAI's expectations were miscalibrated. Yet, as the previous sections show, meaningful signal about emotional engagement existed well before GPT-5. Counterfactual outcomes will always be unknown, and we make no claim about what should have been done with that information. We do claim that the information was there---if anyone had been paying attention. Perhaps, in the future, we should do exactly that.
