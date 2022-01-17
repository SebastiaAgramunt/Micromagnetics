# Micromagnetics
A package for micromagnetism in python

<!-- ![Python Versions Supported](https://img.shields.io/badge/python-3.8+-blue.svg)
[![Pre-Commit](https://github.com/pablobd/algorithms/actions/workflows/pre-commit.yaml/badge.svg)](https://github.com/pablobd/algorithms/actions/workflows/pre-commit.yaml) -->

![Lisense](https://img.shields.io/github/license/sebastiaagramunt/micromagnetics)

## Install the package

To use as a package install like

```
pip install .
```

For development install interactive package
```
pip install -e .
```

## For deveopment

Create a virtual environment 

```
bash setup.sh
source venv/bin/activate
make bootstrap
```

## Run the notebooks

Use the ```DockerMakefile``` to make the build-run.

```
make -f DockerMakefile docker-build-run
```

stop and delete dockers and containers

```
make -f DockerMakefile docker-remove-all
```