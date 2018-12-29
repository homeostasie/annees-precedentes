# On est sur la première case.
# On a un grain de riz sur la première case.
# On a un grain de riz sur l'échéquier.

# Nombre de grain de riz par case.
# case est un nombre entier.
case = 1

# Nombre de grain riz au total sur l'échiquier.
# riz est un nombre entier.
riz = 1

# Il y a 8*8=64 cases sur un échiquier.
# Il nous reste 63 cases à remplir de grain de riz.

# Si on veut connaitre pour toutes les cases.
print("Sur la première case, il y a : ", case, "grains de riz, pour un total de : ", riz , "grains sur l'échiquier.")

# On parcours les 63 cases restantes
for i in range(2,65):
    # Les cases suivantes contienent deux fois plus de grain de riz.
    case = case * 2
    # À chaque fois on rajoute les grains de la case dans le sac de riz.
    riz = riz + case
    # Si on veut connaitre pour toutes les cases.
    print("Sur la case : ", i , " , il y a : ", case, "grains de riz, pour un total de : ", riz , "grains sur l'échiquier.")

print("Nombre de grain de riz sur l'échéquier", riz)
print("Écriture scientifique : ", riz*1.)

# Poids en g. On multiplie le nombre de grain par 0.05g
poids = riz * 0.05

# Poids en tonnes. On divise par 10^6 ou on multiplie par 10^-6
poids = riz * 0.05 * 10**(-6) 
print("Poids du riz total en tonnes : ", poids, " tonnes")

# Le nombre d'année nécéssaire.
# Par an, la production mondiale de riz est : 600 millions.
prod_an = 600 * 10 **6
print("La production annuelle de riz est de ", prod_an, "tonnes de riz")

# Le nombre d'année nécéssaire =
# notre poids de riz sur l'échiquier diviser par la production annuelle.
nombre_an = poids / prod_an
print("Il faudra : ", nombre_an, "années à l'empereur afin de combler ça promesse.")
