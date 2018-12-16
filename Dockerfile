FROM debian:stable

MAINTAINER Filip Cima <filip.cima@gmail.com>

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y python3-pip

RUN pip3 install eve flask

RUN mkdir -p /api

COPY src /api
RUN chmod +x /api/app.py

EXPOSE 5000

CMD python3 api/app.py
