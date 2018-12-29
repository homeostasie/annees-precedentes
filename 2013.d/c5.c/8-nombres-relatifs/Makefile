# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf

# Visualiser les pdf
LOG=evince

all: poly img poly exo pres proper

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
	
exo:
	pdflatex tex/8-exo-1.tex
	pdflatex tex/8-exo-1.tex
	mv 8-exo-1.pdf $(PDFDIR)/8-exo-1.pdf
	
dm:
	pdflatex tex/8-dm.tex
	pdflatex tex/8-dm.tex
	mv 8-dm.pdf $(PDFDIR)/8-dm.pdf
		
poly:
	pdflatex tex/8-poly.tex
	pdflatex tex/8-poly.tex	
	mv 8-poly.pdf $(PDFDIR)/8-poly.pdf
		
pres:
	pdflatex tex/8-pres.tex
	pdflatex tex/8-pres.tex
	mv 8-pres.pdf $(PDFDIR)/8-pres.pdf				

ie:
	pdflatex tex/8-ie.tex
	pdflatex tex/8-ie.tex
	mv 8-ie.pdf $(PDFDIR)/8-ie.pdf

e2:
	pdflatex tex/8-exo-2.tex
	pdflatex tex/8-exo-2.tex
	mv 8-exo-2.pdf $(PDFDIR)/8-exo-2.pdf	
# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~

