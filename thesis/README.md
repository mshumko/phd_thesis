# README #

Start by looking a "main.tex" which is the main LaTeX document. main.tex loads 
the template and packages, creates the front matter, and calls other *.tex files
for each chapter.

You can compile the example document into a pdf using

        pdflatex main.tex
        bibtex main
        pdflatex main.tex
        pdflatex main.tex
If you have any questions or comments email Prof. Mark Owkes mark.owkes@montana.edu

Start with the Wiki: [https://bitbucket.org/markowkes/msu-latex/wiki/Home](https://bitbucket.org/markowkes/msu-latex/wiki/Home)

I (Mike Shumko) have added a makefile to this directory. This should help to 
compile/read the dissertation latex files.

- make one : compiles one_chapter.tex (can be changed in the makefile).
- make read_one : opens the evince pdf reader with the one chapter.
- make main : compiles main.tex with the included tex files in it
- make read_main : opens the evince pdf reader with whole dissertation.
- make clean : removed all latex related files except for the pdf and tex extensions.

one_chapter.tex is a dissertation template wrapper file for a file mentioned 
inside with the "\include{}" command. This greatly speeds up the compiling
and debugging time.
