from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd 
from pandas import DataFrame
from selenium.common.exceptions import TimeoutException


url = "https://www.fpi.nsdl.co.in/web/Reports/Film_List_All.aspx"
driver = webdriver.Chrome("C:\webdriver\chromedriver.exe")
driver.get(url)
page = 1
max_page = 266
my_data = []


while page<=266:
    
    try:

        soup = BeautifulSoup(driver.page_source, 'lxml')
        temp =  soup.prettify()
        wait = WebDriverWait(driver, 10)
        table_body=soup.find('tbody')
        rows = table_body.find_all('tr')

        for row in rows:
            cols=row.find_all('td')
            cols=[x.text.strip() for x in cols]
            my_data.append(cols)
            print (cols)
        
            
        first_source_data = my_data[0:]
        print(first_source_data)

        driver.find_element_by_id('myTable_next').click()

    
        page = page + 1
    except TimeoutException:
        break
#soup.find("a", { "id" : 'myTable_next' }) 
    


df = DataFrame(first_source_data,columns=['Sr. No.','ISIN','Issuer Name', 'NRI Limit', 'FPI Limit', 'Sec','Permissible limit','paid up','remarks'])
print (df)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter (r'D:\New folder\G8.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
