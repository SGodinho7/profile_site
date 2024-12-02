from profileapp.app import db


class Profile(db.Model):
    __tablename__ = 'profiles'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.Text, nullable=False)
    sex = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'{self.name}, {self.age}, {self.address}, {self.sex};'
