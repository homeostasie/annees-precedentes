# Dossiers
CODE := $(shell pwd)
PDFDIR = ../_pdf/6_sixieme
THEME = 

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard 6x6-cerles/sources/*.ipe)

FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

6x6-cerles/sources/%.pdf: 6x6-cerles/sources/%.ipe
	ipetoipe -pdf $<

# Chapitre 1 - Théorème de Pythagore

6x6_cercles-ie:
	pdflatex 6x6-cercles/tex/6x6-cercles-ie.tex
	pdflatex 6x6-cercles/tex/6x6-cercles-ie.tex
	mv 6x6-cercles-ie.pdf '$(PDFDIR)'/6x6-cercles-ie.pdf
	


# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~