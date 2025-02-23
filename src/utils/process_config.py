from pydantic import BaseSettings
import os, sys
from dotenv import load_dotenv
import configparser


class Config(BaseSettings):

    system_name = "METADATA COLLECTOR"

    crypt_key: str

    sink_host: str
    sink_port: int

    metadata_manager_base_url: str
    get_meta_system_info_api: str
    set_meta_ingestion_status_api: str

    @classmethod
    def get_yaml(cls):
        # .env 파일 로드
        load_dotenv()

        config_file = os.getenv("METADATA_COLLECTOR_CONFIG_FILE")

        if config_file is None:
            print("env 에 프로세스 환경설정 파일을 설정하세요 [예: METADATA_COLLECTOR_CONFIG_FILE = config.ini]")
            sys.exit()

        config_data = configparser.ConfigParser()
        config_data.read(config_file)

        metadata_manager_api_config = config_data["metadata_manager.api"]

        sink_host = metadata_manager_api_config[host]
        sink_port = metadata_manager_api_config[port]

        metadata_manager_base_url = f"http://{metadata_manager_api_config['host']}:{metadata_manager_api_config['port']}{metadata_manager_api_config['prefix']}"
        get_meta_system_info_api = metadata_manager_api_config['get_meta_system_info_api']
        set_meta_ingestion_status_api = metadata_manager_api_config['set_meta_ingestion_status_api']


        return cls(
            crypt_key=config_data["security"]["cryptkey"],
            metadata_manager_base_url=metadata_manager_base_url,
            get_meta_system_info_api=get_meta_system_info_api,
            set_meta_ingestion_status_api = set_meta_ingestion_status_api
        )


config = Config.get_yaml()

