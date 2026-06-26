const memo = document.getElementById("memo");
const saveBtn = document.getElementById("saveBtn");
const loadBtn = document.getElementById("loadBtn");
const statusEl = document.getElementById("status");

function setStatus(message, type = "") {
    statusEl.textContent = message;
    statusEl.className = `status ${type}`;
}

async function saveNote() {
    try {
        const text = memo.value;

        const result = await window.pywebview.api.save_note(text);

        setStatus(`저장되었습니다: ${result.path}`, "success");
    } catch (error) {
        console.error(error);
        setStatus("저장 중 오류가 발생했습니다.", "error");
    }
}

async function loadNote() {
    try {
        const result = await window.pywebview.api.load_note();

        memo.value = result.text || "";
        setStatus("메모를 불러왔습니다.", "success");
    } catch (error) {
        console.error(error);
        setStatus("불러오기 중 오류가 발생했습니다. 아직 저장된 메모가 없을 수 있습니다.", "error");
    }
}

saveBtn.addEventListener("click", saveNote);
loadBtn.addEventListener("click", loadNote);

document.addEventListener("keydown", (event) => {
    if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "s") {
        event.preventDefault();
        saveNote();
    }

    if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "o") {
        event.preventDefault();
        loadNote();
    }
});

window.addEventListener("pywebviewready", () => {
    loadNote();
});
