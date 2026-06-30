"""LaTeX and plain-math cleanup constants."""

import re

_TEXT_LATEX_COMMAND_RE = re.compile(
    r"\\(?:emph|mathbb|mathcal|mathscr|mathrm|mathbf|mathit|operatorname|text|textbf|textit)\{([^{}]+)\}"
)
_LATEX_FRAC_RE = re.compile(r"\\frac\{([^{}]+)\}\{([^{}]+)\}")

_DOLLAR_SIGN_RE = re.compile(r"\$")
_DISPLAY_MATH_SPAN_RE = re.compile(r"\$\$(?P<math>.+?)\$\$", re.S)
_INLINE_MATH_SPAN_RE = re.compile(r"(?<!\$)\$(?!\$)(?P<math>[^$\n]+?)(?<!\$)\$(?!\$)")
_PLAIN_LATEX_ELL_ARTIFACT_RE = re.compile(r"\bell_(?=[A-Za-z0-9])")
_PLAIN_LATEX_GREEK_IN_ARTIFACT_RE = re.compile(
    r"\b(?P<var>alpha|beta|gamma|delta|epsilon|zeta|eta|theta|iota|kappa|"
    r"lambda|mu|nu|xi|pi|rho|sigma|tau|upsilon|phi|chi|psi|omega)in"
    r"(?=\s*(?:[\[({]|mathbb))"
)
_PLAIN_LATEX_VARIABLE_IN_ARTIFACT_RE = re.compile(r"\b(?P<var>[a-z])in(?=\s*[\[(]\s*(?:[-+]?\d|infinity))")
_PLAIN_LATEX_STAR_ARTIFACT_RE = re.compile(r"\b(?P<var>[A-Z])star\b")
_PLAIN_LATEX_LIMIT_INFINITY_ARTIFACT_RE = re.compile(r"\blim_(?P<var>[A-Za-z])toinfinity(?P<expr>[A-Za-z])")
_PLAIN_LATEX_EMPH_ARTIFACT_RE = re.compile(r"(?:\{\\em\s+(?P<braced>[^{}]+)\}|\\emph\{(?P<command>[^{}]+)\})")
_PLAIN_LATEX_MATHSCR_ARTIFACT_RE = re.compile(r"\bmathscr(?=[A-Z])")
_PLAIN_LATEX_MATHBB_ARTIFACT_RE = re.compile(r"\bmathbb(?=[A-Z])")
_PLAIN_LATEX_SUBSET_ARTIFACT_RE = re.compile(r"(?<=[A-Za-z])subset\b")
_PLAIN_LATEX_WORD_OPERATOR_ARTIFACT_RE = re.compile(r"\b(?:triangleq|lesssim|gtrsim)\b")
_PLAIN_LATEX_CAL_ARTIFACT_RE = re.compile(r"\bcal\s+(?P<symbol>[A-Z])\b")
_PLAIN_LATEX_WIDETILDE_ARTIFACT_RE = re.compile(r"\bwidetilde(?P<symbol>[A-Z])\b")
_PLAIN_LATEX_TEXTIT_ARTIFACT_RE = re.compile(r"\btextit(?P<word>[A-Za-z][A-Za-z-]*)")

_LATEX_NAMED_SYMBOLS = {
    "alpha": "alpha",
    "beta": "beta",
    "gamma": "gamma",
    "delta": "delta",
    "epsilon": "epsilon",
    "varepsilon": "epsilon",
    "zeta": "zeta",
    "eta": "eta",
    "theta": "theta",
    "vartheta": "theta",
    "iota": "iota",
    "kappa": "kappa",
    "lambda": "lambda",
    "ell": "l",
    "mu": "mu",
    "nu": "nu",
    "xi": "xi",
    "pi": "pi",
    "rho": "rho",
    "sigma": "sigma",
    "tau": "tau",
    "upsilon": "upsilon",
    "phi": "phi",
    "varphi": "phi",
    "chi": "chi",
    "psi": "psi",
    "omega": "omega",
    "Gamma": "Gamma",
    "Delta": "Delta",
    "Theta": "Theta",
    "Lambda": "Lambda",
    "Xi": "Xi",
    "Pi": "Pi",
    "Sigma": "Sigma",
    "Upsilon": "Upsilon",
    "Phi": "Phi",
    "Psi": "Psi",
    "Omega": "Omega",
    "leq": "<=",
    "le": "<=",
    "geq": ">=",
    "ge": ">=",
    "neq": "!=",
    "ne": "!=",
    "approx": "approx",
    "sim": "~",
    "in": "in",
    "to": "to",
    "cdot": "*",
    "times": "x",
    "pm": "+/-",
    "mp": "-/+",
    "infty": "infinity",
    "exp": "exp",
    "log": "log",
    "ln": "ln",
    "sin": "sin",
    "cos": "cos",
    "tan": "tan",
    "min": "min",
    "max": "max",
    "argmin": "argmin",
    "argmax": "argmax",
    "notin": "not in",
    "subset": "subset",
    "subseteq": "subseteq",
    "supset": "supset",
    "supseteq": "supseteq",
    "cup": "union",
    "cap": "intersection",
    "forall": "for all",
    "exists": "exists",
    "nabla": "nabla",
    "partial": "partial",
    "triangleq": "defined as",
    "lesssim": "<~",
    "gtrsim": ">~",
}
_LATEX_SPACED_WORD_SYMBOLS = {
    "approx",
    "exists",
    "for all",
    "in",
    "intersection",
    "not in",
    "subset",
    "subseteq",
    "supset",
    "supseteq",
    "to",
    "union",
}
_UNICODE_MATH_SYMBOLS = str.maketrans(
    {
        "\u03b1": "alpha",
        "\u03b2": "beta",
        "\u03b3": "gamma",
        "\u03b4": "delta",
        "\u03b5": "epsilon",
        "\u03b6": "zeta",
        "\u03b7": "eta",
        "\u03b8": "theta",
        "\u03b9": "iota",
        "\u03ba": "kappa",
        "\u03bb": "lambda",
        "\u03bc": "mu",
        "\u03bd": "nu",
        "\u03be": "xi",
        "\u03c0": "pi",
        "\u03c1": "rho",
        "\u03c3": "sigma",
        "\u03c4": "tau",
        "\u03c5": "upsilon",
        "\u03c6": "phi",
        "\u03c7": "chi",
        "\u03c8": "psi",
        "\u03c9": "omega",
        "\u0393": "Gamma",
        "\u0394": "Delta",
        "\u0398": "Theta",
        "\u039b": "Lambda",
        "\u039e": "Xi",
        "\u03a0": "Pi",
        "\u03a3": "Sigma",
        "\u03a5": "Upsilon",
        "\u03a6": "Phi",
        "\u03a8": "Psi",
        "\u03a9": "Omega",
    }
)

__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
