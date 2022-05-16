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

poly:
	pdflatex tex/$(CHAP)-poly.tex
	pdflatex tex/$(CHAP)-poly.tex
	mv $(CHAP)-poly.pdf '$(PDFDIR)'/$(CHAP)-poly.pdf	

pres:
	pdflatex tex/$(CHAP)-pres.tex
	pdflatex tex/$(CHAP)-pres.tex
	mv $(CHAP)-pres.pdf '$(PDFDIR)'/$(CHAP)-pres.pdf	

cos-poly:
	pdflatex tex/2_cos-poly.tex
	pdflatex tex/2_cos-poly.tex
	mv 2_cos-poly.pdf '$(PDFDIR)'/2_cos-poly.pdf

cos-pres:
	pdflatex tex/2_cos-pres.tex
	pdflatex tex/2_cos-pres.tex
	mv 2_cos-pres.pdf '$(PDFDIR)'/2_cos-pres.pdf

demoPy:
	pdflatex tex/$(CHAP)-pythagore-demonstration.tex
	pdflatex tex/$(CHAP)-pythagore-demonstration.tex
	mv $(CHAP)-pythagore-demonstration.pdf '$(PDFDIR)'/$(CHAP)-demoPy.pdf	
# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
