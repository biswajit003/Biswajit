from __future__ import annotations

from typing import Dict, Tuple

from .models import (
    Avastha,
    Chart,
    Dignity,
    ODD_SIGNS,
    Planet,
    PlanetPlacement,
    Sign,
)


# --- Exaltation / Debilitation core table (from your docs) ---

EXALTATION_DEBILITATION: Dict[Planet, Tuple[Sign, float, Sign, float]] = {
    Planet.SUN: (Sign.ARIES, 10.0, Sign.LIBRA, 10.0),
    Planet.MOON: (Sign.TAURUS, 3.0, Sign.SCORPIO, 3.0),
    Planet.MARS: (Sign.CAPRICORN, 28.0, Sign.CANCER, 28.0),
    Planet.MERCURY: (Sign.VIRGO, 15.0, Sign.PISCES, 15.0),
    Planet.JUPITER: (Sign.CANCER, 5.0, Sign.CAPRICORN, 5.0),
    Planet.VENUS: (Sign.PISCES, 27.0, Sign.VIRGO, 27.0),
    Planet.SATURN: (Sign.LIBRA, 20.0, Sign.ARIES, 20.0),
}


# --- Natural friendships (naisargika maitri) (from your docs) ---

NATURAL_FRIENDS: Dict[Planet, Dict[str, Tuple[Planet, ...]]] = {
    Planet.SUN: {
        "friends": (Planet.MOON, Planet.MARS, Planet.JUPITER),
        "neutrals": (Planet.MERCURY,),
        "enemies": (Planet.VENUS, Planet.SATURN),
    },
    Planet.MOON: {
        "friends": (Planet.SUN, Planet.MERCURY),
        "neutrals": (Planet.MARS, Planet.JUPITER, Planet.VENUS, Planet.SATURN),
        "enemies": (),
    },
    Planet.MARS: {
        "friends": (Planet.SUN, Planet.MOON, Planet.JUPITER),
        "neutrals": (Planet.VENUS, Planet.SATURN),
        "enemies": (Planet.MERCURY,),
    },
    Planet.MERCURY: {
        "friends": (Planet.SUN, Planet.VENUS),
        "neutrals": (Planet.MARS, Planet.SATURN),
        "enemies": (Planet.MOON,),
    },
    Planet.JUPITER: {
        "friends": (Planet.SUN, Planet.MOON, Planet.MARS),
        "neutrals": (Planet.SATURN,),
        "enemies": (Planet.MERCURY, Planet.VENUS),
    },
    Planet.VENUS: {
        "friends": (Planet.MERCURY, Planet.SATURN),
        "neutrals": (Planet.MARS, Planet.JUPITER),
        "enemies": (Planet.SUN, Planet.MOON),
    },
    Planet.SATURN: {
        "friends": (Planet.MERCURY, Planet.VENUS),
        "neutrals": (Planet.JUPITER,),
        "enemies": (Planet.SUN, Planet.MOON, Planet.MARS),
    },
}


# --- House lordships for a given lagna ---

SIGN_SEQUENCE = [
    Sign.ARIES,
    Sign.TAURUS,
    Sign.GEMINI,
    Sign.CANCER,
    Sign.LEO,
    Sign.VIRGO,
    Sign.LIBRA,
    Sign.SCORPIO,
    Sign.SAGITTARIUS,
    Sign.CAPRICORN,
    Sign.AQUARIUS,
    Sign.PISCES,
]


def compute_house_signs(lagna_sign: Sign) -> Dict[int, Sign]:
    """
    Given lagna sign, return mapping house -> sign (1–12).
    """
    start_index = SIGN_SEQUENCE.index(lagna_sign)
    seq = SIGN_SEQUENCE[start_index:] + SIGN_SEQUENCE[:start_index]
    return {house: seq[house - 1] for house in range(1, 13)}


def compute_house_lordships(lagna_sign: Sign) -> Dict[int, Dict[str, str]]:
    """
    Compute house -> {sign, lord, role} for the given lagna.

    For Cancer lagna, the functional benefic/malefic notes follow your table:
    - Mars = Raja Yoga Karaka (5th + 10th lord)
    - Mercury = double dusthana lord (3rd + 12th)
    - etc.
    For other lagnas we provide sign + lord only (role="Generic").
    """
    sign_by_house = compute_house_signs(lagna_sign)
    result: Dict[int, Dict[str, str]] = {}

    for house, sign in sign_by_house.items():
        lord = get_sign_lord(sign, lagna_sign)
        role = "Generic"

        if lagna_sign == Sign.CANCER:
            # From Biswajit_Kundli_Analysis.md Section 5
            if house == 1:
                role = "Lagna lord"
            elif house == 2:
                role = "Wealth, speech, family"
            elif house == 3:
                role = "Dusthana lord"
            elif house == 4:
                role = "Kendra lord"
            elif house == 5:
                role = "Trikona lord"
            elif house == 6:
                role = "Dusthana lord"
            elif house == 7:
                role = "Kendra lord"
            elif house == 8:
                role = "Dusthana lord"
            elif house == 9:
                role = "Trikona lord"
            elif house == 10:
                role = "Kendra lord"
            elif house == 11:
                role = "Upachaya lord"
            elif house == 12:
                role = "Dusthana lord"

            # Functional summary for key planets (duplicating your notes)
            if lord == Planet.MARS:
                role = "Raja Yoga Karaka (5th+10th lord)"
            elif lord == Planet.MERCURY:
                role = "Functional malefic (double dusthana lord)"

        result[house] = {
            "sign": sign.value,
            "lord": lord.value if lord else "Unknown",
            "role": role,
        }

    return result


