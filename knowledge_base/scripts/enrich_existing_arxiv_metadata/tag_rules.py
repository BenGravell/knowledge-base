"""Tag derivation rules for arXiv records."""

from __future__ import annotations

from knowledge_base.utils.arxiv_utils import ArxivRecord

CATEGORY_TAGS = {
    "cs.AI": "Artificial intelligence",
    "cs.AR": "Computer architecture",
    "cs.CC": "Computational complexity",
    "cs.CE": "Computational engineering",
    "cs.CG": "Computational geometry",
    "cs.CL": "Natural language processing",
    "cs.CR": "Cryptography and security",
    "cs.CV": "Computer vision",
    "cs.CY": "Computers and society",
    "cs.DB": "Databases",
    "cs.DC": "Distributed computing",
    "cs.DL": "Digital libraries",
    "cs.DM": "Discrete mathematics",
    "cs.DS": "Data structures and algorithms",
    "cs.ET": "Emerging technologies",
    "cs.FL": "Formal languages",
    "cs.GL": "General literature",
    "cs.GR": "Computer graphics",
    "cs.GT": "Game theory",
    "cs.HC": "Human-computer interaction",
    "cs.IR": "Information retrieval",
    "cs.IT": "Information theory",
    "cs.LG": "Machine learning",
    "cs.LO": "Logic in computer science",
    "cs.MA": "Multiagent systems",
    "cs.MM": "Multimedia",
    "cs.MS": "Mathematical software",
    "cs.NA": "Numerical analysis",
    "cs.NE": "Neural computing",
    "cs.NI": "Networking",
    "cs.OH": "Other computer science",
    "cs.OS": "Operating systems",
    "cs.PF": "Performance",
    "cs.PL": "Programming languages",
    "cs.RO": "Robotics",
    "cs.SC": "Symbolic computation",
    "cs.SD": "Sound",
    "cs.SE": "Software engineering",
    "cs.SI": "Social and information networks",
    "cs.SY": "Systems and control",
    "eess.AS": "Audio and speech processing",
    "eess.IV": "Image and video processing",
    "eess.SP": "Signal processing",
    "eess.SY": "Systems and control",
    "math.OC": "Optimization and control",
    "math.NA": "Numerical analysis",
    "math.PR": "Probability",
    "math.ST": "Statistics theory",
    "stat.ML": "Machine learning",
    "stat.TH": "Statistics theory",
}

KEYWORD_TAGS = (
    ("reinforcement learning", "Reinforcement learning"),
    ("imitation learning", "Imitation learning"),
    ("inverse reinforcement learning", "Inverse reinforcement learning"),
    ("optimal control", "Optimal control"),
    ("model predictive control", "Model predictive control"),
    ("trajectory optimization", "Trajectory optimization"),
    ("motion planning", "Motion planning"),
    ("path planning", "Path planning"),
    ("diffusion", "Diffusion models"),
    ("transformer", "Transformers"),
    ("large language model", "Large language models"),
    ("foundation model", "Foundation models"),
    ("neural network", "Neural networks"),
    ("deep learning", "Deep learning"),
    ("graph neural", "Graph neural networks"),
    ("bayesian", "Bayesian methods"),
    ("convex optimization", "Convex optimization"),
    ("nonconvex", "Nonconvex optimization"),
    ("stochastic optimization", "Stochastic optimization"),
    ("linear quadratic", "Linear quadratic control"),
    ("lyapunov", "Lyapunov methods"),
    ("safety", "Safety"),
    ("safe", "Safety"),
    ("robust", "Robustness"),
    ("uncertainty", "Uncertainty"),
    ("gaussian process", "Gaussian processes"),
    ("markov decision process", "Markov decision processes"),
    ("mdp", "Markov decision processes"),
    ("partially observable", "Partial observability"),
    ("pompd", "Partial observability"),
    ("multi-agent", "Multi-agent systems"),
    ("multiagent", "Multi-agent systems"),
    ("autonomous driving", "Autonomous driving"),
    ("robot", "Robotics"),
    ("quadrotor", "Aerial robotics"),
    ("aerial", "Aerial robotics"),
    ("vehicle", "Vehicles"),
)


def build_tags(record: ArxivRecord) -> list[str]:
    tags: list[str] = []
    for category in record.categories:
        tag = CATEGORY_TAGS.get(category)
        if tag and tag not in tags:
            tags.append(tag)
    corpus = f"{record.title} {record.abstract}".lower()
    for needle, tag in KEYWORD_TAGS:
        if needle in corpus and tag not in tags:
            tags.append(tag)
    return tags[:12]
