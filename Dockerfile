#base image
FROM python:3.8

# setup environment variable
ENV PYTHONUNBUFFERED 11
# set work directory
RUN mkdir -p $  DockerHOME

# where your code lives
WORKDIR /app


ADD . /app

COPY ./requirements.txt  /app/requirements.txt

RUN pip install -r requirements.txt


COPY . /app



