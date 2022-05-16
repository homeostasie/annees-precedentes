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
FIGSRC = $(wildcard sources/ch2-thm-pythagore/*.ipe sources/ch3-trigonometrie/*.ipe sources/ch5-thales/*.ipe )

FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/ch2-thm-pythagore/%.pdf: sources/ch2-thm-pythagore/%.ipe
	ipetoipe -pdf $<
	
sources/ch3-trigonometrie/%.pdf: sources/ch3-trigonometrie/%.ipe
	ipetoipe -pdf $<

sources/ch5-thales/%.pdf: sources/ch5-thales/%.ipe
	ipetoipe -pdf $<	
# Cinquième

# Quatrième
4.2_pythagore:
	pdflatex tex/t2-ch2_theoreme-de-pythagore.tex
	pdflatex tex/t2-ch2_theoreme-de-pythagore.tex
	mv t2-ch2_theoreme-de-pythagore.pdf '$(PDFDIR)'/cours/t2-ch2_theoreme-de-pythagore.pdf
	
ie-4.2-1:
	pdflatex tex/t2-ch2_pyt-ie1.tex
	pdflatex tex/t2-ch2_pyt-ie1.tex
	mv t2-ch2_pyt-ie1.pdf '$(PDFDIR)'/eval/t2-ch2_pyt-ie1.pdf
	
ie-4.3-1:
	pdflatex tex/t2-ch3-tri_ie1.tex
	pdflatex tex/t2-ch3-tri_ie1.tex
	mv t2-ch3-tri_ie1.pdf '$(PDFDIR)'/eval/t2-ch3-tri_ie1.pdf

ie-4.5-1:
	pdflatex tex/t2-ch5-thales_ie2.tex
	pdflatex tex/t2-ch5-thales_ie2.tex
	mv t2-ch5-thales_ie2.pdf '$(PDFDIR)'/eval/t2-ch5-thales_ie2.pdf	

# Troisième
ie-3.5-1:
	pdflatex tex/t2-ch5-thales_ie1.tex
	pdflatex tex/t2-ch5-thales_ie1.tex
	mv t2-ch5-thales_ie1.pdf '$(PDFDIR)'/eval/t2-ch5-thales_ie1.pdf

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
