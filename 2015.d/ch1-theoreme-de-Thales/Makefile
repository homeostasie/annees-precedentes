# Dossiers
CODE := $(shell pwd)
PDFDIR = pdf
CHAP = 1_thales

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: exo

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

exo1: 
	pdflatex tex/$(CHAP)-exo-1.tex
	pdflatex tex/$(CHAP)-exo-1.tex
	mv $(CHAP)-exo-1.pdf '$(PDFDIR)'/$(CHAP)-exo-1.pdf

exo2: 
	pdflatex tex/$(CHAP)-exo-2.tex
	pdflatex tex/$(CHAP)-exo-2.tex
	mv $(CHAP)-exo-2.pdf '$(PDFDIR)'/$(CHAP)-exo-2.pdf

exo2b: 
	pdflatex tex/$(CHAP)-exo-2b.tex
	pdflatex tex/$(CHAP)-exo-2b.tex
	mv $(CHAP)-exo-2b.pdf '$(PDFDIR)'/$(CHAP)-exo-2b.pdf

exo2c: 
	pdflatex tex/$(CHAP)-exo-2c.tex
	pdflatex tex/$(CHAP)-exo-2c.tex
	mv $(CHAP)-exo-2c.pdf '$(PDFDIR)'/$(CHAP)-exo-2c.pdf


exo3: 
	pdflatex tex/$(CHAP)-exo-3.tex
	pdflatex tex/$(CHAP)-exo-3.tex
	mv $(CHAP)-exo-3.pdf '$(PDFDIR)'/$(CHAP)-exo-3.pdf

exo4: 
	pdflatex tex/$(CHAP)-exo-4.tex
	pdflatex tex/$(CHAP)-exo-4.tex
	mv $(CHAP)-exo-4.pdf '$(PDFDIR)'/$(CHAP)-exo-4.pdf

poly:
	pdflatex tex/$(CHAP)-poly.tex
	pdflatex tex/$(CHAP)-poly.tex
	mv $(CHAP)-poly.pdf '$(PDFDIR)'/$(CHAP)-poly.pdf	

brenda:
	pdflatex tex/$(CHAP)-poly-brenda.tex
	pdflatex tex/$(CHAP)-poly-brenda.tex
	mv $(CHAP)-poly-brenda.pdf '$(PDFDIR)'/$(CHAP)-poly-brenda.pdf

cherine:
	pdflatex tex/$(CHAP)-poly-cherine.tex
	pdflatex tex/$(CHAP)-poly-cherine.tex
	mv $(CHAP)-poly-cherine.pdf '$(PDFDIR)'/$(CHAP)-poly-cherine.pdf

ie1: 
	pdflatex tex/$(CHAP)-ie-1.tex
	pdflatex tex/$(CHAP)-ie-1.tex
	mv $(CHAP)-ie-1.pdf '$(PDFDIR)'/$(CHAP)-ie-1.pdf

ie2: 
	pdflatex tex/$(CHAP)-ie-2.tex
	pdflatex tex/$(CHAP)-ie-2.tex
	mv $(CHAP)-ie-2.pdf '$(PDFDIR)'/$(CHAP)-ie-2.pdf

ie2b: 
	pdflatex tex/$(CHAP)-ie-2b.tex
	pdflatex tex/$(CHAP)-ie-2b.tex
	mv $(CHAP)-ie-2b.pdf '$(PDFDIR)'/$(CHAP)-ie-2b.pdf

ie3: 
	pdflatex tex/$(CHAP)-ie-3.tex
	pdflatex tex/$(CHAP)-ie-3.tex
	mv $(CHAP)-ie-3.pdf '$(PDFDIR)'/$(CHAP)-ie-3.pdf

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~

