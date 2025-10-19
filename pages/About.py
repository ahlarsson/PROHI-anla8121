import streamlit as st

st.set_page_config(page_title="About", layout="wide")

st.title("Anna Larsson")

st.markdown(
    """
## About this Project

During the DSHI course, I conducted a data science project that focused on applying analytical methods to health informatics problems. 
The goal of the project was to demonstrate the ability to clean and preprocess data, explore trends through visualization, and apply 
machine learning techniques to test hypotheses and classifier models. 

The domain area of the dataset was influences of Healthcare insurance expenses. The purpose of the dataset was to capture the
relationship between different personal characteristics such as age, gender, BMI, smoking and geographic factors, 
and how they may affect medical insurance charges.

Ice Cream Chart
For this Dashboard project I wanted to simulates ice cream sales data. 
The users can personalize the dashboard through several input widgets. 
By selecting their favorite flavor, number of scoops, and toppings, users 
generate synthetic “sales” data that updates the chart and metrics in 
real time.
"""
)
