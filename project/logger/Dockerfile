# syntax=docker/dockerfile:1.4

FROM python:3.7-alpine

WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
RUN mkdir data
COPY . /app

ENTRYPOINT [ "python3" ]
CMD ["stats_logger.py"]
