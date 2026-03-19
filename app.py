from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Webhook Triggered Deployment 🚀"

@app.route("/load")
def load():
    if random.randint(1,10) > 7:
        return "ERROR: CPU spike detected"
    return "System Normal"

app.run(host="0.0.0.0", port=5000)
