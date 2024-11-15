FROM mirror.gcr.io/library/python:3.12-slim as builder

WORKDIR /NewsParserService

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .

RUN pip install -r requirements.txt --target /install

FROM mirror.gcr.io/library/python:3.12-slim

WORKDIR /NewsParserService

COPY --from=builder /install /usr/local
COPY . .

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000", "--reload" ]
