# Dossiers
CODE := $(shell pwd)
PDFDIR = ../_pdf
THEME = nombres-et-calculs 

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
	
sources/2/%.pdf: sources/2/%.ipe
	ipetoipe -pdf $<



# Ressources
help:
	ls tex/

r1:
	pdflatex tex/1-pythagore.tex
	pdflatex tex/1-pythagore.tex
	mv 1-pythagore.pdf '$(PDFDIR)'/res/1-pythagore.pdf	

	
r2:
	pdflatex tex/2-thales.tex
	pdflatex tex/2-thales.tex
	mv 2-thales.pdf '$(PDFDIR)'/res/2-thales.pdf	

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
