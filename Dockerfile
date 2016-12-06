FROM dmodules/dmodules-django-docker:latest

ADD requirements.txt /localapp/
RUN pip install -r requirements.txt

COPY . /localapp

# collectstatic
# -------------
RUN DJANGO_MODE=build python manage.py collectstatic --noinput
#RUN DJANGO_MODE=build python manage.py migrate
