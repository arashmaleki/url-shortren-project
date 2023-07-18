# define the global arguments
ARG PYTHON_VERSION=3.8

# base image
FROM python:${PYTHON_VERSION} as base

LABEL MAINTAINER "Arash Maleki <arashmaleki77>"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /src

# set work directory
COPY . /src/

RUN pip install --upgrade pip
RUN pip install -r /src/requirements.txt


ENTRYPOINT [ "./docker-init.sh" ]