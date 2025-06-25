FROM python:3.10.6-slim

WORKDIR /app

COPY src/ ./src/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar la app
CMD uvicorn src.api.api:app --host 0.0.0.0 --port $PORT