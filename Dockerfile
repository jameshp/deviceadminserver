#Container for message creator conversion services

FROM google/dart-runtime

#install python as the server executs a python script
RUN apt-get update && apt-get install -yqq \
  python \
  python-pip

#install protobuf - currently message creator converison works only up to beta2
RUN pip install protobuf==3.0.0b2
