# Micromagnetics
A package for micromagnetism in python


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