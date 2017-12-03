#有了myTestCase以后，再写测试用例就不需要重新写setUp和tearDown方法
import os

from selenium import webdriver

from day5.myTestCase import MyTestCase


class ZhuCeTest(MyTestCase):
    #3个双引号，表示文档字符串，也是一种注释，和#号的区别是这种注释会显示在文档中
    """注册模块测试用例"""
    #因为myTestCase已经实现了setUp和tearDown方法，我们以后在写测试就
# 不需要重新实现setUp和tearDown方法
    def test_zhu_ce(self):
        """打开注册页面的测试用例"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        #driver.current_url#用来获取当前浏览器中的网址
        actual = driver.title#用来获取当前浏览器中的标签页的title
        excepted = "用户注册 - 道e坊商城 - Powered by Haidao111"
        #driver.get_screenshot_as_png("zhuce")
        #get_screenshot_as_file截取整个浏览器的图片
        base_path = os.path.dirname(__file__)
        path = base_path.replace('day5', 'report/image/')
        #driver.get_screenshot_as_file("zhuce.png")绝对路径
        driver.get_screenshot_as_file(path + "zhuce.png")#相对路径
        self.assertEqual(actual, excepted)
