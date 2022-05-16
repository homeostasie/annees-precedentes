# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf
EXO1 = 1_factorisation


# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: fact

# Générations des images
FIGSRC = $(wildcard sources/cours/*.ipe sources/ie/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/cours/%.pdf: sources/cours/%.ipe
	ipetoipe -pdf $<
sources/ie/%.pdf: sources/ie/%.ipe
	ipetoipe -pdf $<


# interrogation écrite

fact:
	pdflatex tex/$(EXO1).tex
	pdflatex tex/$(EXO1).tex
	mv $(EXO1).pdf '$(PDFDIR)'/$(EXO1).pdf


# nettoyage
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
