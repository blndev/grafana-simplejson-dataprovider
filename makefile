# -----------------------------------------------------------------------------
# Author:  Daniel Bedarf
# Version: 1.0
# -----------------------------------------------------------------------------
# Basic makefile to handle python projects
# Support for dependency managament, build, test and more
# -----------------------------------------------------------------------------

# Configuration
# OUTPUT_BUILD = "build/"
# OUTPUT_BUILD_TESTRESULT = $(OUTPUT_BUILD) + "testresults.xml"

PYTHON=.env/bin/python # path to pyphon
PIP=.env/bin/pip # path to pip
SOURCE_ENV=. .env/bin/activate # shell within the environment

info: #check_env
	#TODO: create better output for help
	cat readme.md

check_env:
	$(SOURCE_ENV) ifndef VIRTUAL_ENV
		$(error "! You don't appear to be in a virtual environment.")
	endif


installEnv:
	python3 -m venv .env

installDependencies: installEnv
	$(SOURCE_ENV) && $(PIP) install . #install requirements defined in setup.py

install: installDependencies
	# there is a separate task fore dependencies and dev dependencies to use it for packaging 
	$(SOURCE_ENV) && $(PIP) install -e .[dev,test] # install development and testing packages

codestyle:
	$(SOURCE_ENV) && .env/bin/pylint src unittests
	$(SOURCE_ENV) && .env/bin/pycodestyle --statistics -qq --show-source src unittests

test:
	$(SOURCE_ENV) && .env/bin/py.test

testci: codestyle
	$(SOURCE_ENV) && .env/bin/py.test --junitxml=build/testresults.xml #$(OUTPUT_BUILD_TESTRESULT)
	$(SOURCE_ENV) && .env/bin/pylint --output-format=pylint2junit.JunitReporter src unittests > build/stylecheck.xml

start:
	$(SOURCE_ENV) && $(PYTHON) src/main.py 

startdebug: 
	$(SOURCE_ENV) && $(PYTHON) src/main.py --debug

ci: installDependencies testci
