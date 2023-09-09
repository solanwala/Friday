import streamlit as st 
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

def dashboard():
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