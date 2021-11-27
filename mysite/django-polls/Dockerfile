# Specify base image 

FROM python:alpine

# Install dependenies for application
WORKDIR ./django-polls/dist

COPY ./ ./

RUN python -m pip install Django
RUN python -m pip install --user ./dist/django-polls-0.1.tar.gz
RUn django-admin startproject mysite
#RUN python -m pip install Pillow


# Run Default Command.

CMD ["python" ,"./mysite/manage.py","runserver"]
