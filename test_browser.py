from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_WeChat:
    def setup(self):
        '''
        浏览器复用
        '''
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_args)

    # def teardown(self):
    #     self.driver.quit()

    def test_cust_contact(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element(By.LINK_TEXT, '客户联系').click()


