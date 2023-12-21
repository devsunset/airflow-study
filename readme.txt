--------------------------------------------------------------------------------

			# AIRFLOW-STUDY #

--------------------------------------------------------------------------------

########################################################
### AIRFLOW

https://airflow.apache.org/

https://github.com/apache/airflow


########################################################
### Reference

https://github.com/tuanavu/airflow-tutorial/
https://github.com/jghoman/awesome-apache-airflow

- Tutorials 
https://blog.si-analytics.ai/59 - sample_file_create_read_delete_drag.py
https://m.blog.naver.com/wideeyed/221565240108 - sample_bash_op_dag.py
https://m.blog.naver.com/wideeyed/221565276777 - sample_python_op_dag.py 
https://www.comtec.kr/2021/08/09/airflow-tutorial/
https://www.comtec.kr/2021/08/11/airflow-operator-소개 
https://www.bucketplace.com/post/2021-04-13-2021-04-13-버킷플레이스-airflow-도입기/
https://www.bearpooh.com/tag/Airflow
https://data-engineer-tech.tistory.com/tag/airflow
https://dydwnsekd.tistory.com/category/BigData/Airflow?page=3
https://lsjsj92.tistory.com/tag/airflow


########################################################
### Airflow Guide

https://airflow.apache.org/

# OverView
https://airflow.apache.org/docs/apache-airflow/stable/index.html

Airflow is a platform created by the community to programmatically author, schedule and monitor workflows.  
Airflow는 Python 코드로 워크플로우(workflow)를 작성하고, 스케쥴링, 모니터링 하는 플랫폼 
Airflow를 통해서 데이터엔지니어링의 ETL 작업을 자동화하고, DAG(Directed Acyclic Graph) 형태의 워크플로우 
작성이 가능 이를 통해 더 정교한 dependency를 가진 파이프라인을 설정할 수 있음
AWS, GCP 모두 Airflow managed service를 제공할 정도로 전세계 데이터팀들에게 널리 사용되고 있으며 
그만큼 넓은 커뮤니티를 형성

Airflow의 특성
Dynamic : Airflow pipeline(동작순서, 방식)을 python을 이용해 구성하기 때문에 동적인 구성이 가능
Extensible : python을 이용해 Operator, executor을 사용해 사용자 환경에 맞게 확장 사용 가능
Elegant : 간결하고 명시적이며 jinja template를 이용해 parameter를 이용해 데이터를 전달하고 파이프라인을 생성하는 것이 가능
Scalable : 분산구조와 메세지큐를 이용해 scale out와 워커간 협업을 지원


# Quick Start
https://airflow.apache.org/docs/apache-airflow/stable/start.html

# Installation
https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html

# Tutorials
https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html

# How-to Guides
https://airflow.apache.org/docs/apache-airflow/stable/howto/index.html

# Airflow 구성 
https://airflow.apache.org/docs/apache-airflow/stable/concepts.html

	* Metadata Database	
	Airflow에서 실행할 작업에 관한 정보들을 저장
	작업 및 파이프라인의 메타데이터 저장소
	예를 들어 task status(queued, scheduled, running, success, failed, etc) 가 저장
	Airflow를 처음 다운로드하면 기본적으로 빠른 시작을 위해 SQLite 가 설치되는데,
	본격적으로 사용하기 위해선 mysql이나 postgres를 연결

	* Webserver 		
	Airflow의 user interface 제공

	* Scheduler 		
	Airflow의 DAG와 작업들을 모니터링하고 실행 순서와 상태 관리
	모든 작업과 DAG을 모니터링하다가 Metadatabase 내 모든 작업의 status를 모니터링
	특정 작업의 dependency가 만족되면 이를 실행시킬 뿐만 아니라, 이런 모든 작업의 실행 순서 또한 결정

		- Executor 
		스케쥴러와 함께 동작하는 구성요소 status가 queued인 태스크를 확인하며 
		실제 어떤 리소스가 투입되어 실행이 될 것인지를 결정
		흔히 쓰이는 것으로는 Local Executor, Celery Executor, Kubernetes Executor 등이 있음 

	* Workers		
	Airflow의 작업을 실행하는 공간
	실제 태스크를 수행하는 구성요소
	필요에 따라 Scale-out 되어 병렬 작업이나 동시에 여러 태스크를 진행
	Executor 및 airflow.cfg 에 의해 작업 환경 구성이 완성

	* DAG Directory 	
	Airflow에서는 Task의 연결관계를 DAG로 관리하고, Webserver를 통해서도 DAG 구조를 시각적으로 확인
	Airflow에서 실행할 작업들을 파이프라인 형태로 저장

