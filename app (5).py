"""
On Paper, Not in Practice
A Timeline of Black Educational Experience in BUSD, 1856-2026

Single-file Streamlit application for the BUSD Historical Study Capstone Report.
UC Berkeley Public Policy Data Lab.

This is a consolidated version of the modular app — all timeline data and
HTML rendering logic is inlined here so the app can be deployed as a single
file with no package structure.
"""

import streamlit as st


# =============================================================================
# Page configuration
# =============================================================================

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


CUSTOM_CSS = """
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 760px;
    }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    [data-testid="stSidebarNav"] { display: none; }
    .main h1, .main h2 {
        font-family: Georgia, "Times New Roman", serif;
        font-weight: 500;
        letter-spacing: -0.01em;
    }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# =============================================================================
# Timeline data
# =============================================================================


HEADER = {
    "eyebrow": "BUSD Historical Study · Capstone Report",
    "title": "On paper, not in practice",
    "subtitle": "A timeline of Black educational experience in Berkeley, 1856–2026",
    "hint": "Click any entry to expand",
}

FOOTER_TEXT = "Source: BUSD Historical Study Capstone Report · UC Berkeley Public Policy Data Lab"


ERAS = [
    {
        "label": "Era I",
        "name": "Foundations of exclusion",
        "span": "1856 – 1923",
        "events": [
            {
                "year": "1856",
                "title": "Ocean View School opens for white children only",
                "summary": (
                    "Berkeley's first school admits white students exclusively. "
                    "Black children are denied access from the city's earliest "
                    "days of public education."
                ),
                "context": (
                    "Ocean View School opened in present-day West Berkeley, six "
                    "years after California statehood and the same year the "
                    "territory's first public schools were being organized. "
                    "The school served the children of white settlers in the "
                    "developing Ocean View district."
                ),
                "matters": (
                    "The earliest institutional act of public education in "
                    "Berkeley was an act of racial exclusion. The pattern set "
                    "in 1856 — that 'public' meant white — would shape the "
                    "district's policies, geography, and demographics for the "
                    "next century and a half."
                ),
            },
            {
                "year": "1860",
                "title": "California codifies racial segregation in schools",
                "summary": (
                    "State school codes formally bar Black, Indigenous, and "
                    "Asian children from public schools, embedding exclusion "
                    "in education law."
                ),
                "context": (
                    "The 1860 California school law explicitly prohibited the "
                    "admission of 'Negroes, Mongolians, and Indians' into "
                    "public schools attended by white children. Districts that "
                    "admitted such children would lose their share of state "
                    "school funds, creating a powerful financial incentive "
                    "for exclusion."
                ),
                "matters": (
                    "This statute moved racial exclusion from local custom "
                    "into state law, and it tied funding to compliance — a "
                    "structural lever that would resurface throughout "
                    "California's education history whenever the state wanted "
                    "to shape local district behavior."
                ),
            },
            {
                "year": "1874",
                "title": "Ward v. Flood upholds 'separate but equal'",
                "summary": (
                    "The California Supreme Court endorses the separate-but-equal "
                    "doctrine 20 years before <em>Plessy v. Ferguson</em> "
                    "nationalizes it."
                ),
                "context": (
                    "Mary Frances Ward, a Black girl, was denied admission to "
                    "a San Francisco school reserved for white students. Her "
                    "father sued. The California Supreme Court ruled that "
                    "while Black children had a right to public education, "
                    "districts could satisfy that right by providing separate "
                    "schools."
                ),
                "matters": (
                    "Ward v. Flood established the legal scaffolding for "
                    "'separate but equal' in California two decades before "
                    "the U.S. Supreme Court applied the same logic nationally "
                    "in <em>Plessy</em>. The doctrine became the legal "
                    "foundation for school segregation across the state."
                ),
            },
            {
                "year": "1880",
                "title": "California ends mandatory school segregation",
                "summary": (
                    "The state mandates open enrollment, formally ending "
                    "<em>de jure</em> segregation. In Berkeley, "
                    "<em>de facto</em> segregation persists for decades "
                    "through housing and zoning."
                ),
                "context": (
                    "An 1880 amendment to the California School Law removed "
                    "the explicit racial bar from school admission, requiring "
                    "schools to be open to 'all children.' Separate schools "
                    "for Asian children remained legal under a later carve-out, "
                    "but the blanket exclusion of Black children was lifted."
                ),
                "matters": (
                    "The end of <em>de jure</em> segregation did not produce "
                    "integrated schools. In Berkeley and across California, "
                    "residential segregation, attendance-zone drawing, and "
                    "informal placement practices reproduced separation "
                    "without naming race — the beginning of the 'on paper, "
                    "not in practice' pattern."
                ),
            },
            {
                "year": "1916",
                "title": "Berkeley passes the nation's first single-family zoning law",
                "summary": (
                    "The ordinance is designed to exclude nonwhite residents "
                    "from the hills and confine Black families to South "
                    "Berkeley, shaping the district's racial geography for "
                    "a century."
                ),
                "context": (
                    "Berkeley's 1916 ordinance designated certain "
                    "neighborhoods, primarily in the hills, as exclusively "
                    "single-family. Drafters and proponents at the time were "
                    "explicit that the goal was to keep these neighborhoods "
                    "white — using housing type as a proxy for race after "
                    "explicit racial zoning had been challenged in court."
                ),
                "matters": (
                    "Because school assignment in Berkeley followed "
                    "neighborhood lines, zoning was school policy by another "
                    "name. Single-family zoning concentrated Black families "
                    "in flatland neighborhoods like South and West Berkeley, "
                    "producing segregated schools without any explicit racial "
                    "assignment rule."
                ),
            },
            {
                "year": "1923",
                "title": "Berkeley principals tout 'racial stock' and adopt mental testing",
                "summary": (
                    "A U.S. Department of Education bulletin authored by "
                    "Berkeley principals praises the city's 'excellent racial "
                    "stock' while introducing student tracking through "
                    "mental tests."
                ),
                "context": (
                    "Berkeley principals contributed to a U.S. Department of "
                    "Education bulletin that celebrated the city's "
                    "demographic profile in eugenicist terms while describing "
                    "the district's adoption of group mental testing to sort "
                    "students into instructional tracks."
                ),
                "matters": (
                    "This document is a hinge moment: it shows that the "
                    "academic tracking systems that would later be identified "
                    "as drivers of racial inequity were introduced in an "
                    "explicitly racialized intellectual climate. Tracking was "
                    "not a race-neutral tool that later acquired racial "
                    "effects — it was built within a framework that already "
                    "viewed students hierarchically by race."
                ),
            },
        ],
    },
    {
        "label": "Era II",
        "name": "Desegregation and its limits",
        "span": "1940s – 1977",
        "events": [
            {
                "year": "1940s–50s",
                "title": "Federal HOLC redlining maps formalize segregation",
                "summary": (
                    "Redlining restricts Black homeownership and concentrates "
                    "Descendant students in under-resourced neighborhood "
                    "schools, hardening the link between zoning and schooling."
                ),
                "context": (
                    "The federal Home Owners' Loan Corporation produced "
                    "color-coded neighborhood risk maps used by lenders to "
                    "decide where to issue mortgages. Black neighborhoods in "
                    "Berkeley — including South and West Berkeley — were "
                    "graded 'hazardous' (red), cutting off access to "
                    "conventional home financing."
                ),
                "matters": (
                    "Redlining compounded the effects of the 1916 zoning "
                    "ordinance: Black families were both confined to specific "
                    "neighborhoods <em>and</em> denied the financial tool that "
                    "would let them build wealth in those neighborhoods. The "
                    "schools serving those neighborhoods inherited "
                    "under-resourced tax bases and concentrated need."
                ),
            },
            {
                "year": "1958",
                "title": "Berkeley NAACP challenges segregated school conditions",
                "summary": (
                    "The local NAACP formally raises segregation before the "
                    "Board of Education, prompting the appointment of the "
                    "Staats Committee to investigate."
                ),
                "context": (
                    "Four years after <em>Brown v. Board</em>, the Berkeley "
                    "NAACP brought a formal challenge to the Board of "
                    "Education documenting the segregated and unequal "
                    "conditions in Berkeley's schools. The Board responded "
                    "by appointing the Staats Committee — a citizen study "
                    "group tasked with examining the claims."
                ),
                "matters": (
                    "This was the first time BUSD was forced into an official "
                    "process that named segregation in its own schools. It "
                    "established a pattern that recurs across the timeline: "
                    "community advocacy → commissioned study → partial reform "
                    "→ persistent inequity."
                ),
            },
            {
                "year": "1959",
                "title": "Staats Committee documents racial tracking",
                "summary": (
                    "The committee finds racial tracking begins as early as "
                    "seventh grade. In response, BUSD hires eight Black "
                    "teachers — its first significant equity hire."
                ),
                "context": (
                    "The Staats Committee report identified that Black "
                    "students were systematically routed into lower "
                    "instructional tracks beginning in junior high, producing "
                    "divergent academic trajectories well before high school. "
                    "BUSD's primary policy response was a hiring action: "
                    "eight Black teachers added to the staff."
                ),
                "matters": (
                    "The 1959 finding documents tracking as a mechanism — "
                    "not just an outcome — of inequity. The district's "
                    "response illustrates a recurring asymmetry: the "
                    "diagnosis named a structural problem (placement systems), "
                    "but the remedy addressed staffing. The tracking system "
                    "itself remained largely intact."
                ),
            },
            {
                "year": "1963",
                "title": "Citizens Committee calls for academic desegregation",
                "summary": (
                    "BUSD's Citizens Committee on De Facto Segregation "
                    "documents systemic racial tracking and calls for "
                    "desegregation of academic pathways, not just buildings."
                ),
                "context": (
                    "Building on the Staats findings, the Citizens Committee "
                    "on De Facto Segregation produced a more comprehensive "
                    "accounting of how segregation operated in Berkeley — "
                    "through attendance boundaries, course placement, and "
                    "counseling. Its report argued that integrating school "
                    "buildings without integrating academic pathways would "
                    "not produce equal education."
                ),
                "matters": (
                    "The 1963 report introduced a distinction that remains "
                    "central to BUSD's history: physical desegregation and "
                    "academic desegregation are not the same thing. The "
                    "recommendation to desegregate pathways was largely "
                    "deferred — a deferral the 2006 <em>Unfinished Business</em> "
                    "report would later trace forward."
                ),
            },
            {
                "year": "1968",
                "title": "Berkeley High Black Student Union wins Black Studies",
                "summary": (
                    "Formed after Dr. King's assassination, the BSU secures "
                    "the hiring of Black teachers and establishes the nation's "
                    "first high school Black Studies department."
                ),
                "context": (
                    "In the weeks following Dr. King's assassination, Black "
                    "students at Berkeley High organized the Black Student "
                    "Union and presented a list of demands to the "
                    "administration. The outcomes included expanded hiring "
                    "of Black faculty and the establishment of a dedicated "
                    "Black Studies department — the first at any U.S. high "
                    "school."
                ),
                "matters": (
                    "The 1968 BSU action is one of the few moments on this "
                    "timeline when structural change came from student "
                    "organizing rather than administrative study. It also "
                    "foregrounded curriculum — what students learn, taught "
                    "by whom — as an equity question on equal footing with "
                    "school assignment."
                ),
            },
            {
                "year": "Sept. 10,<br>1968",
                "title": "BUSD launches the nation's first voluntary busing plan",
                "summary": (
                    "Berkeley becomes the first U.S. district to integrate "
                    "all of its elementary schools through a voluntary "
                    "two-way busing desegregation plan."
                ),
                "context": (
                    "On the first day of the 1968–69 school year, BUSD "
                    "implemented a two-way busing plan that integrated all "
                    "of its elementary schools at once, without a court order. "
                    "Children from the flats were bused to schools in the "
                    "hills and vice versa — a nationally unprecedented "
                    "voluntary desegregation action by a school board."
                ),
                "matters": (
                    "Berkeley earned a national reputation as a desegregation "
                    "pioneer, and that reputation has shaped the district's "
                    "self-understanding ever since. But the busing plan "
                    "addressed building assignment, not the tracking and "
                    "placement systems the 1963 committee had named — a gap "
                    "that subsequent decades would expose."
                ),
            },
            {
                "year": "1977",
                "title": "U.S. Civil Rights Commission flags persistent inequity",
                "summary": (
                    "A federal report documents persistent low-track "
                    "placement of students of color in BUSD and low teacher "
                    "expectations — nearly a decade after integration."
                ),
                "context": (
                    "The U.S. Commission on Civil Rights examined "
                    "post-integration outcomes in BUSD and reported that "
                    "students of color were still disproportionately placed "
                    "in low-track classes and faced lower expectations from "
                    "teachers. The buildings were integrated; the academic "
                    "experience inside them was not."
                ),
                "matters": (
                    "The 1977 report is an external, federal confirmation of "
                    "what the 1963 Citizens Committee had predicted: "
                    "integrating attendance without integrating placement "
                    "leaves the underlying inequity in place. It is the first "
                    "major outside review to grade Berkeley's celebrated "
                    "1968 desegregation as incomplete."
                ),
            },
        ],
    },
    {
        "label": "Era III",
        "name": "Reform, resistance, and unfinished business",
        "span": "1980s – 2026",
        "events": [
            {
                "year": "1980s–90s",
                "title": "Arena self-scheduling reproduces tracking at Berkeley High",
                "summary": (
                    "A self-scheduling system at Berkeley High systematically "
                    "results in Black and Latino students being less likely "
                    "to access higher-level courses."
                ),
                "context": (
                    "Berkeley High's 'arena' system had students assemble "
                    "their own schedules during in-person registration "
                    "sessions. Course access depended on which sections "
                    "filled first, which counselors a student had access to, "
                    "and how well students and families could navigate the "
                    "system."
                ),
                "matters": (
                    "Arena scheduling was facially race-neutral but produced "
                    "racially patterned outcomes. It is a textbook example "
                    "of how a system that distributes opportunity by social "
                    "capital reproduces existing inequities — the same "
                    "dynamic the 1963 and 1977 reports had identified, now "
                    "expressed through a new mechanism."
                ),
            },
            {
                "year": "1996",
                "title": "Proposition 209 bans affirmative action",
                "summary": (
                    "The statewide measure erodes equity-focused hiring and "
                    "admissions frameworks across BUSD and the UC system."
                ),
                "context": (
                    "Proposition 209 amended the California Constitution to "
                    "prohibit state and local government entities from "
                    "considering race, sex, or ethnicity in public "
                    "employment, contracting, and education. It applied to "
                    "school districts and the UC system alike."
                ),
                "matters": (
                    "Prop 209 narrowed the legal toolkit available to BUSD "
                    "and to UC Berkeley for race-conscious remediation just "
                    "as the limits of facially neutral reform were becoming "
                    "clear. Subsequent equity work in BUSD has largely had "
                    "to operate through proxies — geography, income, school "
                    "site — rather than through direct race-conscious "
                    "targeting."
                ),
            },
            {
                "year": "2006",
                "title": "<em>Unfinished Business</em> documents the persisting gap",
                "summary": (
                    "Noguera and Wing show that racial tracking and the "
                    "achievement gap persist in BUSD despite four decades "
                    "of desegregation efforts."
                ),
                "context": (
                    "Pedro Noguera and Jean Yonemura Wing's edited volume "
                    "<em>Unfinished Business: Closing the Racial Achievement "
                    "Gap in Our Schools</em> drew on multi-year research at "
                    "Berkeley High to document how racial inequity persisted "
                    "in course placement, discipline, and outcomes — in a "
                    "district nationally celebrated for desegregation."
                ),
                "matters": (
                    "The book is a hinge in BUSD's self-narrative. It made "
                    "it difficult to treat the 1968 busing plan as the close "
                    "of the desegregation story and reframed the achievement "
                    "gap as a structural problem the district had documented "
                    "but not solved — the same diagnosis offered in 1963, "
                    "1977, and now 2006."
                ),
            },
            {
                "year": "2020",
                "title": "Vision 2020 and the African American Success Framework",
                "summary": (
                    "BUSD adopts new equity frameworks. By 2026, community "
                    "members report limited measurable change in outcomes "
                    "for Descendant students."
                ),
                "context": (
                    "Vision 2020 set district-wide goals for closing the "
                    "achievement gap. The African American Success Framework "
                    "was developed as a more targeted policy instrument "
                    "focused specifically on outcomes for Black students, "
                    "with stated commitments around hiring, curriculum, "
                    "discipline, and academic placement."
                ),
                "matters": (
                    "The frameworks represent the most explicit district-level "
                    "commitment to Black student outcomes since the 1968 era. "
                    "The community feedback gathered for the 2024–26 Capstone "
                    "Report indicates that adoption did not translate into "
                    "measurable change — raising the policy question of "
                    "whether the gap is in framework design, implementation, "
                    "or accountability."
                ),
            },
            {
                "year": "2024–26",
                "title": "BUSD Historical Study Capstone Report",
                "summary": (
                    "Commissioned oral histories and surveys confirm that "
                    "Descendant students continue to experience harms "
                    "consistent with patterns documented since the 1950s."
                ),
                "context": (
                    "The Capstone Report combines archival research, oral "
                    "histories, and contemporary surveys of BUSD families, "
                    "students, and educators. It was commissioned to "
                    "document the lived experience of Descendants of "
                    "enslaved people in BUSD and to support the district's "
                    "reparations work."
                ),
                "matters": (
                    "The 2024–26 findings show continuity, not discontinuity, "
                    "with the patterns documented in 1959, 1963, 1977, and "
                    "2006. That continuity is itself the central finding: "
                    "the same harms have been named, studied, and partially "
                    "remediated for nearly seventy years. The report frames "
                    "this as the case for repair."
                ),
            },
        ],
    },
]



# =============================================================================
# HTML renderer
# =============================================================================


from html import escape


# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------

CSS = """
:root {
    --ink: #1a1a1a;
    --ink-soft: #4a4a4a;
    --ink-muted: #6b6b6b;
    --ink-faint: #9b9b9b;
    --rule: rgba(0,0,0,0.10);
    --rule-strong: rgba(0,0,0,0.18);
    --paper: #ffffff;
    --surface: #f6f4ee;
    --serif: Georgia, "Times New Roman", "Iowan Old Style", serif;
    --sans: -apple-system, BlinkMacSystemFont, "Inter", "Helvetica Neue",
            Arial, sans-serif;
}

