import streamlit as st
from communfn import *
from egalisationfn import *

st.title('Egalisation')
RemoveIndex()

img1,img2 = st.columns(2)
with img1 :
    st.subheader("Image originale")
    # lecture de l'image :
    dim = {'lx': 0, 'ly': 0}
    mat = lireImagePgm('images/chat.pgm', dim)
    st.pyplot(showImage('images/chat.pgm'))

btn = showBtn("Egaliser")
if (btn):
    with img2 :
        moy = moyenne(mat, dim)
        et = ecartType(mat, dim)
        h = histogramme(mat)
        hc = histogramCumule(h)
        heg = histogramegalise(h, calculn1(probCumule(hc, dim)))
        img = mpimg.imread('images/chat.pgm')
        m1 = createNewMatrice(img,mat,dim,calculn1(probCumule(hc, dim)))
        ecrireImagePgm('images/generated/newImage.pgm',m1,dim['lx'],dim['ly'], 255)
        st.subheader("Image égalisée")
        st.pyplot(showImage('images/generated/newImage.pgm'))

    with st.expander("Visualisation des histogrammes"):
        st.table(
            [["moyenne", moy],
             ["écart type", et]]
        )
        visualisationHistog("Histogramme",h)
        visualisationHistog("Histogramme cumulé",hc)
        visualisationHistog("Histogramme égalisé", heg)