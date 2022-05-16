# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf
CHAP = 8_equa-diff

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img exo1 

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
	latex tex/$(CHAP)-poly.tex
	latex tex/$(CHAP)-poly.tex
	dvipdf $(CHAP)-poly.dvi $(CHAP)-poly.pdf
	mv $(CHAP)-poly.pdf '$(PDFDIR)'/$(CHAP)-poly.pdf


# interrogation écrite	
exo1:
	pdflatex tex/$(CHAP)-exo-1.tex
	pdflatex tex/$(CHAP)-exo-1.tex
	mv $(CHAP)-exo-1.pdf '$(PDFDIR)'/$(CHAP)-exo-1.pdf

# interrogation écrite	
exo2:
	pdflatex tex/$(CHAP)-exo-2.tex
	pdflatex tex/$(CHAP)-exo-2.tex
	mv $(CHAP)-exo-2.pdf '$(PDFDIR)'/$(CHAP)-exo-2.pdf

# interrogation écrite	
exo3:
	pdflatex tex/$(CHAP)-exo-3.tex
	pdflatex tex/$(CHAP)-exo-3.tex
	mv $(CHAP)-exo-3.pdf '$(PDFDIR)'/$(CHAP)-exo-3.pdf

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi *.thm
	rm -f *.backup *~

