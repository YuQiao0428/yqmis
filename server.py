from flask import Flask, render_template , request
from datetime import datetime
from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>郁喬Python網頁</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=yuqiao>傳送使用者暱稱</a><br>"
    homepage += "<a href=/about>簡介網頁</a><br>"
    return homepage

@app.route("/mis")
def course():
    return "<h1>seven</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime = str(now))

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)
    
#if __name__ == "__main__":
#    app.run()



