# Espace de travail

setwd("/home/thom/Documents/2017.d/Cycle-4/t3_gestion-de-donnees/sources/ch1-organisation")

# Données


# Tableau d'effectif des marques
x_label_voit = c("Peugeot", "Renault", "Citroën", "Mazda")
x_freq_voit = c(25, 60, 12, 3)

df_voit = data.frame(x_label_voit, x_freq_voit)
df_voit

# Dessin du diagramme circulaire

### Export en pdf
pdf(file = "ch1-diag-circulaire.pdf")

pie(df_voit[,2], df_voit[,1])

### Fin export
dev.off()


# Tableau d'effectif du nombre de frères et sœurs

df_fs = data.frame(c("0","1","2","3","4"), c(15, 10, 25, 5, 8))
names(df_fs) <- c("Nombre de frères et sœurs", "Effectif")
 
# Dessin du diagramme en bâton

### Export en pdf
pdf(file = "ch1-diag-baton-1.pdf")

ggplot(data=df_fs, aes(x=`Nombre de frères et sœurs`, y=Effectif)) +
  geom_bar(stat="identity")

### Fin export
dev.off()


### Export en pdf
pdf(file = "ch1-diag-baton-2.pdf")

x_freq_taille = c(28, 12, 25, 5)
names(x_freq_taille) = c("[1.50 ; 1.60[", "[1.60 ; 1.65[", "[1.65 ; 1.70[", "[1.70 ; 1.80[")

# Control width:
barplot(x_freq_taille, width=c(1, 0.6, 0.6 ,1), ylim = c(0,30) )

### Fin export
dev.off()


data_brute_note = sample(c(rep(5,1) , rep(6,2) , rep(7,2) ,rep(9,2) , rep(10,1) , rep(11,2) , 
         rep(12,1) , rep(13,5) , rep(14,1) , rep(15,1) , rep(16,2) , rep(17,1) ))

dl = table(factor(data_brute_note))

Note = data.frame(dl)
names(Note) <- c("Notes", "Effectif")

### Export en pdf
pdf(file = "ch1-diag-exo-1.pdf")

p = ggplot(data=Note, aes(x=Notes, y=Effectif)) +
  geom_bar(stat="identity")
p

### Fin export
dev.off()


