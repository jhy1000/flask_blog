from flask import Flask,request,redirect,abort,render_template
from flask import make_response
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('user.html',name='jhy')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500



#@app.route('/user/<name>')
#def user(name):
#    return '<h1> hello %s! </h1>' % name

@app.route('/user/<int:id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s<h1>' % user.name


