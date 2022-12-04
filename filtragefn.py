import matplotlib.image as mpimg
import streamlit as st
import random
import math
import statistics
from egalisationfn import moyenne

# --------- Bruiter une image ------------
def genrerBruit(mat):
    for i in range(0,int(len(mat))):
        for j in range(0,int(len(mat[i]))):
            alea = random.randint(0,20)
            if alea == 0 :
                mat[i][j] = 0
            elif alea == 20 :
                mat[i][j] = 255
    return mat

# --------- Filtre Moyenneur ------------
def filtreMoyenneur(Oma1, Sma2, dI1, n):
    v = int(n / 2)
    for i in range(0, dI1['ly']):
        for j in range(0, dI1['lx']):
            s = 0
            for k in range(i - v, i + v + 1):
                for l in range(j - v, j + v + 1):
                    if (k in range(0, dI1['ly'])) & (l in range(0, dI1['lx'])):
                        s += Oma1[k][l]
            Sma2[i][j] = int((s / (n * n)))
    return Sma2

# --------- Filtre Mediane ------------
def filreMediane(matI, matFin, dimI, n):
    a = [0] * (n * n)
    v = int(n / 2)
    pos = int((n * n) / 2) - 1
    for i in range(0, dimI['ly']):
        for j in range(0, dimI['lx']):
            h = 0
            for k in range(i - v, i + v + 1):
                for l in range(j - v, j + v + 1):
                    if (k in range(0, dimI['ly'])) & (l in range(0, dimI['lx'])):
                        a[h] = matI[k][l]
                        h = h + 1
            matFin[i][j] = statistics.median(a)
    return matFin

# ---------- Filtre Passe Haut -----------
def filtreDerivatif(Omat ,matFMT, d , n):
    f = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    v = int(n / 2)
    s = 0
    for i in range(0, d['ly']):
        for j in range(0, d['lx']):
            s=0
            for k in range(i-v, i+v+1):
                for l in range(j-v, j+v+1):
                    if (k in range(0, d['ly'])) & (l in range(0, d['lx'])):
                        s += Omat[k][l] * f[i-k][j-l]
            if(s< 0 ):
                matFMT[i][j] = 0
            elif(s>255):
                matFMT[i][j] = 255
            else:
                matFMT[i][j] = int((s /(n*n)))

# -------------- SNR ----------------
def snr(matr1 ,d1, matr2):
    S=0
    B=0
    u1 = moyenne(matr1,d1)
    for ligne in matr1:
        for j in ligne:
            S += ((j - u1)**2)
    for i in range(0, d1['ly']):
        for j in range(0, d1['lx']):
            B += ((matr2[i][j] - matr1[i][j])**2)
    result = math.sqrt(S/B)
    return result
