import streamlit as st

# Streamlit App Overview
st.write("""
# Streamlit App Overview

This Streamlit App demonstrates how to use various tools and libraries to process and analyze HDB resale flat data via Large Language Model (LLM) methodologies. The app was initially developed using Visual Studio Code and then published on GitHub before being linked to Streamlit for deployment.
""")

# Features
st.write("""
## Features

1. **Query Processing**:
   - Enter your query in the text area and click the 'Submit' button.
   - The app will process your query using LLM, Crew AI, and non-Crew AI methodologies to provide relevant information based on the HDB resale data.

2. **Data Visualization**:
   - View all HDB resale data from 2017 onwards on the 'View All HDB Resale' page.
   - Interactive charts and graphs to help you understand trends and patterns in the data.

3. **Methodologies**:
   - **LLM Methodology**: Utilizes advanced language models to interpret and respond to user queries.
   - **Crew AI Methodology**: Employs collaborative AI techniques for enhanced data processing.
   - **OpenAI Methodology**: Leverages OpenAI's powerful models for natural language understanding

4. **Development and Deployment**:
   - Developed using Visual Studio Code for a robust coding environment.
   - Published on GitHub for version control and collaboration.
   - Linked to Streamlit for seamless deployment and user interaction.
""")

# How to Use
st.write("""
## How to Use

1. **Submit a Query**:
   - Type your question or query related to HDB resale flats in the text area.
   - Click the 'Submit' button to get insights and information based on the latest data.

2. **View All HDB Resale Data**:
   - Navigate to the 'View All HDB Resale' page to explore comprehensive data from 2017 onwards.
   - Use filters and search options to find specific information.
""")

# Source data
st.write("""
## Source data

- Application procedures: https://www.hdb.gov.sg/residential/selling-a-flat/resale-application/application 
- Terms and Conditions for buying or selling HDB resale: https://www.hdb.gov.sg/cs/infoweb/e-resale/resale-purchase-of-an-hdb-resale-flat
- Hdb resale flat database (Jan 2017 onwards): https://data.gov.sg/collections/189/view
""")

# Additional Information
st.write("""
## Additional Information

- The app leverages the power of large language models to provide accurate and relevant responses.
- It integrates multiple AI methodologies to ensure comprehensive data analysis.
- The user-friendly interface makes it easy to navigate and find the information you need.
""")
