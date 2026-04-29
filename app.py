from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_url = "https://angela-salary-api-3300-fndeh3e9fnejamfh.eastus2-01.azurewebsites.net/predict"

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", prediction=None)

@app.route("/predict", methods=["POST"])
def predict():
    data = {
    "age": int(request.form["age"]),
    "gender": int(request.form["gender"]),
    "country": int(request.form["country"]),
    "highest_deg": int(request.form["highest_deg"]),
    "coding_exp": int(request.form["coding_exp"]),
    "title": int(request.form["title"]),
    "company_size": int(request.form["company_size"])
}

    response = requests.post(api_url, json=data)
    prediction = response.json()["predicted_salary"]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)