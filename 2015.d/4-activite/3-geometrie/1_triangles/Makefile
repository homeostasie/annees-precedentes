# Dossiers
CODE := $(shell pwd)
PDFDIR = pdf
CHAP = 1_triangles

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard sources/1/*.ipe sources/2/*.ipe sources/3/*ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/1/%.pdf: sources/1/%.ipe
	ipetoipe -pdf $<
sources/2/%.pdf: sources/2/%.ipe
	ipetoipe -pdf $<
sources/3/%.pdf: sources/3/%.ipe
	ipetoipe -pdf $<

ie2:
	pdflatex tex/2_tri-rec-mi.tex
	pdflatex tex/2_tri-rec-mi.tex
	mv 2_tri-rec-mi.pdf '$(PDFDIR)'/2_tri-rec-mi.pdf	

ie2b:
	pdflatex tex/2_tri-rec-mi-a.tex
	pdflatex tex/2_tri-rec-mi-a.tex
	mv 2_tri-rec-mi-a.pdf '$(PDFDIR)'/2_tri-rec-mi-a.pdf
	pdflatex tex/2_tri-rec-mi-b.tex
	pdflatex tex/2_tri-rec-mi-b.tex
	mv 2_tri-rec-mi-b.pdf '$(PDFDIR)'/2_tri-rec-mi-b.pdf

# interrogation écrite	

poly:
	pdflatex tex/$(CHAP).tex
	pdflatex tex/$(CHAP).tex
	mv $(CHAP).pdf '$(PDFDIR)'/$(CHAP)-poly.pdf	



# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
