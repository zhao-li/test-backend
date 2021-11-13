FROM registry.access.redhat.com/ubi8/python-38 as development
ARG APP_DIR=/usr/src/app/
WORKDIR ${APP_DIR}/

USER root
RUN rpm -ivh \
  https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
RUN yum --nobest --assumeyes update && yum --allowerasing --assumeyes install \
    nc \
  && yum clean all

COPY requirements*.txt ${APP_DIR}/
COPY scripts/install_dependencies.sh ${APP_DIR}/scripts/install_dependencies.sh
RUN pip install --upgrade pip
RUN scripts/install_dependencies.sh -e development

COPY . ${APP_DIR}


FROM registry.access.redhat.com/ubi8/python-38 as builder


FROM registry.access.redhat.com/ubi8/ubi-minimal as production
ARG APP_DIR=/usr/src/app/
ARG BIN_DIR=/usr/bin/
WORKDIR ${APP_DIR}/

RUN microdnf install \
    gcc \
    nc \
    postgresql-devel \
    postgresql-libs \
    python3 \
    python3-devel \
  && microdnf clean all
RUN ln -s ${BIN_DIR}/pip3 ${BIN_DIR}/pip

COPY requirements*.txt ${APP_DIR}/
COPY scripts/install_dependencies.sh ${APP_DIR}/scripts/install_dependencies.sh
RUN pip install --upgrade pip
RUN scripts/install_dependencies.sh

RUN microdnf remove \
    gcc \
    postgresql-devel \
    postgresql-libs \
    python3 \
    python3-devel \
  && microdnf clean all

COPY . ${APP_DIR}

