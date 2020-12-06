from selenium import webdriver
import os
from app.config import exe

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    },
    "safebrowsing.enabled": False
})
# chrome_options.binary_location ="C:\\Users\\Aarthif\\Desktop\\Chrome32_52.0.2743.116\\chrome.exe"
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-user-media-security=true")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

def woolsworth(producturl):
    url = ""
    price = ""
    try:
        driver.get(producturl)
        url = producturl.split("/")
        el = driver.find_element_by_xpath('/html/body/wow-root/wow-app-layout/div/div[3]/main/wow-product-details-container/section/div[1]/div[2]/div[2]/wow-product-details-panel/section/div/div/div/shared-price/div[1]')
        price = el.text
        print(price)
        driver.quit()
    except:
        pass
    return {"name":url[-1],"price": "".join(str(price).split())}

def officeWorks(producturl):
    price = ""
    url = ""
    try:
        driver.get(producturl)
        url = producturl.split("/")
        el = driver.find_element_by_xpath('/html/body/div[3]/div[7]/div/div[6]/div[2]/div/div[1]/div[1]/div[1]/div/span/span')
        price = el.text
        driver.quit()
    except:
        pass
    return {"name": url[-1],"price": "".join(str(price).split())}


