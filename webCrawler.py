from selenium import webdriver
from bs4 import BeautifulSoup
import csv

driver = webdriver.Chrome()
driver.get('https://www.lazada.sg/catalog/?q=shampoo')

res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

with open('product.txt' , 'w', encoding='utf-8') as f:
    soup = BeautifulSoup(res, 'lxml').find('div', {'class': 'c1_t2i'}).find_all('div', {'class':'c2prKC'})
    for product in soup:
        product_name = product.find('div', {'class':'c16H9d'}).find('a').text.strip()
        price = product.find('span').text.strip()
        f.write(product_name + " " + price + ",")
        print(product_name + " " + price)
