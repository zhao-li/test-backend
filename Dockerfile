FROM registry.access.redhat.com/ubi8/python-38 as development
ARG APP_DIR
WORKDIR ${APP_DIR}/

USER root
RUN rpm -ivh \
  https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN yum --nobest --assumeyes update && yum --allowerasing --assumeyes install \
    nc \
    ShellCheck \
  && yum clean all

COPY requirements*.txt ${APP_DIR}/
COPY scripts/install_dependencies.sh ${APP_DIR}/scripts/install_dependencies.sh
RUN scripts/install_dependencies.sh -e development

COPY . ${APP_DIR}


FROM registry.access.redhat.com/ubi8/ubi-minimal
ARG APP_DIR
ARG BIN_DIR=/usr/bin/
WORKDIR ${APP_DIR}/

RUN microdnf install \
    nc \
    python38.x86_64 \
  && microdnf clean all
RUN ln -s ${BIN_DIR}/python3 ${BIN_DIR}/python
RUN ln -s ${BIN_DIR}/pip3 ${BIN_DIR}/pip

COPY requirements*.txt ${APP_DIR}/
COPY scripts/install_dependencies.sh ${APP_DIR}/scripts/install_dependencies.sh
RUN scripts/install_dependencies.sh

# not sure why removing erros with: The transaction was empty
#RUN microdnf remove \
#    python38.x86_64 \
#  && microdnf clean all
#:end not sure why removing erros with: The transaction was empty

COPY . ${APP_DIR}

