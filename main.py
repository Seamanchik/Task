import requests

url = "https://search.yandex-team.ru/suggest/"
params = {
    "text": "Саптех",
    "version": "2",
    "people.per_page": "10"
}
cookies = {
    'Session_id': '3:1756367172.5.0.1739906258662:INY1Lg:e5cf.1.2:3.4:2.100:fR_UJQ.101:1756367172.102:1756367172|1120000001264128.16460914.4002.2:16460914.3:1756367172|5:10239662.45156.zR4xtAT_I7RKRBQ4DIZarsFPfbM',
    'sessionid2': '3:1756367172.5.0.1739906258662:INY1Lg:e5cf.1.2:3.4:2.100:fR_UJQ.101:1756367172.102:1756367172|1120000001264128.16460914.4002.2:16460914.3:1756367172|5:10239662.45156.fakesign0000000000000000000',
    'yandex_login': 'vladryabyshev',
    '_yasc': '27c55FH2B+0TgUbQo0EolWicKSJm4Sgq1Z0Bmtg3/bRWYPqt5s6NyGqsBzMgccmyjAWKxA==',
    '_ym_d': '1755684610',
    '_ym_isad': '2',
    '_ym_uid': '1739906129421248304',
    'app_lang': 'ru',
    'bh': 'EmkiQ2hyb21pdW0iO3Y9IjEzNiIsICJZYUJyb3dzZXIiO3Y9IjI1LjYiLCAiTm90LkEvQnJhbmQiO3Y9Ijk5IiwgIllvd3NlciI7dj0iMi41IiwgIllhQnJvd3NlckNvcnAiO3Y9IjEzNiIaBSJ4ODYiKgI',
    'CSRF-TOKEN': 'e409f332f24600198fae096590da25066c961db5%3A1756374940',
    'font_loaded': 'YSv1',
    'gdpr': '0',
    'i': 'inoU/RJV+c/OfLTWv3us3zsXzjt0lx5RJw/A9cOJ/PKGL9Kp8tT7tzMKThJXKFov6XcSDkK16gXK23jIRCwj1//AQ0U=',
    'L': 'ewV6c3Ngfkh6f2NYAEFxfgxEe3tWUVlYQR8qHh4uKwcVNx0uOw',
    'sessar': '1.33.CiBXvjGCHhBjPemZMf_jE8_LKeEb6VLjmgki2s9pp9QHWw.kVyjre5wcirc-Xj3ZK0BqER4X8Vxii-XzUCaWL0ArwE',
    'yandexuid': '2856787851740581312',
    'yashr': '4547606851744291446',
    'yp': '2071727172.udn.cDp2bGFkcnlhYnlzaGV2#1756117431.szm.1_25:1536x864:1488x740',
    'ys': 'udn.cDp2bGFkcnlhYnlzaGV2',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://search.yandex-team.ru/',
}

response = requests.get(url, params=params, headers=headers, cookies=cookies)

if response.status_code == 200:
    try:
        data = response.json()

        people_list = data.get('people', {}).get('result', [])
        logins = [person.get('login') for person in people_list if person.get('login')]

        print(f"Найдено {len(logins)} логинов:")
        for login in logins:
            print(f"- {login}")

    except requests.exceptions.JSONDecodeError as e:
        print("Ошибка декодирования JSON:", e)
        print("Первые 500 символов ответа:")
        print(response.text[:500])
else:
    print(f"Ошибка запроса: {response.status_code}")
    print("Заголовки:", dict(response.headers))