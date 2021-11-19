FROM python:3-alpine
LABEL name="Logreader"
LABEL authors="mkrejza@gmail.com"
LABEL version="0.1.0"
RUN mkdir /logs
COPY crap.log /logs/
COPY logreader.py /
#RUN /sbin/useradd -D testuser
#USER testuser
CMD ["python", "logreader.py"]