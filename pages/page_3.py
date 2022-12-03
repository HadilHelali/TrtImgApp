import streamlit as st
from commun import *

st.title('Filtrage')

img1,img2 = st.columns(2)
with img1 :
    st.subheader("Image Bruitée")
    # TODO : image bruitée
    st.pyplot(showImage('images/chat.pgm'))


col6, col7 = st.columns([1,1])
with col6 :
    type = st.selectbox(
        'Choisir un type de filtre',
        ('Moyen', 'Médian','Passe haut'))
if (type == 'Moyen') :
    with col7:
        taille = st.number_input('taille du filtre')
col1, col2, col3,col4 = st.columns([1,1,1,1.5])
with col3 :
    btn = st.button("Filtrer",
              # on_click=
              # TODO : Fonction de filtrage
              )
if (btn):
    with img2 :
        st.subheader("Image Filtrée")
        st.pyplot(showImage('images/chat.pgm'))