// app.js
// 방향/속도 제어는 fetch()로 REST 호출, 상태/센서는 SSE로 실시간 수신

const connStatusEl = document.getElementById("conn-status");
const currentDirectionEl = document.getElementById("current-direction");
const speedSlider = document.getElementById("speed-slider");
const speedValueEl = document.getElementById("speed-value");

const sensorDistanceEl = document.getElementById("sensor-distance");
const sensorBatteryEl = document.getElementById("sensor-battery");
const sensorYawEl = document.getElementById("sensor-yaw");
const sensorUpdatedEl = document.getElementById("sensor-updated");

const directionButtons = document.querySelectorAll(".dpad__btn");

function setConnStatus(ok) {
  connStatusEl.textContent = ok ? "연결됨" : "연결 끊김";
  connStatusEl.className = "status " + (ok ? "status--ok" : "status--fail");
}

function highlightDirection(direction) {
  directionButtons.forEach((btn) => {
    btn.classList.toggle("is-active", btn.dataset.direction === direction);
  });
  currentDirectionEl.textContent = direction;
}

function formatTime(ts) {
  const date = new Date(ts * 1000);
  return date.toLocaleTimeString();
}

// ----------------------------------------------------------------------
// 방향 / 속도 제어 (REST)
// ----------------------------------------------------------------------
async function postJson(path, body) {
  const res = await fetch(path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body ?? {}),
  });
  if (!res.ok) {
    throw new Error(`request failed: ${res.status}`);
  }
  return res.json();
}

directionButtons.forEach((btn) => {
  btn.addEventListener("click", async () => {
    const direction = btn.dataset.direction;
    try {
      const state = await postJson("/api/control/direction", { direction });
      highlightDirection(state.direction);
      setConnStatus(true);
    } catch (err) {
      setConnStatus(false);
    }
  });
});

let speedDebounceTimer = null;
speedSlider.addEventListener("input", () => {
  const value = Number(speedSlider.value);
  speedValueEl.textContent = value;

  clearTimeout(speedDebounceTimer);
  speedDebounceTimer = setTimeout(async () => {
    try {
      await postJson("/api/control/speed", { speed: value });
      setConnStatus(true);
    } catch (err) {
      setConnStatus(false);
    }
  }, 100);
});

// ----------------------------------------------------------------------
// 초기 상태 불러오기
// ----------------------------------------------------------------------
async function loadInitialState() {
  try {
    const res = await fetch("/api/state");
    const state = await res.json();
    highlightDirection(state.direction);
    speedSlider.value = state.speed;
    speedValueEl.textContent = state.speed;
    setConnStatus(true);
  } catch (err) {
    setConnStatus(false);
  }
}

loadInitialState();

// ----------------------------------------------------------------------
// 상태 SSE (여러 창 동기화)
// ----------------------------------------------------------------------
const stateEvents = new EventSource("/api/state/events");

stateEvents.addEventListener("message", (event) => {
  const state = JSON.parse(event.data);
  highlightDirection(state.direction);
  speedSlider.value = state.speed;
  speedValueEl.textContent = state.speed;
  setConnStatus(true);
});

stateEvents.addEventListener("error", () => {
  setConnStatus(false);
});

// ----------------------------------------------------------------------
// 센서 SSE (주기적 push)
// ----------------------------------------------------------------------
const sensorEvents = new EventSource("/api/sensors/events");

sensorEvents.addEventListener("message", (event) => {
  const sensor = JSON.parse(event.data);
  sensorDistanceEl.textContent = sensor.distance_cm;
  sensorBatteryEl.textContent = sensor.battery_pct;
  sensorYawEl.textContent = sensor.imu_yaw_deg;
  sensorUpdatedEl.textContent = formatTime(sensor.timestamp);
});

sensorEvents.addEventListener("error", () => {
  setConnStatus(false);
});