from flask import Flask, render_template, request, url_for, Response, redirect
import work_with_db

app = Flask(__name__)
data_base = work_with_db.UrlDataBase()


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        short_url = "http://127.0.0.1:5000/?url=" + data_base.get_short_url(request.data.decode("utf-8"))
        return Response(short_url)
    if request.method == "GET":
        long_url = data_base.get_long_url_from_db(request.args.get("url"))
        if long_url != 0:
            return redirect(long_url)   
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port="5000")
