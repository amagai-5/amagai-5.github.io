PY := python3.10
PORT :=8000

view:
	@echo CHECK HERE ::: http://localhost:$(PORT)/ :::
	$(PY) -m http.server $(PORT)
pdf:
	$(PY) ./bin/gen-pdf.py

clean:
	rm -rf *pdf
