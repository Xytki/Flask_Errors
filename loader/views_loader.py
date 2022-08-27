from json import JSONDecodeError

from flask import render_template, Blueprint, request

from functions import save_picture, func_add_post

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates_name')


@loader_blueprint.route('/post')
def add_post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def add_post():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'No picture or content'
    if picture.filename.split('.')[-1] not in ['jpg', 'png']:
        return 'Incorrect file extension'

    try:
        picture_path: str = '/' + save_picture(picture)
    except FileNotFoundError:
        return 'File is not'
    except JSONDecodeError:
        return 'File is invalid'
    post: dict = func_add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)
