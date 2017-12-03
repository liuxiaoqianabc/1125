from selenium import webdriver
import unittest
# 1.导入ddt代码库
import ddt
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from day4.readCsv2 import read


# 1.导入ddt装饰器

# 2.装饰这个类


@ddt.ddt
class MemberManagerTest(unittest.TestCase):
    # 3.调用之前写好的read()方法，获取配置中的数据
    member_info = read("member_info.csv")

    # print(member_info)#可以读取csv文件的数据
    @classmethod
    # 定义一个方法
    def setUpClass(cls):
        print("在执行所有方法前先执行一次")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.quit()

    def test_a_log_in(self):
        print("登录测试")
        driver = self.driver
        driver.get("http://localhost/admin.php")
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB). \
            send_keys("1234").send_keys(Keys.ENTER).perform()

    @ddt.data(*member_info)
    def test_b_add_member(self, row):
        #data_table = read("member_info.csv")
        #for row in read("member_info.csv"):
        driver = self.driver
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        driver.switch_to.frame("mainFrame")
        # iframe_css = "#mainFrame"
        # iframe_html = driver.find_element_by_css_selector(iframe_css)
        # driver.switch_to.frame(iframe_html)
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        driver.find_element_by_css_selector('[value="{0}"]'.format(row[2])).click()
        driver.find_element_by_id("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").click()
        actual = driver.find_element_by_css_selector("#datagrid-row-r1-2-0 > td:nth-child(1) > div").text
        excepted = row[0]
        # if (actual == excepted):
        #     print("测试通过")
        # else:
        #     print("测试失败")
        self.assertEqual(actual, excepted)
        # driver.switch_to.parent_frame()
        driver.switch_to.default_content()
        # 当程序不稳定的时候加入时间等待即可解决
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
