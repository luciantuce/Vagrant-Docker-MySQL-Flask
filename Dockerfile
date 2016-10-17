FROM ubuntu:16.04

ENV LC_ALL=C

# Install required packages and remove the apt packages cache when done.
RUN apt-get update && apt-get install -y \
        python-pip \
        nginx \
  && pip install --upgrade pip
RUN pip install flask  && pip install flask-mysql && pip install uwsgi

# Create path for the application
RUN mkdir -p /var/www/app

# Copy nginx app config file
COPY app_nginx.conf /etc/nginx/sites-available/default

#Copy uwsgi parm file
COPY app_uwsgi.ini /var/www/app/

#Copy the app
COPY app.py /var/www/app/

# Copy the template
ADD templates /var/www/app/templates

EXPOSE 80
CMD /etc/init.d/nginx start && uwsgi --ini /var/www/app/app_uwsgi.ini