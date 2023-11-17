FROM python:3.9

WORKDIR /code

COPY requirements.txt /code
RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . /code

EXPOSE 5000

WORKDIR /code/runners

CMD ["python", "run_0.py"]
