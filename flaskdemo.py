from flask import Flask, render_template
import sys

app = Flask(__name__)

port = 5001
if len(sys.argv) == 2:
    port = int(sys.argv[1])

@app.route("/")
def hello_world():
    return render_template("index.html")

app.run(host='localhost', port=port)