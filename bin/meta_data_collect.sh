#!/bin/bash

source /home/otdev/ot_data_catalog_server/metadata_collector/venv/bin/activate

export PYTHONPATH=${PYTHONPATH}:/home/otdev/ot_data_catalog_server/metadata_collector/src

python3 /home/otdev/ot_data_catalog_server/metadata_collector/metadata_collector_main.py $1

deactivate