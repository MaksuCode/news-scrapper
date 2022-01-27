from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By


class Home_Page():

    FOOTER_CSS = 'footer.main-footer'
    NEWS_URL_CSS = 'div.news-block div.title a'
    

    def __init__(self,driver):
        self.driver = driver
        driver.get('https://www.newsinlevels.com/')


    def scroll_to_footer(self):
        footer = self.driver.find_element(By.CSS_SELECTOR, self.FOOTER_CSS)
        footer.location_once_scrolled_into_view
    
    def get_news_url(self):
        news_url= []
        news_url_element_list = self.driver.find_elements(By.CSS_SELECTOR, self.NEWS_URL_CSS)
        for news_url_element in news_url_element_list:
            news_url.append(news_url_element.get_attribute('href'))
        return news_url


