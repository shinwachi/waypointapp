FROM python:2.7

# create uwsgi user in normal unix fashion
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip install Flask==0.10.1 flask-bootstrap==3.3.5.6 uWSGI==2.0.8 jupyter==1.0.0
WORKDIR /app

# copy the actual application folder
COPY app /app
# copy the application script to run the application
COPY cmd.sh /cmd.sh

EXPOSE 9090 9191 5757
# USER uwsgi

CMD ["bash", "/cmd.sh"]
