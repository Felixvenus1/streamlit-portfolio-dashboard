"""Page 2 — Steam Gaming Trends."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
import plotly.express as px

from src.data_loaders import load_steam_games
from src.chart_builders import top_genres_bar, release_volume_bar

st.set_page_config(page_title="Steam Trends", page_icon="🎮", layout="wide")
st.title("🎮 Steam Gaming Trends")
st.markdown(
    "Analysis of 27 000+ Steam games from the "
    "[fronkongames/steam-games-dataset](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset) "
    "(CC0 Public Domain)."
)

df = load_steam_games()

# ── Sidebar filters ──────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Filters")
    price_range = st.slider(
        "Max price (USD)", 0.0, 70.0, 60.0, step=1.0
    )
    min_reviews = st.number_input("Min total reviews", min_value=0, value=100, step=100)

df_f = df.copy()
if "price" in df_f.columns:
    df_f = df_f[df_f["price"] <= price_range]
if "total_reviews" in df_f.columns:
    df_f = df_f[df_f["total_reviews"] >= min_reviews]

# ── KPI row ──────────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)
col1.metric("Games in Selection", f"{len(df_f):,}")
if "price" in df_f.columns:
    col2.metric("Median Price", f"${df_f['price'].median():.2f}")
if "review_positivity_ratio" in df_f.columns:
    col3.metric("Median Positivity", f"{df_f['review_positivity_ratio'].median():.1%}")

st.divider()

# ── Charts ────────────────────────────────────────────────────────────────────
genre_col = "genres" if "genres" in df_f.columns else "tags"
c1, c2 = st.columns(2)
with c1:
    st.plotly_chart(top_genres_bar(df_f, genre_col), use_container_width=True)
with c2:
    if "release_date" in df_f.columns:
        st.plotly_chart(release_volume_bar(df_f), use_container_width=True)

# Price vs positivity scatter
if "price" in df_f.columns and "review_positivity_ratio" in df_f.columns:
    paid = df_f[df_f["price"] > 0].copy()
    st.plotly_chart(
        px.scatter(
            paid.sample(min(2000, len(paid)), random_state=42),
            x="price", y="review_positivity_ratio",
            opacity=0.4,
            title="Price vs Review Positivity (paid games)",
            labels={"price": "Price (USD)", "review_positivity_ratio": "Positivity Ratio"},
        ),
        use_container_width=True,
    )
