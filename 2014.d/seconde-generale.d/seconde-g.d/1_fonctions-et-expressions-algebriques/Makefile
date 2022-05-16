# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf
CHAP = 1_fonctions

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: exo

# Générations des images
FIGSRC = $(wildcard sources/cours/*.ipe sources/ie/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/cours/%.pdf: sources/cours/%.ipe
	ipetoipe -pdf $<
sources/ie/%.pdf: sources/ie/%.ipe
	ipetoipe -pdf $<


# interrogation écrite	

exo:
	pdflatex tex/$(CHAP)-exo-1.tex
	pdflatex tex/$(CHAP)-exo-1.tex	
	mv $(CHAP)-exo-1.pdf '$(PDFDIR)'/$(CHAP)-exo-1.pdf

cours:
	pdflatex tex/$(CHAP)-cours.tex
	pdflatex tex/$(CHAP)-cours.tex
	mv $(CHAP)-cours.pdf '$(PDFDIR)'/$(CHAP)-cours.pdf

pres:
	pdflatex tex/$(CHAP)-pres.tex
	pdflatex tex/$(CHAP)-pres.tex
	mv $(CHAP)-pres.pdf '$(PDFDIR)'/$(CHAP)-pres.pdf

ie: 
	pdflatex tex/$(CHAP)-ie-1.tex
	pdflatex tex/$(CHAP)-ie-1.tex
	mv $(CHAP)-ie-1.pdf '$(PDFDIR)'/$(CHAP)-ie-1.pdf
	pdflatex tex/$(CHAP)-ie-2.tex
	pdflatex tex/$(CHAP)-ie-2.tex
	mv $(CHAP)-ie-2.pdf '$(PDFDIR)'/$(CHAP)-ie-2.pdf

cor:
	pdflatex tex/$(CHAP)-ie-COR.tex
	pdflatex tex/$(CHAP)-ie-COR.tex
	mv $(CHAP)-ie-COR.pdf '$(PDFDIR)'/$(CHAP)-ie-COR.pdf
		
# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~

