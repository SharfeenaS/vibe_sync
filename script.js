const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const uploadTitle = document.getElementById("uploadTitle");
const uploadText = document.getElementById("uploadText");
const analyzeBtn = document.getElementById("analyzeBtn");
const form = document.querySelector(".upload-box");

imageInput.addEventListener("change", function () {

    const file = this.files[0];

    if (!file) return;

    preview.src = URL.createObjectURL(file);
    preview.style.display = "block";

    uploadTitle.textContent = "✅ Image Ready!";
    uploadText.textContent = file.name;

    analyzeBtn.disabled = false;

});

form.addEventListener("submit", function (e) {

    e.preventDefault();

    analyzeBtn.textContent = "Analyzing...";

    analyzeBtn.disabled = true;

    // AI integration comes here in the next phase

    setTimeout(() => {

        analyzeBtn.textContent = "Analyze Vibe";
        analyzeBtn.disabled = false;

    }, 2000);

});