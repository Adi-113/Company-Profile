import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
url = "https://www.google.de/search"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}

def extract_domain(data):
    m=[]
    rows=data['company']
    for row in rows:
        company = row 
        params = {"q": company}
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            result = soup.find("div", class_="g")
            if result:
                website_url = result.find("a").get("href")
                n=[company,website_url]
                m.append(n)
            else:
                n=[company,"No Website found"]
                m.append(n)
    df1=pd.DataFrame(m)
    return df1
def extract_linkedin(data):
    m=[]
    rows=data['company']
    for row in rows:
        company = row +"Linkedin"
        params = {"q": company}
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            result = soup.find("div", class_="g")
            if result:
                website_url = result.find("a").get("href")
                n=[company,website_url]
                m.append(n)
            else:
                n=[company,"No Linkedin found"]
                m.append(n)
    df2=pd.DataFrame(m)
    return df2
        
