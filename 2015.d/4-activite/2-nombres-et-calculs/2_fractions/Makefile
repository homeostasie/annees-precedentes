# Dossiers
CODE := $(shell pwd)
PDFDIR = pdf
CHAP = 2_fractions

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard sources/1/*.ipe sources/2/*.ipe sources/3/*.ipe )
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/1/%.pdf: sources/1/%.ipe
	ipetoipe -pdf $<
sources/2/%.pdf: sources/2/%.ipe
	ipetoipe -pdf $<
sources/3/%.pdf: sources/3/%.ipe
	ipetoipe -pdf $<

# interrogation écrite	

exo-add-contexte:
	pdflatex tex/$(CHAP)-add-contexte.tex
	pdflatex tex/$(CHAP)-add-contexte.tex
	mv $(CHAP)-add-contexte.pdf '$(PDFDIR)'/$(CHAP)-add-contexte.pdf	

ie-1a:
	pdflatex tex/$(CHAP)-add-ie-1a.tex
	pdflatex tex/$(CHAP)-add-ie-1a.tex
	mv $(CHAP)-add-ie-1a.pdf '$(PDFDIR)'/$(CHAP)-add-ie-1a.pdf

ie-1b:
	pdflatex tex/$(CHAP)-add-ie-1b.tex
	pdflatex tex/$(CHAP)-add-ie-1b.tex
	mv $(CHAP)-add-ie-1b.pdf '$(PDFDIR)'/$(CHAP)-add-ie-1b.pdf

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
