# On Paper, Not in Practice

A Streamlit application presenting the BUSD Historical Study Capstone Report
timeline of Black educational experience in Berkeley Unified School District,
1856–2026.

Produced for the BUSD Historical Study in partnership with the
**UC Berkeley Public Policy Data Lab**.

---

## What's here

A vertical timeline grouped into three eras:

1. **Era I — Foundations of exclusion** (1856–1923)
2. **Era II — Desegregation and its limits** (1940s–1977)
3. **Era III — Reform, resistance, and unfinished business** (1980s–2026)

Each of the 18 events is collapsed by default and expands on click to show
two additional sections: **Context** (historical background) and
**Why it matters** (pattern-level significance).

---

## Project structure

```
busd_timeline_app/
├── app.py                      # Streamlit entry point
├── components/
│   ├── __init__.py
│   ├── timeline_data.py        # 18 events + era metadata (edit content here)
│   └── timeline_html.py        # HTML/CSS/JS renderer for the timeline
├── .streamlit/
│   └── config.toml             # Theme + server config
├── requirements.txt
└── README.md
```

---

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## Deploy to Streamlit Community Cloud

1. Push this directory to a GitHub repository
   (e.g. `busd-historical-timeline`).
2. At [share.streamlit.io](https://share.streamlit.io), click
   **New app** and select the repo.
3. Set **Main file path** to `app.py`.
4. Click **Deploy**.

No secrets or environment variables are required — the app is fully static
and ships its own content in `components/timeline_data.py`.

---

## Editing the content

All event copy lives in `components/timeline_data.py` as a list of
dictionaries. To revise an entry, edit the relevant `year`, `title`,
`summary`, `context`, or `matters` field and Streamlit will hot-reload on
save.

A small set of inline HTML tags (`<em>`, `<i>`, `<br>`) are passed through
unescaped so legal case names and similar can render in italics. All other
content is HTML-escaped automatically by the renderer.

---

## Source

BUSD Historical Study Capstone Report
UC Berkeley Public Policy Data Lab
