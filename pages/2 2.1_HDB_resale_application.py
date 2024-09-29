# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
from helper_functions import llm
from logics.hdb_resale_query import process_user_message
from helper_functions.utility import check_password  

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("HDB resale Application Procedure query (via Crewai)")

 # Check if the password is correct.  
if not check_password():  
     st.stop()


form = st.form(key="form")
form.subheader("Enter your prompt below to ask questions about how to apply for HDB resale flats.")

user_prompt = form.text_area("E.g. How to buy HDB resale flat? What are the terms and conditions for purchasing a HDB resale flat?", height=100)

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")

    response = process_user_message(user_prompt)
   
    # Display the extracted answer
    st.write(response)





