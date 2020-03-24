FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /twitter_container
WORKDIR /twitter_container
ADD . /twitter_container
RUN pip install -r requirements.txt
EXPOSE 8000



