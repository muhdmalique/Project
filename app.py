from flask import *
from Project import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('Homepage.html')


@app.route('/init')
def init():
    init_table()
    return 'Initialised'


if __name__ == '__main__':
    app.run()