def compute_baladi_avastha(placement: PlanetPlacement) -> Avastha:
    """
    Implements the Baladi Avastha odd/even sign rules from your table.
    """
    degree = placement.degree % 30.0
    is_odd = placement.sign in ODD_SIGNS

    if is_odd:
        if 0 <= degree < 6:
            return Avastha.BALA
        if 6 <= degree < 12:
            return Avastha.KUMARA
        if 12 <= degree < 18:
            return Avastha.YUVA
        if 18 <= degree < 24:
            return Avastha.VRIDDHA
        return Avastha.MRITA
    else:
        if 0 <= degree < 6:
            return Avastha.MRITA
        if 6 <= degree < 12:
            return Avastha.VRIDDHA
        if 12 <= degree < 18:
            return Avastha.YUVA
        if 18 <= degree < 24:
            return Avastha.KUMARA
        return Avastha.BALA


def compute_dignity(placement: PlanetPlacement, lagna_sign: Sign) -> Dignity:
    """
    Very minimal dignity logic:
    - Exaltation / debilitation from EXALTATION_DEBILITATION
    - Own sign via standard moolatrikona / sign ownership (simplified)
    - Friendly / neutral / enemy via naisargika maitri of sign lord
    """
    planet = placement.planet
    sign = placement.sign

    # Exaltation / debilitation
    if planet in EXALTATION_DEBILITATION:
        exalt_sign, _, deb_sign, _ = EXALTATION_DEBILITATION[planet]
        if sign == exalt_sign:
            return Dignity.EXALTED
        if sign == deb_sign:
            return Dignity.DEBILITATED

    # Own sign mapping (classical)
    sign_lord = get_sign_lord(sign, lagna_sign)
    if sign_lord == planet:
        return Dignity.OWN_SIGN

    # Friendly / neutral / enemy based on sign lord's relation
    if sign_lord and sign_lord in NATURAL_FRIENDS.get(planet, {}):
        # This branch is defensive; we use the table below instead
        pass

    if sign_lord is None:
        return Dignity.NEUTRAL

    rel = NATURAL_FRIENDS.get(planet)
    if not rel:
        return Dignity.NEUTRAL

    if sign_lord in rel["friends"]:
        return Dignity.FRIENDLY
    if sign_lord in rel["enemies"]:
        return Dignity.ENEMY
    return Dignity.NEUTRAL


def get_sign_lord(sign: Sign, lagna_sign: Sign | None = None) -> Planet | None:
    """
    Standard Vedic sign lords, independent of lagna.
    (lagna_sign is unused for now but kept for future extensions.)
    """
    if sign in (Sign.ARIES, Sign.SCORPIO):
        return Planet.MARS
    if sign in (Sign.TAURUS, Sign.LIBRA):
        return Planet.VENUS
    if sign in (Sign.GEMINI, Sign.VIRGO):
        return Planet.MERCURY
    if sign in (Sign.CANCER,):
        return Planet.MOON
    if sign in (Sign.LEO,):
        return Planet.SUN
    if sign in (Sign.SAGITTARIUS, Sign.PISCES):
        return Planet.JUPITER
    if sign in (Sign.CAPRICORN, Sign.AQUARIUS):
        return Planet.SATURN
    return None


def summarize_strength(chart: Chart) -> Dict[Planet, Dict[str, str]]:
    """
    Compute a simple strength summary per planet:
    - avastha
    - dignity
    (You can expand later with aspects, yogas, etc.)
    """
    result: Dict[Planet, Dict[str, str]] = {}
    for planet, placement in chart.placements.items():
        avastha = compute_baladi_avastha(placement)
        dignity = compute_dignity(placement, chart.lagna_sign)
        result[planet] = {
            "sign": placement.sign.value,
            "degree": f"{placement.degree:.2f}",
            "avastha": avastha.value,
            "dignity": dignity.value,
        }
    return result

