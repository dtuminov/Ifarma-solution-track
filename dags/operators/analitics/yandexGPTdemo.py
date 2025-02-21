import json
import requests


def get_response(comment: str) -> str:
    prompt = {
        "modelUri": "gpt://b1g3d9jss2ktl1fb8la3/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "user",
                "text": f"определи нежелательную реакцию (напиши название нежелательной реакции) на препарат или "
                        f"скажи что"
                        f"все хорошо если ее нет (если все хорошо, то ты должен ответить нет НР) в данном комментарии "
                        f"от пользователя:  {comment}"
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVN0D19dHpJ_vnF3Hjhd1OMWNq5C2K1cvg5nw69"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.text
    print(result)

    # Преобразуем строку JSON в словарь Python
    data = json.loads(result)

    # Извлекаем текст
    text = data['result']['alternatives'][0]['message']['text']

    # Выводим результат
    print(text)
    return text
