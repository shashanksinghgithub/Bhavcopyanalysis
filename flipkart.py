from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options 
#from fake_useragent import UserAgent
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time,datetime
import pandas as pd, shutil
from googlesearch import search 
import os 
import random
from selenium.webdriver.common.proxy import Proxy,ProxyType
from functools import reduce


output_dir='D:\\flipkart\\output\\'

d=datetime.datetime.now().date()


def process_url(glist,url_start,grocery_list,d):
    web_url=[]
    fp=[]
    fl=[]
    for i in range(0,len(url_start)):
        print ("processing for url that starts with",url_start[i])
        for j in range(0,len(grocery_list)):
            query = url_start[i]+grocery_list[j]#query to search 
            print ("query",query)
            time.sleep(20)
            
            
            for k in search(query+grocery_list[j], tld="co.in", num=1, stop=1, pause=20):
                driver = webdriver.Chrome("C:\webdriver\chromedriver.exe")
                driver.minimize_window()
                print("url",k)
                driver.implicitly_wait(20)
                web_url.append(k)
                if k.startswith("https://www.flipkart.com/"):
                    if k.endswith("na")==False:
                        
                        if grocery_list[j]=="Daawat Devaaya Basmati Rice (Medium Grain)  (5 kg)":
                            driver.implicitly_wait(20)
                            driver.get('https://www.flipkart.com/daawat-devaaya-basmati-rice-medium-grain/p/itmfygcsyqut8grj?pid=RICEUC2YBAXX8BAZ&lid=LSTRICEUC2YBAXX8BAZJXV8FL&marketplace=GROCERY')
                            soup=BeautifulSoup(driver.page_source, 'lxml')
                            rice = soup.find('div',{'class':'_30jeq3 _16Jk6d'})
                            try:
                                fp.append(rice.getText())
                                print ("price dawwat",rice)
                            except:
                                fp.append('na')

                        elif grocery_list[j]=="Tur dal - private label (1 kg)":
                            driver.implicitly_wait(20)
                            driver.get('https://www.flipkart.com/toor-dal-split/p/itmd0c8246077c7f?pid=PLSFUUSEYMC3K8UR&lid=LSTPLSFUUSEYMC3K8URC8JRTG&marketplace=GROCERY&sattr[]=quantity&st=quantity')
                            soup=BeautifulSoup(driver.page_source, 'lxml')
                            tur = soup.find('div',{'class':'_30jeq3 _16Jk6d'})
                            try:
                                fp.append(tur.getText())
                                print ("tur",tur)
                            except:
                                fp.append('na')

                        elif grocery_list[j]=="Tropicana 100% Orange Juice  (1 L)":
                            driver.implicitly_wait(20)
                            driver.get('https://www.flipkart.com/tropicana-100-orange-juice/p/itmew2amcb3gzguy?pid=DAJEUHCZNMW3QB2X&lid=LSTDAJEUHCZNMW3QB2XBDGFGL&marketplace=GROCERY&sattr[]=quantity&st=quantity')
                            soup=BeautifulSoup(driver.page_source, 'lxml')
                            orange = soup.find('div',{'class':'_30jeq3 _16Jk6d'})
                            try:
                                fp.append(orange.getText())
                                print ("tropicana",orange)
                            except:
                                fp.append('na')

                        elif grocery_list[j]=="Hide and Seek Biscuits (120 gm)":
                            driver.implicitly_wait(20)
                            driver.get('https://www.flipkart.com/parle-hide-seek-chocolate-chip-cookies/p/itmfdhxptdy6up3c?pid=CKBET6WUG3F4TGZZ&lid=LSTCKBET6WUG3F4TGZZODAVIA&marketplace=GROCERY')
                            soup=BeautifulSoup(driver.page_source, 'lxml')
                            hideandseek = soup.find('div',{'class':'_30jeq3 _16Jk6d'})
                            try:
                                fp.append(hideandseek.getText())
                                print ("hideandseek",hideandseek)
                            except:
                                fp.append('na')

                        elif grocery_list[j]=="Amul Taaza Milk (1 ltr)":
                            driver.implicitly_wait(20)
                            driver.get('https://www.flipkart.com/amul-taaza-homogenised-toned-milk/p/itmexak2hfpzbuhf?pid=MLKEUGQGM65M2QZC&lid=LSTMLKEUGQGM65M2QZCBAZ0IA&marketplace=GROCERY&sattr[]=quantity&st=quantity')
                            soup=BeautifulSoup(driver.page_source, 'lxml')
                            amul = soup.find('div',{'class':'_30jeq3 _16Jk6d'})
                            try:
                                fp.append(amul.getText())
                                print ("amul",amul)
                            except:
                                fp.append('na')

                        elif grocery_list[j]=="Parle G Original Gluco Biscuits  (800 g)":
                            driver.implicitly_wait(20)
                            driver.get('https://www.flipkart.com/parle-g-original-gluco-biscuits/p/itmfyxnbtgzatmgg?pid=CKBET6WJYZ96WJ9V&lid=LSTCKBET6WJYZ96WJ9VNXXY3X&marketplace=GROCERY&sattr[]=quantity&st=quantity')
                            soup=BeautifulSoup(driver.page_source, 'lxml')
                            parle = soup.find('div',{'class':'_30jeq3 _16Jk6d'})
                            try:
                                fp.append(parle.getText())
                                print ("parle",parle) 
                            except:
                                fp.append('na')
                        
   
                        elif grocery_list[j]=="LUX Fresh Splash Soap  (3 x 150 g)":
                            driver.implicitly_wait(20)
                            driver.get('https://www.flipkart.com/lux-fresh-splash-soap/p/itmexaskjkkns95u?pid=SOPEUBZRYR223TDT&lid=LSTSOPEUBZRYR223TDT12WVBM&marketplace=FLIPKART&sattr[]=quantity&st=quantity')
                            soup=BeautifulSoup(driver.page_source, 'lxml')
                            lux = soup.find('div',{'class':'_30jeq3 _16Jk6d'})
                            try:
                                fp.append(lux.getText())
                                print ("lux",lux) 
                            except:
                                fp.append('na')

                        elif grocery_list[j]=="Pears Soap (3x125 gm)":
                            driver.implicitly_wait(20)
                            driver.get('https://www.flipkart.com/pears-pure-gentle-bath-soap-3-125gm/p/itm4561f8664')
                            soup=BeautifulSoup(driver.page_source, 'lxml')
                            pears = soup.find('div',{'class':'_30jeq3 _16Jk6d'})
                            try:
                                fp.append(pears.getText())
                                print ("pears",pears)
                            except:
                                fp.append('na')
                        
                        elif grocery_list[j]=="Dettol Cool Soap (3x75 gm)":
                            driver.implicitly_wait(20)
                            driver.get('https://www.flipkart.com/dettol-original-soap-3x75g-free-75g/p/itm740c20f55f9db')
                            soup=BeautifulSoup(driver.page_source, 'lxml')
                            dettol = soup.find('div',{'class':'_30jeq3 _16Jk6d'})
                            try:
                                fp.append(dettol.getText())
                                print ("dettol",dettol)
                            except:
                                fp.append('na')
                                
                        elif grocery_list[j]=="Himalaya sparkling white herbal (150 gm)":
                            driver.implicitly_wait(20)
                            driver.get('https://www.flipkart.com/himalaya-sparkling-white-toothpaste-150-gm/p/itmc64b1a1a66c0b?pid=TPSFNJFTAPZYYSK9&lid')
                            soup=BeautifulSoup(driver.page_source, 'lxml')
                            Himalaya = soup.find('div',{'class':'_30jeq3 _16Jk6d'})
                            try:
                                fp.append(Himalaya.getText())
                                print ("Himalaya",Himalaya)
                            except:
                                fp.append('na')
                                
                        elif grocery_list[j]=="Pepsodent germicheck (300 gm)":
                            driver.implicitly_wait(20)
                            driver.get('https://www.flipkart.com/pepsodent-germicheck-toothpaste-value-saver-pack-2x150g-pack-2/p/itmfhkmufkdtzn6j')
                            soup=BeautifulSoup(driver.page_source, 'lxml')
                            Pepsodent = soup.find('div',{'class':'_30jeq3 _16Jk6d'})
                            try:
                                fp.append(Pepsodent.getText())
                                print ("Pepsodent",Pepsodent)
                            except:
                                fp.append('na')
                        else:
                            driver.get(k)
                            driver.implicitly_wait(20)
                            soup=BeautifulSoup(driver.page_source, 'lxml')
                            flipkart = soup.find('div',{'class':'_30jeq3 _16Jk6d'})
                            try:
                                fp.append(flipkart.getText())
                            except:
                                fp.append('na')
                            print ("flipkart price",fp)
                    else:
                        fp.append('na')
                    fl.append(k)
   
