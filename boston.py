import streamlit as st
import pandas as pd
import seaborn as sns
import altair as alt
import plotly.express as px
import numpy as np
from bio import biopage
from exploratory import explore
from intro import intro
from eda import home_price, employment_dist, rooms
from eda2 import dist_pol, income_popl, rooms_value
from analysis import river_homes, available_budget
from predict import estimate

# Setup the page: 
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
   ["Introduction", "Bio", "Data", "EDA-Part1", "EDA-Part2", "Interactive Analysis", "Estimate"]
   )

with tab1:
    intro()

with tab2: 
   biopage()

with tab3:
   explore()

with tab4:
   home_price()
   st.pyplot(rooms())
   employment_dist()

with tab5:
   st.pyplot(dist_pol())
   st.pyplot(income_popl())
   st.pyplot(rooms_value())

with tab6:
   river_homes()
   available_budget()

with tab7:
   estimate()
