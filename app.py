import streamlit as st
import pandas as pd
from procedures import *
from io import StringIO

st.markdown("""<style>
    div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
    border-radius: 0.75rem;
    }
    div.stButton > button:hover {
    background-color: #00ff00;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)


st.title("Domain and Linkedin Finder")
st.markdown("## Upload your File in CSV Format")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    data1=pd.read_csv(uploaded_file)
    a=st.button('Domain finder')
    b= st.button('Linkedin finder')
    if a:
        s=extract_domain(data1)
        csv_file = StringIO(s.to_csv(index=False), newline='')
        data = csv_file.getvalue().encode()
        st.download_button(
            label="Download your file",
            data=data,
            file_name="Website_urls.csv",
            mime="text/csv")
        
    if b:
        s2=extract_linkedin(data1)
        csv_file1 = StringIO(s2.to_csv(index=False), newline='')
        data2 = csv_file1.getvalue().encode()
        st.download_button(
            label="Download your file",
            data=data2,
            file_name="Linkedin_urls.csv",
            mime="text/csv")
        


