from flask import Flask, render_template, request
from src.main import main

app = Flask(__name__)
from dotenv import load_dotenv
load_dotenv()  # must be called before accessing os.getenv


@app.route("/", methods=["GET", "POST"])
def home():
    repo = "suchitsharma2004/Chatapp"
    label = "bug"
    summary = {"issues": [], "mapping": {}, "summary_text": ""}

    if request.method == "POST":
        repo = request.form.get("repo")
        label = request.form.get("label")
        try:
            summary = main(repo=repo, label=label)
        except Exception as e:
            summary = {"issues": [], "mapping": {}, "summary_text": f"❌ Error: {e}"}

    return render_template("index.html", summary=summary, repo=repo, label=label)

if __name__ == "__main__":
    app.run(debug=True)
