# Dossiers
CODE := $(shell pwd)
PDFDIR = pdf
CHAP = 3_puissances

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: target ie proper



# interrogation écrite	

ie:
	pdflatex tex/$(CHAP)-ie.tex
	pdflatex tex/$(CHAP)-ie.tex
	mv $(CHAP)-ie.pdf '$(PDFDIR)'/$(CHAP)-ie.pdf	

ie2:
	pdflatex tex/3_ie.tex
	pdflatex tex/3_ie.tex
	mv 3_ie.pdf '$(PDFDIR)'/3_ie.pdf	


balle:
	pdflatex tex/3_balle-rebond.tex
	pdflatex tex/3_balle-rebond.tex
	mv 3_balle-rebond.pdf '$(PDFDIR)'/3_balle-rebond.pdf	

met:
	pdflatex tex/3_met.tex
	pdflatex tex/3_met.tex
	mv 3_met.pdf '$(PDFDIR)'/3_met.pdf		

met2:
	pdflatex tex/3_met-2.tex
	pdflatex tex/3_met-2.tex
	mv 3_met-2.pdf '$(PDFDIR)'/3_met-2.pdf		


activite:
	pdflatex tex/3_activite.tex
	pdflatex tex/3_activite.tex
	mv 3_activite.pdf '$(PDFDIR)'/3_activite.pdf
# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
