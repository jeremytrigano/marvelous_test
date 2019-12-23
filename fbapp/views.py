from flask import Flask, render_template, url_for, request

app = Flask(__name__)

app.config.from_object('config')

from .utils import find_content, OpenGraphImage

@app.route('/')
@app.route('/index/')
def index():
    if 'img' in request.args:
        img = request.args['img']
        og_url = url_for('index', img=img, _external=True)
        og_image = url_for('static', filename=img, _external=True)
    else:
        og_url = url_for('index', _external=True)
        og_image = url_for('static', filename='tmp/sample.jpg', _external=True)
    description = "Loki _-_ Aussi malin que Loki mais cela ne suffit pas à savoir quel personnage te correspond. Il faut lancer le test ! _-_ http://www.marvel-world.com/"
    page_title = "Marvelous Test"
    og_description = "Découvre quel personnage Marvel te correspond !"
    return render_template('index.html',
                          user_name='Stan Lee',
                          user_image=url_for('static', filename='img/profile.png'),
                          description=description.split(" _-_ "),
                          blur=True,
                          page_title=page_title,
                          og_url=og_url,
                          og_image=og_image,
                          og_description=og_description)


@app.route('/result/')
def result():
    gender = request.args.get('gender')
    description = find_content(gender).description
    user_name = request.args.get('first_name')
    uid = request.args.get('id')
    profile_pic = 'http://graph.facebook.com/' + uid + '/picture?type=large'
    img = OpenGraphImage(uid, user_name, description).location
    og_url = url_for('index', img=img, _external=True)
    return render_template('result.html',
                        user_name=user_name,
                        user_image=profile_pic,
                        description=description.split(" _-_ "),
                        og_url=og_url)


@app.route('/contents/<content_id>/')
def content(content_id):
    return '%s' % content_id


if __name__ == "__main__":
    app.run()
