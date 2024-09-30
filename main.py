import streamlit as st
import pandas as pd
# from helper_functions import llm
from logics.customer_query_handler import process_user_message, filter_df, df_hdb_resale
from helper_functions.utility import check_password  
import json  # Added for JSON handling

# region <--------- Streamlit App Configuration --------->

st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("HDB Resale Flat Finder")

# Check if the password is correct.  
if not check_password():  
    st.stop()

form = st.form(key="form")
form.subheader("You can use this query below to find available HDB resale flats in Singapore, by querying the location and price range. The table output will show you information related to the HDB resale flats based on your query.")

user_prompt = form.text_area("E.g. I am looking for HDB resale flats in Tampines. I want to buy HDB resale flats from Bukit Panjang and my budget is SGD 500,000. I want to buy 16th floor unit in Ang Mo Kio, and my budget is SGD 300,000", height=100)

# Check if the submit button is working
if form.form_submit_button("Submit"):
    st.divider()

    try:
        # Process the user message
        response = process_user_message(user_prompt)
        st.write("Please refer to the results below:")
        st.write(response)
        
        # Filter the DataFrame based on the user input
        filtered_towns = filter_df(user_prompt)
        filtered_df = df_hdb_resale[df_hdb_resale['town'].isin(filtered_towns)]
        
        st.write("Other units to consider:")
        st.write(filtered_df)
    except Exception as e:
        st.error(f"Error processing your request: {e}")
    
    st.divider()
else:
    st.write("Form not yet submitted")  # Just for checking if the button logic is working correctly.
