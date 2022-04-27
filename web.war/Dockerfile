FROM python:3.8-alpine
RUN mkdir /app
COPY . /app
COPY ./requirements.txt /web/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "-m", "web"]