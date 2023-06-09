#file for the roots

from flask import Blueprint, render_template
from flask import request

from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

count = 0
iterr = 0


myviews = Blueprint(__name__, "views")

@myviews.route("/", methods=['GET','POST'])
def getData():
    if request.method == 'POST':  # run code and display output

        username = request.form["username"]
        password = request.form["password"]
        folowers = int(request.form["folowers"])
        folowing = int(request.form["folowing"])



        



        #username = "not_a_l_a_n"
        #password = "freakz"

        nonfollowers = []

        def login(driver):
            driver.find_element("name", "username").send_keys(username)
            driver.find_element("name", "password").send_keys(password)
            driver.find_element("name", "password").send_keys("\ue007")

        def click_button_with_css(driver, css_selector):
            element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
            )
            element.click()

        def navigate_to_profile(driver):
            dropdown_css = '[alt*="' + username + '"]'
            profile_css = '[href*="' + username + '"]'
            click_button_with_css(driver, dropdown_css)
            click_button_with_css(driver, profile_css)

        def get_usernames_from_dialog(driver, n):
            list_xpath = "//div[@role='dialog']//li"
            xpath_name = '//div[@class="_aano"]/*[1]'
            list_elems = []

            time.sleep(4)

            #ADJUST n if needed
            #n = 50 works for about 500 followers/following
            n = n/10
            while (n > 0):
                scroll_down(driver)
                time.sleep(2)
                n = n - 1

            # ancestor div that contains the names is the first child of div with class _aano
            parent_div = driver.find_element("xpath", xpath_name)

            # get all the child div elements of the parent div into a list
            child_divs = parent_div.find_elements("xpath", ".//div")

            # iterate through the child divs to extract the names
            for div in child_divs:
                name = div.text
                name = name.replace("\nVerified", "")
                names_to_ignore = ["", "·", "Follow",
                                "Remove", "Verified", "Following"]
                if "\n" not in name:
                    if name not in names_to_ignore:
                        list_elems.append(name)

            list_elems = list(set(list_elems))

            return list_elems

        def scroll_down(driver):
            global count
            global iterr
            while 1:
                scroll_top_num = str(iterr * 1000)
                iterr += 1
                driver.execute_script(
                    "document.querySelector('div[class=_aano]').scrollTop=" +
                    scroll_top_num
                )
                try:
                    WebDriverWait(driver, 1).until(check_difference_in_count)
                except:
                    count = 0
                    break
            return

        def check_difference_in_count(driver):
            global count
            new_count = len(driver.find_elements("xpath", "//div[@role='dialog']"))
            if count != new_count:
                count = new_count
                return True
            else:
                return False


        #    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge()
        driver.get("https://www.instagram.com/accounts/login")
        time.sleep(2)

        login(driver)
        time.sleep(5)
        navigate_to_profile(driver)
        time.sleep(2)

        followers_css = '[href*="' + username + '/followers/"]'
        css_select_close = '[aria-label="Close"]'
        following_css = '[href*="' + username + '/following/"]'

        click_button_with_css(driver, followers_css)
        followers_list = get_usernames_from_dialog(driver, folowers)
        #print("---------------------------------------")
        #print("FOLLOWERS LIST: ", len(followers_list))
        #print(followers_list)

        time.sleep(2)
        click_button_with_css(driver, css_select_close)
        time.sleep(2)

        click_button_with_css(driver, following_css)
        following_list = get_usernames_from_dialog(driver, folowing)
        #print("---------------------------------------")
        #print("FOLLOWING LIST: ", len(following_list))
        #print(following_list)

        #print("---------------------------------------")
        #print("PEOPLE YOU FOLLOW BUT DO NOT FOLLOW YOU BACK:")
        for name in following_list:
            if name not in followers_list:
                #print(name)
                nonfollowers.append(name)

        time.sleep(20)
        driver.quit()





        
        return render_template("index.html", nonfollowers = nonfollowers)
    else:
        return render_template("index.html")
