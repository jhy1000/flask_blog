from flask import Flask,request,redirect,abort
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    #return '<h1>Hello world!</h1>'
    #return '<p>Your browser is %s' % user_agent
    return '<h1>Bad Request</h1>',400
    return redirect('http://www.baidu.com')

    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response



#@app.route('/user/<name>')
#def user(name):
#    return '<h1> hello %s! </h1>' % name

@app.route('/user/<int:id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s<h1>' % user.name


