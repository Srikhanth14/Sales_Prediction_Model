# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:16:38 2023

@author: ELCOT
"""

import streamlit as st
from PIL import Image

def visualization:
    
    # Visualization Page
    st.title("Visualizations")
    # Introduction
    st.write("Explore visualizations highlighting the relationship between advertising channels and sales.")
   
    # Image 1: Histogram Subplots
    st.header("Histogram Subplots")
    st.image("Histogram.png", caption="Histograms of TV, Radio, Newspaper Ad Spending, and Sales.", use_column_width=True)
    
    # Image 2: Total Advertising Expenditure by Medium
    st.header("Total Advertising Expenditure by Medium")
    st.image("Advertising.png", caption="Bar plot showing total advertising expenditure by TV, Radio, and Newspaper.", use_column_width=True)
    
    # Image 3: Scatter Plot Subplots
    st.header("Scatter Plot Subplots")
    st.image("Scatter.png", caption="Scatter plots of Radio, TV, and  Newspaper Ad Spending.", use_column_width=True)
    
    # Image 4: Correlation Heatmap
    st.header("Correlation Heatmap")
    st.image("Correlation.png", caption="Heatmap showing correlation between variables.", use_column_width=True)
   
    # Image 5: Scatter Plot of Test and Train Data
    st.header("Scatter Plot of Test and Train Data")
    st.image("Train_Test.png", caption="Scatter plot comparing Test and Train data.", use_column_width=True)
    
    # Call to Action
    st.write("Ready to make predictions? Head to the **Input Form** and input your data for personalized sales forecasts.")
