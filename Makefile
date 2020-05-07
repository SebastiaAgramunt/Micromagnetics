.SILENT:
.PHONY: init test
.DEFAULT_GOAL := help


PROJECT := Micromagnetics Simulation Software (Author Sebastia Agramunt)

COLOR_RESET = \033[0m
COLOR_COMMAND = \033[36m
COLOR_YELLOW = \033[33m
COLOR_GREEN = \033[32m
COLOR_RED = \033[31m


# Install all required packages (library and testing)
init:
	pip install -r requirements.txt
	pip install -r requirements.test.txt
	pip install -e .

## Make software tests
test:
	py.test -v
	#python -m unittest discover -v

## Coverage of testing
coverage:
	pytest --cov-fail-under=80 --cov=mmag test/

## Prints help message
help:
	printf "\n${COLOR_YELLOW}${PROJECT}\n-------------------------------------------------------------\n${COLOR_RESET}"
	awk '/^[a-zA-Z\-\_0-9\.%]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "${COLOR_COMMAND}$$ make %s${COLOR_RESET} %s\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST) | sort
	printf "\n"