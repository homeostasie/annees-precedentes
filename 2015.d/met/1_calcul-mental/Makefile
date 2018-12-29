# Dossiers
CODE := $(shell pwd)
CHAP = 1_calcul-mental

# Visualiser les pdf
LOG=evince

all: s1

# Générations des images
FIGSRC = $(wildcard sources/poly/*.ipe sources/exo/*.ipe sources/ie/*ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/poly/%.pdf: sources/poly/%.ipe
	ipetoipe -pdf $<
sources/exo/%.pdf: sources/exo/%.ipe
	ipetoipe -pdf $<
sources/ie/%.pdf: sources/ie/%.ipe
	ipetoipe -pdf $<


# interrogation écrite	

s1: 
	pdflatex $(CHAP)-serie-1.tex
	pdflatex $(CHAP)-serie-1.tex


# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~

