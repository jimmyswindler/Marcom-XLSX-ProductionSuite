## 2026-02-20 - Skip Link Animation Performance
**Learning:** Animating `top` triggers layout recalculations (reflows) on every frame. Using `transform: translateY` promotes the element to its own layer and only triggers compositing, which is much cheaper.
**Action:** Always prefer `transform` over `top`, `left`, `margin`, or `padding` for animations, especially for frequent interactions like focus.
