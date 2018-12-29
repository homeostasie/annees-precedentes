# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf
CHAP = 7_suites

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

sources/ie/%.pdf: sources/ie/%.ipe
	ipetoipe -pdf $<


# interrogation écrite	
poly:
	latex tex/$(CHAP)-poly.tex
	latex tex/$(CHAP)-poly.tex
	dvipdf $(CHAP)-poly.dvi $(CHAP)-poly.pdf
	mv $(CHAP)-poly.pdf '$(PDFDIR)'/$(CHAP)-poly.pdf


# interrogation écrite	
exo1:
	pdflatex tex/$(CHAP)-exo-1.tex
	pdflatex tex/$(CHAP)-exo-1.tex
	mv $(CHAP)-exo-1.pdf '$(PDFDIR)'/$(CHAP)-exo-1.pdf


# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi *.thm
	rm -f *.backup *~

