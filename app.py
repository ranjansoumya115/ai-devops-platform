from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# For Prometheus
@app.get("/metrics")
def metrics():
    df = pd.read_csv("prediction.csv")
    value = df.iloc[-1]["yhat"]

    return f"""# HELP ai_predicted_load Predicted load
# TYPE ai_predicted_load gauge
ai_predicted_load {float(value)}
"""

# For KEDA (VERY IMPORTANT)
@app.get("/metric")
def metric():
    df = pd.read_csv("prediction.csv")
    value = df.iloc[-1]["yhat"]
    return {"value" :float(value)}
