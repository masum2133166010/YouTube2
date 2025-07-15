
from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/api/download', methods=['POST'])
def download():
    data = request.get_json()
    video_url = data.get('url')

    try:
        ydl_opts = {
            'quiet': True,
            'format': 'best',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            return jsonify({
                'status': 'success',
                'title': info['title'],
                'download_url': info['url']
            })

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

app.run(host='0.0.0.0', port=5000)
