import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import streamlit as st

# --------- Remove Index ------------
def RemoveIndex():
    # CSS to inject contained in a string
    hide_table_row_index = """
                <style>
                thead tr:first-child {display:none}
                tbody th {display:none}
                </style>
                """

    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

# --------- Afficher une image ------------
def showImage(imgname):
    img = mpimg.imread(imgname)
    imgplot = plt.imshow(img, cmap='gray')
    plt.show()
    return plt

# --------- Afficher bouton ------------
def showBtn(label):
    col1, col2, col3,col4 = st.columns([1,1,1,1.5])
    with col3 :
        btn = st.button(label)
    return btn

# --------- ecriture d'une image ------------

def ecrireImagePgm(name, mat, lx, ly, ng):
    f = open(name, 'w')
    s = "P2 \n#This is a PGM image\n" + str(lx) + " " + str(ly) + "\n" + str(ng) + "\n"
    for i in mat:
        for j in i:
            s += str(j) + " "
        s += "\n"
    f.write(s)
    f.close()

# --------- Lecture d'une image ------------

def lireImagePgm(name, dim):
    f = open(name, 'r')
    i = 0
    j = 0
    mati1 = []
    for line in f:
        i += 1
        if (i == 3):
            x, y = line.split(" ")
            dim['lx'] = int(x)
            dim['ly'] = int(y)
            mat = [[0 for _ in range(dim['lx'])]] * dim['ly']

        if (i > 4):
            mati = line.split(" ")
            matiLast = mati[len(mati) - 1].split("\n")
            mati[len(mati) - 1] = matiLast[0]
            if ('' in mati):
                mati = mati.remove('')
            if mati is not None:
                mati1 = list(map(int, mati))
            mat[j] = mati1
            j += 1
    f.close()
    return (mat)