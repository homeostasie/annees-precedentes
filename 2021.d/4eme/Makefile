# Dossiers
CODE := $(shell pwd)
PDFDIR = ../_pdf/4eme
THEME = 

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard 4x3-triangles-semblables/*.ipe 4x6-Pythagore/*.ipe 4xbb/*.ipe)

FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

4x3-triangles-semblables/%.pdf: 4x3-triangles-semblables/%.ipe
	ipetoipe -pdf $<

4x6-Pythagore/%.pdf: 4x6-Pythagore/%.ipe
	ipetoipe -pdf $<

4xbb/%.pdf: 4xbb/%.ipe
	ipetoipe -pdf $<

1ie:
	pdflatex 4x1-relatifs/4x1-ie.tex
	pdflatex 4x1-relatifs/4x1-ie.tex
	mv 4x1-ie.pdf '$(PDFDIR)'/4x1-ie-relatifs.pdf

2ie:
	pdflatex 4x2-proportionnalite/4x2-ie.tex
	pdflatex 4x2-proportionnalite/4x2-ie.tex
	mv 4x2-ie.pdf '$(PDFDIR)'/4x2-ie-proportionnalite.pdf

3c:
	pdflatex 4x3-triangles-semblables/4x3-cours.tex
	pdflatex 4x3-triangles-semblables/4x3-cours.tex
	mv 4x3-cours.pdf '$(PDFDIR)'/4x3-cours-semblables.pdf

3ie:
	pdflatex 4x3-triangles-semblables/4x3-ie.tex
	pdflatex 4x3-triangles-semblables/4x3-ie.tex
	mv 4x3-ie.pdf '$(PDFDIR)'/4x3-ie-semblables.pdf


4c:
	pdflatex 4x4-puissances/4x4-cours.tex
	pdflatex 4x4-puissances/4x4-cours.tex
	mv 4x4-cours.pdf '$(PDFDIR)'/4x4-cours-puissances.pdf

4exo:
	pdflatex 4x4-puissances/4x4-exo.tex
	pdflatex 4x4-puissances/4x4-exo.tex
	mv 4x4-exo.pdf '$(PDFDIR)'/4x4-exo-puissances.pdf

4ie:
	pdflatex 4x4-puissances/4x4-ie.tex
	pdflatex 4x4-puissances/4x4-ie.tex
	mv 4x4-ie.pdf '$(PDFDIR)'/4x4-ie-puissances.pdf

5c:
	pdflatex 4x5-calcul-litteral/4x5-cours.tex
	pdflatex 4x5-calcul-litteral/4x5-cours.tex
	mv 4x5-cours.pdf '$(PDFDIR)'/4x5-cours-calcul-litteral.pdf

5pie:
	pdflatex 4x5-calcul-litteral/4x5-prog-ie.tex
	pdflatex 4x5-calcul-litteral/4x5-prog-ie.tex
	mv 4x5-prog-ie.pdf '$(PDFDIR)'/4x5-prog-ie.pdf

5ie:
	pdflatex 4x5-calcul-litteral/4x5-ie.tex
	pdflatex 4x5-calcul-litteral/4x5-ie.tex
	mv 4x5-ie.pdf '$(PDFDIR)'/4x5-ie-calcul-litteral.pdf

6ie:
	pdflatex 4x6-Pythagore/4x6-ie.tex
	pdflatex 4x6-Pythagore/4x6-ie.tex
	mv 4x6-ie.pdf '$(PDFDIR)'/4x6-ie-pythagore.pdf

7ie:
	pdflatex 4x7-vitesse/4x7-ie.tex
	pdflatex 4x7-vitesse/4x7-ie.tex
	mv 4x7-ie.pdf '$(PDFDIR)'/4x7-ie-vitesse.pdf

8ie:
	pdflatex 4x8-statistiques/4x8-ie.tex
	pdflatex 4x8-statistiques/4x8-ie.tex
	mv 4x8-ie.pdf '$(PDFDIR)'/4x8-ie-statistiques.pdf

9dm:
	pdflatex 4x9-volumes/4x9-dm.tex
	pdflatex 4x9-volumes/4x9-dm.tex
	mv 4x9-dm.pdf '$(PDFDIR)'/4x9-dm-volumes.pdf

bb:
	pdflatex 4xbb/4xbb.tex
	pdflatex 4xbb/4xbb.tex
	mv 4xbb.pdf '$(PDFDIR)'/4x9-bb.pdf		

# nettoyage		
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi *.ps
	rm -f *.backup *~