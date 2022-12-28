--------------------------------------------------------------------------------

			# AIRFLOW-WORK #

--------------------------------------------------------------------------------

########################################################
### AIRFLOW

https://airflow.apache.org/

https://github.com/apache/airflow


########################################################
### Reference

https://github.com/tuanavu/airflow-tutorial/
https://github.com/jghoman/awesome-apache-airflow

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
---------------------------------------------------------
* Metadata Database	
- Airflow에서 실행할 작업에 관한 정보들을 저장
작업 및 파이프라인의 메타데이터 저장소
예를 들어 task status(queued, scheduled, running, success, failed, etc) 가 저장
Airflow를 처음 다운로드하면 기본적으로 빠른 시작을 위해 SQLite 가 설치되는데,
본격적으로 사용하기 위해선 mysql이나 postgres를 연결

* Webserver 		
- Airflow의 user interface 제공

* Scheduler 		
- Airflow의 DAG와 작업들을 모니터링하고 실행 순서와 상태 관리
모든 작업과 DAG을 모니터링하다가 Metadatabase 내 모든 작업의 status를 모니터링
특정 작업의 dependency가 만족되면 이를 실행시킬 뿐만 아니라, 이런 모든 작업의 실행 순서 또한 결정
•  Executor - 스케쥴러와 함께 동작하는 구성요소 status가 queued인 태스크를 확인하며 
   실제 어떤 리소스가 투입되어 실행이 될 것인지를 결정
   흔히 쓰이는 것으로는 Local Executor, Celery Executor, Kubernetes Executor 등이 있음 

* Workers		
- Airflow의 작업을 실행하는 공간
실제 태스크를 수행하는 구성요소
필요에 따라 Scale-out 되어 병렬 작업이나 동시에 여러 태스크를 진행
Executor 및 airflow.cfg 에 의해 작업 환경 구성이 완성

* DAG 
DAG: Directed Acyclic Graph의 약자로 비순환 방향 그래프를 의미
그래프 구조에 기반한 데이터 탐색 알고리즘 주로 작업(TASK)의 우선순위/순서를 표현하기 위한 용도로 사용
DAG는 비순환 그래프로써 순환하는 싸이클이 없는 그래프
노드와 노드가 단방향으로 연결되어 있어 그 노드로 향하게 되면 돌아오지 않는 특성
Airflow에서는 Task의 연결관계를 DAG로 관리하고, Webserver를 통해서도 DAG 구조를 시각적으로 확인
Airflow에서 실행할 작업들을 파이프라인 형태로 저장
---------------------------------------------------------


Airflow는 Scheduler가 DAG directory의 작업을 가져와서 Workers에서 실행하는 형태



