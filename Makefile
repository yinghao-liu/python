all:
	pandoc -o README.html README.md
	w3m README.html
clean:
	rm -rf *.html
.PHONY:all clean

