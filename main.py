from flask import Flask, render_template, request
from app import summarize
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    summary = ""
    if request.method == 'POST':
        link = request.form.get('link')
        summary = summarize(link)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True, port=8888)
    