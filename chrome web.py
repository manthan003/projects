from selenium import webdriver
import time
import random
driver = webdriver.Chrome('C:\Users\crman\Downloads\chromedriver_win32\\chromedriver.exe')  

videos=[
    
    'https://www.youtube.com/watch?v=e_04ZrNroTo&t=120s'
    'https://www.youtube.com/watch?v=hq3yfQnllfQ'
    'https://www.youtube.com/watch?v=nyY0xIz6u8Y'
]

for i in range(10):
    print('running the video for {} times'.format(i))
    random_video=random.randint(0,2)
    driver.get(videos(random_video))
    sleep_time=random.randint(10,20)
    time.sleep(sleep_time)
