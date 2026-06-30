"""Compatibility wrapper for the prefill runner."""

from knowledge_base.prefill.runner import *  # noqa: F403
from knowledge_base.prefill.runner import main

if __name__ == "__main__":
    main()
