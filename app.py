import os
import tempfile
import subprocess
import platform
from flask import Flask, request, send_file, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Adjust this string if your bin folder is named differently!
LOCAL_FFMPEG = os.path.join(BASE_DIR, 'ffmpeg', 'bin', 'ffmpeg.exe')

print(f"--- DEBUG INFO ---")
print(f"Checking for local FFmpeg at: {LOCAL_FFMPEG}")
if os.path.exists(LOCAL_FFMPEG):
    print("STATUS: Local FFmpeg FOUND.")
else:
    print("STATUS: Local FFmpeg NOT FOUND. Will try system 'ffmpeg'.")
print(f"------------------")

def get_ffmpeg_command():
    if platform.system() == "Windows" and os.path.exists(LOCAL_FFMPEG):
        return LOCAL_FFMPEG
    return 'ffmpeg'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/how-it-works')
def how_it_works():
    return render_template('how_it_works.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'video' not in request.files:
        return "No file uploaded", 400

    video = request.files['video']
    if video.filename == '':
        return "Empty filename", 400

    # Create temp files
    suffix = os.path.splitext(video.filename)[1]
    input_tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    input_path = input_tmp.name
    input_tmp.close()
    video.save(input_path)

    output_tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    output_path = output_tmp.name
    output_tmp.close()

    try:
        cmd = [
            get_ffmpeg_command(),
            '-y',
            '-i', input_path,
            '-vn',
            '-acodec', 'libmp3lame',
            '-q:a', '2',          
            output_path
        ]

        proc = subprocess.run(
            cmd, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True, 
            shell=(platform.system() == "Windows")
        )

        if proc.returncode != 0:
            return f"Conversion error: {proc.stderr}", 500

        return send_file(
            output_path, 
            mimetype='audio/mpeg', 
            as_attachment=True,
            download_name=os.path.splitext(video.filename)[0] + '.mp3'
        )
    finally:
        for path in [input_path, output_path]:
            try:
                if os.path.exists(path):
                    os.remove(path)
            except:
                pass

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True, host='0.0.0.0', port=5000)