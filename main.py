from selenium import webdriver
from time import sleep
from getpass import getpass

# Username and password
username = input("Username: ")
password = getpass("Password: ")

# Path to WebDriver
webdriver_path = ""

# Find the ChromeDriver
driver = webdriver.Chrome(executable_path=webdriver_path)

# Fetch instagram
driver.get("https://www.instagram.com/")

# Wait till the page loads
sleep(4)

# Accept the cookies
driver.find_element_by_xpath("//button[text()='Accept']")\
    .click()

# Find username input and fill it
driver.find_element_by_xpath("//input[@name='username']")\
    .send_keys(username)

# Find password input and fill it
driver.find_element_by_xpath("//input[@name='password']")\
    .send_keys(password)

# Submit the login form
driver.find_element_by_xpath("//button[@type='submit']")\
    .click()

# Wait till the page loads
sleep(4)

# Go to profile page
driver.get("https://www.instagram.com/" + username)
sleep(2)

# Open followers modal
driver.find_element_by_partial_link_text("followers")\
    .click()
sleep(2)

# Fetch follower container and scroll to bottom
# and place them in an array
follower_container = driver.find_element_by_class_name("isgrP")
driver.execute_script("arguments[0].scrollIntoView()", follower_container)
sleep(1)
last_ht, ht = 0, 1
while last_ht != ht:
    last_ht = ht
    sleep(1)
    ht = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight);
        return arguments[0].scrollHeight;
        """, follower_container)
links = follower_container.find_elements_by_tag_name("a")
followers = [follower.text for follower in links if follower.text != ""]
driver.find_element_by_css_selector("[aria-label='Close']")\
    .click()

# Wait inbetween modals
sleep(2)

# Open following modal
driver.find_element_by_partial_link_text("following")\
    .click()
sleep(2)

# Fetch people you follow container and scroll to bottom
# and place them in an array
following_container = driver.find_element_by_class_name("isgrP")
driver.execute_script("arguments[0].scrollIntoView()", following_container)
sleep(1)
last_ht, ht = 0, 1
while last_ht != ht:
    last_ht = ht
    sleep(1)
    ht = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight);
        return arguments[0].scrollHeight;
        """, following_container)
links = following_container.find_elements_by_tag_name("a")
followings = [following.text for following in links if following.text != ""]
driver.find_element_by_css_selector("[aria-label='Close']")\
    .click()

# Checking which users are not following back by iterating
# over both arrays and checking who's not in followers
not_followings = [user for user in followings if user not in followers]
for not_following in not_followings:
    print(not_following.center(30, " "))