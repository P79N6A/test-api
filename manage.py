#!/usr/bin/env python
import sys

import os


if __name__ == "__main__":

    if 'runserver' == sys.argv[1]:
        from gevent import monkey
        monkey.patch_all()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_server.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
