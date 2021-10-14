from flask import Flask
from flask import render_template

from parser import get_currencies

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello_world():
    data = get_currencies()
    return render_template(
            'index.html',
            date=data['date'],
            currencies=data['currencies'])


if __name__=="__main__":
    app.run("0.0.0.0")



