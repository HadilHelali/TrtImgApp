from functions.communfn import *
from functions.filtragefn import *

st.title('Filtrage')
RemoveIndex()

img1,img2 = st.columns(2)
with img1 :
    st.subheader("Image Bruitée")
    # TODO : image bruitée
    dim = {'lx': 0, 'ly': 0}
    mat = lireImagePgm("images/chat.pgm", dim)
    mat1 = genrerBruit(mat)
    ecrireImagePgm("images/generated/ImageBruit.pgm",
                   mat, dim['lx'], dim['ly'], 255)
    st.pyplot(showImage('images/generated/ImageBruit.pgm'))

matF = lireImagePgm('images/chat.pgm', dim)
col6, col7 = st.columns([1,1])
with col6 :
    type = st.selectbox(
        'Choisir un type de filtre',
        ('Moyenneur', 'Mediane','Passe Haut'))

with col7:
    taille = int(st.number_input('taille du filtre',min_value=1))

if (type == 'Moyenneur'):
    matF = filtreMoyenneur(mat, matF,dim,taille)

if (type == 'Mediane') :
    filreMediane(mat1, matF, dim, taille)

if (type == 'Passe Haut') :
    filtreDerivatif(mat, matF, dim, taille)

btn = showBtn("Filtrer")
if (btn):
    with img2 :
        ecrireImagePgm("images/generated/ImageF.pgm", matF, dim['lx'], dim['ly'], 255)
        st.subheader("Image Filtrée")
        st.pyplot(showImage('images/generated/ImageF.pgm'))

    st.table(
            [["coefficient SNR ", snr(mat ,dim, matF)]] )