import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:149.0) Gecko/20100101 Firefox/149.0",
    "Content-Type": "application/json",
    "Origin": "https://my.spbstu.ru",
    "Accept": "*/*",
}

cookies = {
    "sessionid": "yp9yk9y7igfnjfc162ldn2ckw70qugut",
    "cookie_name": "cookie_value"
}

response = requests.post(
    "https://my.spbstu.ru/home/get-code-list",
    json={
        "id_1": "2",
        "id_2": "1",
        "education_level": "bachelor"
    },
    headers=headers,
    cookies=cookies
)
codes = dict()
for code in response.json()['code_list']:
    id = code['id']
    num = code['title'][0:8]
    codes[num] = id
