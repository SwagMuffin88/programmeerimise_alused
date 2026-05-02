from statistics import Statistics


def run_tests():
    """Run methods from Statistics class with test data."""
    stats = Statistics("data.txt")

    print("=== 1. KOKKUVÕTTEV STATISTIKA ===")
    print(f"Mängijad: {stats.get('/players')}")
    print(f"Mängud: {stats.get('/games')}")
    print(f"Mänge kokku: {stats.get('/total')}")
    print(f"Points-tüüpi mänge: {stats.get('/total/points')}")
    print("-" * 30)

    print("=== 2. MÄNGIJA STATISTIKA (Joosep) ===")
    print(f"Mänge mängitud: {stats.get('/player/joosep/amount')}")
    print(f"Mänge võidetud: {stats.get('/player/joosep/won')}")
    print(f"Lemmikmäng: {stats.get('/player/joosep/favourite')}")
    print("-" * 30)

    print("=== 3. MÄNGU STATISTIKA (Terraforming Mars) ===")
    print(f"Mitu korda mängitud: {stats.get('/game/terraforming mars/amount')}")
    print(f"Tavalisim mängijate arv: {stats.get('/game/terraforming mars/player-amount')}")
    print(f"Enim võite (nimi): {stats.get('/game/terraforming mars/most-wins')}")
    print(f"Suurim võiduprotsent: {stats.get('/game/terraforming mars/most-frequent-winner')}")
    print(f"Rekordiomanik (punktid): {stats.get('/game/terraforming mars/record-holder')}")
    print("-" * 30)

    print("=== 4. KAOTUSTE STATISTIKA (7 wonders) ===")
    # 7 wonders kaotaja peaks olema Kristjan (20 punkti)
    print(f"Enim kaotusi: {stats.get('/game/7 wonders/most-losses')}")
    print(f"Suurim kaotuseprotsent: {stats.get('/game/7 wonders/most-frequent-loser')}")

    print("\n=== TESTID LÄBITUD ===")


if __name__ == "__main__":
    run_tests()