#!/bin/sh
if [ "$#" -ne 1 ]; then \
    echo "$0 requires exactly one argument." >&2 ; \
    echo "Usage: $0 venv_dir=VENV_DIR_DESTINATION" >&2 ; \
    exit 1 ; \
fi
venv_dir=$1
python3 -m venv $venv_dir
source $venv_dir/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
