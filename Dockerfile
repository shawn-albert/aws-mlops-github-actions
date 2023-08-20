# Accept the Python version as a build argument
ARG PYTHON_VERSION

# Use the latest version of Ubuntu
FROM ubuntu:latest

# Install Python using the specified version
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get install -y python${PYTHON_VERSION} python${PYTHON_VERSION}-distutils python${PYTHON_VERSION}-dev && \
    apt-get clean

# Install pip
RUN apt-get install -y python3-pip

# Install poetry
RUN pip3 install poetry

# Create and set the working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install the project dependencies
RUN poetry install

# Command to run the application
CMD ["poetry", "run", "pytest"]
