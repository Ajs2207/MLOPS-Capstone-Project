# 🚀 MLOps Pipeline

<div align="center">

[![MLOps](https://img.shields.io/badge/MLOps-Capstone-blue?style=for-the-badge)](https://ml-ops.org/)
[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-API-red?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-EKS-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)

**An End-to-End Machine Learning Operations Pipeline with Automated CI/CD, Container Orchestration, and Real-Time Monitoring**

</div>

---

## 📋 Table of Contents
- [✨ Overview](#-overview)
- [🏗️ Architecture](#️-architecture)
- [🛠️ Technology Stack](#️-technology-stack)
- [🚀 Features](#-features)
- [📁 Project Structure](#-project-structure)
- [🔧 Infrastructure & Deployment](#-infrastructure--deployment)
- [📊 Monitoring & Observability](#-monitoring--observability)
- [⚡ CI/CD Pipeline](#-cicd-pipeline)
- [🚀 Getting Started](#-getting-started)
- [📞 Contact](#-contact)

---

## ✨ Overview

**Atlas** is a production-grade MLOps pipeline that demonstrates the complete lifecycle of machine learning models - from data ingestion and experimentation to deployment and monitoring. This project showcases industry best practices for automating ML workflows, containerizing applications, orchestrating deployments on Kubernetes, and implementing comprehensive observability.

**Key Highlights:**
- 🔄 **End-to-End ML Pipeline**: From data ingestion to production-ready API
- ☁️ **Cloud-Native Architecture**: Leveraging AWS EKS, S3, and ECR
- 🤖 **Automated CI/CD**: GitHub Actions for seamless deployment
- 📈 **Production-Ready**: Scalable, maintainable, and monitored
- 🐳 **Container Orchestration**: Docker + Kubernetes on EKS
- 📊 **Real-Time Monitoring**: Prometheus & Grafana integration

---

## 🏗️ Architecture

```mermaid
graph TB
    subgraph "CI/CD Pipeline"
        A[GitHub Push] --> B[GitHub Actions]
        B --> C[Run Tests]
        C --> D[Build Docker]
        D --> E[Push to ECR]
        E --> F[Deploy to EKS]
    end
    
    subgraph "Data & Experiment Tracking"
        G[DVC] --> H[S3 Bucket]
        I[MLFlow] --> J[Dagshub]
    end
    
    subgraph "Kubernetes Cluster EKS"
        K[Flask App Pod] --> L[LoadBalancer Service]
        L --> M[External Traffic]
    end
    
    subgraph "Monitoring Stack"
        N[Prometheus] --> O[Grafana]
        O --> P[Dashboards]
    end
    
    F --> K
    K --> N

🛠️ Tech Stack
Backend & ML
https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white Python 3.10

https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white Flask API

https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white Pandas & NumPy

https://img.shields.io/badge/-Scikit--learn-F7931E?logo=scikit-learn&logoColor=white Scikit-learn

Data Version Control & Experiment Tracking
https://img.shields.io/badge/-DVC-13ADC7?logo=dvc&logoColor=white DVC for Data Version Control

https://img.shields.io/badge/-MLFlow-0194E2?logo=mlflow&logoColor=white MLFlow Experiment Tracking

https://img.shields.io/badge/-Dagshub-2c3e50 Dagshub Remote Tracking

Containerization & Orchestration
https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white Docker Containerization

https://img.shields.io/badge/-Kubernetes-326CE5?logo=kubernetes&logoColor=white Kubernetes (EKS)

https://img.shields.io/badge/-eksctl-FF9900 eksctl Cluster Management

https://img.shields.io/badge/-kubectl-326CE5 kubectl CLI

Cloud Services (AWS)
https://img.shields.io/badge/-AWS%2520EKS-FF9900?logo=amazonaws&logoColor=white Amazon EKS

https://img.shields.io/badge/-AWS%2520S3-569A31?logo=amazons3&logoColor=white AWS S3 Storage

https://img.shields.io/badge/-AWS%2520ECR-FF9900?logo=amazonaws&logoColor=white Amazon ECR

https://img.shields.io/badge/-AWS%2520IAM-FF9900?logo=amazonaws&logoColor=white AWS IAM Security

CI/CD & Automation
https://img.shields.io/badge/-GitHub%2520Actions-2088FF?logo=githubactions&logoColor=white GitHub Actions CI/CD

https://img.shields.io/badge/-GitHub%2520Secrets-2088FF?logo=github&logoColor=white Secrets Management

Monitoring & Observability
https://img.shields.io/badge/-Prometheus-E6522C?logo=prometheus&logoColor=white Prometheus Metrics Collection

https://img.shields.io/badge/-Grafana-F46800?logo=grafana&logoColor=white Grafana Dashboards

Custom Logging Framework

Real-time Application Monitoring

Development Tools
https://img.shields.io/badge/-Cookiecutter-D4AA00?logo=cookiecutter&logoColor=white Data Science Project Template

https://img.shields.io/badge/-Git-F05032?logo=git&logoColor=white Version Control

https://img.shields.io/badge/-Jupyter-F37626?logo=jupyter&logoColor=white Development Notebooks

📦 Pipeline Components
Data Pipeline
https://img.shields.io/badge/-Data%2520Ingestion-4CAF50 MongoDB-like Data Loading

https://img.shields.io/badge/-Data%2520Preprocessing-2196F3 Cleaning & Transformation

https://img.shields.io/badge/-Feature%2520Engineering-FF9800 Feature Creation

https://img.shields.io/badge/-DVC%2520Pipeline-13ADC7 Reproducible Workflows

Model Pipeline
https://img.shields.io/badge/-Model%2520Building-9C27B0 Training & Hyperparameter Tuning

https://img.shields.io/badge/-Model%2520Evaluation-F44336 Performance Metrics

https://img.shields.io/badge/-Model%2520Registry-607D8B Version Control & Storage

https://img.shields.io/badge/-Model%2520Serving-795548 Flask API Endpoint

Infrastructure Components
https://img.shields.io/badge/-Parameter%2520Management-FF5722 params.yaml Configuration

https://img.shields.io/badge/-Logging-9E9E9E Centralized Logger

https://img.shields.io/badge/-Testing-4CAF50 Unit & Integration Tests

https://img.shields.io/badge/-Utility%2520Scripts-607D8B Automation Scripts

🔄 CI/CD Pipeline Stages
Stage	Tools	Purpose
Code Commit	Git, GitHub	Version control & collaboration
Continuous Integration	GitHub Actions, pytest	Automated testing & validation
Container Build	Docker, Dockerfile	Image creation & optimization
Registry Push	AWS ECR, AWS CLI	Private image storage
Continuous Deployment	kubectl, eksctl	Kubernetes deployment
Health Check	curl, custom scripts	Deployment verification
☁️ AWS Services Used
Service	Purpose
EKS (Elastic Kubernetes Service)	Container orchestration cluster
S3 (Simple Storage Service)	DVC remote storage for datasets & models
ECR (Elastic Container Registry)	Private Docker image repository
EC2	Prometheus & Grafana server instances
IAM	Access management & security policies
LoadBalancer	External traffic routing to EKS
📊 Monitoring Stack Components
Prometheus Server
Deployed on EC2 (t3.medium)

Scrapes metrics from Flask app every 15s

Stores time-series data

Configurable alerting rules

Grafana Server
Deployed on EC2 (t3.medium)

Visualizes metrics from Prometheus

Custom dashboards for model performance

Real-time system monitoring

Metrics Tracked
Request latency & throughput

Model prediction times

Error rates & success rates

CPU & Memory utilization

Custom application metrics

🔒 Security Components
IAM Roles & Policies: Least privilege access control

GitHub Secrets: Encrypted environment variables

AWS Security Groups: Network-level firewall rules

Kubernetes Secrets: Container-level secret management

Private Repositories: Code & image security

🧪 Testing Framework
Test Type	Tools	Coverage
Unit Tests	pytest	Individual functions & modules
Integration Tests	pytest	Pipeline component interactions
API Tests	curl, requests	Flask endpoint validation
Model Tests	custom scripts	Model accuracy & performance