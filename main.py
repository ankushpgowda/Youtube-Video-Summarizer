from flask import Flask, render_template, request
from app import summarize
import re
app = Flask(__name__)

def get_video_id(link):
    match = re.search(r"(?<=v=|v/|vi=|youtu\.be/|embed/)[^#\?]*", link)
    return match.group(0) if match else None

@app.route("/", methods=['POST', 'GET'])
def index():
    summary = ""
    if request.method == 'POST':
        link = request.form.get('link')
        pro_link = get_video_id(link)
        summary = summarize(pro_link)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=False)
    