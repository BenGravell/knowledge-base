"""Data tables for algorithm-label validation."""

import re

_URL_RE = re.compile(r"\b(?:https?://|ftp://|www\.)[^\s<>()]+", re.IGNORECASE)

_GENERIC_ALGORITHM_VALUES = {
    "ai",
    "algorithm",
    "algorithms",
    "approach",
    "architecture",
    "basis",
    "conservative",
    "constraints",
    "control",
    "deployment",
    "descent",
    "design",
    "did",
    "different",
    "efficient",
    "estimation",
    "fast",
    "feedback",
    "flow",
    "framework",
    "gradient",
    "guarantee",
    "hessian",
    "inference",
    "interface",
    "iteration",
    "learning",
    "metric",
    "method",
    "methods",
    "mixing",
    "model",
    "models",
    "need",
    "noising",
    "optimization",
    "past",
    "planning",
    "plus",
    "policy",
    "regret",
    "robotics",
    "scale",
    "search",
    "series",
    "sparsity",
    "space",
    "stability",
    "strategy",
    "survey",
    "systems",
    "tasks",
    "transforms",
    "transport",
    "vehicles",
    "work",
}

_BROAD_ALGORITHM_FAMILY_LABELS = {
    "gradientdescent": "Gradient Descent",
    "linearquadraticcontrol": "Linear Quadratic Control",
    "linearquadraticregulator": "Linear Quadratic Regulator",
    "lqr": "LQR",
    "modelpredictivecontrol": "Model Predictive Control",
    "modelpredictivepathintegral": "Model Predictive Path Integral",
    "modelpredictivepathintegralcontrol": "Model Predictive Path Integral Control",
    "mpc": "MPC",
    "mppi": "MPPI",
    "newtonmethod": "Newton Method",
    "newtonsmethod": "Newton's Method",
    "policygradient": "Policy Gradient",
    "trajectoryoptimization": "Trajectory Optimization",
}

_BROAD_ALGORITHM_FAMILY_ORIGIN_ENTRIES = {
    ("gradientdescent", "1847_cauchy_methode_generale_pour_la"),
}

_BARE_ALGORITHM_LABEL_ALLOWED_ENTRIES = {
    ("rrt*", "2011_karaman_anytime_motion_planning_using"),
}

_ALGORITHM_DESCRIPTIVE_WORDS = {
    "analysis",
    "application",
    "applications",
    "benchmark",
    "benchmarking",
    "case",
    "comparison",
    "comparative",
    "convergence",
    "control",
    "controller",
    "extension",
    "framework",
    "improvement",
    "interpretation",
    "learning",
    "method",
    "modification",
    "optimization",
    "robust",
    "robustness",
    "sampling",
    "scheme",
    "study",
    "survey",
    "template",
    "templates",
    "theory",
    "variant",
    "variants",
}

_ALGORITHM_EXPANDED_NAMES = {
    "adam": ("adam",),
    "ddp": ("differential dynamic programming",),
    "ddpg": ("deep deterministic policy gradient",),
    "ddpm": ("denoising diffusion probabilistic models",),
    "dqn": ("deep q-network", "deep q network"),
    "gradientdescent": ("gradient descent methods",),
    "ilqr": ("iterative linear quadratic regulator",),
    "linearquadraticcontrol": ("linear quadratic control",),
    "linearquadraticregulator": ("linear quadratic regulator",),
    "lqr": (
        "linear quadratic regulator",
        "linear quadratic regulators",
        "linear quadratic control",
    ),
    "modelpredictivecontrol": ("model predictive control",),
    "modelpredictivepathintegral": (
        "model predictive path integral",
        "model predictive path integral control",
    ),
    "mppi": (
        "model predictive path integral",
        "model predictive path integral control",
    ),
    "mpc": ("model predictive control",),
    "mpcc": ("model predictive contouring control",),
    "newtonmethod": ("newton method", "newton methods", "newton's methods"),
    "newtonsmethod": ("newton method", "newton methods", "newton's methods"),
    "policygradient": (
        "policy gradients",
        "policy gradient methods",
        "policy gradient algorithms",
    ),
    "ppo": ("proximal policy optimization",),
    "rrt": ("rapidly-exploring random tree", "rapidly-exploring random trees"),
    "rrt*": ("rrt*", "rapidly-exploring random tree star"),
    "sac": ("soft actor-critic", "soft actor critic"),
    "sam": ("sharpness-aware minimization",),
    "spynet": ("spatial pyramid network",),
    "svrpg": ("stochastic variance-reduced policy gradient",),
    "td3": ("twin delayed deep deterministic policy gradient",),
    "trajectoryoptimization": (
        "trajectory optimization",
        "trajectory optimization methods",
    ),
}

