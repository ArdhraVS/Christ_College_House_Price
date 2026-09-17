import streamlit as st
import joblib

model=joblib.load("MultilinearRegression_HousePrice_model.pkl")
st.title("House Price Prediction")
area=st.number_input("Enter Area:", min_value=600.0 ,max_value=3000.0, value=600.0)
bedrooms=st.number_input("Enter no of bedrooms:", min_value=1 ,max_value=4, value=3)
floors=st.number_input("Enter no of floors:", min_value=0 ,max_value=10, value=1)

if st.button("Predict"):
  if area<600 or area>3000:
    st.error("Area should be within the 600 - 3000")
  elif (bedrooms<1 or bedroom>4):
    st.error("Bedrooms should be within the range 1 - 4")
  elif floors<0 and floors>10:
    st.error("Floors should be within the range 0 - 10")
  else:
    prediction=model.predict([[area,bedrooms,floors]])
    st.success(f"Predicted price: {prediction[0]:.2f} Lakhs")
