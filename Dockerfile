# Construct our own image based on this one
FROM python:3.5

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

# It may be better to use our own image 
# with our requirements
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 4200

ENTRYPOINT ["uwsgi"]

CMD ["--ini", "server.ini"]