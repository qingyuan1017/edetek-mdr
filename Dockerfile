# syntax=docker/dockerfile:1

FROM python:3.7-slim-buster

RUN apt-get update \
    && apt-get -y install gcc \
    && apt-get -y install default-libmysqlclient-dev
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


COPY . .

ENV FLASK_APP=flaskr
ENV FLASK_ENV=development

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]