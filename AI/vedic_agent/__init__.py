"""
Vedic astrology agent package.

Focuses on:
- Clean chart data structures
- Pure Vedic computation logic (no invented rules)
- Agent skeleton that can be wired to any LLM API
"""

from .models import Chart, PlanetPlacement

__all__ = ["Chart", "PlanetPlacement"]

