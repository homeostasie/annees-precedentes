# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper ie

# Générations des images
FIGSRC = $(wildcard sources/cours/*.ipe sources/ie/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/cours/%.pdf: sources/cours/%.ipe
	ipetoipe -pdf $<
sources/ie/%.pdf: sources/ie/%.ipe
	ipetoipe -pdf $<

	
# interrogation écrite	
	
poly:
	pdflatex tex/11-poly.tex
	pdflatex tex/11-poly.tex	
	mv 11-poly.pdf '$(PDFDIR)'/11-poly.pdf
	
	
pres:
	pdflatex tex/11-pres.tex
	pdflatex tex/11-pres.tex	
	mv 11-pres.pdf '$(PDFDIR)'/11-pres.pdf		
	
ie:
	pdflatex tex/11-ie-a.tex
	pdflatex tex/11-ie-a.tex
	pdflatex tex/11-ie-b.tex
	pdflatex tex/11-ie-b.tex		
	mv 11-ie-a.pdf '$(PDFDIR)'/11-ie-a.pdf
	mv 11-ie-b.pdf '$(PDFDIR)'/11-ie-b.pdf		
		
# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~

