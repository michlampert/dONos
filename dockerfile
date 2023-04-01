FROM python:3.10

ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install python3-dev default-libmysqlclient-dev build-essential -yq
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY backend /app
ENTRYPOINT ["python"]
CMD ["main.py"]
