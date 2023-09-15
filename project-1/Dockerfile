FROM python:3.11.5-bookworm

ENV VAR1=10

# Keeps python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTRHONBUFFERED=1

# Install and use pipenv
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy

WORKDIR /app
COPY . /app

# Creates a non-root user and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

EXPOSE 8000

# During debugging this entry point will be overriden
CMD ["uvicorn", "books:app", "--reload", "--host", "0.0.0.0"]