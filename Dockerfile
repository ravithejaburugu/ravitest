FROM alpine:3.6

RUN apk add --update python py-pip

RUN pip install -r requirements.txt

COPY dbpedia.py /src/dbpedia.py



CMD ["python", “dbPedia.py"]
