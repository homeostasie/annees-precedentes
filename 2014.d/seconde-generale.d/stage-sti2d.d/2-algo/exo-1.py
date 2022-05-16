from __future__ import division
# -*- coding: utf-8 -*-
import math

# Notion d'algorithmie 


#########################################################
#                                                       #
#              Exercice 1                               #
#                                                       #
#########################################################

def ex1_met1(x):
    "Pas a pas"

    print("Avec x= ",x)
    a = x + 1
    b = a * 2
    c = b - 3

    print("-------------> Le resultat est : ",c)


def ex1_met2(x):
    "Un peu moins gourmand"
  
    print("Avec x= ",x)
    x = x + 1
    x = x * 2
    x = x - 3

    print("-------------> Le resultat est : ",x)

def ex1_met3(x):
    "Ligne a ligne"
    
    print("Avec x= ",x)
    x = (x + 1)*2 - 3

    print("-------------> Le resultat est : ",x)



#########################################################
#                                                       #
#              Exercice 2                               #
#                                                       #
#########################################################

def ex2_met1(x):
    "Un peu plus rapide"
    
    print("Avec x= ",x)
    #x = 
    #x =  
    #x = 

    print("-------------> Le resultat est : ",x)


def ex2_met2(x):
    "Un peu plus rapide"
    
    print("Avec x= ",x)
    #x = 
   
    print("-------------> Le resultat est : ",x)



#########################################################
#                                                       #
#              Exercice 3                               #
#                                                       #
#########################################################

def ex3(N):
    "Exercice 3"
    
    print("Avec N= ",N)
    Q = (N+2)**2
    Q = Q - (N+4)
    Q = Q/(N+3)
    print("-------------> Le resultat Q est : ",Q)




#------------- Execution -------------------------------#

print("-------- Exo 1 ---------")

#------------------------------------#
# On execute pour 3, -4, 0 et 1/3


print("Methode pas a pas avec des noms de variables differents")
ex1_met1(3)
ex1_met1(-4)
ex1_met1(0)
ex1_met1(1/3.)


print("Methode pas a pas avec une seule variable")
ex1_met2(3)
ex1_met2(-4)
ex1_met2(0)
ex1_met2(1/3.)


print("Methode directe")

ex1_met3(3)
ex1_met3(-4)
ex1_met3(0)
ex1_met3(1/3.)




print("-------- Exo 2 ---------")
#print("Methode pas a pas avec une seule variable")

#ex2_met1(2)
#ex2_met1(math.sqrt(2))

#print("Methode directe")
#ex2_met2(2)
#ex2_met2(math.sqrt(2))


print("-------- Exo 2 ---------")

#print("Methode ligne a ligne")

#ex3(4)
#ex3(-7)
#ex3(-3)
