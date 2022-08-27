from flask import render_template, Blueprint, request
from json import JSONDecodeError

from functions import get_posts_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates_name')


@main_blueprint.route('/')
def main_post():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_post():
    search_query = request.args.get('s', '')
    try:
        posts = get_posts_by_word(search_query)
    except FileNotFoundError:
        return 'file is not'
    except JSONDecodeError:
        return 'invalid file'
    return render_template('post_list.html', posts=posts)