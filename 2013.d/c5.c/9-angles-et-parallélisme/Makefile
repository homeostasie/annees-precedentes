# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly ie proper

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
	
poly:
	pdflatex tex/9-poly.tex
	pdflatex tex/9-poly.tex	
	mv 9-poly.pdf '$(PDFDIR)'/9-poly.pdf

pres:
	pdflatex tex/9-pres.tex
	pdflatex tex/9-pres.tex	
	mv 9-pres.pdf '$(PDFDIR)'/9-pres.pdf
	
ie:
	pdflatex tex/9-ie-A.tex
	pdflatex tex/9-ie-A.tex
	pdflatex tex/9-ie-B.tex
	pdflatex tex/9-ie-B.tex		
	mv 9-ie-A.pdf '$(PDFDIR)'/9-ie-A.pdf
	mv 9-ie-B.pdf '$(PDFDIR)'/9-ie-B.pdf			
# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~

