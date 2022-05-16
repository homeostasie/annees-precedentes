# Dossiers
CODE := $(shell pwd)
PDFDIR = ../_pdf
THEME = grandeurs-et-mesures

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard src/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/%.pdf: src/%.ipe
	ipetoipe -pdf $<


# Cinquième

# Quatrième

# Troisième

# met

met:
	pdflatex tex/met-$(THEME).tex
	pdflatex tex/met-$(THEME).tex
	mv met-$(THEME).pdf '$(PDFDIR)'/met/met-$(THEME).pdf



# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
