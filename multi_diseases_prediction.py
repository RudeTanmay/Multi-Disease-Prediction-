import pickle
import streamlit as st  
from streamlit_option_menu import option_menu
import numpy as np

diabetes_model=pickle.load(open('train_model.sav','rb'))
heart_model=pickle.load(open('trained_model.sav','rb'))

def dia_pred(input_data):
            input_data_numeric = [float(x) for x in input_data]
            input_reshape = np.array(input_data_numeric).reshape(1, -1)
            prediction=diabetes_model.predict(input_reshape)
            if(prediction[0]==1):
                return "The pPerson is Diabetic"
            else:
                return "The person is not Diabetic"
            
def heart_pred(input_data):
    # Convert input data to numeric values
    input_data_numeric = [float(x) for x in input_data]
    input_reshape = np.array(input_data_numeric).reshape(1, -1)
    
    # Make prediction
    prediction = heart_model.predict(input_reshape)
    
    # Interpret prediction
    if prediction[0] == 0:
        return "Person does not have heart disease"
    else:
        return "Person has heart disease"
def main():
    with st.sidebar:
        selected=option_menu('Multiple Diseases Prediction System',
                            ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                            icons=['activity','heart'],
                            default_index=0)
        
    if(selected=='Diabetes Prediction'):
        st.title('Diabetes Prediction Using Naive Bayes Algorithm')
        Pregnancies=st.text_input('Number of Pregnancies')
        Glucose=st.text_input('Glucose Level')
        BloodPressure=st.text_input('Blood Pressure')
        SkinThickness=st.text_input('SkinThickness')
        Insulin=st.text_input('Insulin')
        BMI =st.text_input('Body Mass Index')
        DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function")
        Age=st.text_input("Age")

        diab_diagnosis=''
        if st.button("Predict"):
            diab_diagnosis=dia_pred([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
            st.success(diab_diagnosis)

    if(selected=='Heart Disease Prediction'):
        st.title('Heart Disease Prediction Using Logistic Regression ')
        st.title("Heart Disease Predictor")

        age =st.text_input("Enter the Age")
        sex =st.text_input("Gender 0.Female 1. Male ")
        cp= st.text_input('''Angina Pectoris: 2
                            Stable Angina: 1
                            Unstable Angina: 3
                            Prinzmetal's (Variant) Angina: 2''')
        trestbps=st.text_input("Resting blood pressure (in mm Hg on admission to the hospital)")
        chol=st.text_input("Serum cholestoral in mg/dl")
        fbs=st.text_input("Fasting blood sugar > 120 mg/dl")
        restecg=st.text_input("Resting Electrocardiographic Results (0: Normal, 1: Abnormal ST-T wave changes, 2: Probable or Definite Left Ventricular Hypertrophy)")
        thalach=st.text_input("Maximum heart rate achieved")
        exang=st.text_input("Exercise Induced Angina (1: Yes, 0: No)")
        oldpeak = st.text_input("Oldpeak (ST Depression Induced by Exercise Relative to Rest)")
        slope=st.text_input("The slope of the peak exercise ST segment")
        ca=st.text_input("Number of major vessels (0-3) colored by flourosopy")
        thal=st.text_input(" Thal (0: Normal, 1: Fixed Defect, 2: Reversible Defect)")
        Diagnosis=''
        if st.button("Predict"):
            Diagnosis=heart_pred([age,	sex	,cp	,trestbps,	chol,	fbs,	restecg,	thalach	,exang	,oldpeak	,slope	,ca	,thal	])
            st.success(Diagnosis)

if __name__=='__main__':
     main()
