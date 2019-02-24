FROM python:3.6

RUN apt-get -y update

# Create an user with the same uid/gid as the user running docker-compose in development to avid permissions conflicts
ARG uid=1000
ARG gid=1000
RUN addgroup --gid $gid python36
RUN useradd -m --uid $uid -g python36 python36

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /app
USER python36
