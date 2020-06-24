FROM httpd

RUN apt-get update && apt-get install -y \
    python3 python3-pip vim  \
    && apt-get clean

RUN mkdir /var/locust_test
ADD . /var/locust_test/
WORKDIR /var/locust_test
RUN ls

RUN pip3 install locustio