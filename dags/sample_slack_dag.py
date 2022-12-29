from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from utils.slack_op import on_failure
from airflow.operators.bash import BashOperator


# on_failure_callback에 on_failure 함수를 넣는다.
default_args = {
    'owner': 'airflow',
    'depends_on_past': True,
    'on_failure_callback': on_failure
}

dag = DAG(
    'sample_slack_dag',
    default_args=default_args,
    start_date = days_ago(1),
    schedule_interval='0 1 * * *',
)

# 항상 실패하도록 한다.
BashOperator(
	task_id="test",
	bash_command='exit(1)',
	dag=dag
)
