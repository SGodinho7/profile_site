from flask import Blueprint, render_template, request, jsonify

from profileapp.app import db
from profileapp.blueprints.profiles.models import Profile

profiles = Blueprint('profiles', __name__, template_folder='templates',
                     static_folder='static', static_url_path='/static')


@profiles.route('/', methods=['GET'])
def index():
    profiles = Profile.query.all()

    return render_template('profiles/index.html', profiles=profiles)


@profiles.route('/register-profile', methods=['GET'])
def register_profile():
    return render_template('profiles/register.html')


@profiles.route('/post-profile', methods=['POST'])
def post_profile():
    data = request.get_json()
    profile = Profile(name=data['name'], email=data['email'],
                      age=data['age'], address=data['address'], sex=data['sex'])

    db.session.add(profile)
    db.session.commit()

    return jsonify("{'message': 'Success'}")
