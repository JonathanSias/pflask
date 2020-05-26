from flask import Flask, render_template, request
# from markupsafe import escape
import search
# 
app = Flask(__name__)
app.debug = True


# @app.route('/')
# def index():
#     return 'Index'


@app.route('/')
def hello():
    data = search.findText('TCP')
    return render_template('index.html', wordFind='TCP', filesFound = data)


if __name__ == '__main__':
    app.run(debug=True)

#####################################################

