# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:24:40 2023

@author: ELCOT
"""
import pandas as pd
import numpy as np
import pickle
import streamlit as st
def form():
    loaded_model = pickle.load(open('Sales_Trained_Model.sav', 'rb'))
    
    # Creating function for prediction
    def sales_prediction(input_data):
        # Change the input data to a numpy array
        input_data_np_array = np.asarray(input_data)
        # Reshape the numpy array as we are predicting for only one instance
        input_data_reshaped = input_data_np_array.reshape(1, -1)
        
        columns=['TV','Radio','Newspaper']
        # Make predictions using the trained sales prediction model
        input_data_reshaped_df=pd.DataFrame(input_data_reshaped,columns=columns)
        
        prediction=loaded_model.predict(input_data_reshaped_df)
        # Display prediction result
        st.subheader("Predicted Sales:")
        st.write(prediction[0])
        
    def main():
        st.title('Sales Prediction Web App')
        st.write("Enter Advertising Expenses: ")
        TV = st.text_input("TV Advertising Expense")
        Radio = st.text_input('Radio Advertising Expense')
        Newspaper = st.text_input("Newspaper Advertising Expense")
        
        if st.button('Predict Sales'):
            sales_prediction([TV,Radio,Newspaper])
    
    # Run the main function
    main()
