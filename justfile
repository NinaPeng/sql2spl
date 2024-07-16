#!/usr/bin/env just --justfile

set shell := ["bash", "-uc"]

default: all

all : install black_format test build

install: 
	poetry install

test:
	poetry run pytest

black_format: install
	poetry run black -l 120 sql2spl && poetry run black -l 120 tests

build: install black_format
	rm -rf dist && poetry build -vvv

run: 
    poetry run python sql2spl/queryTranslator.py 