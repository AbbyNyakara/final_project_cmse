import streamlit as st
from bio import biopage
from exploratory import explore
from intro import intro
from eda import home_price, employment_dist, rooms
from eda2 import dist_pol, income_popl, rooms_value
from analysis import river_homes, available_budget
from predict import estimate
from model import model

# Setup the page: 
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout='wide', 
                   initial_sidebar_state='expanded',
                   page_icon="🏠"
                   )

with st.sidebar:

    tab_selected = st.radio("Navigation", ["Intro", "Bio", "Data", "EDA-Part1", "EDA-Part2", "Interactive Analysis", "Model Training", "Estimate"])

# Display content based on selected tab
if tab_selected == "Intro":
    intro()
elif tab_selected == "Bio":
    biopage()
elif tab_selected == "Data":
    explore()
elif tab_selected == "EDA-Part1":
    home_price()
    st.pyplot(rooms())
    st.pyplot(rooms_value())
    employment_dist()
elif tab_selected == "EDA-Part2":
    st.pyplot(dist_pol())
    st.pyplot(income_popl())
    
elif tab_selected == "Interactive Analysis":
    river_homes()
    available_budget()
elif tab_selected == "Model Training":
    model()
elif tab_selected == "Estimate":
    estimate()