* { box-sizing: border-box; }

body {
    margin: 0;
    padding: 0;
    background: var(--paper);
    color: var(--ink);
    font-family: var(--sans);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

.tl-wrap {
    padding: 2.5rem 1.25rem 2rem;
    max-width: 680px;
    margin: 0 auto;
}

.tl-header {
    text-align: center;
    padding-bottom: 2rem;
    border-bottom: 0.5px solid var(--rule);
    margin-bottom: 2rem;
}

.tl-eyebrow {
    font-size: 11px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--ink-faint);
    margin: 0 0 0.75rem;
    font-weight: 500;
}

.tl-title {
    font-family: var(--serif);
    font-size: 30px;
    font-weight: 500;
    line-height: 1.2;
    margin: 0 0 0.6rem;
    color: var(--ink);
    letter-spacing: -0.01em;
}

.tl-sub {
    font-size: 15px;
    color: var(--ink-soft);
    margin: 0 0 1.25rem;
    line-height: 1.55;
    font-style: italic;
    font-family: var(--serif);
}

.tl-hint {
    font-size: 12px;
    color: var(--ink-faint);
    margin: 0 0 0.75rem;
    letter-spacing: 0.02em;
}

.tl-controls {
    display: flex;
    gap: 8px;
    justify-content: center;
    margin-top: 0.75rem;
}

