#!/usr/bin/env bash

cd ${HOME}/${MM_NAME}
export MIRROR=${PWD}
mkdir -p ${MIRROR}/modules &&

# Ip
cd ${MIRROR}/modules &&
git clone https://github.com/fewieden/MMM-ip.git &&

cd ${HOME}
