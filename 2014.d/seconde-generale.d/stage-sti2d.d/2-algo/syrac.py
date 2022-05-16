from __future__ import division
# -*- coding: utf-8 -*-
import math

#########################################################
#                                                       #
#              Conjecture de                            #
#              Syracuse                                 #
#                                                       #
#########################################################

def syracuse(nombre):
    "Conjecture de Syracuse"

     # tant que le nombre est différent de 1
    while(nombre != 1):
        # on test si le nombre est pair
        if 2*math.floor(nombre/2) == nombre:
            nombre = nombre / 2
        else:
            nombre = nombre*3 + 1
        print(nombre)
            
    print("La conjecture est verifié pour N = ",nombre)


print("-------- Syracuse ---------")

syracuse(22)


def syracuse2(nombre):
    "Conjecture de Syracuse"

     # tant que le nombre est différent de 1
    while(nombre != 1):
        # on test si le nombre est pair
        if nombre/2 == nombre//2:
            nombre = nombre / 2
        else:
            nombre = nombre*3 + 1
        print(nombre)
            
    print("La conjecture est verifié pour N = ",nombre)


print("-------- Syracuse ---------")

#syracuse(22)
