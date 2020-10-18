FROM registry.access.redhat.com/ubi8/python-38 as development
ARG APP_DIR

USER root
RUN rpm -ivh \
  https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN yum --nobest --assumeyes update && yum --allowerasing --assumeyes install \
    nc \
    ShellCheck \
  && yum clean all

WORKDIR ${APP_DIR}/

COPY . ${APP_DIR}


FROM registry.access.redhat.com/ubi8/ubi-minimal
ARG APP_DIR

RUN microdnf install \
    nc \
  && microdnf clean all

WORKDIR ${APP_DIR}/

COPY . ${APP_DIR}
