# Dossiers
CODE := $(shell pwd)
PDFDIR = pdf
CHAP = 1_nombres-relatifs

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

ie:
	pdflatex tex/$(CHAP)-ie-1a.tex
	pdflatex tex/$(CHAP)-ie-1a.tex
	mv $(CHAP)-ie-1a.pdf '$(PDFDIR)'/$(CHAP)-ie-1a.pdf
	pdflatex tex/$(CHAP)-ie-1b.tex
	pdflatex tex/$(CHAP)-ie-1b.tex
	mv $(CHAP)-ie-1b.pdf '$(PDFDIR)'/$(CHAP)-ie-1b.pdf
	pdflatex tex/$(CHAP)-ie-1c.tex
	pdflatex tex/$(CHAP)-ie-1c.tex
	mv $(CHAP)-ie-1c.pdf '$(PDFDIR)'/$(CHAP)-ie-1c.pdf
	pdflatex tex/$(CHAP)-ie-1d.tex
	pdflatex tex/$(CHAP)-ie-1d.tex
	mv $(CHAP)-ie-1d.pdf '$(PDFDIR)'/$(CHAP)-ie-1d.pdf


# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
