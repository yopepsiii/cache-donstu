FROM python:3.12-slim

# Рабочая директория
WORKDIR /usr/src/cacheDonstu/schedule-service

# Копирование зависимостей
COPY requirements.txt .

# Установка системных библиотек для сборки пакетов
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . .

# Установка переменной PYTHONPATH
ENV PYTHONPATH=/usr/src/cacheDonstu

CMD ["python3", "main.py"]
