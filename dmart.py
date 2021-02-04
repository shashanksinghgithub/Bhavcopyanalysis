from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options 
#from fake_useragent import UserAgent
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.common.by import By
from functools import reduce
from bs4 import BeautifulSoup
import time,datetime
import pandas as pd, shutil
from googlesearch import search 
import os,re
import random
from selenium.webdriver.common.proxy import Proxy,ProxyType

output_dir="D:\\dmart\\output\\"
_URL_dmart="https://www.dmart.in/product/"
wait_imp = 5


#fucntion to get price when first one dosent give
def getvalues(soup):
    li=soup.find_all('span',{'class':'class="src-client-app-product-details-styles-__price-details-component-module___value"'})
    val=li.gettext()
    print("price",val)
    return val

     

#function returns price based on possible outcomes or else returns na

        
def process_url(glist,url_start,grocery_list,d):
    dp=[]
    for i in range(0,len(url_start)):
        print("url",url_start[i])
        for j in range(0,len(glist)):

            
            driver = webdriver.Chrome("C:\webdriver\chromedriver.exe")
            driver.minimize_window()
            driver.implicitly_wait(20)
            print(glist["dmart_url"][j])
#            driver.get(glist["dmart_url"][j])
            driver.get(glist["dmart_url"][j])
            soup=BeautifulSoup(driver.page_source, 'lxml')
            if glist["dmart_url"][j].startswith(_URL_dmart) and glist["dmart_url"][j].endswith("na")==False:
                if grocery_list[j]=="Aashirvaad Multigrain Flour (1 kg)" or grocery_list[j]=="Madhur sugar (1 kg)" or grocery_list[j]== "Tur dal - Premia (1 kg)" or grocery_list[j]=="Rin detergent powder (1 kg)" or grocery_list[j]=="Ariel Matic front load (1 kg)":
                    buttons = driver.find_elements_by_xpath("//*[contains(text(), '1 kg')]")
                    for btn in buttons:
                        btn.click()
                    li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                    dp.append((li[5:]))
                                    
                if grocery_list[j]=="Devaaya rice (5 kg)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '5 kg')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()
                      
                if grocery_list[j]=="Fortune Sunflower Oil (5 ltr)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '5 L')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()
                        
                if grocery_list[j]=="Cashew nut - Premia (500 gm)" or grocery_list[j]=="Amul Butter (500 gm)" or grocery_list[j]=="Brooke Bond Red Label (500 gm)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '500 gm')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()
            
                if grocery_list[j]=="Cumin - Premia (100 gm)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '100 gm')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()
            
                
                if grocery_list[j]=="Kellogg's Cornflakes - Original (875 gm)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '500 gm')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()
            
                            
                if grocery_list[j]=="Tropicana Orange Juice (1 ltr)" or grocery_list[j]=="Amul Taaza Milk (1 ltr)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '1 L')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()
            
              
                if grocery_list[j]=="Parle G Biscuits (800 gm)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '800 gm')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()
                            
                if grocery_list[j]=="Britannia Bourbon (150 gm)" or grocery_list[j]=="Colgate calci-lock (150 gm)" or grocery_list[j]=="Himalaya sparkling white herbal (150 gm)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '150 gm')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()
                            
                if grocery_list[j]=="Hide and Seek Biscuits (120 gm)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '120 gm')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()      
                    
                            
                if grocery_list[j]=="Nescafe Instant Coffee (50 gm jar)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '50 gm')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()    
                
                if grocery_list[j]== "Dove Intense Repair (340 ml)" or grocery_list[j]=="Sunsilk thick and long (340 ml)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '340 ml')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()     
               
                if grocery_list[j]=="Pantene Silky Smooth care (675 ml)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '675 ml')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()
                            
                if grocery_list[j]=="Clinic Plus Strong & Long (650 ml)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '650 ml')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()
                            
                if grocery_list[j]=="Lux Fresh Splash (3x150 gm)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '3x150 gm')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()
                            
                if grocery_list[j]=="Dettol Cool Soap (3x75 gm)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '3x75 gm')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()
                            
                if grocery_list[j]=="Pears Soap (3x125 gm)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '3x125 gm')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()
                            
                if grocery_list[j]=="Lifebuoy (4x125 gm)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '4x125 gm')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()
                            
                if grocery_list[j]=="Surf Excel Quick Wash (2 kg)" or  grocery_list[j]=="Tide Plus (2 kg)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '2 kg')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()
          
                if grocery_list[j]=="Pepsodent germicheck (300 gm)":
                    try:
                        buttons = driver.find_elements_by_xpath("//*[contains(text(), '300 gm')]")
                        for btn in buttons:
                            btn.click()
                        li=driver.find_element_by_class_name("src-client-app-product-details-styles-__price-details-component-module___sp").text
                        dp.append((li[5:]))
                        driver.quit()
                    except:
                        dp.append('na')
                        print("item not available")
                        driver.quit()
              
                 
            
           
    dp=pd.DataFrame(dp,columns=["dmart_price"])
     
#        dp.to_excel(output_dir+"dmaprice.xlsx",index=False)
    grocery_list=pd.DataFrame(grocery_list,columns=["grocery_items"])
        
    final_list=[grocery_list,glist,dp]
#        print final_list
    final_df=reduce(lambda left,right:pd.merge(left,right,left_index=True, right_index=True,how="left"),final_list)
#        print final_df
    final_df.reset_index(inplace=True)

    
    final_df.drop(columns=["index","level_0"],axis=1,inplace=True)
    
    final_df.to_excel(output_dir+"grocery_dmart_{}.xlsx".format(d),index=False)
    
    return final_df

def dmart_main(d):
    #    d=datetime.datetime.now().date()
    grocery_list=["Aashirvaad Multigrain Flour (1 kg)",
                  "Madhur sugar (1 kg)",
                  "Devaaya rice (5 kg)",
                  "Fortune Sunflower Oil (5 ltr)",
                  "Tur dal - Premia (1 kg)",
                  "Cashew nut - Premia (500 gm)",
                  "Cumin - Premia (100 gm)",
                  "Kellogg's Cornflakes - Original (875 gm)",
                  "Tropicana Orange Juice (1 ltr)",
                  "Parle G Biscuits (800 gm)",
                  "Hide and Seek Biscuits (120 gm)",
                  "Britannia Bourbon (150 gm)",
                  "Amul Butter (500 gm)",
                  "Amul Taaza Milk (1 ltr)",
                  "Brooke Bond Red Label (500 gm)",
                  "Nescafe Instant Coffee (50 gm jar)",
                  "Dove Intense Repair (340 ml)",
                  "Sunsilk thick and long (340 ml)",
                  "Pantene Silky Smooth care (675 ml)",
                  "Clinic Plus Strong & Long (650 ml)",
                  "Lux Fresh Splash (3x150 gm)",
                  "Dettol Cool Soap (3x75 gm)",
                  "Pears Soap (3x125 gm)",
                  "Lifebuoy (4x125 gm)",
                  "Rin detergent powder (1 kg)",
                  "Surf Excel Quick Wash (2 kg)",
                  "Tide Plus (2 kg)",
                  "Ariel Matic front load (1 kg)",
                  "Colgate calci-lock (150 gm)",
                  "Himalaya sparkling white herbal (150 gm)",
                  "Pepsodent germicheck (300 gm)"]
    
    
    
    glist=pd.read_excel("D:\dmart\dmart_url.xlsx")
    glist.reset_index(inplace=True)
    
    url_start=[_URL_dmart]
    
    final_df=process_url(glist,url_start,grocery_list,d)
    
    return final_df

dmart_main(datetime.datetime.now().date())
