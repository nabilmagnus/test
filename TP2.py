#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:41:34 2018

@author: nabil
"""

from copy import deepcopy
import numpy as np
from matplotlib import pyplot as plt
from sklearn import *
from numpy import *
from matplotlib.pyplot import *
from random import randint

iris = datasets.load_iris()
X = iris.data
Y = iris.target

# **********************************************************************************************

"""
def Kmeans(X, k):

    C = zeros((k,X.shape[1]))
    liste = []
    for l in range(k):
        h = randint(0, 149)
        C[l]=X[h]

    classe = []

    dis = metrics.pairwise.euclidean_distances(X, C)

    liste = zeros((k,X.shape[1]))

    classe = zeros(X.shape[0])

    changed = 1

    while (changed == 1 ):  
        print ('ok')
        changed = 0

        for i in range(X.shape[0]):
            Min=argmin(dis[i,:])
            classe[i] = Min


        for i in range(k):

            if ( any (liste[i] != X[classe == i].mean(0)) ):

                a = X[classe == i].mean(0)       

                liste[i] = a

                changed = 1

        dis = metrics.pairwise.euclidean_distances(X, liste)

    return liste
"""


# print Kmeans(X,10)

# **************************************************************************************

def KmeansPlus(X, k):

    C = zeros((k, X.shape[1]))

    rand = randint(0, 149)

    C[0] = X[rand]

    dis = metrics.pairwise.euclidean_distances(X, [C[0]])

    distance = dis / dis.sum()

    Max = argmax(distance)

    C[1] = X[Max]

    # neme Centre

    classe = zeros((2,150))

    for i in range(2):
        dis2 = metrics.pairwise.euclidean_distances(X, [C[i]])
        dis2[dis2 == 0] = 99
        classe[i] = dis2[:,0]


    classe = classe.transpose()

    Y1 = zeros((150))

    for i in range (classe.shape[0]):
        if argmin(classe[i]) == 0:
            Y1[i] = 0
        else:
            Y1[i] = 1


    print Y1


    """
    C = zeros((k,X.shape[1]))
    liste = []

    classe = []

    dis = metrics.pairwise.euclidean_distances(X, C)

    liste = zeros((k,X.shape[1]))

    classe = zeros(X.shape[0])

    changed = 1

    while (changed == 1 ):  
        print ('ok')
        changed = 0

        for i in range(X.shape[0]):
            Min=argmin(dis[i,:])
            classe[i] = Min


        for i in range(k):

            if ( any (liste[i] != X[classe == i].mean(0)) ):

                a = X[classe == i].mean(0)       

                liste[i] = a

                changed = 1

        dis = metrics.pairwise.euclidean_distances(X, liste)

    return liste 

    """


# ********************************************************************************************************

print KmeansPlus(X, 4)

print("Yaw te pas la ")
