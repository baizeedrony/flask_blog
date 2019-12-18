from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/about')
def about():
    return "<H1>about page</h1>"

if __name__=='__main__':
    app.run(debug=True)