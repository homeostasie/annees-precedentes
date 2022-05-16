# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf
CHAP = 4_trigonometrie

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

poly:
	latex tex/$(CHAP)-poly.tex
	latex tex/$(CHAP)-poly.tex	
	dvipdf $(CHAP)-poly.dvi $(CHAP)-poly.pdf 
	mv $(CHAP)-poly.pdf '$(PDFDIR)'/$(CHAP)-poly.pdf

exo1:
	latex tex/$(CHAP)-exo-1.tex
	latex tex/$(CHAP)-exo-1.tex	
	dvipdf $(CHAP)-exo-1.dvi $(CHAP)-exo-1.pdf 
	mv $(CHAP)-exo-1.pdf '$(PDFDIR)'/$(CHAP)-exo-1.pdf

exo2:
	latex tex/$(CHAP)-exo-2.tex
	latex tex/$(CHAP)-exo-2.tex	
	dvipdf $(CHAP)-exo-2.dvi $(CHAP)-exo-2.pdf 
	mv $(CHAP)-exo-2.pdf '$(PDFDIR)'/$(CHAP)-exo-2.pdf

ie:
	pdflatex tex/$(CHAP)-ie-1.tex
	pdflatex tex/$(CHAP)-ie-1.tex	 
	mv $(CHAP)-ie-1.pdf '$(PDFDIR)'/$(CHAP)-ie-1.pdf
	pdflatex tex/$(CHAP)-ie-2.tex
	pdflatex tex/$(CHAP)-ie-2.tex	 
	mv $(CHAP)-ie-2.pdf '$(PDFDIR)'/$(CHAP)-ie-2.pdf



# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~

