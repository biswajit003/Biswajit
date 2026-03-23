from vedic_agent.models import Sign
from vedic_agent.vedic_logic import compute_house_lordships


def test_cancer_lagna_house_lordships():
    lordships = compute_house_lordships(Sign.CANCER)

    # Basic sanity: 12 houses
    assert set(lordships.keys()) == set(range(1, 13))

    # Check a few key houses against your table
    # H1: Cancer, lord Moon, Lagna lord
    h1 = lordships[1]
    assert h1["sign"] == "Cancer"
    assert h1["lord"] == "Moon"
    assert "Lagna lord" in h1["role"]

    # H5: Scorpio, lord Mars, Raja Yoga Karaka
    h5 = lordships[5]
    assert h5["sign"] == "Scorpio"
    assert h5["lord"] == "Mars"
    assert "Raja Yoga Karaka" in h5["role"]

    # H3: Virgo, lord Mercury, functional malefic
    h3 = lordships[3]
    assert h3["sign"] == "Virgo"
    assert h3["lord"] == "Mercury"
    assert "Functional malefic" in h3["role"]

