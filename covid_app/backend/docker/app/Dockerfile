FROM python:3.8.5-slim-buster

# update & install
RUN apt-get update && \
    apt-get -y --with-new-pkgs upgrade

RUN apt-get install -y \
    build-essential libgomp1 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# env
ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

# install python requirements
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir -U pip setuptools

# get app
RUN mkdir /app
WORKDIR /app
COPY /app /app
RUN /opt/venv/bin/pip install -r /app/requirements.txt

ENV PATH="/opt/venv/bin:$PATH"
