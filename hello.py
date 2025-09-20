#Example 2-1. hello.py: A complete Flask application
#Example 2-2. hello.py: Flask application with a dynamic route
#from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def index():
#    return '<h1>Hello World!</h1>'

#@app.route('/user/<name>')
#def user(name):
#    return '<h1>Hello, {}!</h1>'.format(name)

#if __name__ == '__main__':
#    app.run()

from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)