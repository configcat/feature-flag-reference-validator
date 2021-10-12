FROM python:3.9-alpine

RUN apk update
RUN apk add --no-cache the_silver_searcher

COPY . /ref-validator
WORKDIR /ref-validator

RUN pip install .

ENTRYPOINT ["configcat-validator.py"]