import streamlit as st
import pandas as pd

st.set_page_config(page_title="Degiro Tools App", layout="wide")

st.title("📈 Degiro Tools App")
st.write("Welcome! This is my first Streamlit app.")

# Example input
ticker = st.text_input("Enter a stock ticker (e.g., AAPL, MSFT)")

# Example button + output
if st.button("Show ticker"):
    if ticker:
        st.success(f"You entered: {ticker}")
    else:
        st.warning("Please enter a ticker first.")

# Example text
st.write("""
# DEGIRO TOOLS APP
Extend your DEGIRO experience with custom tools and features. This app provides various functionalities to analyze and manage your DEGIRO investments effectively. Explore the different sections to get insights into your portfolio, track performance, and make informed decisions.
""")

st.line_chart([1, 2, 3, 4, 5])