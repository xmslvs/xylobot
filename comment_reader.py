from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time
import random

def init_comment_loader():
    global numberOfComments
    driver = webdriver.Firefox()
    print("webdriver initialized")
    driver.get("https://www.youtube.com/live_chat?v=d4L4YQ9PF4k")
    print("webdriver link get")
    initialWait = WebDriverWait(driver, 60)
    print("webdriver waited")
    commentsContainer = initialWait.until(expected_conditions.presence_of_element_located([By.CSS_SELECTOR, "div[id^=items]"]))
    print("container found")
    if commentsContainer == None:
        print("Page unresponsive!!!")
    time.sleep(1)
    numberOfComments = len(commentsContainer.find_elements(By.CSS_SELECTOR, "yt-live-chat-text-message-renderer"))
    print("element size found: " + str(numberOfComments))
    return driver


def read_new_comment(driver):
    global numberOfComments
    newCommentText = "div[id^=items] > :nth-child(" + str(numberOfComments) + " of yt-live-chat-text-message-renderer) > div[id^=content] > span[id^=message]"
    newCommentAuthor = "div[id^=items] > :nth-child(" + str(numberOfComments) + " of yt-live-chat-text-message-renderer) > div[id^=content] > yt-live-chat-author-chip > span[id^=author-name]"
    print("reading comments...")
    
    for i in range(0, random.randint(20, 30)):
        new_comment = driver.find_elements(By.CSS_SELECTOR, newCommentText)
        if (len(new_comment) == 0):
            time.sleep(1)
        else:
            newCommentTextData = (WebDriverWait(driver, 1)).until(expected_conditions.visibility_of_element_located([By.CSS_SELECTOR, newCommentText]))
            newCommentAuthorData = (WebDriverWait(driver, 1)).until(expected_conditions.visibility_of_element_located([By.CSS_SELECTOR, newCommentAuthor]))
            print("newCommentFound")
            numberOfComments += 1
            print("numberOfComments incremented")
            print(newCommentAuthorData.text + ": " + newCommentTextData.text)  #prints current user's comment
            newCommentData = {"user": newCommentAuthorData.text, "response": newCommentTextData.text, "response_datetime": time.ctime()}
            break
    if (len(new_comment) == 0):
        new_comment = driver.find_elements(By.CSS_SELECTOR, newCommentText)
        print("new comment not found, generating independent prompt")
        newCommentData = {"user": "","response": "", "response_datetime": time.ctime()}
    
    return newCommentData

