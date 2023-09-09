import streamlit as st 
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu


def loadfile():
    with open("database/data.json") as file:
        data = json.load(file)
        return data

def save_reminder(newrem):
   data =  loadfile()
   allrem = data["reminders"]
   allrem.append(newrem)
   with open("data.json", "w") as f:
      json.dump(data,f, indent=3)
      







def create_rem():
   st.title("Create New Reminder")
   reminder = st.text_input("What you want to remined")
   date = st.date_input("Select a date")
   time= st.time_input("Select a time slot") 
   new_reminder = {"reminder": reminder,
                    "date": date,
                      "time": time
                      }
   save_reminder(new_reminder)
   


def view_rem():
   st.title("All Reminders")

def chatting():
   st.title("Chatbot")

def dashboard():

   with st.sidebar:
      selected = option_menu(None, ["Create Reminder", "View Reminders", "Chat", "Logout"], icons = ["📝", "📋", "💬", "🔓"] )

   if selected == "Create Reminder":
      create_rem()
   elif selected == "View Reminders":
      view_rem()
   elif selected == "Chat":
      chatting()
   elif selected == "Logout":
      st.session_state["users"] == "Guest"
      st.experimental_rerun()
   else:
      st.write("No option selected")