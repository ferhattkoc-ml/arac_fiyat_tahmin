## 🏎️ AudiPredict AI — Enterprise Vehicle Valuation Platform

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/CatBoost-Production_Model-yellow?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Flask-REST_API-black?style=for-the-badge&logo=flask"/>
  <img src="https://img.shields.io/badge/PostgreSQL-Analytics_DB-336791?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/MLOps-Production_Ready-success?style=for-the-badge"/>
</p>
<h3 align="center">
AI-Powered Vehicle Price Intelligence & Real-Time ML Inference System
</h3>
<p align="center">
  Production-grade Machine Learning deployment infrastructure serving a high-performance CatBoost regression model through a scalable Flask REST API with integrated analytics, observability, and enterprise monitoring.
</p>

⸻

## ✨ Overview

AudiPredict AI is a full-stack machine learning deployment platform developed for real-time secondary market vehicle valuation.

The project focuses on the productionization phase of Machine Learning systems, transforming a research-grade predictive model into a scalable inference infrastructure capable of handling real-world prediction traffic with full auditability and analytics visibility.

Unlike notebook-based ML projects, this repository demonstrates how trained models are deployed, monitored, and consumed within a modern software architecture.

⸻

## 🧠 Project Vision

Traditional vehicle valuation systems rely heavily on static pricing heuristics and manual expertise.

AudiPredict AI introduces a data-driven valuation pipeline capable of processing:

* Complex categorical vehicle attributes
* Mileage-to-age relationships
* Market-sensitive equipment packages
* Damage history impact
* Fuel & transmission effects
* High-cardinality Audi model configurations

The system delivers instant market value estimations while simultaneously collecting inference telemetry for future model monitoring and retraining strategies.

⸻

## 🏗️ Production Architecture

flowchart LR

A[🌐 Frontend Client] --> B[⚡ Flask REST API]
B --> C[🛡️ Validation Layer]
C --> D[🧠 CatBoost Inference Engine]

D --> E[💰 Prediction Response]
D --> F[(📊 SQLAlchemy Analytics DB)]

F --> G[📈 Admin Dashboard]
G --> H[🔍 Monitoring & Insights]

style D fill:#f5b7ff,stroke:#222,stroke-width:3px,color:#000
style F fill:#b7d7ff,stroke:#222,stroke-width:3px,color:#000
style G fill:#c6ffd1,stroke:#222,stroke-width:3px,color:#000
style B fill:#ffe7b7,stroke:#222,stroke-width:2px,color:#000
style C fill:#ffd6d6,stroke:#222,stroke-width:2px,color:#000
style E fill:#fff2a8,stroke:#222,stroke-width:2px,color:#000

⸻

## 🚀 Key Capabilities

⚡ Real-Time Inference

* Millisecond-level prediction latency
* Optimized CatBoost .cbm deployment
* Memory-efficient inference pipeline
* Dynamic feature vector generation

⸻

## 🧩 Native Categorical Intelligence

The system leverages CatBoost’s native categorical feature processing capabilities, eliminating:

* One-hot encoding overhead
* Sparse matrix inefficiencies
* High-memory transformations 

This enables significantly better scalability in production environments.

⸻

## 📊 Enterprise Observability

Every prediction request is fully logged for:

* Auditability
* Monitoring
* Model drift analysis
* Future retraining pipelines
* User behavior analytics

Captured metadata includes:

* Input payloads
* Prediction outputs
* Request timestamps
* Session activity
* Model inference behavior

⸻

## 🔐 Internal Admin Dashboard

A dedicated analytics panel provides:

* Historical prediction tracking
* Search & filtering
* Real-time request monitoring
* Prediction frequency analytics
* Operational visibility

⸻

## 🌐 RESTful API Infrastructure

The platform follows a decoupled architecture:

Layer	Technology
Backend API	Flask
ML Engine	CatBoost
Database ORM	SQLAlchemy
Frontend	HTML / CSS / JavaScript
Deployment	Gunicorn + Docker
Database	PostgreSQL / SQLite

⸻

