"""
このモジュールは、基本的な Flask アプリケーションを提供します。
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
    int以外が来たら404
    """
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    """
    パスや文字列を受け取れる
    """
    return f'Subpath {escape(subpath)}'

@app.route('/projects/')
def projects():
    """
    リソースがコレクションまたはディレクトリの場合（例：ブログのカテゴリ、プロジェクトリストなど）は、URLの最後にスラッシュ(/)をつけると良いでしょう。これは、コレクションやディレクトリは通常、その下に他のリソースが存在し、その集合を示すものと見なされるためです。
    """
    return 'The project page'

@app.route('/about')
def about():
    """
    リソースが特定のページや項目（例：特定のブログ記事、特定のプロジェクトなど）を指す場合、URLの最後にスラッシュをつけないと良いでしょう。これは、そのURLが一つの特異なリソースを指すものと見なされ、その下に他のリソースが存在しないと想定されるためです。
    """
    return 'The about page'
