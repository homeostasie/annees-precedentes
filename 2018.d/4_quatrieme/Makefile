# Dossiers
CODE := $(shell pwd)
PDFDIR = ../_pdf/4_quatrieme
THEME = 

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard 4x1-pythagore/sources/*.ipe 4x2-trigonometrie/sources/*.ipe 4x6-thales/sources/*ipe)

FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

4x1-pythagore/sources/%.pdf: 4x1-pythagore/sources/%.ipe
	ipetoipe -pdf $<
	
4x2-trigonometrie/sources/%.pdf: 4x2-trigonometrie/sources/%.ipe
	ipetoipe -pdf $<

4x6-thales/sources/%.pdf: 4x6-thales/sources/%.ipe
	ipetoipe -pdf $<	

# Chapitre 1 - Théorème de Pythagore

4x1_pythagore:
	pdflatex 4x1-pythagore/tex/4x1-pythagore.tex
	pdflatex 4x1-pythagore/tex/4x1-pythagore.tex
	mv 4x1-pythagore.pdf '$(PDFDIR)'/4x1-pythagore.pdf
	
4x1e_pythagore-exo:
	pdflatex 4x1-pythagore/tex/4x1-pythagore-exo.tex
	pdflatex 4x1-pythagore/tex/4x1-pythagore-exo.tex
	mv 4x1-pythagore-exo.pdf '$(PDFDIR)'/4x1-pythagore-exo.pdf

4x1ie_calc:
	pdflatex 4x1-pythagore/tex/4x1-pythagore-ie-calculer.tex
	pdflatex 4x1-pythagore/tex/4x1-pythagore-ie-calculer.tex
	mv 4x1-pythagore-ie-calculer.pdf '$(PDFDIR)'/4x1-pythagore-ie-calculer.pdf

4x1ie_chap:
	pdflatex 4x1-pythagore/tex/4x1-pythagore-ie-chap.tex
	pdflatex 4x1-pythagore/tex/4x1-pythagore-ie-chap.tex
	mv 4x1-pythagore-ie-chap.pdf '$(PDFDIR)'/4x1-pythagore-ie-chap.pdf

# Chapitre 2 - Trigonométrie

4x2_trigonometrie:
	pdflatex 4x2-trigonometrie/tex/4x2-trigonometrie.tex
	pdflatex 4x2-trigonometrie/tex/4x2-trigonometrie.tex
	mv 4x2-trigonometrie.pdf '$(PDFDIR)'/4x2-trigonometrie.pdf
	
4x2e_trigonometrie-exo:
	pdflatex 4x2-trigonometrie/tex/4x2-trigonometrie-exo.tex
	pdflatex 4x2-trigonometrie/tex/4x2-trigonometrie-exo.tex
	mv 4x2-trigonometrie-exo.pdf '$(PDFDIR)'/4x2-trigonometrie-exo.pdf

4x2ie_chap:
	pdflatex 4x2-trigonometrie/tex/4x2-trigonometrie-ie.tex
	pdflatex 4x2-trigonometrie/tex/4x2-trigonometrie-ie.tex
	mv 4x2-trigonometrie-ie.pdf '$(PDFDIR)'/4x2-trigonometrie-ie.pdf

# Chapitre 3 - Puissance

4x3_puissances:
	pdflatex 4x3-puissances/tex/4x3-puissances.tex
	pdflatex 4x3-puissances/tex/4x3-puissances.tex
	mv 4x3-puissances.pdf '$(PDFDIR)'/4x3-puissances.pdf
	
4x3e_puissances-exo:
	pdflatex 4x3-puissances/tex/4x3-puissances-exo.tex
	pdflatex 4x3-puissances/tex/4x3-puissances-exo.tex
	mv 4x3-trigonometrie-exo.pdf '$(PDFDIR)'/4x3-puissances-exo.pdf

4x3e_puissances-pb:
	pdflatex 4x3-puissances/tex/4x3-puissances-exo-pb.tex
	pdflatex 4x3-puissances/tex/4x3-puissances-exo-pb.tex
	mv 4x3-puissances-exo-pb.pdf '$(PDFDIR)'/4x3-puissances-exo-pb.pdf

4x3ie_chap:
	pdflatex 4x3-puissances/tex/4x3-puissances-ie.tex
	pdflatex 4x3-puissances/tex/4x3-puissances-ie.tex
	mv 4x3-puissances-ie.pdf '$(PDFDIR)'/4x3-puissances-ie.pdf		


# Chapitre 4 - Petits problèmes de maths

4x4_ppm:
	pdflatex 4x4-petits-problemes-maths/tex/4x4-ppm.tex
	pdflatex 4x4-petits-problemes-maths/tex/4x4-ppm.tex
	mv 4x4-ppm.pdf '$(PDFDIR)'/4x4-ppm.pdf

4x4ie_ppm:
	pdflatex 4x4-petits-problemes-maths/tex/4x4-ppm-ie.tex
	pdflatex 4x4-petits-problemes-maths/tex/4x4-ppm-ie.tex
	mv 4x4-ppm-ie.pdf '$(PDFDIR)'/4x4-ppm-ie.pdf

# Chapitre 6 - Théorème de Thalès

4x6ie:
	pdflatex 4x6-thales/tex/4x6-thales-ie.tex
	pdflatex 4x6-thales/tex/4x6-thales-ie.tex
	mv 4x6-thales-ie.pdf '$(PDFDIR)'/4x6-thales-ie.pdf


# Chapitre 7 - Équations

4x7ie:
	pdflatex 4x7-equations/tex/4x7-equations-ie.tex
	pdflatex 4x7-equations/tex/4x7-equations-ie.tex
	mv 4x7-equations-ie.pdf '$(PDFDIR)'/4x7-equations-ie.pdf			

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~