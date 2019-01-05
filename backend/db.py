from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Table(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'), nullable = False)
    bids = db.relationship('Bid', cascade = 'delete')


    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')
        self.club_id = kwargs.get('club_id')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'club_id': self.club_id, 
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
    bid_amount = db.Column(db.Double, nullable = False)
    time = db.Column(db.Integer, default = 0)
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)


    def __init__(self, **kwargs):
        self.bid_amount = kwargs.get('bid_amount', '')
        self.table_id = kwargs.get('table_id')
        self.user_id = kwargs.get('user_id')


    def serialize(self):
        return {
            'id': self.id,
            'bid_amount': self.bit_amount,
            'table_id': self.table_id,
            'user_id': self.user_id,
            'timestamp': self.time
        }
