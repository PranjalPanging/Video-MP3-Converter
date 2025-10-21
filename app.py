import os
import tempfile
import subprocess
from flask import Flask, request, send_file, render_template, abort

app = Flask(__name__, static_folder='static', template_folder='templates')

app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'video' not in request.files:
        return "No file uploaded", 400

    video = request.files['video']
    if video.filename == '':
        return "Empty filename", 400

    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(video.filename)[1]) as input_tmp:
        input_path = input_tmp.name
        video.save(input_path)

    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as output_tmp:
        output_path = output_tmp.name

    try:
        cmd = [
            'ffmpeg',
            '-y',
            '-i', input_path,
            '-vn',
            '-acodec', 'libmp3lame',
            '-q:a', '2',          
            output_path
        ]

        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if proc.returncode != 0:
            error_msg = proc.stderr or 'ffmpeg failed'
            return f"Conversion error: {error_msg}", 500

        return send_file(output_path, mimetype='audio/mpeg', as_attachment=True,
                         download_name=os.path.splitext(video.filename)[0] + '.mp3')
    finally:
        try:
            os.remove(input_path)
        except Exception:
            pass
        try:
            os.remove(output_path)
        except Exception:
            pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
