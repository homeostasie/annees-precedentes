# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf
CHAP = 2_probabilite

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img exo

# Générations des images
FIGSRC = $(wildcard sources/ie/*.ipe sources/ie/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/cours/%.pdf: sources/cours/%.ipe
	ipetoipe -pdf $<
sources/ie/%.pdf: sources/ie/%.ipe
	ipetoipe -pdf $<


exo:
	pdflatex tex/$(CHAP)-exo-1.tex
	pdflatex tex/$(CHAP)-exo-1.tex	
	mv $(CHAP)-exo-1.pdf '$(PDFDIR)'/$(CHAP)-exo-1.pdf

poly:
	latex tex/$(CHAP)-poly.tex
	latex tex/$(CHAP)-poly.tex	
	dvipdf $(CHAP)-poly.dvi $(CHAP)-poly.pdf 
	mv $(CHAP)-poly.pdf '$(PDFDIR)'/$(CHAP)-poly.pdf


ie:
	pdflatex tex/$(CHAP)-ie-1.tex
	pdflatex tex/$(CHAP)-ie-1.tex	
	mv $(CHAP)-ie-1.pdf '$(PDFDIR)'/$(CHAP)-ie-1.pdf

cor:
	latex tex/$(CHAP)-ie-COR.tex
	latex tex/$(CHAP)-ie-COR.tex	
	dvipdf $(CHAP)-ie-COR.dvi $(CHAP)-ie-COR.pdf 
	mv $(CHAP)-ie-COR.pdf '$(PDFDIR)'/$(CHAP)-ie-COR.pdf

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~

