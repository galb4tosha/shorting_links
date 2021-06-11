from flask import Flask, render_template, request, url_for, Response
import work_with_db

app = Flask(__name__)
data_base = work_with_db.UrlDataBase()


@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        short_url = data_base.get_short_url(request.data.decode("utf-8"))
        print(request.data.decode("utf-8"))
        #short_url = "http://azazza.com/Qtu98"
        return Response(short_url)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port="5000")
