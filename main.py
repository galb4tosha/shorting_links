from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        pass
    return render_template('index.html')