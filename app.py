from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        thread_id = request.form.get("thread_id")
        message = request.form.get("message")
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return render_template("index.html", sent=True, thread_id=thread_id, message=message, time=now)
    return render_template("index.html", sent=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
