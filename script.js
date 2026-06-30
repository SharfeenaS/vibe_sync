const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const uploadTitle = document.getElementById("uploadTitle");
const uploadText = document.getElementById("uploadText");
const analyzeBtn = document.getElementById("analyzeBtn");
const form = document.querySelector(".upload-box");

imageInput.addEventListener("change", () => {

    const file = imageInput.files[0];

    if (!file) return;

    preview.src = URL.createObjectURL(file);
    preview.style.display = "block";

    uploadTitle.textContent = "✅ Image Ready!";
    uploadText.textContent = file.name;

    analyzeBtn.disabled = false;

});

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const file = imageInput.files[0];

    if (!file) {
        alert("Please upload an image.");
        return;
    }

    analyzeBtn.textContent = "Analyzing...";
    analyzeBtn.disabled = true;

    const formData = new FormData();
    formData.append("image", file);

    try {

        const response = await fetch("http://127.0.0.1:8000/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        alert(JSON.stringify(data, null, 2));

    } catch (error) {

        alert("Backend connection failed!");
        console.error(error);

    }

    analyzeBtn.textContent = "Analyze Vibe";
    analyzeBtn.disabled = false;

});