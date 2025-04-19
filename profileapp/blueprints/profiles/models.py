from profileapp.app import db


# sqlalchemy database profile table class
class Profile(db.Model):
    __tablename__ = 'profiles'

    # columns
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.Text, nullable=False)
    sex = db.Column(db.Text, nullable=False)
    image_uuid = db.Column(db.Text)

    def __repr__(self):
        return f'{self.name}, {self.age}, {self.address}, {self.sex};'
