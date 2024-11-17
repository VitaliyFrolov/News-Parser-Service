FROM python:3.12-slim-bullseye AS builder

WORKDIR /NewsParserService

RUN apt-get update && \
  apt-get install -y --no-install-recommends gcc && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .

RUN python -m venv .venv
RUN . .venv/bin/activate && pip install -r requirements.txt

FROM python:3.12-slim-bullseye

WORKDIR /NewsParserService

COPY --from=builder /NewsParserService/.venv .venv
COPY . .

CMD [".venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000", "--reload"]