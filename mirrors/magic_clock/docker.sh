#!/usr/bin/env bash

docker run  -d \
--publish 80:8080 \
--restart always \
--env TZ=Europe\Stockholm \
--mount type=bind,src=`pwd`/config,dst=/opt/control_magic/config \
--mount type=bind,src=`pwd`/css/custom.css,dst=/opt/control_magic/css/custom.css \
--volume `pwd`/modules/iFrame:/opt/control_magic/modules/iFrame \
--volume `pwd`/modules/MMM-ip:/opt/control_magic/modules/MMM-ip \
--name mm \
bastilimbach/docker-magicmirror

