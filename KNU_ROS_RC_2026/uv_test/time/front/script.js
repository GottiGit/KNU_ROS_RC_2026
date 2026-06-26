const timeEl = document.getElementById('time');
const dateEl = document.getElementById('date');

async function refreshClock() {
    try {
        const payload = await window.pywebview.api.getClockPayload();
        if (!payload) {
            return;
        }

        timeEl.textContent = payload.time;
        dateEl.textContent = payload.date;
    } catch (error) {
        // Temporary API errors should not crash the demo UI.
    }
}

window.addEventListener('pywebviewready', () => {
    refreshClock();
    setInterval(refreshClock, 1000);
});
