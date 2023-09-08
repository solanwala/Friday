import streamlit as st
import json
from streamlit_option_menu import option_menu

def loadfile():
    with open("data.json") as file:
        data = json.load(file)
        return data

def savefile(newuser):
    data = loadfile()
    data['reminders'].append(newuser)
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def Signup():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confpass = st.text_input("Confirm Password", type="password")
    
    newuser = {
        "username": username,"password": password
    }
    if st.button("Signup"):
            if password == confpass:
                savefile(newuser)
        
            st.write("You are Registered Sucessfully")
    else:
     st.error("Try again")

    

def Login():
    username = st.text_input("username")
    password = st.text_input("Password")
    
    if st.button("Login"):
    
        if  username == "Username" and password == "password":
            st.sucess("You are logged in")
        else:
            st.error("Your username or password do not match")

def main():
    with st.sidebar:
        selected = option_menu("Menu", ["Login", "Signup"], icons = ["house", "person"])
    if selected == "Login":
        Login()

    elif selected == "Signup":
        Signup()

main()

        
