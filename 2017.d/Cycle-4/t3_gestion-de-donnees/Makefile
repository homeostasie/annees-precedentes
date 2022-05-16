# Dossiers
CODE := $(shell pwd)
PDFDIR = ../_pdf
THEME = 

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)
	test -d $(PDFDIR)/cours || mkdir $(PDFDIR)/cours
	test -d $(PDFDIR)/eval || mkdir $(PDFDIR)/eval

all: img poly proper

# Générations des images
FIGSRC = $(wildcard sources/ch1-organisation/*.ipe sources/2/*.ipe )

FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/ch1-organisation/%.pdf: sources/ch1-organisation/%.ipe
	ipetoipe -pdf $<

R:
	R -q --vanilla < sources/ch1-organisation/scripts/t3-ch1-cours-1.R

# Cinquième

# Quatrième

temperature:
	pdflatex tex/t4-data-temperature.tex
	pdflatex tex/t4-data-temperature.tex
	mv t4-data-temperature.pdf '$(PDFDIR)'/cours/t4-data-temperature.pdf	

# Troisième
3.1_observation:
	pdflatex tex/t3-ch1_etude-de-l-observation.tex
	pdflatex tex/t3-ch1_etude-de-l-observation.tex
	mv t3-ch1_etude-de-l-observation.pdf '$(PDFDIR)'/cours/t3-ch1_etude-de-l-observation.pdf	

ie3.1.1:
	pdflatex tex/t3-ch1_n3-ie1.tex
	pdflatex tex/t3-ch1_n3-ie1.tex
	mv t3-ch1_n3-ie1.pdf '$(PDFDIR)'/eval/t3-ch1_n3-ie1.pdf	



# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
