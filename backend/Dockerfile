ARG PYTHON_VERSION=3.10-slim-buster

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

# RUN python3 -m venv env

COPY requirements.txt /tmp/requirements.txt

RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY . /code/

RUN python manage.py collectstatic --noinput

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

EXPOSE 8000

# replace demo.wsgi with <project_name>.wsgi
# CMD env/bin/activate && exec python myapp.py
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "backend.wsgi"]

