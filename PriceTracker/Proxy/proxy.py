from selenium import webdriver
import random

file = open('proxy.txt')
proxies = []
for proxy in file:
    proxies.append(proxy)
file.close()

def proxy():
    PROXY = random.choice(proxies)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)

    chrome = webdriver.Chrome(options=chrome_options)

    return PROXY
