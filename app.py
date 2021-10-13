from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello_world():
    return '<p style="color:red;">Hello, World!</p>'

@app.route("/app", methods=['POST'])
def bitrix_app():
    return '<h1>opa</h1>'

if __name__=="__main__":
    app.run("0.0.0.0")



