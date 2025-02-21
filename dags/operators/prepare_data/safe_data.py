import logging
import os

import pandas as pd
from airflow.decorators import task

# Конфигурация логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Логи в консоль
    ]
)

logger = logging.getLogger(__name__)

file_path = '/opt/airflow/output/data_from_sites/output_data.csv'


# Функция для сохранения данных
@task
def save_data(df: pd.DataFrame):
    logger.info(f"Starting to save data with {len(df)} records.")

    # Логируем содержимое DataFrame
    logger.info(f'final df: {df}')
    # Проверяем, существует ли файл
    if not os.path.isfile(file_path):
        logger.info(f"File {file_path} does not exist. Creating a new file.")
        # Если файл не существует, создаем новый DataFrame с заголовками
        df.to_csv(file_path, index=False, mode='w')
        logger.info(f"Successfully created a new CSV file at {file_path}.")
    else:
        logger.info(f"File {file_path} exists. Attempting to append data.")
        # Если файл существует, добавляем новые данные в него
        df.to_csv(file_path, index=False, mode='a', header=False)
        logger.info(f"Successfully appended {len(df)} records to {file_path}.")

    logger.info(f"Data successfully saved to {file_path}. Total records: {len(df)}.")
