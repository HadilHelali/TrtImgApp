from functions.opMorphfn import *
from functions.communfn import *
import streamlit as st

st.title('Opérations Morphologiques')

img1,img2 = st.columns(2)
with img1 :
    st.subheader("Image binaire originale")
    imgb, lg, cl = readImageBinary('images/chat.txt')
    st.pyplot(showImageBinary(imgb))

op = st.selectbox(
        'Choisir une operation ',
        ('Erosion', 'Dilatation','Ouverture','Fermeture'))
btn = showBtn("Opérer")

if (op == 'Erosion'):
    imgb21, lg2, cl2 = readImageBinary('images/chat.txt')
    imgb22 = Erosion(imgb21)

if (op == 'Dilatation'):
    imgb21, lg2, cl2 = readImageBinary('images/chat.txt')
    imgb22 = dilatation(imgb21)

if (op == 'Ouverture'):
    imgb21, lg2, cl2 = readImageBinary('images/chat.txt')
    imgb22 = Ouverture(imgb21)

if (op == 'Fermeture'):
    imgb21, lg2, cl2 = readImageBinary('images/chat.txt')
    imgb22 = Fermeture(imgb21)
if (btn):
    with img2 :
        st.subheader("Image après "+op)
        st.pyplot(showImageBinary(imgb22))
