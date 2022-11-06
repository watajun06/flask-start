from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask"

@app.route("/hiraizumi")
def hiraizumi():
    return "Hello Hhhiraizumi"

@app.route("/user/<name>")
def heyName(name):
    return name
# http://192.168.40.100:5000/user/jun

@app.route("/user/age/<age>")
def heyage(age):
    return age
# http://192.168.40.100:5000/user/age/3

@app.route("/html")
def html():
    # return "<h1>Hello HTML</h1>"
    # http://192.168.40.100:5000/html
    return render_template("index.html")

@app.route("/html/<name>")
def htmlName(name):
    return render_template("name.html", name=name)

@app.route("/html/<age>")
def htmlAge(age):
    return render_template("age.htmml", htmlAge) 

@app.route("/query")
def query():
    search_text = request.args.get("search_text")
    return search_text
#  http://192.168.40.100:5000/query?AAA=XXX


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
