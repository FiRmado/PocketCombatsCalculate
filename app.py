# app.py
from flask import Flask, request, render_template
from calculator_logic import calculate_all

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    lang = request.args.get("lang", "uk")  # язык по умолчанию — украинский
    if request.method == "POST":
        data = request.form
        result = calculate_all(data)
    return render_template("index.html", result=result, request=request, lang=lang)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
