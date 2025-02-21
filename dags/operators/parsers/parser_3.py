import pandas as pd
from airflow.decorators import task
import logging

logger = logging.getLogger(__name__)


# Функции для парсеров
@task
def parser_3() -> pd.DataFrame:
    logger.info("Starting parser 3")
    print("Парсер 3 выполняется")
    # Здесь будет код для парсинга данных
    return pd.DataFrame(columns=['comment','drag_name'])  # Возвращаем пустой датафрейм
