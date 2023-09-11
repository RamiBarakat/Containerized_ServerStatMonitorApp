FROM python:3.9-slim

RUN apt-get update -y


WORKDIR /app


COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


COPY . .

RUN chmod +x /app/start.sh

#ENV user=root password=root host=mysql port=3306 database=db

#ENTRYPOINT ["/app/start.sh"]
