from airflow import DAG
import datetime as dt
import logging

from operators.prepare_data import safe_data, consolidate_date
from operators.parsers import parser_1, parser_2, parser_3
from operators.analitics import process_and_label_data

from operators.sourses import medication_urls_yandex, medication_urls_Uteka

# Настройка логирования
logger = logging.getLogger(__name__)

file_path_to_df = '/opt/airflow/output/data_from_sites/output_data.csv'

with DAG(
        dag_id='pipeline',
        start_date=dt.datetime(2023, 10, 1),
        schedule_interval='@daily',
        catchup=False,
) as dag:
    df_eapteka = parser_1.parser_for_Uteka(medication_urls_Uteka)
    df_yandex = parser_2.parser_for_Yandex(medication_urls_yandex)
    df_parser_3 = parser_3.parser_3()

    # Консолидация данных в один датафрейм
    consolidated_data = consolidate_date.consolidate_data(df_eapteka, df_yandex, df_parser_3)

    # Сохранение данных
    saving_data = safe_data.save_data(consolidated_data)

    # Обработка данных
    processing_data = process_and_label_data.process_data(file_path_to_df)

    # Задача на обработку полученных данных
    var = saving_data >> processing_data


