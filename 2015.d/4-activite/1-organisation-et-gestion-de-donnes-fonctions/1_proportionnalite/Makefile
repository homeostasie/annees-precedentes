# Dossiers
CODE := $(shell pwd)
PDFDIR = pdf
CHAP = 1_proportionnalite

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard sources/1/*.ipe sources/2/*.ipe )

FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/1/%.pdf: sources/1/%.ipe
	ipetoipe -pdf $<
sources/2/%.pdf: sources/2/%.ipe
	ipetoipe -pdf $<

# interrogation écrite	

ie1:
	pdflatex tex/$(CHAP)-ie-1.tex
	pdflatex tex/$(CHAP)-ie-1.tex
	mv $(CHAP)-ie-1.pdf '$(PDFDIR)'/$(CHAP)-ie-1.pdf	

ie1C:
	pdflatex tex/$(CHAP)-ie-1-COR.tex
	pdflatex tex/$(CHAP)-ie-1-COR.tex
	mv $(CHAP)-ie-1-COR.pdf '$(PDFDIR)'/$(CHAP)-ie-1-COR.pdf

ie2:
	pdflatex tex/$(CHAP)-ie-2.tex
	pdflatex tex/$(CHAP)-ie-2.tex
	mv $(CHAP)-ie-2.pdf '$(PDFDIR)'/$(CHAP)-ie-2.pdf

ie3:
	pdflatex tex/$(CHAP)-ie-3.tex
	pdflatex tex/$(CHAP)-ie-3.tex
	mv $(CHAP)-ie-3.pdf '$(PDFDIR)'/$(CHAP)-ie-3.pdf

ie3ab:
	pdflatex tex/$(CHAP)-ie-3a.tex
	pdflatex tex/$(CHAP)-ie-3a.tex
	mv $(CHAP)-ie-3a.pdf '$(PDFDIR)'/$(CHAP)-ie-3a.pdf
	pdflatex tex/$(CHAP)-ie-3b.tex
	pdflatex tex/$(CHAP)-ie-3b.tex
	mv $(CHAP)-ie-3b.pdf '$(PDFDIR)'/$(CHAP)-ie-3b.pdf

iev:
	pdflatex tex/vitesse-ie.tex
	pdflatex tex/vitesse-ie.tex
	mv vitesse-ie.pdf '$(PDFDIR)'/vitesse-ie.pdf

ievfm:
	pdflatex tex/vitesse-ie-2.tex
	pdflatex tex/vitesse-ie-2.tex
	mv vitesse-ie-2.pdf '$(PDFDIR)'/vitesse-ie-2.pdf
	pdflatex tex/vitesse-ie-3.tex
	pdflatex tex/vitesse-ie-3.tex
	mv vitesse-ie-3.pdf '$(PDFDIR)'/vitesse-ie-3.pdf

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
