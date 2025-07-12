FROM python:3.10.6-slim

ARG MODEL_TARGET
ENV MODEL_TARGET=$MODEL_TARGET

WORKDIR /app

COPY src/ ./src/
COPY models/ ./models/
COPY requirements.txt .

# ✅ Install system dependencies for LightGBM
RUN apt-get update && apt-get install -y libgomp1 && apt-get clean

RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar la app
CMD uvicorn src.api.api:app --host 0.0.0.0 --port $PORT