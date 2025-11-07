
# 🎬 Video-to-MP3 Converter

[![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Issues](https://img.shields.io/github/issues/PranjalPanging/Video-MP3-Converter)](https://github.com/PranjalPanging/Video-MP3-Converter/issues)
[![GitHub stars](https://img.shields.io/github/stars/PranjalPanging/Video-MP3-Converter?style=social)](https://github.com/PranjalPanging/Video-MP3-Converter/stargazers)

**Video-to-MP3 Converter** is a sleek web application that allows users to upload video files and extract audio in MP3 format. Built with **Flask**, **Tailwind CSS**, and **JavaScript**, it provides a clean, responsive interface for safe, fast, and local video-to-audio conversion.

---

## 🛠️ Features
- Upload videos and convert them to MP3 effortlessly.
- Responsive and intuitive UI with **Tailwind CSS**.
- Fast, local conversion using **FFmpeg** (no cloud uploads required).
- Cross-platform support (Windows, macOS, Linux).

---

## Installation

1.    Clone the Repository
```bash
git clone https://github.com/PranjalPanging/Video-MP3-Converter.git
cd Video-MP3-Converter
```
2.   Create & Activate a Virtual Environment
```
python -m venv venv
```
-    Windows
```bash
venv\Scripts\activate
```
-    macOS / Linux

```
source venv/bin/activate
```
3.    Install Dependencies
```
pip install -r requirements.txt
```
4.   Run the Application
```
python app.py
```
Open your browser and go to:

```
http://127.0.0.1:5000
```
## Usage
-   Click Upload Video and select your video file.
-   Wait for the conversion to complete.
-   Click Download MP3 to save your audio file.

## Tech Stack
-   Backend: Flask
-   Frontend: HTML, Tailwind CSS, JavaScript
-   Audio Processing: FFmpeg

## Contributing
Contributions are welcome!

-   Improve the UI/UX
-   Add new features
-   Fix bugs or optimize performance
-   Please fork the repository, make changes, and submit a Pull Request.

## License
This project is licensed under the MIT License.
