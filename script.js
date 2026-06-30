const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const uploadTitle = document.getElementById("uploadTitle");
const uploadText = document.getElementById("uploadText");
const analyzeBtn = document.getElementById("analyzeBtn");
const form = document.querySelector(".upload-box");
const languageChips = document.querySelectorAll(".language-chip");

let selectedLanguages = [];

languageChips.forEach(chip => {

    chip.addEventListener("click", () => {

        chip.classList.toggle("active");

        selectedLanguages = [...document.querySelectorAll(".language-chip.active")]
            .map(chip => chip.textContent.trim());

        console.log(selectedLanguages);

    });

});
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
if(selectedLanguages.length === 0){

    alert("Please select at least one language.");

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
        console.log(data);

        const result = document.getElementById("result");

result.style.display = "block";

result.innerHTML = `
<h2>✨ AI Vibe Analysis</h2>

<p><strong>🎭 Mood:</strong> ${data.mood}</p>

<p><strong>🎨 Aesthetic:</strong> ${data.aesthetic}</p>

<p><strong>💡 Lighting:</strong> ${data.lighting}</p>

<p><strong>📍 Scene:</strong> ${data.scene}</p>

<p><strong>🌈 Colors:</strong> ${data.dominant_colors.join(", ")}</p>

<p><strong>❤️ Emotions:</strong> ${data.emotions.join(", ")}</p>

<p><strong>🏷️ Keywords:</strong> ${data.keywords.join(", ")}</p>

<p><strong>🎯 Confidence:</strong> ${data.confidence}%</p>
`;

    } catch (error) {

        alert("Backend connection failed!");
        console.error(error);

    }

    analyzeBtn.textContent = "Analyze Vibe";
    analyzeBtn.disabled = false;

});