import os
from pathlib import Path
from flask import Flask, render_template, request, url_for, redirect

from modules.classes import InstagramPage

app = Flask(__name__)


# @app.after_request
# def add_header(r):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     r.headers["Pragma"] = "no-cache"
#     r.headers["Expires"] = "0"
#     r.headers['Cache-Control'] = 'public, max-age=0'
#     return r


# @app.after_request
# def after_request(response):
#     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
#     response.headers["Expires"] = '0'
#     response.headers["Pragma"] = "no-cache"
#     return response


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
    nickname = request.form.get("nickname")
    if nickname:
        inst = InstagramPage(nickname)
        os.chdir('static')
        try:
            Path(os.path.join(os.getcwd(), f'{nickname}')).mkdir()
            os.chdir(f'{nickname}')
            inst.visualize()
            inst.happiest_photo.save(f'{nickname}_happiest_photo.png', 'png')
            os.chdir('..')
        except FileExistsError:
            pass
        os.chdir('..')

        return render_template("emotions.html", data={'nickname': nickname, 'fakeness': inst.relative_fakeness(), 'happiest': f"../static/{nickname}/{nickname}_happiest_photo.png", 'emoji': inst.get_emoji(),
                                                      'diagram_1': f"../static/{nickname}/{nickname}_emotion_graphic.png", 'diagram_2': f"../static/{nickname}/{nickname}_emotion_piechart.png"})


# @app.route("/new", methods=["POST"])
# def send_post():
#     global data
#
#     name = request.form.get('register')
#     return render_template("all.html", content=data)
#
#
# @app.route("/teacher/<string:teacher_name>")
# def go_to_htos(teacher_name):
#     global data
#     our_person = None
#     teacher_str = ' '.join(teacher_name.split('_'))
#     for person in data:
#         if person[0] == teacher_str:
#             our_person = person
#             break
#     return render_template("page_of_teacher.html", teacher=our_person)
#
# # for info in data:
# #     name = '_'.join(person[0].splt()
# #     @app.route(f"/{name}", methods=["GET", "POST"])
# #     def go_to_htos():
# #         return render_template("page_of_teacher.html")


if __name__ == "__main__":
    app.run(debug=True)