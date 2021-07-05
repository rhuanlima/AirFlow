from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from textwrap import dedent

default_args = {
   'owner': 'rhuan_lima',
   'depends_on_past': False,
   'start_date': datetime(2021, 1, 1),
   'retries': 0,
   }

with DAG(
   'dag-001',
   schedule_interval=timedelta(minutes=1),
   catchup=False,
   default_args=default_args
   ) as dag:
   t1 = BashOperator(
      task_id='print_date',
      bash_command='date',
   )
   t2 = BashOperator(
      task_id='first_etl',
      bash_command="""
      cd $AIRFLOW_HOME/dags/etl_scripts/
      python3 py1.py
      """)
   t3 = BashOperator(
      task_id='second_etl',
      bash_command="""
      cd $AIRFLOW_HOME/dags/etl_scripts/
      python3 py2.py
      """)
   t1.doc_md = dedent("""\
   # Documentação da Task
   Voce pode usar a tag doc_md para passar uma documentação em `Markdow` para o airflow

   """
   )
   t1 >> t2 >> t3