.tl-controls button {
    font-size: 12px;
    padding: 6px 14px;
    background: transparent;
    color: var(--ink);
    border: 0.5px solid var(--rule-strong);
    border-radius: 8px;
    cursor: pointer;
    font-family: var(--sans);
    transition: background 0.12s ease, border-color 0.12s ease;
}

.tl-controls button:hover {
    background: var(--surface);
    border-color: var(--ink-faint);
}

.tl-controls button:active { transform: scale(0.98); }

.era {
    margin: 2rem 0 1.5rem;
    padding: 1.25rem 1.25rem 1rem;
    background: var(--surface);
    border-radius: 12px;
}

.era-num {
    font-size: 11px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--ink-faint);
    margin: 0 0 0.4rem;
    font-weight: 500;
}

.era-name {
    font-family: var(--serif);
    font-size: 21px;
    font-weight: 500;
    line-height: 1.3;
    margin: 0 0 0.35rem;
    color: var(--ink);
    letter-spacing: -0.005em;
}

.era-span {
    font-size: 13px;
    color: var(--ink-soft);
    margin: 0;
    font-variant-numeric: tabular-nums;
}

.events {
    position: relative;
    padding: 0.5rem 0 1rem 0;
}

.events::before {
    content: "";
    position: absolute;
    left: 88px;
    top: 0;
    bottom: 0;
    width: 0.5px;
    background: var(--rule);
}

