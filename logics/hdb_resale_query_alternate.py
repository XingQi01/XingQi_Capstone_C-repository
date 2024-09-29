
import os
from dotenv import load_dotenv
import json 
import requests
from helper_functions import llm
# Import the key CrewAI classes

# Load the environment variables
# If the .env file is not found, the function will return `False`
load_dotenv('.env')


# Initialize the web scraping tools

file_path1 = "./data/HDB_Terms_and_Conditions.txt"

with open(file_path1, 'r') as file:
    HDB_Terms_and_Conditions = file.read()

file_path2 = "./data/HDB_Application_source.txt"

with open(file_path2, 'r') as file:
    HDB_Application_source= file.read()


def policy_query(user_message):
    delimiter = "####"

    system_message = f"""
    You will be provided with customer service queries on HDB resale application procedures and terms and conditions \
    The customer service query will be enclosed in
    the pair of {delimiter}.

    Decide if the query is relevant to the datasets {HDB_Terms_and_Conditions} and {HDB_Application_source}.
    In HDB_Terms_and_Conditions there are information on policy for HDB resale. In HDB_Application_source there are application procedure details. 

    For query related to {HDB_Terms_and_Conditions} and {HDB_Application_source}, provide the response based on these datasets

    If no relevant informations are found, output an empty list.

    Ensure your response contains only all the relevant rows information from the two datasets \
    without any enclosing tags or delimiters.
    """

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    hdb_policy_str = llm.get_completion_by_messages(messages)
    hdb_policy_str = hdb_policy_str.replace("'", "\"")
    return hdb_policy_str

def process_user_message(user_input):

    reply = policy_query(user_input)
    
    return reply


