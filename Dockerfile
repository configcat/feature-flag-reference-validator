FROM alpine:3.8

RUN apk update
RUN apk add --no-cache the_silver_searcher
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["./main.py"]