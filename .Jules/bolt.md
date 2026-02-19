## 2026-02-19 - FOUT Prevention with Script Deferral
**Learning:** Loading `script.js` synchronously blocks rendering, but deferring it without handling theme initialization inline causes a Flash of Unstyled Theme (FOUT).
**Action:** Extract critical theme initialization logic to an inline script in `<head>` and defer the main bundle to unblock rendering while maintaining correct initial state.
