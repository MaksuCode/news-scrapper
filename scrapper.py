from news import News
from home_page import Home_Page
from news_page import News_Page
from selenium import webdriver
from pdf_creator import Pdf_Creator
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# driver setup
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# Navigation to home page and get url of the news
home_page =  Home_Page(driver)
home_page.scroll_to_footer()
url_list = home_page.get_news_url()

# Looping over each news and scrapping data
news_list = []
iter = 1 ;
for url in url_list:
    news_page = News_Page(driver, url)
    link = news_page.link
    title = news_page.get_title()
    img = news_page.get_img_url()
    content = news_page.get_content()
    news = News(link, title, img, content)
    news_list.append(news)
    print("Scanned {} news...".format(iter))
    iter += 1

# Create PDF containing the news
pdf = Pdf_Creator('News-2.pdf', news_list)
