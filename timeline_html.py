"""
Render the timeline as a self-contained HTML string for embedding in
Streamlit via st.components.v1.html.

The component is fully self-contained: it includes its own styles and
the small JS handler for expand/collapse interactions. It does not depend
on any of Streamlit's own theming so it renders consistently inside the
component iframe.
"""

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
