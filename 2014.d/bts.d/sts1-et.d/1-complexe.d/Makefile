# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf
CHAP = 1_complexes

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img ie1 correc cours py

# Générations des images
FIGSRC = $(wildcard sources/ie/*.ipe sources/ie/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/cours/%.pdf: sources/cours/%.ipe
	ipetoipe -pdf $<
sources/ie/%.pdf: sources/ie/%.ipe
	ipetoipe -pdf $<


# interrogation écrite	
ie1:
	pdflatex tex/$(CHAP)-ie-1-algebre-A.tex
	pdflatex tex/$(CHAP)-ie-1-algebre-A.tex
	mv $(CHAP)-ie-1-algebre-A.pdf '$(PDFDIR)'/$(CHAP)-ie-1-algebre-A.pdf
	pdflatex tex/$(CHAP)-ie-1-algebre-B.tex
	pdflatex tex/$(CHAP)-ie-1-algebre-B.tex
	mv $(CHAP)-ie-1-algebre-B.pdf '$(PDFDIR)'/$(CHAP)-ie-1-algebre-B.pdf

ie2:
	pdflatex tex/$(CHAP)-ie-2.tex
	pdflatex tex/$(CHAP)-ie-2.tex
	mv $(CHAP)-ie-2.pdf '$(PDFDIR)'/$(CHAP)-ie-2.pdf

cor1:
	pdflatex tex/$(CHAP)-ie-1-correction.tex
	pdflatex tex/$(CHAP)-ie-1-correction.tex
	mv $(CHAP)-ie-1-correction.pdf '$(PDFDIR)'/$(CHAP)-ie-1-correction.pdf

cours:
	latex tex/$(CHAP)-BTS-cours.tex
	latex tex/$(CHAP)-BTS-cours.tex
	dvipdf $(CHAP)-BTS-cours
	mv $(CHAP)-BTS-cours.pdf '$(PDFDIR)'/$(CHAP)-BTS-cours.pdf

coursT:	
	latex tex/$(CHAP)-BTS-cours_TROUS.tex	
	latex tex/$(CHAP)-BTS-cours_TROUS.tex
	dvipdf $(CHAP)-BTS-cours	
	mv $(CHAP)-BTS-cours_TROUS.pdf '$(PDFDIR)'/$(CHAP)-BTS-cours_TROUS.pdf

py:
	python3 python/$(CHAP)-ie-1-correction.py
	
# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi *.thm
	rm -f *.backup *~

