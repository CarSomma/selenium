from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TWITTER_URL = "https://twitter.com"
search_str = "SPICEDAcademy"

# Start the session
browser = webdriver.Chrome()

# Take actions on a browser:
## Navigating to a specific url
browser.get(TWITTER_URL)

# Define a wait object 
# to use in combination of a certain condition
wait = WebDriverWait(browser,50)

# Find an element:
## Search box
search_box = wait.until(
    EC.visibility_of_element_located((By.TAG_NAME , "input")))

# Take actions on an element:
## Enter SPICEDAcademy text into the search box 
search_box.send_keys(search_str)

## Perform "ENTER" keyboard action
search_box.send_keys(Keys.ENTER)

# Close annoying pop-up windows:

not_now_button = wait.until(
    EC.visibility_of_element_located(
    (By.XPATH , '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div')
    )).click()

# Get text of HTML elements:

top_tweet = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[1]/div/div/article')
    )).text

print(top_tweet)

# Close the session

browser.quit()

