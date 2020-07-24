.SILENT:
.DEFAULT_GOAL := list

AUTHOR := Sebastia Agramunt Puig
PROJECT := Micromagnetics Simulation Software (Author ${AUTHOR})

CODE_PATH=src

COLOR_RESET = \033[0m
COLOR_COMMAND = \033[36m
COLOR_YELLOW = \033[33m
COLOR_GREEN = \033[32m
COLOR_RED = \033[31m

.PHONY: bootstrap # : install all requirements needed
bootstrap:
	pip install --upgrade pip
	pip install -r ./pip-dep/requirements.txt
	pip install -r ./pip-dep/requirements.test.txt
	pip install -r ./pip-dep/requirements.notebook.txt
	pip install -e .


.PHONY: format # : check code format
format:
	autoflake --recursive --in-place $(CODE_PATH)
	black $(CODE_PATH)

.PHONY: test # : run software tests
test:
	py.test -v
	#python -m unittest discover -v

.PHONY: coverage # : check for coverage
coverage:
	pytest --cov-fail-under=80 --cov=mmag test/



.PHONY: list # : Makefile command list
list:
	printf "\n${COLOR_YELLOW}${PROJECT}\n-------------------------------------------------------------------\n${COLOR_RESET}"
	@grep '^.PHONY: .* #' Makefile | sed 's/\.PHONY: \(.*\) # \(.*\)/\1 \2/' | expand -t20
