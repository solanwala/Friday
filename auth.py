import streamlit as st
import json
from streamlit_option_menu import option_menu
from home import dashboard

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
                st.write("You are Registered Sucessfully")
            else:
                "Password do not match"


def test():
    value = st.text_input("Value")
    with open("data.txt", "w") as file:
        file.write(value)

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
