FROM alpine:3.6



RUN  apk add --update python py-pip --no-cache gcc
     

ADD . /DBPedia

WORKDIR /DBPedia


RUN pip install -r requirements.txt

CMD ["python", “dbPedia.py"]
