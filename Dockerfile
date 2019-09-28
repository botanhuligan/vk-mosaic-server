FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p downloaded
RUN mkdir -p results
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pip3 install -r requirements.txt
CMD python3 server.py






