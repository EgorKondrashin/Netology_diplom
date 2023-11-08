FROM python:3.10.11

ENV SECRET_KEY UQWBDNOWHE&!@#*(*YU!@#YFyibjk1n38yo12fg3iuohb!*@#)ownfm
ENV DEBUG True
ENV ALLOWED_HOSTS 127.0.0.1
ENV DB_ENGINE django.db.backends.postgresql
ENV DB_NAME diplom_db
ENV DB_USER postgres
ENV DB_PASSWORD postgres123
ENV DB_HOST localhost
ENV DB_PORT 5431

ADD . /app/

WORKDIR /app/

RUN pip install -r requirements.txt

WORKDIR ./orders

CMD python manage.py makemigrations && \
    python manage.py migrate
