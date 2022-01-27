from selenium.webdriver.common.by import By

class News_Page():

    CONTENT_CSS = 'div[id=\'nContent\'] p'
    ARTICLE_TITLE_CSS = 'div.article-title h2'
    IMG_CSS = 'div.upper-content div.img-wrap a img'

    def __init__(self, driver, link):
        self.driver = driver
        self.link = link
        driver.get(link)

    def get_content(self):
        paragraphs = self.driver.find_elements(By.CSS_SELECTOR, self.CONTENT_CSS);
        content = ''
        for paragraph in paragraphs:
            content += '\ '
            content += paragraph.text
        return content   

    def get_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.ARTICLE_TITLE_CSS).text

    def get_img_url(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.IMG_CSS).get_attribute('src')


