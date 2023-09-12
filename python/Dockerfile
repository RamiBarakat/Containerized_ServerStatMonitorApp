FROM python:3.9-slim

RUN apt-get update -y && apt-get -y install cron

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

RUN chmod +x /app/start.sh

COPY cronfile /etc/cron.d/cronfile
RUN chmod 0644 /etc/cron.d/cronfile
RUN crontab /etc/cron.d/cronfile


CMD ["cron", "-f"]
