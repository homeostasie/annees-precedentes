# Dossiers
CODE := $(shell pwd)
PDFDIR = ../_pdf
THEME = organisation-et-gestion-de-donnees-fonctions 

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard sources/1/*.ipe sources/2/*.ipe )

FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/1/%.pdf: sources/1/%.ipe
	ipetoipe -pdf $<

# Cinquième

# Quatrième

# Troisième

ie3:
	pdflatex tex/3ie_ch1_organisation-de-donnees-ie.tex
	pdflatex tex/3ie_ch1_organisation-de-donnees-ie.tex
	mv 3ie_ch1_organisation-de-donnees-ie.pdf '$(PDFDIR)'/3/3ie_ch1_organisation-de-donnees-ie.pdf	

ie3-2:
	pdflatex tex/3ie_ch1_gestion-de-donnees-salaire-ie.tex
	pdflatex tex/3ie_ch1_gestion-de-donnees-salaire-ie.tex
	mv 3ie_ch1_gestion-de-donnees-salaire-ie.pdf '$(PDFDIR)'/3/3ie_ch1_gestion-de-donnees-salaire-ie.pdf	

ie3-3:
	pdflatex tex/3ie_ch1_gestion-de-donnees-plantules-ie.tex
	pdflatex tex/3ie_ch1_gestion-de-donnees-plantules-ie.tex
	mv 3ie_ch1_gestion-de-donnees-plantules-ie.pdf '$(PDFDIR)'/3/3ie_ch1_gestion-de-donnees-plantules-ie.pdf	


p182ex34:
	pdflatex tex/ex-p182ex34-representation-TICE.tex
	pdflatex tex/ex-p182ex34-representation-TICE.tex
	mv ex-p182ex34-representation-TICE.pdf '$(PDFDIR)'/3/ex-p182ex34-representation-TICE.pdf	

p194ex:
	pdflatex tex/ex-p194-caracteristiques.tex
	pdflatex tex/ex-p194-caracteristiques.tex
	mv ex-p194-caracteristiques.pdf '$(PDFDIR)'/3/ex-p194-caracteristiques.pdf	
	
# met

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
