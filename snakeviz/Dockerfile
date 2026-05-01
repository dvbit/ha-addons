ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-pip \
  && pip3 install --no-cache-dir --break-system-packages snakeviz

COPY main.py /usr/lib/python3.12/site-packages/snakeviz/main.py
COPY run.sh /init
RUN chmod a+x /init
