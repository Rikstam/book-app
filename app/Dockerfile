# pull official base image
FROM python:3.10.1-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install pipenv netcat gcc postgresql \
    && apt-get clean

# install dependencies
COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv install --system --deploy

# add app
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
