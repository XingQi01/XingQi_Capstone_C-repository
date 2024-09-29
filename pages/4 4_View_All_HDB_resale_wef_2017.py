import streamlit as st
import pandas as pd



# Load the CSV file
filepath = './data/Resale_prices_wef_2017.csv'  # Make sure the path points to your CSV file
df = pd.read_csv(filepath)



# display the `dict_of_course` as a Pandas DataFrame

# Streamlit App Overview
st.write("""
# HDB resale flats since Jan 2017 """)
         
df = pd.DataFrame(df)
df