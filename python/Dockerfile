FROM python:3.9-slim

RUN apt-get update -y


WORKDIR /app


COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


COPY . .

RUN chmod +x /app/start.sh

# Specify the entrypoint script
ENTRYPOINT ["/app/start.sh"]