.event {
    position: relative;
    display: grid;
    grid-template-columns: 76px 1fr;
    gap: 24px;
    padding: 0.6rem 0;
    align-items: flex-start;
}

.event-year {
    font-family: var(--serif);
    font-size: 15px;
    font-weight: 500;
    color: var(--ink);
    text-align: right;
    padding-top: 14px;
    font-variant-numeric: tabular-nums;
    line-height: 1.3;
}

.event-dot {
    position: absolute;
    left: 84px;
    top: 1.4rem;
    width: 9px;
    height: 9px;
    border-radius: 50%;
    background: var(--paper);
    border: 1.5px solid var(--ink);
    z-index: 1;
    transition: background 0.15s ease;
}

.event.open .event-dot { background: var(--ink); }

.event-card { padding-left: 12px; }

.event-toggle {
    width: 100%;
    text-align: left;
    background: transparent;
    border: 0;
    padding: 10px 36px 10px 0;
    cursor: pointer;
    position: relative;
    border-radius: 8px;
    transition: background 0.12s ease;
    font-family: var(--sans);
    color: inherit;
}

.event-toggle:hover { background: var(--surface); }

.event-toggle:focus-visible {
    outline: none;
    box-shadow: 0 0 0 2px rgba(50, 100, 200, 0.45);
}

