

# import requests

# for i in range(1, 10):
#     session = requests.Session()
#     session.proxies = {"http": "socks5://localhost:9150", "https": "socks5://localhost:9150"}
#     print("Hi")
#     html = session.get("http://icanhazip.com/")
#     print(html.content)