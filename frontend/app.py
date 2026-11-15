import streamlit as st
from add_update_ui import add_update_ui_tab
from analytics_ui import analytics_ui_tab
from analytics_by_month_ui import analytics_by_month_ui_tab


st.title("Expense Tracking System")

tab1 , tab2 , tab3 = st.tabs(["Add/Update" , "Analytics by Category" , "Analytics by Month"])

# Add/Update tab :
with tab1:
     add_update_ui_tab()

# Analytics by Category tab :
with tab2:
     analytics_ui_tab()

# Analytics by Month tab :
with tab3:
     analytics_by_month_ui_tab()