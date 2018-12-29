# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf
CHAP = 3_derivees

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img exo1 

# Générations des images
FIGSRC = $(wildcard sources/ie/*.ipe sources/ie/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/cours/%.pdf: sources/cours/%.ipe
	ipetoipe -pdf $<
sources/ie/%.pdf: sources/ie/%.ipe
	ipetoipe -pdf $<


# interrogation écrite	
exo1:
	pdflatex tex/$(CHAP)-exo-1.tex
	pdflatex tex/$(CHAP)-exo-1.tex
	mv $(CHAP)-exo-1.pdf '$(PDFDIR)'/$(CHAP)-exo-1.pdf

cor1:
	pdflatex tex/$(CHAP)-exo-1-COR.tex
	pdflatex tex/$(CHAP)-exo-1-COR.tex
	mv $(CHAP)-exo-1-COR.pdf '$(PDFDIR)'/$(CHAP)-exo-1-COR.pdf


# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi *.thm
	rm -f *.backup *~

