import unittest

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MembermanagerTest(unittest.TestCase):
    #变量前面加上self.表示这个变量是类的属性，可以被所有的方法访问
    def setUp(self):
        #打开浏览器
        #driver声明在setUp方法之内，不能被其他方法访问
        self.driver =webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
    def tearDown(self):
        #quit()退出浏览器
        #close()关闭一个浏览器标签
        #代码编写和调试的时候需要在quit()方法前加一个时间等待，清楚运行过程
        #正式运行的时候去掉时间等待，为了提高程序执行速度
        time.sleep(20)
        self.driver.quit()
    def test_add_member(self):
        #self.driver.get("http://localhost/index.php?m=admin&c=index&a=index&pid=4#")
        driver=self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_class_name("Btn").submit()
        driver.find_element_by_link_text("会员管理").click()
        #driver.find_element_by_link_text("添加会员").click()
        time.sleep(2)
        driver.switch_to.frame("mainFrame")
        #添加会员
        # driver.find_element_by_xpath('//*[@id="addrow"]/span/span[1]').click()
        # driver.find_element_by_name("username").send_keys("lxq2")
        # driver.find_element_by_name("mobile_phone").send_keys("18714785238")
        # driver.find_element_by_css_selector('[value="1"]').click()
        # driver.find_element_by_name("birthday").send_keys("1990-03-12")
        # driver.find_element_by_name("email").send_keys("742303876@qq.com")
        # driver.find_element_by_name("qq").send_keys("742303876")
        # driver.find_element_by_class_name("button_search").click()
        # time.sleep(2)
        #driver.switch_to_alert().accept()
        #删除会员??
        driver.find_element_by_css_selector('[value="29"]').click()
        driver.find_element_by_xpath('//*[@id="delrows"]/span/span[1]').click()
        time.sleep(2)
       # driver.find_element_by_xpath('//*[@class="messager-button"]/a[1]').click()
       # 移动滚动条
       #  ac = ActionChains(driver)
       #  for i in range(10):
       #      ac.send_keys(Keys.ARROW_RIGHT)
       #  ac.perform()
        driver.find_element_by_link_text("删除").click()
        time.sleep(2)
        #driver.switch_to_alert().accept()



