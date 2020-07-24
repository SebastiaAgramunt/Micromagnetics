#!/bin/sh

[ $# -eq 0 ] && { VENV_DIR=venv; }
[ $# -eq 1 ] && { VENV_DIR=$1; }


if [ ! -d "${VENV_DIR}" ]; then
  echo "creating virtual environment ${VENV_DIR}"
  python3 -m venv $VENV_DIR
else
  echo "${VENV_DIR} created previously"
fi

echo "activating virtual environment ${VENV_DIR}"
. $VENV_DIR/bin/activate



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
