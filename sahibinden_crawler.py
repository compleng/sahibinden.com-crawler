from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import os
path = os.getcwd()
driver = wd.Chrome(executable_path=path + '/chromedriver')
driver.get('https://www.sahibinden.com/cep-telefonu-giyilebilir-teknoloji?pagingSize=50&query_text_mf=apple+watch&query_text=apple+watch&address_city=6')
#text = "apple watch"
#driver.find_element_by_id('searchText').send_keys(text)
#driver.find_element_by_xpath("//button[@value='Ara']").click()
#driver.find_element_by_link_text('Giyilebilir Teknoloji').click()

driver.execute_script('''
        var element = document.getElementsByClassName("ad-title"), index;
        for (index = element.length - 1; index >= 0; index--) {
            element[index].parentNode.removeChild(element[index]);
        }
    ''')


pages = driver.find_elements_by_xpath('//tbody[contains(@class,"searchResultsRowClass")][not(contains(@style,"display:none"))]/tr[contains(@class,"searchResultsItem")]')

values = 0
for values in range(30) :
    driver.execute_script('''
         var element = document.getElementsByClassName("ad-title"), index;
         for (index = element.length - 1; index >= 0; index--) {
             element[index].parentNode.removeChild(element[index]);
         }
     ''')
    driver.execute_script('''
             var element = document.getElementsByClassName("nativeAd"), index;
             for (index = element.length - 1; index >= 0; index--) {
                 element[index].parentNode.removeChild(element[index]);
             }
         ''')


    pages = driver.find_elements_by_xpath('//tbody[contains(@class,"searchResultsRowClass")][not(contains(@style,"display:none"))]/tr[contains(@class,"searchResultsItem")]')
    pages1 = driver.find_elements_by_xpath('//tbody[contains(@class,"searchResultsRowClass")][not(contains(@style,"display:none"))]/tr[contains(@class,"searchResultsItem")]')[values]
    pages1.click()

    user = driver.find_elements_by_class_name("username-info-area")[0]
    user_text = user.text

    try:
        phone = driver.find_element_by_class_name("pretty-phone-part")
        phone_text = phone.text

    except NoSuchElementException:
        phone_text = "Telefon numarası yok"
        pass

    f = open("output.txt", "a")
    f.write(user_text + "  -  " + phone_text + "\n")
    f.close()

    WebDriverWait(driver,5)


    driver.execute_script("window.history.go(-1)")
    WebDriverWait(driver, 10)
