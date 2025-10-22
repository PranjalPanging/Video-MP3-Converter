# Video-MP3-Converter
A web app that lets users upload video files and extract audio as MP3. Built with Flask, Tailwind CSS, and JavaScript, it provides a clean, responsive interface for safe, local video-to-audio conversion.

## 🛠️ Installation

### 1. Clone the repository
```
git clone https://github.com/PranjalPanging/Video-MP3-Converter.git
cd video-to-audio
```
### 2. Create and activate a virtual environment
```
python -m venv venv
```
##### 2.1 On Windows
```
venv\Scripts\activate
```
##### 2.2 On macOS/Linux
```
source venv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Install FFmpeg

FFmpeg is required for audio extraction.

#### 4.1 Windows

<li> Download from https://ffmpeg.org/download.html </li>

<li>Extract it and add the bin folder to your PATH environment variable.</li>

#### 4.2 macOS

```
brew install ffmpeg

```
#### 4.3 Linux (Ubuntu/Debian)
```
sudo apt update
sudo apt install ffmpeg
```
To verify installation:
```
ffmpeg -version
```
### 5. Run the App
```
python app.py
```
Then open your browser and visit:
```
http://127.0.0.1:5000
```
### 6. Usage
<li>Click Upload Video and select a video file.</li>
<li>Wait for the conversion to complete.</li>
<li>Click Download MP3 to save the extracted audio.</li>

### 7. Tech Stack
<li>Backend: Flask</li>
<li>Frontend: Html, Tailwind CSS, JavaScript</li>
<li>Audio Processing: FFmpeg</li>

### 8. Contributing
Pull requests and issues are welcome!
If you’d like to improve the UI, add new features, or fix bugs — feel free to contribute.

### 9. License
This project is licensed under the MIT License.
