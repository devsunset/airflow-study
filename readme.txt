--------------------------------------------------------------------------------

			# AIRFLOW-WORK #

--------------------------------------------------------------------------------

########################################################
### AIRFLOW

https://airflow.apache.org/

https://github.com/apache/airflow

########################################################
### Reference


- sample
https://blog.si-analytics.ai/59 - sample_file_create_read_delete_drag.py
https://m.blog.naver.com/wideeyed/221565240108 - sample_bash_op_dag.py
https://m.blog.naver.com/wideeyed/221565276777 - sample_python_op_dag.py 



########################################################
### Airflow Guide

# Airflow
- Airflow is a platform created by the community to programmatically author, schedule and monitor workflows.  

# OverView
https://airflow.apache.org/docs/apache-airflow/stable/index.html

# Installation
https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html

# Airflow 구조
* Scheduler 		- Airflow의 DAG와 작업들을 모니터링하고 실행 순서와 상태 관리
* Workers에서		- Airflow의 작업을 실행하는 공간
* Metadata Database	- Airflow에서 실행할 작업에 관한 정보들을 저장
* Webserver 		- Airflow의 user interface 제공
* DAG directory 	- Airflow에서 실행할 작업들을 파이프라인 형태로 저장

Airflow는 Scheduler가 DAG directory의 작업을 가져와서 Workers에서 실행하는 형태

# DAG 
DAG는 비순환 그래프로써 순환하는 싸이클이 없는 그래프
노드와 노드가 단방향으로 연결되어 있어 그 노드로 향하게 되면 돌아오지 않는 특성
Airflow에서는 Task의 연결관계를 DAG로 관리하고, Webserver를 통해서도 DAG 구조를 시각적으로 확인