.event-headline {
    font-size: 15.5px;
    font-weight: 600;
    line-height: 1.4;
    margin: 0 0 0.4rem;
    color: var(--ink);
    padding: 0 8px;
}

.event-desc {
    font-size: 14px;
    line-height: 1.65;
    color: var(--ink-soft);
    margin: 0;
    padding: 0 8px;
}

.chev {
    position: absolute;
    right: 8px;
    top: 14px;
    width: 12px;
    height: 12px;
    color: var(--ink-faint);
    transition: transform 0.2s ease;
}

.event.open .chev { transform: rotate(180deg); }

.event-detail {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease;
}

.event.open .event-detail { max-height: 1200px; }

.event-detail-inner {
    margin: 8px 8px 12px 12px;
    padding: 16px 18px;
    background: var(--surface);
    border-left: 2px solid var(--rule-strong);
    border-radius: 0 8px 8px 0;
}

.detail-label {
    font-size: 10px;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--ink-faint);
    font-weight: 600;
    margin: 0 0 6px;
}

.detail-label + p { margin-top: 0; }

.event-detail p {
    font-size: 13.5px;
    line-height: 1.7;
    color: var(--ink-soft);
    margin: 0 0 12px;
}

.event-detail p:last-child { margin-bottom: 0; }

.event-detail .detail-section + .detail-section {
    margin-top: 16px;
    padding-top: 16px;
    border-top: 0.5px solid var(--rule);
}

