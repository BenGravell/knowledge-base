"""Compatibility wrapper for the Map data generator."""

from knowledge_base.map.pipeline.generate_data import (
    added_only_cache_hit,
    incremental_neighbor_positions,
    main,
)

__all__ = ["added_only_cache_hit", "incremental_neighbor_positions", "main"]

if __name__ == "__main__":
    main()
