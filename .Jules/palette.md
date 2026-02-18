## 2026-02-12 - Initial Project Setup
**Learning:** Setting up a project from scratch allows for foundational accessibility choices (semantic HTML, focus management) that are harder to retrofit later.
**Action:** Always include a `skip-to-content` link and proper `lang` attribute in the initial template.
\n## 2026-02-12 - Skip Link Focus Management
**Learning:** Skip links targeting non-interactive elements like <main> fail to move focus programmatically without tabindex="-1".
**Action:** Always add tabindex="-1" to the target container of a skip link.
