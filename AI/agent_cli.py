"""
Minimal CLI entrypoint to experiment with the Vedic agent inside Cursor.

Usage (from workspace root in Cursor terminal):
  pip install -r requirements.txt
  python agent_cli.py

This version does NOT yet call the OpenAI API.
It demonstrates:
- building a D1 chart (using your own placements as an example)
- running Baladi Avastha + dignity computations
"""

from vedic_agent.models import Chart, Planet, PlanetPlacement, Sign
from vedic_agent.vedic_logic import summarize_strength


def build_example_chart() -> Chart:
    # Based on Biswajit_Kundli_Analysis.md D1 positions
    placements = {
        Planet.MARS: PlanetPlacement(Planet.MARS, Sign.LEO, 12.94, house=2),
        Planet.VENUS: PlanetPlacement(Planet.VENUS, Sign.VIRGO, 22.26, house=3),
        Planet.RAHU: PlanetPlacement(Planet.RAHU, Sign.VIRGO, 11.9, house=3),
        Planet.SUN: PlanetPlacement(Planet.SUN, Sign.LIBRA, 25.8, house=4),
        Planet.MERCURY: PlanetPlacement(Planet.MERCURY, Sign.SCORPIO, 1.57, house=5),
        Planet.MOON: PlanetPlacement(Planet.MOON, Sign.SCORPIO, 2.83, house=5),
        Planet.JUPITER: PlanetPlacement(Planet.JUPITER, Sign.SAGITTARIUS, 20.8, house=6),
        Planet.SATURN: PlanetPlacement(
            Planet.SATURN, Sign.PISCES, 7.21, house=9, retrograde=True
        ),
        Planet.KETU: PlanetPlacement(Planet.KETU, Sign.PISCES, 11.9, house=9),
    }
    return Chart(lagna_sign=Sign.CANCER, placements=placements)


def main() -> None:
    chart = build_example_chart()
    strength = summarize_strength(chart)

    print("=== Vedic D1 Strength Summary (Example Chart) ===")
    print(f"Lagna: {chart.lagna_sign.value}")
    print()
    for planet, info in strength.items():
        print(
            f"{planet.value:7s} | {info['sign']:10s} {info['degree']:>6s}°"
            f" | Avastha: {info['avastha']:<7s}"
            f" | Dignity: {info['dignity']}"
        )


if __name__ == "__main__":
    main()

