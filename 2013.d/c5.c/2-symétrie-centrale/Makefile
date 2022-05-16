# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf

# Visualiser les pdf
LOG=evince

all: poly img ie exo proper

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

# Générations des images
FIGSRC = $(wildcard sources/ie/*.ipe sources/exo/*.ipe sources/cours/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/ie/%.pdf: sources/ie/%.ipe
	ipetoipe -pdf $<
sources/exo/%.pdf: sources/exo/%.ipe
	ipetoipe -pdf $<
sources/cours/%.pdf: sources/cours/%.ipe
	ipetoipe -pdf $<

# interrogation écrite	
ie:
	pdflatex tex/2-ie.tex
	pdflatex tex/2-ie.tex
	mv 2-ie.pdf $(PDFDIR)/2-ie.pdf
	
exo:
	pdflatex tex/2-exo-1.tex
	pdflatex tex/2-exo-1.tex
	mv 2-exo-1.pdf $(PDFDIR)/2-exo-1.pdf
	
poly:
	pdflatex tex/2-poly.tex
	pdflatex tex/2-poly.tex	
	mv 2-poly.pdf $(PDFDIR)/2-poly.pdf
			
# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~

