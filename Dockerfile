FROM python:3.10.11-slim-bullseye

WORKDIR /app 

COPY req.txt .

COPY app .

RUN pip install -r req.txt

CMD [ "python3", "main.py" ]
