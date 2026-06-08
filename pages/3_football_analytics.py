"""Page 3 — Premier League Football Analytics."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
import plotly.express as px

from src.data_loaders import load_pl_teams
from src.chart_builders import team_goals_bar, shot_accuracy_scatter

st.set_page_config(page_title="Football Analytics", page_icon="⚽", layout="wide")
st.title("⚽ Premier League Performance Analytics")
st.markdown(
    "Two seasons (2022-23 and 2023-24) of Premier League team statistics from "
    "[football-data.co.uk](https://www.football-data.co.uk)."
)

df = load_pl_teams()

# ── Sidebar filters ──────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Filters")
    if "season" in df.columns:
        seasons = sorted(df["season"].unique().tolist())
        selected = st.multiselect("Season", seasons, default=seasons)
        df = df[df["season"].isin(selected)]

# ── KPI row ──────────────────────────────────────────────────────────────────
if "goals_for" in df.columns:
    col1, col2, col3 = st.columns(3)
    col1.metric("Teams", df["team"].nunique() if "team" in df.columns else "—")
    col2.metric("Total Goals", int(df["goals_for"].sum()))
    if "goal_diff" in df.columns:
        top_team = df.loc[df["goal_diff"].idxmax(), "team"] if "team" in df.columns else "—"
        col3.metric("Best Goal Difference", top_team)

st.divider()

# ── Charts ────────────────────────────────────────────────────────────────────
c1, c2 = st.columns(2)
with c1:
    st.plotly_chart(team_goals_bar(df), use_container_width=True)
with c2:
    if "shot_accuracy" in df.columns and "goals_for" in df.columns:
        st.plotly_chart(shot_accuracy_scatter(df), use_container_width=True)

# Correlation heatmap
import numpy as np

num_cols = [c for c in ["goals_for", "goals_against", "goal_diff", "shots",
                         "shots_on_target", "shot_accuracy", "corners", "yellows"]
            if c in df.columns]
if len(num_cols) >= 3:
    corr = df[num_cols].corr().round(2)
    import plotly.graph_objects as go
    fig = go.Figure(
        go.Heatmap(
            z=corr.values,
            x=corr.columns.tolist(),
            y=corr.index.tolist(),
            colorscale="RdYlGn",
            zmid=0,
            text=corr.values,
            texttemplate="%{text}",
        )
    )
    fig.update_layout(title="Team Stats Correlation Heatmap")
    st.plotly_chart(fig, use_container_width=True)
