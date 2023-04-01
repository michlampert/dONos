FROM python:3.10

ENV PYTHONUNBUFFERED=1
WORKDIR /backend
COPY requirements.txt /backend
RUN pip install -r requirements.txt

COPY backend /backend
ENTRYPOINT ["python"]
CMD ["app.py"]
