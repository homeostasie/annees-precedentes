# Dossiers
CODE := $(shell pwd)
PDFDIR = ../_pdf
THEME = nombres-et-calculs

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard sources/1/*.ipe sources/2/*.ipe )

FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/1/%.pdf: sources/1/%.ipe
	ipetoipe -pdf $<

sources/2/%.pdf: sources/2/%.ipe
	ipetoipe -pdf $<

# Cinquième
ie5-ch1:
	pdflatex tex/5ie_ch1_problemes-priorite-de-calcul-ie.tex
	pdflatex tex/5ie_ch1_problemes-priorite-de-calcul-ie.tex
	mv 5ie_ch1_problemes-priorite-de-calcul-ie.pdf '$(PDFDIR)'/5/5ie_ch1_problemes-priorite-de-calcul-ie.pdf

ie5-ch5:
	pdflatex tex/5ie_ch5_nombres-relatifs-ie-1.tex
	pdflatex tex/5ie_ch5_nombres-relatifs-ie-1.tex
	pdflatex tex/5ie_ch5_nombres-relatifs-ie-2.tex
	pdflatex tex/5ie_ch5_nombres-relatifs-ie-2.tex
	pdflatex tex/5ie_ch5_nombres-relatifs-ie-3.tex
	pdflatex tex/5ie_ch5_nombres-relatifs-ie-3.tex
	mv 5ie_ch5_nombres-relatifs-ie-1.pdf '$(PDFDIR)'/5/5ie_ch5_nombres-relatifs-ie-1.pdf
	mv 5ie_ch5_nombres-relatifs-ie-2.pdf '$(PDFDIR)'/5/5ie_ch5_nombres-relatifs-ie-2.pdf
	mv 5ie_ch5_nombres-relatifs-ie-3.pdf '$(PDFDIR)'/5/5ie_ch5_nombres-relatifs-ie-3.pdf


# Quatrième

ie4-ch1:
	pdflatex tex/4ie_ch1_nombres-relatifs-ie.tex
	pdflatex tex/4ie_ch1_nombres-relatifs-ie.tex
	mv 4ie_ch1_nombres-relatifs-ie.pdf '$(PDFDIR)'/4/4ie_ch1_nombres-relatifs-ie.pdf

ie4-ch4:
	pdflatex tex/4ie_ch4_fractions-ie.tex
	pdflatex tex/4ie_ch4_fractions-ie.tex
	mv 4ie_ch4_fractions-ie.pdf '$(PDFDIR)'/4/4ie_ch4_fractions-ie.pdf

ie4-ch5:
	pdflatex tex/4ie_ch5_puissance-ie-1.tex
	pdflatex tex/4ie_ch5_puissance-ie-1.tex
	pdflatex tex/4ie_ch5_puissance-ie-2.tex
	pdflatex tex/4ie_ch5_puissance-ie-2.tex
	mv 4ie_ch5_puissance-ie-1.pdf '$(PDFDIR)'/4/4ie_ch5_puissance-ie-1.pdf
	mv 4ie_ch5_puissance-ie-2.pdf '$(PDFDIR)'/4/4ie_ch5_puissance-ie-2.pdf



ie4-rat-ch5:
	pdflatex tex/4ie_ch5_puissance-ie-rat-1.tex
	pdflatex tex/4ie_ch5_puissance-ie-rat-1.tex
	pdflatex tex/4ie_ch5_puissance-ie-rat-2.tex
	pdflatex tex/4ie_ch5_puissance-ie-rat-2.tex
	mv 4ie_ch5_puissance-ie-rat-1.pdf '$(PDFDIR)'/4/4ie_ch5_puissance-ie-rat-1.pdf
	mv 4ie_ch5_puissance-ie-rat-2.pdf '$(PDFDIR)'/4/4ie_ch5_puissance-ie-rat-2.pdf

# Troisième
ex3-eq1-ch9:
	pdflatex tex/3ie_ch9_equation.tex
	pdflatex tex/3ie_ch9_equation.tex
	mv 3ie_ch9_equation.pdf '$(PDFDIR)'/3/3ie_ch9_equation.pdf	


# met


# nettoyage
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
