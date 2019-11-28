FROM python:3.7-slim

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y vim git wget\
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN git clone https://github.com/mnxzyw/selenium_demo.git
WORKDIR /app/selenium_demo
RUN pip install -r requirements.txt

ENTRYPOINT dockerize -wait http://selenium:4444  python3 -m app