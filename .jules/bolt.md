# Bolt's Journal

## 2026-02-12 - Initial Setup
**Learning:** This journal tracks critical performance learnings specific to this project.
**Action:** Consult this file before making architectural decisions.

## 2026-02-12 - Animation Performance
**Learning:** Animating `top` triggers layout reflows which are expensive.
**Action:** Use `transform` (e.g., `translateY`) for position animations to strictly trigger composition.
