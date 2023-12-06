import streamlit as st
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
# tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
#    ["Introduction", "Bio", "Data", "EDA-Part1", "EDA-Part2", "Interactive Analysis", "Estimate"]
#    )

# Create tabs in the sidebar
with st.sidebar:
    st.title("Navigation")
    tab_selected = st.radio("Select Tab", ["Intro", "Biopage", "Data", "EDA-Part1", "EDA-Part2", "Interactive Analysis", "Estimate"])

# Display content based on selected tab
if tab_selected == "Intro":
    intro()
elif tab_selected == "Biopage":
    biopage()
elif tab_selected == "Data":
    explore()
elif tab_selected == "EDA-Part1":
    home_price()
    st.pyplot(rooms())
    employment_dist()
elif tab_selected == "EDA-Part2":
    st.pyplot(dist_pol())
    st.pyplot(income_popl())
    st.pyplot(rooms_value())
elif tab_selected == "Interactive Analysis":
    river_homes()
    available_budget()
elif tab_selected == "Estimate":
    estimate()
