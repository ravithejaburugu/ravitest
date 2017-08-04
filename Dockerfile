FROM alpine:3.6

RUN apk add --update python py-pip



COPY dbpedia.py /src/dbpedia.py

COPY requirements.txt /src/requirements.txt

RUN pip install -r requirements.txt

CMD ["python", “dbPedia.py"]
