# Dossiers
CODE := $(shell pwd)
PDFDIR = ../_pdf
THEME = 

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

# Cinquième

# Quatrième

# Troisième

ie4.1:
	pdflatex tex/4ie_ch4_puis_ie.1.tex
	pdflatex tex/4ie_ch4_puis_ie.1.tex
	mv 4ie_ch4_puis_ie.1.pdf '$(PDFDIR)'/eval/4ie_ch4_puis_ie.1.pdf
	pdflatex tex/4ie_ch4_puis_ie.2.tex
	pdflatex tex/4ie_ch4_puis_ie.2.tex
	mv 4ie_ch4_puis_ie.2.pdf '$(PDFDIR)'/eval/4ie_ch4_puis_ie.2.pdf	


ie3.1:
	pdflatex tex/3ie_arith-fonc.tex
	pdflatex tex/3ie_arith-fonc.tex
	mv 3ie_arith-fonc.pdf '$(PDFDIR)'/eval/3ie_arith-fonc.pdf

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
	rm -f tex/*.fls tex/*.aux 
