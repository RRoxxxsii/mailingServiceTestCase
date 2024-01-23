FROM python:3.11.1

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

WORKDIR /service

COPY . .

RUN poetry install
