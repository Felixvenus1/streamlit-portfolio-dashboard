# Dashboard Wireframe (ARTEFACT 10-A)

Low-fidelity layout shared by every page: a persistent left sidebar (navigation +
global/page filters) and a wide main column (title → KPI metric row → chart grid).

```
┌──────────────────────────────────────────────────────────────────────────┐
│ ┌───────────────┐  ┌─────────────────────────────────────────────────────┐ │
│ │  SIDEBAR      │  │  MAIN AREA                                          │ │
│ │               │  │                                                     │ │
│ │ 📊 Portfolio  │  │  🎮  Page Title                                     │ │
│ │  Dashboard    │  │  short description / data source link               │ │
│ │ ───────────── │  │  ─────────────────────────────────────────────────  │ │
│ │  • app (home) │  │  ┌─────────┐ ┌─────────┐ ┌─────────┐                 │ │
│ │  • uk open    │  │  │ KPI 1   │ │ KPI 2   │ │ KPI 3   │   (st.metric)   │ │
│ │  • steam      │  │  └─────────┘ └─────────┘ └─────────┘                 │ │
│ │  • football   │  │  ─────────────────────────────────────────────────  │ │
│ │  • about      │  │  ┌───────────────────┐ ┌───────────────────┐         │ │
│ │ ───────────── │  │  │  Plotly chart A   │ │  Plotly chart B   │         │ │
│ │  Filters      │  │  │  (interactive)    │ │  (interactive)    │         │ │
│ │  [ Season  ▾] │  │  └───────────────────┘ └───────────────────┘         │ │
│ │  [ Metric  ▾] │  │  ┌─────────────────────────────────────────┐         │ │
│ │  [ Date  ──○ ]│  │  │  Plotly chart C / data table            │         │ │
│ │               │  │  └─────────────────────────────────────────┘         │ │
│ │  Source links │  │                                                     │ │
│ └───────────────┘  └─────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────┘
```

## Page navigation & data sources (ARTEFACT 10-C)

```mermaid
graph TD
    APP["app.py (Home)"]
    APP --> UK["1 · UK Open Data"]
    APP --> ST["2 · Steam Trends"]
    APP --> FB["3 · Football Analytics"]
    APP --> AB["4 · About"]

    UK -->|load_road_safety| D1["road_safety_sample.csv<br/>(← P04 STATS19)"]
    ST -->|load_steam_games| D2["steam_games_sample.csv<br/>(← P05 Steam)"]
    FB -->|load_pl_teams| D3["pl_teams_sample.csv<br/>(← P06 football-data)"]
    AB --> META["methodology & links"]

    classDef data fill:#eef,stroke:#88a;
    class D1,D2,D3 data;
```

All loaders are wrapped in `@st.cache_data` so each CSV is read once per session.
