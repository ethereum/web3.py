FROM python:3.9

# Set up code directory
WORKDIR /usr/src/app

# Install Linux dependencies
RUN apt-get update && apt-get install -y libssl-dev

COPY web3 ./web3/
COPY tests ./tests/
COPY ens ./ens/
COPY ethpm ./ethpm/

COPY poetry.lock pyproject.toml ./
COPY README.md .

# Install Poetry & Install dependencies
RUN	curl -sSL https://install.python-poetry.org | python3 - --version 1.6.1
RUN /root/.local/bin/poetry install --no-interaction --no-ansi --no-root --extras "dev"

WORKDIR /code
