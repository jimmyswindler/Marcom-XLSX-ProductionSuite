## 2026-02-12 - Initial Project Setup
**Learning:** Setting up a project from scratch allows for foundational accessibility choices (semantic HTML, focus management) that are harder to retrofit later.
**Action:** Always include a `skip-to-content` link and proper `lang` attribute in the initial template.

## 2026-02-16 - Reduced Motion Support
**Learning:** Overriding global transitions with `*` selector requires `!important` to be effective against specific selectors, and `0.01ms` is safer than `0s` for event listeners.
**Action:** Use the standard CSS snippet for reduced motion in all future projects to ensure broad coverage.

## 2026-02-21 - Dark Mode & Skip Link Robustness
**Learning:** Skip links pointing to non-interactive elements (like `<main>`) fail to move focus in some browsers unless the target has `tabindex="-1"`.
**Action:** Audit all skip links to ensure their target container has `tabindex="-1"`.

**Learning:** Dark mode implementation requires script execution in `<head>` to block rendering and prevent "Flash of Unstyled Theme" (FOUT), which is jarring for users.
**Action:** Always place theme initialization logic in `<head>`, separate from the toggle event listeners in `<body>` or deferred scripts.
