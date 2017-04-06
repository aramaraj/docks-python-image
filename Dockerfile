FROM python:2.7
ADD . /PYTHON-TRACK-APP
WORKDIR /PYTHON-TRACK-APP
RUN pip install flask
RUN pip install web.py
RUN  pip install geocode

EXPOSE 5000
CMD [ "python", "./trackLocationFromWeb.py" ]
