# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf
CHAP = 5_fonctions-affines

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: exo

# Générations des images
FIGSRC = $(wildcard sources/cours/*.ipe sources/ie/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/cours/%.pdf: sources/cours/%.ipe
	ipetoipe -pdf $<
sources/ie/%.pdf: sources/ie/%.ipe
	ipetoipe -pdf $<


# interrogation écrite

poly:
	pdflatex tex/$(CHAP)-poly.tex
	pdflatex tex/$(CHAP)-poly.tex
	mv $(CHAP)-poly.pdf '$(PDFDIR)'/$(CHAP)-poly.pdf
exo:
	pdflatex tex/$(CHAP)-exo.tex
	pdflatex tex/$(CHAP)-exo.tex
	mv $(CHAP)-exo.pdf '$(PDFDIR)'/$(CHAP)-exo.pdf

pres:
	pdflatex tex/$(CHAP)-pres.tex
	pdflatex tex/$(CHAP)-pres.tex
	mv $(CHAP)-pres.pdf '$(PDFDIR)'/$(CHAP)-pres.pdf


# nettoyage
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
