# Dossiers
CODE := $(shell pwd)
PDFDIR = ../_pdf
THEME = espace-et-geometrie

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard sources/1/*.ipe)

FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/1/%.pdf: sources/1/%.ipe
	ipetoipe -pdf $<



# 1 - Géométrie plane
1gp:
	pdflatex tex/geometrie-plane-cycle-3.tex
	pdflatex tex/geometrie-plane-cycle-3.tex
	mv geometrie-plane-cycle-3.pdf '$(PDFDIR)'/6ie_3eg_geometrie-plane-cycle-3.pdf



# nettoyage
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f tex/*.log tex/*.toc tex/*.aux tex/*.nav tex/*.snm tex/*.out tex/*.bbl tex/*.blg tex/*.dvi
	rm -f *.backup *~
