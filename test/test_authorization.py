# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class MoreTV(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_more_t_v(self):
        wd = self.wd
        wd.get("https://beta.more.tv/")
        wd.find_element_by_link_text(u"войти").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("more")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("more3qabd+beta@yandex.ru")
        wd.find_element_by_xpath("//div[@id='blackout-container']/div/div/div").click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("1217470")
        wd.find_element_by_xpath("//button[@type='submit']").click()
        wd.find_element_by_xpath("//img[@alt='arrow']").click()
        wd.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/section/div/div[2]/div[2]/div/div[4]/div[2]/div/div/div").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
