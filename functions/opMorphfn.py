from functions.communfn import *
import cv2
import numpy as np

# ----------------- lecture d'image binaire --------------------------
def readImageBinary(filename):
    # Use a breakpoint in the code line below to debug your script.*
    with open(filename, 'r') as f:
        file_lines = f.readlines()
    f.close()
    values = []
    matrix = []
    for i in range(0, len(file_lines)):
        values = []
        for j in file_lines[i]:
            if (j != '\n'):
                values.append(j)
        ligne = [int(i) for i in values]
        matrix.append(ligne)
    return matrix ,len(matrix) , len(matrix[0])

# --------- Afficher une image binaire ------------
def showImageBinary(img):
    imgplot = plt.imshow(img, cmap='gray')
    plt.show()
    return plt

# --------- Erosion ------------
def Erosion(matOrig):
    matFiltre = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    matR = [[0] * len(matOrig[0])] * len(matOrig)
    for i in range(0, len(matOrig)):
        for j in range(0, len(matOrig[i])):
            matR[i][j] = matOrig[i][j]

    for i in range(0, len(matOrig)):
        for j in range(0, len(matOrig[i])):
            if ((i == 0) | (j == 0) | (i == len(matOrig) - 1) | (j == len(matOrig[i]) - 1)):
                matOrig[i][j] = 0

            elif (matR[i][j] == 1):
                ind1 = i - 1
                ind2 = j - 1
                indV = 0
                val = [1] * (9)

                for l in range(0, len(matFiltre)):
                    for k in range(0, len(matFiltre[l])):
                        if (((matR[ind1 + l][ind2 + k] == 0) & (matFiltre[l][k] == 1))):
                            val[indV] = 0
                            print(val)

                        indV += 1

                if (val.count(0) != 0):
                    matOrig[i][j] = 0
                val = [1] * (9)

    return matOrig

# --------- Dilatation ------------

def dilatation(matOrigD):
    '''
    matFiltreD = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    matR = [[0] * len(matOrigD[0])] * len(matOrigD)

    for i in range(0, len(matOrigD)):
        for j in range(0, len(matOrigD[i])):
            matR[i][j] = matOrigD[i][j]

    for i in range(0, len(matOrigD)):
        for j in range(0, len(matOrigD[i])):
            if (matR[i][j] == 1):
                if (i == 0 & j == 0):
                    ind1 = 0
                    ind2 = 0
                    for l in range(0, 2):
                        for k in range(0, 2):
                            if (((matR[ind1 + l][ind2 + k] == 0) & (matFiltreD[l][k] == 1))):
                                matOrigD[ind1 + l][ind2 + k] = 1
                                print('ok', l, k)
                elif (i == 0 & j < (len(matOrigD[i]) - 1)):
                    ind1 = i
                    ind2 = j - 1
                    for l in range(0, 2):
                        for k in range(0, 3):
                            if (((matR[ind1 + l][ind2 + k] == 0) & (matFiltreD[l][k] == 1))):
                                matOrigD[ind1 + l][ind2 + k] = 1
                elif (i == 0 & j == (len(matOrigD[i]) - 1)):
                    ind1 = i
                    ind2 = j - 1
                    for l in range(0, 2):
                        for k in range(0, 2):
                            if (((matR[ind1 + l][ind2 + k] == 0) & (matFiltreD[l][k] == 1))):
                                matOrigD[ind1 + l][ind2 + k] = 1
                elif (i == len(matOrigD) - 1 & j == 0):
                    ind1 = i - 1
                    ind2 = j
                    for l in range(0, 2):
                        for k in range(0, 2):
                            if (((matR[ind1 + l][ind2 + k] == 0) & (matFiltreD[l][k] == 1))):
                                matOrigD[ind1 + l][ind2 + k] = 1
                elif ((i == len(matOrigD) - 1) & (j < (len(matOrigD[i]) - 1))):
                    ind1 = i - 1
                    ind2 = j - 1
                    for l in range(0, 2):
                        for k in range(0, 3):

                            if (((matR[ind1 + l][ind2 + k] == 0) & (matFiltreD[l][k] == 1))):
                                matOrigD[ind1 + l][ind2 + k] = 1
                elif ((i == len(matOrigD) - 1) & (j == (len(matOrigD[i]) - 1))):
                    ind1 = i - 1
                    ind2 = j - 1
                    for l in range(0, 2):
                        for k in range(0, 2):
                            if (((matR[ind1 + l][ind2 + k] == 0) & (matFiltreD[l][k] == 1))):
                                matOrigD[ind1 + l][ind2 + k] = 1
                elif (i < len(matOrigD) - 1 & j == 0):
                    ind1 = i - 1
                    ind2 = j
                    for l in range(0, 3):
                        for k in range(0, 2):
                            if (((matR[ind1 + l][ind2 + k] == 0) & (matFiltreD[l][k] == 1))):
                                matOrigD[ind1 + l][ind2 + k] = 1
                elif ((i < len(matOrigD) - 1) & (j < (len(matOrigD[i]) - 1))):
                    ind1 = i - 1
                    ind2 = j - 1
                    for l in range(0, 3):
                        for k in range(0, 3):
                            if (((matR[ind1 + l][ind2 + k] == 0) & (matFiltreD[l][k] == 1))):
                                matOrigD[ind1 + l][ind2 + k] = 1
                elif ((i < len(matOrigD) - 1) & (j == (len(matOrigD[i]) - 1))):
                    ind1 = i - 1
                    ind2 = j - 1
                    for l in range(0, 3):
                        for k in range(0, 2):
                            if (((matR[ind1 + l][ind2 + k] == 0) & (matFiltreD[l][k] == 1))):
                                matOrigD[ind1 + l][ind2 + k] = 1

    return matOrigD
    '''
    img_dilation = cv2.dilate(np.array(matOrigD).astype('uint8'),
                                  np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]).astype('uint8'), iterations=1)

    return img_dilation


# --------- Fermeture ------------
def Fermeture(matFermeture):
    mF_Er= dilatation(matFermeture)
    mFer = Erosion(mF_Er)
    return  mFer

# --------- Ouverture ------------
def Ouverture(matOuverture):
    mEr = Erosion(matOuverture)
    mOuv = dilatation(mEr)
    return mOuv