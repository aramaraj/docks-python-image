FROM python:2.7
ADD trackLocationFromWeb.py /
RUN pip install flask
RUN pip install web.py
RUN  pip install geocode

EXPOSE 5000
CMD [ "python", "./trackLocationFromWeb.py" ]
