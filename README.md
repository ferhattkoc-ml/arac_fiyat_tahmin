# 🏎️ AudiPredict AI — Enterprise Vehicle Valuation Platform

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/CatBoost-Production_Model-FFCC00?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Flask-REST_API-000000?style=for-the-badge&logo=flask"/>
  <img src="https://img.shields.io/badge/PostgreSQL-Analytics_DB-336791?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/MLOps-Production_Ready-2EA043?style=for-the-badge"/>
</p>

<h3 align="center">
AI-Powered Vehicle Price Intelligence Platform
</h3>

<p align="center">
Production-grade machine learning infrastructure delivering real-time vehicle valuation through a scalable Flask API, optimized CatBoost inference engine, and enterprise observability stack.
</p>

---

# ✨ Overview

AudiPredict AI is an end-to-end machine learning deployment platform designed for real-time secondary market vehicle valuation.

The project focuses on the production engineering lifecycle of machine learning systems — transforming a trained regression model into a scalable, observable, and enterprise-ready inference service.

Core engineering goals include:

- High-performance inference
- API reliability
- Structured analytics logging
- Monitoring & operational visibility
- Production deployment architecture

---

# 🚀 Core Features

## ⚡ Real-Time Inference Engine
- Optimized CatBoost .cbm deployment
- Low-latency prediction responses
- Production-ready REST architecture

## 🧩 Native Categorical Processing
- Eliminates One-Hot Encoding complexity
- Efficient categorical feature handling
- Reduced sparse matrix overhead

## 📊 Enterprise Observability
- Request & prediction logging
- Inference telemetry collection
- Data drift monitoring capability
- Audit-friendly analytics pipeline

## 🔐 Operational Dashboard
- Historical prediction tracking
- Real-time request monitoring
- Operational analytics visibility

---

# 🔄 Prediction Workflow

bash ''' Client Request     
↓ Validation & Sanitization    
↓ Feature Vector Construction     
↓ CatBoost ML Inference     
↓ Prediction Logging    
↓ Response Delivery 

'''
### Workflow Details

- Users submit vehicle specifications through the frontend interface
- Incoming payloads are validated and transformed into feature vectors
- The CatBoost inference engine performs real-time valuation prediction
- Prediction metadata is persisted for analytics and monitoring
- The API returns estimated market value with inference metadata

---

# 📂 Repository Structure

bash ```
├── app.py                # Flask application & API routes 
├── model.cbm             # Production CatBoost model 
├── requirements.txt      # Python dependencies 
├── runtime.txt           # Deployment runtime configuration 
├── templates/            # Frontend templates & admin panel 
├── static/               # CSS, JS & assets 
├── database/             # Analytics & prediction storage 
└── logs/                 # Structured application logs 
```
---

# 🛠️ Local Setup

## Clone Repository

bash 
``` git clone https://github.com/ferhattkoc-ml/arac_fiyat_tahmin.git 
cd arac_fiyat_tahmin  ```

## Create Virtual Environment

bash
 ``` python -m venv venv ``` 

## Activate Environment

### Linux / macOS

bash
```source venv/bin/activate ```

### Windows

bash
```venv\Scripts\activate ```

## Install Dependencies

bash
```pip install -r requirements.txt ```

## Run Application

bash
```python app.py ```

Application runs at:

bash
```http://127.0.0.1:5000 ```

---

# 📡 API Documentation

## Prediction Endpoint

bash POST /predict 

---

## Request Example
```
json {   "model_variant": "Audi A6",  
"year": 2021,   
"mileage": 38000,  
"fuel_type": "Diesel",  
"transmission": "Automatic",  
"damage_history": "Minor",  
"engine_power": 204 } 
```
---

## Response Example
```
json {   "status": "success",  
"predicted_price": 2450000,  
"currency": "TRY", 
"model_version": "v1.0-production" } 
```
---

# 📈 Engineering Philosophy

This repository intentionally excludes:

- Training notebooks
- Experimental pipelines
- Raw datasets

The platform is designed specifically around production deployment engineering and ML inference operations.

This mirrors enterprise ML architecture where:

- Training environments remain isolated
- Inference systems operate independently
- Production services prioritize scalability, observability, and reliability

---

# 🧠 Tech Stack

```

| Layer | Technologies |
|---|---|
| Machine Learning | CatBoost |
| Backend API | Flask |
| Database | PostgreSQL / SQLAlchemy |
| Deployment | Docker |
| Monitoring | Structured Logging |
| Language | Python 3.11 |

```
---

# 🔮 Future Enhancements

- Kubernetes deployment orchestration
- CI/CD integration pipelines
- Model version registry
- Automated drift detection
- Real-time monitoring dashboards
- Redis inference caching
- Async prediction queue system

---

# 📜 License

This project is intended for educational, portfolio, and production engineering demonstration purposes
