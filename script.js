const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const uploadTitle = document.getElementById("uploadTitle");
const uploadText = document.getElementById("uploadText");
const analyzeBtn = document.getElementById("analyzeBtn");
const form = document.querySelector(".upload-box");
const languageChips = document.querySelectorAll(".language-chip");

let selectedLanguages = [];

// Language Selection
languageChips.forEach(chip => {

    chip.addEventListener("click", () => {

        chip.classList.toggle("active");

        selectedLanguages = [...document.querySelectorAll(".language-chip.active")]
            .map(chip => chip.textContent.trim());

        console.log(selectedLanguages);

    });

});

// Image Preview
imageInput.addEventListener("change", () => {

    const file = imageInput.files[0];

    if (!file) return;

    preview.src = URL.createObjectURL(file);
    preview.style.display = "block";

    uploadTitle.textContent = "✅ Image Ready!";
    uploadText.textContent = file.name;

    analyzeBtn.disabled = false;

});

// Analyze
form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const file = imageInput.files[0];

    if (!file) {
        alert("Please upload an image.");
        return;
    }

    if (selectedLanguages.length === 0) {
        alert("Please select at least one language.");
        return;
    }

    analyzeBtn.textContent = "Analyzing...";
    analyzeBtn.disabled = true;

    const formData = new FormData();

    formData.append("image", file);

// Send selected languages
    formData.append("languages", JSON.stringify(selectedLanguages));


    try {

        const response = await fetch("https://vibe-sync-qa2g.onrender.com//analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        console.log(data);

        const result = document.getElementById("result");

        let html = `

        <h2>✨ AI Vibe Analysis</h2>

        <p><strong>🎭 Mood:</strong> ${data.analysis.mood}</p>

        <p><strong>🎨 Aesthetic:</strong> ${data.analysis.aesthetic}</p>

        <p><strong>💡 Lighting:</strong> ${data.analysis.lighting}</p>

        <p><strong>📍 Scene:</strong> ${data.analysis.scene}</p>

        <p><strong>🌈 Colors:</strong> ${data.analysis.dominant_colors.join(", ")}</p>

        <p><strong>❤️ Emotions:</strong> ${data.analysis.emotions.join(", ")}</p>

        <p><strong>🏷️ Keywords:</strong> ${data.analysis.keywords.join(", ")}</p>

        <p><strong>🎯 Confidence:</strong> ${data.analysis.confidence}%</p>

        <hr>

        <h2>🎵 Recommended Songs</h2>

        `;

        data.recommendations.forEach(song => {

            html += `

            <div class="song-card">

                <h3>${song.title}</h3>

                <p><strong>Artist:</strong> ${song.artist}</p>

                <p><strong>⭐ Score:</strong> ${song.score}</p>

                <p><strong>🔥 Popularity:</strong> ${song.popularity}</p>

            </div>

            `;

        });

        result.innerHTML = html;
        result.style.display = "block";

    }
    catch (error) {

        console.error(error);
        alert("Backend connection failed!");

    }

    analyzeBtn.textContent = "Analyze Vibe";
    analyzeBtn.disabled = false;

});