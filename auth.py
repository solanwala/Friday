import streamlit as st
import json
import pandas as pd
from streamlit_option_menu import option_menu
from home import dashboard
import pymongo

uri = st.secrets["MONGO_CONNECTION_STRING"]

client = pymongo.MongoClient(uri, ssl=False, tls=False)

db = client["myapp"]

col = db["users"]

if "users" not in st.session_state:
    st.session_state["users"] = "Guest"


def loadfile():
    with open("database/data.json") as file:
        data = json.load(file)
        return data

def savefile(newuser):
    data = loadfile()
    usrdata = data['users']
    usrdata.append(newuser)
    with open("database/data.json", "w") as f: 
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
                col.insert_one(newuser)
                st.write("You are Registered Sucessfully")
            else:
                "Password do not match"


def test():
    values = {
        "one": "jslkjgs",
        "two": "ssgs"    }
    data = "https://drive.google.com/file/d/1lsxPqJAZyrr_T1gtiamgwrKDIHg4rO6Z/view?usp=drive_link"
    with open(data) as f:
        dtta = json.load(f)
    dtta.append(values)
    with open(data, "w") as file:
        file.write(json.dumps(dtta,file, indent=4))
    

def Login():
    username = st.text_input("username")
    password = st.text_input("Password")
    
    data = loadfile()
    alluser = data["users"]
    if st.button("Login"):
        for everyusr in alluser:
            if  username == everyusr["username"] and password == everyusr["password"]:
                st.session_state["users"] = "User"
                st.success("Logged in as {}".format(username))
                st.experimental_rerun()
            else:
                st.error("Your username or password do not match")

def main():
    
    if st.session_state["users"] == "Guest":
        with st.sidebar:
            selected = option_menu("Menu", ["Login", "Signup", "testing"], icons = ["house", "person"])
        if selected == "Login":
            Login()

        elif selected == "Signup":
            Signup()
        elif selected == "testing":
            test()
    elif st.session_state["users"] == "User":
        dashboard()

main()
