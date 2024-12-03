from flask import Blueprint, render_template, request, jsonify
from profileapp.app import db

profiles = Blueprint('profiles', __name__, template_folder='templates',
                     static_folder='static', static_url_path='/static')


@profiles.route('/', methods=['GET'])
def index():
    return render_template('profiles/index.html')


@profiles.route('/register-profile', methods=['GET'])
def register_profile():
    return render_template('profiles/register.html')


@profiles.route('/post-profile', methods=['POST'])
def post_profile():
    data = request.get_json()

    return jsonify(f'{data}')
