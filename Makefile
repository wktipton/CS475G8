# Makefile

INPUT ?= nfa_input.txt

run:
	python3 main.py $(INPUT)

.DEFAULT_GOAL := run
