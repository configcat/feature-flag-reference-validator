FROM python:3.7-alpine

RUN apk update
RUN apk add --no-cache the_silver_searcher

RUN pip install .

COPY . /ref-validator
WORKDIR /ref-validator

ENTRYPOINT ["configcat-validator"]