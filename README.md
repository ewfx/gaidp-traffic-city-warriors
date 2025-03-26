# 🚀 Project Name

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
Data Profiling Application built using Streamlit and Python. Here's a breakdown of its key components and functionalities:

**Core Functionality:**

- 🔹**Data Upload:**
The left sidebar provides a file uploader (st.file_uploader) that allows users to upload CSV files.
This is the primary way for users to input their datasets for analysis.
- 🔹**Data Display:**
The code snippet df = pd.DataFrame(data) indicates that the application uses the pandas library to handle tabular data.
The uploaded CSV data is likely also loaded into a pandas DataFrame.
It is then highly likely that the dataframes are displayed using the st.write() command.
- 🔹**Data Analysis:**
The "Regulatory Reporting Instruction" text area suggests that the application performs some form of data analysis or validation based on user-provided instructions.
The hard coded data, and the uploaded csv data, are used together in conjunction with the regulatory reporting instructions.
It is very likely that the bard API is used to process the natural language instructions, and then to compare the data to those instructions.
- 🔹**Regulatory Compliance:**
The instructions provided in the text area are related to regulatory compliance for financial transactions.
This indicates that the application is designed to help users ensure their data meets specific regulatory requirements.
- 🔹**Data Validation:**
The instructions mention checks for:
Transaction amount vs. reported amount.
Account balance (negative values).
ISO 4217 currency codes.
Cross-border transaction limits.
- 🔹**Jurisdiction validation.**
Potential Use of Bard API:
It is very likely that the bard api is used, to process the natural language instructions, and then to compare the data to those instructions.


In essence, this is a Streamlit application designed to:
- 🔹Enable users to upload their financial data in CSV format.
- 🔹Allow users to input regulatory reporting instructions in natural language.
- 🔹Analyze the data against the instructions.
- 🔹Display the analysis results in a user-friendly web interface.
- 🔹This type of application could be very useful for financial analysts, compliance officers, and anyone who needs to ensure their data meets regulatory requirements.

## 🎥 Demo
🔗 [Live/ Demo](https://github.com/ewfx/gaidp-traffic-city-warriors/blob/main/artifacts/demo/Data%20Profiling%20Application%20Video.mp4) (Applicable)  
- https://github.com/ewfx/gaidp-traffic-city-warriors/blob/main/artifacts/demo/Data%20Profiling%20Application%20Video.mp4
  
📹 [Video Demo](https://github.com/ewfx/gaidp-traffic-city-warriors/blob/main/artifacts/demo/Data%20Profiling%20Application%20Video.mp4) (Same as above )
- https://github.com/ewfx/gaidp-traffic-city-warriors/blob/main/artifacts/demo/Data%20Profiling%20Application%20Video.mp4
  
🖼️ Screenshots:
- https://github.com/ewfx/gaidp-traffic-city-warriors/blob/main/artifacts/arch/Data%20Profiling%20Application.pptx

🖼️ Data Flow Diagram :
- https://github.com/ewfx/gaidp-traffic-city-warriors/blob/main/artifacts/arch/Architecture%20or%20DataFlow%20Diagram.docx


## 💡 Inspiration
- 🔹 Leverage the power of Python and NLP to improve efficiency and accuracy.

## ⚙️ What It Does
- 🔹Enable users to upload their financial data in CSV format.
- 🔹Allow users to input regulatory reporting instructions in natural language.
- 🔹Analyze the data against the instructions.
- 🔹Display the analysis results in a user-friendly web interface.
- 🔹This type of application could be very useful for financial analysts, compliance officers, and anyone who needs to ensure their data meets regulatory requirements.

## 🛠️ How We Built It
**Technical Details:**
- 🔹**Streamlit:**
The application is built using Streamlit, a Python framework for creating web applications.
Streamlit makes it easy to create interactive web interfaces for data science and machine learning.
- 🔹**Pandas:**
The pandas library is used for data manipulation and analysis, particularly for working with DataFrames.
- 🔹**Python:**
Python is the programming language used to build the application.
- 🔹**User Interface:**
The application has a user-friendly web interface with a sidebar for input and a main area for output.
- 🔹**Localhost:**
The application is running on localhost:8501, indicating it's being run locally on the user's machine.

## 🚧 Challenges We Faced
- 🔹Contextual Understanding
- 🔹Environment Setup

## 🏃 How to Run
Refer :** https://github.com/ewfx/gaidp-traffic-city-warriors/blob/main/artifacts/arch/How%20to%20run%20the%20code.docx**
1. Clone the repository  
   ```sh
   git clone https://github.com/ewfx/gaidp-traffic-city-warriors/tree/main/code/src
   Open DataProfiling Project in PyCharm
   ```
2. Install dependencies  
   ```sh
   Open Terminal and run pip install -r requirements.txt

   Create Virtual Environment & Install Requirement (Refer - https://github.com/ewfx/gaidp-traffic-city-warriors/blob/main/artifacts/arch/How%20to%20run%20the%20code.docx)
   Note : It will take approx. 5 mins

   ```
3. Run the project  
   ```sh
   Close the Terminal Select .venv using mouse then Open Terminal
   Open Terminal in .venv and run streamlit run main.py (Refer - Refer - https://github.com/ewfx/gaidp-traffic-city-warriors/blob/main/artifacts/arch/How%20to%20run%20the%20code.docx)

   Open the URL in Browser
   ```

Application Screen Shot is mentioned in ppt & captured flow in video 
- 🔹Application Screen Shot - https://github.com/ewfx/gaidp-traffic-city-warriors/blob/main/artifacts/arch/Data%20Profiling%20Application.pptx
- 🔹Application Demo Video - https://github.com/ewfx/gaidp-traffic-city-warriors/blob/main/artifacts/demo/Data%20Profiling%20Application%20Video.mp4
  
- 🔹 Data Flow Diagram - https://github.com/ewfx/gaidp-traffic-city-warriors/blob/main/artifacts/arch/Architecture%20or%20DataFlow%20Diagram.docx

## 🏗️ Tech Stack
- 🔹 Python
- 🔹 Streamlit is for visualization and creating interactive webpages
- 🔹 Bard API is a powerful tool that allows developers to access the capabilities of Google’s large language model. Bard to generate text, translate languages, write different kinds of creative content, and answer questions in an informative way.
- 🔹 Pandas is a powerful and popular Python library used for data manipulation and analysis
- 🔹 PyCharm is a popular integrated development environment (IDE) developed by JetBrains, specifically designed for Python development


## 👥 Team
- **Anoop Velappan** - [GitHub](https://github.com/anoop387) | [LinkedIn](https://www.linkedin.com/in/anoop387/)
- **Anoop Thakur** - [GitHub](#) | [LinkedIn](#)
- **Abhishek Gupta** - [GitHub](#) | [LinkedIn](#)
