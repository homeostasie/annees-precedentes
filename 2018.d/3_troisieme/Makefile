# Dossiers
CODE := $(shell pwd)
PDFDIR = ../_pdf/3_troisieme
THEME = 

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard 4x1-pythagore/sources/*.ipe 4x2-pythagore/sources/*.ipe 3xx-dm/sources/dm1/*.ipe)

FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

4x1-pythagore/sources/%.pdf: 4x1-pythagore/sources/%.ipe
	ipetoipe -pdf $<

3xx-dm/sources/dm1/%.pdf: 3xx-dm/sources/dm1/%.ipe
	ipetoipe -pdf $<

# Chapitre 1 - Théorème de Pythagore

3x1_statistiques-dm1:
	pdflatex 3x1-statistiques/tex/3x1-statistiques-dm1.tex
	pdflatex 3x1-statistiques/tex/3x1-statistiques-dm1.tex
	mv 3x1-statistiques-dm1.pdf '$(PDFDIR)'/3x1-statistiques-dm1.pdf
	
3x1_statistiques-ie1:
	pdflatex 3x1-statistiques/tex/3x1-statistiques-ie1.tex
	pdflatex 3x1-statistiques/tex/3x1-statistiques-ie1.tex
	mv 3x1-statistiques-ie1.pdf '$(PDFDIR)'/3x1-statistiques-ie1.pdf

# Chapitre 10 - Fonctions affines et linéaires.



3x10_droites-ie1:
	pdflatex 3x10-affines-lineaires/tex/3x10-droites-ie1.tex
	pdflatex 3x10-affines-lineaires/tex/3x10-droites-ie1.tex
	mv 3x10-droites-ie1.pdf '$(PDFDIR)'/3x10-droites-ie1.pdf

3xx_dm1:
	pdflatex 3xx-dm/tex/3xx-dm1.tex
	pdflatex 3xx-dm/tex/3xx-dm1.tex
	mv 3xx-dm1.pdf '$(PDFDIR)'/3xx-dm1.pdf


3xx_dm2:
	pdflatex 3xx-dm/tex/3xx-dm2.tex
	pdflatex 3xx-dm/tex/3xx-dm2.tex
	mv 3xx-dm2.pdf '$(PDFDIR)'/3xx-dm2.pdf
	
3xx_atk:
	pdflatex 3xx-dm/tex/3xx-atk-brevet.tex
	pdflatex 3xx-dm/tex/3xx-atk-brevet.tex
	mv 3xx-atk-brevet.pdf '$(PDFDIR)'/3xx-atk-brevet.pdf

hist-ie1:
	R -q --vanilla < _scripts/bilan-eval.R
	mv ie1.pdf '$(PDFDIR)'/3x1-hist-ie1.pdf

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~