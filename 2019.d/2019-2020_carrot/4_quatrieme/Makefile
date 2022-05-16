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
FIGSRC = $(wildcard 4x4-pythagore/sources/*.ipe 4x2-trigonometrie/sources/*.ipe 4x6-thales/sources/*ipe)

FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

4x4-pythagore/sources/%.pdf: 4x4-pythagore/sources/%.ipe
	ipetoipe -pdf $<


# Chapitre 1 - Nombres relatifs 1

1_cours:
	pdflatex 4x1-nombres-relatifs-1/4x1-nombres-relatifs-1.tex
	pdflatex 4x1-nombres-relatifs-1/4x1-nombres-relatifs-1.tex
	mv 4x1-nombres-relatifs-1.pdf '$(PDFDIR)'/4x1-nombres-relatifs-1.pdf
	
1_ie:
	pdflatex 4x1-nombres-relatifs-1/4x1-nombres-relatifs-1-ie.tex
	pdflatex 4x1-nombres-relatifs-1/4x1-nombres-relatifs-1-ie.tex
	mv 4x1-nombres-relatifs-1-ie.pdf '$(PDFDIR)'/4x1-nombres-relatifs-1-ie.pdf

# Chapitre 2 - Proportionnalité 1

# Chapitre 3 - Puissances

3_cours:
	pdflatex 4x3-puissances/4x3-puissances.tex
	pdflatex 4x3-puissances/4x3-puissances.tex
	mv 4x3-puissances.pdf '$(PDFDIR)'/4x3-puissances.pdf
	
3_exo:
	pdflatex 4x3-puissances/4x3-puissances-exo.tex
	pdflatex 4x3-puissances/4x3-puissances-exo.tex
	mv 4x3-puissances-exo.pdf '$(PDFDIR)'/4x3-puissances-exo.pdf

3_ie:
	pdflatex 4x3-puissances/4x3-puissances-ie.tex
	pdflatex 4x3-puissances/4x3-puissances-ie.tex
	mv 4x3-puissances-ie.pdf '$(PDFDIR)'/4x3-puissances-ie.pdf	

# Chapitre 4 - Pythagore

4_cours:
	pdflatex 4x4-pythagore/4x4-pythagore.tex
	pdflatex 4x4-pythagore/4x4-pythagore.tex
	mv 4x4-pythagore.pdf '$(PDFDIR)'/4x4-pythagore.pdf

4_ie:
	pdflatex 4x4-pythagore/4x4-pythagore-ie.tex
	pdflatex 4x4-pythagore/4x4-pythagore-ie.tex
	mv 4x4-pythagore-ie.pdf '$(PDFDIR)'/4x4-pythagore-ie.pdf

4_ie_short:
	pdflatex 4x4-pythagore/4x4-pythagore-ie-2.tex
	pdflatex 4x4-pythagore/4x4-pythagore-ie-2.tex
	mv 4x4-pythagore-ie-2.pdf '$(PDFDIR)'/4x4-pythagore-ie-2.pdf

4_ie_long:
	pdflatex 4x4-pythagore/4x4-pythagore-ie-3.tex
	pdflatex 4x4-pythagore/4x4-pythagore-ie-3.tex
	mv 4x4-pythagore-ie-3.pdf '$(PDFDIR)'/4x4-pythagore-ie-3.pdf


# Chapitre 5 - Expression litterale

5_eq:
	pdflatex 4x5-calcul-litteral-1/4x5-calcul-litteral-eq.tex
	pdflatex 4x5-calcul-litteral-1/4x5-calcul-litteral-eq.tex
	mv 4x5-calcul-litteral-eq.pdf '$(PDFDIR)'/4x5-calcul-litteral-eq.pdf


5_cours:
	pdflatex 4x5-calcul-litteral-1/4x5-calcul-litteral.tex
	pdflatex 4x5-calcul-litteral-1/4x5-calcul-litteral.tex
	mv 4x5-calcul-litteral.pdf '$(PDFDIR)'/4x5-calcul-litteral.pdf

5_pp:
	pdflatex 4x5-calcul-litteral-1/4x5-calcul-litteral-pp.tex
	pdflatex 4x5-calcul-litteral-1/4x5-calcul-litteral-pp.tex
	mv 4x5-calcul-litteral-pp.pdf '$(PDFDIR)'/4x5-calcul-litteral-pp.pdf


5_ns:
	pdflatex 4x5-calcul-litteral-1/4x5-calcul-litteral-ns.tex
	pdflatex 4x5-calcul-litteral-1/4x5-calcul-litteral-ns.tex
	mv 4x5-calcul-litteral-ns.pdf '$(PDFDIR)'/4x5-calcul-litteral-ns.pdf

5_sci:
	pdflatex 4x5-calcul-litteral-1/4x5-calcul-litteral-sci.tex
	pdflatex 4x5-calcul-litteral-1/4x5-calcul-litteral-sci.tex
	mv 4x5-calcul-litteral-sci.pdf '$(PDFDIR)'/4x5-calcul-litteral-sci.pdf

5_cs:
	pdflatex 4x5-calcul-litteral-1/4x5-calcul-litteral-cs.tex
	pdflatex 4x5-calcul-litteral-1/4x5-calcul-litteral-cs.tex
	mv 4x5-calcul-litteral-cs.pdf '$(PDFDIR)'/4x5-calcul-litteral-cs.pdf

4c1:
	pdflatex _continuite/4c1-continuite.tex 
	pdflatex _continuite/4c1-continuite.tex 
	mv 4c1-continuite.pdf '$(PDFDIR)'/4c1-continuite.pdf

4cc1:
	pdflatex _continuite/4c1-continuite-cor.tex 
	pdflatex _continuite/4c1-continuite-cor.tex 
	mv 4c1-continuite-cor.pdf '$(PDFDIR)'/4c1-continuite-cor.pdf

4c1-exc:
	latex _continuite/4c1-exc.tex
	dvips 4c1-exc.dvi
	ps2pdf 4c1-exc.ps
	
	mv 4c1-exc.pdf '$(PDFDIR)'/4c1-exc.pdf


4c2-exc:
	latex _continuite/4c2-exc.tex
	dvips 4c2-exc.dvi
	ps2pdf 4c2-exc.ps
	
	mv 4c2-exc.pdf '$(PDFDIR)'/4c2-exc.pdf

4c3-exc:
	pdflatex _continuite/4c3-exc.tex 
	pdflatex _continuite/4c3-exc.tex 	
	mv 4c3-exc.pdf '$(PDFDIR)'/4c3-exc.pdf		


# nettoyage		
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~