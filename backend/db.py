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
    __tablename__ = 'club'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    address = db.Column(db.String, nullable = False)
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'), nullable = False)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')
        self.address = kwargs.get('address', '')
        self.table_id = kwargs.get('table_id')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name, 
            'description': self.description, 
            'address': self.address
        }

class User(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, default = 0)
    password = db.Column(db.String, nullable = False)
    phone_number = db.Column(db.String, nullable= False)
    id_number = db.Column(db.String, nullable=False)
    bid_id = db.Column(db.Integer, db.ForeignKey('bid.id'), nullable = False)

    def __init__(self, **kwargs):
        self.username = kwargs.get('username', '')
        self.password = kwargs.get('password', '')
        self.phone_number = kwargs.get('phone_number', '')
        self.id_number = kwargs.get('id_number', '')
        self.bid_id = kwargs.get('bid_id')

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username, 
            'password': self.password, 
            'phone_number': self.phone_number, 
            "id_number": self.id_number
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
