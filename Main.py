# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 14:51:40 2023

@author: ELCOT
"""

from streamlit_option_menu import option_menu
import home, Visualization, Dataset, Input_Form

st.set_page_config(page_title="Sales Prediction",page_icon="coin",layout="wide")

selected = option_menu(
                        menu_title="Sales",
                        options=["Home", "Dataset","Visualization", "Input_Form"],
                        icons=["house-door", "database-down", "pie-chart", "ui-checks-grid"],
                        default_index=0,
                        menu_icon="receipt",
                        orientation="horizontal"
                       )
if selected == "Home":
    home.home()
if selected == "Dataset":
    Dataset.dataset()
if selected == "Input_Form":
    Input_Form.form()
if selected == "Visualization":
    Visualization.visualization()
