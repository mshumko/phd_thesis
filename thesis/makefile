# A makefile utility to compile the entire dissertation or one chapter.

filename=one_chapter

one: ${filename}.tex # Dependency
	pdflatex ${filename}
	bibtex ${filename}
	pdflatex ${filename}
	pdflatex ${filename}
	
main: main.tex 
	pdflatex main
	bibtex main
	pdflatex main
	pdflatex main
	
read_one:
	evince ${filename}.pdf &
	
read_main:
	evince main.pdf &
	
clean:
	find -name "main*" -type f -not -name '*.tex' -not -name '*.pdf' -delete
	find -name "*.aux" -delete
	find -name "*.tex.bak" -delete
