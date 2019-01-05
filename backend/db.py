from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Table(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key = True)

    def __init__(self, **kwargs):
        self.text = kwargs.get('text', '')
        self.username = kwargs.get('username', '')
        self.task_id = kwargs.get('task_id')

    def serialize(self):
        return {
            'id': self.id,
            'score': self.score,
            'text': self.text,
            'username': self.username
        }

class Club(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key = True)
    score = db.Column(db.Integer, default = 0)
    text = db.Column(db.String, nullable = False)
    username = db.Column(db.String, nullable= False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable = False)

    def __init__(self, **kwargs):
        self.text = kwargs.get('text', '')
        self.username = kwargs.get('username', '')
        self.task_id = kwargs.get('task_id')

    def serialize(self):
        return {
            'id': self.id,
            'score': self.score,
            'text': self.text,
            'username': self.username
        }

class User(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key = True)
    score = db.Column(db.Integer, default = 0)
    text = db.Column(db.String, nullable = False)
    username = db.Column(db.String, nullable= False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable = False)

    def __init__(self, **kwargs):
        self.text = kwargs.get('text', '')
        self.username = kwargs.get('username', '')
        self.task_id = kwargs.get('task_id')

    def serialize(self):
        return {
            'id': self.id,
            'score': self.score,
            'text': self.text,
            'username': self.username
        }
        
class Bid(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key = True)
    score = db.Column(db.Integer, default = 0)
    text = db.Column(db.String, nullable = False)
    username = db.Column(db.String, nullable= False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable = False)

    def __init__(self, **kwargs):
        self.text = kwargs.get('text', '')
        self.username = kwargs.get('username', '')
        self.task_id = kwargs.get('task_id')

    def serialize(self):
        return {
            'id': self.id,
            'score': self.score,
            'text': self.text,
            'username': self.username
        }
