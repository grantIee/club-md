import json
from flask import Flask, request
from flasgger import Swagger
from db import db, Post, Comment

db_filename = 'posts.db'
app = Flask(__name__)

# Configuration of SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SWAGGER'] = {
   "title": "Cornell AppDev - CS1998: Reddit-like Website API",
   "version": "0.0.1",
   "description": "This is the API for Cornell AppDev Fall 2018" +
   "Course CS1998: Intro to Backend Development. This API is for" +
   "a reddit-like forum website. Some links for this API:" +
   "[Course Github](https://github.com/appdev-courses) |" +
   "[Course Website](https://github.com/appdev-courses) |" +
   "[Course Piazza](https://piazza.com/class/jmb59vq5rqv2c5)"
}

# Initiation of db
db.init_app(app)
with app.app_context():
    db.create_all()

swagger = Swagger(app)

PORT = 8000

#### Code Begins Here #### 

@app.route('/api/posts/')
def get_posts():
    '''
    file: ./documentation/get_posts.yml
    '''

    posts = Post.query.all()
    res = {'success': True, 'data': [post.serialize() for post in posts]}
    return json.dumps(res), 200

@app.route('/api/posts/', methods = ['POST'])
def create_post():
    '''
    file: ./documentation/create_post.yml
    '''
    
    request_body = json.loads(request.data)
    # Code here checks for blank body requests / @beforerequests checks for None body requests
    if not request_body.get('text') == '' and not request_body.get('username') == '':
        post = Post(
            text = request_body.get('text'),
            username = request_body.get('username')
        )
        # Keep the two acts separate to reduce automatic commits to the server
        db.session.add(post)
        db.session.commit()
        return json.dumps({'success': True, 'data': post.serialize()}), 201
    return json.dumps({'success': False, 'error': 'invalid body format'}), 412

@app.route('/api/post/<int:post_id>/')
def get_post(post_id):
    '''
    file: ./documentation/get_post.yml
    '''

    post = Post.query.filter_by(id = post_id).first()
    if post is not None:
        return json.dumps({'success': True, 'data': post.serialize()}), 200
    return json.dumps({'success': False, 'error': 'Post not found!'}), 404

@app.route('/api/post/<int:post_id>/', methods = ['POST'])
def update_post(post_id):
    '''
    file: ./documentation/edit_post.yml
    '''

    post = Post.query.filter_by(id = post_id).first()
    if post is not None:
        request_body = json.loads(request.data)
        if not request_body.get('text') == '' and not request_body.get('username') == '':
            post.text = request_body.get('text', post.text)
            post.username = request_body.get('username', post.username)
            db.session.commit()
        return json.dumps({'success': True, 'data': post.serialize()}), 200
    return json.dumps({'success': False, 'error': 'Post not found!'}), 404

@app.route('/api/post/<int:post_id>/', methods = ['DELETE'])
def delete_post(post_id):
    '''
    file: ./documentation/delete_post.yml
    '''

    post = Post.query.filter_by(id = post_id).first()
    if post is not None:
        db.session.delete(post)
        db.session.commit()
        return json.dumps({'success': True, 'data': post.serialize()}), 200
    return json.dumps({'success': False, 'error': 'Post not found!'}), 404

@app.route('/api/post/<int:post_id>/comments/')
def get_comments(post_id):
    '''
    file: ./documentation/get_comments.yml
    '''

    post = Post.query.filter_by(id = post_id).first()
    if post is not None:
        comments = [comment.serialize() for comment in post.comments]
        if len(comments) != 0:
            return json.dumps({'success': True, 'data': comments}), 200
        return json.dumps({'success': True, 'data': 'There are no comments for this post.'}), 200
    return json.dumps({'success': False, 'error': 'Post not found!'}), 404



@app.route('/api/club/<int:club_id>/table/<int:table_id>/make_bid', methods = ['POST'])
def create_bid(table_id):
    '''
    file: ./documentation/create_bid.yml
    '''

    bid = Table.query.filter_by(id = table_id).first()
    if bid is not None:
        request_body = json.loads(request.data)
        # Code here checks for blank body requests / @beforerequests checks for None body requests
        if not request_body.get('text') == '' and not request_body.get('username') == '':
            bid = Bid(
                bid_amount = request_body.get('bid_amount'),
                table_id = request_body.get('table_id'),
                user_id = request_body.get('user_id'),
                club_id = club_id
            )
            club.tables.append(bid)
            db.session.add(bid)
            db.session.commit()
            return json.dumps({'success': True, 'data': bid.serialize()}), 201
        return json.dumps({'success': False, 'error': 'invalid body format'}), 412
    return json.dumps({'success': False, 'error': 'Table not found!'}), 404

@app.route('/api/club/<int:club_id>/table<int:table_id>/delete_bid/', methods = ['DELETE'])
def delete_bid(table_id):
    '''
    file: ./documentation/delete_bid.yml
    '''

    bid_amount = Table.query.filter_by(id = post_id).first()
    if bid is not None:
        db.session.delete(bid)
        db.session.commit()
        return json.dumps({'success': True, 'data': delete.serialize()}), 200
    return json.dumps({'success': False, 'error': 'Table not found!'}), 404


@app.route('/api/user/<int: user_id>/')
def get_user_info(user_id):
    '''
    file: ./documentation/get_user_info.yml
    '''

    user = User.query.filter_by(id = user_id).first()
    if user is not None:
        return json.dumps({'success': True, 'data': user.serialize()}), 200
    return json.dumps({'success': False, 'error': 'User not found!'}), 404

@app.route('/api/user/<int:user_id>/bids/')
def get_user_bids(user_id):
    '''
    file: ./documentation/get_comments.yml
    '''

    user = User.query.filter_by(id = user_id).first()
    if user is not None:
        bids = [bid.serialize() for bid in user.bids]
        if len(bids) != 0:
            return json.dumps({'success': True, 'data': bids}), 200
        return json.dumps({'success': True, 'data': 'There are no bids for this user.'}), 200
    return json.dumps({'success': False, 'error': 'User not found!'}), 404


@app.before_request
def before_request():
    if request.method == 'POST':
        if request.data is None:
            return json.dumps({'success': False, 'error': 'invalid body format'}), 412

if __name__ == "__main__":
    app.run(debug=True,port=PORT)

