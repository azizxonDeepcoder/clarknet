from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

horror_events = [
    "Tunda yolg‘iz uyda qadam tovushlari eshitildi...",
    "Oynada ortingda kimdir turgandek tuyuldi...",
    "Telefon o‘zi qo‘ng‘iroq qildi, lekin ovoz yo‘q edi...",
    "Qorong‘uda kimdir ismingni pichirladi...",
    "Eshik ochiq edi, lekin sen yopgan eding..."
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enter", methods=["POST"])
def enter():
    age = request.form.get("age")
    region = request.form.get("region")

    if age != "18+":
        return "Kirish taqiqlangan ❌"

    return render_template(
        "home.html",
        region=region,
        event=random.choice(horror_events)
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)