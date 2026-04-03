import requests
import csv
import time

PROM_URL = "http://localhost:9090/api/v1/query_range"

query = 'rate(node_cpu_seconds_total[1m])'

end = int(time.time())
start = end - 3600

params = {
    "query": query,
    "start": start,
    "end": end,
    "step": 60
}

response = requests.get(PROM_URL, params=params)
data = response.json()

with open("data.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["ds", "y"])

    for result in data['data']['result']:
        for value in result['values']:
            ts = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(value[0]))
            writer.writerow([ts, float(value[1])])

print("Data saved to data.csv")
