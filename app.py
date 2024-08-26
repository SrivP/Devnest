
from flask import (Flask, flash, redirect, render_template, request,
                   send_from_directory, url_for)
from flask_uploads import IMAGES, UploadSet, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import SubmitField

from ml import classify

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = "no."

# Uploads
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

# Flask Form
class UploadForm(FlaskForm):
    photo = FileField(
        validators=[
            FileAllowed(photos, 'Only images are allowed'),
            FileRequired('File field should not be empty')
        ]
    )
    submit = SubmitField('Upload')

@app.route('/uploads/<filename>')
def get_file(fileName):
    return send_from_directory(app.config['UPLOAD_FOLDER'], fileName)

# Path for our main Svelte page
@app.route("/", methods=['GET', 'POST'])
def upload_image():
    form = UploadForm()
    if form.validate_on_submit():
        file_name = photos.save(form.photo.data)
        file_url = url_for('get_file', filename= file_name)
    else:
        file_url = None
    return render_template('index.html', form=form, file_url=file_url)


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('templates', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)

