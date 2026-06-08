"""Reusable Plotly chart builders for the portfolio dashboard."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def annual_trend(df: pd.DataFrame, date_col: str, title: str) -> go.Figure:
    """Line chart of annual event counts."""
    annual = df.groupby(df[date_col].dt.year).size().reset_index(name="count")
    annual.columns = ["year", "count"]
    return px.line(annual, x="year", y="count", title=title, markers=True)


def severity_stacked_bar(df: pd.DataFrame) -> go.Figure:
    """Stacked bar chart of annual collisions by severity label."""
    sev = df.groupby(["year", "severity_label"]).size().reset_index(name="count")
    return px.bar(
        sev, x="year", y="count", color="severity_label",
        title="Annual Collisions by Severity",
        color_discrete_map={"Fatal": "#d62728", "Serious": "#ff7f0e", "Slight": "#1f77b4"},
    )


def top_genres_bar(df: pd.DataFrame, genre_col: str = "genres", top_n: int = 10) -> go.Figure:
    """Horizontal bar chart of top-N genres by game count."""
    genre_counts = (
        df[genre_col].dropna().str.split(";").explode().str.strip().value_counts().head(top_n)
    )
    return px.bar(
        genre_counts.reset_index(),
        x="count",
        y=genre_col,
        orientation="h",
        title=f"Top {top_n} Genres by Game Count",
        labels={genre_col: "Genre", "count": "Games"},
    )


def release_volume_bar(df: pd.DataFrame) -> go.Figure:
    """Bar chart of games released per year."""
    years = pd.to_datetime(df["release_date"], errors="coerce").dt.year.value_counts().sort_index()
    years = years[(years.index >= 2000) & (years.index <= 2024)]
    fig = px.bar(
        years.reset_index(), x="release_date", y="count",
        title="Steam Games Released per Year",
        labels={"release_date": "Year", "count": "Games"},
    )
    return fig


def team_goals_bar(df: pd.DataFrame) -> go.Figure:
    """Ranked horizontal bar of total goals by team."""
    totals = df.groupby("team")["goals_for"].sum().sort_values()
    return px.bar(
        totals.reset_index(), x="goals_for", y="team",
        orientation="h",
        title="Total Goals Scored by Club",
        labels={"goals_for": "Goals", "team": "Club"},
    )


def shot_accuracy_scatter(df: pd.DataFrame) -> go.Figure:
    """Scatter of shot accuracy vs goals for, coloured by season."""
    return px.scatter(
        df.dropna(subset=["shot_accuracy", "goals_for"]),
        x="shot_accuracy", y="goals_for",
        color="season", text="team",
        title="Shot Accuracy vs Goals Scored",
        labels={"shot_accuracy": "Shot Accuracy", "goals_for": "Goals"},
        trendline="ols",
    )
