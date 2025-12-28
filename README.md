# 🎬 Video-to-MP3 Converter
### A Private, Local-First Audio Extraction Tool

[![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/PranjalPanging/Video-MP3-Converter?style=social)](https://github.com/PranjalPanging/Video-MP3-Converter/stargazers)

**Video-to-MP3 Converter** is a lightweight web application that allows you to extract audio from video files instantly. Unlike online converters, this tool works **entirely on your local machine**, meaning your videos are never uploaded to a server. 

---

## 🚀 Features
* **Privacy Focused:** All processing happens locally. No data is sent to the cloud.
* **Fast Extraction:** Uses the power of **FFmpeg** for high-speed audio demuxing.
* **Clean UI:** Built with **Tailwind CSS** for a modern, responsive look.
* **Simple Workflow:** Just upload, wait for the conversion, and download your MP3.

---

## 📐 How it Works
The application uses a **Flask** backend to handle the file system and process the conversion logic.



1.  **Frontend:** A JavaScript-powered interface handles the file selection and progress state.
2.  **Backend:** Flask receives the video and saves it to a temporary directory.
3.  **Engine:** The system executes an FFmpeg command to strip the video stream and encode the audio into a high-quality MP3 file.
4.  **Cleanup:** Temporary files are managed to ensure your storage stays clean.

---

## 🛠️ Installation

### 1. Prerequisites
You must have **FFmpeg** installed on your system for this app to work:
* **Windows:** `winget install ffmpeg`
* **macOS:** `brew install ffmpeg`
* **Linux:** `sudo apt install ffmpeg`

### 2. Clone and Setup
```bash
# Clone the repository
git clone https://github.com/PranjalPanging/Video-MP3-Converter.git
cd Video-MP3-Converter

# Create a virtual environment
python -m venv venv

# Activate the environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
### 3. Run the App
```
python app.py
```
Visit: http://127.0.0.1:5000

### 🧪 Tech Stack
- Language: Python 3.x
- Web Framework: Flask
- Styling: Tailwind CSS
- Core Engine: FFmpeg (via subprocess)

### 🤝 Contributing
I am a student developer and I am always looking for ways to make my code better. If you have ideas for:
- Supporting more formats (WAV, AAC, OGG).
- Batch processing multiple videos at once.
- Adding a "Dark Mode" toggle.
Please feel free to open an issue or submit a pull request!

### 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
