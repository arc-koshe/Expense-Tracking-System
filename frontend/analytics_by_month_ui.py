import streamlit as st
from datetime import datetime
import requests
import pandas as pd

api_url = "http://localhost:8000"

def analytics_by_month_ui_tab():

    st.title("Expense Breakdown by Month")

    response = requests.get(f"{api_url}/analytics_by_month").json()
    response = {item['month'] : item['total'] for item in response}

    st.bar_chart(response)

    st.table(response)
    

    #st.bar_chart(data = df.set_index("Category")['Percentage'])