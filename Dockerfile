FROM python:3.6

# Set up code directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install Linux dependencies
RUN apt-get update && apt-get install -y libssl-dev

# Copy over requirements
COPY setup.py .
COPY README.md .
COPY requirements-dev.txt .

# Install python dependencies
RUN pip install -r requirements-dev.txt
RUN pip install -e .

WORKDIR /code
