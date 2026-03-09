![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Render](https://img.shields.io/badge/Deployed%20on-Render-purple)


# Credit Risk Prediction API (End-to-End ML Deployment)

A production-ready Machine Learning API that predicts whether a customer is **Risky** or **Not Risky** for credit default.

This project demonstrates a complete **ML deployment pipeline** including model training, API development, containerization, and cloud deployment.

---

# Live API

Base URL

https://credit-risk-ml-api-8s0o.onrender.com

Swagger Documentation

https://credit-risk-ml-api-8s0o.onrender.com/docs

---
<img width="1854" height="939" alt="image" src="https://github.com/user-attachments/assets/ed68b6b6-2ad5-4148-8600-1f2954ad29de" />
<img width="1861" height="843" alt="image" src="https://github.com/user-attachments/assets/62952289-c061-43cd-901f-7ba2d8583b28" />


# Architecture

Dataset  
↓  
Machine Learning Model Training (Scikit-Learn)  
↓  
Saved Model (model.pkl)  
↓  
FastAPI REST API  
↓  
Docker Container  
↓  
Render Cloud Deployment  
↓  
Public Prediction API  

---

# API Endpoints

## Health Check

GET /

Response

```json
{
  "message": "Credit Risk Prediction API running"
}


Predict Credit Risk

POST /predict

Example Request

{
  "limit_balance": 20000,
  "sex": "male",
  "education": "university",
  "marriage": "single",
  "age": 24,
  "pay_0": -1,
  "pay_2": -1,
  "pay_3": -1,
  "pay_4": -1,
  "pay_5": -2,
  "pay_6": -2
}
Example Response
{
  "credit_risk": "Not Risky"
}
Tech Stack

Machine Learning

Python

Scikit-Learn

Pandas

NumPy

Backend

FastAPI

Pydantic

Deployment

Docker

Render Cloud

Tools

Git

GitHub

Project Structure

credit-risk-ml-api
│
├── app.py
├── train_model.py
├── model.pkl
├── requirements.txt
├── Dockerfile
└── README.md

Run Locally

Clone repository

git clone https://github.com/yuvrajsinghdrmlau/credit-risk-ml-api.git
cd credit-risk-ml-api

Install dependencies

pip install -r requirements.txt

Run API

uvicorn app:app --reload

Open Swagger UI

http://127.0.0.1:8000/docs
Docker Usage

Build image

docker build -t credit-risk-api .

Run container

docker run -p 8000:8000 credit-risk-api
Learning Outcomes

Machine Learning model training

Model serialization using joblib

REST API development using FastAPI

Interactive API documentation using Swagger

Containerization using Docker

Cloud deployment using Render

End-to-end MLOps workflow
