from seuillagefn import *

st.title('Seuillage')

img1,img2 = st.columns(2)
with img1 :
    st.subheader("Image originale")
    st.pyplot(showImage("images/peppers.ppm"))
    mt ,lines, columns = readImagePpm("images/peppers.ppm")

# les histogrammes des 3 couleurs :
hcol = histgCouleur(mt)
typeSeuil = st.selectbox(
        'choisir le type de seuil',
        ('seuil median', 'seuil paramétrable','seuil automatique avec OTSU'))

if(typeSeuil == 'seuil median'):
    seuils = [sorted(h)[int(255 / 2)] for h in hcol]
    nvseuils = [hcol[i].index(seuils[i]) for i in range(3)]
    btn = showBtn("Seuiller")
    col7, col8, col9 = st.columns([1, 1, 1])

if (typeSeuil == 'seuil paramétrable'):
    col6, col7,col8,col9 = st.columns([1,1,1,1])
    with col6 :
        nvseuils = [0,0,0]
        for i in range(3):
            nvseuils[i] = st.slider('Choisir un seuil pour la couleur **'+colorFromIdx(i)+'**',
                                  0, 255, 0)
        seuils = [hcol[i][nvseuils[i]] for i in range(3)]
        btn = st.button('Seuiller')

if(typeSeuil == 'seuil automatique avec OTSU'):
    nvseuils = [otsu_thresholding(hcol[0]) for i in range(3)]
    seuils = [hcol[i][nvseuils[i]] for i in range(3)]
    btn = showBtn("Seuiller")
    col7, col8, col9 = st.columns([1, 1, 1])

if (btn):
    visualHigCouleur(hcol,seuils,col7,col8,col9)
    with img2:
        mts = SeuilmatriceCouleur(mt,nvseuils)
        writeImagePpm(mts, 'images/generated/imageSeuillée', lines, columns)
        st.subheader("Image seuillée")
        st.pyplot(showImage("images/generated/imageSeuillée.ppm"))
    # fonction ET
    matETFinal = et(mts,columns)
    ecrireImagePgm("images/generated/ImageSeuilET.pgm", matETFinal, int(columns/3), lines, 255)
    # fonction OU
    matOUFinal = ou(mts, columns)
    ecrireImagePgm("images/generated/ImageSeuilOU.pgm", matOUFinal, int(columns / 3), lines, 255)
    grph1, grph2 = st.columns(2)
    with grph1:
        st.subheader("Image avec fonction ET")
        st.pyplot(showImage("images/generated/ImageSeuilET.pgm"))
    with grph2:
        st.subheader("Image avec fonction OU")
        st.pyplot(showImage("images/generated/ImageSeuilOU.pgm"))