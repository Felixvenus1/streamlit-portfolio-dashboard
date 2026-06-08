"""Page 1 — UK Open Data (STATS19 road safety)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st

from src.data_loaders import load_road_safety
from src.chart_builders import annual_trend, severity_stacked_bar

st.set_page_config(page_title="UK Open Data", page_icon="🇬🇧", layout="wide")
st.title("🇬🇧 UK Road Safety — STATS19 Explorer")
st.markdown(
    "Road casualty statistics from the Department for Transport (last 5 years). "
    "[Data source](https://data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-safety-data) — "
    "Open Government Licence v3.0."
)

df = load_road_safety()

# ── Sidebar filters ──────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Filters")
    years = sorted(df["year"].dropna().unique().tolist())
    selected_years = st.multiselect("Years", years, default=years)
    severities = sorted(df["severity_label"].dropna().unique().tolist())
    selected_sev = st.multiselect("Severity", severities, default=severities)

filtered = df[df["year"].isin(selected_years) & df["severity_label"].isin(selected_sev)]

# ── KPI row ──────────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)
col1.metric("Total Collisions", f"{len(filtered):,}")
col2.metric("Fatal", f"{(filtered['severity_label'] == 'Fatal').sum():,}")
col3.metric(
    "Fatal Rate",
    f"{(filtered['severity_label'] == 'Fatal').mean() * 100:.2f}%",
)

st.divider()

# ── Charts ────────────────────────────────────────────────────────────────────
c1, c2 = st.columns(2)
with c1:
    st.plotly_chart(
        annual_trend(filtered, "date", "Annual Collision Count"), use_container_width=True
    )
with c2:
    st.plotly_chart(severity_stacked_bar(filtered), use_container_width=True)

# Hour of day
import plotly.express as px

hour_counts = filtered.groupby("hour").size().reset_index(name="count")
st.plotly_chart(
    px.bar(hour_counts, x="hour", y="count", title="Collisions by Hour of Day",
           labels={"hour": "Hour (24h)", "count": "Collisions"}),
    use_container_width=True,
)

# Road type
road_counts = filtered["road_type_label"].value_counts().reset_index()
road_counts.columns = ["road_type", "count"]
c3, c4 = st.columns(2)
with c3:
    st.plotly_chart(
        px.bar(road_counts, x="count", y="road_type", orientation="h",
               title="Collisions by Road Type"),
        use_container_width=True,
    )
with c4:
    area_fatal = (
        filtered.groupby("area_label")
        .apply(lambda d: (d["severity_label"] == "Fatal").mean() * 100)
        .reset_index(name="fatal_pct")
    )
    st.plotly_chart(
        px.bar(area_fatal, x="area_label", y="fatal_pct",
               title="Fatal Rate: Urban vs Rural (%)",
               labels={"area_label": "", "fatal_pct": "% Fatal"}),
        use_container_width=True,
    )
