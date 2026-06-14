FROM python:3.12-slim

WORKDIR /app

COPY local/ .
COPY .env .

RUN pip install requests python-dotenv psycopg2-binary boto3

CMD ["python", "run_pipeline.py"]