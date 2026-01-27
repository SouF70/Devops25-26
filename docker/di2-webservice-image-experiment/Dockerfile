FROM python:3.8-slim

WORKDIR /home/webservice

RUN pip install flask --no-cache-dir --progress-bar off

COPY ./static /home/webservice/static
COPY ./templates /home/webservice/templates
COPY webservice_app.py /home/webservice/

EXPOSE 5050

CMD ["python3", "webservice_app.py"]