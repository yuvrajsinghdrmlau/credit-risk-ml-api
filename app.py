from fastapi import FastAPI
from pydantic import BaseModel, Field
from enum import Enum
import joblib

app = FastAPI(
    title="Credit Risk Prediction API",
    description="""
Predict whether a customer is risky or not.

Field meanings:
- sex → male / female
- marriage → married / single / other
- education → graduate_school / university / high_school / others
""",
    version="1.0"
)

# Load trained ML model
model = joblib.load("model.pkl")


# Enums for readable inputs
class Sex(str, Enum):
    male = "male"
    female = "female"


class Marriage(str, Enum):
    married = "married"
    single = "single"
    other = "other"


class Education(str, Enum):
    graduate_school = "graduate_school"
    university = "university"
    high_school = "high_school"
    others = "others"


# Input schema
class CreditInput(BaseModel):

    limit_balance: float = Field(..., description="Credit limit of the customer")

    sex: Sex = Field(..., description="Gender of customer: male or female")

    education: Education = Field(
        ..., description="Education level: graduate_school / university / high_school / others"
    )

    marriage: Marriage = Field(
        ..., description="Marital status: married / single / other"
    )

    age: int = Field(..., description="Age of the customer")

    pay_0: int = Field(..., description="Repayment status in September")
    pay_2: int = Field(..., description="Repayment status in August")
    pay_3: int = Field(..., description="Repayment status in July")
    pay_4: int = Field(..., description="Repayment status in June")
    pay_5: int = Field(..., description="Repayment status in May")
    pay_6: int = Field(..., description="Repayment status in April")

    bill_amt1: float = 0
    bill_amt2: float = 0
    bill_amt3: float = 0
    bill_amt4: float = 0
    bill_amt5: float = 0
    bill_amt6: float = 0

    pay_amt1: float = 0
    pay_amt2: float = 0
    pay_amt3: float = 0
    pay_amt4: float = 0
    pay_amt5: float = 0
    pay_amt6: float = 0

    class Config:
        schema_extra = {
            "example": {
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
        }


@app.get("/")
def home():
    return {"message": "Credit Risk Prediction API running"}


@app.post("/predict")
def predict(data: CreditInput):

    # Convert readable inputs to numeric values for the ML model
    sex_map = {"male": 1, "female": 2}

    marriage_map = {
        "married": 1,
        "single": 2,
        "other": 3
    }

    education_map = {
        "graduate_school": 1,
        "university": 2,
        "high_school": 3,
        "others": 4
    }

    features = [[
        data.limit_balance,
        sex_map[data.sex],
        education_map[data.education],
        marriage_map[data.marriage],
        data.age,
        data.pay_0,
        data.pay_2,
        data.pay_3,
        data.pay_4,
        data.pay_5,
        data.pay_6,
        data.bill_amt1,
        data.bill_amt2,
        data.bill_amt3,
        data.bill_amt4,
        data.bill_amt5,
        data.bill_amt6,
        data.pay_amt1,
        data.pay_amt2,
        data.pay_amt3,
        data.pay_amt4,
        data.pay_amt5,
        data.pay_amt6
    ]]

    prediction = model.predict(features)[0]

    result = "Risky" if prediction == 1 else "Not Risky"

    return {"credit_risk": result}