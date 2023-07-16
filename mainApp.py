from PIL import Image
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename

import compressor

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def compress_image():
    picture = request.files['file']

    image = Image.open(picture.stream)

    return send_file(compressor.compress(image), mimetype='image/JPEG')


if __name__ == '__main__':
    app.run()
