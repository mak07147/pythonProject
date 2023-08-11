FROM ubuntu:latest
LABEL authors="anduser"

ENTRYPOINT ["top", "-b"]