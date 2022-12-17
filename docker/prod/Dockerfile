FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

WORKDIR /code

# install python dependences
# install pip-tools and pip
# hadolint ignore=DL3013
RUN pip install --no-cache-dir -U pip-tools pip
COPY requirements requirements

# hadolint ignore=DL3042
RUN pip-compile -o ./requirements/requirements.txt ./requirements/requirements.in && \
  pip install --no-cache-dir --no-deps -r ./requirements/requirements.txt

# entrypoint
COPY docker docker
ENTRYPOINT ["docker/dev/entrypoint.sh"]


EXPOSE 8000
