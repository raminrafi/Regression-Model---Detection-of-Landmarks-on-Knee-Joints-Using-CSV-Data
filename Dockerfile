FROM python:3.6.9

RUN mkdir /code
WORKDIR /code
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt
CMD jupyter notebook
