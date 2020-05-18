from flask import Flask
# from markupsafe import escape
app = Flask(__name__)
# app.debug = True


@app.route('/')
def index():
    return 'Index'


@app.route('/hello')
def hello():
    return 'Hello, World !'


# if __name__ == '__main__':
#     app.run(debug=True)