_ALGORITHM_RELATIONAL_CUES: tuple[tuple[str, str, str], ...] = (
    (
        "preconditioned-gradient interpretation",
        r"{name}[^.\n]{0,140}\bas\s+(?:a\s+)?preconditioned\s+gradient\s+descent\b|"
        r"\bpreconditioned\s+gradient\s+descent\b[^.\n]{0,140}{name}",
        "{algorithm} preconditioned-gradient analysis",
    ),
    (
        "low-frequency sampling",
        r"\blow[-\s]+frequency\s+sampling\b[^.\n]{0,100}{name}|"
        r"{name}[^.\n]{0,100}\blow[-\s]+frequency\s+sampling\b",
        "{algorithm} low-frequency sampling",
    ),
    (
        "learning-based optimization",
        r"\blearning\s+to\s+optimi[sz]e\b[^.\n]{0,100}{name}|"
        r"{name}[^.\n]{0,100}\blearn(?:ed|ing)?\s+(?:optimizer|update|controller|control)\b",
        "{algorithm} learning-based optimization",
    ),
    (
        "transformer-based variant",
        r"\btransformer-based\b[^.\n]{0,100}{name}|" r"{name}[^.\n]{0,100}\btransformer-based\b",
        "Transformer-based {algorithm}",
    ),
    (
        "convergence analysis",
        r"\b(?:convergence|convergent|non[-\s]?convergence|analysis|study)\s+"
        r"(?:of|for|in|on)\s+{name}|"
        r"{name}(?:'s)?[^.\n]{0,120}\b(?:convergence|convergent|converges?|"
        r"non[-\s]?convergence|stationarity|descent guarantees?|regret bounds?)\b",
        "{algorithm} convergence analysis",
    ),
    (
        "stability analysis",
        r"\b(?:stability|stabilization|stable|stabilizing)\s+(?:of|for|in|on)\s+{name}|"
        r"{name}[^.\n]{0,120}\b(?:stability|stabilization|stable|stabilizing)\b",
        "{algorithm} stability analysis",
    ),
    (
        "robust variant or analysis",
        r"\b(?:robust|robustness|uncertain|uncertainty-aware)\b[^.\n]{0,120}{name}|"
        r"{name}[^.\n]{0,120}\b(?:robust|robustness|uncertainty|disturbance)\b",
        "Robust {algorithm}",
    ),
    (
        "existing-method discussion",
        r"\b(?:widely\s+used|classical|standard|existing|established|"
        r"recently\s+proposed)\b[^.\n]{0,120}{name}|"
        r"{name}[^.\n]{0,120}\b(?:widely\s+used|classical|standard|existing|"
        r"established|recently\s+proposed)\b",
        "{algorithm} analysis",
    ),
)

_BROAD_ALGORITHM_FAMILY_CUES: tuple[tuple[str, str], ...] = (
    (
        "a more specific variant or modifier in the title/abstract",
        r"\b(?:"
        r"adaptive|approximate|bootstrapped|constrained|covariance|damped|"
        r"data[-\s]+driven|deep|differentiable|domain[-\s]+randomi[sz]ed|"
        r"efficient|flow[-\s]+policy|generative|global(?:ly)?|"
        r"interaction[-\s]+rich|koopman|large[-\s]+deviations?|learned|"
        r"learning[-\s]+based|linear|momentum|natural|nonfragile|"
        r"operator[-\s]+splitting|regulari[sz]ed|risk[-\s]+averse|"
        r"sampling[-\s]+based|second[-\s]+order|stochastic|subspace|"
        r"super[-\s]+universal|temporal|warm[-\s]+start(?:ing|s)?|"
        r"zero(?:th)?[-\s]+order"
        r")\b[^.\n]{0,120}{name}|"
        r"{name}[^.\n]{0,120}\b(?:"
        r"using|via|with|for|from|of|on|by|based\s+on|under|"
        r"domain[-\s]+randomi[sz]ation|dynamic\s+environments?|"
        r"international\s+space\s+station|point\s+clouds?|"
        r"covariance|koopman"
        r")\b|"
        r"\b(?:for|of|on|from|via|using|with|by)\s+{name}\b",
    ),
    (
        "analysis, survey, benchmark, or application of a broad family",
        r"\b(?:"
        r"analysis|applications?|benchmark(?:ing)?|bounds?|comparison|"
        r"convergence|converges?|definitive\s+guide|efficient|extension|"
        r"performance|perspective|stability|survey|theory|tour|view"
        r")\b[^.\n]{0,140}{name}|"
        r"{name}[^.\n]{0,140}\b(?:"
        r"analysis|applications?|benchmark(?:ing)?|bounds?|comparison|"
        r"convergence|converges?|efficient|extension|performance|"
        r"perspective|stability|survey|theory"
        r")\b",
    ),
)

_ALGORITHM_INTRO_VERB_RE = (
    r"introduc(?:e|es|ed|ing)|propos(?:e|es|ed|ing)|"
    r"present(?:s|ed|ing)?|develop(?:s|ed|ing)?|"
    r"deriv(?:e|es|ed|ing)|formulat(?:e|es|ed|ing)"
)
