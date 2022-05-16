# Dossiers
CODE := $(shell pwd)
PDFDIR = ../_pdf/3eme
THEME = 

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard 3x6-pythagore/sources/*.ipe 4x2-trigonometrie/sources/*.ipe 4x6-thales/sources/*ipe)

FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

3x6-pythagore/sources/%.pdf: 3x6-pythagore/sources/%.ipe
	ipetoipe -pdf $<

# Mise en route

auto1:
	latex 3x0_automatismes/S1-10_mini-exo.tex
	dvips S1-10_mini-exo.dvi
	ps2pdf S1-10_mini-exo.ps

# Chapitre 1

1exo:
	latex 3x1-calcul-algebrique-et-litteral/3x1-exo-pyro.tex
	dvips 3x1-exo-pyro.dvi
	ps2pdf 3x1-exo-pyro.ps
	mv 3x1-exo-pyro.pdf '$(PDFDIR)'/3x1-exo-pyro.pdf

1cours:
	pdflatex 3x1-calcul-algebrique-et-litteral/3x1-cours.tex
	pdflatex 3x1-calcul-algebrique-et-litteral/3x1-cours.tex
	mv 3x1-cours.pdf '$(PDFDIR)'/3x1-cours-calculer.pdf



2ie:
	pdflatex 3x2-triangles-semblables/3x2-ie.tex
	pdflatex 3x2-triangles-semblables/3x2-ie.tex
	mv 3x2-ie.pdf '$(PDFDIR)'/3x2-ie.pdf

4cours:
	pdflatex 3x4-factoriser/3x4-cours.tex
	pdflatex 3x4-factoriser/3x4-cours.tex
	mv 3x4-cours.pdf '$(PDFDIR)'/3x4-factoriser.pdf

4ie:
	pdflatex 3x4-factoriser/3x4-ie.tex
	pdflatex 3x4-factoriser/3x4-ie.tex
	mv 3x4-ie.pdf '$(PDFDIR)'/3x4-ie.pdf

5ie:
	latex 3x5-thales/3x5-ie.tex
	dvips 3x5-ie.dvi
	ps2pdf 3x5-ie.ps
	mv 3x5-ie.pdf '$(PDFDIR)'/3x5-ie.pdf

6cours:
	pdflatex 3x6-pythagore/3x6-pythagore.tex
	pdflatex 3x6-pythagore/3x6-pythagore.tex
	mv 3x6-pythagore.pdf '$(PDFDIR)'/3x6-pythagore.pdf


6ie:
	pdflatex 3x6-pythagore/3x6-ie.tex
	pdflatex 3x6-pythagore/3x6-ie.tex
	mv 3x6-ie.pdf '$(PDFDIR)'/3x6-ie.pdf

11cours:
	pdflatex 3x11-equations/3x11-equations.tex
	pdflatex 3x11-equations/3x11-equations.tex
	mv 3x11-equations.pdf '$(PDFDIR)'/3x11-equations.pdf

bb:
	latex 3xz-brevet-blanc/bb1.tex
	dvips bb1.dvi
	ps2pdf bb1.ps
	mv bb1.pdf '$(PDFDIR)'/bb1.pdf		

bbcc:
	latex 3xz-brevet-blanc/bb1-cor.tex
	dvips bb1-cor.dvi
	ps2pdf bb1-cor.ps
	mv bb1-cor.pdf '$(PDFDIR)'/bb1-cor.pdf		

9ie:
	pdflatex 3x9-probabilite/3x9-ie.tex
	pdflatex 3x9-probabilite/3x9-ie.tex
	mv 3x9-ie.pdf '$(PDFDIR)'/3x9-ie.pdf

prep:
	pdflatex 3xz-brevet-blanc/prep.tex
	pdflatex 3xz-brevet-blanc/prep.tex
	mv prep.pdf '$(PDFDIR)'/prep.pdf

# nettoyage		
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi *.ps
	rm -f *.backup *~