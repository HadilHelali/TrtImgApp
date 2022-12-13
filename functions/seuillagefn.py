import pandas as pd
import numpy as np
from functions.communfn import *

# --------- calcul de l'histogramme d'une image RGB ------------
def histogrammeRGB(matC, car):
    h = [0] * (256)
    for i in range(0, 256):
        h[i] = 0
    for i in range(len(matC)):
        h[matC[i][color.get(car)]] += 1
    return h

# --------- histogrammes des couleurs ------------

def histgCouleur(mat):
    hcol = []
    for i in color.keys():
        hcol.append(histogrammeRGB(mat,i))
    return hcol

# --------- visualization des histogrammes des couleurs ------------
def visualHigCouleur(hgcol,seuils,col7,col8,col9):
    cols = [col7,col8,col9]
    for i in range(3):
        with cols[i]:
            #color=colorFromIdxEn(i)
            st.subheader(colorFromIdx(i))
            df = pd.DataFrame({
                'seuil' : [seuils[i] for j in range(0, 256)],
                'histogramme' : hgcol[i]
            })
            st.line_chart(df)


# --------- seuillage d'une matrice couleur ------------
def SeuilmatriceCouleur(matS,s):
    # Matrice après seuillage :
    mrs = []
    for i in range(0 ,len(matS)):
        tpl = ()
        for j in range(0 ,3):
            if(matS[i][j] <= s[j]):
                tpl = tpl + (0,)
            else:
                tpl = tpl + (255,)
        mrs.append(tpl)
    return mrs

# --------- fonction ET ------------

def et(matS,s):
    # Matrice après seuillage :
    mrset = []
    for i in range(0 ,len(matS)):
        if(matS[i][0] > s[0]) & (matS[i][1] > s[1]) & (matS[i][2] > s[2]):
            tpl = (255,255,225)
        else:
            tpl = (0,0,0)
        mrset.append(tpl)
    return mrset

'''def et(matET,columns):
    cols = int(columns / 3)
    matETF = []
    matligne = []
    for l in range(0, len(matET)):
        if (((l % cols) == 0) & (l != 0)):
            matETF.append(matligne)
            matligne = []
        if (matET[l][0] == 0) | (matET[l][1] == 0) | (matET[l][2] == 0):
            matligne.append(0)
        else:
            matligne.append(225)
    matETF.append(matligne)
    return matETF'''

# --------- fonction OU ------------
'''def ou(matOU,columns):
    cols = int(columns / 3)
    matOUF = []
    matligneOU = []
    for l in range(0, len(matOU)):
        if (((l % cols) == 0) & (l != 0)):
            matOUF.append(matligneOU)
            matligneOU = []
        if (matOU[l][0] == 0) & (matOU[l][1] == 0) & (matOU[l][2] == 0):
            matligneOU.append(0)
        else:
            matligneOU.append(225)
    matOUF.append(matligneOU)
    return matOUF'''
def ou(matS,s):
    # Matrice après seuillage :
    mrsou = []
    for i in range(0 ,len(matS)):
        if(matS[i][0] > s[0]) | (matS[i][1] > s[1]) | (matS[i][2] > s[2]):
            tpl = (255,255,225)
        else:
            tpl = (0,0,0)
        mrsou.append(tpl)
    return mrsou

# --------- algorithme Otsu ------------
def class_average(cl, start, end):
    niv = np.arange(start, end)
    m = np.multiply(cl,niv)
    return np.sum(m) / np.sum(cl)


def get_variance(hist, s):
    c0 = hist[:s]
    c1 = hist[s:]
    pc0 = np.sum(c0) / np.sum(hist)
    pc1 = np.sum(c1) / np.sum(hist)
    m = class_average(hist, 0, 256)
    m0 = class_average(c0, 0, s)
    m1 = class_average(c1, s, 256)
    return pc0 * (m0 - m) * 2 + pc1 * (m1 - m) * 2


def otsu_thresholding(hist):
    max_variance = 0
    seuil = 0
    for s in range(1, 254):
        variance = get_variance(hist, s)
        if variance > max_variance:
            max_variance = variance
            seuil = s
    return seuil