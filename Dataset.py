# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:06:19 2023

@author: ELCOT
"""

import streamlit as st
import pandas as pd
def dataset():
    # Dataset Information
    st.header("Dataset Information:")
    st.write('''The predictive model is trained on a dataset obtained from Kaggle. It includes
    information about advertising channels such as TV, Radio and Newspaper''')
    
    # Data Source
    st.header("Data Source:")
    st.write("For more details, you can explore the dataset on Kaggle: [Click here](https://www.kaggle.com/code/ashydv/sales-prediction-simple-linear-regression)")
    
    # Sample Data
    st.header("Sample Data:")
    st.write("Here's a glimpse of the dataset:")
    
    data=pd.read_csv("advertising.csv")
    st.dataframe(data.head())
    
    st.subheader("Download Dataset")
    st.write("You can download the full Sales dataset for further exploration:")
    def data_read(data):
        return data.to_csv().encode('utf-8')
    
    csv=data_read(data)
    st.download_button(
                        label='Download Sample Data',
                        data=csv,
                        file_name='sales.csv',
                        mime='text/csv'
                      )
    
    # Input Your Data
    st.header("Input Your Data:")
    st.write("Want predictions for your specific advertising expenses? Enter your data in the input form and discover the forecasted sales.")
    
    # Guidance on Data Format
    st.header("Guidance on Data Format:")
    st.write('''To ensure successful predictions, enter your data in the same format as the sample
    data. Include columns for TV, Radio, and Newspaper advertising expenses.''')
    
    # GitHub Link
    st.header("GitHub Repository:")
    st.write("Explore the code and details of this project on my GitHub repository:")
    st.write("[Sales Prediction GitHub Repository](https://github.com/Srikhanth14/CODSOFT/blob/main/Project_4_Sales_Prediction_Using_Python.ipynb)")
    
    # Conclusion
    st.write('''Ready to get predictions for your data? Input your data in the input form, and let the
    Sales Prediction app work its magic!''')
