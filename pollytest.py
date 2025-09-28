from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

def init_comment_loader():
    global numberOfComments
    driver = webdriver.Firefox()
    print("webdriver initialized")
    driver.get("https://www.youtube.com/live_chat?is_popout=1&dark_theme=1&v=Ub8YwqMKfGs")
    print("webdriver link get")
    initialWait = WebDriverWait(driver, 60)
    print("webdriver waited")
    commentsContainer = initialWait.until(expected_conditions.presence_of_element_located([By.CSS_SELECTOR, "div[id^=items]"]))
    print(commentsContainer)
    print("container found")
    if commentsContainer == None:
        print("Page unresponsive!!!")
    time.sleep(1)
    print(len(commentsContainer.find_elements(By.CSS_SELECTOR, "yt-live-chat-text-message-renderer")) + 1)
    return driver

init_comment_loader()