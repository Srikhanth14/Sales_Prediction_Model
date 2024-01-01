# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:00:03 2023

@author: ELCOT
"""

import streamlit as st
from PIL import Image

def home():
    st.image(Image.open('Sales.jpg'),use_column_width=True)
    
    # Introduction
    st.header("Welcome to the Sales Prediction App!")
    st.write('''Explore the art of predicting sales with cutting-edge data science. This web app is a
    testament to my dedication to unraveling patterns in advertising data—enabling accurate
    sales forecasts.''')
    
    # Key Features
    st.subheader("Key Features:")
    st.write('''1. **Predictive Analytics:** Dive into the capabilities of predictive analytics. My model analyzes data from TV, Radio,and Newspaper advertising to provide accurate sales forecasts.''')
    
    st.write('''2. **User-Friendly Interface:**Experience a seamless journey through the app's user-friendly interface. No coding skills required – simply input your data and witness the predictive power.''')
    
    st.write('''3. **Data Visualization:** Visualize the impact of each advertising channel on sales with interactive charts and graphs. Gain valuable insights for your business strategies.''')
    
    # About Me
    st.subheader("About Me:")
    st.write('''Curious about the mind behind the model? I'm SRIKHANTH R, a passionate data analyst dedicated to leveraging technology for insightful predictions.''')
    st.write("Feel free to reach out if you have questions, collaborations, or just want to chat about data science and analyst!")
    st.write("Check out my [portfolio](https://www.datascienceportfol.io/srikhanth_r) to explore more of my data science projects.")
    st.write("Connect with me on [LinkedIn](https://www.linkedin.com/in/srikhanth-r). I'd love to hear from you!")
    
    # Call to Action
    st.write('''Ready to explore the world of sales forecasting? Head over to the **Dataset** page
    to upload your data and witness the results firsthand!''')
