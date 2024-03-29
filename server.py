import uuid

from flask import Flask, request, redirect, url_for, flash, send_file, after_this_request
from werkzeug.utils import secure_filename
import os

from mosaic import create

THIS_FILE_PATH = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = THIS_FILE_PATH + '/downloaded'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def ext(filename):
    return filename.rsplit('.', 1)[1].lower()


def allowed_file(filename):
    return '.' in filename and ext(filename) in ALLOWED_EXTENSIONS


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'image' not in request.files:
            # flash('No file part')
            print("NO FILE")
            return redirect(request.url)
        file = request.files['image']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = str(uuid.uuid4()) + "." + ext(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_path))
            new_file_path = create(file_path)

            @after_this_request
            def remove_file(response):
                try:
                    os.remove(file_path)
                    os.remove(new_file_path)
                except Exception as error:
                    app.logger.error("Error removing or closing downloaded file handle", error)
                return response

            return send_file(new_file_path, mimetype='image/png')

    return 'fail'


if __name__ == "__main__":
    app.run("0.0.0.0", port=9082)