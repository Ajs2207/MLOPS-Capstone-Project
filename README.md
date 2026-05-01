🚀 MLOps Pipeline
<div align="center">
https://img.shields.io/badge/MLOps-Capstone-blue?style=for-the-badge
https://img.shields.io/badge/Python-3.10-green?style=for-the-badge
https://img.shields.io/badge/Flask-API-red?style=for-the-badge
https://img.shields.io/badge/Docker-Containerization-blue?style=for-the-badge
https://img.shields.io/badge/Kubernetes-EKS-326CE5?style=for-the-badge
https://img.shields.io/badge/AWS-Cloud-orange?style=for-the-badge

An End-to-End Machine Learning Operations Pipeline with Automated CI/CD, Container Orchestration, and Real-Time Monitoring

</div>

📋 Table of Contents
Overview

Architecture

Technology Stack

Features

Project Structure

Infrastructure & Deployment

Monitoring & Observability

CI/CD Pipeline

Getting Started

Contributor


🎯 Overview
This project is  a production-grade MLOps pipeline that demonstrates the complete lifecycle of machine learning models - from data ingestion and experimentation to deployment and monitoring. This project showcases industry best practices for automating ML workflows, containerizing applications, orchestrating deployments on Kubernetes, and implementing comprehensive observability.

┌─────────────────────────────────────────────────────────────────────────────┐
│                              CI/CD Pipeline (GitHub Actions)                 │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌────────┐ │
│  │  Code    │───▶│  Tests   │───▶│  Build   │───▶│  Push    │───▶│Deploy  │ │
│  │  Commit  │    │  (CI)    │    │ (Docker) │    │  to ECR  │    │ to EKS │ │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘    └────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           DATA & EXPERIMENT TRACKING                         │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────────┐  │
│  │      DVC        │    │     MLFlow      │    │       Dagshub           │  │
│  │  Data Version   │    │  Experiment     │    │    Remote Tracking      │  │
│  │    Control      │    │   Tracking      │    │       & Storage         │  │
│  └─────────────────┘    └─────────────────┘    └─────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          APPLICATION DEPLOYMENT (EKS)                        │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                        Kubernetes Cluster                            │    │
│  │  ┌───────────────┐    ┌───────────────┐    ┌───────────────────────┐  │    │
│  │  │   Flask App   │    │  LoadBalancer │    │   AWS ECR (Images)    │  │    │
│  │  │   Pod/Service │    │   (Ingress)   │    │                       │  │    │
│  │  └───────────────┘    └───────────────┘    └───────────────────────┘  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          MONITORING STACK                                    │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────────┐  │
│  │   Prometheus    │───▶│     Grafana     │    │   Metrics Collection    │  │
│  │   (Metrics)     │    │  (Visualization)│    │   & Alerting            │  │
│  └─────────────────┘    └─────────────────┘    └─────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘


💻 Technology Stack
Category	Technologies
Language	https://img.shields.io/badge/Python-3.10-3776AB?logo=python
Data Version Control	https://img.shields.io/badge/DVC-Data%2520Versioning-13ADC7?logo=dvc
Experiment Tracking	https://img.shields.io/badge/MLFlow-Experiments-0194E2?logo=mlflow • https://img.shields.io/badge/Dagshub-Remote%2520Tracking-2c3e50
Web Framework	https://img.shields.io/badge/Flask-API-000000?logo=flask
Containerization	https://img.shields.io/badge/Docker-Container-2496ED?logo=docker
Orchestration	https://img.shields.io/badge/Kubernetes-EKS-326CE5?logo=kubernetes • https://img.shields.io/badge/AWS-EKS-FF9900?logo=amazonaws
Cloud Services	https://img.shields.io/badge/AWS-S3-569A31?logo=amazons3 • https://img.shields.io/badge/AWS-ECR-FF9900
CI/CD	https://img.shields.io/badge/GitHub-Actions-2088FF?logo=githubactions
Monitoring	https://img.shields.io/badge/Prometheus-Metrics-E6522C?logo=prometheus • https://img.shields.io/badge/Grafana-Dashboards-F46800?logo=grafana
Infrastructure as Code	https://img.shields.io/badge/eksctl-Cluster%2520Management-FF9900 • https://img.shields.io/badge/kubectl-K8s%2520CLI-326CE5


✨ Features
📊 Data Management
Data Version Control with DVC for tracking datasets and models

Automated Data Pipelines with DVC repro for reproducible workflows

S3 Integration for scalable remote storage of data artifacts

🧪 Experiment Tracking
MLFlow Integration with Dagshub for experiment logging and comparison

Model Registry for versioning and promoting models

Parameter Management via centralized params.yaml

🔄 CI/CD Pipeline
Automated Testing on every push using GitHub Actions

Docker Image Building and pushing to AWS ECR

Zero-Downtime Deployment to EKS cluster

