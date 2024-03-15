from flask import Flask, render_template, request
from app import summarize
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    summary = ""
    if request.method == 'POST':
        link = request.form.get('link')
        pro_link = link.split('=')
        summary = summarize(pro_link[-1])
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=False)
    