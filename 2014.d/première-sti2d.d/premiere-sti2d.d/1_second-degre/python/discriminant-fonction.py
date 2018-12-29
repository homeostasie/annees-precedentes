#!/usr/bin/env python

# Import modules
import math
import numpy
import matplotlib.pyplot as plt # import plot

def trinome(a,b,c,x):
    return (a*x**2 + b*x + c)

# fonction calculant le discriminant
def discriminant(a,b,c):
    return b**2 - 4*a*c

# fonction retournant la solution double
def solutiondouble(a,b):
    return (-b/(2*a))

# fonction retournant les solutions
def solution(a,b,delta):
    x1 = (-b - math.sqrt(delta)) /(2*a)
    x2 = (-b + math.sqrt(delta)) /(2*a) 
    return x1, x2


# fonction de base de résolution de l'équation
def resolution(a,b,c):
    print("Soit l'équation : ",a,"x**2 + ",b,"x + ",c, " = 0" )
    delta = discriminant(a,b,c)

    if(delta < 0):
        print("L'équation n'a pas de solution")

        # Sinon, delta peut être positif ou nul    
    else:
        # Si delta est nul
        if (delta == 0):
            print("L'équation a une solution double.")
            print ("La solution est x = ", solutiondouble(a,b))
            
            #Sinon,  delta ne peut plus qu'être positif.
        else:
            print("L'équation a deux solutions solutions.")
            x1, x2 = solution(a,b,delta)
            print ("Les solutions sont x1 = ",x1, " et ", x2)



def plot_trinome(a,b,c):
    # L'intervalle de trace
    x = numpy.linspace(-10,10,100)
    
    # La courbe
    plt.plot(x,trinome(a,b,c, x))

    # Les axes
    plt.axvline(x=0, color ='r')
    plt.axhline(y=0, color ='r')   
    axes = plt.gca()
    axes.set_xlabel('x : abscisse')
    axes.set_ylabel('f(x) : ordonnée')

    plt.show()



# a*x**2 + b*x + c un trinôme du second degré.
# On rentre les valeurs de a, b et c.
# On souhaite que a, b et c soient des nombres rééls (float en anglais)
# et non une chaîne de charactère (comme pour une phrase)
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))

# Sinon, on fait un simple appel à la fonction avec les bon paramètres:
print(" ---------- Exercice 1 ------------")
resolution(1,-120,2000)

print(" ---------- Exercice 2 ------------")
print("Exercice 2.1")
resolution(1,2,-3)

# On peut également appeler le tracer avec matplotlib.
plot_trinome(1,2,-3)


print("Exercice 2.2")
resolution(1,6,9)

print("Exercice 2.3")
resolution(2,1,(1/2))

print("Exercice 2.4")
resolution(3,2,(1/3))
