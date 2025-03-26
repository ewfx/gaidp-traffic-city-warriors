from nbformat import write
from bardapi import Bard
import os
import streamlit as st
import pandas as pd
import numpy as np
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport
from transformers import pipeline

print("Hello, PyCharm!")
st.title("Data Profiling App")
st.subheader("This app will help you to do Data Exploration")
st.sidebar.header("User Input Features")
#File Uploader to upload CSV Dataset (Upload Transaction Details)
uploaded_file = st. sidebar.file_uploader("upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    st .markdown("----")
    #Read Data from CSV File & put into ny_data object
    csv_dataset = pd.read_csv(uploaded_file, index_col=None)

    #Displaying CSV Dataset in UI
    st.subheader("Uploaded CSV File- Sample Dataset")
    st.write(csv_dataset)

    #Setting Bard API Key
    st.subheader("OpenAI Analysis")
    os.environ['_BARD_API_KEY'] = "Your Key"
    api_key = os.environ.get("_BARD_API_KEY")

    #Setting Default Regulatory Instruction to a default_RegInstr_text variable
    default_RegInstr_text = """Transaction Amount should always match Reported Amount, except when the transaction involves cross-currency conversions, in which case a permissible deviation of up to 1% is allowed.
Account Balance should never be negative, except in cases of overdraft accounts explicitly marked with an "OD" flag.
Currency should be a valid ISO 4217 currency code, and the transaction must adhere to cross-border transaction limits as per regulatory guidelines.
Country should be an accepted jurisdiction based on bank regulations, and cross-border transactions should include mandatory transaction remarks if the amount exceeds $10,000.Display Row Level Transaction Details"""

    #Assigning default Regulatory instruction which we set in default_RegInstr_text variable to RegInstr_input_text .
    #RegInstr_input_text can be edited from UI if Required.
    RegInstr_input_text = st.text_area("Regulatory Reporting Instruction",  height=250,value=default_RegInstr_text)

    #Passing Regulatory instruction which we set in RegInstr_input_text variable and CSV Dataset Variable csv_dataset with api key to Bard .
    #we will get the response in answer variable
    answer = Bard(token=api_key).get_answer(f'{RegInstr_input_text} this data {csv_dataset}')['content']

    #Bard API response is displayed in UI
    st.write(f'{answer}')

    #Chatbot - Raise You Question Input field where we put out Question which will get assigned to userQuestion variable
    userQuestion = st.text_area("ChatBot - Raise Your Question")

    # Passing user question which we set in userQuestion variable and CSV Dataset Variable csv_dataset with api key to Bard API.
    #The BARD API response in will assign to userQuestionResponse variable
    if userQuestion:
        userQuestionResponse = Bard(token=api_key).get_answer(f'{userQuestion} this data {csv_dataset}')['content']
        #Bard API response is displayed in UI
        st.write(f'{userQuestionResponse}')
    else:
        st.write("No Input Question")

    #Profile Report of CSV dataset is displayed below
    st.markdown("----")
    st.subheader("Pandas Review")
    profile = ProfileReport(csv_dataset, title="Summary of the Data")
    st_profile_report(profile)

else:
    st. markdown('----')
    st.write("You did not upload a new file")
