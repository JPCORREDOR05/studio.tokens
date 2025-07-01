FROM python:3.10-slim
WORKDIR /app
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/app ./app
COPY backend/entrypoint.sh /entrypoint.sh
COPY .env.example /app/.env
ENTRYPOINT ["/entrypoint.sh"]
