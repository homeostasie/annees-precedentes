# Dossiers
CODE := $(shell pwd)
PDFDIR = pdf
CHAP = 2_gestion-donnees

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard sources/1/*.ipe sources/2/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/1/%.pdf: sources/1/%.ipe
	ipetoipe -pdf $<
sources/2/%.pdf: sources/2/%.ipe
	ipetoipe -pdf $<


# interrogation écrite	

poly:
	pdflatex tex/$(CHAP).tex
	pdflatex tex/$(CHAP).tex
	mv $(CHAP).pdf '$(PDFDIR)'/$(CHAP)-poly.pdf	


# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
