## 2026-02-12 - CSS Performance: Layout Thrashing
**Learning:** Animating properties like `top`, `left`, `margin`, or `padding` forces the browser to recalculate layout (reflow) on every frame, which is expensive.
**Action:** Always prefer `transform: translate()` for movement animations as it only triggers composition, which is much faster and smoother.
