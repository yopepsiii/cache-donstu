FROM python:3.12-alpine

# Рабочая директория
WORKDIR /usr/src/cacheDonstu/schedule-service

# Копирование зависимостей
COPY requirements.txt .

# Установка системных библиотек для сборки пакетов
RUN apk add --no-cache gcc musl-dev linux-headers && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev linux-headers

# Копирование исходного кода
COPY . .

# Установка переменной PYTHONPATH
ENV PYTHONPATH=/usr/src/cacheDonstu

CMD ["python3", "main.py"]
