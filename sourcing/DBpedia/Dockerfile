FROM alpine:3.6


RUN apk --update add python py-pip gcc openssl ca-certificates py-openssl wget
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip 
     
ADD . /DBPedia

WORKDIR /DBPedia

RUN pip install -r requirements.txt

CMD ["python", “dbpedia.py"]
