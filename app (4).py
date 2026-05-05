"""
On Paper, Not in Practice
A Timeline of Black Educational Experience in BUSD, 1856–2026

Streamlit application for the BUSD Historical Study Capstone Report.
UC Berkeley Public Policy Data Lab.
"""

import streamlit as st
from pathlib import Path

from components.timeline_data import ERAS, FOOTER_TEXT, HEADER
from components.timeline_html import render_timeline_html


# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="On Paper, Not in Practice — BUSD Historical Timeline",
    page_icon="📜",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        "About": (
            "On Paper, Not in Practice is a public-history timeline of "
            "Black educational experience in Berkeley Unified School District, "
            "1856–2026. Produced for the BUSD Historical Study Capstone Report "
            "in partnership with the UC Berkeley Public Policy Data Lab."
        )
    },
)


# ---------------------------------------------------------------------------
# Global styling
# ---------------------------------------------------------------------------

CUSTOM_CSS = """
<style>
    /* Tighten Streamlit's default container padding for a more editorial feel */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 760px;
    }

    /* Hide the default Streamlit chrome we don't need on a public-history site */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }

    /* Sidebar toggle styling */
    [data-testid="stSidebarNav"] { display: none; }

    /* Use a serif accent on H1/H2 inside the main content area */
    .main h1, .main h2 {
        font-family: Georgia, "Times New Roman", serif;
        font-weight: 500;
        letter-spacing: -0.01em;
    }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Sidebar — navigation and context
# ---------------------------------------------------------------------------

with st.sidebar:
    st.markdown("### About this timeline")
    st.markdown(
        "**On Paper, Not in Practice** traces the history of Black "
        "educational experience in Berkeley Unified School District "
        "across three eras, drawing on the BUSD Historical Study "
        "Capstone Report."
    )

    st.markdown("---")

    st.markdown("### Eras")
    for era in ERAS:
        st.markdown(
            f"**{era['label']}**  \n"
            f"<span style='color:#6b6b6b;font-size:13px'>"
            f"{era['name']} · {era['span']}</span>",
            unsafe_allow_html=True,
        )

    st.markdown("---")

    st.markdown("### Source")
    st.markdown(
        "BUSD Historical Study Capstone Report  \n"
        "UC Berkeley Public Policy Data Lab"
    )

    st.markdown("---")
    st.caption("v1.0 · Last updated May 2026")


# ---------------------------------------------------------------------------
# Main content
# ---------------------------------------------------------------------------

# Render the full interactive timeline as a single HTML component so the
# expand/collapse interactions and editorial styling stay intact.
timeline_html = render_timeline_html(
    header=HEADER,
    eras=ERAS,
    footer_text=FOOTER_TEXT,
)

# Height tuned to fit the full timeline with all entries collapsed.
# The component's internal expand/collapse behavior handles overflow when
# entries are opened (the iframe scrolls within itself).
st.components.v1.html(timeline_html, height=4200, scrolling=True)
