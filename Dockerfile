FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

LABEL org.opencontainers.image.source=https://github.com/adonm/homelab
LABEL org.opencontainers.image.description="Build a search index from some tagged urls"
LABEL org.opencontainers.image.licenses=Apache-2.0

# Copy the project into the image
ADD . /app

# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app
RUN ["uv", "sync", "--frozen"]

ENV PATH="/app/.venv/bin:$PATH"

CMD ["uv", "run", "build.py"]