# Dossiers
CODE := $(shell pwd)
PDFDIR = pdf
CHAP = 2_fractions

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard sources/dm1/*.ipe sources/*.ipe sources/3/*.ipe )
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/dm1/%.pdf: sources/dm1/%.ipe
	ipetoipe -pdf $<
sources/%.pdf: sources/%.ipe
	ipetoipe -pdf $<
sources/3/%.pdf: sources/3/%.ipe
	ipetoipe -pdf $<

# interrogation écrite	

dm1-vit-pourc-pyt:
	pdflatex tex/dm1-vit-pour-pyt.tex
	pdflatex tex/dm1-vit-pour-pyt.tex
	mv dm1-vit-pour-pyt.pdf '$(PDFDIR)'/dm1-vit-pour-pyt.pdf	

dc1:
	pdflatex tex/dc1.tex
	pdflatex tex/dc1.tex
	mv dc1.pdf '$(PDFDIR)'/dc1.pdf

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
