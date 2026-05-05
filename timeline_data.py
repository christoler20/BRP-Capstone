"""
Timeline data for the BUSD Historical Study Capstone Report.

Each event has:
    - year:     short label rendered next to the timeline rail
    - title:    bold headline
    - summary:  1–2 sentence collapsed description
    - context:  expanded historical background
    - matters:  expanded "why it matters" / pattern-level significance

Edit this file to revise content; the app picks up changes on rerun.
"""

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
