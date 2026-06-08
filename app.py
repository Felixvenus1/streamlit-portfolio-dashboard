"""Streamlit portfolio dashboard — entry point."""

import streamlit as st

st.set_page_config(
    page_title="Felix Venus — Data Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("📊 Portfolio Dashboard")
st.sidebar.markdown(
    "Multi-page analytics dashboard showcasing work from three data projects."
)
st.sidebar.markdown("---")
st.sidebar.markdown(
    "**Projects**\n"
    "- [P04 UK Open Data](https://github.com/Felixvenus1)\n"
    "- [P05 Steam Trends](https://github.com/Felixvenus1)\n"
    "- [P06 Football Analytics](https://github.com/Felixvenus1)"
)

st.title("Welcome to the Portfolio Dashboard")
st.markdown(
    """
    Use the **sidebar** or the page links below to navigate between analytical views.

    | Page | Description |
    |---|---|
    | 🇬🇧 UK Open Data | Road safety collision trends from STATS19 |
    | 🎮 Steam Trends | Game genre popularity, pricing, and release volume |
    | ⚽ Football Analytics | Premier League team and player performance |
    | ℹ️ About | Data sources, methodology, portfolio links |
    """
)
