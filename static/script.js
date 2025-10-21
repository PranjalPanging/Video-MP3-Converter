const proceedBtn = document.getElementById("proceedBtn");
const downloadBtn = document.getElementById("downloadBtn");
const fileInput = document.getElementById("fileInput");
const status = document.getElementById("status");

let mp3Blob = null;

proceedBtn.addEventListener("click", async () => {
  const file = fileInput.files[0];
  if (!file) {
    status.textContent = "Choose a video file first.";
    return;
  }

  status.textContent = "Uploading and converting...";

  const form = new FormData();
  form.append("video", file);

  try {
    const res = await fetch("/convert", {
      method: "POST",
      body: form,
    });

    if (!res.ok) {
      const txt = await res.text();
      throw new Error(txt || "Server error");
    }

    mp3Blob = await res.blob();

    status.textContent =
      'Conversion complete. Click "Download" to get your MP3.';
    downloadBtn.classList.remove("hidden");
  } catch (err) {
    status.textContent = "Error: " + err.message;
  }
});

downloadBtn.addEventListener("click", () => {
  if (!mp3Blob) return;

  const a = document.createElement("a");
  a.href = URL.createObjectURL(mp3Blob);
  const originalName = fileInput.files[0].name.replace(/\.[^/.]+$/, "");
  a.download = `${originalName}.mp3`;
  a.click();
});
