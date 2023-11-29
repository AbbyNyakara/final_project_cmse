import streamlit as st
from PIL import Image, ImageOps

image1 = Image.open('img2.jpg')
image2 = Image.open('img1.jpg')
image1 = ImageOps.exif_transpose(image1)
image2 = ImageOps.exif_transpose(image2)


def biopage():
    st.subheader("But first before we dive in.. Nice to meet you! I'm Abby!")
    col1, col2 = st.columns(2)
    with col1:
        st.image(image1, caption='Back before winter hit')

    with col2:
        st.image(image2, caption='My orchestra days')
    st.markdown(
        '''
        **About Me**

        I am a budding data scientist eager to explore the world of data science.
        I enjoy turning raw data into meaningful insights in a fun and easy-to-understand way.

        **Skills**:

        Programming Languages: JavaScript, Ruby, Python, R

        Data Manipulation: Pandas, NumPy

        Visualization: Matplotlib, Seaborn, Plotly, Altair

        Machine Learning: Scikit-Learn, Deep learning

        Database: SQL

        Version Control: Git
        
        **Hobbies**

        In my spare time, You'll find me playing my violin or listening to classical music, or ziplining 
        in a forest in the middle of nowhere. Nature speaks to my soul. 
        '''
    )

    
    
    