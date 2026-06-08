"""Generate small bundled sample CSVs so the dashboard runs without
downloading the full P04/P05/P06 datasets."""

import random
from pathlib import Path

import numpy as np
import pandas as pd

random.seed(42)
rng = np.random.default_rng(42)

OUT = Path(__file__).parent

# ── 1. Road safety sample ────────────────────────────────────────────────────
n = 10_000
dates = pd.date_range("2019-01-01", "2023-12-31", periods=n)
severities = rng.choice(["Slight", "Serious", "Fatal"], size=n, p=[0.75, 0.20, 0.05])
road_types = rng.choice(
    ["Single carriageway", "Dual carriageway", "Roundabout", "One way street"],
    size=n, p=[0.60, 0.20, 0.10, 0.10],
)
areas = rng.choice(["Urban", "Rural"], size=n, p=[0.67, 0.33])
hours = rng.integers(0, 24, size=n)

pd.DataFrame({
    "date": dates,
    "year": pd.DatetimeIndex(dates).year,
    "severity_label": severities,
    "road_type_label": road_types,
    "area_label": areas,
    "hour": hours,
}).to_csv(OUT / "road_safety_sample.csv", index=False)

print("road_safety_sample.csv written")

# ── 2. Steam games sample ─────────────────────────────────────────────────────
n = 2_000
genre_pool = [
    "Action", "Adventure", "Casual", "Indie", "RPG", "Simulation",
    "Sports", "Strategy", "Racing", "Puzzle",
]
release_years = rng.integers(2000, 2025, size=n).astype(str)
prices = np.where(rng.random(n) < 0.15, 0.0, rng.exponential(10, n)).round(2)
prices = np.clip(prices, 0, 60)
total_reviews = rng.integers(0, 50_000, size=n)
pos_pct = rng.beta(5, 2, n)

genres = [
    ";".join(random.sample(genre_pool, k=rng.integers(1, 4)))
    for _ in range(n)
]

pd.DataFrame({
    "name": [f"Game_{i}" for i in range(n)],
    "genres": genres,
    "release_date": release_years,
    "price": prices,
    "total_reviews": total_reviews,
    "review_positivity_ratio": pos_pct.round(3),
}).to_csv(OUT / "steam_games_sample.csv", index=False)

print("steam_games_sample.csv written")

# ── 3. Premier League team stats sample ───────────────────────────────────────
teams = [
    "Arsenal", "Aston Villa", "Brentford", "Brighton", "Burnley",
    "Chelsea", "Crystal Palace", "Everton", "Fulham", "Liverpool",
    "Luton", "Man City", "Man Utd", "Newcastle", "Nottm Forest",
    "Sheffield Utd", "Tottenham", "West Ham", "Wolves", "Bournemouth",
]
seasons = ["2022-23", "2023-24"]
rows = []
for season in seasons:
    for team in teams:
        gf = rng.integers(25, 95)
        ga = rng.integers(20, 85)
        shots = rng.integers(250, 600)
        sot = rng.integers(80, 200)
        rows.append({
            "season": season,
            "team": team,
            "goals_for": gf,
            "goals_against": ga,
            "goal_diff": gf - ga,
            "shots": shots,
            "shots_on_target": sot,
            "shot_accuracy": round(sot / shots, 3),
            "corners": rng.integers(100, 250),
            "yellows": rng.integers(30, 90),
        })

pd.DataFrame(rows).to_csv(OUT / "pl_teams_sample.csv", index=False)
print("pl_teams_sample.csv written")
