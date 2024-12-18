FROM python:3.12-slim

WORKDIR /usr/src/cacheDonstu/api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/usr/src/cacheDonstu

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]