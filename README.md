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