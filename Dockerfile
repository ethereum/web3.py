FROM python:3.6

# Set up code directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install Linux dependencies
RUN apt-get update && apt-get install -y libssl-dev

# Copy over requirements
COPY requirements-dev.txt .
# Install python dependencies
RUN pip install -r requirements-dev.txt

COPY web3 ./web3/
COPY tests ./tests/
COPY ens ./ens/

COPY setup.py .
COPY README.md .

RUN pip install -e .[tester]

WORKDIR /code
