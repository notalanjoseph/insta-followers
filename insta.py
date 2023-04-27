from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

count = 0
username = 'not_a_l_a_n'
password = ''

def login(driver):
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("name", "password").send_keys(u'\ue007')
    
def click_button_with_css(driver, css_selector):
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    element.click()
    
def navigate_to_followers(driver):
    dropdown_css = '[alt*="' + username + '"]'
    profile_css = "[href*=\"" + username + "\"]"
    click_button_with_css(driver, dropdown_css)
    click_button_with_css(driver, profile_css)
    
    
def get_usernames_from_dialog(driver):
    list_xpath ="//div[@role='dialog']//li"
    
    
 #   try:
    WebDriverWait(driver, 20).until(
            #EC.presence_of_element_located((By.XPATH, list_xpath)))
       driver.find_element(By.XPATH, list_xpath)) #SO
#    except:
#        print("wait error")
    
    try:
        scroll_down(driver)
    except:
        print("scroll error")
    
    try:
        list_elems = driver.find_element("xpath", list_xpath)
    except:
        print("list error")
    
    users = []
    for i in range(len(list_elems)):
        try:
            row_text = list_elems[i].text
            if "Follow" in row_text or "Remove" in row_text:
                username = row_text[:row_text.index("\n")]
                users += [username]
        except:
            print("continue")
            
    return users     

            
def scroll_down(driver):
    global count
    iter = 0
    while 1:
        scroll_top_num = str(iter * 1000)
        iter +=1
        driver.execute_script("document.querySelector('div[role=dialog] ul').parentNode.scrollTop=" + scroll_top_num)
        
        try:
            WebDriverWait(driver, 1).until(check_difference_in_count)
        except:
            count = 0
            break
    return

def check_difference_in_count(driver):
    global count
    new_count = len(driver.find_element("xpath", "//div[@role='dialog']//li"))
    if count != new_count:
        count = new_count
        return True
    else:
        return False
    
    
def no_followback(followers, following):
    followers.sort()
    following.sort()
    no_followback_list = []
    for i in range(len(following)):
        try:
            followers.index(following[i])
        except ValueError:
            no_followback_list += [following[i]]
    return no_followback_list



def __main__():
#    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge()
    driver.get('https://www.instagram.com/accounts/login')
    time.sleep(2)
    
    login(driver)
    navigate_to_followers(driver)
    
    
    followers_css = "[href*=\"" + username + "/followers/\"]"
    css_select_close = '[aria-label="Close"]'
    following_css = "[href*=\"" + username + "/following/\"]"
    
    click_button_with_css(driver, followers_css)
    followers_list = get_usernames_from_dialog(driver)
    
    click_button_with_css(driver, css_select_close)
    time.sleep(2)
    
    click_button_with_css(driver, following_css)
    following_list = get_usernames_from_dialog(driver)
    
    
    no_followbacks = no_followback(followers_list, following_list)
    for i in range(len(unfollow_list)):
        print (no_followbacks[i])
    
    
    
    
    
    time.sleep(100)
    
    
    driver.quit()
    
    

  
    
__main__() 
