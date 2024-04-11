import streamlit as st
import pandas as pd
import pickle
# Load the trained model  from the pickle files
with open('adamodel.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
def predict_exited(data):
    # Predict the probability of exit
    predictions = model.predict(data)
    return predictions

# Streamlit app
st.title("Customer Churn Prediction")

# Input form for user to enter data
credit_score = st.number_input("Credit Score:", value=0)
gender = st.radio("Gender:", ("Male", "Female"))
age = st.number_input("Age:", value=0)
tenure = st.number_input("Tenure (months):", value=0)
balance = st.number_input("Balance ($):", value=0)
num_products = st.number_input("Number of Products:", value=0)
has_credit_card = st.radio("Has Credit Card:", ("Yes", "No"))
is_active_member = st.radio("Is Active Member:", ("Yes", "No"))
estimated_salary = st.number_input("Estimated Salary ($):", value=0)

# Convert categorical variables to numerical
gender_num = 1 if gender == "Male" else 0
has_credit_card_num = 1 if has_credit_card == "Yes" else 0
is_active_member_num = 1 if is_active_member == "Yes" else 0

# Create a DataFrame with user input data
data = pd.DataFrame([[credit_score, gender_num, age, tenure, balance, num_products,
                      has_credit_card_num, is_active_member_num, estimated_salary]],
                    columns=['CreditScore', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts',
                            'HasCrCard', 'IsActiveMember', 'EstimatedSalary'])

# Predictions
predictions = predict_exited(data)

# Display the prediction result
st.subheader("Prediction Result")
if predictions[0]==0:
    st.write("The chance of customer exiting is high")
else:
    st.write("The chance of customer exiting is less")
# Display the input data
st.subheader("Input Data")
st.write(data)
