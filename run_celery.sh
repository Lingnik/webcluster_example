#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

# run Celery worker for our project webcluster with Celery configuration stored in Celeryconf
echo "Launching celery worker."
su -m myuser -c "celery worker -A webcluster.celeryconf -Q default -n default@%h"
