# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/app

# ENV SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

# ENV SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'

EXPOSE 8080

CMD ["python","app/run.py"]