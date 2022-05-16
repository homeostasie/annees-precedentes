# Dossiers
CODE := $(shell pwd)
PDFDIR = $(CODE)/pdf

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img exo1 

# Générations des images
FIGSRC = $(wildcard sources/ie/*.ipe sources/ie/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/cours/%.pdf: sources/cours/%.ipe
	ipetoipe -pdf $<
sources/ie/%.pdf: sources/ie/%.ipe
	ipetoipe -pdf $<


# interrogation écrite	
cd2-3:
	pdflatex tex/cd-2-3.tex
	pdflatex tex/cd-2-3.tex
	mv cd-2-3.pdf '$(PDFDIR)'/cd-2-3.pdf

# interrogation écrite	
cd2-2:
	pdflatex tex/cd-2-2.tex
	pdflatex tex/cd-2-2.tex
	mv cd-2-2.pdf '$(PDFDIR)'/cd-2-2.pdf

# interrogation écrite	
cd2-4:
	pdflatex tex/cd-2-4.tex
	pdflatex tex/cd-2-4.tex
	mv cd-2-4.pdf '$(PDFDIR)'/cd-2-4.pdf

# interrogation écrite	
cd2-5:
	pdflatex tex/cd-2-5.tex
	pdflatex tex/cd-2-5.tex
	mv cd-2-5.pdf '$(PDFDIR)'/cd-2-5.pdf


# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi *.thm
	rm -f *.backup *~

