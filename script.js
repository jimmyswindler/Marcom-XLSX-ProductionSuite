document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('theme-toggle');
    const root = document.documentElement;

    function updateButton() {
        const isDark = root.getAttribute('data-theme') === 'dark';
        if (toggleButton) {
            toggleButton.textContent = isDark ? '☀️' : '🌙';
            toggleButton.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
        }
    }

    // Initialize button state
    updateButton();

    if (toggleButton) {
        toggleButton.addEventListener('click', () => {
            const isDark = root.getAttribute('data-theme') === 'dark';
            const newTheme = isDark ? 'light' : 'dark';

            if (newTheme === 'dark') {
                root.setAttribute('data-theme', 'dark');
            } else {
                root.removeAttribute('data-theme');
            }

            localStorage.setItem('theme', newTheme);
            updateButton();
        });
    }
});
