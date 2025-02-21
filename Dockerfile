FROM apache/airflow:latest

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./dags /opt/airflow/dags