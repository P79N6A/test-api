#!/usr/bin/env bash
#source env/bin/activate && exec supervisord -c etc/supervisord.conf

export RUN_MODE=PRODUCT
source env/bin/activate && gunicorn ap
i_server.wsgi:application -k gevent -w 4 --access-logfile  var/log/gunicorn-access.log --error-logfile var/log/gunicorn-error.log -p var/run/test-api.pid -b 0.0.0.0:2500 $@ -D