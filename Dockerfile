FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pip3 install -r requirements.txt
RUN mkdir -p downloaded
RUN mkdir -p results
CMD python3 server.py






