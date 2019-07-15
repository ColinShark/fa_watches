from time import sleep
from math import ceil

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class FaTransfer:
    """Initialize the Transfer of Watches from the old account to the new one.

    Parameters
    ==========

    `old_user` (`str`):
        The Username of the old Account

    `username` (`str`):
        The Username of the new account. You log in with this.

    `password` (`str`):
        The Password of the new account. You log in with this.
    """
    def __init__(self,
                 old_user: str = None,
                 username: str = None,
                 password: str = None):
        self.old_user = old_user or input("Your old username? ")
        self.username = username or input("Your new username? ")
        self.password = password or input("Your password? ")
        self.driver = webdriver.Firefox()

    def login(self):
        driver = self.driver
        driver.get('https://furaffinity.net/login/')
        sleep(1)
        driver.find_element_by_name('name').send_keys(self.username)
        driver.find_element_by_id('captcha-switch').click()
        driver.find_element_by_name('pass').send_keys(self.password)

        WebDriverWait(driver, 30).until(
            lambda driver: driver.find_element_by_id('my-username'),
            message="Password not entered in time.")

    def get_watches(self):
        driver = self.driver
        driver.get('https://furaffinity.net/user/' + self.old_user)
        watch_link = driver.find_elements_by_partial_link_text('Full List')[1]
        watches = int(''.join([i for i in watch_link if i.isdigit()]))
        pages = ceil(watches/200)

        for page in range(pages):
            driver.get(f'https://furaffinity.net/watchlist/by/{self.old_user}/{page+1}')
            sleep(1)
            for artist in driver.find_elements_by_class_name('artist_name'):
                driver.get('https://furaffinity.net/user/' + artist)
                try:
                    driver.find_element_by_link_text('+Watch').click()
                except NoSuchElementException:
                    pass
                sleep(1)


# Enter your Login Credentials on the line below. An Example would be:
# fa = FaTransfer('old_username', 'new_user', 'password1')
fa = FaTransfer()
fa.login()
fa.get_watches()
