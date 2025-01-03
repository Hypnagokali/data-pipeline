# copied from:
FROM python: 3.13.1-bookworm

RUN mkdir -p /application/src
WORKDIR /application

COPY requirements.txt /application
COPY ./src /application/src

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "importer.py"]
