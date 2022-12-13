import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import streamlit as st

color = {'rouge' : 0,'vert' : 1,'bleu' : 2 }
colorEn = {'rouge' : "red",'vert' : "green",'bleu' : "blue" }

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

# --------- retourner la couleur ------------
def colorFromIdx(i):
    return list({j for j in color if color[j]==i})[0]

# --------- retourner la couleur en anglais ------------
def colorFromIdxEn(i):
    return colorEn.get(list({j for j in color if color[j]==i})[0])

# --------- Afficher une image pgm ------------
def showImage(imgname):
    img = mpimg.imread(imgname)
    imgplot = plt.imshow(img, cmap='gray')
    plt.show()
    return plt

# --------- Afficher une image ppm ------------
def showImagePpm(imgname):
    imgPpm = mpimg.imread(imgname)
    imgplot = plt.imshow(imgPpm)
    plt.show()
    return plt

# --------- Afficher bouton ------------
def showBtn(label):
    col1, col2, col3,col4 = st.columns([1,1,1,1.5])
    with col3 :
        btn = st.button(label)
    return btn

# --------- ecriture d'une image pgm ------------

def ecrireImagePgm(name, mat, lx, ly, ng):
    f = open(name, 'w')
    s = "P2 \n#This is a PGM image\n" + str(lx) + " " + str(ly) + "\n" + str(ng) + "\n"
    for i in mat:
        for j in i:
            s += str(j) + " "
        s += "\n"
    f.write(s)
    f.close()

# --------- Lecture d'une image pgm ------------

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

# --------- lecture d'une image ppm ------------

def readImagePpm(filename):
    with open(filename, 'r') as f:
        file_lines = f.readlines()
    f.close()
    words = file_lines[2].split()
    columns = int(words[0])
    lines = int(words[1])
    print("type image", file_lines[0])
    print("comment image", file_lines[1])
    print("columns image", columns)
    print("lines image", lines)
    print("max value image", file_lines[3])
    array_values = []
    for i in range(4, len(file_lines)):
        values = file_lines[i].split()
        array_values = array_values + values

    array_values = [int(i) for i in array_values]

    matrix = [tuple(array_values[i:i + 3]) for i in range(0, len(array_values), 3)]

    return matrix , lines , columns

# --------- écriture d'une image ppm ------------
def writeImagePpm(img, filename,ligs,cols, maxVal=255, magicNum='P3'):
    image = open(filename + ".ppm", 'w')
    file = open(filename + ".txt", "w+")
    content = str(img)
    file.write(content)
    file.close()
    image.write(magicNum + '\n')
    image.write(str(cols) + ' ' + str(ligs) + '\n')
    image.write(str(maxVal) + '\n')
    j = 0
    for i in range(len(img)):
        if (j == cols-1):
            image.write(str(img[i][0]) + ' '+str(img[i][1]) + ' '+str(img[i][2]))
        else :
            image.write(str(img[i][0]) + ' '+str(img[i][1]) + ' '+str(img[i][2]) + ' ')
        j = j + 1
        if (j == cols):
            image.write('\n')
            j = 0
    image.close()