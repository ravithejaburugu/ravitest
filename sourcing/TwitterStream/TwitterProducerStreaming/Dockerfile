FROM alpine:3.6

RUN  apk add --no-cache --update bash && \
     apk add python py-pip gcc python-dev build-base g++ musl-dev tar ca-certificates openssl && \
     pip install --upgrade pip

ADD . /TWITTERPRODUCER

WORKDIR /TWITTERPRODUCER

RUN pip install -r requirements.txt

CMD ["/bin/bash", "-c", "source arguments.env && python TwitterProducerStreaming.py"]
