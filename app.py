import streamlit as st
import pandas as pd

st.set_page_config(page_title="Google Sheets CRM Automation")

st.title("📋 Google Sheets CRM Automation")

st.subheader("Add New Lead")

name = st.text_input("Customer Name")
email = st.text_input("Email")

status = st.selectbox(
    "Lead Status",
    ["New", "Contacted", "Qualified", "Closed"]
)

if st.button("Add Lead"):
    st.success(f"{name} added successfully")

st.divider()

st.subheader("CRM Dashboard")

df = pd.DataFrame({
    "Customer":["Rahul","Priya","Amit","Neha"],
    "Status":["New","Qualified","Closed","Contacted"],
    "Revenue":[10000,25000,40000,15000]
})

col1,col2,col3 = st.columns(3)

col1.metric("Total Leads", len(df))
col2.metric("Qualified Leads",
            len(df[df["Status"]=="Qualified"]))
col3.metric("Revenue",
            f"₹{df['Revenue'].sum():,}")

st.dataframe(df)

st.subheader("Lead Status Distribution")

st.bar_chart(df["Status"].value_counts())

st.subheader("Revenue Analysis")

st.bar_chart(
    df.set_index("Customer")["Revenue"]
)

csv = df.to_csv(index=False)

st.download_button(
    "Download Report",
    csv,
    "crm_report.csv",
    "text/csv"
)