Environment Secrets Management with GitHub Secrets

☁️ Cloud Infrastructure
AWS EKS Cluster for container orchestration

AWS S3 for persistent data storage

AWS ECR for private Docker image registry

LoadBalancer Service for external traffic routing

📈 Monitoring & Observability
Prometheus for metrics collection and scraping

Grafana for real-time dashboards and visualization

Custom Metrics from Flask application

Alerting capabilities for proactive monitoring


📁 Project Structure

atlas-mlops/
├── .github/workflows/
│   └── ci.yaml                 # CI/CD pipeline definition
├── flask_app/
│   ├── app.py                  # Flask application entry point
│   ├── requirements.txt        # Python dependencies
│   └── Dockerfile              # Container configuration
├── src/
│   ├── __init__.py
│   ├── logger.py               # Logging configuration
│   ├── data_ingestion.py       # Data loading module
│   ├── data_preprocessing.py   # Data cleaning & transformation
│   ├── feature_engineering.py  # Feature creation module
│   ├── model_building.py       # Model training script
│   ├── model_evaluation.py     # Model performance metrics
│   └── register_model.py       # Model version registration
├── tests/                      # Unit & integration tests
├── scripts/                    # Utility scripts
├── models/                     # Saved model artifacts
├── dvc.yaml                    # DVC pipeline definition
├── params.yaml                 # Hyperparameters configuration
├── dvc.lock                    # Pipeline lock file
├── requirements.txt            # Core dependencies
├── Dockerfile                  # Root Docker configuration
├── deployment.yaml             # Kubernetes deployment manifest
└── README.md                   # Project documentation


🚢 Infrastructure & Deployment
🐳 Containerization
# Multi-stage Docker build for optimized images
FROM python:3.10-slim AS builder
...
FROM python:3.10-slim
COPY --from=builder /app /app
EXPOSE 5000
CMD ["python", "app.py"]

☸️ Kubernetes Deployment
# EKS Deployment with LoadBalancer service
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: flask-app
---
apiVersion: v1
kind: Service
metadata:
  name: flask-app-service
spec:
  type: LoadBalancer
  ports:
    - port: 5000
      targetPort: 5000

🔐 Security & IAM
Least Privilege Access for IAM users and roles

Secrets Management via Kubernetes Secrets and GitHub Secrets

Private Container Registry (ECR) for secure image storage

📊 Monitoring & Observability
Prometheus Configuration
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "flask-app"
    static_configs:
      - targets: ["<load-balancer-dns>:5000"]

Grafana Dashboards
Real-time metrics visualization

Custom dashboards for model performance

System resource monitoring (CPU, Memory, Network)

Alert rules for anomaly detection
⚡ CI/CD Pipeline
graph LR
    A[Code Push] --> B[Run Tests]
    B --> C[Build Docker Image]
    C --> D[Push to ECR]
    D --> E[Deploy to EKS]
    E --> F[Health Check]
    F --> G[Update LoadBalancer]

Stage	Description	Tools
Test	Unit & integration tests	pytest, GitHub Actions
Build	Docker image creation	Docker, Dockerfile
Push	Upload to registry	AWS ECR, AWS CLI
Deploy	Kubernetes deployment	kubectl, eksctl
Verify	Health check & validation	curl, custom scripts


🚀 Getting Started
Prerequisites
# Required installations
- Python 3.10+
- Docker Desktop
- kubectl
- eksctl
- AWS CLI
- Git

Local Development Setup
# Clone repository
git clone https://github.com/your-username/atlas-mlops.git
cd atlas-mlops

# Create virtual environment
conda create -n atlas python=3.10
conda activate atlas

# Install dependencies
pip install -r requirements.txt

# Run locally
cd flask_app
python app.py

DVC Pipeline Execution
# Initialize DVC
dvc init

# Configure remote storage
dvc remote add -d myremote s3://your-bucket-name

# Run pipeline
dvc repro

# Check status
dvc status

Docker Build & Run
# Build image
docker build -t capstone-app:latest .

# Run container
docker run -p 8888:5000 -e CAPSTONE_TEST=<your-token> capstone-app:latest

Deploy to EKS
# Create EKS cluster
eksctl create cluster --name flask-app-cluster --region us-east-1 \
  --nodegroup-name flask-app-nodes --node-type t3.small --nodes 1

# Update kubeconfig
aws eks --region us-east-1 update-kubeconfig --name flask-app-cluster

# Deploy application
kubectl apply -f deployment.yaml

# Get LoadBalancer URL
kubectl get svc flask-app-service

👥 Contributors
Project Lead: Abhijeet Samal

Role: Software Engineer II

Contact: abhijeetsml4@gmail.com


📝 License
This project is for demonstration purposes as part of an MLOps portfolio.

<div align="center"> <sub>Built with ❤️ for Production ML Systems</sub> </div>