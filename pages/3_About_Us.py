import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About this App")
st.markdown('<p style="color:red;">For your info, I used crewai for 2.1 HDB resale application but it seems that Streamlit is unable to support it. Hence, I recreated 2.2 HDB resale application using non-crewai method. For your review please.</p>', unsafe_allow_html=True)
st.write("This is a Streamlit App built by HDB that demonstrates how to use the OpenAI API to generate text completions to answer your queries related to HDB resale flats.")

with st.expander("How to use this App"):
    st.write("1. S/N 2 to 4 is relevant to the main page and HDB resale application procedure page.")
    st.write("2. Enter your prompt in the text area.")
    st.write("3. Click the 'Submit' button.")
    st.write("4. The app will generate a text completion based on your prompt.")
    st.write("5. For the View All HDB resale wef 2017 page, you can scroll around to find the HDB resale that you are looking for.")