# Dossiers
CODE := $(shell pwd)
PDFDIR = ../_pdf/5eme
THEME = 

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard 5x2-triangles/sources/*.ipe 5x10-angles/sources/*.ipe 4x6-thales/sources/*ipe)

FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

5x2-triangles/sources/%.pdf: 5x2-triangles/sources/%.ipe
	ipetoipe -pdf $<

5x10-angles/sources/%.pdf: 5x10-angles/sources/%.ipe
	ipetoipe -pdf $<	

# Mise en route

auto1:
	latex 5x0_automatismes/S1-10_mini-exo.tex
	dvips S1-10_mini-exo.dvi
	ps2pdf S1-10_mini-exo.ps

# Chapitre 1

1exo:
	latex 5x1-calculer-et-rediger-des-calculs/5x1-exo-pyro.tex
	dvips 5x1-exo-pyro.dvi
	ps2pdf 5x1-exo-pyro.ps
	mv 5x1-exo-pyro.pdf '$(PDFDIR)'/5x1-exo-pyro.pdf
	

1cours:
	pdflatex 5x1-calculer-et-rediger-des-calculs/5x1-cours.tex
	pdflatex 5x1-calculer-et-rediger-des-calculs/5x1-cours.tex
	mv 5x1-cours.pdf '$(PDFDIR)'/5x1-cours-calculer.pdf

1photocop:
	pdflatex 5x1-calculer-et-rediger-des-calculs/5x1-photocop.tex
	pdflatex 5x1-calculer-et-rediger-des-calculs/5x1-photocop.tex
	mv 5x1-photocop.pdf '$(PDFDIR)'/5x1-photocop-calculer.pdf


# Chapitre 2

2cours:
	pdflatex 5x2-triangles/5x2-cours.tex
	pdflatex 5x2-triangles/5x2-cours.tex
	mv 5x2-cours.pdf '$(PDFDIR)'/5x2-cours-triangle.pdf

2ie:
	pdflatex 5x2-triangles/5x2-ie.tex
	pdflatex 5x2-triangles/5x2-ie.tex
	mv 5x2-ie.pdf '$(PDFDIR)'/5x2-ie.pdf

2h:
	pdflatex 5x2-triangles/5x2-hauteur.tex
	pdflatex 5x2-triangles/5x2-hauteur.tex
	mv 5x2-hauteur.pdf '$(PDFDIR)'/5x2-hauteur.pdf


# Chapitre 2

3ie:
	pdflatex 5x3-fractions-egales/5x3-ie.tex
	pdflatex 5x3-fractions-egales/5x3-ie.tex
	mv 5x3-ie.pdf '$(PDFDIR)'/5x3-ie.pdf


# Chapitre 2

6ie:
	pdflatex 5x6-fractions-calculs/5x6-ie.tex
	pdflatex 5x6-fractions-calculs/5x6-ie.tex
	mv 5x6-ie.pdf '$(PDFDIR)'/5x6-ie.pdf


# Chapitre 2

7ie:
	pdflatex 5x7-proportionnalite/5x7-ie.tex
	pdflatex 5x7-proportionnalite/5x7-ie.tex
	mv 5x7-ie.pdf '$(PDFDIR)'/5x7-ie.pdf	

# Chapitre 2

8ie:
	latex 5x8-relatifs/5x8-ie.tex
	dvips 5x8-ie.dvi
	ps2pdf 5x8-ie.ps
	mv 5x8-ie.pdf '$(PDFDIR)'/5x8-ie.pdf	

10cours:
	pdflatex 5x10-angles/5x10-angles.tex
	pdflatex 5x10-angles/5x10-angles.tex
	mv 5x10-angles.pdf '$(PDFDIR)'/5x10-angles.pdf	

10pres:
	pdflatex 5x10-angles/5x10-pres.tex
	pdflatex 5x10-angles/5x10-pres.tex
	mv 5x10-pres.pdf '$(PDFDIR)'/5x10-pres.pdf	

11ie:
	pdflatex 5x11-calcul-litteral/5x11-ie.tex
	pdflatex 5x11-calcul-litteral/5x11-ie.tex
	mv 5x11-ie.pdf '$(PDFDIR)'/5x11-ie.pdf

# nettoyage		
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi *.ps
	rm -f *.backup *~