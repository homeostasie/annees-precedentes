# Dossiers
CODE := $(shell pwd)
PDFDIR = pdf
CHAP = 4_calcul-litteral

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard sources/1/*.ipe sources/2/*.ipe sources/3/*.ipe sources/4/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/1/%.pdf: sources/1/%.ipe
	ipetoipe -pdf $<
sources/2/%.pdf: sources/2/%.ipe
	ipetoipe -pdf $<
sources/3/%.pdf: sources/3/%.ipe
	ipetoipe -pdf $<
sources/4/%.pdf: sources/4/%.ipe
	ipetoipe -pdf $<

# interrogation écrite	

exo1:
	pdflatex tex/$(CHAP)-exo.tex
	pdflatex tex/$(CHAP)-exo.tex
	mv $(CHAP)-exo.pdf '$(PDFDIR)'/$(CHAP)-exo.pdf	

ie1:
	pdflatex tex/$(CHAP)-ie-1a.tex
	pdflatex tex/$(CHAP)-ie-1a.tex
	pdflatex tex/$(CHAP)-ie-1b.tex
	pdflatex tex/$(CHAP)-ie-1b.tex
	mv $(CHAP)-ie-1a.pdf '$(PDFDIR)'/$(CHAP)-ie-1a.pdf	
	mv $(CHAP)-ie-1b.pdf '$(PDFDIR)'/$(CHAP)-ie-1b.pdf

met:
	pdflatex tex/4_met.tex
	pdflatex tex/4_met.tex
	mv 4_met.pdf '$(PDFDIR)'/4_met.pdf

met2:
	pdflatex tex/4_met-2.tex
	pdflatex tex/4_met-2.tex
	mv 4_met-2.pdf '$(PDFDIR)'/4_met-2.pdf

met_pres:
	pdflatex tex/4_met-pres.tex
	pdflatex tex/4_met-pres.tex
	mv 4_met-pres.pdf '$(PDFDIR)'/4_met-pres.pdf	

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
