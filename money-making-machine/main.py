# Imports
import streamlit as st
import random 
import time
import requests 

st.title("Money Making Machine")


def generate_money():
    return random.randint(1,100)


st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(5)
    amount = generate_money()
    st.success(f"You have made ${amount}")


def fetch_side_hustle():
    try:
        respone = requests.get("http://127.0.0.1:8000/side_hustles")
        if respone.status_code == 200:
            side_hustle = respone.json()
            return side_hustle["side_hustle"]
        else:
            return "Freelancing"
    except:
        return "something went wrong"

st.subheader("Side Hustle")
if st.button("Get side hustles"):
    idea = fetch_side_hustle()
    st.success(idea)


def fetch_money_quote():
    try:
        respone = requests.get("http://127.0.0.1:8000/money_quotes")
        if respone.status_code == 200:
            money_quote = respone.json()
            return money_quote["money_quotes"]
        else:
            return "Money is the root of all evil"
    except:
        return "something went wrong"

st.subheader("Money-Making Motivation")
if st.button("Get Inspired"):
    quote = fetch_money_quote()
    st.success(quote)



