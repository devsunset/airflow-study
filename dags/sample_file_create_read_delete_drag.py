from airflow import models
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
 
default_args = {
                 'owner': 'root',
                         'depends_on_past': False,
                                 'start_date': datetime(2020, 2, 9),
                                         'retries': 1,
                                                 'retry_delay': timedelta(minutes=5)}
  
with models.DAG(
                 dag_id='sample_file_create_read_delete_dag', description='sample_file_create_read_delete_dag',
                         schedule_interval=None,
                                 max_active_runs=5,
                                         concurrency=10,
                                                 default_args=default_args) as dag:
      
        text_file_path = '/workspace/program/airflow/dags'
          
        #### create txt file  --> 텍스트 파일을 생성
        create_text_file_command = f'cd {text_file_path} && echo hello airflow > test.txt'
        create_text_file = BashOperator(
                                task_id='create_text_file',
                                        bash_command=create_text_file_command,
                                                        dag=dag)
                        
        #### cat txt file  --> 텍스트 파일을 읽습니다
        read_text_file_command = f'cd {text_file_path} && cat test.txt'
        read_text_file = BashOperator(
                        task_id='cat_text_file',
                                        bash_command=read_text_file_command,
                                                dag=dag)

        #### remove txt file  --> 텍스트 파일을 삭제
        remove_text_file_command = f'cd {text_file_path} && rm test.txt'
        remove_text_file = BashOperator(
                                task_id='remove_text_file',
                                        bash_command=remove_text_file_command,
                                                        dag=dag)
                
        create_text_file >> read_text_file >> remove_text_file 
