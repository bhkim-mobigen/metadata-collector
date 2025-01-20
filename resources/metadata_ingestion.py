from datetime import datetime

from airflow import DAG
from airflow.decorators import task

from airflow.providers.ssh.operators.ssh import SSHOperator

from airflow.hooks.postgres_hook import PostgresHook

with DAG(dag_id="metadata_ingestion", start_date=datetime(2024, 8, 28), schedule="0 * * * *") as dag:

    @task()
    def get_command_list():
        hook = PostgresHook(postgres_conn_id='postgres-72')

        rows = hook.get_records("select system_id from tb_meta_system_info where collect_flag is true")

        command_list = []
        for row in rows:
            command_list.append(f"sh /home/otdev/ot_data_catalog_server/metadata_collector/bin/meta_data_collect.sh {row[0]}")

        return command_list

    command_list = get_command_list()

    ssh_task = SSHOperator.partial(task_id='run_ingestion', ssh_conn_id='otdev01-vm04',conn_timeout=60,
                                   cmd_timeout=None,
                                   environment={
                                       "KeepAlive":"yes"
                                   }).expand(
        command=command_list
    )