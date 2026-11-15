import streamlit as st
from datetime import datetime
import requests

api_url = "http://localhost:8000"

def add_update_ui_tab():    
    selected_date = st.date_input("Enter a date : ",datetime(2024,8,1) , label_visibility = 'collapsed')
    response = requests.get(f"{api_url}/expenses/{selected_date}")
    if response.status_code == 200 :
        existing_expenses = response.json()

    else:
        st.write("Failed to get expenses")
        existing_expenses = []

    categories = ["Rent" , "Food" , "Shopping" , "Entertainment" , "Other"]

    with st.form(key = "expense_form"):

            header1, header2, header3 = st.columns(3)
            header1.subheader("Amount")
            header2.subheader("Category")
            header3.subheader("Notes")

            expenses = []

            for i in range(5):

                if i < len(existing_expenses):
                     amount = existing_expenses[i]['amount']
                     category = existing_expenses[i]['category']
                     notes = existing_expenses[i]['notes']
                else:
                     amount = 0.0
                     category = "Other"
                     notes = ""

                col1 , col2 , col3 = st.columns(3)
                with col1:
                     amount_input = st.number_input(label = "Amount" , min_value = 0.0 , step = 1.0 , value = amount , key = f"amount_{i}_{selected_date}" , label_visibility = 'collapsed')
                with col2:
                     category_input = st.selectbox(label = "Category" , options = categories , index = categories.index(category), key = f"category_{i}_{selected_date}", label_visibility = 'collapsed')      
                with col3:
                     notes_input = st.text_input(label = "Notes" , value = notes , key = f"notes_{i}_{selected_date}", label_visibility = 'collapsed')

                expenses.append({
                    "amount": amount_input ,
                    "category" : category_input ,
                    "notes" : notes_input
                })         

            submit_button = st.form_submit_button()  
            if submit_button:
                 filtered_expenses = [expense for expense in expenses if expense["amount"] > 0]
                 response = requests.post(f"{api_url}/expenses/{selected_date}" , json = filtered_expenses)
                 if response.status_code == 200:
                      st.write(filtered_expenses)
                      st.success("Expenses updated successfully!")
                 else:
                      st.error("Failed to update expenses.")