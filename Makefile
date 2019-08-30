SHELL := /bin/sh


format:
	@black backend

sort:
	@isort