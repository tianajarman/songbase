from flask import Flask, session, render_template, request, redirect, url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = 'wersdfxcvt'


@app.route('/')
def home():
    # return '<h1>hello world!!!!!</h1>'
    return render_template('index.html')


@app.route('/user/<string:name>')
def get_user(name):
    # return '<h1>hello %s your age is %d</h1>' % (name, 3)
    return render_template('user.html', user_name=name)


@app.route('/songs')
def list_songs():
    songs = [
        'Supercut',
        'Wolves',
        'Holy Ground'
    ]
    return render_template('songs.html', songs=songs)


@app.route('/form-demo', methods=['GET', 'POST'])
def form_demo():
    if request.method == 'GET':
        first_name = request.args.get('first_name')
        if first_name:
            return render_template('form-demo.html', first_name=first_name)
        else:
            first_name = session.get('first_name')
            return render_template('form-demo.html', first_name=first_name)
    if request.method == 'POST':  # could also use 'else' by itself
        session['first_name'] = request.form['first_name']
        # return render_template('form-demo.html', first_name=first_name)
        return redirect(url_for('form_demo'))  # important endpoint after post


if __name__ == '__main__':
    app.run()
