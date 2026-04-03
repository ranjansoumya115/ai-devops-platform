import pandas as pd
from prophet import Prophet

# Load data
df = pd.read_csv("data.csv")

# Ensure correct column names
df.columns = ["ds", "y"]

# Train model
model = Prophet()
model.fit(df)

# Predict next 10 minutes
future = model.make_future_dataframe(periods=10, freq='min')
forecast = model.predict(future)

# Save prediction
forecast[['ds','yhat']].to_csv("prediction.csv", index=False)

print("Model trained and prediction saved")
