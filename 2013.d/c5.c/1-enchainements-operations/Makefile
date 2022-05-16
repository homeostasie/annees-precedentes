# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf

# Visualiser les pdf
LOG=evince

all: img poly dm ie exo proper

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

# Générations des images
FIGSRC = $(wildcard sources/ie/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/ie/%.pdf: sources/ie/%.ipe
	ipetoipe -pdf $<

# polycopié de cours
poly:
	pdflatex tex/1-poly.tex
	pdflatex tex/1-poly.tex
	mv 1-poly.pdf $(PDFDIR)/1-poly.pdf

# le devoir maison et son corrigé
dm:
	pdflatex tex/1-dm.tex
	pdflatex tex/1-dm.tex
	mv 1-dm.pdf $(PDFDIR)/1-dm.pdf
	pdflatex tex/1-dm-COR.tex
	pdflatex tex/1-dm-COR.tex
	mv 1-dm-COR.pdf	$(PDFDIR)/1-dm-COR.pdf	

# interrogation écrite	
ie:
	pdflatex tex/1-ie.tex
	pdflatex tex/1-ie.tex
	mv 1-ie.pdf $(PDFDIR)/1-ie.pdf		
	pdflatex tex/1-ie-COR.tex
	pdflatex tex/1-ie-COR.tex
	mv 1-ie-COR.pdf $(PDFDIR)/1-ie-COR.pdf
	
# exercices de cours
exo:
	pdflatex tex/1-exo-1.tex
	pdflatex tex/1-exo-1.tex
	mv 1-exo-1.pdf $(PDFDIR)/1-exo-1.pdf

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~

