import streamlit as st
from PIL import Image, ImageOps

image1 = Image.open('img1.jpg')
image2 = Image.open('img2.jpg')
image3 = Image.open('img3.jpg')
image1 = ImageOps.exif_transpose(image1)
image2 = ImageOps.exif_transpose(image2)
image3 = ImageOps.exif_transpose(image3)

def biopage():
    st.subheader("About Me:")
    col1, col2 = st.columns(2)
    with col1:
        st.image(image3, caption="Big brother")
        st.image(image1, caption="Orchestra days")
    with col2:
        
        st.markdown(
            '''
            **About Me 🤔**

            It depends on who you ask, really. To some, I am a sister, to others, a talented violinist; to some, just a broke college student.
             
            One thing for sure, I am the developer of this application. Currently, I'm a data science student at Michigan State University, enthusiastic about unraveling the intricacies of the data science world.

            **Skills 💡**:

            - **Programming Languages:** JavaScript, Ruby, Python, R

            - **Data Manipulation:** Pandas, NumPy

            - **Visualization:** Matplotlib, Seaborn, Plotly, Altair

            - **Machine Learning:** Scikit-Learn, Deep learning

            - **Database:** SQL

            - **Version Control:** Git

            **Contacts 📧**

            Feel free to reach out to me at mogusuab@msu.edu. Especially if you are hiring

            **Hobbies 🎻**

            In my spare time, you'll find me lost in the enchanting melodies of my violin or immersed in the world of classical music. If not, I might be ziplining through a forest in the middle of nowhere. Nature speaks to my soul, and I find solace in its beauty.
            '''
        )
  