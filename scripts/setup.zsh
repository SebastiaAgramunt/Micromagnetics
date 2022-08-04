#!/bin/zsh

source ~/.zshrc


PYTHON_VERSION=3.9.10

# check if pyenv is installed
if [[ -z "${PYENV_ROOT}" ]]; then
  echo "PYENV_ROOT not found, maybe pyenv is not installed or variable is not initialized"
  echo "Exiting..."
  exit 1
fi

# check python version installation
if [[ ! -d "${PYENV_ROOT}/versions/${PYTHON_VERSION}" ]]; then
  echo "\U274C Python ${PYTHON_VERSION} not installed, installing"
  pyenv install -f ${PYTHON_VERSION}
else
  echo "\U2705 Python ${PYTHON_VERSION} already installed"
fi

# set shell python version for this script
pyenv shell ${PYTHON_VERSION}

# set poetry to create environment in this directory
# under .venv folder
poetry config virtualenvs.in-project true;

# remove previous virtual environment (if any)
rm -rf .venv

# create environment and install 
poetry install

if [[ $? -eq 0 ]]; then
  echo "\n\n\U2705 Envionment installed successfully"
else
  echo "\n\n\U274C Couldn't install environment, check logs"
  exit 1  
fi

echo "\n\n\U25CC Activate environment:\n\n\tsource .venv/bin/activate\n"
echo "\U25CC Deactivate environment:\n\n\tsource deactivate\n"
echo "\U25CC Remove environment:\n\n\trm -rf .venv\n"


# [ $# -eq 0 ] && { VENV_DIR=venv; }
# [ $# -eq 1 ] && { VENV_DIR=$1; }


# if [ ! -d "${VENV_DIR}" ]; then
#   echo "creating virtual environment ${VENV_DIR}"
#   python3 -m venv $VENV_DIR
# else
#   echo "${VENV_DIR} created previously"
# fi

# echo "activating virtual environment ${VENV_DIR}"
# . $VENV_DIR/bin/activate



# if [ "$#" -ne 1 ]; then \
#     echo "$0 requires exactly one argument." >&2 ; \
#     echo "Usage: $0 venv_dir=VENV_DIR_DESTINATION" >&2 ; \
#     exit 1 ; \
# fi
# venv_dir=$1
# python3 -m venv $venv_dir
# source $venv_dir/bin/activate
# pip3 install --upgrade pip
# pip3 install -r requirements.txt
