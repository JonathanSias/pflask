from flask import Flask, render_template, request
# from markupsafe import escape
import search
# 
app = Flask(__name__)
app.debug = True

# 

# @app.route('/')
# def index():
#     return 'Index'

@app.route('/')
def index():
    data = search.findText('TCP')
    return render_template('index.html', wordFind='TCP', filesFound = data)

@app.route('/read-pdf')
def readpdf():
    data = search.findText('TCP')
    return render_template('read-pdf.html', wordFind='TCP', filesFound = data)
    # with open("seminarios.pdf", "rb") as data_file:
    #     data = data_file.read()
    # encoded_data = base64.b64encode(data).decode('utf-8')
    # return render_template("read-pdf.html", encoded_data=encoded_data)

@app.route('/documents')
def documents():
    data = search.findText('TCP')
    return render_template('documents.html', wordFind='TCP', filesFound = data)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

#####################################################

