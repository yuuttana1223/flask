"""
このモジュールは、基本的な Flask アプリケーションを提供します。
ユーザーが "Hello, World!" を表示するページにアクセスできるようになります。
"""

from markupsafe import escape

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    この関数は単純なHTML文字列を戻します。
    """
    return "<p>Hello, World!</p>"

@app.route('/user/<username>')
def show_user_profile(username):
    """
    show the user profile for that user
    """
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    """
    show the post with the given id, the id is an integer
    """
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    """
    show the subpath after /path/
    """
    return f'Subpath {escape(subpath)}'
