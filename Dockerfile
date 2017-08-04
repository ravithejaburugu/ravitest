FROM alpine:3.6

RUN  easy_install pip \
  && pip install --upgrade pip \
  && if [[ ! -e /usr/bin/pip ]]; then ln -sf /usr/bin/pip3.4 /usr/bin/pip; fi


ADD . /dbPedia

WORKDIR /dbPedia

RUN pip install --default-timeout=100 -r requirements.txt


CMD ["python", “dbPedia.py"]
