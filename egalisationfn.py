import math
import streamlit as st

# --------- calcul de Moyenne ------------
from matplotlib import pyplot as plt


def moyenne(mat, dim):
    sum = 0
    for i in mat:
        for j in i:
            sum += j
    m = (1 / (dim['lx'] * dim['ly'])) * sum
    return m

# --------- calcul de l'Ecart Type ------------

def ecartType(mat, dim):
    sum = 0
    moy = moyenne(mat, dim)
    for i in mat:
        for j in i:
            sum += ((j - moy) ** 2)

    ecart = math.sqrt((1 / (dim['lx'] * dim['ly'])) * sum)
    return ecart

# --------- calcul de l'histogramme ------------

def histogramme(mat):
    h = [0] * (256)
    for i in range(0, 256):
        h[i] = 0

    for i in mat:
        for j in i:
            h[j] += 1
    return h

# ------ calcul de l'histogramme cumule ---------

def histogramCumule(h):
    hc = [0] * (256)
    hc[0] = 0
    for i in range(1, 256):
        for j in range(1, i + 1):
            hc[i] += h[j]
    return hc

#------ calcul de la probabilité Cumulée --------

def probCumule(hist, dim):
    Pc = [0] * (256)
    for i in range(0, 256):
        Pc[i] = 0

    for i in range(0, 256):
        Pc[i] = hist[i] / (dim['lx'] * dim['ly'])
    return Pc

#------ calcul de n1 ------

def calculn1(Pc):
    n1 = [0] * (256)
    for i in range(0, 256):
        n1[i] = 0

    for i in range(0, 256):
        n1[i] = int(255 * Pc[i])
    return n1

#------ calcul de l'histogramme égalisé ------
def histogramegalise(hist, n1):
    heg = [0] * (256)
    for i in range(0, 256):
        heg[i] = 0
    for i in range(0, 256):
        heg[n1[i]] += hist[i]
    return heg


# ---- creer une nouvelle matrice a partir de l'histogramme egalisé ----
def createNewMatrice(image, matNM, dNM, n1):
    lx = image.shape[0]
    ly = image.shape[1]
    for i in range(0, lx):
        for j in range(0, ly):
            matNM[i][j] = n1[image[i, j]]

    return matNM

# -------- visualisation de l'histogramme ------------------
def visualisationHistog(title, h):
    st.subheader(title)
    st.line_chart(data=h)