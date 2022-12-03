import streamlit as st
import numpy as np
from communfn import *

st.title('Lecture et écriture')
RemoveIndex()

lec, ecr = st.tabs(["Lecture", "Ecriture"])
# -------------- LECTURE ----------------
with lec:
    f = st.file_uploader("Importer une image :",type=(["pgm"]))
    if f is not None:
        path_in = f.name
        print(path_in)
        st.pyplot(showImage('images/'+path_in))
        # lecture de l'image
        dim = {'lx': 0, 'ly': 0}
        mat = lireImagePgm('images/'+path_in, dim)
        with st.expander("Plus d'informations sur l'image"):
            st.table(
                [["taille",f.size],
                ["nombre de lignes",dim['lx']],
                ["nombre de colonnes",dim['ly']],
                ["niveau de gris", 255]]
            )
    else:
        path_in = None

# -------------- ECRITURE ----------------
with ecr:
    name = st.text_input("nom de l'image")
    lx = int(st.number_input("nombre de lignes"))
    ly = int(st.number_input("nombre de colonnes"))
    ng = int(st.number_input("niveau de gris"))
    txt = st.text_area("matrice")
    mat = [[int(j) for j in i.split(' ')] for i in txt.splitlines()]
    btn = showBtn("Ecrire")
    if (btn):
        ecrireImagePgm(name, mat, lx, ly, ng)
        st.pyplot(showImage(name))