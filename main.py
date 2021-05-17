import os
from pathlib import Path
from flask import Flask, render_template, request, url_for, send_file

from modules.classes import InstagramPage

app = Flask(__name__)


@app.context_processor
def override_url_for():
    """
    Generate a new token on every request to prevent the browser from
    caching static files.
    """
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/infopage")
def infopage():
    return render_template("infopage.html")


@app.route("/emotions", methods=['POST'])
def emotions():
    """
    Show the twitter map in the internet
    """
    try:
        nickname = request.form.get("nickname")
        if nickname:
            try:
                Path(os.path.join(os.getcwd(), 'static', 'data', f'{nickname}')).mkdir()
                inst = InstagramPage(nickname)
                os.chdir(os.path.join(os.getcwd(), 'static', 'data', f'{nickname}'))
                inst.visualize()
                inst.zip_result()
                inst.happiest_photo.save(f'{nickname}_happiest_photo.png', 'png')
                fakeness = inst.relative_fakeness()
                emoji_path = inst.get_emoji()
                with open('emoji_and_fakeness.txt', 'w') as file:
                    file.write(str(fakeness))
                    file.write('\n')
                    file.write(emoji_path)
                os.chdir(os.path.join('..', '..', '..'))
            except FileExistsError:
                with open(os.path.join(os.getcwd(), 'static', 'data', f'{nickname}', 'emoji_and_fakeness.txt'), 'r') as file:
                    fakeness = file.readline()
                    emoji_path = file.readline()

            happiest_path = os.path.join('..', 'static', 'data', f'{nickname}',
                                         f'{nickname}_happiest_photo.png')
            emotion_graphic_path = os.path.join('..', 'static', 'data',
                                                f'{nickname}',
                                                f'{nickname}_emotion_graphic.png')
            emotion_piechart_path = os.path.join('..', 'static', 'data',
                                                 f'{nickname}',
                                                 f'{nickname}_emotion_piechart.png')

            return render_template("emotions.html",
                                   data={'nickname': nickname,
                                         'fakeness': fakeness,
                                         'happiest': happiest_path,
                                         'emoji': emoji_path,
                                         'diagram_1': emotion_graphic_path,
                                         'diagram_2': emotion_piechart_path})
    except Exception:
        return render_template('failure.html')


@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    UPLOAD_DIRECTORY = 'uploads'
    # Appending app path to upload folder path within app root folder
    # uploads = os.path.join(app.root_path, app.config[UPLOAD_DIRECTORY])
    # Returning file from appended path
    print(filename)
    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
