import streamlit as st
import pandas as pd

st.write("""
    # GCR Facilitator Student Progress Report:
""")
df = pd.read_csv('Progress.csv')
tickerSymbol = st.text_input("Enter Your Name: ")
st.write('Your Progress Report: ', tickerSymbol)

if tickerSymbol:
    df = df[df['Student Name'] == tickerSymbol]
    st.write(df)
else:
    st.write('')
