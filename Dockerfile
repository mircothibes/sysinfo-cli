FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ARG USER=appuser
ARG UID=10001
RUN useradd -m -u ${UID} ${USER}

WORKDIR /app
COPY pyproject.toml README.md /app/
COPY src /app/src

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir .

USER ${USER}
ENTRYPOINT ["python", "-m", "sysinfo.cli"]
