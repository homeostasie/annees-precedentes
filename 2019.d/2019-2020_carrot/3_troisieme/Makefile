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

# Chapitre 1 - Probabilité

3x1:
	pdflatex 3x1-probabilite/3x1-proba.tex
	pdflatex 3x1-probabilite/3x1-proba.tex
	mv 3x1-proba.pdf '$(PDFDIR)'/3x1-proba.pdf

3x1-ie:
	pdflatex 3x1-probabilite/3x1-proba-ie.tex
	pdflatex 3x1-probabilite/3x1-proba-ie.tex
	mv 3x1-proba-ie.pdf '$(PDFDIR)'/3x1-proba-ie.pdf

3x1-dm:
	pdflatex 3x1-probabilite/3x1-proba-dm.tex
	pdflatex 3x1-probabilite/3x1-proba-dm.tex
	mv 3x1-proba-dm.pdf '$(PDFDIR)'/3x1-proba-dm.pdf	

3x1-exo:
	pdflatex 3x1-probabilite/3x1-exercices.tex
	pdflatex 3x1-probabilite/3x1-exercices.tex
	mv 3x1-exercices.pdf '$(PDFDIR)'/3x1-exercices.pdf
	
3x1-pb:
	pdflatex 3x1-probabilite/3x1-problemes.tex
	pdflatex 3x1-probabilite/3x1-problemes.tex
	mv 3x1-problemes.pdf '$(PDFDIR)'/3x1-problemes.pdf

# Chapitre 2 - Calcul littéral

3x2:
	pdflatex 3x2-calcul-litteral-1/3x2-calcul-litteral.tex
	pdflatex 3x2-calcul-litteral-1/3x2-calcul-litteral.tex
	mv 3x2-calcul-litteral.pdf '$(PDFDIR)'/3x2-calcul-litteral.pdf	

3x2-dm:
	pdflatex 3x2-calcul-litteral-1/3x2-calcul-litteral-dm.tex
	pdflatex 3x2-calcul-litteral-1/3x2-calcul-litteral-dm.tex
	mv 3x2-calcul-litteral-dm.pdf '$(PDFDIR)'/3x2-calcul-litteral-dm.pdf

3x2-pi:
	pdflatex 3x2-calcul-litteral-1/3x2-calcul-litteral-pi.tex
	pdflatex 3x2-calcul-litteral-1/3x2-calcul-litteral-pi.tex
	mv 3x2-calcul-litteral-pi.pdf '$(PDFDIR)'/3x2-calcul-litteral-pi.pdf	

3x2-drill:
	pdflatex 3x2-calcul-litteral-1/3x2-calcul-litteral-drill.tex
	pdflatex 3x2-calcul-litteral-1/3x2-calcul-litteral-drill.tex
	mv 3x2-calcul-litteral-drill.pdf '$(PDFDIR)'/3x2-calcul-litteral-drill.pdf

3x2-ie:
	pdflatex 3x2-calcul-litteral-1/3x2-calcul-litteral-ie.tex
	pdflatex 3x2-calcul-litteral-1/3x2-calcul-litteral-ie.tex
	mv 3x2-calcul-litteral-ie.pdf '$(PDFDIR)'/3x2-calcul-litteral-ie.pdf		



# Chapitre 3 - volume

3x3:
	pdflatex 3x3-volumes-1/3x3-volumes-1.tex
	pdflatex 3x3-volumes-1/3x3-volumes-1.tex
	mv 3x3-volumes.pdf '$(PDFDIR)'/3x3-volumes.pdf	

3x3-pb:
	pdflatex 3x3-volumes-1/3x3-volumes-1-pb.tex 
	pdflatex 3x3-volumes-1/3x3-volumes-1-pb.tex 
	mv 3x3-volumes-1-pb.pdf '$(PDFDIR)'/3x3-volumes-1-pb.pdf

3x3-ie:
	pdflatex 3x3-volumes-1/3x3-volumes-1-ie.tex 
	pdflatex 3x3-volumes-1/3x3-volumes-1-ie.tex 
	mv 3x3-volumes-1-ie.pdf '$(PDFDIR)'/3x3-volumes-1-ie.pdf

# Chapitre 6 - Thalès
3x6:
	pdflatex 3x6-thales/3x6-thales.tex
	pdflatex 3x6-thales/3x6-thales.tex
	mv 3x6-thales.pdf '$(PDFDIR)'/3x6-thales.pdf	


# Brevet blanc

bb:
	latex _bb/bb-2019.tex
	dvips bb-2019.dvi
	ps2pdf bb-2019.ps
	
	mv bb-2019.pdf '$(PDFDIR)'/bb-2019.pdf


# Continuité

# Semaine 1

3c1:
	pdflatex _continuite/3c1-continuite.tex 
	pdflatex _continuite/3c1-continuite.tex 
	mv 3c1-continuite.pdf '$(PDFDIR)'/3c1-continuite.pdf
3cc1:
	pdflatex _continuite/3c1-continuite-cor.tex 
	pdflatex _continuite/3c1-continuite-cor.tex 
	mv 3c1-continuite-cor.pdf '$(PDFDIR)'/3c1-continuite-cor.pdf

3bb1:
	latex _continuite/3c1-bb1.tex
	dvips 3c1-bb1.dvi
	ps2pdf 3c1-bb1.ps
	
	mv 3c1-bb1.pdf '$(PDFDIR)'/3c1-bb1.pdf

# Semaine 2

3bb2:
	latex _continuite/3c2-bb2.tex
	dvips 3c2-bb2.dvi
	ps2pdf 3c2-bb2.ps
	
	mv 3c2-bb2.pdf '$(PDFDIR)'/3c2-bb2.pdf	

3cc2:
	pdflatex _continuite/3c2-continuite-cor.tex 
	pdflatex _continuite/3c2-continuite-cor.tex 
	mv 3c2-continuite-cor.pdf '$(PDFDIR)'/3c2-continuite-cor.pdf


# Semaine 3

3bb3:
	pdflatex _continuite/3c3-bb3.tex
	pdflatex _continuite/3c3-bb3.tex
	mv 3c3-bb3.pdf '$(PDFDIR)'/3c3-bb3.pdf

3cc3:
	pdflatex _continuite/3c3-continuite-cor.tex
	pdflatex _continuite/3c3-continuite-cor.tex
	mv 3c3-continuite-cor.pdf '$(PDFDIR)'/3c3-continuite-cor.pdf



# Semaine 4

3bb4:
	latex _continuite/3c4-bb4.tex
	dvips 3c4-bb4.dvi
	ps2pdf 3c4-bb4.ps

	mv 3c4-bb4.pdf '$(PDFDIR)'/3c4-bb4.pdf


# Semaine 5

3cc5:
	pdflatex _continuite/3c5-continuite-cor.tex
	pdflatex _continuite/3c5-continuite-cor.tex
	mv 3c5-continuite-cor.pdf '$(PDFDIR)'/3c5-continuite-cor.pdf


# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi *.ps
	rm -f *.backup *~
	