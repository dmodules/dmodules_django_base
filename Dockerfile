FROM dmodules/dmodules-django-docker

ADD requirements.txt /localapp/
RUN pip install -r requirements.txt

ADD . /localapp

# collectstatic
# -------------
RUN DJANGO_MODE=build python manage.py collectstatic --noinput
#RUN DJANGO_MODE=build python manage.py migrate
