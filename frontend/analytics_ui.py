import streamlit as st
from datetime import datetime
import requests
import pandas as pd

api_url = "http://localhost:8000"

def analytics_ui_tab():
     
     col1 , col2 = st.columns(2)

     with col1:
        start_date = st.date_input("Start Date: " , datetime(2024,8,1) , key = "start_date")
     with col2:   
        end_date = st.date_input("End Date: " , datetime(2024,8,5) ,key = "end_date")
        
     if st.button("Get Analytics"):

         payload = {
             "start_date" : start_date.strftime("%Y-%m-%d") ,
             "end_date" : end_date.strftime("%Y-%m-%d") 
         }

         response = requests.post(f"{api_url}/analytics" , json = payload).json()

         data = {
             "Category" : list(response.keys()) , 
             "Total" : [response[category]["total"] for category in response] ,
             "Percentage" : [response[category]["percentage"] for category in response] 
         }

         df = pd.DataFrame(data)
         df = df.sort_values(by = "Percentage" , ascending = False)

         st.title("Expense Breakdown By Category")

         st.bar_chart(data = df.set_index("Category")['Percentage'])

         st.table(df)
        




