import streamlit as st
from send_email import send_email
import pandas


st.header("Contact Me")

df = pandas.read_csv("topics.csv")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")

    option = st.selectbox(
        "What topic do you want to discuss?",
        df["topic"])
    raw_message = st.text_area("Text")
    message = f"""
    Subject: New email form {user_email}
    From: {user_email}
    Topic {option}
    {raw_message}
    """



    message = message + "\n" + user_email
    button = st.form_submit_button("Submit")

    if button:
        send_email(message)
        st.info("Your email was sent successfully")
        
