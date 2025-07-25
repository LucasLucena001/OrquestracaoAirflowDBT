from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from datetime import datetime

@dag(start_date=datetime(2023, 1, 1), schedule=None, catchup=False, tags=["dbt"])
def dbt_ecommerce_dag():

    dbt_seed = BashOperator(
        task_id="dbt_seed",
        bash_command="cd /usr/local/airflow/include/dbteco && dbt seed --profiles-dir ."
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /usr/local/airflow/include/dbteco && dbt run --profiles-dir ."
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /usr/local/airflow/include/dbteco && dbt test --profiles-dir ."
    )

    dbt_seed >> dbt_run >> dbt_test

dbt_ecommerce_dag()
