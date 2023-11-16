import requests
 
def translate_word(phrase: str, source_lang: str = 'pt-BR', target_lang: str = 'en'):
    headers = {
        'authority': 'translate.yandex.net',
        'accept': '*/*',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://translate.yandex.com',
        'referer': 'https://translate.yandex.com/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'x-retpath-y': 'https://translate.yandex.com',
    }
 
    params = {
        'id': '6b056a99.65542663.afe9e98a.74722d74657874-0-0',
        'srv': 'tr-text',
        'source_lang': source_lang,
        'target_lang': target_lang,
        'yu': '9679616211700012813',
        'yum': '1700012819583959298',
        'sprvk': 'dD0xNzAwMDEzNjY2O2k9MjAwLjc5LjE4Ni44OTtEPUIyMzk2RkMxMjBFMDBENEI0RDBFQjkxRjJBRDY4NEI5RjI5RDUxMkJGNzAzQkVGNDc1M0Q4NTAwNjdEMEFDNDYxNDM0RUFEMkE5Q0FGOTY1MEM1Q0NGQUI1OTM5MEVBQjBERTI4MEZEQzcxQjZDRDMwNzEyMEIxMkQwQkU0N0ZENzMzRUJEMTAzQTkzRDNCNjNCQThDRkRERjc4MTI2QjY7dT0xNzAwMDEzNjY2OTM5NzMxMDkyO2g9MWQxNDlhMTc0YTg3ODk5YWYxNjdiODU4Mzc5MWNmMTU=',
    }
 
    data = {
        'text': phrase,
        'options': '1'
    }
 
    translate_word = requests.post('https://translate.yandex.net/api/v1/tr.json/translate', params=params, headers=headers, data=data).json()
 
    return translate_word.get('text')[0]


