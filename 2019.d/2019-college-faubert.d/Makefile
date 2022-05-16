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



tp:
	pdflatex travail-personnel.tex
	pdflatex travail-personnel.tex
	
# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~