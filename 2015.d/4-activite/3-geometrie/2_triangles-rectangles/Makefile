# Dossiers
CODE := $(shell pwd)
PDFDIR = pdf
CHAP = 2_triangles-rectangles

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: target img poly proper

# Générations des images
FIGSRC = $(wildcard sources/1/*.ipe sources/2/*.ipe sources/3/*ipe sources/4/*ipe)
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

dm-demo:
	pdflatex tex/$(CHAP)-DM-demo.tex
	pdflatex tex/$(CHAP)-DM-demo.tex
	mv $(CHAP)-DM-demo.pdf '$(PDFDIR)'/$(CHAP)-DM-demo.pdf	

ie1:
	pdflatex tex/$(CHAP)-ie-1a.tex
	pdflatex tex/$(CHAP)-ie-1a.tex
	mv $(CHAP)-ie-1a.pdf '$(PDFDIR)'/$(CHAP)-ie-1a.pdf	
	pdflatex tex/$(CHAP)-ie-1b.tex
	pdflatex tex/$(CHAP)-ie-1b.tex
	mv $(CHAP)-ie-1b.pdf '$(PDFDIR)'/$(CHAP)-ie-1b.pdf

ieCos:
	pdflatex tex/2_cos-ie.tex
	pdflatex tex/2_cos-ie.tex
	mv 2_cos-ie.pdf '$(PDFDIR)'/2_cos-ie.pdf

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
