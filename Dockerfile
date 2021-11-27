# Base image
From ubuntu:latest

# install dependencies.

RUN mkdir ./usr/dev
WORKDIR  ./usr/dev

RUN  apt-get update &&  apt-get -y upgrade


RUN echo Y|apt-get install python3
RUN apt-get install  -y python3-pip
RUN  pip3 install virtualenv
#RUN apt-get  install django

RUN  apt-get install -y libpq-dev
RUN  pip install psycopg2
RUN virtualenv venv
RUN chmod 755 ./venv/bin/activate 
RUN ./venv/bin/activate
RUN pip install django
RUN django-admin startproject mysite
#RUN export PYTHONPATH=$PYHONPATH:/usr/lib/python3.8

#WORKDIR  ./usr/dev/venv
COPY ./ ./
#RUN pip install --user  ./django-polls-0.1.tar.gz

# Run Default Command.

#RUN export PATH=$PATH:/usr/dev/venv/bin
CMD ["/usr/dev/venv/bin/python3" ,"./mysite/manage.py","runserver","0:8000"]
