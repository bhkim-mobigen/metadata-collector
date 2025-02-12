FROM python:3.8

WORKDIR /home/otdev/ot_data_catalog_server/metadata_collector

# PYTHONPATH 환경 변수 설정
ENV PYTHONPATH="/home/otdev/ot_data_catalog_server/metadata_collector/src:$PYTHONPATH"

COPY ./requirements.txt /home/otdev/ot_data_catalog_server/metadata_collector/requirements.txt
RUN pip install --no-cache-dir -r /home/otdev/ot_data_catalog_server/metadata_collector/requirements.txt

COPY .env /home/otdev/ot_data_catalog_server/metadata_collector/.env
COPY ./conf /home/otdev/ot_data_catalog_server/metadata_collector/conf
COPY ./src /home/otdev/ot_data_catalog_server/metadata_collector/src
COPY ./metadata_collector_main.py /home/otdev/ot_data_catalog_server/metadata_collector/metadata_collector_main.py