# Airflow 용어 및 기본 개념
	* DAG (Directed Acyclic Graph)
	지향성 비순환 그래프 python으로 작성하고 순서를 정해 하나의 workflow형식으로 동작
	DAG는 아래와 같은 그림으로 표시할 수 있으며, 각 노드들은 task로 DAG가 실행되는 순서를 파악할 수 있음  

	* Task
	하나의 작업 단위를 Task라고 하며 하나 또는 여러 개의 Task를 이용해 하나의 DAG를 생성
	Task 간에는 순서를 지정할 수 있으며, <<, >>를 통해 간단하게 지정하는 것이 가능
	Task는 Operator로 만들 수 있으며, Python code를 실행시키기 위한 PythonOperator, 
	Bash command를 실행시키기 위한 BashOperator 등이 제공

	* Operator
	Operator은 Task를 만들기 위해 사용되는 Airflow class 
	제공된 Operator뿐만 아니라 Operator을 생성하는 것도 가능

	* Sensor
	Sensor은 Operator과 마찬가지로 하나의 Task로 사용할 수 있는데 특정 조건이 채워지기를 기다리면 
	조건을 만족하는 경우 이후 Task로 넘어가게 하는 역할

	* Pool
	Airflow는 동시성 제어를 위해 Pool이라는 기능도 제공하는데 이는 Web UI에서 제어하며
	Pool 안에서 지정된 슬롯 숫자만큼의 DAG만 동시에 실행 가능하도록 설정
	자원이 한정적인 cluster환경에서 우선순위가 떨어지는 DAG를 사용할 때 이용하면 자원 관리를 좀 더 효율적으로 할 수 있음

	* Xcom
	Xcom은 Airflow task간 데이터 전달을 위한 기능으로 push, pull 방식으로 데이터를 공유하는 기능을 말하는데
	주의할 점은 한 DAG안에서만 공유된다는 점이다 (다른 DAG 간 공통된 값을 이용하려는 경우에는 Variable를 사용)
	xcom_push, xcom_pull을 이용해 데이터를 전달하고 전달받는 방식이며 PythonOperator을 사용하는 경우에는
	return 값이 자동으로 Xcom에 push 된다
	Xcom에 대한 설명을 보고 DAG파일 안에서 데이터를 공유하는 것이 가능한데 Xcom이라는 기능이 왜 필요한지를 생각할 수 있는데,
	Airflow Worker을 여러 개 사용하는 경우 하나의 DAG가 동일한 Worker에서 동작하는 것을 보장할 수 없다
	예를 들어, DAG안에 t1, t2 task가 존재하는 경우 t1은 server1에서 동작하고, t2는 server2에서 동작하게 되면 task 간 
	데이터를 공유하기 위해 Xcom을 사용하는 방법밖에 없는 것이다.

	* Variable
	Variable는 위에서 언급한 것과 같이 Airflow에서 공통적으로 사용 가능한 변수들을 모아놓는 곳으로 Web UI에서 관리가 가능하다
	key-value의 형식으로 저장되어 있으며 보안을 위해 password, secret, passwd, authorization, api_key, apikey
	access_token 등의 키워드가 포함된 key를 가지는 경우 Web UI에서는 value가 보이지 않는 암호화된 key를 생성할 수 있다.

	* Connection
	Connecion은 외부 시스템과 연결하는 방식에 대한 정보를 저장해놓는 곳으로 Operator, Hook등에서 Connection의 정보를 사용한다.
	UI에서 설정이 가능하며, (Menu -> Admin -> Connections)에서 설정 및 수정 등이 가능
	인증을 위한 username, password에 대한 설정과 host에 대한 설정, 사용 Hook, Operator에 따라 추가 옵션도 설정할 수 있다

	* Hook
	Hook는 외부 플랫폼에 대한 인터페이스를 제공하는 것으로 Hive, S3, MySQL HDFS 등에 접근할 수 있는 
	다양한 Hook을 제공 Hook은 독립적으로 task가 될 수 없으며, Operator과 함께 사용된다.





