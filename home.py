import streamlit as st 
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

def dashboard():
   st.title("This is dashblsddhlkshlgkoard")

   df = pd.DataFrame(
      np.random.randn(50, 20), 
      columns=('col %d' % i for i in range(20)))

   st.dataframe(df)  # Same as st.write(df)