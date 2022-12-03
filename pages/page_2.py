import streamlit as st
from commun import *

st.title('Egalisation')

img1,img2 = st.columns(2)
with img1 :
    st.subheader("Image originale")
    st.pyplot(showImage('images/chat.pgm'))

col1, col2, col3,col4 = st.columns([1,1,1,1.5])
with col3 :
    btn = st.button("Egaliser",
              # on_click=
              # TODO : Fonction d'égalisation
              )
if (btn):
    with img2 :
        st.subheader("Image égalisée")
        st.pyplot(showImage('images/chat.pgm'))

    with st.expander("Visualisation des histogrammes"):
        st.write("les plots des histogrammes")