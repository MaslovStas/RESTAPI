import urllib.request

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    with urllib.request.urlopen(url) as response:
        if response.getcode() == 200:
            data = response.read()
            print("Данные с https://api.coindesk.com/v1/bpi/currentprice.json:\n", data.decode('utf-8'))

except Exception as e:
    print(f"Ошибка запроса: {e}")
