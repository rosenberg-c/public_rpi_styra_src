#!/usr/bin/env bash

MPATH="${HOME}/rpi_styra/mirrors/${NAME}"
MM_PATH="${HOME}/${MM_NAME}"

# Remove config & link
rm ${MM_PATH}/config/config.js &&
ln -s ${MPATH}/config/config.js ${MM_PATH}/config/config.js &&

# Remove custom css & link
rm ${MM_PATH}/css/custom.css
ln -s ${MPATH}/css/custom.css ${MM_PATH}/css/custom.css &&

# Create script start link
ln -s ${MPATH}/start.sh ${HOME}/${NAME}.sh

