# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 14:51:40 2023

@author: ELCOT
"""

from streamlit_option_menu import option_menu
import home, Visualization, Dataset, Input_Form

selected = option_menu(
                        menu_title="Main Menu",
                        options=["Home", "Dataset","Visualization", "Input_Form"],
                        icons=["home", "bar-chart", "edit", "check"],
                        default_index=0,
                        orientation="horizontal"
                       )
if selected == "Home":
    home.home()
if selected == "Dataset":
    Dataset.dataset()
if selected == "Input_form":
    Input_Form.form()
if selected == "Visualization":
    Visualization.visualization()
