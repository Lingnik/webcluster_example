
# webcluster_example
An example docker composition running Django 1.10 on Python 3.6.0 in a pyenv-virtualenv, celery, RabbitMQ, Redis, and Postgresql.

## References
This project was inspired by [Syncano's post](https://www.syncano.io/blog/configuring-running-django-celery-docker-containers-pt-1/) on running Django+Celery on docker containers.

## Using
1. `docker-compose build`
2. `docker-compose up`
3. Point your browser to http://localhost:8000/ and try POSTing a job.
4. Click the link to the job you ran and check that it succeeded.
