FROM python:3.12
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
COPY main.py /app/
COPY data/ /app/data/
CMD ["python", "main.py"]
