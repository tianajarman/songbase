from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return 'hello world'


@app.route('/user/<string:name>')
def get_user(name):
    return '<h1>hello %s your age is %d</h1>' % (name, 3)


if __name__ == '_main_':
    app.run(debug=True)
