"""
High-level Vedic astrology agent wired to OpenAI.

Usage inside Cursor (from workspace root):
  pip install -r requirements.txt
  # create a .env file with:
  #   OPENAI_API_KEY=sk-...
  python agent.py

This uses:
- Your example D1 chart (Biswajit) as default
- Vedic logic from vedic_agent.vedic_logic
and lets you ask natural-language questions in the terminal.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

from vedic_agent.models import Chart, Planet, PlanetPlacement, Sign
from vedic_agent.vedic_logic import compute_house_lordships, summarize_strength


def build_example_chart() -> Chart:
    # Same as agent_cli.py – D1 positions from Biswajit_Kundli_Analysis.md
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


def format_chart_context(chart: Chart) -> str:
    strength = summarize_strength(chart)
    lordships = compute_house_lordships(chart.lagna_sign)

    lines = []
    lines.append(f"Lagna: {chart.lagna_sign.value}")
    lines.append("\nPlanetary strength summary (D1):")
    for planet, info in strength.items():
        lines.append(
            f"- {planet.value}: {info['sign']} {info['degree']}°, "
            f"Avastha={info['avastha']}, Dignity={info['dignity']}"
        )

    lines.append("\nHouse lordships (Cancer lagna):")
    for house in range(1, 13):
        h = lordships[house]
        lines.append(
            f"- H{house}: {h['sign']} | Lord={h['lord']} | Role={h['role']}"
        )

    return "\n".join(lines)


def chat_loop():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY not set. Create a .env file with OPENAI_API_KEY=..."
        )

    client = OpenAI(api_key=api_key)

    chart = build_example_chart()
    chart_context = format_chart_context(chart)

    system_prompt = (
        "You are a Vedic astrologer (BPHS-oriented) specializing in Cancer lagna charts.\n"
        "Use ONLY the rules implied by the chart context I give you. "
        "Do NOT invent new rules. Be gentle, non-fatalistic, and avoid medical or "
        "financial guarantees.\n\n"
        "Chart context:\n"
        f"{chart_context}"
    )

    print("=== Vedic Astrology Agent (Vedic, Cancer Lagna) ===")
    print("Type a question about this chart. Type 'exit' to quit.\n")

    history = [
        {"role": "system", "content": system_prompt},
    ]

    while True:
        try:
            user_q = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if not user_q:
            continue
        if user_q.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break

        history.append({"role": "user", "content": user_q})

        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=history,
            temperature=0.4,
        )

        answer = resp.choices[0].message.content
        print(f"\nAgent:\n{answer}\n")

        history.append({"role": "assistant", "content": answer})


if __name__ == "__main__":
    chat_loop()

