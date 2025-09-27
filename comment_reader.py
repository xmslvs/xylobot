from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

def init_comment_loader():
    global numberOfComments
    driver = webdriver.Firefox()
    print("webdriver initialized")
    driver.get("https://www.youtube.com/live_chat?is_popout=1&dark_theme=1&v=Ub8YwqMKfGs")
    print("webdriver link get")
    initialWait = WebDriverWait(driver, 60)
    print("webdriver waited")
    commentsContainer = initialWait.until(expected_conditions.presence_of_element_located([By.CSS_SELECTOR, "div[id^=items]"]))
    print("container found")
    if commentsContainer == None:
        print("Page unresponsive!!!")
    numberOfComments = len(commentsContainer.find_elements(By.CSS_SELECTOR, "style-scope.yt-live-chat-item-list-renderer")) + 1
    print("element size found")
    return driver


def read_new_comment(driver):
    global numberOfComments
    newCommentSelector = "div[id^=items] > :nth-child(" + str(numberOfComments) + " of yt-live-chat-text-message-renderer) > div[id^=content] > span[id^=message]"
    print(newCommentSelector)
    newComment = (WebDriverWait(driver, 6000)).until(expected_conditions.visibility_of_element_located([By.CSS_SELECTOR, newCommentSelector]))
    print("newCommentFound")
    numberOfComments += 1
    print("numberOfComments incremented")
    print(newComment.text)  #prints current user's comment
    return newComment.text

