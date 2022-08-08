from flask import Flask, render_template,jsonify, render_template_string, request
import config
from dataset.utils import CreditCardApproval

app = Flask(__name__)

@app.route('/')  

def hello_flask():

    print("Welcome to Data science")
    return 'vasanti'


@app.route('/Approval_status')

def credit_status():
    Gender = "Female"
    Married = "No"
    Dependents = 3
    Education = "Not Graduate"
    Self_Employed = "Yes"
    ApplicantIncome = 6851.0
    CoapplicantIncome = 1246.0
    LoanAmount = 133.0
    Loan_Amount_Term = 180.0
    Credit_History = 1.0
    Property_Area = "Urban"

    status_prediction = CreditCardApproval(Gender, Married, Dependents, Education, Self_Employed,
    ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area)
   
    status_prediction.get_approval_status()


    return jsonify({"Result": f"status of credit card aprroval:{status_prediction}"})

if __name__ == "__main__":
 app.run()