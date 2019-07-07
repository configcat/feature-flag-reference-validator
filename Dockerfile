FROM python:3.7-alpine

RUN apk update
RUN apk add --no-cache the_silver_searcher
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["./main.py"]