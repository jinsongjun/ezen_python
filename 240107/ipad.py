from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from bs4 import BeautifulSoup as bs

driver = webdriver.Chrome()
<<<<<<< HEAD
=======

>>>>>>> e7b4319dddf97594256030d5a88374575b1ca062
driver.get('https://www.naver.com')

time.sleep(0.5)

<<<<<<< HEAD
element = driver.find_element(By.ID, "query")
element.send_keys('아이패드')
=======
element = driver.find_element(By.ID, 'query')

element.send_keys('아이패드')

>>>>>>> e7b4319dddf97594256030d5a88374575b1ca062
element.send_keys(Keys.ENTER)

time.sleep(0.5)

element2 = driver.find_element(By.XPATH, '//*[@id="main_pack"]/section[2]/div[1]/div[4]/a')
<<<<<<< HEAD
=======

>>>>>>> e7b4319dddf97594256030d5a88374575b1ca062
element2.click()

time.sleep(0.5)

all_window = driver.window_handles
<<<<<<< HEAD
driver.switch_to.window(all_window[1])
end_element = driver.find_element(By.XPATH, '//*[@ID="wrap"]/div[3]')
for i in range(10) :
    action = webdriver.ActionChains(driver)
    action.move_to_element(end_element).perform()
    time.sleep(0.5)

soup = bs(driver.page_source, "html.parser")
div_list = soup.find_all('div', attrs = {
    'class' : 'product_title__Mmw2K'
})

item_name=[]
for i in div_list :
    item_name.append(i.get_text())

div_list2 = soup.find_all('div', attrs= {
=======

driver.switch_to.window(all_window[1])

end_element = driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]')

for i in range(10):
    action = webdriver.ActionChains(driver)
    action.move_to_element(end_element).perform()
    time.sleep(0.2)

soup = bs(driver.page_source, 'html.parser')

div_list = soup.find_all('div', attrs={
    'class' : 'product_title__Mmw2K'
})

item_list = []
for i in div_list:
    # print(i.get_text())
    item_list.append(i.get_text())

item_list

div_list2 = soup.find_all('div', attrs={
>>>>>>> e7b4319dddf97594256030d5a88374575b1ca062
    'class' : 'product_price_area__eTg7I'
})

price_list = []
<<<<<<< HEAD
for i in div_list2 :
    data = i.find('span' , attrs = {
    'class' : 'price_num__S2p_v'
    }).get_text()
    price_list.append(data)

data =  {
    '상품명' : item_name ,
    '가격' : price_list
=======
for i in div_list2:
    data = i.find('span', attrs = {
        'class' : 'price_num__S2p_v'
    }).get_text()
    price_list.append(data)
price_list

data = {
    '상품명' : item_list, 
    '상품가격' : price_list
>>>>>>> e7b4319dddf97594256030d5a88374575b1ca062
}

df = pd.DataFrame(data)

from datetime import datetime

now = datetime.now()

<<<<<<< HEAD
df.to_excel(f'아이패드가격{now.date()}.xlsx' , index=False)
=======
df.to_excel(f'아이패드가격{now.date()}.xlsx', index=False)
>>>>>>> e7b4319dddf97594256030d5a88374575b1ca062

driver.quit()