
# start image
FROM python:3.9.13-slim

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the image exclding those listed in .dockerignore
COPY ./Labirinto ./

# create a virtual environment
RUN python -m venv ./env

# activate the virtual environment
ENV VIRTUAL_ENV /env
ENV PATH /usr/src/app/env/bin:$PATH

# update pip if needed
RUN pip install --upgrade pip

# install dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

##################################################################
# WARNING volumes to be mounted must be specified as absolute path
# in the form HOSTVOLUME:IMAGEVOLUME:ro/rw
##################################################################

# create mount points of input data and results
VOLUME /usr/src/app/Indata
VOLUME /usr/src/app/output

# run the command
CMD ["python", "./main.py"]
