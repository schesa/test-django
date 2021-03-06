FROM python:3.7

RUN pip install django
RUN pip install Pillow
RUN pip install graphene_django

RUN mkdir /app
ADD . /app
WORKDIR /app

RUN python mysite/manage.py migrate

CMD ["python", "mysite/manage.py", "runserver", "0:8080"]