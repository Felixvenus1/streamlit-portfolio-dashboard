"""Cached data loading functions for the portfolio dashboard."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

DATA = Path(__file__).parent.parent / "data"


@st.cache_data
def load_road_safety() -> pd.DataFrame:
    """Load the STATS19 road safety sample CSV."""
    return pd.read_csv(DATA / "road_safety_sample.csv", parse_dates=["date"])


@st.cache_data
def load_steam_games() -> pd.DataFrame:
    """Load the Steam games sample CSV."""
    return pd.read_csv(DATA / "steam_games_sample.csv")


@st.cache_data
def load_pl_teams() -> pd.DataFrame:
    """Load the Premier League team season stats sample CSV."""
    return pd.read_csv(DATA / "pl_teams_sample.csv")
