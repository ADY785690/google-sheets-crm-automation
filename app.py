import streamlit as st
import pandas as pd

st.title("📋 Google Sheets CRM Automation")

lead_name = st.text_input("Lead Name")
email = st.text_input("Email")
status = st.selectbox(
    "Lead Status",
    ["New", "Contacted", "Qualified", "Closed"]
)

if st.button("Save Lead"):
    st.success("Lead Saved Successfully")

st.subheader("CRM Dashboard")

data = {
    "Lead": ["Rahul", "Priya", "Aman"],
    "Status": ["New", "Qualified", "Closed"]
}

df = pd.DataFrame(data)

st.dataframe(df)

st.bar_chart(df["Status"].value_counts())
