FROM python:3.7-slim

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y vim git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/mnxzyw/selenium_demo.git
WORKDIR /app/selenium_demo
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "-m", "app"]