import streamlit as st
from PIL import Image, ImageOps

image2 = Image.open('img2.jpg')
image2 = ImageOps.exif_transpose(image2)

def biopage():
    st.subheader("Bio Page")
    col1, col2 = st.columns(2)
    with col1:
        st.image(image2)
    with col2:
        
        st.markdown(
            '''
            **About Me 🤔**

            Currently, I'm a data science student at Michigan State University, enthusiastic about unraveling the intricacies of the data science world.

            **Skills 💡**:

            - **Programming Languages:** JavaScript, Ruby, Python, R

            - **Data Manipulation:** Pandas, NumPy

            - **Visualization:** Matplotlib, Seaborn, Plotly, Altair

            - **Machine Learning:** Scikit-Learn, Deep learning

            - **Database:** SQL

            - **Version Control:** Git

            **Contacts 📧**

            Feel free to reach out to me at mogusuab@msu.edu

            **Hobbies 🎻**

            In my spare time, you'll find me lost in the enchanting melodies of my violin or immersed in the world of classical music. If not, I might be ziplining through a forest in the middle of nowhere. Nature speaks to my soul, and I find solace in its beauty.
            '''
        )
  