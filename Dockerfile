FROM python:3.6
SHELL [ "/bin/bash", "-c" ]
# proxy settings
ARG PROXY
ENV http_proxy=${PROXY}
ENV https_proxy=${PROXY}
ENV PIP_PROXY=${PROXY}

RUN apt-get update && apt-get install -y \
  nano \
  python-dev \
  python-pip \
  libxml2-dev \
  libxslt1-dev \
  zlib1g-dev \
  libffi-dev \
  libssl-dev \
  python3 \
  python3-dev

RUN mkdir -p /opt/services/collector/src && mkdir -p /etc/scrapyd/conf.d
WORKDIR /opt/services/collector/src
COPY Pipfile Pipfile.lock /opt/services/collector/src/
COPY ./scrapyd/scrapyd.conf /etc/scrapyd/conf.d/scrapyd.conf

# install our dependencies
RUN pip install --upgrade pip && \
  pip install pipenv && \
  pipenv install --system

# copy our project code
COPY . /opt/services/collector/src

EXPOSE 6800

# Set bash monitor mode on; run server on the background, deploy eggs, get server to the foreground again.
CMD set -m; scrapyd & cd ali && scrapyd-deploy && cd .. & fg scrapyd
#CMD scrapyd