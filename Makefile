SOURCE:=README.md 1.md 2.md
F?=0
all:$(SOURCE:.md=.html)

%.html:%.md
	pandoc -o $@ $<
ifeq ($(F),0)
	w3m $@
endif

help:
	@echo "* this makefile is used for convert md files to html,and open the modified file with w3m "
	@echo "* when you don't want open html file,please use command like this:"
	@echo "* make F=1"
	@echo "* this way just convert md files to html"
	
clean:
	rm -rf *.html



.PHONY:clean help

