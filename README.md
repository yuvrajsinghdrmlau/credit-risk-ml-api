# credit-risk-ml-api
Credit Risk Prediction API
End-to-End Machine Learning Deployment
Yuvraj Singh
1 Project Overview
This project demonstrates a complete Machine Learning deployment pipeline that predicts
whether a customer is risky or not for credit default.
The system includes model training, REST API development, containerization, and cloud
deployment.
2 Live API
Base URL
https://credit-risk-ml-api-8s0o.onrender.com
Swagger Documentation
https://credit-risk-ml-api-8s0o.onrender.com/docs
3 Architecture
Dataset → Model Training → Saved Model (model.pkl)
→ FastAPI Backend → Docker Container
→ Render Cloud Deployment → Public API
4 API Endpoints
4.1 Health Check
GET /
Response
{
"message": "Credit Risk Prediction API running"
}
4.2 Predict Credit Risk
POST /predict
Example Request
{
"limit_balance": 20000,
"sex": "male",
"education": "university",
"marriage": "single",
"age": 24,
1
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
5 Tech Stack
Machine Learning
• Python
• Scikit-Learn
• Pandas
• NumPy
Backend
• FastAPI
• Pydantic
Deployment
• Docker
• Render Cloud
6 Project Structure
credit-risk-ml-api
app.py
train_model.py
model.pkl
requirements.txt
Dockerfile
README.md
7 How to Run Locally
Clone repository
git clone https://github.com/yuvrajsinghdrmlau/credit-risk-ml-api.git
cd credit-risk-ml-api
Install dependencies
pip install -r requirements.txt
Run API
uvicorn app:app --reload
2
8 Key Learnings
• Machine Learning model deployment
• REST API development using FastAPI
• Docker containerization
• Cloud deployment on Render
• Production ML pipeline
9 Author
Yuvraj Singh
GitHub: https://github.com/yuvrajsinghdrmlau
3