## 🔄 Prediction Lifecycle

1️⃣ Client Request

The user submits vehicle specifications through the frontend interface.

Example:

{
  "model_variant": "Audi A4",
  "year": 2020,
  "mileage": 45000,
  "fuel_type": "Diesel",
  "transmission": "Automatic",
  "damage_history": "None",
  "engine_power": 190
}

⸻

## 2️⃣ Validation Layer

Incoming payloads are:

* Sanitized
* Validated
* Structured into feature vectors

before reaching the inference engine.

⸻

## 3️⃣ ML Inference Engine

The optimized CatBoost model (model.cbm) performs real-time regression inference using production-grade prediction pipelines.

⸻

## 4️⃣ Prediction Generation

The API returns:

* Estimated market value
* Processed feature metadata
* Inference status response

within milliseconds.

⸻

## 5️⃣ Database Logging

SQLAlchemy persists:

* User requests
* Model outputs
* System activity logs

for observability and analytics purposes.

⸻

## 📂 Repository Structure

.
├── app.py
│   └── Flask application, routing & API endpoints
│
├── model.cbm
│   └── Optimized CatBoost production model
│
├── requirements.txt
│   └── Python dependency definitions
│
├── runtime.txt
│   └── Runtime & deployment configuration
│
├── templates/
│   └── Frontend HTML templates
│
├── static/
│   ├── css/
│   ├── js/
│   └── assets/
│
├── database/
│   └── Prediction logs & analytics storage
│
├── logs/
│   ├── inference.log
│   ├── api.log
│   └── system.log
│
└── README.md
    └── Project documentation

⸻

## 🛠️ Local Installation

# Clone Repository

git clone https://github.com/ferhattkoc-ml/arac_fiyat_tahmin.git
cd arac_fiyat_tahmin

⸻

# Create Virtual Environment

python -m venv venv

Linux / macOS

source venv/bin/activate

Windows

venv\Scripts\activate

⸻

# Install Dependencies

pip install -r requirements.txt

⸻

# Run Application

python app.py

Application will start on:

http://127.0.0.1:5000

⸻

# 📡 API Reference

Prediction Endpoint

POST /predict

⸻

# Request Body

{
  "model_variant": "Audi A6",
  "year": 2021,
  "mileage": 38000,
  "fuel_type": "Diesel",
  "transmission": "Automatic",
  "damage_history": "Minor",
  "engine_power": 204
}

⸻

# Response Example

{
  "status": "success",
  "predicted_price": 2450000,
  "currency": "TRY",
  "model_version": "v1.0-production"
}

⸻

##  📈 MLOps Philosophy

This repository intentionally excludes:

* Training notebooks
* Raw datasets
* Experimental pipelines
* EDA workflows

because the focus is strictly:

Machine Learning Deployment, Inference Engineering, and Production Observability

This mirrors real-world enterprise ML system design where:

* training environments remain isolated,
* deployment artifacts are versioned independently,
* and inference systems operate as standalone production services.

⸻

## 🔒 Security & Reliability

The system includes:

* Input sanitization
* Payload validation
* ORM-based database security
* Structured logging
* Exception handling
* Production-ready API architecture

⸻

## 🧪 Future Improvements

Planned roadmap includes:

* JWT authentication
* Redis caching layer
* Kubernetes deployment
* CI/CD automation
* Model drift monitoring
* Grafana + Prometheus integration
* Real-time inference metrics
* Automated retraining pipelines

⸻

## 👨‍💻 Author

Ferhat Koç

Machine Learning • Data Science • MLOps • Analytics Engineering

* Production ML Systems
* Predictive Analytics
* Data Infrastructure
* AI Deployment Architectures

⸻

## 📜 License

This project is intended for:

* Academic research
* Portfolio demonstration
* Machine Learning deployment education
* Production architecture showcase

⸻

## ⭐ Final Note

AudiPredict AI is not a simple notebook-based ML demo.

It represents the transformation of a trained machine learning model into a deployable, observable, and scalable production inference platform — closely reflecting real-world industry deployment standards in modern AI engineering.
