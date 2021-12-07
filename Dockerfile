# Specify base image 

FROM ubuntu:latest

# Install dependenies for application

RUN mkdir ./usr/dev
WORKDIR  ./usr/dev

RUN  apt-get update &&  apt-get -y upgrade
RUN echo Y|apt-get install python3
RUN apt-get install  -y python3-pip

RUN pip3 install virtualenv
RUN virtualenv myenv
RUN chmod 755 ./myenv/bin/activate
RUN $source ./myenv/bin/activate

#RUN pip install django
RUN  apt-get install -y libpq-dev
RUN  pip install psycopg2

WORKDIR ./django-polls/dist
COPY ./ ./
RUN python3 -m pip install --user ./django-polls-0.1.tar.gz

#EXPOSE 8080
# Run Default Command.


CMD ["python3","./mysite/manage.py","runserver","0:8000"]


