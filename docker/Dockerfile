FROM python:3.8

WORKDIR /home/otdev/ot_data_catalog_server/metadata_collector

# PYTHONPATH 환경 변수 설정
ENV PYTHONPATH="/home/otdev/ot_data_catalog_server/metadata_collector/src:$PYTHONPATH"

# 시스템 의존성 설치
#RUN yum -y groupinstall "Development Tools" && \
#    yum -y install libcouchbase-devel cyrus-sasl-devel && \
#    yum clean all

#RUN apt-get update && \
#    apt-get install -y \
#    build-essential \
#    libcouchbase-dev \
#    libsasl2-dev && \
#    rm -rf /var/lib/apt/lists/*

RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get libcouchbase-dev
RUN apt-get libsasl2-dev
RUN rm -rf /var/lib/apt/lists/*

# Python 의존성 설치
RUN pip install --upgrade pip setuptools wheel

COPY ./requirements.txt /home/otdev/ot_data_catalog_server/metadata_collector/requirements.txt
RUN pip install --no-cache-dir -r /home/otdev/ot_data_catalog_server/metadata_collector/requirements.txt

COPY .env /home/otdev/ot_data_catalog_server/metadata_collector/.env
COPY ./conf /home/otdev/ot_data_catalog_server/metadata_collector/conf
COPY ./src /home/otdev/ot_data_catalog_server/metadata_collector/src
COPY ./metadata_collector_main.py /home/otdev/ot_data_catalog_server/metadata_collector/metadata_collector_main.py

CMD ["tail", "-f", "/dev/null"]