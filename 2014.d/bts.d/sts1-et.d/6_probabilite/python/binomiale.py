#!/usr/bin/env python

# Fonction factorielle
def factorielle(n):
    res = 1;
    while(n >= 2):
        res = res*n
        n = n - 1
    return res
   

# Fonction combinaison
def combi(n,k):
    return( factorielle(n) / (factorielle(k)*factorielle(n-k)) )

# Fonction binomiale
def binomiale(n,p,k):
    return combi(n,k) * p**k * (1-p)**(n-k)



# def binomiale cumulative : au moins 2
def cumulbinomiale(n,p,k):
    res = 0
    while (k <= n):
        res = res + binomiale(n, p, k)
        k = k + 1
    return res

# Fonction pour appeler le script
def binom():
    n = int(input("n = "))
    p = float(input("p = "))
    k = int(input("k = "))
    print(binomiale(n,p,k))

binom()
