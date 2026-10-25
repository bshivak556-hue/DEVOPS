#!/usr/bin/env sh
# Experiment 6: Docker container/image commands. Destructive examples are commented.
set -eu
docker version
docker ps
docker ps -a
docker images
# docker run --name mycontainer -it ubuntu:22.04 /bin/bash
# docker start mycontainer
# docker stop mycontainer
# docker rm mycontainer
# docker pull ubuntu:22.04
# docker tag myimage YOUR_DOCKERHUB_USER/myimage:latest
# docker push YOUR_DOCKERHUB_USER/myimage:latest