import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px
import numpy as np
from bio import biopage
from exploratory import explore
from intro import intro
from eda import home_price, employment_dist, rooms

# Setup the page: 
st.set_option('deprecation.showPyplotGlobalUse', False)
tab1, tab2, tab3, tab4, tab5 = st.tabs(
   ["Introduction", "Bio", "Data", "EDA-Part1", "EDA-Part2"]
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

