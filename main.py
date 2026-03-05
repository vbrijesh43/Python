
import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(page_title="My Streamlit Website", page_icon="🌐", layout="wide")

# Title
st.title("🌐 My First Streamlit Website")
st.write("Welcome to my website built with Streamlit!")

# Sidebar navigation
menu = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Data Visualization", "Contact"]
)

# Home Page
if menu == "Home":
    st.header("Home Page")
    st.write("This is a simple website created using Streamlit.")

    name = st.text_input("Enter your name")

    if st.button("Submit"):
        st.success(f"Hello {name}, welcome to the website!")

# Data Visualization Page
elif menu == "Data Visualization":
    st.header("Data Visualization")

    data = pd.DataFrame(
        np.random.randn(50, 3),
        columns=["A", "B", "C"]
    )

    st.line_chart(data)
    st.bar_chart(data)

# Contact Page
elif menu == "Contact":
    st.header("Contact Us")

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")

        submit = st.form_submit_button("Send")

        if submit:
            st.success("Message sent successfully!")

