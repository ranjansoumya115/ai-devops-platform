![Kubernetes](https://img.shields.io/badge/Kubernetes-Autoscaling-blue)
![KEDA](https://img.shields.io/badge/KEDA-Enabled-orange)
![AI](https://img.shields.io/badge/AI-Driven-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

# 🚀 AI-Based Autoscaling in Kubernetes using KEDA

## 📌 Project Overview

This project demonstrates an **AI-driven autoscaling system** where Kubernetes workloads automatically scale based on **machine learning predictions** instead of traditional CPU/memory metrics.

The system uses:

* A trained ML model to predict load
* A FastAPI service to expose predictions
* KEDA to scale Kubernetes workloads dynamically

---

## 🧠 Architecture

```
ML Model → FastAPI → KEDA → Kubernetes (HPA) → Auto Scaling
```

---

## 🛠️ Tech Stack

* 🐍 Python (Pandas, ML model)
* ⚡ FastAPI
* 🐳 Docker
* ☸️ Kubernetes
* 📈 KEDA (Kubernetes Event-Driven Autoscaling)

---
## ⚙️ Prerequisites

- Kubernetes cluster
- Docker
- KEDA installed
- Python 3.x

---
## 🚀 Setup Instructions

1. Clone repo
2. Build Docker image
3. Deploy to Kubernetes
4. Apply KEDA config
5. Test scaling

---
## 📂 Project Structure

```
ai-autoscale/
│
├── app.py              # FastAPI application (metrics + KEDA endpoint)
├── fetch_data.py       # Fetch data / simulate load
├── train_model.py      # Train ML model
├── prediction.csv      # Predicted load values
├── Dockerfile          # Docker image build file
├── prediction-api.yaml # Kubernetes Deployment & Service
├── keda.yaml           # KEDA autoscaling configuration
├── README.md           # Project documentation
│
└── images/
    └── architecture.png   # Architecture diagram
```

---

## ⚙️ How It Works

1. ML model predicts system load and stores results in `prediction.csv`
2. FastAPI reads latest prediction and exposes:

   * `/metrics` → for Prometheus
   * `/metric` → for KEDA
3. KEDA reads `/metric` endpoint
4. KEDA creates HPA dynamically
5. Kubernetes scales pods based on prediction

---

## 🔌 API Endpoints

### 1️⃣ Prometheus Metrics

```
GET /metrics
```

Returns:

```
ai_predicted_load 0.117
```

---

### 2️⃣ KEDA Metric Endpoint

```
GET /metric
```

Returns:

```json
{
  "value": 0.5
}
```

---

## 🐳 Docker Build & Push

```bash
docker build -t <your-docker-username>/prediction-api:v1 .
docker push <your-docker-username>/prediction-api:v1
```

---

## ☸️ Kubernetes Deployment

```bash
kubectl apply -f prediction-api.yaml
```

---

## ⚡ KEDA Configuration

```bash
kubectl apply -f keda.yaml
```

---

## 🔍 Verify Scaling

```bash
kubectl get scaledobject
kubectl get hpa
kubectl get pods
```

---

## 🧪 Testing Autoscaling

Update prediction:

```bash
nano prediction.csv
```

Change value:

```
2026-04-03 09:29:43,0.8
```

Then check:

```bash
kubectl get pods
```
ranjansoumya115@devops-vm:~/ai-autoscale$ kubectl get pods
NAME                              READY   STATUS    RESTARTS      AGE
ai-devops-6bb7f59498-67mpw        1/1     Running   1 (16d ago)   16d
ai-devops-6bb7f59498-c2k2r        1/1     Running   0             2m27s
ai-devops-6bb7f59498-dx6h2        1/1     Running   1 (16d ago)   16d
ai-devops-6bb7f59498-kpsv8        1/1     Running   0             2m27s
ai-devops-6bb7f59498-vrxpc        1/1     Running   0             2m12s
prediction-api-856b56cc94-czp5d   1/1     Running   0             6m22s

Pods will scale automatically 🚀

---

## 📊 Example Output

```bash
kubectl get hpa
```

```
TARGETS: 250m / 120m
REPLICAS: 2
```
ranjansoumya115@devops-vm:~/ai-autoscale$ kubectl get hpa
NAME                     REFERENCE              TARGETS           MINPODS   MAXPODS   REPLICAS   AGE
keda-hpa-ai-autoscaler   Deployment/ai-devops   250m/120m (avg)   1         10        2          32s
---

## 🎯 Key Features

* ✅ AI-driven autoscaling (not CPU-based)
* ✅ Custom metrics API
* ✅ Real-time scaling with KEDA
* ✅ Kubernetes-native solution
* ✅ Production-ready architecture

---

## 🧠 Learnings

* Kubernetes autoscaling concepts (HPA, KEDA)
* Docker image lifecycle
* API-driven scaling
* Debugging real-world DevOps issues
* Integrating ML with infrastructure

---

## 💼 Resume Point

> Built an AI-driven autoscaling system using FastAPI, Kubernetes, and KEDA to dynamically scale workloads based on machine learning predictions.

---

## 🚀 Future Enhancements

* Integrate Prometheus-based scaling
* Add Grafana dashboards
* CI/CD pipeline (Jenkins / GitHub Actions)
* Deploy on cloud (AWS EKS / GKE / AKS)

---
## 🎬 Demo

- AI predicts load → 0.5
- KEDA reads metric
- Pods scale from 2 → 4 automatically
---
## ⚙️ Prerequisites

- Kubernetes cluster
- Docker
- KEDA installed
- Python 3.x
---


## 👨‍💻 Author

Soumya Ranjan
DevOps | Cloud | AI Enthusiast

---
