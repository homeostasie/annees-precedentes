# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf
CHAP = 5_complexe

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img exo

# Générations des images
FIGSRC = $(wildcard sources/cours/*.ipe sources/cours/*.ipe sources/ie/*ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/ie/%.pdf: sources/ie/%.ipe
	ipetoipe -pdf $<


ie:
	pdflatex tex/$(CHAP)-ie-1.tex
	pdflatex tex/$(CHAP)-ie-1.tex	 
	mv $(CHAP)-ie-1.pdf '$(PDFDIR)'/$(CHAP)-ie-1.pdf
	pdflatex tex/$(CHAP)-ie-2.tex
	pdflatex tex/$(CHAP)-ie-2.tex	 
	mv $(CHAP)-ie-2.pdf '$(PDFDIR)'/$(CHAP)-ie-2.pdf
	pdflatex tex/$(CHAP)-ie-R.tex
	pdflatex tex/$(CHAP)-ie-R.tex	 
	mv $(CHAP)-ie-R.pdf '$(PDFDIR)'/$(CHAP)-ie-R.pdf

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~

