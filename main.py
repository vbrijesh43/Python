import streamlit as st
import pandas as pd

# Load the Excel file
df = pd.read_excel("pending.xlsx")

st.title("Pending Collection Report")

# Show raw data
st.subheader("Raw Data")
st.dataframe(df)

# Summary statistics
st.subheader("Summary")
st.write("Total Pending Amount:", df["TOTAL AMOUNT"].sum())
st.write("Average Pending Amount:", df["TOTAL AMOUNT"].mean())
st.write("Total Pending Amount by Month-Year:", df.groupby("PENDING MONTHS-YEAR")["TOTAL AMOUNT"].sum().reset_index())

st.write("Total Pending Amount by floor:", df.groupby("FLOOR")["TOTAL AMOUNT"].sum().reset_index())


# Pending by Room
st.subheader("Pending Amount by Room")
room_pending = df.groupby("ROOM NUMBER")["TOTAL AMOUNT"].sum().reset_index()
st.bar_chart(room_pending.set_index("ROOM NUMBER"))

# Pending by Year/Month
st.subheader("Pending by Till Month-Year")
month_pending = df.groupby("TILL MONTH-YEAR")["TOTAL AMOUNT"].sum().reset_index()
st.line_chart(month_pending.set_index("TILL MONTH-YEAR"))

# Concession analysis
st.subheader("Concession vs Pending")
concession = df.groupby("ROOM NUMBER")[["TOTAL AMOUNT","CONCESSION AMOUNT"]].sum().reset_index()
st.bar_chart(concession.set_index("ROOM NUMBER"))

# Monthly collection trend
st.subheader("Monthly Collection Trend")
monthly_cols = [col for col in df.columns if "month collection" in col.lower()]
monthly_data = df[monthly_cols].sum().reset_index()
monthly_data.columns = ["Month", "Collection"]
st.line_chart(monthly_data.set_index("Month"))