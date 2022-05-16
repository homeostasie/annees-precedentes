# Dossiers
CODE := $(shell pwd)
PDFDIR = pdf
CHAP = 3_puissances

# Visualiser les pdf
LOG=evince

# Créer le dossier pdf s'il n'éxiste pas.
target:
	test -d $(PDFDIR) || mkdir $(PDFDIR)

all: img poly proper

# Générations des images
FIGSRC = $(wildcard sources/1/*.ipe sources/2/*.ipe sources/3/*.ipe sources/4/*.ipe  sources/5/*.ipe)
FIGOBJ = $(FIGSRC:.ipe=.pdf)

img: $(FIGOBJ)

sources/1/%.pdf: sources/1/%.ipe
	ipetoipe -pdf $<
sources/2/%.pdf: sources/2/%.ipe
	ipetoipe -pdf $<
sources/3/%.pdf: sources/3/%.ipe
	ipetoipe -pdf $<
sources/4/%.pdf: sources/4/%.ipe
	ipetoipe -pdf $<
sources/5/%.pdf: sources/5/%.ipe
	ipetoipe -pdf $<

# interrogation écrite	

poly:
	pdflatex tex/$(CHAP).tex
	pdflatex tex/$(CHAP).tex
	mv $(CHAP).pdf '$(PDFDIR)'/$(CHAP)-poly.pdf	


pres:
	pdflatex tex/$(CHAP)-pres.tex
	pdflatex tex/$(CHAP)-pres.tex
	mv $(CHAP)-pres.pdf '$(PDFDIR)'/$(CHAP)-pres.pdf	

# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
