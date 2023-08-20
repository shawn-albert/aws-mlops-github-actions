FROM python:${{ matrix.python-version }}

WORKDIR /app

COPY . .

RUN poetry install

CMD ["python", "your_script.py"]
