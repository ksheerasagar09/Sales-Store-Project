"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime, timedelta, date
from dataclean import csv_cleaner


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2019, 12,26),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(seconds = 10),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

today = date.today()

dag = DAG("Store_Project", default_args = default_args, schedule_interval = '@daily', catchup=False, template_searchpath = ["/usr/local/airflow/sql_files/"])

t1 = BashOperator(task_id = 'CheckFile', bash_command="shasum ~/store_files_airflow/raw_store_transactions.csv",retries = 2,
    retry_delay = timedelta(seconds = 15), dag=dag)

t2 = PythonOperator(task_id = 'CleanFile', python_callable=csv_cleaner, dag=dag)

t3 = MySqlOperator(task_id = 'CreateTables', mysql_conn_id = "MySql_Conn", sql = "CreateTable.sql",dag=dag)

t4 = MySqlOperator(task_id = "InsertData", mysql_conn_id = "MySql_Conn" , sql = "LoadData.sql",dag=dag)

t5 = MySqlOperator(task_id = "AggregateData", mysql_conn_id = "MySql_Conn", sql = "AggregateData.sql",dag=dag)

t6 = BashOperator(task_id = 'RenamingFile1', bash_command="mv ~/store_files_airflow/loc_wise_profit_agg.csv ~/store_files_airflow/loc_wise_profit_agg_%s.csv" %today,retries = 2,
    retry_delay = timedelta(seconds = 15), dag=dag)
t7 = BashOperator(task_id = 'RenamingFile2', bash_command="mv ~/store_files_airflow/store_wise_profit_agg.csv ~/store_files_airflow/store_wise_profit_agg_%s.csv" %today,retries = 2,
    retry_delay = timedelta(seconds = 15), dag=dag)

t8 = EmailOperator(task_id = "SendEmail", to = "ksheerasagar09@gmail.com" , subject = "Airflow Ouput Files" , 
    html_content=""" <h3>MySql generated aggregated files are attached</h3> """, 
    files = ["/usr/local/airflow/store_files_airflow/loc_wise_profit_agg_%s.csv"%today,"/usr/local/airflow/store_files_airflow/store_wise_profit_agg_%s.csv" %today], dag=dag)

t9 = BashOperator(task_id = 'RenamingOriginalFile', bash_command="mv ~/store_files_airflow/raw_store_transactions.csv ~/store_files_airflow/raw_store_transactions_%s.csv" %today,retries = 2,
    retry_delay = timedelta(seconds = 15), dag=dag)



t1 >> t2 >> t3 >> t4 >>t5 >> t6 >> t7 >> t8 >> t9