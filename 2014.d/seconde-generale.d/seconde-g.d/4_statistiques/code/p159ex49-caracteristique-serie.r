#Récupération des données dans une liste
data=c(12, 9, 6, 13, 10, 9, 8, 16, 11, 17, 9, 9, 16, 13, 17, 9, 14)

# Résumer intéressant des principales caractéristiques de la série
summary(data)

# Histogramme
hist(data,breaks=17,col="red")

# Nuage de points
dotchart(data)
plot(data)

# Diagramme en baton
barplot(data)


