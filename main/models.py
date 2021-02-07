from main import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    q1_result = db.Column(db.Integer)
    q2_result = db.Column(db.Integer)
    q3_result = db.Column(db.Integer)

def init():
    db.create_all()