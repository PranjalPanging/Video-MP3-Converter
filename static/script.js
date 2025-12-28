const uploadForm = document.getElementById("uploadForm");
const videoInput = document.getElementById("videoInput");
const submitBtn = document.getElementById("submitBtn");
const btnText = document.getElementById("btnText");
const fileNameDisplay = document.getElementById("fileName");
const successState = document.getElementById("successState");
const downloadLink = document.getElementById("downloadLink");
const completedFileName = document.getElementById("completedFileName");

let mp3Blob = null;
videoInput.addEventListener("change", function () {
  if (this.files[0]) {
    fileNameDisplay.textContent = this.files[0].name;
    submitBtn.disabled = false;
    submitBtn.classList.remove("opacity-50", "cursor-not-allowed");
    btnText.textContent = "Start Conversion";
  }
});
uploadForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const file = videoInput.files[0];
  if (!file) return;
  submitBtn.disabled = true;
  submitBtn.classList.add("opacity-50", "cursor-not-allowed");
  btnText.textContent = "Processing...";

  const formData = new FormData();
  formData.append("video", file);

  try {
    const response = await fetch("/convert", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(errorText || "Server error during conversion.");
    }
    mp3Blob = await response.blob();
    const url = URL.createObjectURL(mp3Blob);
    const originalName = file.name.replace(/\.[^/.]+$/, "");
    downloadLink.href = url;
    downloadLink.download = `${originalName}.mp3`;
    completedFileName.textContent = `${originalName}.mp3`;
    uploadForm.classList.add("hidden");
    successState.classList.remove("hidden");
  } catch (err) {
    console.error(err);
    alert("Error: " + err.message);
    submitBtn.disabled = false;
    submitBtn.classList.remove("opacity-50", "cursor-not-allowed");
    btnText.textContent = "Start Conversion";
  }
});
