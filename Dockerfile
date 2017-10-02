FROM python:3.6

ENV WORKERS 4

ADD . /app

RUN pip3.6 install --no-cache-dir -r /app/requirements.txt

EXPOSE 80

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY service.py /app/service.py
COPY run.sh /app/run.sh

ENTRYPOINT ["/app/run.sh"]
