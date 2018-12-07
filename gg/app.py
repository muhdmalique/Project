from persistence import *
import functools
from flask import *
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)


@app.route('/')
def home():
    return render_template('signup.html')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session['id'] is None:
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view


@app.route('/init')
def init():
    init.db()
    return 'db initialised'


@app.route('/login',  methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            user = get_user(username, password)
            if user is None:
                error = 'Wrong username and password'
            else:
                session['id'] = user.get_id()
                session['user_name'] = user.get_username()
                return redirect(url_for('signup'))
        flash(error)
    return render_template('login.html')
    # guest mode button if press instantly log in so skip signup page


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not email:
            error = 'Email required'
        else:
            create_user(username, email, password)
            return redirect(url_for('login'))
        flash(error)
    return render_template('signup.html')


@app.route('/forget_password', methods=('GET', 'POST'))
def forget_password():
    if request.method == 'POST':
        email = request.form['email']
        forget_password(email)
    return render_template('forget_password.html')


@app.route('/logout', methods=('GET', 'POST'))
def logout():
    session.clear()
    return redirect(url_for('signup'))


if __name__ == '__main__':
    app.run(debug=True)
