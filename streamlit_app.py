import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
def compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time

def main():
    st.title("Compound Interest Calculator")

    principal = st.number_input("Enter principal amount:")
    rate = st.number_input("Enter annual interest rate:")
    time = st.number_input("Enter time in years:")

    result = compound_interest(principal, rate, time)

    st.write(f"Compound Interest after {time} years: ${result - principal:.2f}")

    # Visualization
    years = np.arange(1, time + 1)
    amounts = principal * (1 + rate / 100) ** years

    st.line_chart(list(zip(years, amounts)))

if __name__ == "__main__":
    main()
