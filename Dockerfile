FROM alpine:3.6



RUN  apk add --no-cache --update bash && \
     apk add python3 py-pip gcc python3-dev build-base g++ musl-dev tar ca-certificates openssl && \
     pip install --upgrade pip

ADD . /DBPedia

WORKDIR /DBPedia


RUN pip install -r requirements.txt

CMD ["python", “dbPedia.py"]
