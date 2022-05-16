# Dossiers
CODE := $(shell pwd)
PDFDIR = ../_pdf
THEME = nombres-et-calculs 

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard sources/1/*.ipe sources/2/*.ipe )

FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/1/%.pdf: sources/1/%.ipe
	ipetoipe -pdf $<


exp:
	pdflatex tex/exo-en-plus.tex
	pdflatex tex/exo-en-plus.tex
	mv exo-en-plus.pdf '$(PDFDIR)'/3/exo-en-plus.pdf	




# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
