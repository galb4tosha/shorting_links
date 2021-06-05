from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        print(request.data.decode("utf-8"))
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port="5000")
