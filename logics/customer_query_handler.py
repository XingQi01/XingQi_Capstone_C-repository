import os
import pandas as pd
import openai
from helper_functions import llm
import streamlit as st
import json  # Added for JSON handling

# Load the Resale.csv file
filepath = './data/Resale_prices_wef_2017.csv'  # Make sure the path points to your CSV file
try:
    df_hdb_resale = pd.read_csv(filepath)
except FileNotFoundError:
    st.error(f"File not found: {filepath}")
    df_hdb_resale = pd.DataFrame()  # Empty DataFrame as fallback

unique_towns = df_hdb_resale['town'].unique() if not df_hdb_resale.empty else []
unique_price = df_hdb_resale['resale_price'].unique() if not df_hdb_resale.empty else []

def identify_hdb_flats(user_message):
    delimiter = "####"

    system_message = f"""
    You will be provided with customer service queries on HDB resale towns and prices. \
    The customer service query will be enclosed in
    the pair of {delimiter}.

    Decide if the query is relevant to the datasets in unique_towns and unique_price.
    In unique_towns there are towns with HDB resale units. In unique_price there are prices of HDB resale units. 

    For query on unique_towns, if there are any relevant HDB flats found, output the pair(s) of a) unique_towns and b) the range of unique_price from minimum to maximum. 
    Output all the relevant HDB flats from df_hdb_resale, and add serial number in column 1.

    For query on unique_price, if there are any relevant HDB flats found, output unique_towns where the unique_price ranges between 100000 below and 100000 above the 
    queried unique_price. Output all the relevant HDB flats from df_hdb_resale, and add serial number in column 1. 

    {unique_towns}
    {unique_price}

    If no relevant HDB flats are found, output an empty list.

    Ensure your response contains only all the relevant rows from df_hdb_resale \
    without any enclosing tags or delimiters.
    """

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    hdb_flats_str = llm.get_completion_by_messages(messages)
    hdb_flats_str = hdb_flats_str.replace("'", "\"")
    return hdb_flats_str

def generate_response_based_on_hdb_flat(user_message, unique_towns):
    delimiter = "####"

    system_message = f"""
    Follow these steps to answer the customer queries.
    The customer query will be delimited with a pair {delimiter}.

    Step 1:{delimiter} If the user is asking about hdb towns, \
    understand the towns with hdb flats from the following list.
    All available courses shown in the csv data below:
    {unique_towns}

    Step 2:{delimiter} Use the information about hdb resale flats to \
    generate the answer for the customer's query.
    You must only rely on the facts or information in the hdb flats.
    Your response should be as detailed as possible and \
    include information that is useful for the customer to better understand the course.

    Step 3:{delimiter} Answer the customer in a friendly tone.
    Make sure the statements are factually accurate.
    Your response should be comprehensive and informative to help the \
    customers make their decision.
    Complete with details with 5 recommended list of hdb flats for the customer to buy. 
    Use Neural Linguistic Programming to construct your response.

    Use the following format:
    Step 1:{delimiter} <step 1 reasoning>
    Step 2:{delimiter} <step 2 reasoning>
    Step 3:{delimiter} <step 3 response to customer>
    """

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    response_to_customer = llm.get_completion_by_messages(messages)
    response_to_customer = response_to_customer.split(delimiter)[-1]
    return response_to_customer

import re

def extract_unique_towns(hdb_flats_str):
    """
    Extracts unique town names from the input string, ignoring any numerical values (e.g., prices).

    Parameters:
    hdb_flats_str (str): String containing town names and possible numerical values.

    Returns:
    list: A list of unique town names.
    """

    # Split the string into lines
    lines = hdb_flats_str.splitlines()

    # Regular expression to extract town names (text after the first number and before the next number)
    town_names = []
    for line in lines:
        if line.strip():  # Ensure the line is not empty
            match = re.search(r"\d+\s+([A-Za-z\s]+)\s+\d+", line)
            if match:
                town_names.append(match.group(1).strip())

    # Return unique town names
    return list(set(town_names))


def process_user_message(user_input):
    user_input1 = identify_hdb_flats(user_input)
    reply = generate_response_based_on_hdb_flat(user_input1, unique_towns)
    return reply

def filter_df(user_input):
    user_input1 = identify_hdb_flats(user_input)
    reply = extract_unique_towns(user_input1)
    return reply