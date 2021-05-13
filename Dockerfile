FROM python:3.6-alpine
RUN adduser -D myproj
WORKDIR /home/myproj
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./src/app.py ./
COPY ./src/worker.py ./


ENV FLASK_APP=app.py
RUN chown -R myproj:myproj ./
USER myproj

CMD flask run --host 0.0.0.0 --port 5057