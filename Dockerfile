FROM python:3.7.5

# Updating repository sources
RUN apt-get update

COPY ./pip-dep/requirements.txt /tmp/
COPY ./pip-dep/requirements.notebook.txt /tmp/
RUN pip install --upgrade pip
RUN pip install --requirement /tmp/requirements.txt
RUN pip install --requirement /tmp/requirements.notebook.txt

# Setting Working Directory
WORKDIR /home

# Launching Jupyter Notebook
# change token for more security
EXPOSE 8888
#CMD jupyter notebook --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token='' --NotebookApp.password=''
CMD jupyter lab --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token='' --NotebookApp.password=''
