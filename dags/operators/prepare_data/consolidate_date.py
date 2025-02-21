from airflow.decorators import task
import logging
import pandas as pd

logger = logging.getLogger(__name__)


@task
def consolidate_data(df1, df2, df3):
    logger.info(df1, df2, df3)
    return pd.concat([df1, df2, df3])