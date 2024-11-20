from flask import Blueprint, render_template
from profileapp.app import db

profiles = Blueprint('profiles', __name__, template_folder='templates',
                     static_folder='static', static_url_path='/static')


@profiles.route('/', methods=['GET'])
def index():
    render_template('profiles/index.html')
