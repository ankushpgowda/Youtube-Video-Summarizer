from flask import Flask, render_template, request
from app import summarize
import re
app = Flask(__name__)

def get_video_id(link):
    if "youtu.be" in link:
        return re.search(r"(?<=youtu\.be\/)[^#\?]*", link).group(0)
    else:
        match = re.search(r"(?:[?&]v=|\/embed\/)([^#\?]*)", link)
        return match.group(1) if match else None

@app.route("/", methods=['POST', 'GET'])
def index():
    summary = ""
    if request.method == 'POST':
        link = request.form.get('link')
        pro_link = get_video_id(link)
        summary = summarize(pro_link)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True, port=8888)
    