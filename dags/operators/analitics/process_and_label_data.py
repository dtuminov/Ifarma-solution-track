import logging

import pandas as pd
from airflow.decorators import task
from operators.analitics.yandexGPTdemo import get_response

# Конфигурация логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Логи в консоль
    ]
)

logger = logging.getLogger(__name__)
file_path_to_save = '/opt/airflow/output/process_data/labeled_data.csv'


@task
def process_data(file_path: str):
    logger.info(f"Начато обрабатываем данных из файла: {file_path}")

    # Чтение данных из CSV файла
    df = pd.read_csv(file_path, header=None)
    logger.info(f"Данные считаны. Всего строк: {len(df)}")

    # Переименование столбцов
    columns = ['comment', 'drag_name']
    df.columns = columns

    logger.info(f"Столбцы переименованы в: {columns}")

    # Выводим данные для отладки (можно отключить, если не нужно)
    logger.debug(f"Считанный DataFrame:\n{df}")

    # Удаление дубликатов
    df = df.drop_duplicates().reset_index(drop=True)
    logger.info(f"Удалено дубликатов. Новое количество строк: {len(df)}")

    logger.debug(f"Новый DataFrame после удаления дубликатов:\n{df}")

    # Применение функции get_response
    df['side_effects'] = df['comment'].apply(get_response)
    logger.info("Функция get_response применена к столбцу 'comment'.")

    # Выводим данные для отладки
    logger.debug(f"DataFrame после применения get_response:\n{df}")

    # Сохранение обработанных данных в новый CSV файл
    df.to_csv(file_path_to_save, index=False)
    logger.info(f"Обработанные данные сохранены в файл: {file_path_to_save}")


