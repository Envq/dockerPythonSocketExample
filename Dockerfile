FROM ubuntu

RUN apt update
RUN apt install -y python3

RUN mkdir workspace
COPY *.py workspace/