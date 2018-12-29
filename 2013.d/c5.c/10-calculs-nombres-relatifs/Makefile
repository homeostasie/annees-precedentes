# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard sources/cours/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/cours/%.pdf: sources/cours/%.ipe
	ipetoipe -pdf $<

# interrogation écrite	
	
poly:
	pdflatex tex/10-poly.tex
	pdflatex tex/10-poly.tex	
	mv 10-poly.pdf '$(PDFDIR)'/10-poly.pdf
		
pres:
	pdflatex tex/10-pres.tex
	pdflatex tex/10-pres.tex	
	mv 10-pres.pdf '$(PDFDIR)'/10-pres.pdf		
# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~

