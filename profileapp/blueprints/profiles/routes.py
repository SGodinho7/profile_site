from flask import Blueprint, render_template, request, jsonify

import uuid

from profileapp.app import db
from profileapp.blueprints.profiles.models import Profile

profiles = Blueprint('profiles', __name__, template_folder='templates',
                     static_folder='static', static_url_path='/static')


@profiles.route('/', methods=['GET'])
def index():
    profiles = Profile.query.all()

    return render_template('profiles/index.html', profiles=profiles)


@profiles.route('/view-profile/<pid>', methods=['GET'])
def view_profile(pid):
    profile = db.get_or_404(Profile, pid)

    return render_template('profiles/view.html', profile=profile)


@profiles.route('/update-profile/<pid>', methods=['GET'])
def update_profile(pid):
    profile = db.get_or_404(Profile, pid)

    return render_template('profiles/update.html', profile=profile)


@profiles.route('/register-profile', methods=['GET'])
def register_profile():
    return render_template('profiles/register.html')


@profiles.route('/post-profile', methods=['POST'])
def post_profile():
    data = request.get_json()
    profile = Profile(name=data['name'], email=data['email'],
                      age=data['age'], address=data['address'], sex=data['sex'], image_uuid='default.png')

    db.session.add(profile)
    db.session.commit()

    return jsonify("{'message': 'Success'}")


@profiles.route('/delete-profile/<pid>', methods=['DELETE'])
def delete_profile(pid):
    profile = db.session.get(Profile, pid)

    db.session.delete(profile)
    db.session.commit()

    return jsonify("{'message': 'Success'}")


@profiles.route('/put-profile', methods=['PUT'])
def put_profile():
    data = request.form
    profile = db.session.get(Profile, int(data['pid']))

    profile.name = data['name']
    profile.email = data['email']
    profile.age = int(data['age'])
    profile.address = data['address']
    profile.sex = data['sex']

    if 'image' in request.files:
        profile.image_uuid = f'{uuid.uuid4()}.jpg'
        img = request.files['image']
        img.save(
            f'profileapp/blueprints/profiles/static/img/{profile.image_uuid}')

    db.session.commit()

    return jsonify("{'message': 'Success'}")
