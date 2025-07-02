
const okButton = document.getElementById("ok-button");
const welcomeScreen = document.getElementById("welcome-screen");
const mainUI = document.getElementById("main-ui");

okButton.addEventListener("click", () => {
    welcomeScreen.style.display = "none";
    disclaimer.style.display = "none";
    description.style.display = "none";
    mainUI.style.display = "block";
});

const dropArea = document.getElementById("drop-area");
const fileInput = document.getElementById("fileElem");
const preview = document.getElementById("preview");
const result = document.getElementById("result");

dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.classList.add("hover");
});

dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("hover");
});

dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    dropArea.classList.remove("hover");
    const file = e.dataTransfer.files[0];
    handleImage(file);
});

fileInput.addEventListener("change", () => {
    const file = fileInput.files[0];
    handleImage(file);
});

function handleImage(file) {
    if (!file) return;
    preview.innerHTML = `<img src="${URL.createObjectURL(file)}" alt="Preview" width="200"/>`;
    result.textContent = "Predicting...";

    const formData = new FormData();
    formData.append("file", file);

    fetch("/predict", {
        method: "POST",
        body: formData
    })
    .then((response) => response.json())
    .then((data) => {
        result.innerHTML = `
            <strong>Prediction:</strong> ${data["predicted_class"]}<br>
            <strong>Confidence:</strong> ${data["confidence"]}%<br>
            <strong>Remedy:</strong> ${data["remedy"]}<br>
            <a href="${data["google_search_url"]}" target="_blank" class="learn_more">🔎 Learn More</a>
        `;
    })
    .catch(() => {
        result.textContent = "Error in prediction. Please try again.";
    });
}
