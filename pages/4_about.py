"""Page 4 — About this dashboard."""

import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️", layout="wide")
st.title("ℹ️ About This Dashboard")

st.markdown(
    """
This dashboard aggregates analytical work from three portfolio projects into a single navigable application, demonstrating Streamlit multipage architecture, `@st.cache_data` caching, and Plotly interactive charts.

---

## Data Sources

| Page | Dataset | Source | Licence |
|---|---|---|---|
| UK Open Data | STATS19 road casualty statistics | [data.gov.uk](https://www.data.gov.uk) | OGL v3 |
| Steam Trends | Steam games + reviews dataset | [Kaggle (fronkongames)](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset) | CC0 |
| Football Analytics | Premier League match statistics | [football-data.co.uk](https://www.football-data.co.uk) | Free non-commercial |

---

## Methodology

### UK Open Data
STATS19 collision data (last 5 years) is loaded and grouped by year, severity, road type, and hour-of-day. The sample used here is 10 000 rows; the full analysis notebook (`uk-open-data-explorer`) uses the complete ~700 k-row dataset.

### Steam Gaming Trends
The Steam games dataset provides pricing, genre tags, review counts, and playtime. Three derived features are engineered: review positivity ratio, price-per-playtime-hour, and release year lag. See `steam-gaming-trends` for the full multi-notebook analysis.

### Football Analytics
Match-level statistics from two Premier League seasons are aggregated to team level. Key metrics include goals scored/conceded, shots on target, and shot accuracy. See `premier-league-analytics` for full correlation analysis and player similarity scoring.

---

## Portfolio

- **GitHub**: [github.com/Felixvenus1](https://github.com/Felixvenus1)
- All source code is open-source under the MIT licence.
"""
)
