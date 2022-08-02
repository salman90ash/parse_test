import requests
from bs4 import BeautifulSoup
import psycopg2
from config import host, user, password, db_name

# URL = 'https://roszdravnadzor.gov.ru/'
URL = 'https://2ip.ru/'

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}


def get_html(url):
    proxy = {'https': '81.23.100.154:8080'}
    r = requests.get(url, headers=HEADERS, proxies=proxy)
    soup = BeautifulSoup(r.text, 'lxml')

    ip = soup.find('div', class_='ip').text.strip()
    location = soup.find('div', class_='value value-country').text.strip()

    return ip, location


#
# try:
#     connection = psycopg2.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=db_name
#     )
#
#     # cursor = connection.cursor()
#     with connection.cursor() as cursor:
#         cursor.execute(
#             "SELECT version();"
#         )
#         print(f"Server version: {cursor.fetchone()}")
#
# except Exception as _ex:
#     print("[INFO] Error while working with PostgreSQL", _ex)
# finally:
#     if connection:
#         # cursor.close()
#         connection.close()
#         print("[INFO] PostgreSQL connection closed")

print(get_html(URL))
