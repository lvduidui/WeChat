import json

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_WeChat:
    def setup(self):
        self.driver = webdriver.Chrome()

    # def test_cookie(self):
    #     # 获取cookie
    #     # cookies = self.driver.get_cookies()
    #     # with open('cookie.josn', 'w') as f:
    #     #     json.dump(cookies, f)



    def test_cust_contact(self):
        self.driver.get('https://work.weixin.qq.com')

        with open('cookie.josn', 'r') as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element(By.LINK_TEXT, '客户联系').click()

