## 2026-02-12 - Initial Project Setup
**Learning:** Setting up a project from scratch allows for foundational accessibility choices (semantic HTML, focus management) that are harder to retrofit later.
**Action:** Always include a `skip-to-content` link and proper `lang` attribute in the initial template.

## 2026-02-14 - Reduced Motion and Global Transitions
**Learning:** When using global transitions (like on `body` for theme switching), it is critical to provide a `prefers-reduced-motion` override to prevent motion sickness.
**Action:** Always pair `transition` properties with a `@media (prefers-reduced-motion: reduce)` block that disables them.
