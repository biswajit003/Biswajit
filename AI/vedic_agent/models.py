from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


class Sign(str, Enum):
    ARIES = "Aries"
    TAURUS = "Taurus"
    GEMINI = "Gemini"
    CANCER = "Cancer"
    LEO = "Leo"
    VIRGO = "Virgo"
    LIBRA = "Libra"
    SCORPIO = "Scorpio"
    SAGITTARIUS = "Sagittarius"
    CAPRICORN = "Capricorn"
    AQUARIUS = "Aquarius"
    PISCES = "Pisces"


class Planet(str, Enum):
    SUN = "Sun"
    MOON = "Moon"
    MARS = "Mars"
    MERCURY = "Mercury"
    JUPITER = "Jupiter"
    VENUS = "Venus"
    SATURN = "Saturn"
    RAHU = "Rahu"
    KETU = "Ketu"


ODD_SIGNS = {
    Sign.ARIES,
    Sign.GEMINI,
    Sign.LEO,
    Sign.LIBRA,
    Sign.SAGITTARIUS,
    Sign.AQUARIUS,
}


class Avastha(str, Enum):
    BALA = "Bala"  # infant
    KUMARA = "Kumara"  # adolescent
    YUVA = "Yuva"  # youth
    VRIDDHA = "Vriddha"  # old
    MRITA = "Mrita"  # dead


class Dignity(str, Enum):
    EXALTED = "Exalted"
    DEBILITATED = "Debilitated"
    OWN_SIGN = "Own sign"
    FRIENDLY = "Friendly sign"
    NEUTRAL = "Neutral sign"
    ENEMY = "Enemy sign"


@dataclass
class PlanetPlacement:
    planet: Planet
    sign: Sign
    degree: float
    house: int
    retrograde: bool = False


@dataclass
class Chart:
    """Minimal D1 chart representation for Vedic logic."""

    lagna_sign: Sign
    placements: Dict[Planet, PlanetPlacement] = field(default_factory=dict)

    def get(self, planet: Planet) -> Optional[PlanetPlacement]:
        return self.placements.get(planet)

