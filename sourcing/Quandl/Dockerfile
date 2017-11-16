FROM alpine:3.6

RUN  apk add --no-cache --update bash && \
     apk add python py-pip gcc python-dev build-base g++ musl-dev tar ca-certificates openssl && \
     pip install --upgrade pip

ADD . /QUANDLFINDATA

WORKDIR /QUANDLFINDATA

RUN apk add python-dev curl gcc musl-dev libgcc openssl-dev

RUN pip install -r requirements.txt

CMD ["/bin/bash", "-c", "source arguments.env && python QuandlDataExtractor.py"]
