# python3 -m pip install apache-airflow-providers-slack
from airflow.operators.slack_operator import SlackAPIPostOperator
from dateutil.relativedelta import relativedelta

def on_failure(context):
	
    # 슬랙 채널명을 적는다.
    channel = 'your_channel_name'
    # 슬랙 토큰명을 적는다.
    token = 'your_slack_token'
    
    
    task_instance = context.get('task_instance')
    task_id = task_instance.task_id
    dag_id = task_instance.dag_id
    
    # 서버가 UTC 시간 기준일 경우 9시간을 더해준다.
    execution_date = (context.get('execution_date') + relativedelta(hours=9)).strftime('%Y-%m-%d %H:%M:%S')
    next_execution_date = (context.get('next_execution_date') + relativedelta(hours=9)).strftime('%Y-%m-%d %H:%M:%S')
    
    # 여기에 슬랙으로 보낼 메세지를 적는다.
    text = f'''
*[:exclamation: AIRFLOW ERROR REPORT]*
■ DAG: _{dag_id}_
■ Task: _{task_id}_
■ Execution Date (KST): _{execution_date}_
■ Next Execution Date (KST): _{next_execution_date}_'''

    # Slack Operator를 사용하여 메세지를 보내도록 한다.
    alert = SlackAPIPostOperator(
        task_id='slack_failed',
        channel=channel,
        token=token,
        text=text)
    return alert.execute(context=context)