#    all_url=pd.DataFrame(web_url)
#    all_url.to_excel("all_url_{}.xlsx".format(d),index=False)   
            
    fl=pd.DataFrame(fl,columns=["flipkart_url"])
#    fl.to_excel(output_dir+"flipurl_{}.xlsx".format(d),index=False)
    fp=pd.DataFrame(fp,columns=["flipkart_price"])
#    fp.to_excel(output_dir+"flipprice_{}.xlsx".format(d),index=False)

    final_list=[glist,fl,fp]
#    print final_list
    final_df=reduce(lambda left,right:pd.merge(left,right,left_index=True, right_index=True,how="left"),final_list)
#    print final_df
    final_df.to_excel(output_dir+"grocery_flipkart_{}.xlsx".format(d),index=False)
    
    return final_df

def flipkart_main(d):
    d=datetime.datetime.now().date()
    grocery_list=["Aashirvaad Multigrain Flour (1 kg)",
                  "Madhur Sugar  (1 kg)",
                  "Daawat Devaaya Basmati Rice (Medium Grain)  (5 kg)",
                  "Fortune Sunlite Refined Sunflower Oil Can  (5 L)",
                  "Tur dal - private label (1 kg)",
                  "Cashew nut (500 gm)",
                  "Cumin - private label (100 gm)",
                  "Kellogg's Cornflakes - Original (875 gm)",
                  "Tropicana 100% Orange Juice  (1 L)",
                  "Parle G Original Gluco Biscuits  (800 g)",
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
                  "LUX Fresh Splash Soap  (3 x 150 g)",
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
  
 
    glist=pd.DataFrame(grocery_list,columns=["grocery_items"])

    
    url_start=["https://www.flipkart.com/"]
    
    final_df=process_url(glist,url_start,grocery_list,d)
    
    return final_df
flipkart_main(d)