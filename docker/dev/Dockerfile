FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

WORKDIR /code

# install C dependences
# hadolint ignore=DL3008
RUN apt-get update && \
  apt-get -y --no-install-recommends install build-essential && \
  rm -rf /var/lib/apt/lists/*

# install python dependences
# install pip-tools and pip
# hadolint ignore=DL3013
RUN pip install --no-cache-dir -U pip-tools pip
COPY requirements requirements

# hadolint ignore=DL3042
RUN pip-compile -o ./requirements/requirements.txt ./requirements/requirements.in && \
  pip-compile -o ./requirements/dev-requirements.txt ./requirements/dev-requirements.in && \
  pip install --no-cache-dir --no-deps -r ./requirements/requirements.txt && \
  pip install --no-cache-dir --no-deps -r ./requirements/dev-requirements.txt

EXPOSE 8000