.tl-foot {
    margin-top: 2rem;
    padding: 1.25rem 0 0;
    border-top: 0.5px solid var(--rule);
    text-align: center;
}

.tl-foot p {
    font-size: 12px;
    color: var(--ink-faint);
    margin: 0;
    line-height: 1.5;
    font-style: italic;
    font-family: var(--serif);
}

.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0,0,0,0);
    white-space: nowrap;
    border: 0;
}
"""


# ---------------------------------------------------------------------------
# Vanilla JS for expand/collapse — runs once on load
# ---------------------------------------------------------------------------

JS = """
(function() {
    var toggles = document.querySelectorAll('.event-toggle');
    toggles.forEach(function(btn) {
        btn.addEventListener('click', function() {
            var ev = btn.closest('.event');
            var open = ev.classList.toggle('open');
            btn.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
    });

    var expandBtn = document.getElementById('expand-all');
    var collapseBtn = document.getElementById('collapse-all');

    if (expandBtn) {
        expandBtn.addEventListener('click', function() {
            document.querySelectorAll('.event').forEach(function(ev) {
                ev.classList.add('open');
                var t = ev.querySelector('.event-toggle');
                if (t) t.setAttribute('aria-expanded', 'true');
            });
        });
    }

    if (collapseBtn) {
        collapseBtn.addEventListener('click', function() {
            document.querySelectorAll('.event').forEach(function(ev) {
                ev.classList.remove('open');
                var t = ev.querySelector('.event-toggle');
                if (t) t.setAttribute('aria-expanded', 'false');
            });
        });
    }
})();
"""


# ---------------------------------------------------------------------------
# HTML assembly
# ---------------------------------------------------------------------------

# A small set of inline tags we allow through unescaped in event copy so
# titles like "Plessy v. Ferguson" can render in italics. Any other HTML in
# the data file is treated as text.
ALLOWED_INLINE_TAGS = ("<em>", "</em>", "<i>", "</i>", "<br>", "<br/>", "<br />")


def _safe_inline(text: str) -> str:
    """Escape user content but preserve a small allowed inline tag set."""
    escaped = escape(text)
    for tag in ALLOWED_INLINE_TAGS:
        escaped_tag = escape(tag)
        escaped = escaped.replace(escaped_tag, tag)
    return escaped


def _render_event(event: dict) -> str:
    year = _safe_inline(event["year"])
    title = _safe_inline(event["title"])
    summary = _safe_inline(event["summary"])
    context = _safe_inline(event["context"])
    matters = _safe_inline(event["matters"])

    return f"""
    <div class="event">
        <div class="event-year">{year}</div>
        <div class="event-dot"></div>
        <div class="event-card">
            <button class="event-toggle" type="button" aria-expanded="false">
                <p class="event-headline">{title}</p>
                <p class="event-desc">{summary}</p>
                <svg class="chev" viewBox="0 0 12 12" fill="none"
                     stroke="currentColor" stroke-width="1.5">
                    <path d="M2 4l4 4 4-4"/>
                </svg>
            </button>
            <div class="event-detail">
                <div class="event-detail-inner">
                    <div class="detail-section">
                        <p class="detail-label">Context</p>
                        <p>{context}</p>
                    </div>
                    <div class="detail-section">
                        <p class="detail-label">Why it matters</p>
                        <p>{matters}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """


def _render_era(era: dict) -> str:
    label = _safe_inline(era["label"])
    name = _safe_inline(era["name"])
    span = _safe_inline(era["span"])
    events_html = "\n".join(_render_event(ev) for ev in era["events"])

    return f"""
    <section class="era">
        <p class="era-num">{label}</p>
        <h2 class="era-name">{name}</h2>
        <p class="era-span">{span}</p>
    </section>
    <div class="events">
        {events_html}
    </div>
    """


def render_timeline_html(header: dict, eras: list, footer_text: str) -> str:
    """Build the full self-contained HTML document for the timeline."""
    eyebrow = _safe_inline(header["eyebrow"])
    title = _safe_inline(header["title"])
    subtitle = _safe_inline(header["subtitle"])
    hint = _safe_inline(header["hint"])
    footer = _safe_inline(footer_text)

    eras_html = "\n".join(_render_era(era) for era in eras)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>On Paper, Not in Practice — BUSD Historical Timeline</title>
<style>{CSS}</style>
</head>
<body>
<h1 class="sr-only">
    On Paper, Not in Practice: a timeline of Black educational experience
    in Berkeley Unified School District from 1856 to 2026.
</h1>

<div class="tl-wrap">

    <div class="tl-header">
        <p class="tl-eyebrow">{eyebrow}</p>
        <h1 class="tl-title">{title}</h1>
        <p class="tl-sub">{subtitle}</p>
        <p class="tl-hint">{hint}</p>
        <div class="tl-controls">
            <button type="button" id="expand-all">Expand all</button>
            <button type="button" id="collapse-all">Collapse all</button>
        </div>
    </div>

    {eras_html}

    <div class="tl-foot">
        <p>{footer}</p>
    </div>

</div>

<script>{JS}</script>
</body>
</html>
"""



# =============================================================================
# Sidebar
# =============================================================================

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


# =============================================================================
# Main content
# =============================================================================

timeline_html = render_timeline_html(
    header=HEADER,
    eras=ERAS,
    footer_text=FOOTER_TEXT,
)

st.components.v1.html(timeline_html, height=4200, scrolling=True)
