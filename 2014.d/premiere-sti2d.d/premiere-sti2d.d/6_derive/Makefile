# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf
CHAP = 6_derive

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

sources/cours/%.pdf: sources/cours/%.ipe
	ipetoipe -pdf $<

sources/ie/%.pdf: sources/ie/%.ipe
	ipetoipe -pdf $<


exo1:
	pdflatex tex/$(CHAP)-exo-1.tex
	pdflatex tex/$(CHAP)-exo-1.tex	
	#dvipdf $(CHAP)-exo-1.dvi $(CHAP)-exo-1.pdf 
	mv $(CHAP)-exo-1.pdf '$(PDFDIR)'/$(CHAP)-exo-1.pdf

ie1:
	pdflatex tex/$(CHAP)-ie-1.tex
	pdflatex tex/$(CHAP)-ie-1.tex	
	mv $(CHAP)-ie-1.pdf '$(PDFDIR)'/$(CHAP)-ie-1.pdf

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~

