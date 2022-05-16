# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf
CHAP = 7_probabilités

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: exo

# Générations des images
FIGSRC = $(wildcard sources/cours/*.ipe sources/ie/*.ipe sources/exo/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/cours/%.pdf: sources/cours/%.ipe
	ipetoipe -pdf $<
sources/ie/%.pdf: sources/ie/%.ipe
	ipetoipe -pdf $<
sources/exo/%.pdf: sources/exo/%.ipe
	ipetoipe -pdf $<

# interrogation écrite

poly:
	pdflatex tex/$(CHAP)-poly.tex
	pdflatex tex/$(CHAP)-poly.tex
	mv $(CHAP)-poly.pdf '$(PDFDIR)'/$(CHAP)-poly.pdf

ie:
	latex tex/$(CHAP)-ie.tex
	latex tex/$(CHAP)-ie.tex
	dvipdf $(CHAP)-ie.dvi '$(PDFDIR)'/$(CHAP)-ie.pdf
	mv $(CHAP)-ie.pdf '$(PDFDIR)'/$(CHAP)-ie.pdf


pres:
	pdflatex tex/$(CHAP)-pres.tex
	pdflatex tex/$(CHAP)-pres.tex
	mv $(CHAP)-pres.pdf '$(PDFDIR)'/$(CHAP)-pres.pdf


# interrogation écrite	
exo1:
	pdflatex tex/$(CHAP)-exo-1.tex
	pdflatex tex/$(CHAP)-exo-1.tex
	mv $(CHAP)-exo-1.pdf '$(PDFDIR)'/$(CHAP)-exo-1.pdf

# nettoyage
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
