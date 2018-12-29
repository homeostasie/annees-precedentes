# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf
CHAP = 9_hyperbole

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img exo1 

# Générations des images
FIGSRC = $(wildcard sources/1/*.ipe sources/2/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)


# interrogation écrite	
poly:
	latex tex/$(CHAP)-poly.tex
	latex tex/$(CHAP)-poly.tex
	dvipdf $(CHAP)-poly.dvi $(CHAP)-poly.pdf
	mv $(CHAP)-poly.pdf '$(PDFDIR)'/$(CHAP)-poly.pdf


# interrogation écrite	
exo1:
	pdflatex tex/$(CHAP)-exo.tex
	pdflatex tex/$(CHAP)-exo.tex
	mv $(CHAP)-exo.pdf '$(PDFDIR)'/$(CHAP)-exo.pdf



# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi *.thm
	rm -f *.backup *~

