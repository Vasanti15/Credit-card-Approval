import pickle
import json
import re
import numpy as np
import config

class CreditCardApproval():
    def __init__ (self, Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, 
    CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area):

        self.Gender = Gender
        self.Married = Married
        self.Dependents = Dependents
        self.Education = Education
        self.Self_Employed = Self_Employed
        self.ApplicantIncome = ApplicantIncome
        self.CoapplicantIncome = CoapplicantIncome
        self.LoanAmount = LoanAmount
        self.Loan_Amount_Term = Loan_Amount_Term
        self.Credit_History = Credit_History
        self.Property_Area =  'Property_Area_' + Property_Area

    def load_model (self):
        with open (config.PICKLE_FILE_PATH,"rb") as f:
            self.pkl = pickle.load(f)

        with open (config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)
    
    def get_approval_status(self):
        self.load_model()

        Property_Area_index = self.json_data["columns"].index(self.Property_Area)

        test_array = np.zeros(len( self.json_data["columns"]))

        test_array[0] = self.json_data['Gender'][self.Gender]
        test_array[1] = self.json_data['Married'][self.Married]
        test_array[2] = self.Dependents
        test_array[3] = self.json_data['Education'][self.Education]
        test_array[4] = self.json_data['Self_Employed'][self.Self_Employed]
        test_array[5] = self.ApplicantIncome
        test_array[6] = self.CoapplicantIncome
        test_array[7] = self.LoanAmount
        test_array[8] = self.Loan_Amount_Term
        test_array[9] = self.Credit_History
        test_array[Property_Area_index] = 1    

        approval_status = self.pkl.predict([test_array])
        return approval_status


if __name__ == "__main__":
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

    cc_aprroval_status_pred = CreditCardApproval(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, 
    LoanAmount, Loan_Amount_Term, Credit_History, Property_Area)
    cc_aprroval_status_pred.get_approval_status()