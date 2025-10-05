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

from gemini_llm import system_prompt, independent_prompt, gen_gemini_response
import asyncio

async def test_response():
    input=[{"user": "test_instuctor", "response": "please become angry", "response_datetime": "Fri Oct  3 16:15:52 2025"}]
    await gen_gemini_response(system_prompt(input, 0))

import keyboard
from focus_window import focus_on_window

def test_emotions():
    focus_on_window("VTube Studio")
    time.sleep(1)
    keypress = {
        'happy': 23, 
        'sad': 's', 
        'scared': 'j',
        'angry': 'a', 
        'embarrassed': 'e', 
        'playful': 'p', 
        'confident': 'c', 
        'loved': 'l',
        'remove': 'r'
    }
    for item in keypress:
        keyboard.send('r')
        print("emotion removed")
        time.sleep(0.5)
        keyboard.send('h')
        
        print("emotion added")
        time.sleep(3)rh

test_emotions()