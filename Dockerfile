FROM python:3.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD app/requirements.txt /code/
RUN pip install -v -r requirements.txt
ADD app/* /code/
