# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf
CHAP = 3_variations

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

ie:
	pdflatex tex/$(CHAP)-ie-A.tex
	pdflatex tex/$(CHAP)-ie-A.tex
	mv $(CHAP)-ie-A.pdf '$(PDFDIR)'/$(CHAP)-ie-A.pdf
	pdflatex tex/$(CHAP)-ie-B.tex
	pdflatex tex/$(CHAP)-ie-B.tex
	mv $(CHAP)-ie-B.pdf '$(PDFDIR)'/$(CHAP)-ie-B.pdf

poly:
	pdflatex tex/$(CHAP)-poly.tex
	pdflatex tex/$(CHAP)-poly.tex
	mv $(CHAP)-poly.pdf '$(PDFDIR)'/$(CHAP)-poly.pdf


# nettoyage
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
