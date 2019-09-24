FROM debian:sid-slim as base
RUN groupadd -g 1001 nvidia && useradd -r -u 1001 -g nvidia nvidia

WORKDIR /tmp

RUN set -ex \
    && apt-get -yq update \
    && apt-get install -yq --no-install-recommends --no-upgrade \
        pkg-config \
        python3 \ 
        python3-wheel \
        python3-pip \
        python3-setuptools \
        python3-cffi 

RUN set -ex && python3 --version
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
RUN set -ex \
    && pip3 install --upgrade pip wheel setuptools 

RUN set -ex \
    && apt-get update -yq \
    && apt-get install -yq \
        qt5-default \
        qml-module-* \
        qtdeclarative5-dev \
        python3-pyside2.*


# RUN set -ex \
#     && apt-get update -yq \
#     && apt-get install -yq python3-dev libdbus-glib-1-dev libdbus-1-dev build-essential 

COPY src /src
WORKDIR /src
RUN pip install -e ./