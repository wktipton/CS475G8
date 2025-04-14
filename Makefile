# Disable default run behavior
.DEFAULT_GOAL := help

# Rule shown when you run just `make`
help:
	@echo "Usage: make <testname>.txt"
	@echo ""
	@echo "Available tests:"
	@ls tests/*.txt | xargs -n 1 basename

# Run a specific test with `make filename.txt`
%.txt:
	python3 main.py tests/$@

# List tests manually
list:
	@echo "Available tests:"
	ls tests/*.txt | xargs -n 1 basename
