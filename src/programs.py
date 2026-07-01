import requests

from codes import codes

url = "https://my.spbstu.ru/home/get-abit-list"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:149.0) Gecko/20100101 Firefox/149.0",
    "Accept": "*/*",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Sec-GPC": "1",
    "DNT": "1",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=0",
}

cookies = {
    "sessionid": "yp9yk9y7igfnjfc162ldn2ckw70qugut",
    "cookie_name": "cookie_value"
}
def get_list(quote: int, program: str) -> list:
    params = {
        "filter_1": "2",                
        "filter_2": str(quote),           # Квота
        "filter_3": codes[program],       # Программа
        "education_level": "bachelor"
    }
    response = requests.get(
        url,
        params=params,
        headers=headers,
        cookies=cookies
    )
    return response.json()["results"]