from flask import Flask, request, render_template
from textblob import TextBlob
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get['text']
        print(text)
        s = TextBlob(text).sentiment
        return (render_template("index.html", result=s))
    else:
        return(render_template("index.html", result1="Please Try Again"))

if __name__ == "__main__":
    app.run()