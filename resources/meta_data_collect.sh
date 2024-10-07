#!/bin/bash

source /home/otdev/ot_data_catalog_svr/venv/bin/activate

python3 /home/otdev/ot_data_catalog_svr/src/metadata_ingestion.py $1

deactivate


