FROM alpine:3.6

RUN  apk add --no-cache --update bash
RUN apk --update add python py-pip gcc openssl ca-certificates py-openssl wget
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip 
     
ADD . /DBPedia

WORKDIR /DBPedia

RUN pip install -r requirements.txt

RUN ["/bin/bash", "-c", "source arguments.env"]

CMD ["/bin/bash", "-c","source arguments.env && python dbpedia.py"]