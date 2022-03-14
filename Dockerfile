FROM python:3.9

# Set up code directory
WORKDIR /usr/src/app

# Install Linux dependencies
RUN apt-get update && apt-get install -y libssl-dev

COPY web3 ./web3/
COPY tests ./tests/
COPY ens ./ens/
COPY ethpm ./ethpm/

COPY setup.py .
COPY README.md .

RUN pip install -e .[dev]

WORKDIR /code
