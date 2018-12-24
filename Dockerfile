FROM docker.io/python:2.7.15-stretch

MAINTAINER  "daxwang@tencent.com"

ADD test-api.tar.gz /data/install/

RUN /data/install/test-api/bin/deploy.sh

EXPOSE 80
