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
FIGSRC = $(wildcard sources/1/*.ipe sources/2/*.ipe sources/3/*.ipe sources/4/*.ipe sources/5/*.ipe sources/6/*.ipe sources/7/*.ipe)

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
	
sources/6/%.pdf: sources/6/%.ipe
	ipetoipe -pdf $<	

sources/7/%.pdf: sources/7/%.ipe
	ipetoipe -pdf $<	
		
# Cinquième

ie52:
	pdflatex tex/5ie_ch2_symetrie-ie.tex
	pdflatex tex/5ie_ch2_symetrie-ie.tex
	mv 5ie_ch2_symetrie-ie.pdf '$(PDFDIR)'/5/5ie_ch2_symetrie-ie.pdf	

ie54:
	pdflatex tex/5ie_ch4_triangles-ie.tex
	pdflatex tex/5ie_ch4_triangles-ie.tex
	mv 5ie_ch4_triangles-ie.pdf '$(PDFDIR)'/5/5ie_ch4_triangles-ie.pdf	

ie56:
	pdflatex tex/5ie_ch7_aire-perimetre-ie-1a.tex
	pdflatex tex/5ie_ch7_aire-perimetre-ie-1a.tex
	mv 5ie_ch7_aire-perimetre-ie-1a.pdf '$(PDFDIR)'/5/5ie_ch7_aire-perimetre-ie-1a.pdf	


# Quatrième

gr41:
	pdflatex tex/4ie_graph-1-dm.tex
	pdflatex tex/4ie_graph-1-dm.tex
	mv 4ie_graph-1-dm.pdf '$(PDFDIR)'/4/4dm_graph-1-dm.pdf	

ie42:
	pdflatex tex/4ie_ch2_pythagore-ie.tex
	pdflatex tex/4ie_ch2_pythagore-ie.tex
	mv 4ie_ch2_pythagore-ie.pdf '$(PDFDIR)'/4/4ie_ch2_pythagore-ie.pdf
	
	
ie46:
	pdflatex tex/4ie_ch6_trigonometrie-ie.tex
	pdflatex tex/4ie_ch6_trigonometrie-ie.tex
	mv 4ie_ch6_trigonometrie-ie.pdf '$(PDFDIR)'/4/4ie_ch6_trigonometrie-ie.pdf

ie462:
	pdflatex tex/4ie_ch6_trigonometrie-ie-2a.tex
	pdflatex tex/4ie_ch6_trigonometrie-ie-2a.tex
	mv 4ie_ch6_trigonometrie-ie-2a.pdf '$(PDFDIR)'/4/4ie_ch6_trigonometrie-ie-2a.pdf
	pdflatex tex/4ie_ch6_trigonometrie-ie-2b.tex
	pdflatex tex/4ie_ch6_trigonometrie-ie-2b.tex
	mv 4ie_ch6_trigonometrie-ie-2b.pdf '$(PDFDIR)'/4/4ie_ch6_trigonometrie-ie-2b.pdf
	

ie463:
	pdflatex tex/4ie_ch6_trigonometrie-ie-3a.tex
	pdflatex tex/4ie_ch6_trigonometrie-ie-3a.tex
	mv 4ie_ch6_trigonometrie-ie-3a.pdf '$(PDFDIR)'/4/4ie_ch6_trigonometrie-ie-3a.pdf
	pdflatex tex/4ie_ch6_trigonometrie-ie-3b.tex
	pdflatex tex/4ie_ch6_trigonometrie-ie-3b.tex
	mv 4ie_ch6_trigonometrie-ie-3b.pdf '$(PDFDIR)'/4/4ie_ch6_trigonometrie-ie-3b.pdf
		
dm44:
	pdflatex tex/4ie_ch4_rotation-dm.tex
	pdflatex tex/4ie_ch4_rotation-dm.tex
	mv 4ie_ch4_rotation-dm.pdf '$(PDFDIR)'/4/4dm_ch4_rotation-dm.pdf		

# Troisième

ie32:
	pdflatex tex/3ie_ch2_thales-ie.tex
	pdflatex tex/3ie_ch2_thales-ie.tex
	mv 3ie_ch2_thales-ie.pdf '$(PDFDIR)'/3/3ie_ch2_thales-ie.pdf	

ie36:
	pdflatex tex/3ie_ch6_trigonometrie-ie-1a.tex
	pdflatex tex/3ie_ch6_trigonometrie-ie-1a.tex
	mv 3ie_ch6_trigonometrie-ie-1a.pdf '$(PDFDIR)'/3/3ie_ch6_trigonometrie-ie-1a.pdf
# met


# nettoyage			
proper:
	rm -f *.log *.toc *.aux *.nav *.snm *.out *.bbl *.blg *.dvi
	rm -f *.backup *~
