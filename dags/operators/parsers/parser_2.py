import logging

import pandas as pd
from airflow.decorators import task
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат сообщений
    handlers=[
        logging.FileHandler('app.log'),  # Сохранение логов в файл
    ]
)


@task
def parser_for_Yandex(medication_urls: dict) -> pd.DataFrame:
    logging.info("Open webdriver_remote")

    # Настройка опций для Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    remote_webdriver = 'remote_chromedriver'
    driver = webdriver.Remote(
        command_executor=f'{remote_webdriver}:4444/wd/hub',
        options=options
    )
    logging.info("Webdriver opened")

    all_reviews = []

    try:
        for drag_name, url in medication_urls.items():
            logging.info(f"Processing {drag_name} with URL {url}")

            driver.get(url)
            logging.info("Page loaded successfully")

            # Ожидаем загрузки элементов отзывов на странице
            elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[class="Cut-Visible"]'))
            )

            logging.info(f"Found {len(elements)} review elements for {drag_name}")

            # Извлекаем текст из каждого элемента
            for element in elements:
                review_text = element.text
                all_reviews.append({'comment': review_text, 'drag_name': drag_name})

        logging.info("Data collected successfully")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return pd.DataFrame(data=[])

    finally:
        driver.quit()  # Закрываем драйвер после завершения работы

    df = pd.DataFrame(all_reviews)
    return df

