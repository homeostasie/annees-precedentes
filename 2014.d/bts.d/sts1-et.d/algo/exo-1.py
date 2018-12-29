import math
# Notion d'algorithmie 

### Exercice 1 

###### pas a pas

def ex1_met1(x):
    "Pas a pas"
    
    a = x + 1
    b = a * 2
    c = b - 3

    print("Le resultat est : ",c)


def ex1_met2(x):
    "Un peu moins gourmand"
    
    x = x + 1
    x = x * 2
    x = x - 3

    print("Le resultat est : ",x)

def ex1_met3(x):
    "Un peu plus rapide"
    
    x = (x + 1)*2 - 3

    print("Le resultat est : ",x)

def ex3(x):
    "exo3"
    
    x= (x+2)**2-(x+4)/(x+3)

    print("Le resultat est : ",x)


#------------------------------------#
# On execute pour 3, -4, 0 et 1/3

print("-------- Exo 1 ---------")
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




print("-------- Exo 3 ---------")

ex3(4)
ex3(7)
ex3(-3.)
