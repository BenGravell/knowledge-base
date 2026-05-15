#!/usr/bin/env python3
"""Split todo/PAPERS_MISC.md into Claude-sized topical batches.

The misc queue is intentionally messy: it contains papers, project pages,
library docs, blog posts, datasets, and publisher links that are not worth
handling with one broad prefill script.  This script uses high-confidence URL
filters only, writes grouped lists under todo/papers_misc/, and then replaces
todo/PAPERS_MISC.md with a short pointer once every URL has been moved.

Usage:
    python3 knowledge_base/scripts/split_misc_papers.py --dry-run
    python3 knowledge_base/scripts/split_misc_papers.py
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = REPO_ROOT / "todo" / "PAPERS_MISC.md"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "todo" / "papers_misc"
DEFAULT_MAX_SIZE = 20
URL_RE = re.compile(r"^https?://", re.IGNORECASE)


@dataclass(frozen=True)
class Rule:
    stem: str
    title: str
    patterns: tuple[str, ...]


RULES: tuple[Rule, ...] = (
    Rule(
        "robotics_motion_planning",
        "Robotics Motion Planning",
        (
            "mppi",
            "mpc",
            "motion-planning",
            "motion_planning",
            "trajectory-planning",
            "trajectory_optimization",
            "trajectory-optimization",
            "trajopt",
            "kinodynamic",
            "dubins",
            "clothoid",
            "pathfollowing",
            "path-following",
            "obstacle-avoidance",
            "robotic",
            "robotics",
            "loco-manipulation",
            "interlimb",
            "whole-body",
            "exotica",
            "dynoplan",
            "komo",
            "roboplan",
            "rai-inst.com/resources/papers",
            "picknik.ai",
            "tinympc.org",
            "rll.berkeley.edu/trajopt",
            "kavrakilab.org/publications",
            "ompl.kavrakilab.org",
            "personal.ntu.edu.sg/cuong",
            "khatib.stanford.edu",
            "web.ece.ucsb.edu/~hespanha",
            "lis.csail.mit.edu/pubs/goretkin",
            "rpg.ifi.uzh.ch/docs/icra",
            "stanfordasl.github.io/wp-content",
            "people.eecs.berkeley.edu/~jfc/papers/91/lcicra91",
            "publications.ri.cmu.edu/storage/publications/pub_files/pub4/branicky",
            "asso.lcsr.jhu.edu",
            "asco.lcsr.jhu.edu",
            "roboticexplorationlab.org",
            "github.com/acdslab/mppi-generic",
            "github.com/quimortiz/dynoplan",
            "github.com/ipab-slmc/exotica",
            "github.com/lijiangnanbit/path_optimizer_ilqr",
            "github.com/jgillis/fatrop_demo",
            "github.com/ethz-adrl/control-toolbox",
            "github.com/ebertolazzi/clothoids",
            "github.com/stack-of-tasks/eigenpy",
        ),
    ),
    Rule(
        "autonomous_driving_and_av",
        "Autonomous Driving And AV",
        (
            "autonomous",
            "automobile",
            "driving",
            "nuplan",
            "waymo",
            "comma.ai",
            "controls_challenge",
            "pufferdrive",
            "nuro.ai",
            "openautonomy",
            "badas.nexar",
            "physicalai-autonomous-vehicles",
            "publications.ri.cmu.edu/storage/publications/pub_files/pub4/urmson",
            "publications.ri.cmu.edu/storage/publications/pub_files/pub4/ferguson",
            "publications.ri.cmu.edu/storage/publications/pub_files/2009/2/automatic_steering",
            "driving.stanford.edu",
            "brachengineering.com/content/publications/sae",
            "mos.ed.tum.de/fileadmin",
            "ai.stanford.edu/~ddolgov",
            "ai.stanford.edu/~gabeh",
            "github.com/waymo-research",
            "github.com/motional/nuplan-devkit",
            "commonroad.in.tum.de",
            "highway-env.farama.org",
        ),
    ),
    Rule(
        "control_theory_and_mpc",
        "Control Theory And MPC",
        (
            "control",
            "kalman",
            "stabilization",
            "contraction",
            "policy-iteration",
            "dynamic-programming",
            "bellman",
            "ackermann",
            "sindy-mpc",
            "minimumjerk",
            "state-space",
            "koopman",
            "relaxed-controls",
            "bounded-controls",
            "systems/control",
            "liberzon.csl.illinois.edu",
            "bertsekas_1976_dynamic-programming",
            "seminariomatematico.polito.it",
            "deepwiki.com/acados",
            "www.mos.ed.tum.de",
            "wjongeneel.nl/pub",
            "web.stanford.edu/~pavone/papers/singh",
            "github.com/markosvec/bicycle-model-koopman",
            "github.com/eurika-kaiser/sindy-mpc",
            "se.mathworks.com/help/uav/ref/minimumjerk",
            "blog.comma.ai/rlcontrols",
            "digital-library.theiet.org",
            "elib.dlr.de",
        ),
    ),
    Rule(
        "optimization_theory",
        "Optimization Theory",
        (
            "optimization",
            "optimisation",
            "convex",
            "nonconvex",
            "invex",
            "admm",
            "primal-dual",
            "gradient",
            "steepest",
            "lbfgs",
            "bfgs",
            "hessian",
            "cma-es",
            "simulated_annealing",
            "random_fourier",
            "assignment",
            "linear_sum_assignment",
            "hungarian",
            "nevergrad",
            "pyhessian",
            "hessianfree",
            "optax",
            "cvxpygen",
            "ecos",
            "ceres-solver",
            "scptoolbox",
            "fatrop",
            "nocedal",
            "nemirovs",
            "muon",
            "distrobopt",
            "zju-fast-lab/lbfgs-lite",
            "github.com/5had3z/motion-perceiver",
            "github.com/ltatzel/pytorchhessianfree",
            "github.com/fmeirinhos/pytorch-hessianfree",
            "github.com/amirgholami/pyhessian",
            "github.com/uw-acl/scptoolbox",
            "engineering.fb.com/2018/12/20/ai-research/nevergrad",
            "andrew.gibiansky.com/blog/machine-learning/hessian-free",
            "people.sc.fsu.edu/~inavon",
            "cambridge.org/core/journals/acta-numerica",
            "web.mit.edu/~a_a_a",
            "web.stanford.edu/~boyd",
            "calhoun.nps.edu/server/api/core/bitstreams",
            "publications.ri.cmu.edu/tron",
            "asmedigitalcollection.asme.org",
        ),
    ),
    Rule(
        "pathfinding_search_and_graphs",
        "Pathfinding Search And Graphs",
        (
            "a*_search",
            "astar",
            "a-star",
            "beam_search",
            "jump_point_search",
            "contraction_hierarchies",
            "clearance-based-pathfinding",
            "hierarchical-pathfinding",
            "gridmaps",
            "movingai",
            "pathfinding",
            "path_optimizer",
            "graphify",
            "bloom",
            "cuckoo",
            "prefix_sum",
            "spatial-hash",
            "nanoflann",
            "pynndescent",
            "flann",
            "vector-search",
            "rapids-raft",
            "cuvs",
            "faiss",
            "github.com/mit-spark/spatial-hash",
            "github.com/jlblancoc/nanoflann",
            "github.com/lmcinnes/pynndescent",
            "github.com/rapidsai/cuvs",
            "codekata.com/kata/kata05-bloom",
            "cs.princeton.edu/courses/archive/spr06/cos423/handouts/gh05",
            "cs.cmu.edu/~maxim/files/sipp_icra",
            "theory.stanford.edu/~amitp",
            "www.cs.cmu.edu/~dga/papers/cuckoo",
            "cse.yorku.ca/~amana/research/grid",
            "alexene.dev/2019/06/02/hierarchical",
        ),
    ),
    Rule(
        "machine_learning_foundations",
        "Machine Learning Foundations",
        (
            "neural",
            "neat",
            "back-propagation",
            "backprop",
            "kernel-machines",
            "kitchensinks",
            "random-fourier",
            "polynomialfeatures",
            "kernelridge",
            "feature_selection",
            "scorecard",
            "contrastive",
            "optbinning",
            "kmedians",
            "autogluon",
            "openfe",
            "transformer",
            "performer",
            "diffusion",
            "flow-matching",
            "flow-planner",
            "simple-policy-optimization",
            "policy-gradient",
            "reinforcement-learning",
            "imitation",
            "explainable",
            "interpret.ml",
            "metric-learn",
            "pytorch-metric-learning",
            "safeflowmatching",
            "diffusionad",
            "scikit-learn",
            "inria.github.io/scikit-learn-mooc",
            "github.com/huggingface/transformers",
            "github.com/autogluon/autogluon",
            "github.com/iiis-li-group/openfe",
            "github.com/myrepositories-hub/simple-policy-optimization",
            "github.com/kevinmusgrave/pytorch-metric-learning",
            "contrib.scikit-learn.org/metric-learn",
            "pyclustering.github.io/docs",
            "nn.cs.utexas.edu/?stanley:ec02",
            "imitation.readthedocs.io",
            "ericsson.com/en/blog/2023/11/reinforcement-learning",
            "research.google/blog/performer-mpc",
            "jamespreiss.com/pubs",
            "people.eecs.berkeley.edu/~brecht/kitchensinks",
            "m0nads.wordpress.com",
        ),
    ),
    Rule(
        "llms_and_foundation_models",
        "LLMs And Foundation Models",
        (
            "llm",
            "language_model",
            "large-behavioral-models",
            "behaviorgpt",
            "foundation-model",
            "token-abundance",
            "nanochat",
            "nanogpt",
            "mingpt",
            "modded-nanogpt",
            "dall-e",
            "openai.com/index/dall-e",
            "better-language-models",
            "sam3",
            "samaudio",
            "v-jepa",
            "dino-v2",
            "dinov2",
            "transformer-explainer",
            "depth-anything",
            "trace-anything",
            "segment-anything",
            "sam3",
            "ai.meta.com",
            "cdn.openai.com",
            "research.unboxai.com",
            "langkilde.se/blog/navigating-the-token",
            "github.com/karpathy",
            "kellerjordan",
            "poloclub.github.io/transformer-explainer",
            "huggingface.co/facebook",
            "github.com/facebookresearch/eupe",
            "github.com/radarfudan/awesome-state-space-models",
        ),
    ),
    Rule(
        "computer_vision_images_and_graphics",
        "Computer Vision Images And Graphics",
        (
            "vision",
            "image",
            "images",
            "ocr",
            "edge",
            "edge-prsl",
            "object-selection",
            "vector-graphics",
            "photo-mosaics",
            "mosaic",
            "dino",
            "visualizing",
            "compressai",
            "svd-image",
            "line_integral_convolution",
            "structural_similarity",
            "uqi.html",
            "ssim",
            "learned-features",
            "learning-features",
            "pointcloud",
            "genesis-embodied-ai",
            "gear-sonic",
            "spatial-hash",
            "catmullclark",
            "subdivision",
            "bezier",
            "menger_curvature",
            "hausdorff_distance",
            "miniball",
            "catmull",
            "computer-vision",
            "hms.harvard.edu/bss/neuro/bornlab",
            "vision.stanford.edu",
            "lecun.com/exdb",
            "yann.lecun.com/exdb",
            "roboflow/notebooks",
            "interdigitalinc.github.io/compressai",
            "timbaumann.info/svd-image",
            "dgp.toronto.edu/~donovan/color",
            "neoformix.com/2011/obamamultiscalemosaic",
            "blog.notability.com",
            "pomax.github.io/bezierinfo",
            "github.com/hbf/miniball",
            "github.com/tumftm/pointcloudcrafter",
            "nvlabs.github.io/gear-sonic",
            "diglib.eg.org",
            "rreusser.github.io",
        ),
    ),
    Rule(
        "time_series_forecasting_and_signals",
        "Time Series Forecasting And Signals",
        (
            "time_series",
            "time-series",
            "forecast",
            "forecasting",
            "matrix_profile",
            "pattern_matching",
            "minirocket",
            "inceptiontime",
            "dtw",
            "dynamic_time_warping",
            "savitzky",
            "lulu_smoothing",
            "one-euro-filter",
            "kernelreg",
            "stumpy",
            "sktime",
            "tslearn",
            "nixtla",
            "neuralforecast",
            "statsforecast",
            "skforecast",
            "transformers/model_doc/time_series",
            "cs.ucr.edu/~eamonn/time_series",
            "github.com/hfawaz/inceptiontime",
            "github.com/angus924/minirocket",
            "github.com/fspinna/lasts",
            "github.com/nixtla/nixtla",
            "direct.mit.edu/books/oa-monograph",
            "statsmodels.org/dev/generated/statsmodels.nonparametric.kernel_regression",
            "jaantollander.com/post/noise-filtering",
        ),
    ),
    Rule(
        "statistics_probability_and_decisions",
        "Statistics Probability And Decisions",
        (
            "statistics",
            "probability",
            "bandit",
            "cvar",
            "risk-aware",
            "ab-test",
            "a-b-test",
            "sequential-design",
            "highdimensional-statistics",
            "hdp-book",
            "conformal",
            "mapie",
            "qmc",
            "halton",
            "sobol",
            "uniform",
            "regression",
            "bernoulli",
            "random",
            "tor-lattimore",
            "vershyn",
            "sites.math.washington.edu/~rtr",
            "rkeramati.github.io/assets/pdf/cvar",
            "projecteuclid.org",
            "pubsonline.informs.org",
            "engineering.atspotify.com/2024/03/risk-aware",
            "medium.com/toyotaresearch/statistical-thinking",
            "docs.scipy.org/doc/scipy/reference/generated/scipy.stats.qmc",
            "scikit-learn-contrib.github.io/mapie",
            "nixtlaverse.nixtla.io/statsforecast/docs/tutorials/conformalprediction",
        ),
    ),
    Rule(
        "math_numerics_and_theory",
        "Math Numerics And Theory",
        (
            "chebyshev",
            "midpoint_method",
            "fast_marching",
            "dynamic_programming",
            "what_is_invexity",
            "mthode",
            "cauchy",
            "mathematical",
            "theoryofgames",
            "optimal-transport",
            "cedric-villani",
            "rtr179",
            "diffrax",
            "pythonot.github.io",
            "partial differential",
            "seminariomatematico",
            "mathnet.ru",
            "math.ucla.edu",
            "uvammm.github.io/docs/theoryofgames",
            "amp.i.kyoto-u.ac.jp",
            "cambridge.org/core/books/highdimensional-statistics",
            "math.uci.edu/~rvershyn",
            "scirp.org/reference",
            "worldscientific.com/doi",
            "bibbase.org/network/publication/cauchy",
            "en.wikipedia.org/wiki/invex_function",
            "en.wikipedia.org/wiki/chebyshev_polynomials",
            "en.wikipedia.org/wiki/midpoint_method",
            "en.wikipedia.org/wiki/fast_marching_method",
            "en.wikipedia.org/wiki/simulated_annealing",
        ),
    ),
    Rule(
        "systems_hpc_and_performance",
        "Systems HPC And Performance",
        (
            "cuda",
            "gpu",
            "webgpu",
            "hpc",
            "performance",
            "precompiled-headers",
            "jax-mlsys",
            "vectorclass",
            "agner.org/optimize",
            "abseil.io/fast",
            "perfwiki",
            "warp",
            "hydrogym",
            "cuvs",
            "rapids",
            "nvidia",
            "hdf5",
            "highfive",
            "msgpack",
            "nevergrad",
            "github.com/nvidia/warp",
            "cs.stanford.edu/~rfrostig/pubs/jax",
            "developer.nvidia.com/blog",
            "docs.nvidia.com/cuda",
            "huggingface.co/spaces/webml-community/bonsai-webgpu",
            "huggingface.co/collections/prism-ml/bonsai",
            "github.com/vectorclass/version2",
            "edgl.dev/blog/cmake-precompiled-headers",
            "bluebrain.github.io/highfive",
            "github.com/dynamicslab/hydrogym",
        ),
    ),
    Rule(
        "programming_languages_and_devtools",
        "Programming Languages And Devtools",
        (
            "go.dev",
            "ziglang",
            "bun.com",
            "lightpanda",
            "ghostty",
            "pixi",
            "uv",
            "ray.io",
            "gradio",
            "rerun.io",
            "hydra.cc",
            "ibis-project",
            "msgpack",
            "cmake",
            "filepilot",
            "mendeley",
            "github.com/astral-sh/uv",
            "prefix-dev.github.io/pixi",
            "github.com/ibis-project/ibis",
            "shiny.posit.co/py",
            "onnx.ai/sklearn-onnx",
            "pregex",
            "github.com/manoss96/pregex",
            "github.com/slidevjs/slidev",
            "mermaid.ai",
            "marp.app",
        ),
    ),
    Rule(
        "visualization_color_and_design",
        "Visualization Color And Design",
        (
            "visualization",
            "visualizing",
            "colormap",
            "oklab",
            "color",
            "bluenoise",
            "blue_noise",
            "dither",
            "mosaic",
            "line_integral_convolution",
            "lic.readthedocs",
            "momentsingraphics.de/bluenoise",
            "research.google/blog/turbo",
            "bottosson.github.io/posts/oklab",
            "flowersofproximity.com",
            "complexity-explorables.org",
            "poloclub.github.io",
        ),
    ),
    Rule(
        "urban_planning_architecture_and_geodata",
        "Urban Planning Architecture And Geodata",
        (
            "urban",
            "municipal",
            "housing",
            "geodata",
            "lidar",
            "generative-urban-design",
            "drl-urban-planning",
            "autodesk.com/autodesk-university",
            "parametric.se/post",
            "github.com/tsinghua-fib-lab/drl-urban-planning",
            "usgs-lidar.gishub.org",
            "geodatakatalogen.naturvardsverket.se",
        ),
    ),
    Rule(
        "datasets_benchmarks_and_evaluation",
        "Datasets Benchmarks And Evaluation",
        (
            "dataset",
            "benchmarks",
            "benchmark",
            "open-dataset",
            "waymo-open-dataset",
            "nuplan",
            "badas",
            "motion.ipynb",
            "physicalai-autonomous-vehicles",
            "dragon-age-origins",
            "movingai.com/benchmarks",
            "digitalcommons.du.edu/gridmaps2d",
            "du-researchportal.esploro",
            "usgs-lidar",
            "geodatakatalogen",
        ),
    ),
    Rule(
        "biology_neuroscience_and_medicine",
        "Biology Neuroscience And Medicine",
        (
            "genome",
            "neuro",
            "jneurosci",
            "lancet",
            "medicine",
            "species",
            "darwin",
            "wallace",
            "hms.harvard.edu/bss/neuro",
            "www.jneurosci.org",
            "thelancet.com",
            "softlib.rice.edu/pub/crpc-trs/reports/crpc-tr89003",
            "sandjournal.com/wp-content/uploads/2021/04/on-the-tendency-of-species",
        ),
    ),
    Rule(
        "classical_ai_and_historical_papers",
        "Classical AI And Historical Papers",
        (
            "turing",
            "a-theoretical-framework-for-back-propagation",
            "lecun-88",
            "lecun-89",
            "lecun98",
            "ros.pdf",
            "marr-hildreth",
            "lisp",
            "an-algorithm-for-the-organization-of-information",
            "courses.cs.umbc.edu/471/papers/turing",
            "ai.stanford.edu/~ang/papers/icraoss09-ros",
            "vision.stanford.edu/cs598_spring07/papers/lecun98",
            "yann.lecun.com/exdb/publis/pdf/lecun-88",
            "yann.lecun.com/exdb/publis/pdf/lecun-89",
            "semanticscholar.org/paper/an-algorithm-for-the-organization",
            "semanticscholar.org/paper/a-theoretical-framework-for-back-propagation",
        ),
    ),
    Rule(
        "repositories_and_project_pages",
        "Repositories And Project Pages",
        (
            "github.com",
            "gitlab.com",
            "readthedocs.io",
            "docs.",
            "github.io",
            "sites.google.com",
            "colab.research.google.com",
            "drake.mit.edu",
            "databookuw.com",
            "mykel.kochenderfer.com/textbooks",
            "mykel.kochenderfer.com/publications",
            "mpcworkshop.org",
            "stockfishchess.org",
            "openalex.org",
            "graphify.net",
            "rpg.ifi.uzh.ch",
            "rll.berkeley.edu",
        ),
    ),
    Rule(
        "publisher_and_library_links",
        "Publisher And Library Links",
        (
            "dl.acm.org",
            "proceedings.neurips.cc",
            "jstor.org",
            "semanticscholar.org",
            "pdfs.semanticscholar.org",
            "arxiv.org",
            "sciencedirect.com",
            "openreview.net",
            "researchgate.net",
            "jmlr.org",
            "mdpi.com",
            "bmva-archive.org.uk",
            "drops.dagstuhl.de",
            "spiedigitallibrary.org",
            "nvlpubs.nist.gov",
            "academic.oup.com",
            "roboticsconference.org",
            "usenix.org",
            "direct.mit.edu",
            "projecteuclid.org",
            "iopscience.iop.org",
            "pubs.acs.org",
            "ans.org",
            "cir.nii.ac.jp",
            "hal.science",
            "theses.hal.science",
            "aaltodoc.aalto.fi",
            "dspace.mit.edu",
            "repository.cam.ac.uk",
            "repository.gatech.edu",
            "eprints.whiterose.ac.uk",
            "ora.ox.ac.uk",
            "liu.diva-portal.org",
            "diva-portal.org",
            "lunduniversity.lu.se",
            "stir.ac.uk",
            "ojs.",
            "scholar.google.com",
            "academia.edu",
            "weizmann.elsevierpure.com",
        ),
    ),
    Rule(
        "essays_blogs_and_misc_references",
        "Essays Blogs And Misc References",
        (
            "blog",
            "medium.com",
            "substack.com",
            "wordpress.com",
            "wikipedia.org",
            "hotairengines.org",
            "boring-tech",
            "checklist_manifesto",
            "human-likeness",
            "object-selection-adventures",
            "adventofcode",
            "vg.no",
            "mendeley.com",
            "filepilot.tech",
            "the_checklist_manifesto",
            "daphnecornelisse.substack.com",
            "joshhornby.com",
            "sanket-pixel.github.io",
            "blog.notability.com",
            "medium.com/@tomhuds",
            "medium.com/data-science-in-your-pocket",
            "lilianweng.github.io",
            "gregorygundersen.com",
        ),
    ),
)


def normalize_url(raw: str) -> str:
    return raw.strip()


def read_items(path: Path) -> list[str]:
    items: list[str] = []
    seen: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        item = normalize_url(line)
        if not item or item.startswith("#"):
            continue
        if not URL_RE.match(item):
            continue
        if item in seen:
            continue
        seen.add(item)
        items.append(item)
    return items


def haystack(url: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc.lower().removeprefix("www.")
    path = parsed.path.lower()
    query = parsed.query.lower()
    return f"{host}{path}?{query}".replace("%2f", "/")


def classify(url: str) -> tuple[str, str]:
    text = haystack(url)
    for rule in RULES:
        if any(pattern in text for pattern in rule.patterns):
            return rule.stem, rule.title
    return "misc_manual_triage", "Misc Manual Triage"


def sharded_name(stem: str, index: int, shard_count: int) -> str:
    if shard_count == 1:
        return f"{stem}.md"
    return f"{stem}_{index:02d}.md"


def numbered_name(sequence: int, base_name: str) -> str:
    return f"{sequence:03d}_{base_name}"


def plan_groups(items: list[str], max_size: int) -> dict[str, list[str]]:
    grouped: dict[tuple[str, str], list[str]] = {}
    for item in items:
        key = classify(item)
        grouped.setdefault(key, []).append(item)

    shards: list[tuple[str, list[str]]] = []
    for (stem, _title), urls in sorted(grouped.items()):
        shard_count = (len(urls) + max_size - 1) // max_size
        for index in range(1, shard_count + 1):
            start = (index - 1) * max_size
            shard = urls[start : start + max_size]
            shards.append((sharded_name(stem, index, shard_count), shard))

    planned: dict[str, list[str]] = {}
    for sequence, (base_name, shard) in enumerate(shards, start=1):
        planned[numbered_name(sequence, base_name)] = shard
    return planned


def generated_header() -> str:
    return (
        "# Moved to todo/papers_misc/\n"
        "\n"
        "This queue was split by `knowledge_base/scripts/split_misc_papers.py`.\n"
        "The grouped files under `todo/papers_misc/` are now the source of truth for these manual-ingest batches.\n"
    )


def write_groups(groups: dict[str, list[str]], output_dir: Path, dry_run: bool) -> None:
    if dry_run:
        return
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, urls in groups.items():
        (output_dir / name).write_text("\n".join(urls) + "\n", encoding="utf-8")


def clear_removed_outputs(output_dir: Path, planned_names: set[str], dry_run: bool) -> list[Path]:
    if not output_dir.exists():
        return []
    stale = sorted(
        path
        for path in output_dir.glob("*.md")
        if path.name not in planned_names and re.match(r"^[a-z0-9_]+(?:_\d{2})?\.md$", path.name)
    )
    if not dry_run:
        for path in stale:
            path.unlink()
    return stale


def rewrite_source(input_path: Path, keep_source: bool, dry_run: bool) -> None:
    if keep_source or dry_run:
        return
    input_path.write_text(generated_header(), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Source misc URL file")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Directory for grouped files")
    parser.add_argument(
        "--max-size",
        type=int,
        default=DEFAULT_MAX_SIZE,
        help="Maximum URLs per generated group file",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print the split plan without changing files")
    parser.add_argument(
        "--keep-source",
        action="store_true",
        help="Copy grouped files but leave the input file unchanged",
    )
    args = parser.parse_args()

    if args.max_size < 1:
        raise SystemExit("--max-size must be at least 1")

    items = read_items(args.input)
    if not items:
        print(f"No items found in {args.input.relative_to(REPO_ROOT)}.")
        return

    groups = plan_groups(items, args.max_size)
    stale = clear_removed_outputs(args.output_dir, set(groups), args.dry_run)
    write_groups(groups, args.output_dir, args.dry_run)
    rewrite_source(args.input, args.keep_source, args.dry_run)

    mode = "DRY RUN " if args.dry_run else ""
    print(f"{mode}Split {len(items)} item(s) into {len(groups)} file(s):")
    for name, urls in groups.items():
        print(f"  {args.output_dir.relative_to(REPO_ROOT) / name}: {len(urls)}")
    if stale:
        print(f"\nRemoved {len(stale)} stale generated file(s):")
        for path in stale:
            print(f"  {path.relative_to(REPO_ROOT)}")
    if args.keep_source:
        print(f"\nKept source file unchanged: {args.input.relative_to(REPO_ROOT)}")
    elif args.dry_run:
        print(f"\nWould replace {args.input.relative_to(REPO_ROOT)} with a pointer note.")
    else:
        print(f"\nReplaced {args.input.relative_to(REPO_ROOT)} with a pointer note.")


if __name__ == "__main__":
    main()
