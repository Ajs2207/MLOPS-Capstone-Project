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


🛠️ Technology Stack
Category	Technologies
Language	https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white Python 3.10
Data Version Control	https://img.shields.io/badge/-DVC-13ADC7?logo=dvc&logoColor=white DVC
Experiment Tracking	https://img.shields.io/badge/-MLFlow-0194E2?logo=mlflow&logoColor=white MLFlow • https://img.shields.io/badge/-Dagshub-2c3e50 Dagshub
Web Framework	https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white Flask
Containerization	https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white Docker
Orchestration	https://img.shields.io/badge/-Kubernetes-326CE5?logo=kubernetes&logoColor=white Kubernetes • https://img.shields.io/badge/-EKS-FF9900?logo=amazonaws&logoColor=white AWS EKS
Cloud Services	https://img.shields.io/badge/-AWS%2520S3-569A31?logo=amazons3&logoColor=white S3 • https://img.shields.io/badge/-AWS%2520ECR-FF9900?logo=amazonaws&logoColor=white ECR
CI/CD	https://img.shields.io/badge/-GitHub%2520Actions-2088FF?logo=githubactions&logoColor=white GitHub Actions
Monitoring	https://img.shields.io/badge/-Prometheus-E6522C?logo=prometheus&logoColor=white Prometheus • https://img.shields.io/badge/-Grafana-F46800?logo=grafana&logoColor=white Grafana
Infrastructure	https://img.shields.io/badge/-eksctl-FF9900 eksctl • https://img.shields.io/badge/-kubectl-326CE5 kubectl
## 🛠️ Technology Stack


| Category | Technologies |
| :--- | :--- |
| **Language** | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) Python 3.10 |
| **Data Version Control** | ![DVC](https://img.shields.io/badge/-DVC-13ADC7?logo=dvc&logoColor=white) DVC |
| **Experiment Tracking** | ![MLFlow](https://img.shields.io/badge/-MLFlow-0194E2?logo=mlflow&logoColor=white) MLFlow • ![Dagshub](https://img.shields.io/badge/-Dagshub-2c3e50) Dagshub |
| **Web Framework** | ![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white) Flask |
| **Containerization** | ![Docker](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white) Docker |
| **Orchestration** | ![Kubernetes](https://img.shields.io/badge/-Kubernetes-326CE5?logo=kubernetes&logoColor=white) Kubernetes • ![EKS](https://img.shields.io/badge/-EKS-FF9900?logo=amazonaws&logoColor=white) AWS EKS |
| **Cloud Services** | ![S3](https://shields.io) S3 • ![ECR](https://shields.io) ECR |
| **CI/CD** | ![GitHub Actions](https://shields.io) GitHub Actions |
| **Monitoring** | ![Prometheus](https://img.shields.io/badge/-Prometheus-E6522C?logo=prometheus&logoColor=white) Prometheus • ![Grafana](https://img.shields.io/badge/-Grafana-F46800?logo=grafana&logoColor=white) Grafana |
| **Infrastructure** | ![eksctl](https://img.shields.io/badge/-eksctl-FF9900) eksctl • ![kubectl](https://img.shields.io/badge/-kubectl-326CE5) kubectl |

## 🚀 Features

### 📊 Data Management
* **Data Version Control** with DVC for tracking datasets and models
* **Automated Data Pipelines** with `dvc repro` for reproducible workflows
* **S3 Integration** for scalable remote storage of data artifacts

### 🧪 Experiment Tracking
* **MLFlow Integration** with Dagshub for experiment logging and comparison
* **Model Registry** for versioning and promoting models
* **Parameter Management** via centralized `params.yaml`

### 🔄 CI/CD Pipeline
* **Automated Testing** on every push using GitHub Actions
* **Docker Image Building** and pushing to AWS ECR
* **Zero-Downtime Deployment** to EKS cluster
* **Environment Secrets Management** with GitHub Secrets

### ☁️ Cloud Infrastructure
* **AWS EKS Cluster** for container orchestration
* **AWS S3** for persistent data storage
* **AWS ECR** for private Docker image registry
* **LoadBalancer Service** for external traffic routing

### 📈 Monitoring & Observability
* **Prometheus** for metrics collection and scraping
* **Grafana** for real-time dashboards and visualization
* **Custom Metrics** from Flask application


📁 Project Structure