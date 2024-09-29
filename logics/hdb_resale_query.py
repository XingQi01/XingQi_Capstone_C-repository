
import os
from dotenv import load_dotenv
import json 
import requests
import crewai
import crewai_tools
from helper_functions import llm
# Import the key CrewAI classes
from crewai import Agent, Task, Crew

# Load the environment variables
# If the .env file is not found, the function will return `False`
load_dotenv('.env')

# Import other necessary packages you need
from crewai_tools import FileReadTool
from crewai_tools import ScrapeWebsiteTool

# Initialize the web scraping tools
tool_read_termsandcondition = FileReadTool("./data/HDB_Terms_and_Conditions.txt")
tool_read_application = FileReadTool("./data/HDB_Application_source.txt")

# Agent 1: SOP advisor
sop_advisor = Agent(
    role= "Provide application advice for buying HDB resale flats",
    goal= "Provide comprehensive guidance on the application process for HDB resale flats, ensuring applicants understand each step and the necessary requirements to facilitate a smooth transaction.",
    tools=[tool_read_application],
    verbose=False,
    backstory=("""\As an expert in HDB resale applications, you possess a thorough understanding of the 
    various steps and requirements involved in the process. Your experience allows you to guide 
    applicants through each phase, ensuring they grasp the essential elements necessary for a successful 
    transaction. By clarifying complex procedures and addressing common concerns, you empower individuals
     to navigate the application process with confidence. Your support plays a crucial role in making the
      journey of purchasing an HDB resale flat as seamless as possible.
               """
              )
)

# Agent 2: Policy advisor
policy_advisor = Agent(
    role= "Policy advisor for applicants",
    goal= "Analyze the terms and conditions and provide guidance to customers",
    tools=[tool_read_termsandcondition, tool_read_application],
    verbose=False,
    backstory=("As a seasoned policy advisor, you possess a deep understanding of the intricacies involved in the sale and purchase of HDB flats. "
               "Your expertise allows you to navigate the regulatory landscape effectively, ensuring that both buyers and sellers comply with all "
               "necessary terms and conditions. With a keen eye for detail, you analyze the legalities surrounding the resale process, "
               "including requirements for Intent to Sell and HDB Flat Eligibility Letters. Your guidance empowers clients to make informed decisions, "
               "helping them understand their rights and responsibilities throughout the transaction. By clarifying complex policies and offering "
               "tailored advice, you play a crucial role in facilitating smooth and compliant real estate dealings."
               
)
)

# Define tasks
sop_task = Task(
    description="""\Provide full details on application procedures for purchasing HDB resale flat. """,
    expected_output="Application procedure HDB resale flat.",
    agent=sop_advisor,
    async_execution=False  # This task is synchronous
)

policy_task = Task(
    description="""\Compile information on HDB resale based on terms and conditions and also make references to the application procedures.""",
    expected_output="Comprehensive advice on the main terms and conditions of buying HDB resale flat.",
    agent=policy_advisor,
    async_execution=False  # This task is synchronous
)

crew = Crew(
    agents=[sop_advisor, policy_advisor],
    tasks=[sop_task, policy_task],
    verbose=False
)

def process_user_message(query_inputs):

    user_prompt = {"query": query_inputs}

    # Execute the tasks with the input query
    reply = crew.kickoff(inputs=user_prompt)

    # Print the result to inspect its structure (optional)
    print("Result structure:", reply)

    # Return the actual reply so that Streamlit can display it
    return reply







