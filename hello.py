"""
このモジュールは、基本的な Flask アプリケーションを提供します。
ユーザーが "Hello, World!" を表示するページにアクセスできるようになります。
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    この関数は単純なHTML文字列を戻します。
    """
    return "<p>Hello, World!</p>"
