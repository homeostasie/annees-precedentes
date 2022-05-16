# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf
CHAP = 11_droites

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img exo1 

# Générations des images
FIGSRC = $(wildcard sources/ie/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/ie/%.pdf: sources/ie/%.ipe
	ipetoipe -pdf $<

# interrogation écrite	
ie:
	pdflatex tex/$(CHAP)-ie.tex
	pdflatex tex/$(CHAP)-ie.tex
	mv $(CHAP)-ie.pdf '$(PDFDIR)'/$(CHAP)-ie.pdf



# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi *.thm
	rm -f *.backup *~

