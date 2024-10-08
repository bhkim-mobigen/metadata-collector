#!/bin/bash

source /home/otdev/ot_data_catalog_server/metadata_collector/venv/bin/activate

python3 /home/otdev/ot_data_catalog_server/metadata_collector/src/metadata_collector.py $1

deactivate