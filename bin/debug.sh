export RUN_MODE=PRODUCT
source env/bin/activate && exec python manage.py runserver $@
