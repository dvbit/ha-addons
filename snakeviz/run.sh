#!/bin/sh

mkdir -p /share/snakeviz

exec snakeviz \
  --hostname 0.0.0.0 \
  --port 8080 \
  --server \
  /share/snakeviz
